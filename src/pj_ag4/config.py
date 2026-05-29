from __future__ import annotations

from dataclasses import dataclass, field
import json
import os
from pathlib import Path
from typing import Sequence

from dotenv import find_dotenv, load_dotenv

# 默认内置JSON文档路径
_DEFAULT_AGENTS_FILE = Path(__file__).resolve().parent / "data" / "agents.json"


def _load_runtime_env() -> None:
    dotenv_path = find_dotenv(usecwd=True)
    if dotenv_path:
        load_dotenv(dotenv_path=dotenv_path, override=False)
        return
    repo_root_env = Path(__file__).resolve().parents[2] / ".env"
    if repo_root_env.exists():
        load_dotenv(dotenv_path=repo_root_env, override=False)


@dataclass(frozen=True)
class MarketConfig:
    demand_base: float = 180.0
    demand_growth: float = 0.6
    seasonal_amplitude_7: float = 18.0
    seasonal_amplitude_30: float = 10.0
    seasonal_phase: float = 0.3
    shock_round: int = 35
    shock_magnitude: float = -20.0
    ar_rho: float = 0.45
    ar_sigma: float = 7.0
    observation_noise_sigma: float = 5.0
    demand_floor: int = 50
    reputation_weight: float = 1.2
    reputation_delivery_weight: float = 0.5
    reputation_pricing_weight: float = 0.3
    reputation_cooperation_weight: float = 0.2
    price_weight: float = 0.7
    cooperation_alpha0: float = -0.8
    cooperation_alpha1: float = 2.5
    cooperation_alpha2: float = 1.2
    cooperation_alpha3: float = 1.5
    indirect_reciprocity_alpha: float = 0.1
    transfer_markup: float = 0.05
    max_transfer: float = 15.0
    reputation_update_rate: float = 0.25
    demand_window: int = 5


@dataclass(frozen=True)
class AgentConfig:
    name: str
    role: str
    persona: str
    forecaster_style: str
    pricer_style: str
    allocator_style: str
    risk_style: str
    base_price: float
    price_floor: float
    price_ceiling: float
    price_step: float
    quantity_step: int
    max_quantity: int
    inventory_start: float
    reputation_start: float
    brand_strength: float
    linear_cost: float
    quadratic_cost: float
    holding_cost_rate: float
    obsolescence_rate: float
    obsolescence_penalty: float
    sla_penalty: float
    menu_cost_rate: float


@dataclass(frozen=True)
class LLMConfig:
    base_url: str = "http://127.0.0.1:8045/v1"
    api_key: str | None = None
    model: str = "gemini-3-flash"
    temperature: float = 0.0
    max_tokens: int = 512
    max_retries: int = 1
    timeout_seconds: float = 30.0


@dataclass(frozen=True)
class SimulationConfig:
    seed: int = 7
    rounds: int = 30
    output_dir: Path = Path("outputs")
    agent_mode: str = "heuristic"
    market: MarketConfig = field(default_factory=MarketConfig)
    llm: LLMConfig | None = None
    agents: tuple[AgentConfig, ...] = field(default_factory=tuple)




def load_agent_configs(
    profile: str = "default",
    *,
    source: str | Path | None = None,
) -> tuple[AgentConfig, ...]:
    """重构1：去除原有default_simulation_config里的agent config构造，
    将agent配置独立为一个JSON文档进行加载
    并新增读取JSON文件的API。
    
    暂时保持原有的函数式编程和annotations风格

    参数:
        profile: 要加载的agent配置集的名称，默认为"default"
        source: JSON文件路径，None时使用默认内置JSON文档
    """
    path = Path(source) if source is not None else _DEFAULT_AGENTS_FILE
    with path.open("r", encoding="utf-8") as fh:
        data = json.load(fh)
    profile_data = data.get("profiles", {}).get(profile)
    if profile_data is None:
        known = ", ".join(sorted(data.get("profiles", {})))
        raise ValueError(
            f"unknown agent profile {profile!r}; "
            f"available profiles: {known or '(none)'}"
        )
    return tuple(AgentConfig(**entry) for entry in profile_data)


def default_simulation_config(
    *,
    seed: int = 7,
    rounds: int = 30,
    output_dir: str | Path = "outputs",
    agent_mode: str = "heuristic",
    llm_base_url: str | None = None,
    llm_api_key: str | None = None,
    llm_model: str | None = None,
    agents_profile: str = "default",
    agents_file: str | Path | None = None,
) -> SimulationConfig:
    _load_runtime_env()
    agents = load_agent_configs(agents_profile, source=agents_file)
    resolved_llm_api_key = llm_api_key or os.getenv("PJ_AG4_OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
    llm_config = LLMConfig(
        base_url=llm_base_url or os.getenv("PJ_AG4_OPENAI_BASE_URL") or "http://127.0.0.1:8045/v1",
        api_key=resolved_llm_api_key,
        model=llm_model or os.getenv("PJ_AG4_OPENAI_MODEL") or "gemini-3-flash",
    )
    return SimulationConfig(
        seed=seed,
        rounds=rounds,
        output_dir=Path(output_dir),
        agent_mode=agent_mode,
        llm=llm_config,
        agents=agents,
    )
