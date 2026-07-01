# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | supply_shock | 12 | llm-context | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit | Price Pressure Cost |
| --- | --- | --- | --- | --- | --- |
| 2532 | 2407.99 | 0.95 | 5.54 | 3696.31 | 0.00 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Price Pressure Cost | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 1028.03 | 85.67 | 11.50 | 4.60 | 1299.11 | 0.96 | 0.00 | 50.31 | 0.00 | 9 | 3 | 0.00 | 0.52 | 63.11 |
| PremiumCloud | premium | 1606.01 | 133.83 | 10.83 | 6.45 | 534.35 | 0.94 | 17.21 | 0.00 | 0.00 | 0 | 4 | 0.00 | 0.78 | 40.51 |
| SpotBroker | spot | 1062.27 | 88.52 | 4.92 | 5.58 | 574.53 | 0.97 | 33.10 | 0.00 | 0.00 | 0 | 2 | 0.00 | 0.80 | 20.39 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 180.00 | 5.20 | 534.46 | 1.00 | 14.55 | 23.33 | 0.64 |
| 1 | 196 | 194 | 189.36 | 5.33 | 228.42 | 6.64 | 8.92 | 22.37 | 3.39 |
| 2 | 196 | 195 | 192.61 | 5.40 | 236.82 | 3.39 | 8.36 | 12.54 | 1.67 |
| 3 | 203 | 205 | 201.33 | 5.47 | 246.95 | 1.67 | 4.91 | 7.37 | 0.87 |
| 4 | 196 | 197 | 195.13 | 5.53 | 257.33 | 0.87 | 6.60 | 9.90 | 0.46 |
| 5 | 184 | 185 | 178.72 | 5.47 | 253.23 | 5.28 | 1.53 | 9.51 | 1.82 |
| 6 | 169 | 173 | 167.18 | 5.47 | 254.62 | 1.82 | 1.77 | 2.66 | 0.55 |
| 7 | 194 | 196 | 193.88 | 5.53 | 261.63 | 0.12 | 3.66 | 3.95 | 0.07 |
| 8 | 253 | 244 | 232.73 | 5.67 | 368.65 | 20.27 | 0.00 | 5.98 | 7.82 |
| 9 | 256 | 254 | 232.18 | 5.73 | 357.29 | 23.82 | 0.00 | 11.79 | 7.53 |
| 10 | 257 | 257 | 232.47 | 5.87 | 380.13 | 24.53 | 0.00 | 10.63 | 7.60 |
| 11 | 247 | 244 | 212.40 | 5.87 | 316.78 | 34.60 | 0.00 | 0.00 | 11.19 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `supply_shock`, `PremiumCloud` ends first with cumulative profit `1606.01` and reputation `78.27%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `120.05` units and leaves final SLA backlog `11.19`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `50.31` units while average forecast error is `9.08`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 11 | 247 | 212.40 | shock=60.00; shortage=34.60; dump_flags=1; default_flags=3 |
| 10 | 257 | 232.47 | shock=60.00; shortage=24.53; dump_flags=1; default_flags=2 |
| 9 | 256 | 232.18 | shock=60.00; shortage=23.82; dump_flags=1; default_flags=1 |
| 8 | 253 | 232.73 | shock=60.00; shortage=20.27; dump_flags=1; default_flags=1 |
| 1 | 196 | 189.36 | shortage=6.64; transfer=8.92; dump_flags=1; default_flags=1 |
| 2 | 196 | 192.61 | shortage=3.39; transfer=8.36; dump_flags=1 |
| 4 | 196 | 195.13 | shortage=0.87; transfer=6.60; dump_flags=1 |
| 5 | 184 | 178.72 | shortage=5.28; transfer=1.53; default_flags=1 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm-context | 184.00 | 6.00 | 4.60 | 0.00 | 80.00 | inventory target capped quantity | forecast 184.0 + 6.0; price 4.60 + 0.00; quantity target 80.0; risk gate inventory target capped quantity; final forecast=190, price=4.60, quantity=80 |
| 0 | PremiumCloud | llm-context | 184.00 | -4.00 | 6.80 | -0.40 | 20.00 | inventory target capped quantity | forecast 184.0 + -4.0; price 6.80 + -0.40; quantity target 20.0; risk gate inventory target capped quantity; final forecast=180, price=6.40, quantity=0 |
| 0 | SpotBroker | llm-context | 184.00 | -4.00 | 5.00 | -0.40 | 20.00 | none | forecast 184.0 + -4.0; price 5.00 + -0.40; quantity target 20.0; risk gate none; final forecast=180, price=4.60, quantity=20 |
| 1 | Hyperscaler | llm-context | 184.00 | 16.00 | 4.60 | 0.00 | 120.00 | none | forecast 184.0 + 16.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=200, price=4.60, quantity=120 |
| 1 | PremiumCloud | llm-context | 184.00 | 6.00 | 6.80 | -0.40 | 40.00 | sla_guard reduced quantity under SLA/reputation pressure | forecast 184.0 + 6.0; price 6.80 + -0.40; quantity target 40.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; final forecast=190, price=6.40, quantity=40 |
| 1 | SpotBroker | llm-context | 184.00 | 11.00 | 5.00 | 0.00 | 30.00 | none | forecast 184.0 + 11.0; price 5.00 + 0.00; quantity target 30.0; risk gate none; final forecast=195, price=5.00, quantity=30 |
| 2 | Hyperscaler | llm-context | 196.00 | 4.00 | 4.60 | 0.00 | 120.00 | none | forecast 196.0 + 4.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=200, price=4.60, quantity=120 |
| 2 | PremiumCloud | llm-context | 192.00 | 3.00 | 7.00 | -0.60 | 50.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 192.0 + 3.0; price 7.00 + -0.60; quantity target 50.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=195, price=6.40, quantity=40 |
| 2 | SpotBroker | llm-context | 198.00 | 0.00 | 5.00 | 0.20 | 40.00 | none | forecast 198.0 + 0.0; price 5.00 + 0.20; quantity target 40.0; risk gate none; final forecast=198, price=5.20, quantity=40 |
| 3 | Hyperscaler | llm-context | 196.00 | 14.00 | 4.60 | 0.00 | 120.00 | none | forecast 196.0 + 14.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=210, price=4.60, quantity=120 |
| 3 | PremiumCloud | llm-context | 194.00 | 6.00 | 7.00 | -0.60 | 50.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 194.0 + 6.0; price 7.00 + -0.60; quantity target 50.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=200, price=6.40, quantity=40 |
| 3 | SpotBroker | llm-context | 198.00 | 12.00 | 5.20 | 0.20 | 50.00 | none | forecast 198.0 + 12.0; price 5.20 + 0.20; quantity target 50.0; risk gate none; final forecast=210, price=5.40, quantity=50 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Conclusion Notes

- **Winner:** `PremiumCloud` ends with cumulative profit `1606.01`, the highest value in this run.
- **Service leader:** `SpotBroker` posts the strongest average service rate at `96.69%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.45`.
- **Market fulfillment:** the run sells `2407.99` units against `2532.00` true demand for a fulfillment ratio of `95.10%`.
- **Operational stress:** peer transfers total `50.31` units, customer reallocation totals `120.05`, final SLA backlog is `11.19`, with `9` dump flags and `9` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
