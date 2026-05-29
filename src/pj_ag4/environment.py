"""
重构3：
拆分environment模块中的数据模型储存职责与io职责
"""

from __future__ import annotations

from dataclasses import dataclass
import random
from statistics import median

from .config import AgentConfig, MarketConfig, SimulationConfig
from .contracts import AgentAction, SettlementRow
from .timeseries import DemandSnapshot
from .utils import clamp, sigmoid, stable_softmax


@dataclass
class AgentState:
    inventory: float
    rep_delivery: float
    rep_pricing: float
    rep_cooperation: float
    reputation_delivery_weight: float
    reputation_pricing_weight: float
    reputation_cooperation_weight: float
    cumulative_profit: float = 0.0
    last_profit: float = 0.0
    last_shortage: float = 0.0
    last_price: float = 0.0
    last_dump_flag: bool = False

    @property
    def reputation(self) -> float:
        return _weighted_reputation_values(
            delivery=self.rep_delivery,
            pricing=self.rep_pricing,
            cooperation=self.rep_cooperation,
            delivery_weight=self.reputation_delivery_weight,
            pricing_weight=self.reputation_pricing_weight,
            cooperation_weight=self.reputation_cooperation_weight,
        )


def _weighted_reputation_values(
    *,
    delivery: float,
    pricing: float,
    cooperation: float,
    delivery_weight: float,
    pricing_weight: float,
    cooperation_weight: float,
) -> float:
    total_weight = delivery_weight + pricing_weight + cooperation_weight
    if total_weight <= 0:
        return 0.0
    return clamp(
        (
            delivery_weight * delivery
            + pricing_weight * pricing
            + cooperation_weight * cooperation
        )
        / total_weight,
        0.0,
        1.0,
    )


def _weighted_reputation(
    *,
    delivery: float,
    pricing: float,
    cooperation: float,
    market: MarketConfig,
) -> float:
    return _weighted_reputation_values(
        delivery=delivery,
        pricing=pricing,
        cooperation=cooperation,
        delivery_weight=market.reputation_delivery_weight,
        pricing_weight=market.reputation_pricing_weight,
        cooperation_weight=market.reputation_cooperation_weight,
    )


