# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | no_transfer | 12 | llm-context | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit | Price Pressure Cost |
| --- | --- | --- | --- | --- | --- |
| 2298 | 2256.86 | 0.98 | 5.58 | 3355.75 | 0.00 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Price Pressure Cost | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 1062.73 | 88.56 | 8.75 | 4.60 | 1384.84 | 1.00 | 0.00 | 0.00 | 0.00 | 10 | 0 | 8.05 | 0.65 | 0.00 |
| PremiumCloud | premium | 1543.55 | 128.63 | 8.42 | 6.50 | 504.12 | 0.96 | 0.00 | 0.00 | 0.00 | 0 | 3 | 7.42 | 0.90 | 22.45 |
| SpotBroker | spot | 749.46 | 62.46 | 2.83 | 5.65 | 367.90 | 0.95 | 0.00 | 0.00 | 0.00 | 0 | 3 | 0.00 | 0.78 | 18.69 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 180.00 | 5.13 | 541.63 | 1.00 | 0.00 | 28.00 | 0.61 |
| 1 | 197 | 195 | 196.39 | 5.33 | 240.81 | 0.61 | 0.00 | 26.85 | 0.34 |
| 2 | 198 | 197 | 197.66 | 5.47 | 261.62 | 0.34 | 0.00 | 23.21 | 0.18 |
| 3 | 202 | 204 | 193.68 | 5.60 | 265.71 | 8.32 | 0.00 | 22.42 | 4.58 |
| 4 | 193 | 194 | 185.42 | 5.53 | 243.56 | 7.58 | 0.00 | 24.74 | 3.88 |
| 5 | 182 | 183 | 176.49 | 5.60 | 206.51 | 5.51 | 0.00 | 16.88 | 2.57 |
| 6 | 171 | 175 | 166.76 | 5.67 | 255.49 | 4.24 | 0.00 | 6.56 | 1.52 |
| 7 | 194 | 196 | 193.14 | 5.73 | 263.45 | 0.86 | 0.00 | 3.41 | 0.47 |
| 8 | 196 | 187 | 195.53 | 5.67 | 296.93 | 0.47 | 0.00 | 14.24 | 0.28 |
| 9 | 200 | 198 | 194.10 | 5.73 | 283.72 | 5.90 | 0.00 | 13.22 | 3.23 |
| 10 | 198 | 198 | 195.00 | 5.80 | 290.16 | 3.00 | 0.00 | 5.55 | 1.19 |
| 11 | 186 | 183 | 182.68 | 5.73 | 206.15 | 3.32 | 0.00 | 8.18 | 1.34 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `no_transfer`, `PremiumCloud` ends first with cumulative profit `1543.55` and reputation `90.15%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `193.26` units and leaves final SLA backlog `1.34`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `0.00` units while average forecast error is `6.67`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 3 | 202 | 193.68 | shortage=8.32; dump_flags=1; default_flags=1 |
| 4 | 193 | 185.42 | shortage=7.58; dump_flags=1; default_flags=1 |
| 9 | 200 | 194.10 | shortage=5.90; dump_flags=1; default_flags=1 |
| 5 | 182 | 176.49 | shortage=5.51; dump_flags=1; default_flags=1 |
| 11 | 186 | 182.68 | shortage=3.32; dump_flags=1; default_flags=1 |
| 6 | 171 | 166.76 | shortage=4.24; default_flags=1 |
| 10 | 198 | 195.00 | shortage=3.00; dump_flags=1 |
| 7 | 194 | 193.14 | shortage=0.86; dump_flags=1 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm-context | 184.00 | 0.00 | 4.60 | 0.00 | 90.00 | inventory target capped quantity | forecast 184.0 + 0.0; price 4.60 + 0.00; quantity target 90.0; risk gate inventory target capped quantity; final forecast=184, price=4.60, quantity=70 |
| 0 | PremiumCloud | llm-context | 184.00 | -24.00 | 6.80 | -0.80 | 40.00 | inventory target capped quantity | forecast 184.0 + -24.0; price 6.80 + -0.80; quantity target 40.0; risk gate inventory target capped quantity; final forecast=160, price=6.00, quantity=10 |
| 0 | SpotBroker | llm-context | 184.00 | -4.00 | 5.00 | -0.20 | 20.00 | none | forecast 184.0 + -4.0; price 5.00 + -0.20; quantity target 20.0; risk gate none; final forecast=180, price=4.80, quantity=20 |
| 1 | Hyperscaler | llm-context | 184.00 | 26.00 | 4.60 | 0.00 | 120.00 | none | forecast 184.0 + 26.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=210, price=4.60, quantity=120 |
| 1 | PremiumCloud | llm-context | 184.00 | 6.00 | 6.80 | -0.60 | 50.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 184.0 + 6.0; price 6.80 + -0.60; quantity target 50.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=190, price=6.20, quantity=50 |
| 1 | SpotBroker | llm-context | 184.00 | 16.00 | 5.00 | 0.20 | 30.00 | none | forecast 184.0 + 16.0; price 5.00 + 0.20; quantity target 30.0; risk gate none; final forecast=200, price=5.20, quantity=30 |
| 2 | Hyperscaler | llm-context | 198.00 | 12.00 | 4.60 | 0.00 | 120.00 | none | forecast 198.0 + 12.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=210, price=4.60, quantity=120 |
| 2 | PremiumCloud | llm-context | 193.00 | 2.00 | 7.00 | -0.60 | 50.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 193.0 + 2.0; price 7.00 + -0.60; quantity target 50.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=195, price=6.40, quantity=50 |
| 2 | SpotBroker | llm-context | 200.00 | 0.00 | 5.20 | 0.20 | 30.00 | none | forecast 200.0 + 0.0; price 5.20 + 0.20; quantity target 30.0; risk gate none; final forecast=200, price=5.40, quantity=30 |
| 3 | Hyperscaler | llm-context | 198.00 | 17.00 | 4.60 | 0.00 | 120.00 | none | forecast 198.0 + 17.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=215, price=4.60, quantity=120 |
| 3 | PremiumCloud | llm-context | 195.00 | 5.00 | 7.00 | -0.40 | 60.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 195.0 + 5.0; price 7.00 + -0.40; quantity target 60.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=200, price=6.60, quantity=40 |
| 3 | SpotBroker | llm-context | 200.00 | 10.00 | 5.40 | 0.20 | 30.00 | none | forecast 200.0 + 10.0; price 5.40 + 0.20; quantity target 30.0; risk gate none; final forecast=210, price=5.60, quantity=30 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Conclusion Notes

- **Winner:** `PremiumCloud` ends with cumulative profit `1543.55`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.50`.
- **Market fulfillment:** the run sells `2256.86` units against `2298.00` true demand for a fulfillment ratio of `98.21%`.
- **Operational stress:** peer transfers total `0.00` units, customer reallocation totals `193.26`, final SLA backlog is `1.34`, with `10` dump flags and `6` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
