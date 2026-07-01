# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | supply_shock | 12 | llm | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit | Price Pressure Cost |
| --- | --- | --- | --- | --- | --- |
| 2532 | 2360.43 | 0.93 | 5.63 | 3597.16 | 0.00 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Price Pressure Cost | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 940.17 | 78.35 | 11.67 | 4.60 | 1279.19 | 0.94 | 0.00 | 15.15 | 0.00 | 9 | 3 | 0.00 | 0.51 | 90.30 |
| PremiumCloud | premium | 1502.32 | 125.19 | 11.67 | 6.72 | 444.36 | 0.90 | 8.35 | 0.00 | 0.00 | 0 | 4 | 0.00 | 0.83 | 57.71 |
| SpotBroker | spot | 1154.67 | 96.22 | 6.50 | 5.58 | 636.87 | 0.97 | 6.80 | 0.00 | 0.00 | 0 | 2 | 0.00 | 0.80 | 23.56 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 170.00 | 5.13 | 501.26 | 11.00 | 6.19 | 25.79 | 4.66 |
| 1 | 196 | 194 | 191.34 | 5.27 | 138.47 | 4.66 | 2.66 | 2.13 | 1.89 |
| 2 | 196 | 195 | 194.55 | 5.40 | 255.33 | 1.45 | 1.17 | 1.23 | 0.80 |
| 3 | 203 | 205 | 202.20 | 5.60 | 305.45 | 0.80 | 1.06 | 1.59 | 0.44 |
| 4 | 196 | 197 | 174.33 | 5.67 | 305.93 | 21.67 | 0.00 | 2.56 | 8.77 |
| 5 | 184 | 185 | 184.00 | 5.73 | 219.06 | 0.00 | 0.00 | 0.00 | 0.00 |
| 6 | 169 | 173 | 169.00 | 5.67 | 169.08 | 0.00 | 0.00 | 0.00 | 0.00 |
| 7 | 194 | 196 | 194.00 | 5.73 | 345.86 | 0.00 | 4.06 | 4.39 | 0.00 |
| 8 | 253 | 244 | 224.40 | 5.80 | 339.50 | 28.60 | 0.00 | 5.20 | 12.89 |
| 9 | 256 | 254 | 217.11 | 5.87 | 333.32 | 38.89 | 0.00 | 7.86 | 12.22 |
| 10 | 257 | 257 | 227.78 | 5.87 | 367.40 | 29.22 | 0.00 | 9.01 | 8.30 |
| 11 | 247 | 244 | 211.70 | 5.87 | 316.49 | 35.30 | 0.00 | 0.00 | 11.10 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `supply_shock`, `PremiumCloud` ends first with cumulative profit `1502.32` and reputation `83.45%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `59.78` units and leaves final SLA backlog `11.10`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `15.15` units while average forecast error is `9.94`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 9 | 256 | 217.11 | shock=60.00; shortage=38.89; dump_flags=1; default_flags=2 |
| 11 | 247 | 211.70 | shock=60.00; shortage=35.30; dump_flags=1; default_flags=2 |
| 10 | 257 | 227.78 | shock=60.00; shortage=29.22; dump_flags=1; default_flags=1 |
| 8 | 253 | 224.40 | shock=60.00; shortage=28.60; dump_flags=1; default_flags=1 |
| 0 | 181 | 170.00 | shortage=11.00; transfer=6.19; default_flags=2 |
| 4 | 196 | 174.33 | shortage=21.67; default_flags=1 |
| 1 | 196 | 191.34 | shortage=4.66; transfer=2.66; dump_flags=1 |
| 7 | 194 | 194.00 | transfer=4.06; dump_flags=1 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm | 184.00 | 6.00 | 4.60 | 0.00 | 70.00 | none | forecast 184.0 + 6.0; price 4.60 + 0.00; quantity target 70.0; risk gate none; final forecast=190, price=4.60, quantity=70 |
| 0 | PremiumCloud | llm | 184.00 | -4.00 | 6.80 | -0.40 | 20.00 | inventory target capped quantity | forecast 184.0 + -4.0; price 6.80 + -0.40; quantity target 20.0; risk gate inventory target capped quantity; final forecast=180, price=6.40, quantity=0 |
| 0 | SpotBroker | llm | 184.00 | -4.00 | 5.00 | -0.60 | 20.00 | none | forecast 184.0 + -4.0; price 5.00 + -0.60; quantity target 20.0; risk gate none; final forecast=180, price=4.40, quantity=20 |
| 1 | Hyperscaler | llm | 184.00 | 21.00 | 4.60 | 0.00 | 120.00 | none | forecast 184.0 + 21.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=205, price=4.60, quantity=120 |
| 1 | PremiumCloud | llm | 184.00 | 6.00 | 6.60 | -0.20 | 50.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 184.0 + 6.0; price 6.60 + -0.20; quantity target 50.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=190, price=6.40, quantity=40 |
| 1 | SpotBroker | llm | 184.00 | 16.00 | 4.40 | 0.40 | 70.00 | inventory target capped quantity | forecast 184.0 + 16.0; price 4.40 + 0.40; quantity target 70.0; risk gate inventory target capped quantity; final forecast=200, price=4.80, quantity=60 |
| 2 | Hyperscaler | llm | 196.00 | 9.00 | 4.60 | 0.00 | 100.00 | none | forecast 196.0 + 9.0; price 4.60 + 0.00; quantity target 100.0; risk gate none; final forecast=205, price=4.60, quantity=100 |
| 2 | PremiumCloud | llm | 192.00 | 3.00 | 7.00 | -0.40 | 50.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 192.0 + 3.0; price 7.00 + -0.40; quantity target 50.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=195, price=6.60, quantity=40 |
| 2 | SpotBroker | llm | 198.00 | -2.00 | 5.20 | -0.20 | 60.00 | none | forecast 198.0 + -2.0; price 5.20 + -0.20; quantity target 60.0; risk gate none; final forecast=196, price=5.00, quantity=60 |
| 3 | Hyperscaler | llm | 196.00 | 19.00 | 4.60 | 0.00 | 110.00 | none | forecast 196.0 + 19.0; price 4.60 + 0.00; quantity target 110.0; risk gate none; final forecast=215, price=4.60, quantity=110 |
| 3 | PremiumCloud | llm | 194.00 | 4.00 | 7.00 | -0.20 | 40.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 194.0 + 4.0; price 7.00 + -0.20; quantity target 40.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=198, price=6.80, quantity=40 |
| 3 | SpotBroker | llm | 198.00 | 12.00 | 5.20 | 0.20 | 50.00 | none | forecast 198.0 + 12.0; price 5.20 + 0.20; quantity target 50.0; risk gate none; final forecast=210, price=5.40, quantity=50 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Conclusion Notes

- **Winner:** `PremiumCloud` ends with cumulative profit `1502.32`, the highest value in this run.
- **Service leader:** `SpotBroker` posts the strongest average service rate at `96.64%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.72`.
- **Market fulfillment:** the run sells `2360.43` units against `2532.00` true demand for a fulfillment ratio of `93.22%`.
- **Operational stress:** peer transfers total `15.15` units, customer reallocation totals `59.78`, final SLA backlog is `11.10`, with `9` dump flags and `9` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
