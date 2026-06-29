# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | supply_shock | 12 | llm-context | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit | Price Pressure Cost |
| --- | --- | --- | --- | --- | --- |
| 2532 | 2350.06 | 0.93 | 5.53 | 3463.15 | 0.00 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Price Pressure Cost | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 1000.90 | 83.41 | 10.33 | 4.60 | 1299.61 | 0.95 | 0.00 | 45.63 | 0.00 | 10 | 3 | 0.00 | 0.44 | 78.47 |
| PremiumCloud | premium | 1464.64 | 122.05 | 11.08 | 6.58 | 452.37 | 0.87 | 4.97 | 1.90 | 0.00 | 0 | 6 | 0.00 | 0.69 | 73.53 |
| SpotBroker | spot | 997.61 | 83.13 | 5.33 | 5.42 | 598.08 | 0.95 | 44.38 | 1.82 | 0.00 | 0 | 2 | 0.00 | 0.90 | 29.94 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 180.00 | 5.13 | 523.83 | 1.00 | 16.19 | 25.79 | 0.64 |
| 1 | 196 | 194 | 169.36 | 5.33 | 171.96 | 26.64 | 0.00 | 23.77 | 12.18 |
| 2 | 196 | 195 | 183.82 | 5.20 | 190.03 | 12.18 | 16.75 | 18.32 | 5.20 |
| 3 | 203 | 205 | 198.20 | 5.40 | 266.65 | 4.80 | 10.38 | 13.01 | 1.95 |
| 4 | 196 | 197 | 187.07 | 5.47 | 195.22 | 8.93 | 1.90 | 10.10 | 3.10 |
| 5 | 184 | 185 | 183.42 | 5.53 | 219.29 | 0.58 | 0.05 | 0.05 | 0.30 |
| 6 | 169 | 173 | 169.00 | 5.53 | 261.25 | 0.00 | 2.26 | 2.52 | 0.00 |
| 7 | 194 | 196 | 190.70 | 5.60 | 268.55 | 3.30 | 1.82 | 5.51 | 1.95 |
| 8 | 253 | 244 | 232.07 | 5.67 | 355.22 | 20.93 | 0.00 | 0.55 | 10.26 |
| 9 | 256 | 254 | 219.74 | 5.80 | 326.09 | 36.26 | 0.00 | 6.53 | 12.00 |
| 10 | 257 | 257 | 218.00 | 5.87 | 335.70 | 39.00 | 0.00 | 3.34 | 11.32 |
| 11 | 247 | 244 | 218.68 | 5.87 | 349.34 | 28.32 | 0.00 | 0.00 | 7.81 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `supply_shock`, `PremiumCloud` ends first with cumulative profit `1464.64` and reputation `69.14%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `109.48` units and leaves final SLA backlog `7.81`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `49.35` units while average forecast error is `8.92`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 10 | 257 | 218.00 | shock=60.00; shortage=39.00; dump_flags=1; default_flags=2 |
| 9 | 256 | 219.74 | shock=60.00; shortage=36.26; dump_flags=1; default_flags=2 |
| 11 | 247 | 218.68 | shock=60.00; shortage=28.32; dump_flags=1; default_flags=2 |
| 8 | 253 | 232.07 | shock=60.00; shortage=20.93; dump_flags=1; default_flags=1 |
| 1 | 196 | 169.36 | shortage=26.64; dump_flags=1; default_flags=2 |
| 2 | 196 | 183.82 | shortage=12.18; transfer=16.75; dump_flags=1; default_flags=1 |
| 4 | 196 | 187.07 | shortage=8.93; transfer=1.90; dump_flags=1; default_flags=1 |
| 3 | 203 | 198.20 | shortage=4.80; transfer=10.38; dump_flags=1 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm-context | 184.00 | 6.00 | 4.60 | 0.00 | 80.00 | inventory target capped quantity | forecast 184.0 + 6.0; price 4.60 + 0.00; quantity target 80.0; risk gate inventory target capped quantity; final forecast=190, price=4.60, quantity=80 |
| 0 | PremiumCloud | llm-context | 184.00 | -4.00 | 6.80 | -0.40 | 20.00 | inventory target capped quantity | forecast 184.0 + -4.0; price 6.80 + -0.40; quantity target 20.0; risk gate inventory target capped quantity; final forecast=180, price=6.40, quantity=0 |
| 0 | SpotBroker | llm-context | 184.00 | -4.00 | 5.00 | -0.60 | 20.00 | none | forecast 184.0 + -4.0; price 5.00 + -0.60; quantity target 20.0; risk gate none; final forecast=180, price=4.40, quantity=20 |
| 1 | Hyperscaler | llm-context | 184.00 | 20.00 | 4.60 | 0.00 | 110.00 | none | forecast 184.0 + 20.0; price 4.60 + 0.00; quantity target 110.0; risk gate none; final forecast=204, price=4.60, quantity=110 |
| 1 | PremiumCloud | llm-context | 184.00 | 6.00 | 6.80 | -0.20 | 50.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 184.0 + 6.0; price 6.80 + -0.20; quantity target 50.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=190, price=6.60, quantity=30 |
| 1 | SpotBroker | llm-context | 184.00 | 16.00 | 5.00 | -0.20 | 30.00 | none | forecast 184.0 + 16.0; price 5.00 + -0.20; quantity target 30.0; risk gate none; final forecast=200, price=4.80, quantity=30 |
| 2 | Hyperscaler | llm-context | 196.00 | 10.00 | 4.60 | 0.00 | 120.00 | none | forecast 196.0 + 10.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=206, price=4.60, quantity=120 |
| 2 | PremiumCloud | llm-context | 192.00 | 3.00 | 7.00 | -0.40 | 50.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 192.0 + 3.0; price 7.00 + -0.40; quantity target 50.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=195, price=6.60, quantity=40 |
| 2 | SpotBroker | llm-context | 198.00 | -2.00 | 4.20 | 0.20 | 40.00 | none | forecast 198.0 + -2.0; price 4.20 + 0.20; quantity target 40.0; risk gate none; final forecast=196, price=4.40, quantity=40 |
| 3 | Hyperscaler | llm-context | 196.00 | 19.00 | 4.60 | 0.00 | 120.00 | none | forecast 196.0 + 19.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=215, price=4.60, quantity=120 |
| 3 | PremiumCloud | llm-context | 194.00 | 6.00 | 7.00 | -0.40 | 50.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 194.0 + 6.0; price 7.00 + -0.40; quantity target 50.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=200, price=6.60, quantity=40 |
| 3 | SpotBroker | llm-context | 198.00 | 10.00 | 4.80 | 0.20 | 40.00 | none | forecast 198.0 + 10.0; price 4.80 + 0.20; quantity target 40.0; risk gate none; final forecast=208, price=5.00, quantity=40 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Conclusion Notes

- **Winner:** `PremiumCloud` ends with cumulative profit `1464.64`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `95.37%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.58`.
- **Market fulfillment:** the run sells `2350.06` units against `2532.00` true demand for a fulfillment ratio of `92.81%`.
- **Operational stress:** peer transfers total `49.35` units, customer reallocation totals `109.48`, final SLA backlog is `7.81`, with `10` dump flags and `11` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
