# LLM Mode Alignment With Context Engineering

All runs use seed 7, 12 rounds, six scenario profiles, and the local `gemini-3-flash` endpoint. Direct `llm` and bounded `llm-adaptive` are reused because their code path did not change; both context modes were rerun after the context engineering prompt update.

## Validation

| mode | scenario | rows | decision sources | strategy sources | decision fallback | strategy fallback |
|---|---:|---:|---|---|---:|---:|
| llm | baseline | 36 | llm:36 | - | 0 | 0 |
| llm | price_war | 36 | llm:36 | - | 0 | 0 |
| llm | supply_shock | 36 | llm:36 | - | 0 | 0 |
| llm | high_volatility | 36 | llm:36 | - | 0 | 0 |
| llm | no_reputation | 36 | llm:36 | - | 0 | 0 |
| llm | no_transfer | 36 | llm:36 | - | 0 | 0 |
| llm-context-engineering | baseline | 36 | llm-context:36 | - | 0 | 0 |
| llm-context-engineering | price_war | 36 | llm-context:36 | - | 0 | 0 |
| llm-context-engineering | supply_shock | 36 | llm-context:36 | - | 0 | 0 |
| llm-context-engineering | high_volatility | 36 | llm-context:36 | - | 0 | 0 |
| llm-context-engineering | no_reputation | 36 | llm-context:36 | - | 0 | 0 |
| llm-context-engineering | no_transfer | 36 | llm-context:36 | - | 0 | 0 |
| llm-adaptive | baseline | 36 | llm-adaptive:36 | llm-adaptive:36 | 0 | 0 |
| llm-adaptive | price_war | 36 | llm-adaptive:36 | llm-adaptive:36 | 0 | 0 |
| llm-adaptive | supply_shock | 36 | llm-adaptive:36 | llm-adaptive:36 | 0 | 0 |
| llm-adaptive | high_volatility | 36 | llm-adaptive:36 | llm-adaptive:36 | 0 | 0 |
| llm-adaptive | no_reputation | 36 | llm-adaptive:36 | llm-adaptive:36 | 0 | 0 |
| llm-adaptive | no_transfer | 36 | llm-adaptive:36 | llm-adaptive:36 | 0 | 0 |
| llm-context-adaptive-engineering | baseline | 36 | llm-context-adaptive:36 | llm-context-adaptive:36 | 0 | 0 |
| llm-context-adaptive-engineering | price_war | 36 | llm-context-adaptive:36 | llm-context-adaptive:36 | 0 | 0 |
| llm-context-adaptive-engineering | supply_shock | 36 | llm-context-adaptive:36 | llm-context-adaptive:36 | 0 | 0 |
| llm-context-adaptive-engineering | high_volatility | 36 | llm-context-adaptive:36 | llm-context-adaptive:36 | 0 | 0 |
| llm-context-adaptive-engineering | no_reputation | 36 | llm-context-adaptive:36 | llm-context-adaptive:36 | 0 | 0 |
| llm-context-adaptive-engineering | no_transfer | 36 | llm-context-adaptive:36 | llm-context-adaptive:36 | 0 | 0 |

## Scenario Summary

| mode | scenario | profit | fulfill | MAE | transfer | defaults | final backlog |
|---|---:|---:|---:|---:|---:|---:|---:|
| llm | baseline | 3372.66 | 99.55% | 6.03 | 7.12 | 0 | 0.36 |
| llm | price_war | 2850.31 | 98.81% | 5.42 | 31.67 | 1 | 0.53 |
| llm | supply_shock | 3597.16 | 93.22% | 9.94 | 15.15 | 9 | 11.10 |
| llm | high_volatility | 3332.45 | 98.84% | 8.31 | 6.04 | 2 | 0.74 |
| llm | no_reputation | 3182.76 | 99.76% | 5.50 | 5.76 | 0 | 0.67 |
| llm | no_transfer | 3434.63 | 98.84% | 5.36 | 0.00 | 2 | 0.00 |
| llm-context-engineering | baseline | 3173.89 | 97.77% | 5.81 | 5.12 | 5 | 0.02 |
| llm-context-engineering | price_war | 3045.81 | 97.58% | 6.25 | 22.45 | 2 | 0.06 |
| llm-context-engineering | supply_shock | 3696.31 | 95.10% | 9.08 | 50.31 | 9 | 11.19 |
| llm-context-engineering | high_volatility | 3211.96 | 97.45% | 8.56 | 4.88 | 5 | 0.18 |
| llm-context-engineering | no_reputation | 3371.59 | 99.13% | 5.97 | 3.01 | 0 | 0.67 |
| llm-context-engineering | no_transfer | 3355.75 | 98.21% | 6.67 | 0.00 | 6 | 1.34 |
| llm-adaptive | baseline | 3716.37 | 99.34% | 26.86 | 39.99 | 2 | 0.52 |
| llm-adaptive | price_war | 3597.09 | 99.78% | 27.33 | 10.73 | 0 | 0.00 |
| llm-adaptive | supply_shock | 4237.78 | 95.30% | 55.36 | 92.52 | 7 | 10.92 |
| llm-adaptive | high_volatility | 3706.56 | 98.88% | 40.06 | 33.85 | 4 | 1.32 |
| llm-adaptive | no_reputation | 3532.82 | 98.86% | 28.17 | 41.87 | 4 | 3.23 |
| llm-adaptive | no_transfer | 3558.80 | 97.92% | 27.25 | 0.00 | 8 | 3.02 |
| llm-context-adaptive-engineering | baseline | 3823.67 | 99.20% | 27.61 | 38.96 | 3 | 0.58 |
| llm-context-adaptive-engineering | price_war | 3501.24 | 98.96% | 27.72 | 11.70 | 1 | 0.08 |
| llm-context-adaptive-engineering | supply_shock | 4326.60 | 96.08% | 57.03 | 83.96 | 7 | 3.65 |
| llm-context-adaptive-engineering | high_volatility | 3745.00 | 99.27% | 39.61 | 41.65 | 2 | 1.10 |
| llm-context-adaptive-engineering | no_reputation | 3693.09 | 98.96% | 26.47 | 40.89 | 5 | 2.63 |
| llm-context-adaptive-engineering | no_transfer | 3591.06 | 98.29% | 27.33 | 0.00 | 7 | 0.00 |

## Best Profit By Scenario

`llm-context-adaptive-engineering` 3823.67, `llm-adaptive` 3716.37, `llm` 3372.66, `llm-context-engineering` 3173.89
`llm-adaptive` 3597.09, `llm-context-adaptive-engineering` 3501.24, `llm-context-engineering` 3045.81, `llm` 2850.31
`llm-context-adaptive-engineering` 4326.60, `llm-adaptive` 4237.78, `llm-context-engineering` 3696.31, `llm` 3597.16
`llm-context-adaptive-engineering` 3745.00, `llm-adaptive` 3706.56, `llm` 3332.45, `llm-context-engineering` 3211.96
`llm-context-adaptive-engineering` 3693.09, `llm-adaptive` 3532.82, `llm-context-engineering` 3371.59, `llm` 3182.76
`llm-context-adaptive-engineering` 3591.06, `llm-adaptive` 3558.80, `llm` 3434.63, `llm-context-engineering` 3355.75
