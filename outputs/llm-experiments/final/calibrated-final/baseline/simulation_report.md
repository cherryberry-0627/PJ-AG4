# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | baseline | 12 | llm-adaptive | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit |
| --- | --- | --- | --- | --- |
| 2298 | 2282.82 | 0.99 | 5.83 | 3716.37 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 1481.83 | 123.49 | 25.83 | 4.97 | 1360.29 | 1.00 | 0.00 | 25.98 | 0 | 0 | 9.50 | 0.92 | 0.00 |
| PremiumCloud | premium | 1073.72 | 89.48 | 13.67 | 6.77 | 316.42 | 0.96 | 39.99 | 0.00 | 0 | 2 | 0.00 | 0.91 | 13.01 |
| SpotBroker | spot | 1160.81 | 96.73 | 41.08 | 5.77 | 606.10 | 1.00 | 0.00 | 14.01 | 0 | 0 | 14.06 | 0.93 | 2.18 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 180.00 | 5.47 | 576.32 | 1.00 | 0.00 | 23.81 | 0.27 |
| 1 | 197 | 195 | 196.73 | 5.53 | 228.69 | 0.27 | 6.63 | 14.03 | 0.06 |
| 2 | 198 | 197 | 198.00 | 5.80 | 303.81 | 0.00 | 6.99 | 22.56 | 0.00 |
| 3 | 202 | 204 | 201.09 | 5.80 | 343.21 | 0.91 | 0.00 | 31.91 | 0.25 |
| 4 | 193 | 194 | 193.00 | 5.87 | 285.65 | 0.00 | 6.01 | 20.30 | 0.00 |
| 5 | 182 | 183 | 182.00 | 5.87 | 224.18 | 0.00 | 5.20 | 17.32 | 0.00 |
| 6 | 171 | 175 | 166.56 | 5.93 | 170.99 | 4.44 | 0.00 | 15.70 | 3.65 |
| 7 | 194 | 196 | 190.35 | 5.93 | 342.48 | 3.65 | 2.16 | 7.57 | 2.19 |
| 8 | 196 | 187 | 193.81 | 5.93 | 272.93 | 2.19 | 1.18 | 4.17 | 1.17 |
| 9 | 200 | 198 | 198.83 | 5.93 | 361.63 | 1.17 | 3.82 | 13.60 | 0.88 |
| 10 | 198 | 198 | 197.12 | 5.93 | 352.81 | 0.88 | 3.99 | 14.27 | 0.67 |
| 11 | 186 | 183 | 185.33 | 6.00 | 253.67 | 0.67 | 4.00 | 14.69 | 0.52 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `baseline`, `Hyperscaler` ends first with cumulative profit `1481.83` and reputation `91.83%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `199.93` units and leaves final SLA backlog `0.52`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `39.99` units while average forecast error is `26.86`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 7 | 194 | 190.35 | shortage=3.65; transfer=2.16; default_flags=1 |
| 6 | 171 | 166.56 | shortage=4.44; default_flags=1 |
| 2 | 198 | 198.00 | transfer=6.99 |
| 1 | 197 | 196.73 | shortage=0.27; transfer=6.63 |
| 4 | 193 | 193.00 | transfer=6.01 |
| 5 | 182 | 182.00 | transfer=5.20 |
| 9 | 200 | 198.83 | shortage=1.17; transfer=3.82 |
| 10 | 198 | 197.12 | shortage=0.88; transfer=3.99 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm-adaptive | 184.00 | 4.00 | 4.60 | 0.20 | 90.00 | inventory target capped quantity | adaptive state risk=0.72, price=0.68, demand=0.62, inventory=0.34, shock=0.48, rivals=0.46; last update: initial strategy prior; fallback forecast=184, price=4.60, quantity=70; final forecast=188, price=4.80, quantity=70 |
| 0 | PremiumCloud | llm-adaptive | 184.00 | -1.00 | 6.80 | -0.20 | 0.00 | none | adaptive state risk=0.38, price=0.58, demand=0.46, inventory=0.72, shock=0.36, rivals=0.32; last update: initial strategy prior; fallback forecast=184, price=6.80, quantity=0; final forecast=183, price=6.60, quantity=0 |
| 0 | SpotBroker | llm-adaptive | 184.00 | 3.00 | 5.00 | 0.00 | 30.00 | none | adaptive state risk=0.56, price=0.44, demand=0.58, inventory=0.54, shock=0.76, rivals=0.78; last update: initial strategy prior; fallback forecast=184, price=5.00, quantity=30; final forecast=187, price=5.00, quantity=30 |
| 1 | Hyperscaler | llm-adaptive | 184.00 | 4.00 | 4.60 | 0.20 | 120.00 | none | adaptive state risk=0.74, price=0.70, demand=0.63, inventory=0.32, shock=0.48, rivals=0.47; last update: Captured dominant 55% market share and top profitability in Round 0 with zero ending inventory. Boosting risk tolerance and reducing inventory caution to secure capacity readiness for sustained market capture, while maintaining high price aggressiveness to keep competitors at bay.; fallback forecast=184, price=4.60, quantity=120; final forecast=188, price=4.80, quantity=120 |
| 1 | PremiumCloud | llm-adaptive | 184.00 | -1.00 | 6.80 | -0.20 | 30.00 | none | adaptive state risk=0.38, price=0.57, demand=0.47, inventory=0.74, shock=0.36, rivals=0.31; last update: Round 0 was highly successful with a perfect 1.0 SLA service rate and near-optimal profits. To protect our premium brand and maintain price discipline, we slightly decrease competitor reactivity and price aggressiveness, while marginally increasing inventory caution to ensure we sustain our flawless service record.; fallback forecast=184, price=6.80, quantity=40; final forecast=183, price=6.60, quantity=30 |
| 1 | SpotBroker | llm-adaptive | 184.00 | 3.00 | 5.00 | 0.20 | 60.00 | inventory target capped quantity | adaptive state risk=0.58, price=0.51, demand=0.60, inventory=0.58, shock=0.79, rivals=0.83; last update: Competitors are pricing significantly higher (5.70 vs our 5.00). Increasing price aggressiveness and competitor reactivity to tactically close this gap, while keeping inventory caution high to maintain a light and flexible footprint.; fallback forecast=184, price=5.00, quantity=60; final forecast=187, price=5.20, quantity=60 |
| 2 | Hyperscaler | llm-adaptive | 198.00 | 22.00 | 4.60 | 0.40 | 120.00 | none | adaptive state risk=0.77, price=0.68, demand=0.67, inventory=0.29, shock=0.49, rivals=0.49; last update: Maintaining scale dominant strategy by keeping inventory caution low and risk tolerance high to secure capacity readiness. Adjusting demand sensitivity upward to correct the slight under-forecast, and slightly easing price aggressiveness to reclaim margin while keeping a strong market share lead.; fallback forecast=198, price=4.60, quantity=120; final forecast=220, price=5.00, quantity=120 |
| 2 | PremiumCloud | llm-adaptive | 193.00 | 10.00 | 7.00 | -0.20 | 20.00 | none | adaptive state risk=0.37, price=0.58, demand=0.47, inventory=0.76, shock=0.36, rivals=0.30; last update: Maintaining premium pricing discipline and perfect SLA execution yielded the market's best profit. We slightly increase inventory caution to secure reliability and reduce competitor reactivity to avoid margin erosion from cheaper operators.; fallback forecast=193, price=7.00, quantity=30; final forecast=203, price=6.80, quantity=20 |
| 2 | SpotBroker | llm-adaptive | 200.00 | 32.00 | 5.60 | 0.00 | 60.00 | inventory target capped quantity | adaptive state risk=0.61, price=0.58, demand=0.65, inventory=0.60, shock=0.80, rivals=0.88; last update: Increased competitor reactivity and price aggressiveness to close the margin gap against higher competitor pricing, while raising demand sensitivity to resolve the minor supply shortage.; fallback forecast=200, price=5.60, quantity=50; final forecast=232, price=5.60, quantity=60 |
| 3 | Hyperscaler | llm-adaptive | 198.00 | 23.00 | 4.60 | 0.40 | 120.00 | none | adaptive state risk=0.80, price=0.70, demand=0.66, inventory=0.27, shock=0.50, rivals=0.51; last update: Secured dominant 57% market share and top profit last round. Decreasing inventory caution and increasing risk tolerance to maintain capacity readiness and support aggressive share capture, while keeping competitive pricing margins relative to competitors.; fallback forecast=198, price=4.60, quantity=120; final forecast=221, price=5.00, quantity=120 |
| 3 | PremiumCloud | llm-adaptive | 195.00 | 11.00 | 7.00 | -0.20 | 20.00 | none | adaptive state risk=0.38, price=0.57, demand=0.46, inventory=0.77, shock=0.36, rivals=0.29; last update: Achieved a perfect 1.0 service rate and solid profits while preserving premium margins above competitor averages. We are slightly lowering competitor reactivity and price aggressiveness to resist undercutting temptation, maintaining our premium brand positioning and SLA discipline.; fallback forecast=195, price=7.00, quantity=30; final forecast=206, price=6.80, quantity=20 |
| 3 | SpotBroker | llm-adaptive | 200.00 | 32.00 | 5.60 | 0.00 | 50.00 | none | adaptive state risk=0.62, price=0.61, demand=0.62, inventory=0.65, shock=0.81, rivals=0.90; last update: We successfully cleared our inventory but left money on the table by pricing below the competitor average. Increasing price aggressiveness and competitor reactivity to capture better margins, while raising inventory caution to maintain a light, flexible posture after a slight over-forecast.; fallback forecast=200, price=5.60, quantity=50; final forecast=232, price=5.60, quantity=50 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | Scale aggressor | 0.02 | -0.02 | 0.02 | 0.70 | 0.32 | 0.74 | Captured dominant 55% market share and top profitability in Round 0 with zero ending inventory. Boosting risk tolerance and reducing inventory caution to secure capacity readiness for sustained market capture, while maintaining high price aggressiveness to keep competitors at bay. |
| 0 | PremiumCloud | Reputation guardian | -0.01 | 0.02 | 0.00 | 0.57 | 0.74 | 0.38 | Round 0 was highly successful with a perfect 1.0 SLA service rate and near-optimal profits. To protect our premium brand and maintain price discipline, we slightly decrease competitor reactivity and price aggressiveness, while marginally increasing inventory caution to ensure we sustain our flawless service record. |
| 0 | SpotBroker | Agile spread hunter | 0.07 | 0.04 | 0.02 | 0.51 | 0.58 | 0.58 | Competitors are pricing significantly higher (5.70 vs our 5.00). Increasing price aggressiveness and competitor reactivity to tactically close this gap, while keeping inventory caution high to maintain a light and flexible footprint. |
| 1 | Hyperscaler | Scale aggressor | -0.02 | -0.02 | 0.03 | 0.68 | 0.29 | 0.77 | Maintaining scale dominant strategy by keeping inventory caution low and risk tolerance high to secure capacity readiness. Adjusting demand sensitivity upward to correct the slight under-forecast, and slightly easing price aggressiveness to reclaim margin while keeping a strong market share lead. |
| 1 | PremiumCloud | Reputation guardian | 0.01 | 0.02 | -0.01 | 0.58 | 0.76 | 0.37 | Maintaining premium pricing discipline and perfect SLA execution yielded the market's best profit. We slightly increase inventory caution to secure reliability and reduce competitor reactivity to avoid margin erosion from cheaper operators. |
| 1 | SpotBroker | Agile spread hunter | 0.06 | 0.02 | 0.03 | 0.58 | 0.60 | 0.61 | Increased competitor reactivity and price aggressiveness to close the margin gap against higher competitor pricing, while raising demand sensitivity to resolve the minor supply shortage. |
| 2 | Hyperscaler | Scale aggressor | 0.02 | -0.02 | 0.03 | 0.70 | 0.27 | 0.80 | Secured dominant 57% market share and top profit last round. Decreasing inventory caution and increasing risk tolerance to maintain capacity readiness and support aggressive share capture, while keeping competitive pricing margins relative to competitors. |
| 2 | PremiumCloud | Reputation guardian | -0.01 | 0.01 | 0.00 | 0.57 | 0.77 | 0.38 | Achieved a perfect 1.0 service rate and solid profits while preserving premium margins above competitor averages. We are slightly lowering competitor reactivity and price aggressiveness to resist undercutting temptation, maintaining our premium brand positioning and SLA discipline. |
| 2 | SpotBroker | Agile spread hunter | 0.04 | 0.05 | 0.02 | 0.61 | 0.65 | 0.62 | We successfully cleared our inventory but left money on the table by pricing below the competitor average. Increasing price aggressiveness and competitor reactivity to capture better margins, while raising inventory caution to maintain a light, flexible posture after a slight over-forecast. |
| 3 | Hyperscaler | Scale aggressor | 0.01 | -0.01 | 0.02 | 0.71 | 0.26 | 0.82 | LLM adjusted bounded strategy parameters. |
| 3 | PremiumCloud | Reputation guardian | -0.01 | 0.01 | 0.00 | 0.56 | 0.78 | 0.38 | LLM adjusted bounded strategy parameters. |
| 3 | SpotBroker | Agile spread hunter | 0.06 | 0.02 | 0.04 | 0.67 | 0.67 | 0.66 | Reacting to the competitor price gap (we priced at 5.6 vs competitor avg of 5.9) by boosting price aggressiveness and competitor reactivity to capture higher margins. Reducing demand sensitivity slightly to correct the mild over-forecasting while maintaining high inventory caution to keep assets light. |

## Conclusion Notes

- **Winner:** `Hyperscaler` ends with cumulative profit `1481.83`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.77`.
- **Market fulfillment:** the run sells `2282.82` units against `2298.00` true demand for a fulfillment ratio of `99.34%`.
- **Operational stress:** peer transfers total `39.99` units, customer reallocation totals `199.93`, final SLA backlog is `0.52`, with `0` dump flags and `2` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