class MarketEnvironment:
    def __init__(self, config: SimulationConfig) -> None:
        self.config = config
        self.market = config.market
        self._rng = random.Random(config.seed + 1009)
        self.agent_configs = {agent.name: agent for agent in config.agents}
        self.states = {
            agent.name: AgentState(
                inventory=agent.inventory_start,
                rep_delivery=agent.reputation_start,
                rep_pricing=agent.reputation_start,
                rep_cooperation=agent.reputation_start,
                reputation_delivery_weight=self.market.reputation_delivery_weight,
                reputation_pricing_weight=self.market.reputation_pricing_weight,
                reputation_cooperation_weight=self.market.reputation_cooperation_weight,
                last_price=agent.base_price,
            )
            for agent in config.agents
        }

    def reputation_for(self, agent_name: str) -> float:
        state = self.states[agent_name]
        return _weighted_reputation(
            delivery=state.rep_delivery,
            pricing=state.rep_pricing,
            cooperation=state.rep_cooperation,
            market=self.market,
        )

    def current_reputations(self) -> dict[str, float]:
        return {name: self.reputation_for(name) for name in self.agent_configs}

    def validate_action(self, agent_name: str, action: AgentAction) -> AgentAction:
        agent_cfg = self.agent_configs[agent_name]
        price = clamp(float(action.price), agent_cfg.price_floor, agent_cfg.price_ceiling)
        quantity = int(round(float(action.quantity) / agent_cfg.quantity_step) * agent_cfg.quantity_step)
        quantity = int(clamp(quantity, 0, agent_cfg.max_quantity))
        forecast = max(0, int(round(float(action.forecast_demand))))
        return AgentAction(
            forecast_demand=forecast,
            price=price,
            quantity=quantity,
            trace=action.trace,
            strategy_state=action.strategy_state,
            strategy_update_trace=action.strategy_update_trace,
        )

    def validate_actions(self, actions: dict[str, AgentAction]) -> dict[str, AgentAction]:
        return {
            name: self.validate_action(name, actions[name])
            for name in self.agent_configs
        }

    def step(
        self,
        *,
        seed: int,
        round_index: int,
        snapshot: DemandSnapshot,
        actions: dict[str, AgentAction],
    ) -> list[SettlementRow]:
        ordered_names = list(self.agent_configs.keys())
        actions = self.validate_actions(actions)
        supply_start: dict[str, float] = {}
        attractiveness: dict[str, float] = {}
        demand_share: dict[str, float] = {}
        allocated_demand: dict[str, float] = {}
        shortage_pre: dict[str, float] = {}
        surplus_pre: dict[str, float] = {}
        transfer_in: dict[str, float] = {name: 0.0 for name in ordered_names}
        transfer_out: dict[str, float] = {name: 0.0 for name in ordered_names}
        transfer_cost: dict[str, float] = {name: 0.0 for name in ordered_names}
        transfer_revenue: dict[str, float] = {name: 0.0 for name in ordered_names}
        transfer_accepts: dict[str, int] = {name: 0 for name in ordered_names}
        transfer_attempts: dict[str, int] = {name: 0 for name in ordered_names}
        transfer_probability_sum: dict[str, float] = {name: 0.0 for name in ordered_names}

        reputation_start = {name: self.reputation_for(name) for name in ordered_names}
        prices = [actions[name].price for name in ordered_names]
        price_softmax = stable_softmax([
            self.agent_configs[name].brand_strength + self.market.reputation_weight * reputation_start[name] - self.market.price_weight * actions[name].price
            for name in ordered_names
        ])

        for idx, name in enumerate(ordered_names):
            agent_cfg = self.agent_configs[name]
            action = actions[name]
            state = self.states[name]
            supply_start[name] = state.inventory + action.quantity
            attractiveness[name] = (
                agent_cfg.brand_strength
                + self.market.reputation_weight * reputation_start[name]
                - self.market.price_weight * action.price
            )
            demand_share[name] = price_softmax[idx]
            allocated_demand[name] = snapshot.true_demand * demand_share[name]
            shortage_pre[name] = max(0.0, allocated_demand[name] - supply_start[name])
            surplus_pre[name] = max(0.0, supply_start[name] - allocated_demand[name])

        shortage_remaining = shortage_pre.copy()
        surplus_remaining = surplus_pre.copy()
        provider_order = sorted(
            ordered_names,
            key=lambda item: surplus_remaining[item],
            reverse=True,
        )
        shortage_order = sorted(
            ordered_names,
            key=lambda item: shortage_remaining[item],
            reverse=True,
        )
        refused_help: dict[str, int] = {name: 0 for name in ordered_names}

        for shortage_name in shortage_order:
            if shortage_remaining[shortage_name] <= 0:
                continue
            shortage_state = self.states[shortage_name]
            for provider_name in provider_order:
                if provider_name == shortage_name or shortage_remaining[shortage_name] <= 0:
                    continue
                if surplus_remaining[provider_name] <= 0:
                    continue
                provider_action = actions[provider_name]
                transfer_attempts[provider_name] += 1
                willingness = sigmoid(
                    self.market.cooperation_alpha0
                    + self.market.cooperation_alpha1 * shortage_state.rep_cooperation
                    - self.market.cooperation_alpha2 * (allocated_demand[provider_name] / (supply_start[provider_name] + 1.0))
                    - self.market.cooperation_alpha3 * (1.0 if shortage_state.last_dump_flag else 0.0)
                )
                transfer_probability_sum[provider_name] += willingness
                accepted = self._rng.random() < willingness
                transfer_accepts[provider_name] += 1 if accepted else 0
                if not accepted:
                    refused_help[provider_name] += 1
                    continue
                amount = min(
                    surplus_remaining[provider_name],
                    shortage_remaining[shortage_name],
                    self.market.max_transfer,
                )
                if amount <= 0:
                    continue
                transfer_in[shortage_name] += amount
                transfer_out[provider_name] += amount
                surplus_remaining[provider_name] -= amount
                shortage_remaining[shortage_name] -= amount
                provider_price = provider_action.price
                buyer_price = provider_price * (1.0 + self.market.transfer_markup)
                transfer_cost[shortage_name] += amount * buyer_price
                transfer_revenue[provider_name] += amount * buyer_price

        row_payloads: dict[str, dict[str, float | int | str]] = {}
        for name in ordered_names:
            state = self.states[name]
            agent_cfg = self.agent_configs[name]
            action = actions[name]
            rep_delivery_start = state.rep_delivery
            rep_pricing_start = state.rep_pricing
            rep_cooperation_start = state.rep_cooperation
            total_supply = supply_start[name] + transfer_in[name] - transfer_out[name]
            realized_sales = min(total_supply, allocated_demand[name])
            shortage_post = max(0.0, allocated_demand[name] - total_supply)
            inventory_end = max(0.0, total_supply - realized_sales)
            obsolescence_units = agent_cfg.obsolescence_rate * inventory_end
            next_inventory = max(0.0, inventory_end - obsolescence_units)
            revenue = realized_sales * action.price
            prod_cost = action.quantity * agent_cfg.linear_cost + 0.5 * (action.quantity**2) * agent_cfg.quadratic_cost
            holding_cost = next_inventory * agent_cfg.holding_cost_rate
            obsolescence_cost = obsolescence_units * agent_cfg.obsolescence_penalty
            sla_penalty = shortage_post * agent_cfg.sla_penalty
            menu_cost = abs(action.price - state.last_price) * agent_cfg.menu_cost_rate
            profit = revenue + transfer_revenue[name] - transfer_cost[name] - prod_cost - holding_cost - obsolescence_cost - sla_penalty - menu_cost
            service_rate = 0.0 if allocated_demand[name] <= 0 else realized_sales / allocated_demand[name]
            help_ratio = 0.0 if surplus_pre[name] <= 0 else transfer_out[name] / surplus_pre[name]
            peer_prices = [price for idx, price in enumerate(prices) if ordered_names[idx] != name]
            peer_median = median(peer_prices) if peer_prices else action.price
            marginal_cost = agent_cfg.linear_cost + agent_cfg.quadratic_cost * max(1, action.quantity)
            dump_flag = int(action.price < marginal_cost and action.price < 0.85 * peer_median)
            default_flag = int(allocated_demand[name] > 0 and shortage_post / allocated_demand[name] > 0.1)
            delivery_score = clamp(service_rate - 0.5 * default_flag, 0.0, 1.0)
            pricing_score = 0.0 if dump_flag else 1.0
            if transfer_attempts[name] > 0:
                cooperation_score = clamp(
                    transfer_accepts[name] / transfer_attempts[name]
                    - self.market.indirect_reciprocity_alpha * refused_help[name],
                    0.0,
                    1.0,
                )
            else:
                cooperation_score = state.rep_cooperation
            rep_delivery_end = clamp(
                (1.0 - self.market.reputation_update_rate) * state.rep_delivery
                + self.market.reputation_update_rate * delivery_score,
                0.0,
                1.0,
            )
            rep_pricing_end = clamp(
                (1.0 - self.market.reputation_update_rate) * state.rep_pricing
                + self.market.reputation_update_rate * pricing_score,
                0.0,
                1.0,
            )
            rep_cooperation_end = clamp(
                (1.0 - self.market.reputation_update_rate) * state.rep_cooperation
                + self.market.reputation_update_rate * cooperation_score,
                0.0,
                1.0,
            )
            reputation_end = clamp(
                _weighted_reputation(
                    delivery=rep_delivery_end,
                    pricing=rep_pricing_end,
                    cooperation=rep_cooperation_end,
                    market=self.market,
                ),
                0.0,
                1.0,
            )

            state.inventory = next_inventory
            state.rep_delivery = rep_delivery_end
            state.rep_pricing = rep_pricing_end
            state.rep_cooperation = rep_cooperation_end
            state.cumulative_profit += profit
            state.last_profit = profit
            state.last_shortage = shortage_post
            state.last_price = action.price
            state.last_dump_flag = bool(dump_flag)
            decision_trace = action.trace
            strategy_update_trace = action.strategy_update_trace
            row_payloads[name] = {
                "forecast_demand": action.forecast_demand,
                "forecast_error_abs": abs(action.forecast_demand - snapshot.true_demand),
                "forecast_error_sq": (action.forecast_demand - snapshot.true_demand) ** 2,
                "agent_action": f"forecast={action.forecast_demand};price={action.price:.2f};quantity={action.quantity}",
                "decision_source": decision_trace.source if decision_trace is not None else "external",
                "decision_reason": decision_trace.summary if decision_trace is not None else "No structured decision trace was provided.",
                "decision_trace": decision_trace.to_json() if decision_trace is not None else "",
                "strategy_state": action.strategy_state.to_json() if action.strategy_state is not None else "",
                "strategy_update_reason": strategy_update_trace.reason if strategy_update_trace is not None else "",
                "strategy_update_trace": strategy_update_trace.to_json() if strategy_update_trace is not None else "",
                "demand_true": snapshot.true_demand,
                "demand_obs": snapshot.observed_demand,
                "trend_component": snapshot.trend_component,
                "season_component": snapshot.seasonal_component,
                "shock_component": snapshot.shock_component,
                "noise_component": snapshot.noise_component,
                "inventory_start": supply_start[name] - action.quantity,
                "reputation_start": reputation_start[name],
                "rep_delivery_start": rep_delivery_start,
                "rep_pricing_start": rep_pricing_start,
                "rep_cooperation_start": rep_cooperation_start,
                "price": action.price,
                "quantity": action.quantity,
                "available_supply": supply_start[name],
                "attractiveness": attractiveness[name],
                "demand_share": demand_share[name],
                "allocated_demand": allocated_demand[name],
                "shortage_pre_transfer": shortage_pre[name],
                "surplus_pre_transfer": surplus_pre[name],
                "transfer_in": transfer_in[name],
                "transfer_out": transfer_out[name],
                "transfer_cost": transfer_cost[name],
                "transfer_revenue": transfer_revenue[name],
                "transfer_attempts": transfer_attempts[name],
                "transfer_accepts": transfer_accepts[name],
                "coop_probability": 0.0 if transfer_attempts[name] <= 0 else transfer_probability_sum[name] / transfer_attempts[name],
                "coop_accept_rate": 0.0 if transfer_attempts[name] <= 0 else transfer_accepts[name] / transfer_attempts[name],
                "realized_sales": realized_sales,
                "shortage_post_transfer": shortage_post,
                "inventory_end": next_inventory,
                "obsolescence_units": obsolescence_units,
                "revenue": revenue,
                "prod_cost": prod_cost,
                "holding_cost": holding_cost,
                "obsolescence_cost": obsolescence_cost,
                "sla_penalty": sla_penalty,
                "menu_cost": menu_cost,
                "profit": profit,
                "cum_profit": state.cumulative_profit,
                "service_rate": service_rate,
                "help_ratio": help_ratio,
                "dump_flag": dump_flag,
                "default_flag": default_flag,
                "rep_delivery_end": rep_delivery_end,
                "rep_pricing_end": rep_pricing_end,
                "rep_cooperation_end": rep_cooperation_end,
                "reputation_end": reputation_end,
            }

        round_total_sales = sum(payload["realized_sales"] for payload in row_payloads.values())
        rows: list[SettlementRow] = []
        for name in ordered_names:
            payload = row_payloads[name]
            rows.append(
                SettlementRow(
                    seed=seed,
                    round=round_index,
                    agent_name=name,
                    agent_role=self.agent_configs[name].role,
                    agent_action=payload["agent_action"],
                    decision_source=str(payload["decision_source"]),
                    decision_reason=str(payload["decision_reason"]),
                    decision_trace=str(payload["decision_trace"]),
                    strategy_state=str(payload["strategy_state"]),
                    strategy_update_reason=str(payload["strategy_update_reason"]),
                    strategy_update_trace=str(payload["strategy_update_trace"]),
                    forecast_demand=int(payload["forecast_demand"]),
                    forecast_error_abs=float(payload["forecast_error_abs"]),
                    forecast_error_sq=float(payload["forecast_error_sq"]),
                    demand_true=int(payload["demand_true"]),
                    demand_obs=int(payload["demand_obs"]),
                    trend_component=float(payload["trend_component"]),
                    season_component=float(payload["season_component"]),
                    shock_component=float(payload["shock_component"]),
                    noise_component=float(payload["noise_component"]),
                    market_avg_price=sum(prices) / len(prices),
                    market_total_sales=round_total_sales,
                    inventory_start=float(payload["inventory_start"]),
                    reputation_start=float(payload["reputation_start"]),
                    rep_delivery_start=float(payload["rep_delivery_start"]),
                    rep_pricing_start=float(payload["rep_pricing_start"]),
                    rep_cooperation_start=float(payload["rep_cooperation_start"]),
                    price=float(payload["price"]),
                    quantity=int(payload["quantity"]),
                    available_supply=float(payload["available_supply"]),
                    attractiveness=float(payload["attractiveness"]),
                    demand_share=float(payload["demand_share"]),
                    allocated_demand=float(payload["allocated_demand"]),
                    shortage_pre_transfer=float(payload["shortage_pre_transfer"]),
                    surplus_pre_transfer=float(payload["surplus_pre_transfer"]),
                    transfer_in=float(payload["transfer_in"]),
                    transfer_out=float(payload["transfer_out"]),
                    transfer_cost=float(payload["transfer_cost"]),
                    transfer_revenue=float(payload["transfer_revenue"]),
                    transfer_attempts=int(payload["transfer_attempts"]),
                    transfer_accepts=int(payload["transfer_accepts"]),
                    coop_probability=float(payload["coop_probability"]),
                    coop_accept_rate=float(payload["coop_accept_rate"]),
                    realized_sales=float(payload["realized_sales"]),
                    shortage_post_transfer=float(payload["shortage_post_transfer"]),
                    inventory_end=float(payload["inventory_end"]),
                    obsolescence_units=float(payload["obsolescence_units"]),
                    revenue=float(payload["revenue"]),
                    prod_cost=float(payload["prod_cost"]),
                    holding_cost=float(payload["holding_cost"]),
                    obsolescence_cost=float(payload["obsolescence_cost"]),
                    sla_penalty=float(payload["sla_penalty"]),
                    menu_cost=float(payload["menu_cost"]),
                    profit=float(payload["profit"]),
                    cum_profit=float(payload["cum_profit"]),
                    service_rate=float(payload["service_rate"]),
                    help_ratio=float(payload["help_ratio"]),
                    dump_flag=int(payload["dump_flag"]),
                    default_flag=int(payload["default_flag"]),
                    rep_delivery_end=float(payload["rep_delivery_end"]),
                    rep_pricing_end=float(payload["rep_pricing_end"]),
                    rep_cooperation_end=float(payload["rep_cooperation_end"]),
                    reputation_end=float(payload["reputation_end"]),
                )
            )
        return rows
