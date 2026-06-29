# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | no_transfer | 12 | llm-context | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit | Price Pressure Cost |
| --- | --- | --- | --- | --- | --- |
| 2298 | 2271.13 | 0.99 | 5.58 | 3522.43 | 0.00 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Price Pressure Cost | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 1013.15 | 84.43 | 8.75 | 4.60 | 1274.85 | 1.00 | 0.00 | 0.00 | 0.00 | 8 | 0 | 5.64 | 0.69 | 0.00 |
| PremiumCloud | premium | 1520.20 | 126.68 | 7.08 | 6.60 | 464.20 | 0.96 | 0.00 | 0.00 | 0.00 | 0 | 2 | 0.00 | 0.95 | 20.08 |
| SpotBroker | spot | 989.08 | 82.42 | 3.17 | 5.55 | 532.08 | 0.99 | 0.00 | 0.00 | 0.00 | 0 | 0 | 0.00 | 0.89 | 6.79 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 170.00 | 5.33 | 522.35 | 11.00 | 0.00 | 21.94 | 5.84 |
| 1 | 197 | 195 | 191.25 | 5.47 | 166.73 | 5.75 | 0.00 | 1.01 | 3.10 |
| 2 | 198 | 197 | 196.49 | 5.53 | 328.07 | 1.51 | 0.00 | 2.28 | 0.65 |
| 3 | 202 | 204 | 201.35 | 5.60 | 302.70 | 0.65 | 0.00 | 1.21 | 0.30 |
| 4 | 193 | 194 | 192.70 | 5.67 | 251.42 | 0.30 | 0.00 | 6.82 | 0.15 |
| 5 | 182 | 183 | 179.76 | 5.60 | 226.93 | 2.24 | 0.00 | 6.49 | 0.79 |
| 6 | 171 | 175 | 169.04 | 5.60 | 269.66 | 1.96 | 0.00 | 4.73 | 0.65 |
| 7 | 194 | 196 | 193.35 | 5.60 | 265.78 | 0.65 | 0.00 | 3.26 | 0.19 |
| 8 | 196 | 187 | 195.81 | 5.67 | 359.70 | 0.19 | 0.00 | 13.05 | 0.07 |
| 9 | 200 | 198 | 198.63 | 5.67 | 245.86 | 1.37 | 0.00 | 4.74 | 0.78 |
| 10 | 198 | 198 | 197.22 | 5.67 | 324.29 | 0.78 | 0.00 | 12.35 | 0.46 |
| 11 | 186 | 183 | 185.54 | 5.60 | 258.94 | 0.46 | 0.00 | 13.68 | 0.25 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `no_transfer`, `PremiumCloud` ends first with cumulative profit `1520.20` and reputation `95.17%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `91.58` units and leaves final SLA backlog `0.25`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `0.00` units while average forecast error is `6.33`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 1 | 197 | 191.25 | shortage=5.75; dump_flags=1; default_flags=1 |
| 0 | 181 | 170.00 | shortage=11.00; default_flags=1 |
| 5 | 182 | 179.76 | shortage=2.24; dump_flags=1 |
| 9 | 200 | 198.63 | shortage=1.37; dump_flags=1 |
| 10 | 198 | 197.22 | shortage=0.78; dump_flags=1 |
| 3 | 202 | 201.35 | shortage=0.65; dump_flags=1 |
| 7 | 194 | 193.35 | shortage=0.65; dump_flags=1 |
| 11 | 186 | 185.54 | shortage=0.46; dump_flags=1 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm-context | 184.00 | 0.00 | 4.60 | 0.00 | 80.00 | inventory target capped quantity | forecast 184.0 + 0.0; price 4.60 + 0.00; quantity target 80.0; risk gate inventory target capped quantity; final forecast=184, price=4.60, quantity=70 |
| 0 | PremiumCloud | llm-context | 184.00 | -24.00 | 6.80 | -0.20 | 40.00 | inventory target capped quantity | forecast 184.0 + -24.0; price 6.80 + -0.20; quantity target 40.0; risk gate inventory target capped quantity; final forecast=160, price=6.60, quantity=0 |
| 0 | SpotBroker | llm-context | 184.00 | -4.00 | 5.00 | -0.20 | 20.00 | none | forecast 184.0 + -4.0; price 5.00 + -0.20; quantity target 20.0; risk gate none; final forecast=180, price=4.80, quantity=20 |
| 1 | Hyperscaler | llm-context | 184.00 | 21.00 | 4.60 | 0.00 | 120.00 | none | forecast 184.0 + 21.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=205, price=4.60, quantity=120 |
| 1 | PremiumCloud | llm-context | 184.00 | 6.00 | 6.60 | 0.00 | 50.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 184.0 + 6.0; price 6.60 + 0.00; quantity target 50.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=190, price=6.60, quantity=40 |
| 1 | SpotBroker | llm-context | 184.00 | 16.00 | 5.00 | 0.20 | 60.00 | none | forecast 184.0 + 16.0; price 5.00 + 0.20; quantity target 60.0; risk gate none; final forecast=200, price=5.20, quantity=60 |
| 2 | Hyperscaler | llm-context | 198.00 | 12.00 | 4.60 | 0.00 | 100.00 | none | forecast 198.0 + 12.0; price 4.60 + 0.00; quantity target 100.0; risk gate none; final forecast=210, price=4.60, quantity=100 |
| 2 | PremiumCloud | llm-context | 193.00 | 2.00 | 7.00 | -0.40 | 50.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 193.0 + 2.0; price 7.00 + -0.40; quantity target 50.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=195, price=6.60, quantity=40 |
| 2 | SpotBroker | llm-context | 200.00 | 0.00 | 5.40 | 0.00 | 50.00 | none | forecast 200.0 + 0.0; price 5.40 + 0.00; quantity target 50.0; risk gate none; final forecast=200, price=5.40, quantity=50 |
| 3 | Hyperscaler | llm-context | 198.00 | 17.00 | 4.60 | 0.00 | 110.00 | none | forecast 198.0 + 17.0; price 4.60 + 0.00; quantity target 110.0; risk gate none; final forecast=215, price=4.60, quantity=110 |
| 3 | PremiumCloud | llm-context | 195.00 | 5.00 | 7.00 | -0.40 | 40.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 195.0 + 5.0; price 7.00 + -0.40; quantity target 40.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=200, price=6.60, quantity=40 |
| 3 | SpotBroker | llm-context | 200.00 | 5.00 | 5.40 | 0.20 | 50.00 | none | forecast 200.0 + 5.0; price 5.40 + 0.20; quantity target 50.0; risk gate none; final forecast=205, price=5.60, quantity=50 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Conclusion Notes

- **Winner:** `PremiumCloud` ends with cumulative profit `1520.20`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.60`.
- **Market fulfillment:** the run sells `2271.13` units against `2298.00` true demand for a fulfillment ratio of `98.83%`.
- **Operational stress:** peer transfers total `0.00` units, customer reallocation totals `91.58`, final SLA backlog is `0.25`, with `8` dump flags and `2` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
