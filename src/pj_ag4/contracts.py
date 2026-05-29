"""
重构3：
将SettlementRow类移入contracts模块。
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class DecisionTrace:
    source: str
    summary: str
    forecast_base: float = 0.0
    forecast_adjustment: float = 0.0
    price_base: float = 0.0
    price_adjustment: float = 0.0
    quantity_target: float = 0.0
    risk_gate_adjustment: str = "none"
    final_forecast: int = 0
    final_price: float = 0.0
    final_quantity: int = 0
    fallback_used: bool = False
    llm_status: str = ""
    llm_error: str = ""
    llm_prompt_excerpt: str = ""

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False, separators=(",", ":"))

    @classmethod
    def from_json(cls, value: str | None) -> "DecisionTrace | None":
        if not value:
            return None
        try:
            payload = json.loads(value)
        except json.JSONDecodeError:
            return None
        if not isinstance(payload, dict):
            return None
        return cls(**{key: payload.get(key) for key in cls.__dataclass_fields__})

    def to_public_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class AgentAction:
    forecast_demand: int
    price: float
    quantity: int
    trace: DecisionTrace | None = None


@dataclass(frozen=True)
class MarketObservation:
    round_index: int
    observed_demand: int
    demand_history: tuple[int, ...]
    observed_demand_history: tuple[int, ...]
    price_history: tuple[tuple[float, ...], ...]
    reputation_history: tuple[tuple[float, ...], ...]
    peer_reputations: tuple[tuple[str, float], ...]
    own_inventory: float
    own_last_profit: float
    own_last_shortage: float
    own_reputation: float
    market_avg_price: float
    market_volatility: float


@dataclass(frozen=True)
class SettlementRow:
    """单回合、单agent的完整字段记录"""
    seed: int
    round: int
    agent_name: str
    agent_role: str
    agent_action: str
    decision_source: str
    decision_reason: str
    decision_trace: str
    forecast_demand: int
    forecast_error_abs: float
    forecast_error_sq: float
    demand_true: int
    demand_obs: int
    trend_component: float
    season_component: float
    shock_component: float
    noise_component: float
    market_avg_price: float
    market_total_sales: float
    inventory_start: float
    reputation_start: float
    rep_delivery_start: float
    rep_pricing_start: float
    rep_cooperation_start: float
    price: float
    quantity: int
    available_supply: float
    attractiveness: float
    demand_share: float
    allocated_demand: float
    shortage_pre_transfer: float
    surplus_pre_transfer: float
    transfer_in: float
    transfer_out: float
    transfer_cost: float
    transfer_revenue: float
    transfer_attempts: int
    transfer_accepts: int
    coop_probability: float
    coop_accept_rate: float
    realized_sales: float
    shortage_post_transfer: float
    inventory_end: float
    obsolescence_units: float
    revenue: float
    prod_cost: float
    holding_cost: float
    obsolescence_cost: float
    sla_penalty: float
    menu_cost: float
    profit: float
    cum_profit: float
    service_rate: float
    help_ratio: float
    dump_flag: int
    default_flag: int
    rep_delivery_end: float
    rep_pricing_end: float
    rep_cooperation_end: float
    reputation_end: float


@dataclass(frozen=True)
class RoundTrace:
    round_index: int
    demand_true: float
    demand_observed: float
    market_total_sales: float
    market_avg_price: float
    transfer_volume: float
    default_count: int
    dump_count: int
    summary: str

    def to_public_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class SimulationResult:
    rows: list[object]
    csv_path: Path
    figure_path: Path | None
    dashboard_path: Path | None = None
    report_path: Path | None = None
