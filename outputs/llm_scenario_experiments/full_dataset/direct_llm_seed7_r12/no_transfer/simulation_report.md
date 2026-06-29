# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | no_transfer | 12 | llm | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit | Price Pressure Cost |
| --- | --- | --- | --- | --- | --- |
| 2298 | 2271.36 | 0.99 | 5.59 | 3434.63 | 0.00 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Price Pressure Cost | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 919.26 | 76.60 | 6.58 | 4.60 | 1246.29 | 1.00 | 0.00 | 0.00 | 0.00 | 7 | 0 | 10.45 | 0.75 | 0.00 |
| PremiumCloud | premium | 1477.48 | 123.12 | 5.25 | 6.60 | 450.29 | 0.95 | 0.00 | 0.00 | 0.00 | 0 | 2 | 0.00 | 0.95 | 25.50 |
| SpotBroker | spot | 1037.89 | 86.49 | 4.25 | 5.58 | 574.79 | 1.00 | 0.00 | 0.00 | 0.00 | 0 | 0 | 0.00 | 0.90 | 1.13 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 170.00 | 5.33 | 522.35 | 11.00 | 0.00 | 21.94 | 5.84 |
| 1 | 197 | 195 | 191.25 | 5.47 | 166.73 | 5.75 | 0.00 | 1.01 | 3.10 |
| 2 | 198 | 197 | 196.15 | 5.60 | 238.31 | 1.85 | 0.00 | 0.00 | 0.93 |
| 3 | 202 | 204 | 200.49 | 5.67 | 309.40 | 1.51 | 0.00 | 2.03 | 0.79 |
| 4 | 193 | 194 | 192.57 | 5.60 | 301.63 | 0.43 | 0.00 | 0.00 | 0.22 |
| 5 | 182 | 183 | 182.00 | 5.60 | 211.70 | 0.00 | 0.00 | 0.00 | 0.00 |
| 6 | 171 | 175 | 171.00 | 5.60 | 230.69 | 0.00 | 0.00 | 0.00 | 0.00 |
| 7 | 194 | 196 | 192.06 | 5.67 | 282.13 | 1.94 | 0.00 | 6.91 | 1.18 |
| 8 | 196 | 187 | 194.16 | 5.60 | 269.79 | 1.84 | 0.00 | 2.19 | 0.99 |
| 9 | 200 | 198 | 197.69 | 5.67 | 291.92 | 2.31 | 0.00 | 4.45 | 1.30 |
| 10 | 198 | 198 | 198.00 | 5.67 | 231.04 | 0.00 | 0.00 | 0.00 | 0.00 |
| 11 | 186 | 183 | 186.00 | 5.67 | 378.95 | 0.00 | 0.00 | 14.02 | 0.00 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `no_transfer`, `PremiumCloud` ends first with cumulative profit `1477.48` and reputation `94.83%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `52.54` units and leaves final SLA backlog `0.00`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `0.00` units while average forecast error is `5.36`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 1 | 197 | 191.25 | shortage=5.75; dump_flags=1; default_flags=1 |
| 0 | 181 | 170.00 | shortage=11.00; default_flags=1 |
| 9 | 200 | 197.69 | shortage=2.31; dump_flags=1 |
| 7 | 194 | 192.06 | shortage=1.94; dump_flags=1 |
| 2 | 198 | 196.15 | shortage=1.85; dump_flags=1 |
| 8 | 196 | 194.16 | shortage=1.84; dump_flags=1 |
| 4 | 193 | 192.57 | shortage=0.43; dump_flags=1 |
| 10 | 198 | 198.00 | dump_flags=1 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm | 184.00 | 0.00 | 4.60 | 0.00 | 80.00 | inventory target capped quantity | forecast 184.0 + 0.0; price 4.60 + 0.00; quantity target 80.0; risk gate inventory target capped quantity; final forecast=184, price=4.60, quantity=70 |
| 0 | PremiumCloud | llm | 184.00 | -4.00 | 6.80 | -0.20 | 30.00 | inventory target capped quantity | forecast 184.0 + -4.0; price 6.80 + -0.20; quantity target 30.0; risk gate inventory target capped quantity; final forecast=180, price=6.60, quantity=0 |
| 0 | SpotBroker | llm | 184.00 | 0.00 | 5.00 | -0.20 | 20.00 | none | forecast 184.0 + 0.0; price 5.00 + -0.20; quantity target 20.0; risk gate none; final forecast=184, price=4.80, quantity=20 |
| 1 | Hyperscaler | llm | 184.00 | 22.00 | 4.60 | 0.00 | 120.00 | none | forecast 184.0 + 22.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=206, price=4.60, quantity=120 |
| 1 | PremiumCloud | llm | 184.00 | 6.00 | 6.60 | 0.00 | 50.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 184.0 + 6.0; price 6.60 + 0.00; quantity target 50.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=190, price=6.60, quantity=40 |
| 1 | SpotBroker | llm | 184.00 | 21.00 | 5.00 | 0.20 | 60.00 | none | forecast 184.0 + 21.0; price 5.00 + 0.20; quantity target 60.0; risk gate none; final forecast=205, price=5.20, quantity=60 |
| 2 | Hyperscaler | llm | 198.00 | 7.00 | 4.60 | 0.00 | 120.00 | inventory target capped quantity | forecast 198.0 + 7.0; price 4.60 + 0.00; quantity target 120.0; risk gate inventory target capped quantity; final forecast=205, price=4.60, quantity=120 |
| 2 | PremiumCloud | llm | 193.00 | 5.00 | 7.00 | -0.40 | 40.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 193.0 + 5.0; price 7.00 + -0.40; quantity target 40.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=198, price=6.60, quantity=40 |
| 2 | SpotBroker | llm | 200.00 | 0.00 | 5.40 | 0.20 | 50.00 | none | forecast 200.0 + 0.0; price 5.40 + 0.20; quantity target 50.0; risk gate none; final forecast=200, price=5.60, quantity=50 |
| 3 | Hyperscaler | llm | 198.00 | 17.00 | 4.60 | 0.00 | 100.00 | none | forecast 198.0 + 17.0; price 4.60 + 0.00; quantity target 100.0; risk gate none; final forecast=215, price=4.60, quantity=100 |
| 3 | PremiumCloud | llm | 195.00 | 5.00 | 7.00 | -0.40 | 70.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 195.0 + 5.0; price 7.00 + -0.40; quantity target 70.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=200, price=6.60, quantity=40 |
| 3 | SpotBroker | llm | 200.00 | 10.00 | 5.40 | 0.40 | 60.00 | inventory target capped quantity | forecast 200.0 + 10.0; price 5.40 + 0.40; quantity target 60.0; risk gate inventory target capped quantity; final forecast=210, price=5.80, quantity=60 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Conclusion Notes

- **Winner:** `PremiumCloud` ends with cumulative profit `1477.48`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.60`.
- **Market fulfillment:** the run sells `2271.36` units against `2298.00` true demand for a fulfillment ratio of `98.84%`.
- **Operational stress:** peer transfers total `0.00` units, customer reallocation totals `52.54`, final SLA backlog is `0.00`, with `7` dump flags and `2` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
