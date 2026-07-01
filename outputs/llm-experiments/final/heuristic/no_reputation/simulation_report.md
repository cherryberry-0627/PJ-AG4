# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | no_reputation | 12 | heuristic | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit | Price Pressure Cost |
| --- | --- | --- | --- | --- | --- |
| 2298 | 2296.73 | 1.00 | 5.57 | 3062.20 | 0.00 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Price Pressure Cost | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 767.72 | 63.98 | 9.67 | 4.60 | 1242.50 | 1.00 | 0.00 | 12.69 | 0.00 | 8 | 0 | 28.22 | 0.00 | 0.00 |
| PremiumCloud | premium | 1316.43 | 109.70 | 9.92 | 6.70 | 387.60 | 1.00 | 14.34 | 0.00 | 0.00 | 0 | 0 | 0.00 | 0.00 | 1.27 |
| SpotBroker | spot | 978.05 | 81.50 | 9.92 | 5.40 | 666.63 | 1.00 | 0.00 | 1.65 | 0.00 | 0 | 0 | 12.87 | 0.00 | 0.00 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 181.00 | 5.27 | 433.09 | 0.00 | 1.17 | 3.58 | 0.00 |
| 1 | 197 | 195 | 197.00 | 5.27 | 229.88 | 0.00 | 3.27 | 10.00 | 0.00 |
| 2 | 198 | 197 | 198.00 | 5.47 | 251.86 | 0.00 | 1.98 | 6.23 | 0.00 |
| 3 | 202 | 204 | 202.00 | 5.53 | 280.71 | 0.00 | 2.38 | 7.77 | 0.00 |
| 4 | 193 | 194 | 191.73 | 5.60 | 181.91 | 1.27 | 0.00 | 4.15 | 0.76 |
| 5 | 182 | 183 | 182.00 | 5.60 | 155.72 | 0.00 | 0.00 | 0.00 | 0.00 |
| 6 | 171 | 175 | 171.00 | 5.60 | 216.42 | 0.00 | 0.00 | 0.00 | 0.00 |
| 7 | 194 | 196 | 194.00 | 5.73 | 393.84 | 0.00 | 0.07 | 0.23 | 0.00 |
| 8 | 196 | 187 | 196.00 | 5.73 | 218.75 | 0.00 | 0.93 | 3.21 | 0.00 |
| 9 | 200 | 198 | 200.00 | 5.67 | 274.34 | 0.00 | 1.74 | 5.97 | 0.00 |
| 10 | 198 | 198 | 198.00 | 5.67 | 223.02 | 0.00 | 1.65 | 5.68 | 0.00 |
| 11 | 186 | 183 | 186.00 | 5.67 | 202.66 | 0.00 | 1.14 | 3.92 | 0.00 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `no_reputation`, `PremiumCloud` ends first with cumulative profit `1316.43` and reputation `0.00%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `50.73` units and leaves final SLA backlog `0.00`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `14.34` units while average forecast error is `9.83`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 3 | 202 | 202.00 | transfer=2.38; dump_flags=1 |
| 2 | 198 | 198.00 | transfer=1.98; dump_flags=1 |
| 9 | 200 | 200.00 | transfer=1.74; dump_flags=1 |
| 10 | 198 | 198.00 | transfer=1.65; dump_flags=1 |
| 4 | 193 | 191.73 | shortage=1.27; dump_flags=1 |
| 11 | 186 | 186.00 | transfer=1.14; dump_flags=1 |
| 8 | 196 | 196.00 | transfer=0.93; dump_flags=1 |
| 5 | 182 | 182.00 | dump_flags=1 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | heuristic | 184.00 | 0.00 | 4.60 | -0.69 | 262.58 | inventory target capped quantity | forecast 184.0 + 0.0; price 4.60 + -0.69; quantity target 262.6; risk gate inventory target capped quantity; final forecast=184, price=4.60, quantity=80 |
| 0 | PremiumCloud | heuristic | 184.00 | 0.00 | 5.40 | 0.85 | 114.08 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 184.0 + 0.0; price 5.40 + 0.85; quantity target 114.1; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=184, price=6.20, quantity=0 |
| 0 | SpotBroker | heuristic | 184.00 | 0.00 | 4.90 | 0.12 | 73.60 | inventory target capped quantity | forecast 184.0 + 0.0; price 4.90 + 0.12; quantity target 73.6; risk gate inventory target capped quantity; final forecast=184, price=5.00, quantity=50 |
| 1 | Hyperscaler | heuristic | 184.00 | 0.00 | 4.60 | -0.69 | 267.78 | inventory target capped quantity | forecast 184.0 + 0.0; price 4.60 + -0.69; quantity target 267.8; risk gate inventory target capped quantity; final forecast=184, price=4.60, quantity=100 |
| 1 | PremiumCloud | heuristic | 184.00 | 0.00 | 5.40 | 0.85 | 124.88 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 184.0 + 0.0; price 5.40 + 0.85; quantity target 124.9; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=184, price=6.20, quantity=30 |
| 1 | SpotBroker | heuristic | 184.00 | 0.00 | 4.90 | 0.12 | 76.65 | inventory target capped quantity | forecast 184.0 + 0.0; price 4.90 + 0.12; quantity target 76.6; risk gate inventory target capped quantity; final forecast=184, price=5.00, quantity=70 |
| 2 | Hyperscaler | heuristic | 191.33 | 5.28 | 4.60 | -1.02 | 292.42 | inventory target capped quantity | forecast 191.3 + 5.3; price 4.60 + -1.02; quantity target 292.4; risk gate inventory target capped quantity; final forecast=198, price=4.60, quantity=110 |
| 2 | PremiumCloud | heuristic | 191.33 | 0.60 | 5.40 | 1.23 | 130.46 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 191.3 + 0.6; price 5.40 + 1.23; quantity target 130.5; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=193, price=6.60, quantity=30 |
| 2 | SpotBroker | heuristic | 191.33 | 7.48 | 4.90 | 0.40 | 89.89 | inventory_guard lifted price under volatility; inventory target capped quantity | forecast 191.3 + 7.5; price 4.90 + 0.40; quantity target 89.9; risk gate inventory_guard lifted price under volatility; inventory target capped quantity; final forecast=200, price=5.20, quantity=60 |
| 3 | Hyperscaler | heuristic | 194.17 | 3.27 | 4.60 | -1.03 | 289.72 | inventory target capped quantity | forecast 194.2 + 3.3; price 4.60 + -1.03; quantity target 289.7; risk gate inventory target capped quantity; final forecast=198, price=4.60, quantity=110 |
| 3 | PremiumCloud | heuristic | 194.17 | 0.28 | 5.40 | 1.25 | 131.70 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 194.2 + 0.3; price 5.40 + 1.25; quantity target 131.7; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=195, price=6.60, quantity=30 |
| 3 | SpotBroker | heuristic | 194.17 | 4.96 | 4.90 | 0.41 | 91.95 | inventory target capped quantity | forecast 194.2 + 5.0; price 4.90 + 0.41; quantity target 91.9; risk gate inventory target capped quantity; final forecast=200, price=5.40, quantity=60 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Conclusion Notes

- **Winner:** `PremiumCloud` ends with cumulative profit `1316.43`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.70`.
- **Market fulfillment:** the run sells `2296.73` units against `2298.00` true demand for a fulfillment ratio of `99.94%`.
- **Operational stress:** peer transfers total `14.34` units, customer reallocation totals `50.73`, final SLA backlog is `0.00`, with `8` dump flags and `0` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
