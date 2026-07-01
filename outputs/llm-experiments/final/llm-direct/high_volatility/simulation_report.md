# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | high_volatility | 12 | llm | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit | Price Pressure Cost |
| --- | --- | --- | --- | --- | --- |
| 2279 | 2252.63 | 0.99 | 5.58 | 3332.45 | 0.00 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Price Pressure Cost | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 926.01 | 77.17 | 10.33 | 4.60 | 1255.50 | 1.00 | 0.00 | 0.58 | 0.00 | 7 | 0 | 21.48 | 0.64 | 0.00 |
| PremiumCloud | premium | 1502.49 | 125.21 | 8.67 | 6.60 | 462.70 | 0.97 | 6.04 | 0.00 | 0.00 | 0 | 1 | 0.00 | 0.91 | 13.87 |
| SpotBroker | spot | 903.94 | 75.33 | 5.92 | 5.53 | 534.43 | 0.98 | 0.00 | 5.46 | 0.00 | 0 | 1 | 12.50 | 0.87 | 12.50 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 179 | 184 | 179.00 | 5.27 | 531.64 | 0.00 | 0.00 | 35.98 | 0.00 |
| 1 | 200 | 197 | 200.00 | 5.40 | 216.66 | 0.00 | 0.00 | 18.26 | 0.00 |
| 2 | 195 | 193 | 179.22 | 5.53 | 263.03 | 15.78 | 0.00 | 13.67 | 6.42 |
| 3 | 211 | 215 | 207.44 | 5.60 | 272.43 | 3.56 | 3.38 | 3.61 | 1.99 |
| 4 | 202 | 204 | 200.01 | 5.67 | 257.74 | 1.99 | 1.36 | 4.90 | 1.14 |
| 5 | 184 | 186 | 182.86 | 5.67 | 169.85 | 1.14 | 0.58 | 1.99 | 0.61 |
| 6 | 155 | 164 | 155.00 | 5.60 | 196.95 | 0.00 | 0.00 | 0.00 | 0.00 |
| 7 | 193 | 198 | 191.45 | 5.60 | 420.46 | 1.55 | 0.00 | 6.21 | 0.52 |
| 8 | 186 | 169 | 186.00 | 5.60 | 230.51 | 0.00 | 0.00 | 0.00 | 0.00 |
| 9 | 191 | 186 | 191.00 | 5.67 | 306.02 | 0.00 | 0.72 | 2.41 | 0.00 |
| 10 | 197 | 197 | 196.01 | 5.67 | 240.66 | 0.99 | 0.00 | 3.32 | 0.55 |
| 11 | 186 | 180 | 184.64 | 5.67 | 226.49 | 1.36 | 0.00 | 2.67 | 0.74 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `high_volatility`, `PremiumCloud` ends first with cumulative profit `1502.49` and reputation `90.88%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `93.03` units and leaves final SLA backlog `0.74`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `6.04` units while average forecast error is `8.31`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 2 | 195 | 179.22 | shortage=15.78; default_flags=2 |
| 3 | 211 | 207.44 | shortage=3.56; transfer=3.38; dump_flags=1 |
| 4 | 202 | 200.01 | shortage=1.99; transfer=1.36; dump_flags=1 |
| 5 | 184 | 182.86 | shortage=1.14; transfer=0.58; dump_flags=1 |
| 11 | 186 | 184.64 | shortage=1.36; dump_flags=1 |
| 10 | 197 | 196.01 | shortage=0.99; dump_flags=1 |
| 1 | 200 | 200.00 | dump_flags=1 |
| 8 | 186 | 186.00 | dump_flags=1 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm | 184.00 | 6.00 | 4.60 | 0.00 | 80.00 | inventory target capped quantity | forecast 184.0 + 6.0; price 4.60 + 0.00; quantity target 80.0; risk gate inventory target capped quantity; final forecast=190, price=4.60, quantity=80 |
| 0 | PremiumCloud | llm | 184.00 | -4.00 | 6.80 | -0.20 | 30.00 | inventory target capped quantity | forecast 184.0 + -4.0; price 6.80 + -0.20; quantity target 30.0; risk gate inventory target capped quantity; final forecast=180, price=6.60, quantity=0 |
| 0 | SpotBroker | llm | 184.00 | -4.00 | 5.00 | -0.40 | 20.00 | none | forecast 184.0 + -4.0; price 5.00 + -0.40; quantity target 20.0; risk gate none; final forecast=180, price=4.60, quantity=20 |
| 1 | Hyperscaler | llm | 184.00 | 26.00 | 4.60 | 0.00 | 120.00 | none | forecast 184.0 + 26.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=210, price=4.60, quantity=120 |
| 1 | PremiumCloud | llm | 184.00 | 11.00 | 6.80 | -0.20 | 40.00 | inventory target capped quantity | forecast 184.0 + 11.0; price 6.80 + -0.20; quantity target 40.0; risk gate inventory target capped quantity; final forecast=195, price=6.60, quantity=40 |
| 1 | SpotBroker | llm | 184.00 | 21.00 | 5.00 | 0.00 | 50.00 | none | forecast 184.0 + 21.0; price 5.00 + 0.00; quantity target 50.0; risk gate none; final forecast=205, price=5.00, quantity=50 |
| 2 | Hyperscaler | llm | 200.00 | 0.00 | 4.60 | 0.00 | 100.00 | none | forecast 200.0 + 0.0; price 4.60 + 0.00; quantity target 100.0; risk gate none; final forecast=200, price=4.60, quantity=100 |
| 2 | PremiumCloud | llm | 195.00 | -5.00 | 7.00 | -0.40 | 30.00 | none | forecast 195.0 + -5.0; price 7.00 + -0.40; quantity target 30.0; risk gate none; final forecast=190, price=6.60, quantity=30 |
| 2 | SpotBroker | llm | 203.00 | -13.00 | 5.40 | -0.20 | 40.00 | inventory_guard lifted price under volatility | forecast 203.0 + -13.0; price 5.40 + -0.20; quantity target 40.0; risk gate inventory_guard lifted price under volatility; final forecast=190, price=5.40, quantity=40 |
| 3 | Hyperscaler | llm | 195.00 | 25.00 | 4.60 | 0.00 | 120.00 | none | forecast 195.0 + 25.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=220, price=4.60, quantity=120 |
| 3 | PremiumCloud | llm | 193.00 | 7.00 | 7.00 | -0.40 | 80.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 193.0 + 7.0; price 7.00 + -0.40; quantity target 80.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=200, price=6.60, quantity=40 |
| 3 | SpotBroker | llm | 197.00 | 18.00 | 5.40 | 0.20 | 70.00 | inventory target capped quantity | forecast 197.0 + 18.0; price 5.40 + 0.20; quantity target 70.0; risk gate inventory target capped quantity; final forecast=215, price=5.60, quantity=60 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Conclusion Notes

- **Winner:** `PremiumCloud` ends with cumulative profit `1502.49`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.60`.
- **Market fulfillment:** the run sells `2252.63` units against `2279.00` true demand for a fulfillment ratio of `98.84%`.
- **Operational stress:** peer transfers total `6.04` units, customer reallocation totals `93.03`, final SLA backlog is `0.74`, with `7` dump flags and `2` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
