# LLM Modes Aligned Experiment Report

## Setting

- Code base for `llm-context`: remote `origin/main` at `c650e9d`.
- Existing `llm-adaptive` baseline: `outputs/llm_scenario_experiments/calibrated_v2_seed7_r12`.
- New direct LLM run: `outputs/llm_scenario_experiments/direct_llm_seed7_r12`.
- New context LLM run: `outputs/llm_scenario_experiments/llm_context_seed7_r12`.
- Scenarios: `baseline`, `price_war`, `supply_shock`, `high_volatility`, `no_reputation`, `no_transfer`.
- Seed: `7`.
- Rounds: `12`.
- Model: `gemini-3-flash`.
- Endpoint: `http://127.0.0.1:8045/v1`.

## Fallback Audit

All three modes completed the 6-scenario run without LLM fallback.

| Mode | Rows | Decision fallback | Strategy fallback |
| --- | ---: | ---: | ---: |
| `llm` | 216 | 0 | 0 |
| `llm-context` | 216 | 0 | 0 |
| `llm-adaptive` | 216 | 0 | 0 |

## Scenario Summary

| Mode | Scenario | Profit | Fulfillment | Forecast MAE | Transfer | Defaults | Final backlog |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `llm` | baseline | 3372.66 | 99.55% | 6.03 | 7.12 | 0 | 0.36 |
| `llm` | price_war | 2850.31 | 98.81% | 5.42 | 31.67 | 1 | 0.53 |
| `llm` | supply_shock | 3597.16 | 93.22% | 9.94 | 15.15 | 9 | 11.10 |
| `llm` | high_volatility | 3332.45 | 98.84% | 8.31 | 6.04 | 2 | 0.74 |
| `llm` | no_reputation | 3182.76 | 99.76% | 5.50 | 5.76 | 0 | 0.67 |
| `llm` | no_transfer | 3434.63 | 98.84% | 5.36 | 0.00 | 2 | 0.00 |
| `llm-context` | baseline | 3514.75 | 99.37% | 6.58 | 6.23 | 1 | 0.04 |
| `llm-context` | price_war | 2847.90 | 97.93% | 5.97 | 11.99 | 1 | 0.66 |
| `llm-context` | supply_shock | 3463.15 | 92.81% | 8.92 | 49.35 | 11 | 7.81 |
| `llm-context` | high_volatility | 3403.94 | 98.06% | 7.31 | 1.71 | 5 | 0.00 |
| `llm-context` | no_reputation | 3411.85 | 97.58% | 6.47 | 8.00 | 5 | 0.09 |
| `llm-context` | no_transfer | 3522.43 | 98.83% | 6.33 | 0.00 | 2 | 0.25 |
| `llm-adaptive` | baseline | 3716.37 | 99.34% | 26.86 | 39.99 | 2 | 0.52 |
| `llm-adaptive` | price_war | 3597.09 | 99.78% | 27.33 | 10.73 | 0 | 0.00 |
| `llm-adaptive` | supply_shock | 4237.78 | 95.30% | 55.36 | 92.52 | 7 | 10.92 |
| `llm-adaptive` | high_volatility | 3706.56 | 98.88% | 40.06 | 33.85 | 4 | 1.32 |
| `llm-adaptive` | no_reputation | 3532.82 | 98.86% | 28.17 | 41.87 | 4 | 3.23 |
| `llm-adaptive` | no_transfer | 3558.80 | 97.92% | 27.25 | 0.00 | 8 | 3.02 |

## Takeaways

- `llm` has very low forecast MAE because it directly outputs the next action, but it has lower total profit than `llm-adaptive` in every scenario.
- `llm-context` adds rolling settlement context and improves profit over direct `llm` in several scenarios, but does not dominate it everywhere.
- `llm-adaptive` remains the strongest final demo mode by profit and stress-response behavior, especially in `supply_shock`.
- `llm-context` is useful as a comparison group: it shows that simply adding historical context to direct action selection is not the same as bounded strategy adaptation.

## Files

- `aligned_llm_modes_seed7_r12_summary.csv`
- `aligned_llm_modes_seed7_r12_agent_summary.csv`
- `direct_llm_seed7_r12/<scenario>/simulation_results.csv`
- `llm_context_seed7_r12/<scenario>/simulation_results.csv`
- `calibrated_v2_seed7_r12/<scenario>/simulation_results.csv`
