# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | baseline | 12 | heuristic | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit | Price Pressure Cost |
| --- | --- | --- | --- | --- | --- |
| 2298 | 2292.00 | 1.00 | 5.71 | 3305.04 | 0.00 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Price Pressure Cost | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 845.98 | 70.50 | 9.67 | 4.60 | 1260.87 | 1.00 | 0.00 | 9.87 | 0.00 | 9 | 0 | 27.17 | 0.66 | 0.00 |
| PremiumCloud | premium | 1507.91 | 125.66 | 9.92 | 6.97 | 415.08 | 0.99 | 15.07 | 0.00 | 0.00 | 0 | 0 | 1.06 | 0.96 | 6.00 |
| SpotBroker | spot | 951.16 | 79.26 | 9.92 | 5.57 | 616.06 | 1.00 | 0.00 | 5.20 | 0.00 | 0 | 0 | 25.58 | 0.93 | 0.00 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 180.00 | 5.47 | 563.12 | 1.00 | 0.00 | 15.92 | 0.67 |
| 1 | 197 | 195 | 196.33 | 5.47 | 171.98 | 0.67 | 0.00 | 4.51 | 0.41 |
| 2 | 198 | 197 | 197.59 | 5.67 | 273.53 | 0.41 | 2.91 | 9.46 | 0.29 |
| 3 | 202 | 204 | 201.71 | 5.73 | 301.91 | 0.29 | 3.09 | 10.33 | 0.21 |
| 4 | 193 | 194 | 192.79 | 5.73 | 210.39 | 0.21 | 2.56 | 8.32 | 0.15 |
| 5 | 182 | 183 | 181.85 | 5.73 | 201.54 | 0.15 | 1.92 | 6.16 | 0.10 |
| 6 | 171 | 175 | 169.60 | 5.73 | 221.46 | 1.40 | 0.00 | 4.16 | 0.87 |
| 7 | 194 | 196 | 193.13 | 5.80 | 417.54 | 0.87 | 0.12 | 0.40 | 0.48 |
| 8 | 196 | 187 | 195.52 | 5.80 | 227.19 | 0.48 | 2.05 | 7.21 | 0.32 |
| 9 | 200 | 198 | 199.68 | 5.80 | 291.46 | 0.32 | 2.37 | 8.04 | 0.21 |
| 10 | 198 | 198 | 197.79 | 5.80 | 219.19 | 0.21 | 0.05 | 0.18 | 0.12 |
| 11 | 186 | 183 | 186.00 | 5.80 | 205.73 | 0.00 | 0.00 | 0.00 | 0.00 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `baseline`, `PremiumCloud` ends first with cumulative profit `1507.91` and reputation `96.13%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `74.68` units and leaves final SLA backlog `0.00`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `15.07` units while average forecast error is `9.83`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 3 | 202 | 201.71 | shortage=0.29; transfer=3.09; dump_flags=1 |
| 2 | 198 | 197.59 | shortage=0.41; transfer=2.91; dump_flags=1 |
| 4 | 193 | 192.79 | shortage=0.21; transfer=2.56; dump_flags=1 |
| 9 | 200 | 199.68 | shortage=0.32; transfer=2.37; dump_flags=1 |
| 8 | 196 | 195.52 | shortage=0.48; transfer=2.05; dump_flags=1 |
| 5 | 182 | 181.85 | shortage=0.15; transfer=1.92; dump_flags=1 |
| 1 | 197 | 196.33 | shortage=0.67; dump_flags=1 |
| 10 | 198 | 197.79 | shortage=0.21; transfer=0.05; dump_flags=1 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | heuristic | 184.00 | 0.00 | 4.60 | -0.57 | 262.58 | inventory target capped quantity | forecast 184.0 + 0.0; price 4.60 + -0.57; quantity target 262.6; risk gate inventory target capped quantity; final forecast=184, price=4.60, quantity=70 |
| 0 | PremiumCloud | heuristic | 184.00 | 0.09 | 5.40 | 1.30 | 114.08 | inventory target capped quantity | forecast 184.0 + 0.1; price 5.40 + 1.30; quantity target 114.1; risk gate inventory target capped quantity; final forecast=184, price=6.80, quantity=0 |
| 0 | SpotBroker | heuristic | 184.00 | 0.00 | 4.90 | 0.12 | 73.60 | inventory target capped quantity | forecast 184.0 + 0.0; price 4.90 + 0.12; quantity target 73.6; risk gate inventory target capped quantity; final forecast=184, price=5.00, quantity=30 |
| 1 | Hyperscaler | heuristic | 184.00 | 0.00 | 4.60 | -0.55 | 304.68 | none | forecast 184.0 + 0.0; price 4.60 + -0.55; quantity target 304.7; risk gate none; final forecast=184, price=4.60, quantity=120 |
| 1 | PremiumCloud | heuristic | 184.00 | 0.09 | 5.40 | 1.31 | 124.88 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 184.0 + 0.1; price 5.40 + 1.31; quantity target 124.9; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=184, price=6.80, quantity=40 |
| 1 | SpotBroker | heuristic | 184.00 | 0.00 | 4.90 | 0.12 | 78.60 | inventory target capped quantity | forecast 184.0 + 0.0; price 4.90 + 0.12; quantity target 78.6; risk gate inventory target capped quantity; final forecast=184, price=5.00, quantity=60 |
| 2 | Hyperscaler | heuristic | 191.33 | 5.28 | 4.60 | -0.89 | 290.27 | inventory target capped quantity | forecast 191.3 + 5.3; price 4.60 + -0.89; quantity target 290.3; risk gate inventory target capped quantity; final forecast=198, price=4.60, quantity=110 |
| 2 | PremiumCloud | heuristic | 191.33 | 0.69 | 5.40 | 1.71 | 130.46 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 191.3 + 0.7; price 5.40 + 1.71; quantity target 130.5; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=193, price=7.00, quantity=30 |
| 2 | SpotBroker | heuristic | 191.33 | 7.48 | 4.90 | 0.40 | 92.70 | inventory_guard lifted price under volatility; inventory target capped quantity | forecast 191.3 + 7.5; price 4.90 + 0.40; quantity target 92.7; risk gate inventory_guard lifted price under volatility; inventory target capped quantity; final forecast=200, price=5.40, quantity=60 |
| 3 | Hyperscaler | heuristic | 194.17 | 3.27 | 4.60 | -0.90 | 297.69 | inventory target capped quantity | forecast 194.2 + 3.3; price 4.60 + -0.90; quantity target 297.7; risk gate inventory target capped quantity; final forecast=198, price=4.60, quantity=110 |
| 3 | PremiumCloud | heuristic | 194.17 | 0.37 | 5.40 | 1.73 | 131.70 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 194.2 + 0.4; price 5.40 + 1.73; quantity target 131.7; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=195, price=7.00, quantity=30 |
| 3 | SpotBroker | heuristic | 194.17 | 4.96 | 4.90 | 0.41 | 91.19 | inventory_guard lifted price under volatility; inventory target capped quantity | forecast 194.2 + 5.0; price 4.90 + 0.41; quantity target 91.2; risk gate inventory_guard lifted price under volatility; inventory target capped quantity; final forecast=200, price=5.60, quantity=60 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Conclusion Notes

- **Winner:** `PremiumCloud` ends with cumulative profit `1507.91`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.97`.
- **Market fulfillment:** the run sells `2292.00` units against `2298.00` true demand for a fulfillment ratio of `99.74%`.
- **Operational stress:** peer transfers total `15.07` units, customer reallocation totals `74.68`, final SLA backlog is `0.00`, with `9` dump flags and `0` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
