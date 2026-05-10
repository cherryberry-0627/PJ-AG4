"""
重构3：
将SettlementRow类移入contracts模块。
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AgentAction:
    forecast_demand: int
    price: float
    quantity: int


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
    forecast_demand: int
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
    reputation_end: float


@dataclass(frozen=True)
class SimulationResult:
    rows: list[object]
    csv_path: Path
    figure_path: Path | None
    dashboard_path: Path | None = None
    report_path: Path | None = None
