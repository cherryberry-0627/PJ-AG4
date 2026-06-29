# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | price_war | 12 | llm-context | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit | Price Pressure Cost |
| --- | --- | --- | --- | --- | --- |
| 2298 | 2250.45 | 0.98 | 5.56 | 2847.90 | 235.25 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Price Pressure Cost | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 971.50 | 80.96 | 8.08 | 4.60 | 1418.10 | 0.99 | 0.00 | 0.00 | 151.38 | 11 | 0 | 0.00 | 0.57 | 15.98 |
| PremiumCloud | premium | 1100.39 | 91.70 | 6.33 | 6.60 | 322.54 | 1.00 | 0.00 | 11.99 | 6.21 | 0 | 0 | 5.76 | 0.81 | 0.00 |
| SpotBroker | spot | 776.02 | 64.67 | 3.50 | 5.48 | 509.81 | 0.95 | 11.99 | 0.00 | 77.66 | 0 | 1 | 0.00 | 0.81 | 31.58 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 180.00 | 5.27 | 485.42 | 1.00 | 11.99 | 37.16 | 0.19 |
| 1 | 197 | 195 | 176.69 | 5.40 | 147.12 | 20.31 | 0.00 | 21.84 | 3.69 |
| 2 | 198 | 197 | 193.38 | 5.53 | 210.12 | 4.62 | 0.00 | 1.08 | 0.60 |
| 3 | 202 | 204 | 199.50 | 5.60 | 243.03 | 2.50 | 0.00 | 8.77 | 0.29 |
| 4 | 193 | 194 | 190.15 | 5.67 | 195.80 | 2.85 | 0.00 | 8.62 | 0.32 |
| 5 | 182 | 183 | 180.68 | 5.53 | 201.91 | 1.32 | 0.00 | 10.39 | 0.27 |
| 6 | 171 | 175 | 170.64 | 5.60 | 210.35 | 0.36 | 0.00 | 0.66 | 0.07 |
| 7 | 194 | 196 | 191.97 | 5.67 | 240.12 | 2.03 | 0.00 | 6.05 | 0.21 |
| 8 | 196 | 187 | 195.41 | 5.60 | 260.40 | 0.59 | 0.00 | 5.25 | 0.10 |
| 9 | 200 | 198 | 196.44 | 5.60 | 218.27 | 3.56 | 0.00 | 1.62 | 0.37 |
| 10 | 198 | 198 | 192.74 | 5.67 | 251.56 | 5.26 | 0.00 | 7.51 | 0.75 |
| 11 | 186 | 183 | 182.86 | 5.60 | 183.81 | 3.14 | 0.00 | 4.58 | 0.66 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `price_war`, `PremiumCloud` ends first with cumulative profit `1100.39` and reputation `81.40%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `113.54` units and leaves final SLA backlog `0.66`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `11.99` units while average forecast error is `5.97`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 1 | 197 | 176.69 | shortage=20.31; dump_flags=1; default_flags=1 |
| 10 | 198 | 192.74 | shortage=5.26; dump_flags=1 |
| 2 | 198 | 193.38 | shortage=4.62; dump_flags=1 |
| 9 | 200 | 196.44 | shortage=3.56; dump_flags=1 |
| 11 | 186 | 182.86 | shortage=3.14; dump_flags=1 |
| 0 | 181 | 180.00 | shortage=1.00; transfer=11.99 |
| 4 | 193 | 190.15 | shortage=2.85; dump_flags=1 |
| 3 | 202 | 199.50 | shortage=2.50; dump_flags=1 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm-context | 184.00 | 6.00 | 4.60 | 0.00 | 80.00 | inventory target capped quantity | forecast 184.0 + 6.0; price 4.60 + 0.00; quantity target 80.0; risk gate inventory target capped quantity; final forecast=190, price=4.60, quantity=80 |
| 0 | PremiumCloud | llm-context | 184.00 | -4.00 | 6.80 | -0.20 | 20.00 | inventory target capped quantity | forecast 184.0 + -4.0; price 6.80 + -0.20; quantity target 20.0; risk gate inventory target capped quantity; final forecast=180, price=6.60, quantity=0 |
| 0 | SpotBroker | llm-context | 184.00 | -4.00 | 5.00 | -0.40 | 20.00 | none | forecast 184.0 + -4.0; price 5.00 + -0.40; quantity target 20.0; risk gate none; final forecast=180, price=4.60, quantity=20 |
| 1 | Hyperscaler | llm-context | 184.00 | 21.00 | 4.60 | 0.00 | 120.00 | none | forecast 184.0 + 21.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=205, price=4.60, quantity=120 |
| 1 | PremiumCloud | llm-context | 184.00 | 6.00 | 6.80 | -0.20 | 30.00 | none | forecast 184.0 + 6.0; price 6.80 + -0.20; quantity target 30.0; risk gate none; final forecast=190, price=6.60, quantity=30 |
| 1 | SpotBroker | llm-context | 184.00 | 16.00 | 5.00 | 0.00 | 30.00 | none | forecast 184.0 + 16.0; price 5.00 + 0.00; quantity target 30.0; risk gate none; final forecast=200, price=5.00, quantity=30 |
| 2 | Hyperscaler | llm-context | 198.00 | 12.00 | 4.60 | 0.00 | 120.00 | none | forecast 198.0 + 12.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=210, price=4.60, quantity=120 |
| 2 | PremiumCloud | llm-context | 193.00 | 2.00 | 7.00 | -0.40 | 30.00 | none | forecast 193.0 + 2.0; price 7.00 + -0.40; quantity target 30.0; risk gate none; final forecast=195, price=6.60, quantity=30 |
| 2 | SpotBroker | llm-context | 200.00 | 0.00 | 5.40 | 0.00 | 50.00 | none | forecast 200.0 + 0.0; price 5.40 + 0.00; quantity target 50.0; risk gate none; final forecast=200, price=5.40, quantity=50 |
| 3 | Hyperscaler | llm-context | 198.00 | 12.00 | 4.60 | 0.00 | 120.00 | growth_tolerant added capacity after shortage | forecast 198.0 + 12.0; price 4.60 + 0.00; quantity target 120.0; risk gate growth_tolerant added capacity after shortage; final forecast=210, price=4.60, quantity=120 |
| 3 | PremiumCloud | llm-context | 195.00 | 5.00 | 7.00 | -0.40 | 30.00 | sla_guard reduced quantity under SLA/reputation pressure | forecast 195.0 + 5.0; price 7.00 + -0.40; quantity target 30.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; final forecast=200, price=6.60, quantity=30 |
| 3 | SpotBroker | llm-context | 200.00 | 5.00 | 5.40 | 0.20 | 50.00 | none | forecast 200.0 + 5.0; price 5.40 + 0.20; quantity target 50.0; risk gate none; final forecast=205, price=5.60, quantity=50 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Conclusion Notes

- **Winner:** `PremiumCloud` ends with cumulative profit `1100.39`, the highest value in this run.
- **Service leader:** `PremiumCloud` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.60`.
- **Market fulfillment:** the run sells `2250.45` units against `2298.00` true demand for a fulfillment ratio of `97.93%`.
- **Operational stress:** peer transfers total `11.99` units, customer reallocation totals `113.54`, final SLA backlog is `0.66`, with `11` dump flags and `1` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
