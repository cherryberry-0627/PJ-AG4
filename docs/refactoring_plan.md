# PJ-AG4 重构计划

## 依赖关系图

```
Layer 0 (无内部依赖)
  utils.py, contracts.py

Layer 1 (仅依赖 Layer 0)
  config.py             → dotenv (外部)
  timeseries.py         → config, utils
  strategy_registry.py  → config

Layer 2 (依赖 Layer 0-1)
  environment.py        → config, contracts, timeseries, utils
  data/observation.py   → contracts, environment, timeseries, utils
  providers/            → config, openai (外部)

Layer 3 (依赖 Layer 0-2)
  core/runtime.py       → config, contracts, data/observation, environment, timeseries
  agents.py             → config, contracts, providers, strategy_registry, utils

Layer 4 (依赖 Layer 0-3)
  simulation.py         → agents, config, contracts, dashboard, core, environment, visualization
  dashboard.py          → config, environment
  visualization.py      → environment, matplotlib (外部)
  cli.py                → config, simulation

Layer 5 (应用层)
  web.py                → agents, config, core, dashboard, data/observation, environment, timeseries
```

---

## 现有问题

### 问题 1: `web.py` 重复仿真核心逻辑

**位置**: `web.py:173-220` (`iter_runtime_payloads`)

**描述**: `web.py` 包含一个独立的仿真循环，与 `SimulationRuntime.run()` + `simulation.run_simulation()` 几乎相同，额外加了 `_apply_runtime_controls()`。每次请求都手动构建 `generator`、`env`、`observations` 并逐回合迭代。

**影响**:
- 修改仿真逻辑需要同步两处（`runtime.py` 和 `web.py`）
- 多次出现过只改了一处的 bug
- `iter_runtime_payloads` 长约 50 行，几乎是 `SimulationRuntime.run()` 的完整拷贝

**方案**: 将 `_apply_runtime_controls()` 提取为 `SimulationRuntime` 的可选参数，使得 Web 端能复用同一代码路径。

---

### 问题 2: `dashboard.py` 内嵌 2000+ 行 HTML 模板

**位置**: `dashboard.py:286-1980`

**描述**: 整个 HTML/CSS/JS 交互面板以 Python 多行字符串形式存在 `_dashboard_html()` 函数中。虽然有 `L294-298` 尝试读取外部 `dashboard_template.html`，但回退路径仍是内嵌字符串。

**影响**:
- 修改前端布局必须在 Python 字符串中编辑，无语法高亮、无 lint
- `dashboard.py` 文件 1900+ 行，绝大部分是 HTML/JS
- 内嵌模板与外部模板可能产生差异

**方案**: 完全移除内嵌 HTML 回退，强制使用外部 `dashboard_template.html`，并在构建脚本中确保模板文件存在。

---

### 问题 3: `environment.py` 职责过载

**位置**: `environment.py`

**描述**: 一个文件同时包含：
- `SettlementRow` 数据模型（30+ 字段的 dataclass）
- `MarketEnvironment` 仿真引擎（~250 行结算逻辑）
- `write_rows_to_csv()` I/O 函数

**影响**:
- `dashboard.py`、`visualization.py` 导入 `environment.py` 仅为了 `SettlementRow` 类型
- 违反了单一职责原则

**方案**:
- `contracts.py` 接管 `SettlementRow`
- 新增 `io.py` 接管 `write_rows_to_csv()`
- `environment.py` 仅保留 `MarketEnvironment` 和 `AgentState`

---

### 问题 4: `config.py` 硬编码 agent 配置

**位置**: `config.py:104-177`

**描述**: `default_simulation_config()` 内联了三个 agent（Hyperscaler、PremiumCloud、SpotBroker）的完整参数。每个 agent 包含 18 个参数字段，总计约 70 行。

**影响**:
- 想用不同参数集运行仿真必须 copy-paste 修改
- 配置与默认值代码混合，不利于测试不同的战略配置
- 无法支持动态 agent 数量

**方案**: 将三个 agent 配置移到独立的数据文件（如 `config/agents.toml` 或 `config/agents.json`），通过数据驱动方式加载。

---

### 问题 5: `SettlementRow` 位置不当

**位置**: `environment.py:25-73`

**描述**: 核心仿真记录类型定义在 `environment.py` 中，被 `dashboard.py`、`visualization.py` 等多处导入。

**影响**: 本应是纯数据契约的类型潜在地引用了整个 environment 模块，增加了模块耦合。

**方案**: 移入 `contracts.py`，与 `AgentAction`、`MarketObservation`、`SimulationResult` 统一管理。

---

### 问题 6: `agents.py` 过大（619 行）

**位置**: `agents.py`

**描述**: 包含以下所有内容：
- 4 种风格调整函数 (`_forecaster_style_adjustment` 等)
- 4 个风格指南字典
- 启发式 Agent 子系统（`HeuristicForecasterStage` 等 3 个 stage 类）
- RolePipelineAgent 与 HeuristicAgent 类层次
- 3 个具体 agent 子类（HyperscalerAgent / PremiumCloudAgent / SpotBrokerAgent）
- LLM 子系统（`LLMPlanningStage` 及其 prompt 构造，3 个 LLM stage 类）
- LLM 与启发式 agent 工厂函数
- 内置策略注册

**影响**: 单一模块内高耦合、低内聚，任何修改都需要理解整个模块。

**方案**: 拆分为：
- `agents/_styles.py` — 风格调整函数与指南字典
- `agents/heuristic.py` — HeuristicAgent 及其子系统
- `agents/llm.py` — LLMPolicyAgent 及 LLM stage
- `agents/factory.py` — agent 工厂函数与策略注册
- `agents/__init__.py` — 公共 API 导出

---

### 问题 7: 类型依赖链条隐晦

`config.py` → `timeseries.py` / `environment.py` / `agents.py` 之间存在深层级依赖链，修改底层模块（如 `MarketConfig`）需要逐一检查所有下游修改。重构后建议引入明确的接口层隔离。

---

## 重构目标

1. **消除重复逻辑** — 统一 `web.py` 和 `simulation.py` 的仿真循环
2. **解耦模块** — 每一个模块有单一明确职责
3. **提取模板** — HTML/CSS/JS 与 Python 逻辑分离
4. **数据驱动配置** — agent 参数从代码中移出
5. **扁平化依赖** — 减少跨层直接引用

## 重构优先级

| 优先级 | 重构项 | 工作量 | 风险 |
|--------|--------|--------|------|
| P0 | SettlementRow 移入 contracts | 小 | 低 |
| P0 | 提取 write_rows_to_csv 到 io.py | 小 | 低 |
| P1 | 移除 dashboard.py 内嵌 HTML | 中 | 中 |
| P1 | 统一 web.py 与 runtime 的仿真循环 | 中 | 中 |
| P2 | 拆分 agents.py 为子模块 | 大 | 中 |
| P2 | agent 配置外移到数据文件 | 中 | 低 |
| P3 | 引入接口层隔离跨层依赖 | 大 | 高 |
