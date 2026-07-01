# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | price_war | 12 | llm | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit | Price Pressure Cost |
| --- | --- | --- | --- | --- | --- |
| 2298 | 2270.57 | 0.99 | 5.61 | 2850.31 | 237.94 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Price Pressure Cost | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 959.13 | 79.93 | 6.33 | 4.60 | 1381.75 | 0.99 | 3.42 | 0.00 | 149.62 | 10 | 0 | 0.00 | 0.64 | 19.42 |
| PremiumCloud | premium | 1128.92 | 94.08 | 5.67 | 6.75 | 309.67 | 1.00 | 0.00 | 31.67 | 4.93 | 0 | 0 | 3.01 | 0.84 | 0.00 |
| SpotBroker | spot | 762.26 | 63.52 | 4.25 | 5.47 | 579.15 | 0.99 | 28.24 | 0.00 | 83.39 | 0 | 1 | 17.79 | 0.81 | 8.01 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 181.00 | 5.07 | 462.23 | 0.00 | 12.70 | 33.40 | 0.00 |
| 1 | 197 | 195 | 197.00 | 5.20 | 178.48 | 0.00 | 6.73 | 33.68 | 0.00 |
| 2 | 198 | 197 | 189.99 | 5.40 | 251.67 | 8.01 | 8.82 | 5.86 | 1.26 |
| 3 | 202 | 204 | 201.65 | 5.53 | 168.42 | 0.35 | 0.00 | 1.41 | 0.04 |
| 4 | 193 | 194 | 188.88 | 5.67 | 254.47 | 4.12 | 0.00 | 1.57 | 0.45 |
| 5 | 182 | 183 | 181.55 | 5.67 | 192.92 | 0.45 | 0.00 | 3.81 | 0.05 |
| 6 | 171 | 175 | 170.95 | 5.67 | 223.96 | 0.05 | 0.00 | 4.14 | 0.01 |
| 7 | 194 | 196 | 193.99 | 5.73 | 243.99 | 0.01 | 3.42 | 4.01 | 0.00 |
| 8 | 196 | 187 | 194.73 | 5.73 | 172.13 | 1.27 | 0.00 | 6.41 | 0.14 |
| 9 | 200 | 198 | 196.58 | 5.80 | 273.44 | 3.42 | 0.00 | 14.43 | 0.40 |
| 10 | 198 | 198 | 192.99 | 5.87 | 227.40 | 5.01 | 0.00 | 17.90 | 0.59 |
| 11 | 186 | 183 | 181.26 | 5.93 | 201.19 | 4.74 | 0.00 | 14.50 | 0.53 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `price_war`, `PremiumCloud` ends first with cumulative profit `1128.92` and reputation `83.70%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `141.13` units and leaves final SLA backlog `0.53`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `31.67` units while average forecast error is `5.42`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 2 | 198 | 189.99 | shortage=8.01; transfer=8.82; dump_flags=1; default_flags=1 |
| 1 | 197 | 197.00 | transfer=6.73; dump_flags=1 |
| 10 | 198 | 192.99 | shortage=5.01; dump_flags=1 |
| 11 | 186 | 181.26 | shortage=4.74; dump_flags=1 |
| 4 | 193 | 188.88 | shortage=4.12; dump_flags=1 |
| 7 | 194 | 193.99 | shortage=0.01; transfer=3.42; dump_flags=1 |
| 9 | 200 | 196.58 | shortage=3.42; dump_flags=1 |
| 0 | 181 | 181.00 | transfer=12.70 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm | 184.00 | 0.00 | 4.60 | 0.00 | 80.00 | inventory target capped quantity | forecast 184.0 + 0.0; price 4.60 + 0.00; quantity target 80.0; risk gate inventory target capped quantity; final forecast=184, price=4.60, quantity=70 |
| 0 | PremiumCloud | llm | 184.00 | -4.00 | 6.80 | -0.80 | 60.00 | inventory target capped quantity | forecast 184.0 + -4.0; price 6.80 + -0.80; quantity target 60.0; risk gate inventory target capped quantity; final forecast=180, price=6.00, quantity=20 |
| 0 | SpotBroker | llm | 184.00 | -4.00 | 5.00 | -0.40 | 20.00 | none | forecast 184.0 + -4.0; price 5.00 + -0.40; quantity target 20.0; risk gate none; final forecast=180, price=4.60, quantity=20 |
| 1 | Hyperscaler | llm | 184.00 | 22.00 | 4.60 | 0.00 | 120.00 | none | forecast 184.0 + 22.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=206, price=4.60, quantity=120 |
| 1 | PremiumCloud | llm | 184.00 | 6.00 | 6.80 | -0.60 | 40.00 | inventory target capped quantity | forecast 184.0 + 6.0; price 6.80 + -0.60; quantity target 40.0; risk gate inventory target capped quantity; final forecast=190, price=6.20, quantity=40 |
| 1 | SpotBroker | llm | 184.00 | 16.00 | 5.00 | -0.20 | 40.00 | none | forecast 184.0 + 16.0; price 5.00 + -0.20; quantity target 40.0; risk gate none; final forecast=200, price=4.80, quantity=40 |
| 2 | Hyperscaler | llm | 198.00 | 2.00 | 4.60 | 0.00 | 120.00 | inventory target capped quantity | forecast 198.0 + 2.0; price 4.60 + 0.00; quantity target 120.0; risk gate inventory target capped quantity; final forecast=200, price=4.60, quantity=110 |
| 2 | PremiumCloud | llm | 193.00 | 2.00 | 7.00 | -0.60 | 30.00 | none | forecast 193.0 + 2.0; price 7.00 + -0.60; quantity target 30.0; risk gate none; final forecast=195, price=6.40, quantity=30 |
| 2 | SpotBroker | llm | 200.00 | 5.00 | 5.20 | -0.20 | 40.00 | inventory_guard lifted price under volatility | forecast 200.0 + 5.0; price 5.20 + -0.20; quantity target 40.0; risk gate inventory_guard lifted price under volatility; final forecast=205, price=5.20, quantity=40 |
| 3 | Hyperscaler | llm | 198.00 | 12.00 | 4.60 | 0.00 | 120.00 | none | forecast 198.0 + 12.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=210, price=4.60, quantity=120 |
| 3 | PremiumCloud | llm | 195.00 | 5.00 | 7.00 | -0.40 | 40.00 | none | forecast 195.0 + 5.0; price 7.00 + -0.40; quantity target 40.0; risk gate none; final forecast=200, price=6.60, quantity=40 |
| 3 | SpotBroker | llm | 200.00 | 8.00 | 5.20 | 0.20 | 70.00 | inventory target capped quantity | forecast 200.0 + 8.0; price 5.20 + 0.20; quantity target 70.0; risk gate inventory target capped quantity; final forecast=208, price=5.40, quantity=60 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Conclusion Notes

- **Winner:** `PremiumCloud` ends with cumulative profit `1128.92`, the highest value in this run.
- **Service leader:** `PremiumCloud` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.75`.
- **Market fulfillment:** the run sells `2270.57` units against `2298.00` true demand for a fulfillment ratio of `98.81%`.
- **Operational stress:** peer transfers total `31.67` units, customer reallocation totals `141.13`, final SLA backlog is `0.53`, with `10` dump flags and `1` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
