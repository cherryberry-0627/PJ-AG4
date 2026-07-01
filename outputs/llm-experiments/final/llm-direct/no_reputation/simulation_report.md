# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | no_reputation | 12 | llm | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit | Price Pressure Cost |
| --- | --- | --- | --- | --- | --- |
| 2298 | 2292.46 | 1.00 | 5.60 | 3182.76 | 0.00 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Price Pressure Cost | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 928.88 | 77.41 | 6.75 | 4.60 | 1351.73 | 1.00 | 0.00 | 5.76 | 0.00 | 11 | 0 | 14.76 | 0.00 | 0.00 |
| PremiumCloud | premium | 1274.67 | 106.22 | 6.25 | 6.70 | 367.99 | 0.99 | 5.76 | 0.00 | 0.00 | 0 | 0 | 0.00 | 0.00 | 5.54 |
| SpotBroker | spot | 979.21 | 81.60 | 3.50 | 5.50 | 572.73 | 1.00 | 0.00 | 0.00 | 0.00 | 0 | 0 | 8.84 | 0.00 | 0.00 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 180.00 | 5.27 | 534.88 | 1.00 | 0.00 | 28.39 | 0.55 |
| 1 | 197 | 195 | 196.45 | 5.27 | 170.89 | 0.55 | 0.00 | 18.17 | 0.39 |
| 2 | 198 | 197 | 197.61 | 5.53 | 244.10 | 0.39 | 0.00 | 15.41 | 0.26 |
| 3 | 202 | 204 | 201.74 | 5.60 | 273.18 | 0.26 | 0.00 | 12.85 | 0.19 |
| 4 | 193 | 194 | 192.81 | 5.60 | 193.49 | 0.19 | 1.27 | 4.15 | 0.11 |
| 5 | 182 | 183 | 181.89 | 5.60 | 257.55 | 0.11 | 0.00 | 12.77 | 0.07 |
| 6 | 171 | 175 | 170.93 | 5.67 | 176.79 | 0.07 | 0.50 | 1.73 | 0.04 |
| 7 | 194 | 196 | 193.96 | 5.73 | 297.80 | 0.04 | 0.85 | 2.94 | 0.02 |
| 8 | 196 | 187 | 195.98 | 5.73 | 289.03 | 0.02 | 0.00 | 13.75 | 0.01 |
| 9 | 200 | 198 | 199.99 | 5.73 | 281.10 | 0.01 | 1.86 | 6.79 | 0.01 |
| 10 | 198 | 198 | 196.22 | 5.73 | 256.16 | 1.78 | 0.00 | 6.49 | 1.12 |
| 11 | 186 | 183 | 184.88 | 5.73 | 207.78 | 1.12 | 1.28 | 4.67 | 0.67 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `no_reputation`, `PremiumCloud` ends first with cumulative profit `1274.67` and reputation `0.00%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `128.11` units and leaves final SLA backlog `0.67`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `5.76` units while average forecast error is `5.50`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 11 | 186 | 184.88 | shortage=1.12; transfer=1.28; dump_flags=1 |
| 9 | 200 | 199.99 | shortage=0.01; transfer=1.86; dump_flags=1 |
| 10 | 198 | 196.22 | shortage=1.78; dump_flags=1 |
| 4 | 193 | 192.81 | shortage=0.19; transfer=1.27; dump_flags=1 |
| 7 | 194 | 193.96 | shortage=0.04; transfer=0.85; dump_flags=1 |
| 6 | 171 | 170.93 | shortage=0.07; transfer=0.50; dump_flags=1 |
| 1 | 197 | 196.45 | shortage=0.55; dump_flags=1 |
| 2 | 198 | 197.61 | shortage=0.39; dump_flags=1 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm | 184.00 | 6.00 | 4.60 | 0.00 | 90.00 | inventory target capped quantity | forecast 184.0 + 6.0; price 4.60 + 0.00; quantity target 90.0; risk gate inventory target capped quantity; final forecast=190, price=4.60, quantity=80 |
| 0 | PremiumCloud | llm | 184.00 | -4.00 | 6.20 | 0.00 | 20.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 184.0 + -4.0; price 6.20 + 0.00; quantity target 20.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=180, price=6.20, quantity=0 |
| 0 | SpotBroker | llm | 184.00 | -4.00 | 5.00 | -0.20 | 20.00 | low reputation fallback lifted price | forecast 184.0 + -4.0; price 5.00 + -0.20; quantity target 20.0; risk gate low reputation fallback lifted price; final forecast=180, price=5.00, quantity=20 |
| 1 | Hyperscaler | llm | 184.00 | 21.00 | 4.60 | 0.00 | 120.00 | none | forecast 184.0 + 21.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=205, price=4.60, quantity=120 |
| 1 | PremiumCloud | llm | 184.00 | 6.00 | 6.20 | 0.00 | 40.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 184.0 + 6.0; price 6.20 + 0.00; quantity target 40.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=190, price=6.20, quantity=30 |
| 1 | SpotBroker | llm | 184.00 | 11.00 | 5.00 | 0.00 | 60.00 | none | forecast 184.0 + 11.0; price 5.00 + 0.00; quantity target 60.0; risk gate none; final forecast=195, price=5.00, quantity=60 |
| 2 | Hyperscaler | llm | 198.00 | 7.00 | 4.60 | 0.00 | 120.00 | none | forecast 198.0 + 7.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=205, price=4.60, quantity=120 |
| 2 | PremiumCloud | llm | 193.00 | 2.00 | 6.60 | -0.20 | 40.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; low reputation fallback lifted price | forecast 193.0 + 2.0; price 6.60 + -0.20; quantity target 40.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; low reputation fallback lifted price; final forecast=195, price=6.60, quantity=30 |
| 2 | SpotBroker | llm | 200.00 | 5.00 | 5.20 | 0.20 | 50.00 | none | forecast 200.0 + 5.0; price 5.20 + 0.20; quantity target 50.0; risk gate none; final forecast=205, price=5.40, quantity=50 |
| 3 | Hyperscaler | llm | 198.00 | 12.00 | 4.60 | 0.00 | 120.00 | none | forecast 198.0 + 12.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=210, price=4.60, quantity=120 |
| 3 | PremiumCloud | llm | 195.00 | 3.00 | 6.60 | 0.00 | 40.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 195.0 + 3.0; price 6.60 + 0.00; quantity target 40.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=198, price=6.60, quantity=30 |
| 3 | SpotBroker | llm | 200.00 | 10.00 | 5.40 | 0.20 | 50.00 | none | forecast 200.0 + 10.0; price 5.40 + 0.20; quantity target 50.0; risk gate none; final forecast=210, price=5.60, quantity=50 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Conclusion Notes

- **Winner:** `PremiumCloud` ends with cumulative profit `1274.67`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.70`.
- **Market fulfillment:** the run sells `2292.46` units against `2298.00` true demand for a fulfillment ratio of `99.76%`.
- **Operational stress:** peer transfers total `5.76` units, customer reallocation totals `128.11`, final SLA backlog is `0.67`, with `11` dump flags and `0` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
