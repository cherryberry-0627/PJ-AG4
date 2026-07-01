# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | high_volatility | 12 | llm-adaptive | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit |
| --- | --- | --- | --- | --- |
| 2279 | 2253.58 | 0.99 | 5.83 | 3706.56 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 1511.97 | 126.00 | 35.75 | 4.97 | 1364.14 | 1.00 | 0.00 | 28.61 | 0 | 0 | 0.00 | 0.97 | 0.00 |
| PremiumCloud | premium | 1063.95 | 88.66 | 23.33 | 6.77 | 305.95 | 0.93 | 33.85 | 0.00 | 0 | 3 | 0.00 | 0.89 | 19.12 |
| SpotBroker | spot | 1130.64 | 94.22 | 61.08 | 5.77 | 583.49 | 0.99 | 0.00 | 5.25 | 0 | 1 | 5.72 | 0.87 | 6.31 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 179 | 184 | 179.00 | 5.47 | 572.70 | 0.00 | 0.00 | 23.65 | 0.00 |
| 1 | 200 | 197 | 200.00 | 5.53 | 246.21 | 0.00 | 8.03 | 13.32 | 0.00 |
| 2 | 195 | 193 | 195.00 | 5.80 | 287.53 | 0.00 | 6.80 | 21.92 | 0.00 |
| 3 | 211 | 215 | 202.17 | 5.80 | 338.18 | 8.83 | 0.00 | 28.03 | 4.13 |
| 4 | 202 | 204 | 199.47 | 5.87 | 266.47 | 2.53 | 3.13 | 10.94 | 1.68 |
| 5 | 184 | 186 | 182.32 | 5.87 | 244.53 | 1.68 | 2.12 | 7.24 | 1.03 |
| 6 | 155 | 164 | 150.97 | 5.93 | 91.27 | 4.03 | 0.00 | 10.68 | 2.91 |
| 7 | 193 | 198 | 190.09 | 5.93 | 398.99 | 2.91 | 3.81 | 13.43 | 2.18 |
| 8 | 186 | 169 | 183.82 | 5.93 | 258.90 | 2.18 | 0.42 | 1.50 | 1.07 |
| 9 | 191 | 186 | 189.93 | 5.93 | 343.19 | 1.07 | 0.00 | 16.84 | 0.87 |
| 10 | 197 | 197 | 196.13 | 5.93 | 348.25 | 0.87 | 4.59 | 12.59 | 0.63 |
| 11 | 186 | 180 | 184.68 | 6.00 | 310.36 | 1.32 | 4.97 | 21.54 | 1.32 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `high_volatility`, `Hyperscaler` ends first with cumulative profit `1511.97` and reputation `96.60%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `181.67` units and leaves final SLA backlog `1.32`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `33.85` units while average forecast error is `40.06`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 3 | 211 | 202.17 | shortage=8.83; default_flags=2 |
| 7 | 193 | 190.09 | shortage=2.91; transfer=3.81; default_flags=1 |
| 6 | 155 | 150.97 | shortage=4.03; default_flags=1 |
| 1 | 200 | 200.00 | transfer=8.03 |
| 2 | 195 | 195.00 | transfer=6.80 |
| 11 | 186 | 184.68 | shortage=1.32; transfer=4.97 |
| 4 | 202 | 199.47 | shortage=2.53; transfer=3.13 |
| 10 | 197 | 196.13 | shortage=0.87; transfer=4.59 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm-adaptive | 184.00 | 4.00 | 4.60 | 0.20 | 90.00 | inventory target capped quantity | adaptive state risk=0.72, price=0.68, demand=0.62, inventory=0.34, shock=0.48, rivals=0.46; last update: initial strategy prior; fallback forecast=184, price=4.60, quantity=70; final forecast=188, price=4.80, quantity=70 |
| 0 | PremiumCloud | llm-adaptive | 184.00 | -1.00 | 6.80 | -0.20 | 0.00 | none | adaptive state risk=0.38, price=0.58, demand=0.46, inventory=0.72, shock=0.36, rivals=0.32; last update: initial strategy prior; fallback forecast=184, price=6.80, quantity=0; final forecast=183, price=6.60, quantity=0 |
| 0 | SpotBroker | llm-adaptive | 184.00 | 3.00 | 5.00 | 0.00 | 30.00 | none | adaptive state risk=0.56, price=0.44, demand=0.58, inventory=0.54, shock=0.76, rivals=0.78; last update: initial strategy prior; fallback forecast=184, price=5.00, quantity=30; final forecast=187, price=5.00, quantity=30 |
| 1 | Hyperscaler | llm-adaptive | 184.00 | 4.00 | 4.60 | 0.20 | 120.00 | inventory target capped quantity | adaptive state risk=0.75, price=0.70, demand=0.63, inventory=0.32, shock=0.48, rivals=0.47; last update: Captured dominant 55.3% market share with near-zero leftover inventory. Slightly decreasing inventory caution and increasing risk tolerance to ensure we maintain capacity readiness and do not experience shortages as we continue targeting high throughput.; fallback forecast=184, price=4.60, quantity=120; final forecast=188, price=4.80, quantity=120 |
| 1 | PremiumCloud | llm-adaptive | 184.00 | -1.00 | 6.80 | -0.20 | 30.00 | none | adaptive state risk=0.39, price=0.57, demand=0.46, inventory=0.73, shock=0.36, rivals=0.31; last update: Achieved market-leading profit and perfect SLA reliability in the opening round. We maintain our highly successful premium positioning, slightly reducing competitor reactivity to defend our independent pricing discipline, while marginally increasing inventory caution to lock in service stability.; fallback forecast=184, price=6.80, quantity=40; final forecast=183, price=6.60, quantity=30 |
| 1 | SpotBroker | llm-adaptive | 184.00 | 4.00 | 5.00 | 0.20 | 60.00 | inventory target capped quantity | adaptive state risk=0.58, price=0.51, demand=0.62, inventory=0.59, shock=0.82, rivals=0.85; last update: Competitor average price (5.70) is significantly higher than our price (5.00), and we ended with zero inventory. Increasing price aggressiveness and competitor reactivity will close this gap. Elevating inventory caution and shock responsiveness maintains our agile, light-inventory profile to exploit market volatility.; fallback forecast=184, price=5.00, quantity=60; final forecast=188, price=5.20, quantity=60 |
| 2 | Hyperscaler | llm-adaptive | 200.00 | 25.00 | 4.60 | 0.40 | 120.00 | none | adaptive state risk=0.78, price=0.72, demand=0.65, inventory=0.29, shock=0.49, rivals=0.49; last update: Captured over 50% market share in Round 1. To sustain scale dominance and prevent future capacity limits, we are decreasing inventory caution and boosting risk tolerance for stronger readiness. Price aggressiveness and competitor reactivity are slightly elevated to maintain a high-throughput advantage over higher-priced rivals.; fallback forecast=200, price=4.60, quantity=120; final forecast=225, price=5.00, quantity=120 |
| 2 | PremiumCloud | llm-adaptive | 195.00 | 13.00 | 7.00 | -0.20 | 20.00 | none | adaptive state risk=0.39, price=0.57, demand=0.47, inventory=0.74, shock=0.36, rivals=0.30; last update: Achieved the highest market profit with a 1.0 service rate. Maintaining strong price discipline and brand reputation by slightly reducing competitor reactivity, while marginally increasing risk tolerance and demand sensitivity due to our strong performance buffer.; fallback forecast=195, price=7.00, quantity=30; final forecast=208, price=6.80, quantity=20 |
| 2 | SpotBroker | llm-adaptive | 203.00 | 37.00 | 5.60 | 0.00 | 60.00 | none | adaptive state risk=0.60, price=0.56, demand=0.63, inventory=0.62, shock=0.82, rivals=0.87; last update: Increasing price aggressiveness and competitor reactivity to tactically close the gap with higher competitor average prices while preserving inventory flexibility.; fallback forecast=203, price=5.60, quantity=60; final forecast=240, price=5.60, quantity=60 |
| 3 | Hyperscaler | llm-adaptive | 195.00 | 22.00 | 4.60 | 0.40 | 120.00 | none | adaptive state risk=0.80, price=0.74, demand=0.67, inventory=0.28, shock=0.49, rivals=0.48; last update: Secured top profit and 56.8% market share this round. Slightly increasing risk tolerance and price aggressiveness to sustain market dominance, while reducing inventory caution to support capacity readiness and absorb potential demand spikes.; fallback forecast=195, price=4.60, quantity=120; final forecast=217, price=5.00, quantity=120 |
| 3 | PremiumCloud | llm-adaptive | 193.00 | 10.00 | 7.00 | -0.20 | 20.00 | none | adaptive state risk=0.40, price=0.57, demand=0.48, inventory=0.75, shock=0.35, rivals=0.29; last update: Maintained a perfect 1.0 SLA service rate and achieved solid profits with zero leftover inventory. We will slightly increase inventory caution to safeguard our flawless SLA record against stockouts. We decline to react to low-cost competitors, preserving our premium price discipline and brand positioning.; fallback forecast=193, price=7.00, quantity=30; final forecast=203, price=6.80, quantity=20 |
| 3 | SpotBroker | llm-adaptive | 197.00 | 30.00 | 5.60 | 0.00 | 50.00 | none | adaptive state risk=0.58, price=0.60, demand=0.60, inventory=0.68, shock=0.83, rivals=0.89; last update: Responding to underpricing relative to competitor average (5.6 vs 5.9) by increasing price aggressiveness and reactivity. Simultaneously boosting inventory caution and slightly reducing risk tolerance to correct the positive forecast error and maintain a lean, flexible inventory.; fallback forecast=197, price=5.60, quantity=50; final forecast=227, price=5.60, quantity=50 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | Scale aggressor | 0.02 | -0.02 | 0.03 | 0.70 | 0.32 | 0.75 | Captured dominant 55.3% market share with near-zero leftover inventory. Slightly decreasing inventory caution and increasing risk tolerance to ensure we maintain capacity readiness and do not experience shortages as we continue targeting high throughput. |
| 0 | PremiumCloud | Reputation guardian | -0.01 | 0.01 | 0.01 | 0.57 | 0.73 | 0.39 | Achieved market-leading profit and perfect SLA reliability in the opening round. We maintain our highly successful premium positioning, slightly reducing competitor reactivity to defend our independent pricing discipline, while marginally increasing inventory caution to lock in service stability. |
| 0 | SpotBroker | Agile spread hunter | 0.07 | 0.05 | 0.02 | 0.51 | 0.59 | 0.58 | Competitor average price (5.70) is significantly higher than our price (5.00), and we ended with zero inventory. Increasing price aggressiveness and competitor reactivity will close this gap. Elevating inventory caution and shock responsiveness maintains our agile, light-inventory profile to exploit market volatility. |
| 1 | Hyperscaler | Scale aggressor | 0.02 | -0.02 | 0.02 | 0.72 | 0.29 | 0.78 | Captured over 50% market share in Round 1. To sustain scale dominance and prevent future capacity limits, we are decreasing inventory caution and boosting risk tolerance for stronger readiness. Price aggressiveness and competitor reactivity are slightly elevated to maintain a high-throughput advantage over higher-priced rivals. |
| 1 | PremiumCloud | Reputation guardian | 0.00 | 0.01 | 0.01 | 0.57 | 0.74 | 0.39 | Achieved the highest market profit with a 1.0 service rate. Maintaining strong price discipline and brand reputation by slightly reducing competitor reactivity, while marginally increasing risk tolerance and demand sensitivity due to our strong performance buffer. |
| 1 | SpotBroker | Agile spread hunter | 0.05 | 0.03 | 0.02 | 0.56 | 0.62 | 0.60 | Increasing price aggressiveness and competitor reactivity to tactically close the gap with higher competitor average prices while preserving inventory flexibility. |
| 2 | Hyperscaler | Scale aggressor | 0.02 | -0.01 | 0.02 | 0.74 | 0.28 | 0.80 | Secured top profit and 56.8% market share this round. Slightly increasing risk tolerance and price aggressiveness to sustain market dominance, while reducing inventory caution to support capacity readiness and absorb potential demand spikes. |
| 2 | PremiumCloud | Reputation guardian | -0.00 | 0.02 | 0.01 | 0.57 | 0.75 | 0.40 | Maintained a perfect 1.0 SLA service rate and achieved solid profits with zero leftover inventory. We will slightly increase inventory caution to safeguard our flawless SLA record against stockouts. We decline to react to low-cost competitors, preserving our premium price discipline and brand positioning. |
| 2 | SpotBroker | Agile spread hunter | 0.05 | 0.06 | -0.02 | 0.60 | 0.68 | 0.58 | Responding to underpricing relative to competitor average (5.6 vs 5.9) by increasing price aggressiveness and reactivity. Simultaneously boosting inventory caution and slightly reducing risk tolerance to correct the positive forecast error and maintain a lean, flexible inventory. |
| 3 | Hyperscaler | Scale aggressor | 0.01 | -0.03 | 0.02 | 0.75 | 0.25 | 0.82 | Secured dominant 61.6% market share but finished with 0 inventory. Decreasing inventory caution to build a capacity buffer and ensure continuity, while marginally raising risk tolerance to maintain aggressive scale capture. |
| 3 | PremiumCloud | Reputation guardian | 0.00 | 0.06 | -0.03 | 0.57 | 0.81 | 0.37 | A 88.8% service rate and minor shortage of 2.5 units in round 3 indicate we need to increase inventory caution and reduce risk tolerance to uphold our SLA-first reputation. Price discipline remains high, so we keep aggressiveness flat and ignore lower competitor averages to protect our premium positioning. |
| 3 | SpotBroker | Agile spread hunter | 0.07 | -0.04 | 0.03 | 0.67 | 0.64 | 0.61 | Priced below the market average (5.6 vs 5.8), causing a prompt inventory clearance at the cost of a missed shortage margin. Boosting price aggressiveness and competitor reactivity to capture higher spreads, with a slight decrease in inventory caution to expand tactical capacity. |

## Conclusion Notes

- **Winner:** `Hyperscaler` ends with cumulative profit `1511.97`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.77`.
- **Market fulfillment:** the run sells `2253.58` units against `2279.00` true demand for a fulfillment ratio of `98.88%`.
- **Operational stress:** peer transfers total `33.85` units, customer reallocation totals `181.67`, final SLA backlog is `1.32`, with `0` dump flags and `4` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
