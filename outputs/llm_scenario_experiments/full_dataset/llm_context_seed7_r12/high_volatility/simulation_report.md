# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | high_volatility | 12 | llm-context | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit | Price Pressure Cost |
| --- | --- | --- | --- | --- | --- |
| 2279 | 2234.85 | 0.98 | 5.61 | 3403.94 | 0.00 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Price Pressure Cost | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 1023.62 | 85.30 | 9.42 | 4.60 | 1334.27 | 1.00 | 0.00 | 1.12 | 0.00 | 9 | 0 | 10.70 | 0.66 | 0.74 |
| PremiumCloud | premium | 1506.57 | 125.55 | 7.75 | 6.60 | 460.32 | 0.95 | 0.00 | 0.59 | 0.00 | 0 | 3 | 0.00 | 0.95 | 25.53 |
| SpotBroker | spot | 873.75 | 72.81 | 4.75 | 5.62 | 440.25 | 0.96 | 1.71 | 0.00 | 0.00 | 0 | 2 | 0.00 | 0.88 | 17.89 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 179 | 184 | 179.00 | 5.27 | 531.64 | 0.00 | 0.00 | 35.98 | 0.00 |
| 1 | 200 | 197 | 190.85 | 5.40 | 232.84 | 9.15 | 0.00 | 29.11 | 4.85 |
| 2 | 195 | 193 | 185.15 | 5.53 | 240.33 | 9.85 | 0.00 | 20.02 | 4.84 |
| 3 | 211 | 215 | 195.16 | 5.60 | 255.68 | 15.84 | 0.00 | 2.35 | 6.09 |
| 4 | 202 | 204 | 193.91 | 5.67 | 274.44 | 8.09 | 0.00 | 0.00 | 3.06 |
| 5 | 184 | 186 | 182.78 | 5.73 | 219.59 | 1.22 | 0.00 | 0.00 | 0.61 |
| 6 | 155 | 164 | 155.00 | 5.60 | 184.95 | 0.00 | 1.12 | 4.41 | 0.00 |
| 7 | 193 | 198 | 193.00 | 5.67 | 303.07 | 0.00 | 0.59 | 2.41 | 0.00 |
| 8 | 186 | 169 | 186.00 | 5.67 | 317.51 | 0.00 | 0.00 | 4.13 | 0.00 |
| 9 | 191 | 186 | 191.00 | 5.67 | 290.43 | 0.00 | 0.00 | 7.92 | 0.00 |
| 10 | 197 | 197 | 197.00 | 5.73 | 278.56 | 0.00 | 0.00 | 9.55 | 0.00 |
| 11 | 186 | 180 | 186.00 | 5.73 | 274.91 | 0.00 | 0.00 | 6.36 | 0.00 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `high_volatility`, `PremiumCloud` ends first with cumulative profit `1506.57` and reputation `95.26%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `122.25` units and leaves final SLA backlog `0.00`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `1.71` units while average forecast error is `7.31`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 3 | 211 | 195.16 | shortage=15.84; dump_flags=1; default_flags=2 |
| 2 | 195 | 185.15 | shortage=9.85; dump_flags=1; default_flags=2 |
| 1 | 200 | 190.85 | shortage=9.15; dump_flags=1; default_flags=1 |
| 4 | 202 | 193.91 | shortage=8.09; dump_flags=1 |
| 5 | 184 | 182.78 | shortage=1.22; dump_flags=1 |
| 7 | 193 | 193.00 | transfer=0.59; dump_flags=1 |
| 9 | 191 | 191.00 | dump_flags=1 |
| 10 | 197 | 197.00 | dump_flags=1 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm-context | 184.00 | 6.00 | 4.60 | 0.00 | 80.00 | inventory target capped quantity | forecast 184.0 + 6.0; price 4.60 + 0.00; quantity target 80.0; risk gate inventory target capped quantity; final forecast=190, price=4.60, quantity=80 |
| 0 | PremiumCloud | llm-context | 184.00 | -4.00 | 6.80 | -0.20 | 30.00 | inventory target capped quantity | forecast 184.0 + -4.0; price 6.80 + -0.20; quantity target 30.0; risk gate inventory target capped quantity; final forecast=180, price=6.60, quantity=0 |
| 0 | SpotBroker | llm-context | 184.00 | -4.00 | 5.00 | -0.40 | 20.00 | none | forecast 184.0 + -4.0; price 5.00 + -0.40; quantity target 20.0; risk gate none; final forecast=180, price=4.60, quantity=20 |
| 1 | Hyperscaler | llm-context | 184.00 | 26.00 | 4.60 | 0.00 | 120.00 | none | forecast 184.0 + 26.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=210, price=4.60, quantity=120 |
| 1 | PremiumCloud | llm-context | 184.00 | 6.00 | 6.80 | -0.20 | 40.00 | inventory target capped quantity | forecast 184.0 + 6.0; price 6.80 + -0.20; quantity target 40.0; risk gate inventory target capped quantity; final forecast=190, price=6.60, quantity=40 |
| 1 | SpotBroker | llm-context | 184.00 | 14.00 | 5.00 | 0.00 | 30.00 | none | forecast 184.0 + 14.0; price 5.00 + 0.00; quantity target 30.0; risk gate none; final forecast=198, price=5.00, quantity=30 |
| 2 | Hyperscaler | llm-context | 200.00 | 10.00 | 4.60 | 0.00 | 120.00 | none | forecast 200.0 + 10.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=210, price=4.60, quantity=120 |
| 2 | PremiumCloud | llm-context | 195.00 | 0.00 | 7.00 | -0.40 | 50.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 195.0 + 0.0; price 7.00 + -0.40; quantity target 50.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=195, price=6.60, quantity=40 |
| 2 | SpotBroker | llm-context | 203.00 | -8.00 | 5.40 | -0.20 | 30.00 | inventory_guard lifted price under volatility | forecast 203.0 + -8.0; price 5.40 + -0.20; quantity target 30.0; risk gate inventory_guard lifted price under volatility; final forecast=195, price=5.40, quantity=30 |
| 3 | Hyperscaler | llm-context | 195.00 | 25.00 | 4.60 | 0.00 | 120.00 | none | forecast 195.0 + 25.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=220, price=4.60, quantity=120 |
| 3 | PremiumCloud | llm-context | 193.00 | 7.00 | 7.00 | -0.40 | 50.00 | sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity | forecast 193.0 + 7.0; price 7.00 + -0.40; quantity target 50.0; risk gate sla_guard reduced quantity under SLA/reputation pressure; inventory target capped quantity; final forecast=200, price=6.60, quantity=40 |
| 3 | SpotBroker | llm-context | 197.00 | 13.00 | 5.40 | 0.20 | 40.00 | none | forecast 197.0 + 13.0; price 5.40 + 0.20; quantity target 40.0; risk gate none; final forecast=210, price=5.60, quantity=40 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Conclusion Notes

- **Winner:** `PremiumCloud` ends with cumulative profit `1506.57`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `99.95%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.60`.
- **Market fulfillment:** the run sells `2234.85` units against `2279.00` true demand for a fulfillment ratio of `98.06%`.
- **Operational stress:** peer transfers total `1.71` units, customer reallocation totals `122.25`, final SLA backlog is `0.00`, with `9` dump flags and `5` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
