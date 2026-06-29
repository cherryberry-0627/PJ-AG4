# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | baseline | 12 | llm | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit | Price Pressure Cost |
| --- | --- | --- | --- | --- | --- |
| 2298 | 2287.55 | 1.00 | 5.63 | 3372.66 | 0.00 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Price Pressure Cost | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 893.71 | 74.48 | 8.00 | 4.60 | 1281.01 | 1.00 | 0.00 | 7.12 | 0.00 | 9 | 0 | 27.89 | 0.72 | 0.00 |
| PremiumCloud | premium | 1484.81 | 123.73 | 6.42 | 6.78 | 425.73 | 0.98 | 7.12 | 0.00 | 0.00 | 0 | 0 | 0.00 | 0.95 | 10.45 |
| SpotBroker | spot | 994.14 | 82.84 | 3.67 | 5.50 | 580.80 | 1.00 | 0.00 | 0.00 | 0.00 | 0 | 0 | 8.87 | 0.85 | 0.00 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 180.00 | 5.27 | 534.87 | 1.00 | 0.00 | 36.17 | 0.68 |
| 1 | 197 | 195 | 196.32 | 5.47 | 226.30 | 0.68 | 0.00 | 24.51 | 0.55 |
| 2 | 198 | 197 | 197.45 | 5.60 | 250.91 | 0.55 | 0.00 | 18.48 | 0.45 |
| 3 | 202 | 204 | 201.55 | 5.67 | 263.06 | 0.45 | 0.00 | 8.03 | 0.28 |
| 4 | 193 | 194 | 192.72 | 5.73 | 276.67 | 0.28 | 1.27 | 4.34 | 0.17 |
| 5 | 182 | 183 | 181.83 | 5.67 | 286.12 | 0.17 | 2.71 | 8.73 | 0.11 |
| 6 | 171 | 175 | 170.89 | 5.67 | 180.97 | 0.11 | 1.67 | 5.53 | 0.07 |
| 7 | 194 | 196 | 193.93 | 5.73 | 317.76 | 0.07 | 0.00 | 3.99 | 0.04 |
| 8 | 196 | 187 | 192.89 | 5.67 | 290.18 | 3.11 | 0.00 | 9.90 | 2.15 |
| 9 | 200 | 198 | 197.85 | 5.73 | 267.06 | 2.15 | 0.87 | 3.01 | 1.21 |
| 10 | 198 | 198 | 196.79 | 5.67 | 286.48 | 1.21 | 0.59 | 1.92 | 0.67 |
| 11 | 186 | 183 | 185.33 | 5.67 | 192.27 | 0.67 | 0.01 | 0.04 | 0.36 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `baseline`, `PremiumCloud` ends first with cumulative profit `1484.81` and reputation `95.16%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `124.63` units and leaves final SLA backlog `0.36`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `7.12` units while average forecast error is `6.03`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 9 | 200 | 197.85 | shortage=2.15; transfer=0.87; dump_flags=1 |
| 10 | 198 | 196.79 | shortage=1.21; transfer=0.59; dump_flags=1 |
| 6 | 171 | 170.89 | shortage=0.11; transfer=1.67; dump_flags=1 |
| 4 | 193 | 192.72 | shortage=0.28; transfer=1.27; dump_flags=1 |
| 11 | 186 | 185.33 | shortage=0.67; transfer=0.01; dump_flags=1 |
| 1 | 197 | 196.32 | shortage=0.68; dump_flags=1 |
| 2 | 198 | 197.45 | shortage=0.55; dump_flags=1 |
| 3 | 202 | 201.55 | shortage=0.45; dump_flags=1 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm | 184.00 | 6.00 | 4.60 | 0.00 | 80.00 | inventory target capped quantity | forecast 184.0 + 6.0; price 4.60 + 0.00; quantity target 80.0; risk gate inventory target capped quantity; final forecast=190, price=4.60, quantity=80 |
| 0 | PremiumCloud | llm | 184.00 | -4.00 | 6.80 | -0.20 | 50.00 | inventory target capped quantity | forecast 184.0 + -4.0; price 6.80 + -0.20; quantity target 50.0; risk gate inventory target capped quantity; final forecast=180, price=6.60, quantity=0 |
| 0 | SpotBroker | llm | 184.00 | -4.00 | 5.00 | -0.40 | 20.00 | none | forecast 184.0 + -4.0; price 5.00 + -0.40; quantity target 20.0; risk gate none; final forecast=180, price=4.60, quantity=20 |
| 1 | Hyperscaler | llm | 184.00 | 22.00 | 4.60 | 0.00 | 120.00 | none | forecast 184.0 + 22.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=206, price=4.60, quantity=120 |
| 1 | PremiumCloud | llm | 184.00 | 6.00 | 6.80 | 0.00 | 40.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 184.0 + 6.0; price 6.80 + 0.00; quantity target 40.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=190, price=6.80, quantity=30 |
| 1 | SpotBroker | llm | 184.00 | 21.00 | 5.00 | 0.00 | 50.00 | none | forecast 184.0 + 21.0; price 5.00 + 0.00; quantity target 50.0; risk gate none; final forecast=205, price=5.00, quantity=50 |
| 2 | Hyperscaler | llm | 198.00 | 7.00 | 4.60 | 0.00 | 120.00 | none | forecast 198.0 + 7.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=205, price=4.60, quantity=120 |
| 2 | PremiumCloud | llm | 193.00 | 3.00 | 7.00 | -0.20 | 30.00 | sla_guard reduced quantity under SLA/reputation pressure | forecast 193.0 + 3.0; price 7.00 + -0.20; quantity target 30.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; final forecast=196, price=6.80, quantity=30 |
| 2 | SpotBroker | llm | 200.00 | 0.00 | 5.40 | 0.00 | 50.00 | none | forecast 200.0 + 0.0; price 5.40 + 0.00; quantity target 50.0; risk gate none; final forecast=200, price=5.40, quantity=50 |
| 3 | Hyperscaler | llm | 198.00 | 14.00 | 4.60 | 0.00 | 120.00 | none | forecast 198.0 + 14.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=212, price=4.60, quantity=120 |
| 3 | PremiumCloud | llm | 195.00 | 3.00 | 7.00 | -0.20 | 40.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 195.0 + 3.0; price 7.00 + -0.20; quantity target 40.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=198, price=6.80, quantity=40 |
| 3 | SpotBroker | llm | 200.00 | 10.00 | 5.40 | 0.20 | 50.00 | none | forecast 200.0 + 10.0; price 5.40 + 0.20; quantity target 50.0; risk gate none; final forecast=210, price=5.60, quantity=50 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Conclusion Notes

- **Winner:** `PremiumCloud` ends with cumulative profit `1484.81`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.78`.
- **Market fulfillment:** the run sells `2287.55` units against `2298.00` true demand for a fulfillment ratio of `99.55%`.
- **Operational stress:** peer transfers total `7.12` units, customer reallocation totals `124.63`, final SLA backlog is `0.36`, with `9` dump flags and `0` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
