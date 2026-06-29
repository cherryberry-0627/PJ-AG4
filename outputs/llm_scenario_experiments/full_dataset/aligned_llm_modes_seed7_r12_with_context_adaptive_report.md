# Four LLM Mode Alignment: seed7 r12

Modes: direct `llm`, direct `llm-context`, bounded `llm-adaptive`, and bounded `llm-context-adaptive`. All runs use seed 7, 12 rounds, the same six scenario profiles, and the local `gemini-3-flash` endpoint.

## Scenario Summary

| mode | scenario | profit | fulfill | MAE | transfer | defaults | final backlog | strategy fallback |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| llm | baseline | 3372.66 | 99.55% | 6.03 | 7.12 | 0 | 0.36 | 0 |
| llm | price_war | 2850.31 | 98.81% | 5.42 | 31.67 | 1 | 0.53 | 0 |
| llm | supply_shock | 3597.16 | 93.22% | 9.94 | 15.15 | 9 | 11.10 | 0 |
| llm | high_volatility | 3332.45 | 98.84% | 8.31 | 6.04 | 2 | 0.74 | 0 |
| llm | no_reputation | 3182.76 | 99.76% | 5.50 | 5.76 | 0 | 0.67 | 0 |
| llm | no_transfer | 3434.63 | 98.84% | 5.36 | 0.00 | 2 | 0.00 | 0 |
| llm-context | baseline | 3514.75 | 99.37% | 6.58 | 6.23 | 1 | 0.04 | 0 |
| llm-context | price_war | 2847.90 | 97.93% | 5.97 | 11.99 | 1 | 0.66 | 0 |
| llm-context | supply_shock | 3463.15 | 92.81% | 8.92 | 49.35 | 11 | 7.81 | 0 |
| llm-context | high_volatility | 3403.94 | 98.06% | 7.31 | 1.71 | 5 | 0.00 | 0 |
| llm-context | no_reputation | 3411.85 | 97.58% | 6.47 | 8.00 | 5 | 0.09 | 0 |
| llm-context | no_transfer | 3522.43 | 98.83% | 6.33 | 0.00 | 2 | 0.25 | 0 |
| llm-adaptive | baseline | 3716.37 | 99.34% | 26.86 | 39.99 | 2 | 0.52 | 0 |
| llm-adaptive | price_war | 3597.09 | 99.78% | 27.33 | 10.73 | 0 | 0.00 | 0 |
| llm-adaptive | supply_shock | 4237.78 | 95.30% | 55.36 | 92.52 | 7 | 10.92 | 0 |
| llm-adaptive | high_volatility | 3706.56 | 98.88% | 40.06 | 33.85 | 4 | 1.32 | 0 |
| llm-adaptive | no_reputation | 3532.82 | 98.86% | 28.17 | 41.87 | 4 | 3.23 | 0 |
| llm-adaptive | no_transfer | 3558.80 | 97.92% | 27.25 | 0.00 | 8 | 3.02 | 0 |
| llm-context-adaptive | baseline | 3799.47 | 99.38% | 26.69 | 40.25 | 2 | 0.52 | 0 |
| llm-context-adaptive | price_war | 3535.85 | 99.49% | 26.31 | 10.68 | 0 | 0.00 | 0 |
| llm-context-adaptive | supply_shock | 4184.98 | 93.79% | 58.31 | 82.96 | 7 | 10.76 | 0 |
| llm-context-adaptive | high_volatility | 3754.89 | 99.02% | 39.67 | 27.05 | 4 | 1.06 | 0 |
| llm-context-adaptive | no_reputation | 3709.82 | 99.22% | 27.53 | 41.81 | 2 | 1.03 | 0 |
| llm-context-adaptive | no_transfer | 3526.23 | 98.05% | 28.08 | 0.00 | 8 | 1.54 | 0 |

## Best Profit By Scenario

- `baseline`: best `llm-context-adaptive` profit 3799.47; runner-up `llm-adaptive` profit 3716.37.
- `price_war`: best `llm-adaptive` profit 3597.09; runner-up `llm-context-adaptive` profit 3535.85.
- `supply_shock`: best `llm-adaptive` profit 4237.78; runner-up `llm-context-adaptive` profit 4184.98.
- `high_volatility`: best `llm-context-adaptive` profit 3754.89; runner-up `llm-adaptive` profit 3706.56.
- `no_reputation`: best `llm-context-adaptive` profit 3709.82; runner-up `llm-adaptive` profit 3532.82.
- `no_transfer`: best `llm-adaptive` profit 3558.80; runner-up `llm-context-adaptive` profit 3526.23.

## Notes

- `llm-context-adaptive` kept zero strategy fallbacks in all six scenarios, so the new rolling-context prompt was accepted by the local model.
- It remains a bounded strategy-update mode: the LLM adjusts strategy state deltas, while price/quantity/forecast are still generated through deterministic transforms and the risk gate.
- The two CSV files beside this report contain full scenario-level and agent-level tables for presentation charts.
