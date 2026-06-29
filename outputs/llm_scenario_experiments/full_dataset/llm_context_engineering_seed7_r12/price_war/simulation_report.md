# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | price_war | 12 | llm-context | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit | Price Pressure Cost |
| --- | --- | --- | --- | --- | --- |
| 2298 | 2242.34 | 0.98 | 5.66 | 3045.81 | 230.04 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Price Pressure Cost | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 929.87 | 77.49 | 8.50 | 4.60 | 1416.13 | 0.98 | 0.00 | 0.00 | 170.51 | 11 | 0 | 0.00 | 0.62 | 35.72 |
| PremiumCloud | premium | 1344.80 | 112.07 | 5.67 | 6.60 | 394.62 | 1.00 | 0.00 | 22.45 | 7.02 | 0 | 0 | 2.19 | 0.83 | 0.00 |
| SpotBroker | spot | 771.14 | 64.26 | 4.58 | 5.77 | 431.60 | 0.96 | 22.45 | 0.00 | 52.50 | 0 | 2 | 0.00 | 0.78 | 19.93 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 180.00 | 5.33 | 501.68 | 1.00 | 11.08 | 28.09 | 0.18 |
| 1 | 197 | 195 | 189.82 | 5.53 | 211.90 | 7.18 | 11.37 | 3.23 | 1.16 |
| 2 | 198 | 197 | 188.84 | 5.67 | 226.38 | 9.16 | 0.00 | 7.16 | 1.05 |
| 3 | 202 | 204 | 195.74 | 5.73 | 245.96 | 6.26 | 0.00 | 16.59 | 0.69 |
| 4 | 193 | 194 | 187.34 | 5.80 | 198.77 | 5.66 | 0.00 | 14.95 | 0.61 |
| 5 | 182 | 183 | 181.39 | 5.67 | 231.51 | 0.61 | 0.00 | 6.82 | 0.06 |
| 6 | 171 | 175 | 163.41 | 5.60 | 161.75 | 7.59 | 0.00 | 3.31 | 1.56 |
| 7 | 194 | 196 | 189.87 | 5.73 | 288.22 | 4.13 | 0.00 | 12.89 | 0.46 |
| 8 | 196 | 187 | 192.56 | 5.67 | 260.46 | 3.44 | 0.00 | 14.11 | 0.69 |
| 9 | 200 | 198 | 194.95 | 5.73 | 199.10 | 5.05 | 0.00 | 15.56 | 0.57 |
| 10 | 198 | 198 | 192.97 | 5.73 | 262.39 | 5.03 | 0.00 | 14.23 | 0.56 |
| 11 | 186 | 183 | 185.44 | 5.67 | 257.72 | 0.56 | 0.00 | 11.19 | 0.06 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `price_war`, `PremiumCloud` ends first with cumulative profit `1344.80` and reputation `82.88%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `148.13` units and leaves final SLA backlog `0.06`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `22.45` units while average forecast error is `6.25`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 1 | 197 | 189.82 | shortage=7.18; transfer=11.37; dump_flags=1; default_flags=1 |
| 6 | 171 | 163.41 | shortage=7.59; dump_flags=1; default_flags=1 |
| 2 | 198 | 188.84 | shortage=9.16; dump_flags=1 |
| 3 | 202 | 195.74 | shortage=6.26; dump_flags=1 |
| 4 | 193 | 187.34 | shortage=5.66; dump_flags=1 |
| 9 | 200 | 194.95 | shortage=5.05; dump_flags=1 |
| 10 | 198 | 192.97 | shortage=5.03; dump_flags=1 |
| 7 | 194 | 189.87 | shortage=4.13; dump_flags=1 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm-context | 184.00 | 6.00 | 4.60 | 0.00 | 100.00 | inventory target capped quantity | forecast 184.0 + 6.0; price 4.60 + 0.00; quantity target 100.0; risk gate inventory target capped quantity; final forecast=190, price=4.60, quantity=80 |
| 0 | PremiumCloud | llm-context | 184.00 | -4.00 | 6.80 | -0.20 | 30.00 | inventory target capped quantity | forecast 184.0 + -4.0; price 6.80 + -0.20; quantity target 30.0; risk gate inventory target capped quantity; final forecast=180, price=6.60, quantity=0 |
| 0 | SpotBroker | llm-context | 184.00 | -4.00 | 5.00 | -0.20 | 20.00 | none | forecast 184.0 + -4.0; price 5.00 + -0.20; quantity target 20.0; risk gate none; final forecast=180, price=4.80, quantity=20 |
| 1 | Hyperscaler | llm-context | 184.00 | 26.00 | 4.60 | 0.00 | 120.00 | none | forecast 184.0 + 26.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=210, price=4.60, quantity=120 |
| 1 | PremiumCloud | llm-context | 184.00 | 6.00 | 6.80 | -0.20 | 40.00 | none | forecast 184.0 + 6.0; price 6.80 + -0.20; quantity target 40.0; risk gate none; final forecast=190, price=6.60, quantity=40 |
| 1 | SpotBroker | llm-context | 184.00 | 16.00 | 5.00 | 0.40 | 30.00 | none | forecast 184.0 + 16.0; price 5.00 + 0.40; quantity target 30.0; risk gate none; final forecast=200, price=5.40, quantity=30 |
| 2 | Hyperscaler | llm-context | 198.00 | 12.00 | 4.60 | 0.00 | 120.00 | none | forecast 198.0 + 12.0; price 4.60 + 0.00; quantity target 120.0; risk gate none; final forecast=210, price=4.60, quantity=120 |
| 2 | PremiumCloud | llm-context | 193.00 | 3.00 | 7.00 | -0.40 | 30.00 | none | forecast 193.0 + 3.0; price 7.00 + -0.40; quantity target 30.0; risk gate none; final forecast=196, price=6.60, quantity=30 |
| 2 | SpotBroker | llm-context | 200.00 | 5.00 | 5.40 | 0.40 | 40.00 | none | forecast 200.0 + 5.0; price 5.40 + 0.40; quantity target 40.0; risk gate none; final forecast=205, price=5.80, quantity=40 |
| 3 | Hyperscaler | llm-context | 200.00 | 15.00 | 4.60 | 0.00 | 120.00 | growth_tolerant added capacity after shortage | forecast 200.0 + 15.0; price 4.60 + 0.00; quantity target 120.0; risk gate growth_tolerant added capacity after shortage; final forecast=215, price=4.60, quantity=120 |
| 3 | PremiumCloud | llm-context | 195.00 | 5.00 | 7.00 | -0.40 | 40.00 | none | forecast 195.0 + 5.0; price 7.00 + -0.40; quantity target 40.0; risk gate none; final forecast=200, price=6.60, quantity=40 |
| 3 | SpotBroker | llm-context | 200.00 | 8.00 | 5.60 | 0.40 | 40.00 | none | forecast 200.0 + 8.0; price 5.60 + 0.40; quantity target 40.0; risk gate none; final forecast=208, price=6.00, quantity=40 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Conclusion Notes

- **Winner:** `PremiumCloud` ends with cumulative profit `1344.80`, the highest value in this run.
- **Service leader:** `PremiumCloud` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.60`.
- **Market fulfillment:** the run sells `2242.34` units against `2298.00` true demand for a fulfillment ratio of `97.58%`.
- **Operational stress:** peer transfers total `22.45` units, customer reallocation totals `148.13`, final SLA backlog is `0.06`, with `11` dump flags and `2` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
