# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | no_reputation | 12 | llm-adaptive | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit |
| --- | --- | --- | --- | --- |
| 2298 | 2281.88 | 0.99 | 5.82 | 3731.65 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 1392.38 | 116.03 | 26.25 | 5.02 | 1254.60 | 1.00 | 0.00 | 35.81 | 0 | 0 | 16.08 | 0.00 | 0.00 |
| PremiumCloud | premium | 1112.20 | 92.68 | 15.00 | 6.70 | 338.10 | 0.95 | 44.30 | 0.00 | 0 | 2 | 0.00 | 0.00 | 16.12 |
| SpotBroker | spot | 1227.07 | 102.26 | 42.75 | 5.73 | 689.18 | 1.00 | 0.00 | 8.49 | 0 | 0 | 13.82 | 0.00 | 0.00 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 181.00 | 5.33 | 494.46 | 0.00 | 1.97 | 4.67 | 0.00 |
| 1 | 197 | 195 | 197.00 | 5.40 | 264.65 | 0.00 | 4.19 | 12.78 | 0.00 |
| 2 | 198 | 197 | 198.00 | 5.67 | 246.08 | 0.00 | 5.80 | 17.69 | 0.00 |
| 3 | 202 | 204 | 202.00 | 5.67 | 315.07 | 0.00 | 6.01 | 18.36 | 0.00 |
| 4 | 193 | 194 | 188.08 | 5.80 | 148.49 | 4.92 | 0.00 | 15.45 | 4.03 |
| 5 | 182 | 183 | 177.97 | 5.87 | 279.51 | 4.03 | 2.16 | 7.06 | 2.45 |
| 6 | 171 | 175 | 168.55 | 5.87 | 221.74 | 2.45 | 1.61 | 5.25 | 1.43 |
| 7 | 194 | 196 | 192.57 | 6.00 | 429.72 | 1.43 | 4.42 | 15.20 | 1.18 |
| 8 | 196 | 187 | 194.82 | 6.00 | 349.18 | 1.18 | 4.52 | 15.52 | 0.99 |
| 9 | 200 | 198 | 199.01 | 6.07 | 335.56 | 0.99 | 4.08 | 14.03 | 0.67 |
| 10 | 198 | 198 | 197.33 | 6.07 | 323.89 | 0.67 | 3.97 | 13.65 | 0.45 |
| 11 | 186 | 183 | 185.55 | 6.07 | 323.30 | 0.45 | 5.57 | 19.16 | 0.38 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `no_reputation`, `Hyperscaler` ends first with cumulative profit `1392.38` and reputation `0.00%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `158.83` units and leaves final SLA backlog `0.38`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `44.30` units while average forecast error is `28.00`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 5 | 182 | 177.97 | shortage=4.03; transfer=2.16; default_flags=1 |
| 4 | 193 | 188.08 | shortage=4.92; default_flags=1 |
| 11 | 186 | 185.55 | shortage=0.45; transfer=5.57 |
| 3 | 202 | 202.00 | transfer=6.01 |
| 7 | 194 | 192.57 | shortage=1.43; transfer=4.42 |
| 2 | 198 | 198.00 | transfer=5.80 |
| 8 | 196 | 194.82 | shortage=1.18; transfer=4.52 |
| 9 | 200 | 199.01 | shortage=0.99; transfer=4.08 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm-adaptive | 184.00 | 4.00 | 4.60 | 0.20 | 100.00 | inventory target capped quantity | adaptive state risk=0.72, price=0.68, demand=0.62, inventory=0.34, shock=0.48, rivals=0.46; last update: initial strategy prior; fallback forecast=184, price=4.60, quantity=80; final forecast=188, price=4.80, quantity=70 |
| 0 | PremiumCloud | llm-adaptive | 184.00 | -1.00 | 6.20 | -0.20 | 0.00 | sla_guard reduced quantity under SLA/reputation pressure; low reputation fallback lifted price | adaptive state risk=0.38, price=0.58, demand=0.46, inventory=0.72, shock=0.36, rivals=0.32; last update: initial strategy prior; fallback forecast=184, price=6.20, quantity=0; final forecast=183, price=6.20, quantity=0 |
| 0 | SpotBroker | llm-adaptive | 184.00 | 3.00 | 5.00 | 0.00 | 50.00 | inventory target capped quantity | adaptive state risk=0.56, price=0.44, demand=0.58, inventory=0.54, shock=0.76, rivals=0.78; last update: initial strategy prior; fallback forecast=184, price=5.00, quantity=50; final forecast=187, price=5.00, quantity=50 |
| 1 | Hyperscaler | llm-adaptive | 184.00 | 4.00 | 4.60 | 0.20 | 120.00 | inventory target capped quantity | adaptive state risk=0.76, price=0.71, demand=0.63, inventory=0.32, shock=0.48, rivals=0.48; last update: Maintaining scale dominance and capacity readiness by increasing risk tolerance and lowering inventory caution, securing high market share even with some inventory carrying risk. Keeping price competitiveness high to match our volume-first pursuit.; fallback forecast=184, price=4.60, quantity=110; final forecast=188, price=4.80, quantity=100 |
| 1 | PremiumCloud | llm-adaptive | 184.00 | -1.00 | 6.20 | 0.00 | 30.00 | sla_guard reduced quantity under SLA/reputation pressure | adaptive state risk=0.38, price=0.58, demand=0.47, inventory=0.73, shock=0.36, rivals=0.31; last update: PremiumCloud achieved the highest profit and a perfect 1.0 service rate in Round 0, validating our premium strategy. We slightly reduce competitor reactivity to resist downward price pressure from cheaper competitors, and slightly increase inventory caution and demand sensitivity to maintain our flawless SLA record.; fallback forecast=184, price=6.20, quantity=40; final forecast=183, price=6.20, quantity=30 |
| 1 | SpotBroker | llm-adaptive | 184.00 | 3.00 | 5.00 | 0.20 | 70.00 | inventory target capped quantity | adaptive state risk=0.60, price=0.51, demand=0.60, inventory=0.59, shock=0.77, rivals=0.83; last update: Increasing price aggressiveness and competitor reactivity to capture higher margins and close the gap with the competitor average price of 5.5, while maintaining inventory caution to preserve asset flexibility.; fallback forecast=184, price=5.00, quantity=70; final forecast=187, price=5.20, quantity=70 |
| 2 | Hyperscaler | llm-adaptive | 198.00 | 21.00 | 4.60 | 0.40 | 120.00 | inventory target capped quantity | adaptive state risk=0.79, price=0.73, demand=0.64, inventory=0.30, shock=0.48, rivals=0.48; last update: Maintaining a scale-dominant posture after a highly successful initial round where we secured the highest profit and nearly 49% market share. By slightly increasing risk tolerance and price aggressiveness while reducing inventory caution, we ensure capacity readiness to capture demand and lock in our market leadership.; fallback forecast=198, price=4.60, quantity=120; final forecast=219, price=5.00, quantity=120 |
| 2 | PremiumCloud | llm-adaptive | 193.00 | 11.00 | 6.60 | -0.20 | 20.00 | sla_guard reduced quantity under SLA/reputation pressure; low reputation fallback lifted price | adaptive state risk=0.39, price=0.59, demand=0.49, inventory=0.75, shock=0.36, rivals=0.30; last update: Maintaining premium price discipline and excellent SLA (1.0 service rate). Sold out completely with zero inventory left, so we slightly increase inventory caution and demand sensitivity to safely capture high-margin demand without risking backlog or overreacting to cheaper competitor pricing.; fallback forecast=193, price=6.60, quantity=30; final forecast=204, price=6.60, quantity=20 |
| 2 | SpotBroker | llm-adaptive | 200.00 | 32.00 | 5.40 | 0.00 | 70.00 | none | adaptive state risk=0.63, price=0.58, demand=0.65, inventory=0.61, shock=0.80, rivals=0.87; last update: Competitors charged higher prices (avg 5.5 vs our 5.2) and we under-forecasted demand. Increasing price aggressiveness and competitor reactivity to close the price gap, while raising demand sensitivity to mitigate the under-forecast and keeping inventory caution high to maintain our agile, low-inventory profile.; fallback forecast=200, price=5.40, quantity=60; final forecast=232, price=5.40, quantity=70 |
| 3 | Hyperscaler | llm-adaptive | 198.00 | 22.00 | 4.60 | 0.40 | 120.00 | inventory target capped quantity | adaptive state risk=0.81, price=0.74, demand=0.66, inventory=0.28, shock=0.48, rivals=0.50; last update: Maintaining scale-dominant posture by decreasing inventory caution to ensure capacity readiness, while adjusting competitor reactivity and demand sensitivity upward to optimize our high market share position against higher competitor pricing.; fallback forecast=198, price=4.60, quantity=120; final forecast=220, price=5.00, quantity=110 |
| 3 | PremiumCloud | llm-adaptive | 195.00 | 12.00 | 6.60 | -0.20 | 20.00 | sla_guard reduced quantity under SLA/reputation pressure; low reputation fallback lifted price | adaptive state risk=0.40, price=0.59, demand=0.50, inventory=0.78, shock=0.36, rivals=0.30; last update: Perfect SLA service rate and a clean inventory sell-out at premium pricing validates our strategy. We slightly raise inventory caution to support reliable buffers and maintain high price discipline without overreacting to competitor actions.; fallback forecast=195, price=6.60, quantity=30; final forecast=207, price=6.60, quantity=20 |
| 3 | SpotBroker | llm-adaptive | 200.00 | 34.00 | 5.40 | 0.00 | 70.00 | inventory_guard lifted price under volatility | adaptive state risk=0.65, price=0.62, demand=0.67, inventory=0.64, shock=0.81, rivals=0.89; last update: Leveraging best-in-market profit by raising competitor reactivity and price aggressiveness to capture more margin against competitors' higher average price ($5.80 vs $5.40). Slightly increased inventory caution to ensure we preserve agile, low-overhead inventory levels.; fallback forecast=200, price=5.40, quantity=60; final forecast=234, price=5.40, quantity=70 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | Scale aggressor | 0.03 | -0.02 | 0.04 | 0.71 | 0.32 | 0.76 | Maintaining scale dominance and capacity readiness by increasing risk tolerance and lowering inventory caution, securing high market share even with some inventory carrying risk. Keeping price competitiveness high to match our volume-first pursuit. |
| 0 | PremiumCloud | Reputation guardian | 0.00 | 0.01 | 0.00 | 0.58 | 0.73 | 0.38 | PremiumCloud achieved the highest profit and a perfect 1.0 service rate in Round 0, validating our premium strategy. We slightly reduce competitor reactivity to resist downward price pressure from cheaper competitors, and slightly increase inventory caution and demand sensitivity to maintain our flawless SLA record. |
| 0 | SpotBroker | Agile spread hunter | 0.07 | 0.05 | 0.04 | 0.51 | 0.59 | 0.60 | Increasing price aggressiveness and competitor reactivity to capture higher margins and close the gap with the competitor average price of 5.5, while maintaining inventory caution to preserve asset flexibility. |
| 1 | Hyperscaler | Scale aggressor | 0.02 | -0.01 | 0.02 | 0.73 | 0.30 | 0.79 | Maintaining a scale-dominant posture after a highly successful initial round where we secured the highest profit and nearly 49% market share. By slightly increasing risk tolerance and price aggressiveness while reducing inventory caution, we ensure capacity readiness to capture demand and lock in our market leadership. |
| 1 | PremiumCloud | Reputation guardian | 0.01 | 0.02 | 0.01 | 0.59 | 0.75 | 0.39 | Maintaining premium price discipline and excellent SLA (1.0 service rate). Sold out completely with zero inventory left, so we slightly increase inventory caution and demand sensitivity to safely capture high-margin demand without risking backlog or overreacting to cheaper competitor pricing. |
| 1 | SpotBroker | Agile spread hunter | 0.07 | 0.02 | 0.04 | 0.58 | 0.61 | 0.63 | Competitors charged higher prices (avg 5.5 vs our 5.2) and we under-forecasted demand. Increasing price aggressiveness and competitor reactivity to close the price gap, while raising demand sensitivity to mitigate the under-forecast and keeping inventory caution high to maintain our agile, low-inventory profile. |
| 2 | Hyperscaler | Scale aggressor | 0.01 | -0.02 | 0.02 | 0.74 | 0.28 | 0.81 | Maintaining scale-dominant posture by decreasing inventory caution to ensure capacity readiness, while adjusting competitor reactivity and demand sensitivity upward to optimize our high market share position against higher competitor pricing. |
| 2 | PremiumCloud | Reputation guardian | 0.01 | 0.03 | 0.01 | 0.59 | 0.78 | 0.40 | Perfect SLA service rate and a clean inventory sell-out at premium pricing validates our strategy. We slightly raise inventory caution to support reliable buffers and maintain high price discipline without overreacting to competitor actions. |
| 2 | SpotBroker | Agile spread hunter | 0.04 | 0.03 | 0.02 | 0.62 | 0.64 | 0.65 | Leveraging best-in-market profit by raising competitor reactivity and price aggressiveness to capture more margin against competitors' higher average price ($5.80 vs $5.40). Slightly increased inventory caution to ensure we preserve agile, low-overhead inventory levels. |
| 3 | Hyperscaler | Scale aggressor | 0.01 | -0.02 | 0.01 | 0.75 | 0.26 | 0.82 | We secured the highest profit and over 50% market share with a perfect service rate. To maintain this scale dominance and capacity readiness, we are decreasing inventory caution to tolerate holding buffer stock. We also bump competitor reactivity to gently adjust to the significant price gap with competitors while keeping our aggressive market-share-first posture. |
| 3 | PremiumCloud | Reputation guardian | 0.00 | 0.02 | -0.01 | 0.59 | 0.80 | 0.39 | Maintained our premium pricing successfully with 100% service rate and zero inventory waste. We are reducing competitor reactivity to avoid margin-eroding price wars, and slightly boosting inventory caution to safeguard our high SLA standards in future rounds. |
| 3 | SpotBroker | Agile spread hunter | 0.05 | 0.04 | 0.02 | 0.67 | 0.68 | 0.67 | Competitor prices averaged 5.8 compared to our 5.4, leaving margin space. Increasing price aggressiveness and competitor reactivity to hunt this spread. Raising inventory caution to maintain a highly agile, light footprint after our slight demand overforecast last round. |

## Conclusion Notes

- **Winner:** `Hyperscaler` ends with cumulative profit `1392.38`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.70`.
- **Market fulfillment:** the run sells `2281.88` units against `2298.00` true demand for a fulfillment ratio of `99.30%`.
- **Operational stress:** peer transfers total `44.30` units, customer reallocation totals `158.83`, final SLA backlog is `0.38`, with `0` dump flags and `2` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
