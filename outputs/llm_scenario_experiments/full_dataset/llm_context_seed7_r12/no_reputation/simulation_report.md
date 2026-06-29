# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | no_reputation | 12 | llm-context | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit | Price Pressure Cost |
| --- | --- | --- | --- | --- | --- |
| 2298 | 2242.49 | 0.98 | 5.73 | 3411.85 | 0.00 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Price Pressure Cost | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 1096.77 | 91.40 | 10.08 | 4.60 | 1419.37 | 1.00 | 0.00 | 1.28 | 0.00 | 11 | 0 | 0.63 | 0.00 | 0.74 |
| PremiumCloud | premium | 1392.31 | 116.03 | 6.17 | 6.75 | 394.76 | 0.93 | 2.17 | 5.84 | 0.00 | 0 | 4 | 0.00 | 0.00 | 33.03 |
| SpotBroker | spot | 922.77 | 76.90 | 3.17 | 5.85 | 428.36 | 0.95 | 5.84 | 0.89 | 0.00 | 0 | 1 | 2.69 | 0.00 | 21.74 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 181.00 | 5.27 | 497.13 | 0.00 | 0.00 | 29.39 | 0.00 |
| 1 | 197 | 195 | 177.65 | 5.40 | 221.96 | 19.35 | 0.00 | 20.06 | 9.27 |
| 2 | 198 | 197 | 190.73 | 5.60 | 271.54 | 7.27 | 5.74 | 14.83 | 3.45 |
| 3 | 202 | 204 | 186.55 | 5.67 | 245.28 | 15.45 | 0.00 | 6.68 | 6.34 |
| 4 | 193 | 194 | 188.38 | 5.80 | 270.41 | 4.62 | 0.10 | 0.49 | 1.68 |
| 5 | 182 | 183 | 181.54 | 5.87 | 242.16 | 0.46 | 1.28 | 5.45 | 0.28 |
| 6 | 171 | 175 | 170.72 | 5.80 | 210.79 | 0.28 | 0.00 | 6.19 | 0.16 |
| 7 | 194 | 196 | 193.84 | 5.80 | 285.79 | 0.16 | 0.00 | 10.95 | 0.10 |
| 8 | 196 | 187 | 195.90 | 5.87 | 304.04 | 0.10 | 0.00 | 7.80 | 0.06 |
| 9 | 200 | 198 | 193.42 | 5.87 | 283.86 | 6.58 | 0.00 | 2.88 | 3.09 |
| 10 | 198 | 198 | 196.91 | 5.93 | 316.20 | 1.09 | 0.00 | 2.32 | 0.36 |
| 11 | 186 | 183 | 185.84 | 5.93 | 262.70 | 0.16 | 0.89 | 3.78 | 0.09 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `no_reputation`, `PremiumCloud` ends first with cumulative profit `1392.31` and reputation `0.00%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `110.82` units and leaves final SLA backlog `0.09`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `8.00` units while average forecast error is `6.47`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 3 | 202 | 186.55 | shortage=15.45; dump_flags=1; default_flags=2 |
| 1 | 197 | 177.65 | shortage=19.35; dump_flags=1; default_flags=1 |
| 2 | 198 | 190.73 | shortage=7.27; transfer=5.74; dump_flags=1; default_flags=1 |
| 9 | 200 | 193.42 | shortage=6.58; dump_flags=1; default_flags=1 |
| 4 | 193 | 188.38 | shortage=4.62; transfer=0.10; dump_flags=1 |
| 5 | 182 | 181.54 | shortage=0.46; transfer=1.28; dump_flags=1 |
| 10 | 198 | 196.91 | shortage=1.09; dump_flags=1 |
| 11 | 186 | 185.84 | shortage=0.16; transfer=0.89; dump_flags=1 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm-context | 184.00 | 16.00 | 4.60 | 0.00 | 90.00 | inventory target capped quantity | forecast 184.0 + 16.0; price 4.60 + 0.00; quantity target 90.0; risk gate inventory target capped quantity; final forecast=200, price=4.60, quantity=90 |
| 0 | PremiumCloud | llm-context | 184.00 | -4.00 | 6.20 | 0.00 | 30.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 184.0 + -4.0; price 6.20 + 0.00; quantity target 30.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=180, price=6.20, quantity=0 |
| 0 | SpotBroker | llm-context | 184.00 | 0.00 | 5.00 | -0.20 | 20.00 | low reputation fallback lifted price | forecast 184.0 + 0.0; price 5.00 + -0.20; quantity target 20.0; risk gate low reputation fallback lifted price; final forecast=184, price=5.00, quantity=20 |
| 1 | Hyperscaler | llm-context | 184.00 | 26.00 | 4.60 | 0.00 | 110.00 | none | forecast 184.0 + 26.0; price 4.60 + 0.00; quantity target 110.0; risk gate none; final forecast=210, price=4.60, quantity=110 |
| 1 | PremiumCloud | llm-context | 184.00 | 6.00 | 6.20 | 0.00 | 40.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 184.0 + 6.0; price 6.20 + 0.00; quantity target 40.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=190, price=6.20, quantity=30 |
| 1 | SpotBroker | llm-context | 184.00 | 21.00 | 5.00 | 0.40 | 30.00 | none | forecast 184.0 + 21.0; price 5.00 + 0.40; quantity target 30.0; risk gate none; final forecast=205, price=5.40, quantity=30 |
| 2 | Hyperscaler | llm-context | 198.00 | 12.00 | 4.60 | 0.00 | 120.00 | none | forecast 198.0 + 12.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=210, price=4.60, quantity=120 |
| 2 | PremiumCloud | llm-context | 193.00 | 2.00 | 6.60 | -0.40 | 50.00 | sla_guard reduced quantity under SLA/reputation pressure; low reputation fallback lifted price | forecast 193.0 + 2.0; price 6.60 + -0.40; quantity target 50.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; low reputation fallback lifted price; final forecast=195, price=6.60, quantity=50 |
| 2 | SpotBroker | llm-context | 200.00 | 0.00 | 5.40 | 0.20 | 30.00 | none | forecast 200.0 + 0.0; price 5.40 + 0.20; quantity target 30.0; risk gate none; final forecast=200, price=5.60, quantity=30 |
| 3 | Hyperscaler | llm-context | 198.00 | 17.00 | 4.60 | 0.00 | 120.00 | none | forecast 198.0 + 17.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=215, price=4.60, quantity=120 |
| 3 | PremiumCloud | llm-context | 195.00 | 5.00 | 6.60 | 0.00 | 60.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 195.0 + 5.0; price 6.60 + 0.00; quantity target 60.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=200, price=6.60, quantity=40 |
| 3 | SpotBroker | llm-context | 200.00 | 5.00 | 5.40 | 0.40 | 30.00 | none | forecast 200.0 + 5.0; price 5.40 + 0.40; quantity target 30.0; risk gate none; final forecast=205, price=5.80, quantity=30 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Conclusion Notes

- **Winner:** `PremiumCloud` ends with cumulative profit `1392.31`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `99.95%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.75`.
- **Market fulfillment:** the run sells `2242.49` units against `2298.00` true demand for a fulfillment ratio of `97.58%`.
- **Operational stress:** peer transfers total `8.00` units, customer reallocation totals `110.82`, final SLA backlog is `0.09`, with `11` dump flags and `5` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
