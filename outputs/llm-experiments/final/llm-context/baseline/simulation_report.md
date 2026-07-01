# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | baseline | 12 | llm-context | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit | Price Pressure Cost |
| --- | --- | --- | --- | --- | --- |
| 2298 | 2246.74 | 0.98 | 5.33 | 3173.89 | 0.00 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Price Pressure Cost | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 987.10 | 82.26 | 8.00 | 4.60 | 1246.07 | 1.00 | 0.00 | 3.75 | 0.00 | 6 | 0 | 10.40 | 0.73 | 0.00 |
| PremiumCloud | premium | 1375.91 | 114.66 | 5.50 | 5.98 | 531.41 | 0.96 | 2.43 | 1.24 | 0.00 | 0 | 3 | 0.00 | 0.88 | 20.84 |
| SpotBroker | spot | 810.88 | 67.57 | 3.92 | 5.42 | 469.26 | 0.94 | 2.70 | 0.13 | 0.00 | 0 | 2 | 0.00 | 0.90 | 30.42 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 181.00 | 5.07 | 514.14 | 0.00 | 0.00 | 21.33 | 0.00 |
| 1 | 197 | 195 | 177.65 | 5.20 | 207.17 | 19.35 | 0.00 | 34.22 | 5.01 |
| 2 | 198 | 197 | 184.99 | 5.33 | 204.69 | 13.01 | 0.00 | 27.17 | 7.48 |
| 3 | 202 | 204 | 192.52 | 5.40 | 242.89 | 9.48 | 2.43 | 15.91 | 5.56 |
| 4 | 193 | 194 | 187.50 | 5.33 | 180.07 | 5.50 | 1.46 | 4.94 | 2.46 |
| 5 | 182 | 183 | 180.18 | 5.33 | 222.99 | 1.82 | 0.00 | 5.98 | 0.59 |
| 6 | 171 | 175 | 170.41 | 5.33 | 248.96 | 0.59 | 1.24 | 4.31 | 0.19 |
| 7 | 194 | 196 | 194.00 | 5.40 | 259.41 | 0.00 | 0.00 | 0.00 | 0.00 |
| 8 | 196 | 187 | 194.99 | 5.40 | 300.57 | 1.01 | 0.00 | 3.46 | 0.32 |
| 9 | 200 | 198 | 199.68 | 5.40 | 275.49 | 0.32 | 0.00 | 9.71 | 0.12 |
| 10 | 198 | 198 | 197.88 | 5.40 | 217.12 | 0.12 | 0.00 | 13.08 | 0.04 |
| 11 | 186 | 183 | 185.96 | 5.40 | 300.39 | 0.04 | 0.00 | 9.42 | 0.02 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `baseline`, `PremiumCloud` ends first with cumulative profit `1375.91` and reputation `88.02%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `149.53` units and leaves final SLA backlog `0.02`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `5.12` units while average forecast error is `5.81`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 2 | 198 | 184.99 | shortage=13.01; dump_flags=1; default_flags=2 |
| 1 | 197 | 177.65 | shortage=19.35; dump_flags=1; default_flags=1 |
| 3 | 202 | 192.52 | shortage=9.48; transfer=2.43; dump_flags=1; default_flags=1 |
| 4 | 193 | 187.50 | shortage=5.50; transfer=1.46; dump_flags=1; default_flags=1 |
| 9 | 200 | 199.68 | shortage=0.32; dump_flags=1 |
| 10 | 198 | 197.88 | shortage=0.12; dump_flags=1 |
| 6 | 171 | 170.41 | shortage=0.59; transfer=1.24 |
| 5 | 182 | 180.18 | shortage=1.82 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm-context | 184.00 | 0.00 | 4.60 | 0.00 | 80.00 | inventory target capped quantity | forecast 184.0 + 0.0; price 4.60 + 0.00; quantity target 80.0; risk gate inventory target capped quantity; final forecast=184, price=4.60, quantity=70 |
| 0 | PremiumCloud | llm-context | 184.00 | -4.00 | 6.80 | -1.00 | 40.00 | inventory target capped quantity | forecast 184.0 + -4.0; price 6.80 + -1.00; quantity target 40.0; risk gate inventory target capped quantity; final forecast=180, price=5.80, quantity=20 |
| 0 | SpotBroker | llm-context | 184.00 | -4.00 | 5.00 | -0.20 | 20.00 | none | forecast 184.0 + -4.0; price 5.00 + -0.20; quantity target 20.0; risk gate none; final forecast=180, price=4.80, quantity=20 |
| 1 | Hyperscaler | llm-context | 184.00 | 22.00 | 4.60 | 0.00 | 110.00 | none | forecast 184.0 + 22.0; price 4.60 + 0.00; quantity target 110.0; risk gate none; final forecast=206, price=4.60, quantity=110 |
| 1 | PremiumCloud | llm-context | 184.00 | 6.00 | 6.80 | -0.80 | 30.00 | none | forecast 184.0 + 6.0; price 6.80 + -0.80; quantity target 30.0; risk gate none; final forecast=190, price=6.00, quantity=30 |
| 1 | SpotBroker | llm-context | 184.00 | 16.00 | 5.00 | 0.00 | 30.00 | none | forecast 184.0 + 16.0; price 5.00 + 0.00; quantity target 30.0; risk gate none; final forecast=200, price=5.00, quantity=30 |
| 2 | Hyperscaler | llm-context | 198.00 | 12.00 | 4.60 | 0.00 | 120.00 | none | forecast 198.0 + 12.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=210, price=4.60, quantity=120 |
| 2 | PremiumCloud | llm-context | 193.00 | 2.00 | 7.00 | -1.00 | 30.00 | none | forecast 193.0 + 2.0; price 7.00 + -1.00; quantity target 30.0; risk gate none; final forecast=195, price=6.00, quantity=30 |
| 2 | SpotBroker | llm-context | 200.00 | 10.00 | 5.20 | 0.20 | 40.00 | none | forecast 200.0 + 10.0; price 5.20 + 0.20; quantity target 40.0; risk gate none; final forecast=210, price=5.40, quantity=40 |
| 3 | Hyperscaler | llm-context | 198.00 | 17.00 | 4.60 | 0.00 | 120.00 | none | forecast 198.0 + 17.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=215, price=4.60, quantity=120 |
| 3 | PremiumCloud | llm-context | 195.00 | 5.00 | 7.00 | -1.00 | 40.00 | sla_guard reduced quantity under SLA/reputation pressure | forecast 195.0 + 5.0; price 7.00 + -1.00; quantity target 40.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; final forecast=200, price=6.00, quantity=40 |
| 3 | SpotBroker | llm-context | 200.00 | 10.00 | 5.20 | 0.40 | 50.00 | inventory target capped quantity | forecast 200.0 + 10.0; price 5.20 + 0.40; quantity target 50.0; risk gate inventory target capped quantity; final forecast=210, price=5.60, quantity=40 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Conclusion Notes

- **Winner:** `PremiumCloud` ends with cumulative profit `1375.91`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `5.98`.
- **Market fulfillment:** the run sells `2246.74` units against `2298.00` true demand for a fulfillment ratio of `97.77%`.
- **Operational stress:** peer transfers total `5.12` units, customer reallocation totals `149.53`, final SLA backlog is `0.02`, with `6` dump flags and `5` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
