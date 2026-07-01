# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | high_volatility | 12 | llm-context | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit | Price Pressure Cost |
| --- | --- | --- | --- | --- | --- |
| 2279 | 2220.78 | 0.97 | 5.44 | 3211.96 | 0.00 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Price Pressure Cost | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 974.12 | 81.18 | 12.67 | 4.60 | 1271.85 | 1.00 | 0.00 | 4.38 | 0.00 | 7 | 0 | 13.55 | 0.71 | 0.00 |
| PremiumCloud | premium | 1452.13 | 121.01 | 8.00 | 6.20 | 520.51 | 0.96 | 1.63 | 0.51 | 0.00 | 0 | 2 | 2.20 | 0.83 | 21.69 |
| SpotBroker | spot | 785.71 | 65.48 | 5.00 | 5.52 | 428.43 | 0.93 | 3.25 | 0.00 | 0.00 | 0 | 3 | 0.00 | 0.84 | 36.53 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 179 | 184 | 179.00 | 5.20 | 504.93 | 0.00 | 0.00 | 25.64 | 0.00 |
| 1 | 200 | 197 | 179.35 | 5.33 | 225.30 | 20.65 | 0.00 | 27.98 | 5.09 |
| 2 | 195 | 193 | 189.91 | 5.40 | 223.36 | 5.09 | 0.00 | 20.45 | 1.19 |
| 3 | 211 | 215 | 203.06 | 5.47 | 270.00 | 7.94 | 0.33 | 19.44 | 5.01 |
| 4 | 202 | 204 | 197.26 | 5.53 | 249.59 | 4.74 | 1.30 | 4.79 | 2.50 |
| 5 | 184 | 186 | 181.50 | 5.47 | 191.92 | 2.50 | 2.75 | 6.84 | 1.20 |
| 6 | 155 | 164 | 152.69 | 5.40 | 168.64 | 2.31 | 0.00 | 7.89 | 0.77 |
| 7 | 193 | 198 | 192.23 | 5.47 | 329.39 | 0.77 | 0.00 | 9.76 | 0.25 |
| 8 | 186 | 169 | 174.54 | 5.47 | 295.23 | 11.46 | 0.00 | 10.57 | 5.12 |
| 9 | 191 | 186 | 189.58 | 5.47 | 207.66 | 1.42 | 0.51 | 1.93 | 0.42 |
| 10 | 197 | 197 | 196.25 | 5.53 | 276.76 | 0.75 | 0.00 | 1.17 | 0.23 |
| 11 | 186 | 180 | 185.42 | 5.53 | 269.18 | 0.58 | 0.00 | 1.22 | 0.18 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `high_volatility`, `PremiumCloud` ends first with cumulative profit `1452.13` and reputation `83.25%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `137.69` units and leaves final SLA backlog `0.18`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `4.88` units while average forecast error is `8.56`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 1 | 200 | 179.35 | shortage=20.65; dump_flags=1; default_flags=1 |
| 8 | 186 | 174.54 | shortage=11.46; default_flags=2 |
| 3 | 211 | 203.06 | shortage=7.94; transfer=0.33; dump_flags=1; default_flags=1 |
| 2 | 195 | 189.91 | shortage=5.09; dump_flags=1; default_flags=1 |
| 4 | 202 | 197.26 | shortage=4.74; transfer=1.30; dump_flags=1 |
| 5 | 184 | 181.50 | shortage=2.50; transfer=2.75; dump_flags=1 |
| 9 | 191 | 189.58 | shortage=1.42; transfer=0.51; dump_flags=1 |
| 10 | 197 | 196.25 | shortage=0.75; dump_flags=1 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm-context | 184.00 | 6.00 | 4.60 | 0.00 | 80.00 | inventory target capped quantity | forecast 184.0 + 6.0; price 4.60 + 0.00; quantity target 80.0; risk gate inventory target capped quantity; final forecast=190, price=4.60, quantity=80 |
| 0 | PremiumCloud | llm-context | 184.00 | -4.00 | 6.80 | -0.60 | 40.00 | inventory target capped quantity | forecast 184.0 + -4.0; price 6.80 + -0.60; quantity target 40.0; risk gate inventory target capped quantity; final forecast=180, price=6.20, quantity=10 |
| 0 | SpotBroker | llm-context | 184.00 | 0.00 | 5.00 | -0.20 | 20.00 | none | forecast 184.0 + 0.0; price 5.00 + -0.20; quantity target 20.0; risk gate none; final forecast=184, price=4.80, quantity=20 |
| 1 | Hyperscaler | llm-context | 184.00 | 26.00 | 4.60 | 0.00 | 110.00 | none | forecast 184.0 + 26.0; price 4.60 + 0.00; quantity target 110.0; risk gate none; final forecast=210, price=4.60, quantity=110 |
| 1 | PremiumCloud | llm-context | 184.00 | 6.00 | 6.80 | -0.60 | 30.00 | none | forecast 184.0 + 6.0; price 6.80 + -0.60; quantity target 30.0; risk gate none; final forecast=190, price=6.20, quantity=30 |
| 1 | SpotBroker | llm-context | 184.00 | 16.00 | 5.00 | 0.20 | 30.00 | none | forecast 184.0 + 16.0; price 5.00 + 0.20; quantity target 30.0; risk gate none; final forecast=200, price=5.20, quantity=30 |
| 2 | Hyperscaler | llm-context | 200.00 | 10.00 | 4.60 | 0.00 | 120.00 | none | forecast 200.0 + 10.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=210, price=4.60, quantity=120 |
| 2 | PremiumCloud | llm-context | 195.00 | -5.00 | 7.00 | -0.80 | 40.00 | none | forecast 195.0 + -5.0; price 7.00 + -0.80; quantity target 40.0; risk gate none; final forecast=190, price=6.20, quantity=40 |
| 2 | SpotBroker | llm-context | 203.00 | -13.00 | 5.20 | 0.20 | 40.00 | none | forecast 203.0 + -13.0; price 5.20 + 0.20; quantity target 40.0; risk gate none; final forecast=190, price=5.40, quantity=40 |
| 3 | Hyperscaler | llm-context | 195.00 | 25.00 | 4.60 | 0.00 | 120.00 | none | forecast 195.0 + 25.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=220, price=4.60, quantity=120 |
| 3 | PremiumCloud | llm-context | 193.00 | 7.00 | 7.00 | -0.80 | 40.00 | none | forecast 193.0 + 7.0; price 7.00 + -0.80; quantity target 40.0; risk gate none; final forecast=200, price=6.20, quantity=40 |
| 3 | SpotBroker | llm-context | 197.00 | 18.00 | 5.40 | 0.20 | 50.00 | inventory target capped quantity | forecast 197.0 + 18.0; price 5.40 + 0.20; quantity target 50.0; risk gate inventory target capped quantity; final forecast=215, price=5.60, quantity=40 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Conclusion Notes

- **Winner:** `PremiumCloud` ends with cumulative profit `1452.13`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.20`.
- **Market fulfillment:** the run sells `2220.78` units against `2279.00` true demand for a fulfillment ratio of `97.45%`.
- **Operational stress:** peer transfers total `4.88` units, customer reallocation totals `137.69`, final SLA backlog is `0.18`, with `7` dump flags and `5` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
