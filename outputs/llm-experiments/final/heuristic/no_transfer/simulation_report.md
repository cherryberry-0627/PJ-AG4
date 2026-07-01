# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | no_transfer | 12 | heuristic | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit | Price Pressure Cost |
| --- | --- | --- | --- | --- | --- |
| 2298 | 2284.45 | 0.99 | 5.71 | 3312.05 | 0.00 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Price Pressure Cost | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 841.89 | 70.16 | 9.67 | 4.60 | 1250.28 | 1.00 | 0.00 | 0.00 | 0.00 | 9 | 0 | 24.95 | 0.67 | 0.00 |
| PremiumCloud | premium | 1528.78 | 127.40 | 9.92 | 6.97 | 414.25 | 0.97 | 0.00 | 0.00 | 0.00 | 0 | 1 | 1.54 | 0.95 | 13.55 |
| SpotBroker | spot | 941.39 | 78.45 | 9.92 | 5.57 | 619.93 | 1.00 | 0.00 | 0.00 | 0.00 | 0 | 0 | 25.77 | 0.90 | 0.00 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 180.00 | 5.47 | 563.12 | 1.00 | 0.00 | 15.92 | 0.67 |
| 1 | 197 | 195 | 196.33 | 5.47 | 171.98 | 0.67 | 0.00 | 4.51 | 0.41 |
| 2 | 198 | 197 | 194.69 | 5.67 | 248.46 | 3.31 | 0.00 | 9.46 | 2.38 |
| 3 | 202 | 204 | 201.52 | 5.73 | 288.92 | 0.48 | 0.00 | 0.00 | 0.26 |
| 4 | 193 | 194 | 193.00 | 5.73 | 232.47 | 0.00 | 0.00 | 0.00 | 0.00 |
| 5 | 182 | 183 | 181.07 | 5.73 | 242.94 | 0.93 | 0.00 | 2.98 | 0.55 |
| 6 | 171 | 175 | 169.76 | 5.73 | 176.75 | 1.24 | 0.00 | 2.24 | 0.72 |
| 7 | 194 | 196 | 191.25 | 5.80 | 421.68 | 2.75 | 0.00 | 6.85 | 1.80 |
| 8 | 196 | 187 | 196.00 | 5.80 | 216.77 | 0.00 | 0.00 | 0.00 | 0.00 |
| 9 | 200 | 198 | 197.86 | 5.80 | 322.14 | 2.14 | 0.00 | 7.22 | 1.41 |
| 10 | 198 | 198 | 196.99 | 5.80 | 221.02 | 1.01 | 0.00 | 0.00 | 0.55 |
| 11 | 186 | 183 | 186.00 | 5.80 | 205.81 | 0.00 | 0.00 | 0.00 | 0.00 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `no_transfer`, `PremiumCloud` ends first with cumulative profit `1528.78` and reputation `94.79%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `49.18` units and leaves final SLA backlog `0.00`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `0.00` units while average forecast error is `9.83`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 2 | 198 | 194.69 | shortage=3.31; dump_flags=1; default_flags=1 |
| 9 | 200 | 197.86 | shortage=2.14; dump_flags=1 |
| 6 | 171 | 169.76 | shortage=1.24; dump_flags=1 |
| 10 | 198 | 196.99 | shortage=1.01; dump_flags=1 |
| 1 | 197 | 196.33 | shortage=0.67; dump_flags=1 |
| 3 | 202 | 201.52 | shortage=0.48; dump_flags=1 |
| 4 | 193 | 193.00 | dump_flags=1 |
| 8 | 196 | 196.00 | dump_flags=1 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | heuristic | 184.00 | 0.00 | 4.60 | -0.57 | 262.58 | inventory target capped quantity | forecast 184.0 + 0.0; price 4.60 + -0.57; quantity target 262.6; risk gate inventory target capped quantity; final forecast=184, price=4.60, quantity=70 |
| 0 | PremiumCloud | heuristic | 184.00 | 0.09 | 5.40 | 1.30 | 114.08 | inventory target capped quantity | forecast 184.0 + 0.1; price 5.40 + 1.30; quantity target 114.1; risk gate inventory target capped quantity; final forecast=184, price=6.80, quantity=0 |
| 0 | SpotBroker | heuristic | 184.00 | 0.00 | 4.90 | 0.12 | 73.60 | inventory target capped quantity | forecast 184.0 + 0.0; price 4.90 + 0.12; quantity target 73.6; risk gate inventory target capped quantity; final forecast=184, price=5.00, quantity=30 |
| 1 | Hyperscaler | heuristic | 184.00 | 0.00 | 4.60 | -0.55 | 304.68 | none | forecast 184.0 + 0.0; price 4.60 + -0.55; quantity target 304.7; risk gate none; final forecast=184, price=4.60, quantity=120 |
| 1 | PremiumCloud | heuristic | 184.00 | 0.09 | 5.40 | 1.31 | 124.88 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 184.0 + 0.1; price 5.40 + 1.31; quantity target 124.9; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=184, price=6.80, quantity=40 |
| 1 | SpotBroker | heuristic | 184.00 | 0.00 | 4.90 | 0.12 | 78.60 | inventory target capped quantity | forecast 184.0 + 0.0; price 4.90 + 0.12; quantity target 78.6; risk gate inventory target capped quantity; final forecast=184, price=5.00, quantity=60 |
| 2 | Hyperscaler | heuristic | 191.33 | 5.28 | 4.60 | -0.89 | 290.27 | inventory target capped quantity | forecast 191.3 + 5.3; price 4.60 + -0.89; quantity target 290.3; risk gate inventory target capped quantity; final forecast=198, price=4.60, quantity=110 |
| 2 | PremiumCloud | heuristic | 191.33 | 0.69 | 5.40 | 1.71 | 130.46 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 191.3 + 0.7; price 5.40 + 1.71; quantity target 130.5; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=193, price=7.00, quantity=30 |
| 2 | SpotBroker | heuristic | 191.33 | 7.48 | 4.90 | 0.40 | 92.70 | inventory_guard lifted price under volatility; inventory target capped quantity | forecast 191.3 + 7.5; price 4.90 + 0.40; quantity target 92.7; risk gate inventory_guard lifted price under volatility; inventory target capped quantity; final forecast=200, price=5.40, quantity=60 |
| 3 | Hyperscaler | heuristic | 194.17 | 3.27 | 4.60 | -0.90 | 293.81 | inventory target capped quantity | forecast 194.2 + 3.3; price 4.60 + -0.90; quantity target 293.8; risk gate inventory target capped quantity; final forecast=198, price=4.60, quantity=110 |
| 3 | PremiumCloud | heuristic | 194.17 | 0.37 | 5.40 | 1.70 | 131.70 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 194.2 + 0.4; price 5.40 + 1.70; quantity target 131.7; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=195, price=7.00, quantity=40 |
| 3 | SpotBroker | heuristic | 194.17 | 4.96 | 4.90 | 0.41 | 91.19 | inventory_guard lifted price under volatility; inventory target capped quantity | forecast 194.2 + 5.0; price 4.90 + 0.41; quantity target 91.2; risk gate inventory_guard lifted price under volatility; inventory target capped quantity; final forecast=200, price=5.60, quantity=60 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Conclusion Notes

- **Winner:** `PremiumCloud` ends with cumulative profit `1528.78`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.97`.
- **Market fulfillment:** the run sells `2284.45` units against `2298.00` true demand for a fulfillment ratio of `99.41%`.
- **Operational stress:** peer transfers total `0.00` units, customer reallocation totals `49.18`, final SLA backlog is `0.00`, with `9` dump flags and `1` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
