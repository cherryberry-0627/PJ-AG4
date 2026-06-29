# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | baseline | 12 | llm-context | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit | Price Pressure Cost |
| --- | --- | --- | --- | --- | --- |
| 2298 | 2283.47 | 0.99 | 5.54 | 3514.75 | 0.00 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Price Pressure Cost | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 1006.74 | 83.89 | 9.83 | 4.60 | 1306.92 | 1.00 | 0.00 | 4.92 | 0.00 | 8 | 0 | 11.47 | 0.67 | 0.00 |
| PremiumCloud | premium | 1700.46 | 141.71 | 6.25 | 6.55 | 538.74 | 0.99 | 0.00 | 1.31 | 0.00 | 0 | 0 | 1.59 | 0.91 | 4.81 |
| SpotBroker | spot | 807.55 | 67.30 | 3.67 | 5.48 | 437.81 | 0.98 | 6.23 | 0.00 | 0.00 | 0 | 1 | 0.00 | 0.87 | 9.72 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 181.00 | 5.20 | 514.38 | 0.00 | 0.00 | 26.82 | 0.00 |
| 1 | 197 | 195 | 197.00 | 5.33 | 230.49 | 0.00 | 0.00 | 28.77 | 0.00 |
| 2 | 198 | 197 | 198.00 | 5.47 | 285.06 | 0.00 | 0.00 | 35.33 | 0.00 |
| 3 | 202 | 204 | 200.89 | 5.53 | 272.05 | 1.11 | 0.00 | 23.89 | 0.71 |
| 4 | 193 | 194 | 189.29 | 5.60 | 254.84 | 3.71 | 0.00 | 24.47 | 2.16 |
| 5 | 182 | 183 | 182.00 | 5.53 | 254.52 | 0.00 | 4.92 | 18.32 | 0.00 |
| 6 | 171 | 175 | 166.76 | 5.53 | 238.37 | 4.24 | 0.11 | 16.19 | 1.76 |
| 7 | 194 | 196 | 190.99 | 5.60 | 217.54 | 3.01 | 0.00 | 4.71 | 0.90 |
| 8 | 196 | 187 | 194.37 | 5.60 | 326.33 | 1.63 | 1.20 | 7.21 | 0.53 |
| 9 | 200 | 198 | 199.47 | 5.67 | 312.04 | 0.53 | 0.00 | 5.26 | 0.18 |
| 10 | 198 | 198 | 197.82 | 5.73 | 311.30 | 0.18 | 0.00 | 2.70 | 0.06 |
| 11 | 186 | 183 | 185.87 | 5.73 | 297.84 | 0.13 | 0.00 | 0.27 | 0.04 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `baseline`, `PremiumCloud` ends first with cumulative profit `1700.46` and reputation `90.68%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `193.93` units and leaves final SLA backlog `0.04`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `6.23` units while average forecast error is `6.58`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 5 | 182 | 182.00 | transfer=4.92; dump_flags=1 |
| 6 | 171 | 166.76 | shortage=4.24; transfer=0.11; default_flags=1 |
| 4 | 193 | 189.29 | shortage=3.71; dump_flags=1 |
| 7 | 194 | 190.99 | shortage=3.01; dump_flags=1 |
| 3 | 202 | 200.89 | shortage=1.11; dump_flags=1 |
| 9 | 200 | 199.47 | shortage=0.53; dump_flags=1 |
| 10 | 198 | 197.82 | shortage=0.18; dump_flags=1 |
| 1 | 197 | 197.00 | dump_flags=1 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm-context | 184.00 | 6.00 | 4.60 | 0.00 | 90.00 | inventory target capped quantity | forecast 184.0 + 6.0; price 4.60 + 0.00; quantity target 90.0; risk gate inventory target capped quantity; final forecast=190, price=4.60, quantity=80 |
| 0 | PremiumCloud | llm-context | 184.00 | -4.00 | 6.80 | -0.60 | 20.00 | inventory target capped quantity | forecast 184.0 + -4.0; price 6.80 + -0.60; quantity target 20.0; risk gate inventory target capped quantity; final forecast=180, price=6.20, quantity=10 |
| 0 | SpotBroker | llm-context | 184.00 | -4.00 | 5.00 | -0.20 | 20.00 | none | forecast 184.0 + -4.0; price 5.00 + -0.20; quantity target 20.0; risk gate none; final forecast=180, price=4.80, quantity=20 |
| 1 | Hyperscaler | llm-context | 184.00 | 26.00 | 4.60 | 0.00 | 120.00 | none | forecast 184.0 + 26.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=210, price=4.60, quantity=120 |
| 1 | PremiumCloud | llm-context | 184.00 | 6.00 | 6.80 | -0.40 | 40.00 | none | forecast 184.0 + 6.0; price 6.80 + -0.40; quantity target 40.0; risk gate none; final forecast=190, price=6.40, quantity=40 |
| 1 | SpotBroker | llm-context | 184.00 | 16.00 | 5.00 | 0.00 | 40.00 | none | forecast 184.0 + 16.0; price 5.00 + 0.00; quantity target 40.0; risk gate none; final forecast=200, price=5.00, quantity=40 |
| 2 | Hyperscaler | llm-context | 198.00 | 12.00 | 4.60 | 0.00 | 120.00 | inventory target capped quantity | forecast 198.0 + 12.0; price 4.60 + 0.00; quantity target 120.0; risk gate inventory target capped quantity; final forecast=210, price=4.60, quantity=120 |
| 2 | PremiumCloud | llm-context | 193.00 | 5.00 | 7.00 | -0.40 | 50.00 | inventory target capped quantity | forecast 193.0 + 5.0; price 7.00 + -0.40; quantity target 50.0; risk gate inventory target capped quantity; final forecast=198, price=6.60, quantity=40 |
| 2 | SpotBroker | llm-context | 200.00 | 10.00 | 5.20 | 0.00 | 30.00 | inventory_guard lifted price under volatility | forecast 200.0 + 10.0; price 5.20 + 0.00; quantity target 30.0; risk gate inventory_guard lifted price under volatility; final forecast=210, price=5.20, quantity=30 |
| 3 | Hyperscaler | llm-context | 198.00 | 14.00 | 4.60 | 0.00 | 120.00 | none | forecast 198.0 + 14.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=212, price=4.60, quantity=120 |
| 3 | PremiumCloud | llm-context | 195.00 | 7.00 | 7.00 | -0.40 | 50.00 | inventory target capped quantity | forecast 195.0 + 7.0; price 7.00 + -0.40; quantity target 50.0; risk gate inventory target capped quantity; final forecast=202, price=6.60, quantity=40 |
| 3 | SpotBroker | llm-context | 200.00 | 10.00 | 5.40 | 0.00 | 40.00 | none | forecast 200.0 + 10.0; price 5.40 + 0.00; quantity target 40.0; risk gate none; final forecast=210, price=5.40, quantity=40 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Conclusion Notes

- **Winner:** `PremiumCloud` ends with cumulative profit `1700.46`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.55`.
- **Market fulfillment:** the run sells `2283.47` units against `2298.00` true demand for a fulfillment ratio of `99.37%`.
- **Operational stress:** peer transfers total `6.23` units, customer reallocation totals `193.93`, final SLA backlog is `0.04`, with `8` dump flags and `1` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
