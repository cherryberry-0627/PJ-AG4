# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | supply_shock | 12 | llm-adaptive | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit |
| --- | --- | --- | --- | --- |
| 2532 | 2413.07 | 0.95 | 5.86 | 4237.78 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 1581.90 | 131.83 | 51.83 | 5.00 | 1320.19 | 0.98 | 10.08 | 78.32 | 0 | 2 | 0.00 | 0.80 | 38.31 |
| PremiumCloud | premium | 1177.76 | 98.15 | 33.67 | 6.77 | 375.17 | 0.86 | 78.06 | 0.00 | 0 | 5 | 0.00 | 0.64 | 73.06 |
| SpotBroker | spot | 1478.12 | 123.18 | 80.58 | 5.80 | 717.70 | 0.99 | 4.38 | 14.20 | 0 | 0 | 0.00 | 0.93 | 7.56 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 180.00 | 5.47 | 586.43 | 1.00 | 8.92 | 14.88 | 0.25 |
| 1 | 196 | 194 | 195.75 | 5.60 | 295.88 | 0.25 | 9.55 | 14.32 | 0.06 |
| 2 | 196 | 195 | 196.00 | 5.73 | 253.80 | 0.00 | 13.37 | 14.06 | 0.00 |
| 3 | 203 | 205 | 203.00 | 5.73 | 331.70 | 0.00 | 13.42 | 13.71 | 0.00 |
| 4 | 196 | 197 | 196.00 | 5.87 | 311.02 | 0.00 | 12.80 | 13.77 | 0.00 |
| 5 | 184 | 185 | 184.00 | 5.87 | 243.47 | 0.00 | 10.94 | 11.77 | 0.00 |
| 6 | 169 | 173 | 169.00 | 5.93 | 246.05 | 0.00 | 9.33 | 10.18 | 0.00 |
| 7 | 194 | 196 | 186.28 | 5.93 | 319.60 | 7.72 | 4.11 | 12.92 | 5.42 |
| 8 | 253 | 244 | 225.25 | 5.93 | 421.70 | 27.75 | 0.00 | 1.79 | 13.01 |
| 9 | 256 | 254 | 236.99 | 6.00 | 433.35 | 19.01 | 10.08 | 16.54 | 6.73 |
| 10 | 257 | 257 | 223.27 | 6.07 | 383.07 | 33.73 | 0.00 | 22.50 | 12.47 |
| 11 | 247 | 244 | 217.53 | 6.13 | 411.72 | 29.47 | 0.00 | 12.40 | 10.92 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `supply_shock`, `Hyperscaler` ends first with cumulative profit `1581.90` and reputation `79.56%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `158.85` units and leaves final SLA backlog `10.92`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `92.52` units while average forecast error is `55.36`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 10 | 257 | 223.27 | shock=60.00; shortage=33.73; default_flags=2 |
| 11 | 247 | 217.53 | shock=60.00; shortage=29.47; default_flags=2 |
| 9 | 256 | 236.99 | shock=60.00; shortage=19.01; transfer=10.08; default_flags=1 |
| 8 | 253 | 225.25 | shock=60.00; shortage=27.75; default_flags=1 |
| 7 | 194 | 186.28 | shortage=7.72; transfer=4.11; default_flags=1 |
| 3 | 203 | 203.00 | transfer=13.42 |
| 2 | 196 | 196.00 | transfer=13.37 |
| 4 | 196 | 196.00 | transfer=12.80 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm-adaptive | 184.00 | 4.00 | 4.60 | 0.20 | 90.00 | inventory target capped quantity | adaptive state risk=0.72, price=0.68, demand=0.62, inventory=0.34, shock=0.48, rivals=0.46; last update: initial strategy prior; fallback forecast=184, price=4.60, quantity=70; final forecast=188, price=4.80, quantity=70 |
| 0 | PremiumCloud | llm-adaptive | 184.00 | -1.00 | 6.80 | -0.20 | 0.00 | none | adaptive state risk=0.38, price=0.58, demand=0.46, inventory=0.72, shock=0.36, rivals=0.32; last update: initial strategy prior; fallback forecast=184, price=6.80, quantity=0; final forecast=183, price=6.60, quantity=0 |
| 0 | SpotBroker | llm-adaptive | 184.00 | 3.00 | 5.00 | 0.00 | 30.00 | none | adaptive state risk=0.56, price=0.44, demand=0.58, inventory=0.54, shock=0.76, rivals=0.78; last update: initial strategy prior; fallback forecast=184, price=5.00, quantity=30; final forecast=187, price=5.00, quantity=30 |
| 1 | Hyperscaler | llm-adaptive | 184.00 | 4.00 | 4.60 | 0.40 | 120.00 | inventory target capped quantity | adaptive state risk=0.76, price=0.70, demand=0.61, inventory=0.31, shock=0.48, rivals=0.49; last update: Ended the round with zero inventory, showing robust demand. Decreasing inventory caution and increasing risk tolerance to ensure capacity readiness and prevent potential future shortages, while slightly raising competitive reactivity to optimize pricing against higher competitor rates.; fallback forecast=184, price=4.60, quantity=120; final forecast=188, price=5.00, quantity=110 |
| 1 | PremiumCloud | llm-adaptive | 184.00 | -2.00 | 6.80 | -0.20 | 30.00 | none | adaptive state risk=0.38, price=0.59, demand=0.45, inventory=0.73, shock=0.36, rivals=0.31; last update: Exceptional round earning us the highest profit despite charging a premium premium rate of 6.6 with a perfect 1.0 service rate. We reduce competitor reactivity to remain focused on our premium positioning, slightly bolster inventory caution to safeguard SLA, and maintain our disciplined pricing stance.; fallback forecast=184, price=6.80, quantity=40; final forecast=182, price=6.60, quantity=30 |
| 1 | SpotBroker | llm-adaptive | 184.00 | 4.00 | 5.00 | 0.20 | 70.00 | inventory target capped quantity | adaptive state risk=0.61, price=0.52, demand=0.61, inventory=0.50, shock=0.80, rivals=0.85; last update: Reacting to the large competitor price gap (our $5.00 vs competitor $5.70 average) by boosting price aggressiveness and competitor reactivity. Reducing inventory caution slightly to eliminate the minor shortage, while maintaining high responsiveness to catch oncoming market volatility.; fallback forecast=184, price=5.00, quantity=60; final forecast=188, price=5.20, quantity=60 |
| 2 | Hyperscaler | llm-adaptive | 196.00 | 19.00 | 4.60 | 0.40 | 120.00 | none | adaptive state risk=0.78, price=0.71, demand=0.63, inventory=0.30, shock=0.48, rivals=0.49; last update: Successfully captured the highest profit and nearly 50% market share in Round 1 by pricing competitively. Maintaining scale-dominant posture by slightly reducing inventory caution and increasing risk tolerance to ensure capacity readiness for future demand.; fallback forecast=196, price=4.60, quantity=120; final forecast=215, price=5.00, quantity=120 |
| 2 | PremiumCloud | llm-adaptive | 192.00 | 9.00 | 7.00 | -0.20 | 20.00 | none | adaptive state risk=0.38, price=0.58, demand=0.47, inventory=0.75, shock=0.36, rivals=0.30; last update: Maintained premium pricing discipline and 100% service rate with strong profits. Slightly increased inventory caution and demand sensitivity to safeguard our high SLA reliability against future demand fluctuations, while avoiding overreaction to competitor pricing.; fallback forecast=192, price=7.00, quantity=30; final forecast=201, price=6.80, quantity=20 |
| 2 | SpotBroker | llm-adaptive | 198.00 | 30.00 | 5.20 | 0.20 | 70.00 | inventory target capped quantity | adaptive state risk=0.62, price=0.58, demand=0.65, inventory=0.55, shock=0.82, rivals=0.87; last update: Our price (5.2) was significantly below the competitor average (5.8), leaving margin on the table. Increasing price aggressiveness and competitor reactivity to tactically close this gap, while boosting demand sensitivity to minimize under-forecasting and inventory caution to sustain our lean, zero-inventory profile.; fallback forecast=198, price=5.20, quantity=60; final forecast=228, price=5.40, quantity=70 |
| 3 | Hyperscaler | llm-adaptive | 196.00 | 19.00 | 4.60 | 0.40 | 120.00 | none | adaptive state risk=0.81, price=0.74, demand=0.64, inventory=0.27, shock=0.48, rivals=0.50; last update: Retained top profit and 50%+ market share with our aggressive pricing strategy. To secure long-term capacity readiness and maintain pressure, we slightly decrease inventory caution and increase risk tolerance to ensure we do not run inventory-light.; fallback forecast=196, price=4.60, quantity=120; final forecast=215, price=5.00, quantity=120 |
| 3 | PremiumCloud | llm-adaptive | 194.00 | 9.00 | 7.00 | -0.20 | 20.00 | none | adaptive state risk=0.37, price=0.57, demand=0.48, inventory=0.77, shock=0.35, rivals=0.29; last update: Maintained a perfect 1.0 service rate and secure premium margins. In line with guarding reputation and preserving price discipline, competitor reactivity and price aggressiveness are reduced to avoid chasing lower competitor prices, while inventory caution is slightly increased to reinforce SLA reliability.; fallback forecast=194, price=7.00, quantity=30; final forecast=203, price=6.80, quantity=20 |
| 3 | SpotBroker | llm-adaptive | 198.00 | 28.00 | 5.20 | 0.20 | 70.00 | inventory target capped quantity | adaptive state risk=0.64, price=0.64, demand=0.60, inventory=0.60, shock=0.83, rivals=0.90; last update: Adjusting parameters to exploit the competitor price gap by increasing aggressiveness and reactivity, while maintaining strict inventory caution following an overforecasted demand round.; fallback forecast=198, price=5.20, quantity=60; final forecast=226, price=5.40, quantity=60 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | Scale aggressor | 0.02 | -0.03 | 0.04 | 0.70 | 0.31 | 0.76 | Ended the round with zero inventory, showing robust demand. Decreasing inventory caution and increasing risk tolerance to ensure capacity readiness and prevent potential future shortages, while slightly raising competitive reactivity to optimize pricing against higher competitor rates. |
| 0 | PremiumCloud | Reputation guardian | 0.01 | 0.01 | 0.00 | 0.59 | 0.73 | 0.38 | Exceptional round earning us the highest profit despite charging a premium premium rate of 6.6 with a perfect 1.0 service rate. We reduce competitor reactivity to remain focused on our premium positioning, slightly bolster inventory caution to safeguard SLA, and maintain our disciplined pricing stance. |
| 0 | SpotBroker | Agile spread hunter | 0.08 | -0.04 | 0.05 | 0.52 | 0.50 | 0.61 | Reacting to the large competitor price gap (our $5.00 vs competitor $5.70 average) by boosting price aggressiveness and competitor reactivity. Reducing inventory caution slightly to eliminate the minor shortage, while maintaining high responsiveness to catch oncoming market volatility. |
| 1 | Hyperscaler | Scale aggressor | 0.01 | -0.01 | 0.02 | 0.71 | 0.30 | 0.78 | Successfully captured the highest profit and nearly 50% market share in Round 1 by pricing competitively. Maintaining scale-dominant posture by slightly reducing inventory caution and increasing risk tolerance to ensure capacity readiness for future demand. |
| 1 | PremiumCloud | Reputation guardian | -0.01 | 0.02 | 0.00 | 0.58 | 0.75 | 0.38 | Maintained premium pricing discipline and 100% service rate with strong profits. Slightly increased inventory caution and demand sensitivity to safeguard our high SLA reliability against future demand fluctuations, while avoiding overreaction to competitor pricing. |
| 1 | SpotBroker | Agile spread hunter | 0.05 | 0.05 | 0.02 | 0.58 | 0.55 | 0.62 | Our price (5.2) was significantly below the competitor average (5.8), leaving margin on the table. Increasing price aggressiveness and competitor reactivity to tactically close this gap, while boosting demand sensitivity to minimize under-forecasting and inventory caution to sustain our lean, zero-inventory profile. |
| 2 | Hyperscaler | Scale aggressor | 0.02 | -0.02 | 0.02 | 0.74 | 0.27 | 0.81 | Retained top profit and 50%+ market share with our aggressive pricing strategy. To secure long-term capacity readiness and maintain pressure, we slightly decrease inventory caution and increase risk tolerance to ensure we do not run inventory-light. |
| 2 | PremiumCloud | Reputation guardian | -0.01 | 0.01 | -0.01 | 0.57 | 0.77 | 0.37 | Maintained a perfect 1.0 service rate and secure premium margins. In line with guarding reputation and preserving price discipline, competitor reactivity and price aggressiveness are reduced to avoid chasing lower competitor prices, while inventory caution is slightly increased to reinforce SLA reliability. |
| 2 | SpotBroker | Agile spread hunter | 0.06 | 0.05 | 0.02 | 0.64 | 0.60 | 0.64 | Adjusting parameters to exploit the competitor price gap by increasing aggressiveness and reactivity, while maintaining strict inventory caution following an overforecasted demand round. |
| 3 | Hyperscaler | Scale aggressor | 0.02 | -0.01 | 0.02 | 0.76 | 0.26 | 0.83 | Maintaining strong market share dominance (currently at 51%) and capacity readiness by increasing risk tolerance and decreasing inventory caution. Slightly increasing competitor reactivity allows us to capture more margin given high competitor pricing, while price aggressiveness ensures we remain the market share leader. |
| 3 | PremiumCloud | Reputation guardian | -0.01 | 0.02 | -0.01 | 0.55 | 0.78 | 0.37 | Maintaining disciplined premium pricing and perfect SLA reliability (1.0). Marginally reduced competitor reactivity and price aggressiveness to resist matching low-cost competitors, while slightly boosting inventory caution to safeguard our flawless service rate. |
| 3 | SpotBroker | Agile spread hunter | 0.05 | 0.04 | 0.01 | 0.69 | 0.64 | 0.65 | Capitalizing on our round win by raising competitor reactivity and price aggressiveness to tactically follow competitor prices upward (they averaged 5.9 vs our 5.4). Increasing inventory caution and demand sensitivity ensures we remain lean, flexible, and responsive to any sudden market shifts. |

## Conclusion Notes

- **Winner:** `Hyperscaler` ends with cumulative profit `1581.90`, the highest value in this run.
- **Service leader:** `SpotBroker` posts the strongest average service rate at `99.01%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.77`.
- **Market fulfillment:** the run sells `2413.07` units against `2532.00` true demand for a fulfillment ratio of `95.30%`.
- **Operational stress:** peer transfers total `92.52` units, customer reallocation totals `158.85`, final SLA backlog is `10.92`, with `0` dump flags and `7` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
