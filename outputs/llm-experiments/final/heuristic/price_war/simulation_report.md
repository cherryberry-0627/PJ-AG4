# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | price_war | 12 | heuristic | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit | Price Pressure Cost |
| --- | --- | --- | --- | --- | --- |
| 2298 | 2281.61 | 0.99 | 5.71 | 2708.40 | 227.50 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Price Pressure Cost | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 942.15 | 78.51 | 9.42 | 4.60 | 1406.58 | 0.99 | 1.33 | 0.00 | 159.64 | 11 | 0 | 0.00 | 0.63 | 15.25 |
| PremiumCloud | premium | 934.15 | 77.85 | 9.92 | 6.97 | 259.76 | 1.00 | 0.00 | 13.85 | 3.49 | 0 | 0 | 15.63 | 0.83 | 0.00 |
| SpotBroker | spot | 832.10 | 69.34 | 9.92 | 5.57 | 615.27 | 1.00 | 13.85 | 1.33 | 64.38 | 0 | 0 | 21.26 | 0.85 | 1.14 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 180.00 | 5.47 | 522.67 | 1.00 | 12.63 | 7.45 | 0.14 |
| 1 | 197 | 195 | 196.86 | 5.47 | 113.63 | 0.14 | 1.22 | 11.75 | 0.02 |
| 2 | 198 | 197 | 198.00 | 5.67 | 214.32 | 0.00 | 0.00 | 0.00 | 0.00 |
| 3 | 202 | 204 | 200.40 | 5.73 | 240.25 | 1.60 | 0.00 | 7.70 | 0.18 |
| 4 | 193 | 194 | 191.86 | 5.73 | 155.70 | 1.14 | 0.00 | 4.75 | 0.13 |
| 5 | 182 | 183 | 182.00 | 5.73 | 176.57 | 0.00 | 0.00 | 0.00 | 0.00 |
| 6 | 171 | 175 | 171.00 | 5.73 | 119.58 | 0.00 | 0.00 | 0.00 | 0.00 |
| 7 | 194 | 196 | 191.41 | 5.80 | 329.40 | 2.59 | 0.00 | 11.34 | 0.29 |
| 8 | 196 | 187 | 193.10 | 5.80 | 210.89 | 2.90 | 0.00 | 11.57 | 0.33 |
| 9 | 200 | 198 | 196.57 | 5.80 | 235.37 | 3.43 | 0.00 | 13.83 | 0.39 |
| 10 | 198 | 198 | 194.77 | 5.80 | 220.61 | 3.23 | 0.00 | 12.72 | 0.37 |
| 11 | 186 | 183 | 185.63 | 5.80 | 169.41 | 0.37 | 1.33 | 6.00 | 0.04 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `price_war`, `Hyperscaler` ends first with cumulative profit `942.15` and reputation `62.66%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `87.11` units and leaves final SLA backlog `0.04`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `15.19` units while average forecast error is `9.75`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 0 | 181 | 180.00 | shortage=1.00; transfer=12.63 |
| 9 | 200 | 196.57 | shortage=3.43; dump_flags=1 |
| 10 | 198 | 194.77 | shortage=3.23; dump_flags=1 |
| 8 | 196 | 193.10 | shortage=2.90; dump_flags=1 |
| 7 | 194 | 191.41 | shortage=2.59; dump_flags=1 |
| 11 | 186 | 185.63 | shortage=0.37; transfer=1.33; dump_flags=1 |
| 3 | 202 | 200.40 | shortage=1.60; dump_flags=1 |
| 1 | 197 | 196.86 | shortage=0.14; transfer=1.22; dump_flags=1 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | heuristic | 184.00 | 0.00 | 4.60 | -0.57 | 262.58 | inventory target capped quantity | forecast 184.0 + 0.0; price 4.60 + -0.57; quantity target 262.6; risk gate inventory target capped quantity; final forecast=184, price=4.60, quantity=70 |
| 0 | PremiumCloud | heuristic | 184.00 | 0.09 | 5.40 | 1.30 | 114.08 | inventory target capped quantity | forecast 184.0 + 0.1; price 5.40 + 1.30; quantity target 114.1; risk gate inventory target capped quantity; final forecast=184, price=6.80, quantity=0 |
| 0 | SpotBroker | heuristic | 184.00 | 0.00 | 4.90 | 0.12 | 73.60 | inventory target capped quantity | forecast 184.0 + 0.0; price 4.90 + 0.12; quantity target 73.6; risk gate inventory target capped quantity; final forecast=184, price=5.00, quantity=30 |
| 1 | Hyperscaler | heuristic | 184.00 | 0.00 | 4.60 | -0.55 | 304.68 | none | forecast 184.0 + 0.0; price 4.60 + -0.55; quantity target 304.7; risk gate none; final forecast=184, price=4.60, quantity=120 |
| 1 | PremiumCloud | heuristic | 184.00 | 0.09 | 5.40 | 1.32 | 124.88 | inventory target capped quantity | forecast 184.0 + 0.1; price 5.40 + 1.32; quantity target 124.9; risk gate inventory target capped quantity; final forecast=184, price=6.80, quantity=40 |
| 1 | SpotBroker | heuristic | 184.00 | 0.00 | 4.90 | 0.04 | 78.60 | inventory target capped quantity | forecast 184.0 + 0.0; price 4.90 + 0.04; quantity target 78.6; risk gate inventory target capped quantity; final forecast=184, price=5.00, quantity=60 |
| 2 | Hyperscaler | heuristic | 191.33 | 5.28 | 4.60 | -0.88 | 315.87 | none | forecast 191.3 + 5.3; price 4.60 + -0.88; quantity target 315.9; risk gate none; final forecast=198, price=4.60, quantity=120 |
| 2 | PremiumCloud | heuristic | 191.33 | 0.70 | 5.40 | 1.72 | 120.64 | inventory target capped quantity | forecast 191.3 + 0.7; price 5.40 + 1.72; quantity target 120.6; risk gate inventory target capped quantity; final forecast=193, price=7.00, quantity=20 |
| 2 | SpotBroker | heuristic | 191.33 | 7.48 | 4.90 | 0.38 | 92.70 | inventory_guard lifted price under volatility; inventory target capped quantity | forecast 191.3 + 7.5; price 4.90 + 0.38; quantity target 92.7; risk gate inventory_guard lifted price under volatility; inventory target capped quantity; final forecast=200, price=5.40, quantity=60 |
| 3 | Hyperscaler | heuristic | 194.17 | 3.27 | 4.60 | -0.90 | 320.85 | none | forecast 194.2 + 3.3; price 4.60 + -0.90; quantity target 320.9; risk gate none; final forecast=198, price=4.60, quantity=120 |
| 3 | PremiumCloud | heuristic | 194.17 | 0.38 | 5.40 | 1.74 | 122.71 | inventory target capped quantity | forecast 194.2 + 0.4; price 5.40 + 1.74; quantity target 122.7; risk gate inventory target capped quantity; final forecast=195, price=7.00, quantity=20 |
| 3 | SpotBroker | heuristic | 194.17 | 4.96 | 4.90 | 0.41 | 91.01 | inventory_guard lifted price under volatility; inventory target capped quantity | forecast 194.2 + 5.0; price 4.90 + 0.41; quantity target 91.0; risk gate inventory_guard lifted price under volatility; inventory target capped quantity; final forecast=200, price=5.60, quantity=60 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Conclusion Notes

- **Winner:** `Hyperscaler` ends with cumulative profit `942.15`, the highest value in this run.
- **Service leader:** `PremiumCloud` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.97`.
- **Market fulfillment:** the run sells `2281.61` units against `2298.00` true demand for a fulfillment ratio of `99.29%`.
- **Operational stress:** peer transfers total `15.19` units, customer reallocation totals `87.11`, final SLA backlog is `0.04`, with `11` dump flags and `0` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
