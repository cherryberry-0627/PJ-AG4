# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | high_volatility | 12 | heuristic | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit | Price Pressure Cost |
| --- | --- | --- | --- | --- | --- |
| 2279 | 2273.15 | 1.00 | 5.71 | 3330.69 | 0.00 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Price Pressure Cost | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 874.33 | 72.86 | 15.00 | 4.60 | 1252.72 | 1.00 | 0.00 | 4.71 | 0.00 | 9 | 0 | 25.08 | 0.72 | 0.00 |
| PremiumCloud | premium | 1492.05 | 124.34 | 13.50 | 6.97 | 411.95 | 0.98 | 13.06 | 0.00 | 0.00 | 0 | 0 | 1.96 | 0.96 | 5.85 |
| SpotBroker | spot | 964.31 | 80.36 | 15.58 | 5.57 | 608.48 | 1.00 | 0.00 | 8.35 | 0.00 | 0 | 0 | 20.40 | 0.92 | 0.00 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 179 | 184 | 179.00 | 5.47 | 559.90 | 0.00 | 0.00 | 15.85 | 0.00 |
| 1 | 200 | 197 | 200.00 | 5.47 | 187.05 | 0.00 | 0.00 | 6.27 | 0.00 |
| 2 | 195 | 193 | 195.00 | 5.67 | 259.24 | 0.00 | 2.84 | 9.24 | 0.00 |
| 3 | 211 | 215 | 211.00 | 5.73 | 348.50 | 0.00 | 3.63 | 12.14 | 0.00 |
| 4 | 202 | 204 | 202.00 | 5.73 | 193.64 | 0.00 | 0.75 | 2.43 | 0.00 |
| 5 | 184 | 186 | 184.00 | 5.73 | 188.74 | 0.00 | 0.00 | 0.00 | 0.00 |
| 6 | 155 | 164 | 155.00 | 5.73 | 197.40 | 0.00 | 0.37 | 1.16 | 0.00 |
| 7 | 193 | 198 | 190.52 | 5.80 | 497.69 | 2.48 | 0.00 | 7.22 | 1.65 |
| 8 | 186 | 169 | 184.35 | 5.80 | 175.21 | 1.65 | 1.51 | 5.30 | 1.04 |
| 9 | 191 | 186 | 189.96 | 5.80 | 330.79 | 1.04 | 1.82 | 6.37 | 0.68 |
| 10 | 197 | 197 | 196.32 | 5.80 | 235.39 | 0.68 | 2.15 | 7.30 | 0.45 |
| 11 | 186 | 180 | 186.00 | 5.80 | 157.14 | 0.00 | 0.00 | 0.00 | 0.00 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `high_volatility`, `PremiumCloud` ends first with cumulative profit `1492.05` and reputation `95.61%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `73.27` units and leaves final SLA backlog `0.00`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `13.06` units while average forecast error is `14.69`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 3 | 211 | 211.00 | transfer=3.63; dump_flags=1 |
| 8 | 186 | 184.35 | shortage=1.65; transfer=1.51; dump_flags=1 |
| 9 | 191 | 189.96 | shortage=1.04; transfer=1.82; dump_flags=1 |
| 2 | 195 | 195.00 | transfer=2.84; dump_flags=1 |
| 10 | 197 | 196.32 | shortage=0.68; transfer=2.15; dump_flags=1 |
| 4 | 202 | 202.00 | transfer=0.75; dump_flags=1 |
| 1 | 200 | 200.00 | dump_flags=1 |
| 5 | 184 | 184.00 | dump_flags=1 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | heuristic | 184.00 | 0.00 | 4.60 | -0.57 | 262.58 | inventory target capped quantity | forecast 184.0 + 0.0; price 4.60 + -0.57; quantity target 262.6; risk gate inventory target capped quantity; final forecast=184, price=4.60, quantity=70 |
| 0 | PremiumCloud | heuristic | 184.00 | 0.09 | 5.40 | 1.30 | 114.08 | inventory target capped quantity | forecast 184.0 + 0.1; price 5.40 + 1.30; quantity target 114.1; risk gate inventory target capped quantity; final forecast=184, price=6.80, quantity=0 |
| 0 | SpotBroker | heuristic | 184.00 | 0.00 | 4.90 | 0.12 | 73.60 | inventory target capped quantity | forecast 184.0 + 0.0; price 4.90 + 0.12; quantity target 73.6; risk gate inventory target capped quantity; final forecast=184, price=5.00, quantity=30 |
| 1 | Hyperscaler | heuristic | 184.00 | 0.00 | 4.60 | -0.55 | 302.92 | none | forecast 184.0 + 0.0; price 4.60 + -0.55; quantity target 302.9; risk gate none; final forecast=184, price=4.60, quantity=120 |
| 1 | PremiumCloud | heuristic | 184.00 | 0.09 | 5.40 | 1.32 | 124.88 | inventory target capped quantity | forecast 184.0 + 0.1; price 5.40 + 1.32; quantity target 124.9; risk gate inventory target capped quantity; final forecast=184, price=6.80, quantity=40 |
| 1 | SpotBroker | heuristic | 184.00 | 0.00 | 4.90 | 0.12 | 78.60 | inventory target capped quantity | forecast 184.0 + 0.0; price 4.90 + 0.12; quantity target 78.6; risk gate inventory target capped quantity; final forecast=184, price=5.00, quantity=60 |
| 2 | Hyperscaler | heuristic | 192.67 | 6.24 | 4.60 | -0.95 | 296.18 | inventory target capped quantity | forecast 192.7 + 6.2; price 4.60 + -0.95; quantity target 296.2; risk gate inventory target capped quantity; final forecast=200, price=4.60, quantity=110 |
| 2 | PremiumCloud | heuristic | 192.67 | 0.81 | 5.40 | 1.78 | 131.70 | inventory target capped quantity | forecast 192.7 + 0.8; price 5.40 + 1.78; quantity target 131.7; risk gate inventory target capped quantity; final forecast=195, price=7.00, quantity=30 |
| 2 | SpotBroker | heuristic | 192.67 | 8.84 | 4.90 | 0.45 | 95.30 | inventory_guard lifted price under volatility; inventory target capped quantity | forecast 192.7 + 8.8; price 4.90 + 0.45; quantity target 95.3; risk gate inventory_guard lifted price under volatility; inventory target capped quantity; final forecast=203, price=5.40, quantity=60 |
| 3 | Hyperscaler | heuristic | 192.83 | 2.35 | 4.60 | -0.89 | 292.89 | inventory target capped quantity | forecast 192.8 + 2.4; price 4.60 + -0.89; quantity target 292.9; risk gate inventory target capped quantity; final forecast=195, price=4.60, quantity=110 |
| 3 | PremiumCloud | heuristic | 192.83 | 0.24 | 5.40 | 1.72 | 130.46 | inventory target capped quantity | forecast 192.8 + 0.2; price 5.40 + 1.72; quantity target 130.5; risk gate inventory target capped quantity; final forecast=193, price=7.00, quantity=30 |
| 3 | SpotBroker | heuristic | 192.83 | 3.76 | 4.90 | 0.39 | 89.17 | inventory_guard lifted price under volatility; inventory target capped quantity | forecast 192.8 + 3.8; price 4.90 + 0.39; quantity target 89.2; risk gate inventory_guard lifted price under volatility; inventory target capped quantity; final forecast=197, price=5.60, quantity=60 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Conclusion Notes

- **Winner:** `PremiumCloud` ends with cumulative profit `1492.05`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.97`.
- **Market fulfillment:** the run sells `2273.15` units against `2279.00` true demand for a fulfillment ratio of `99.74%`.
- **Operational stress:** peer transfers total `13.06` units, customer reallocation totals `73.27`, final SLA backlog is `0.00`, with `9` dump flags and `0` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
