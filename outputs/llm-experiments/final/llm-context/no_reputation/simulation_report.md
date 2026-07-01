# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | no_reputation | 12 | llm-context | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit | Price Pressure Cost |
| --- | --- | --- | --- | --- | --- |
| 2298 | 2277.92 | 0.99 | 5.64 | 3371.59 | 0.00 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Price Pressure Cost | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 1040.61 | 86.72 | 7.58 | 4.60 | 1366.92 | 1.00 | 0.00 | 2.24 | 0.00 | 10 | 0 | 9.11 | 0.00 | 0.00 |
| PremiumCloud | premium | 1334.47 | 111.21 | 6.25 | 6.70 | 387.89 | 0.98 | 0.99 | 0.77 | 0.00 | 0 | 0 | 1.83 | 0.00 | 8.05 |
| SpotBroker | spot | 996.50 | 83.04 | 4.08 | 5.62 | 523.10 | 0.98 | 2.02 | 0.00 | 0.00 | 0 | 0 | 0.00 | 0.00 | 12.03 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 181.00 | 5.27 | 469.85 | 0.00 | 0.00 | 9.39 | 0.00 |
| 1 | 197 | 195 | 197.00 | 5.40 | 275.82 | 0.00 | 0.00 | 19.41 | 0.00 |
| 2 | 198 | 197 | 198.00 | 5.60 | 267.19 | 0.00 | 0.00 | 11.01 | 0.00 |
| 3 | 202 | 204 | 198.31 | 5.67 | 290.53 | 3.69 | 0.00 | 14.99 | 1.21 |
| 4 | 193 | 194 | 188.79 | 5.67 | 249.01 | 4.21 | 0.00 | 13.66 | 2.20 |
| 5 | 182 | 183 | 181.54 | 5.67 | 201.66 | 0.46 | 1.25 | 6.16 | 0.16 |
| 6 | 171 | 175 | 170.84 | 5.67 | 265.06 | 0.16 | 0.77 | 3.78 | 0.05 |
| 7 | 194 | 196 | 194.00 | 5.80 | 305.10 | 0.00 | 0.99 | 3.62 | 0.00 |
| 8 | 196 | 187 | 196.00 | 5.73 | 291.49 | 0.00 | 0.00 | 13.31 | 0.00 |
| 9 | 200 | 198 | 197.88 | 5.73 | 265.67 | 2.12 | 0.00 | 6.53 | 1.33 |
| 10 | 198 | 198 | 190.57 | 5.73 | 263.88 | 7.43 | 0.00 | 6.67 | 3.26 |
| 11 | 186 | 183 | 183.99 | 5.73 | 226.33 | 2.01 | 0.00 | 2.99 | 0.67 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `no_reputation`, `PremiumCloud` ends first with cumulative profit `1334.47` and reputation `0.00%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `111.52` units and leaves final SLA backlog `0.67`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `3.01` units while average forecast error is `5.97`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 10 | 198 | 190.57 | shortage=7.43; dump_flags=1 |
| 4 | 193 | 188.79 | shortage=4.21; dump_flags=1 |
| 3 | 202 | 198.31 | shortage=3.69; dump_flags=1 |
| 9 | 200 | 197.88 | shortage=2.12; dump_flags=1 |
| 11 | 186 | 183.99 | shortage=2.01; dump_flags=1 |
| 5 | 182 | 181.54 | shortage=0.46; transfer=1.25; dump_flags=1 |
| 7 | 194 | 194.00 | transfer=0.99; dump_flags=1 |
| 1 | 197 | 197.00 | dump_flags=1 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm-context | 184.00 | 6.00 | 4.60 | 0.00 | 90.00 | inventory target capped quantity | forecast 184.0 + 6.0; price 4.60 + 0.00; quantity target 90.0; risk gate inventory target capped quantity; final forecast=190, price=4.60, quantity=80 |
| 0 | PremiumCloud | llm-context | 184.00 | -4.00 | 6.20 | 0.00 | 20.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 184.0 + -4.0; price 6.20 + 0.00; quantity target 20.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=180, price=6.20, quantity=0 |
| 0 | SpotBroker | llm-context | 184.00 | -4.00 | 5.00 | -0.20 | 40.00 | low reputation fallback lifted price | forecast 184.0 + -4.0; price 5.00 + -0.20; quantity target 40.0; risk gate low reputation fallback lifted price; final forecast=180, price=5.00, quantity=40 |
| 1 | Hyperscaler | llm-context | 184.00 | 21.00 | 4.60 | 0.00 | 110.00 | none | forecast 184.0 + 21.0; price 4.60 + 0.00; quantity target 110.0; risk gate none; final forecast=205, price=4.60, quantity=110 |
| 1 | PremiumCloud | llm-context | 184.00 | 6.00 | 6.20 | 0.00 | 40.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 184.0 + 6.0; price 6.20 + 0.00; quantity target 40.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=190, price=6.20, quantity=30 |
| 1 | SpotBroker | llm-context | 184.00 | 16.00 | 5.00 | 0.40 | 50.00 | none | forecast 184.0 + 16.0; price 5.00 + 0.40; quantity target 50.0; risk gate none; final forecast=200, price=5.40, quantity=50 |
| 2 | Hyperscaler | llm-context | 198.00 | 12.00 | 4.60 | 0.00 | 120.00 | none | forecast 198.0 + 12.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=210, price=4.60, quantity=120 |
| 2 | PremiumCloud | llm-context | 193.00 | 2.00 | 6.60 | -0.40 | 40.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; low reputation fallback lifted price | forecast 193.0 + 2.0; price 6.60 + -0.40; quantity target 40.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; low reputation fallback lifted price; final forecast=195, price=6.60, quantity=40 |
| 2 | SpotBroker | llm-context | 200.00 | 0.00 | 5.40 | 0.20 | 40.00 | none | forecast 200.0 + 0.0; price 5.40 + 0.20; quantity target 40.0; risk gate none; final forecast=200, price=5.60, quantity=40 |
| 3 | Hyperscaler | llm-context | 198.00 | 12.00 | 4.60 | 0.00 | 120.00 | none | forecast 198.0 + 12.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=210, price=4.60, quantity=120 |
| 3 | PremiumCloud | llm-context | 195.00 | 5.00 | 6.60 | 0.00 | 40.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 195.0 + 5.0; price 6.60 + 0.00; quantity target 40.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=200, price=6.60, quantity=30 |
| 3 | SpotBroker | llm-context | 200.00 | 10.00 | 5.40 | 0.40 | 40.00 | none | forecast 200.0 + 10.0; price 5.40 + 0.40; quantity target 40.0; risk gate none; final forecast=210, price=5.80, quantity=40 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Conclusion Notes

- **Winner:** `PremiumCloud` ends with cumulative profit `1334.47`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.70`.
- **Market fulfillment:** the run sells `2277.92` units against `2298.00` true demand for a fulfillment ratio of `99.13%`.
- **Operational stress:** peer transfers total `3.01` units, customer reallocation totals `111.52`, final SLA backlog is `0.67`, with `10` dump flags and `0` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
