# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | supply_shock | 12 | heuristic | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit | Price Pressure Cost |
| --- | --- | --- | --- | --- | --- |
| 2532 | 2434.88 | 0.96 | 5.73 | 3813.33 | 0.00 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Price Pressure Cost | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 950.16 | 79.18 | 16.50 | 4.60 | 1274.83 | 0.96 | 0.00 | 29.39 | 0.00 | 9 | 3 | 0.00 | 0.50 | 66.51 |
| PremiumCloud | premium | 1608.69 | 134.06 | 16.75 | 6.97 | 449.64 | 0.94 | 30.83 | 0.00 | 0.00 | 0 | 2 | 0.00 | 0.86 | 30.62 |
| SpotBroker | spot | 1254.48 | 104.54 | 16.75 | 5.63 | 710.41 | 1.00 | 3.59 | 5.03 | 0.00 | 0 | 0 | 12.87 | 0.86 | 0.00 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 180.00 | 5.47 | 569.43 | 1.00 | 5.77 | 10.15 | 0.63 |
| 1 | 196 | 194 | 195.37 | 5.47 | 170.06 | 0.63 | 1.29 | 1.93 | 0.37 |
| 2 | 196 | 195 | 195.63 | 5.60 | 217.98 | 0.37 | 5.01 | 5.29 | 0.24 |
| 3 | 203 | 205 | 202.76 | 5.60 | 296.33 | 0.24 | 5.38 | 5.65 | 0.15 |
| 4 | 196 | 197 | 195.85 | 5.73 | 278.22 | 0.15 | 5.43 | 5.80 | 0.10 |
| 5 | 184 | 185 | 183.90 | 5.73 | 215.95 | 0.10 | 4.07 | 4.33 | 0.06 |
| 6 | 169 | 173 | 168.94 | 5.73 | 224.92 | 0.06 | 2.45 | 2.60 | 0.04 |
| 7 | 194 | 196 | 193.93 | 5.73 | 393.48 | 0.07 | 4.13 | 4.44 | 0.04 |
| 8 | 253 | 244 | 232.38 | 5.80 | 350.27 | 20.62 | 0.00 | 7.54 | 10.27 |
| 9 | 256 | 254 | 226.59 | 5.93 | 356.15 | 29.41 | 0.00 | 15.42 | 9.68 |
| 10 | 257 | 257 | 227.83 | 6.00 | 375.03 | 29.17 | 0.00 | 13.35 | 8.29 |
| 11 | 247 | 244 | 231.70 | 6.00 | 365.53 | 15.30 | 0.90 | 11.86 | 4.10 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `supply_shock`, `PremiumCloud` ends first with cumulative profit `1608.69` and reputation `86.32%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `88.37` units and leaves final SLA backlog `4.10`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `34.42` units while average forecast error is `16.67`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 9 | 256 | 226.59 | shock=60.00; shortage=29.41; dump_flags=1; default_flags=2 |
| 10 | 257 | 227.83 | shock=60.00; shortage=29.17; dump_flags=1; default_flags=1 |
| 8 | 253 | 232.38 | shock=60.00; shortage=20.62; dump_flags=1; default_flags=1 |
| 11 | 247 | 231.70 | shock=60.00; shortage=15.30; transfer=0.90; dump_flags=1; default_flags=1 |
| 3 | 203 | 202.76 | shortage=0.24; transfer=5.38; dump_flags=1 |
| 4 | 196 | 195.85 | shortage=0.15; transfer=5.43; dump_flags=1 |
| 2 | 196 | 195.63 | shortage=0.37; transfer=5.01; dump_flags=1 |
| 5 | 184 | 183.90 | shortage=0.10; transfer=4.07; dump_flags=1 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | heuristic | 184.00 | 0.00 | 4.60 | -0.57 | 262.58 | inventory target capped quantity | forecast 184.0 + 0.0; price 4.60 + -0.57; quantity target 262.6; risk gate inventory target capped quantity; final forecast=184, price=4.60, quantity=70 |
| 0 | PremiumCloud | heuristic | 184.00 | 0.09 | 5.40 | 1.30 | 114.08 | inventory target capped quantity | forecast 184.0 + 0.1; price 5.40 + 1.30; quantity target 114.1; risk gate inventory target capped quantity; final forecast=184, price=6.80, quantity=0 |
| 0 | SpotBroker | heuristic | 184.00 | 0.00 | 4.90 | 0.12 | 73.60 | inventory target capped quantity | forecast 184.0 + 0.0; price 4.90 + 0.12; quantity target 73.6; risk gate inventory target capped quantity; final forecast=184, price=5.00, quantity=30 |
| 1 | Hyperscaler | heuristic | 184.00 | 0.00 | 4.60 | -0.55 | 304.68 | none | forecast 184.0 + 0.0; price 4.60 + -0.55; quantity target 304.7; risk gate none; final forecast=184, price=4.60, quantity=120 |
| 1 | PremiumCloud | heuristic | 184.00 | 0.09 | 5.40 | 1.31 | 124.88 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 184.0 + 0.1; price 5.40 + 1.31; quantity target 124.9; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=184, price=6.80, quantity=40 |
| 1 | SpotBroker | heuristic | 184.00 | 0.00 | 4.90 | 0.12 | 78.60 | inventory target capped quantity | forecast 184.0 + 0.0; price 4.90 + 0.12; quantity target 78.6; risk gate inventory target capped quantity; final forecast=184, price=5.00, quantity=60 |
| 2 | Hyperscaler | heuristic | 190.67 | 4.80 | 4.60 | -0.86 | 286.29 | inventory target capped quantity | forecast 190.7 + 4.8; price 4.60 + -0.86; quantity target 286.3; risk gate inventory target capped quantity; final forecast=196, price=4.60, quantity=110 |
| 2 | PremiumCloud | heuristic | 190.67 | 0.64 | 5.40 | 1.68 | 129.84 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 190.7 + 0.6; price 5.40 + 1.68; quantity target 129.8; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=192, price=7.00, quantity=30 |
| 2 | SpotBroker | heuristic | 190.67 | 6.80 | 4.90 | 0.37 | 91.20 | inventory target capped quantity | forecast 190.7 + 6.8; price 4.90 + 0.37; quantity target 91.2; risk gate inventory target capped quantity; final forecast=198, price=5.20, quantity=70 |
| 3 | Hyperscaler | heuristic | 192.83 | 2.77 | 4.60 | -0.86 | 286.05 | inventory target capped quantity | forecast 192.8 + 2.8; price 4.60 + -0.86; quantity target 286.0; risk gate inventory target capped quantity; final forecast=196, price=4.60, quantity=110 |
| 3 | PremiumCloud | heuristic | 192.83 | 0.33 | 5.40 | 1.68 | 131.08 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 192.8 + 0.3; price 5.40 + 1.68; quantity target 131.1; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=194, price=7.00, quantity=30 |
| 3 | SpotBroker | heuristic | 192.83 | 4.23 | 4.90 | 0.37 | 86.80 | inventory target capped quantity | forecast 192.8 + 4.2; price 4.90 + 0.37; quantity target 86.8; risk gate inventory target capped quantity; final forecast=198, price=5.20, quantity=60 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Conclusion Notes

- **Winner:** `PremiumCloud` ends with cumulative profit `1608.69`, the highest value in this run.
- **Service leader:** `SpotBroker` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.97`.
- **Market fulfillment:** the run sells `2434.88` units against `2532.00` true demand for a fulfillment ratio of `96.16%`.
- **Operational stress:** peer transfers total `34.42` units, customer reallocation totals `88.37`, final SLA backlog is `4.10`, with `9` dump flags and `5` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
