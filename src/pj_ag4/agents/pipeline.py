"""
重构2：
pipeline——将各阶段串接成一次完整决策
RolePipelineAgent类定义了固定的四阶段执行顺序
子类通过构造函数注入不同的stage实现
"""

from typing import Any

from ..config import AgentConfig
from ..contracts import AgentAction, MarketObservation


class RolePipelineAgent:
    """
    pipeline基类，按 forecast → price → quantity → risk-gate 顺序执行。
    """

    def __init__(
        self,
        config: AgentConfig,
        *,
        forecaster: Any,
        pricer: Any,
        allocator: Any,
        risk_gate: Any,
    ) -> None:
        self.config = config
        self._forecaster = forecaster
        self._pricer = pricer
        self._allocator = allocator
        self._risk_gate = risk_gate

    def _run_pipeline(
        self,
        observation: MarketObservation,
        *,
        fallback: AgentAction | None = None,
    ) -> AgentAction:
        """执行完整pipeline过程"""
        forecast = self._forecaster.run(observation, fallback=fallback)
        price = self._pricer.run(observation, forecast, fallback=fallback)
        quantity = self._allocator.run(observation, forecast, price, fallback=fallback)
        return self._risk_gate.review(
            observation,
            AgentAction(forecast_demand=forecast, price=price, quantity=quantity),
            fallback=fallback,
        )

    def decide(self, observation: MarketObservation) -> AgentAction:
        """此为仿真环境调用的唯一公共入口。"""
        return self._run_pipeline(observation)
