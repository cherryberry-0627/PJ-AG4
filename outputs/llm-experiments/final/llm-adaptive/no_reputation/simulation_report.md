# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | no_reputation | 12 | llm-adaptive | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit |
| --- | --- | --- | --- | --- |
| 2298 | 2264.43 | 0.99 | 5.84 | 3679.09 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 1390.36 | 115.86 | 27.08 | 5.07 | 1262.31 | 1.00 | 0.00 | 34.25 | 0 | 0 | 28.91 | 0.00 | 0.00 |
| PremiumCloud | premium | 1013.33 | 84.44 | 14.75 | 6.70 | 314.22 | 0.91 | 34.25 | 0.00 | 0 | 5 | 0.00 | 0.00 | 33.57 |
| SpotBroker | spot | 1275.41 | 106.28 | 48.83 | 5.77 | 687.90 | 1.00 | 0.00 | 0.00 | 0 | 0 | 7.01 | 0.00 | 0.00 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 181.00 | 5.33 | 483.26 | 0.00 | 7.66 | 18.11 | 0.00 |
| 1 | 197 | 195 | 197.00 | 5.47 | 240.94 | 0.00 | 5.67 | 17.00 | 0.00 |
| 2 | 198 | 197 | 198.00 | 5.67 | 203.42 | 0.00 | 6.40 | 19.54 | 0.00 |
| 3 | 202 | 204 | 202.00 | 5.73 | 318.86 | 0.00 | 6.70 | 21.02 | 0.00 |
| 4 | 193 | 194 | 187.76 | 5.80 | 230.96 | 5.24 | 0.00 | 16.43 | 4.40 |
| 5 | 182 | 183 | 177.60 | 5.87 | 237.90 | 4.40 | 1.54 | 5.02 | 2.50 |
| 6 | 171 | 175 | 168.50 | 5.93 | 226.06 | 2.50 | 0.68 | 2.33 | 1.28 |
| 7 | 194 | 196 | 192.72 | 6.07 | 457.70 | 1.28 | 4.05 | 13.21 | 0.96 |
| 8 | 196 | 187 | 195.04 | 6.07 | 367.90 | 0.96 | 0.00 | 18.50 | 0.90 |
| 9 | 200 | 198 | 190.80 | 6.07 | 335.34 | 9.20 | 0.00 | 16.49 | 6.83 |
| 10 | 198 | 198 | 191.17 | 6.07 | 245.12 | 6.83 | 0.13 | 0.45 | 3.15 |
| 11 | 186 | 183 | 182.85 | 6.07 | 331.63 | 3.15 | 1.43 | 4.92 | 1.64 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `no_reputation`, `Hyperscaler` ends first with cumulative profit `1390.36` and reputation `0.00%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `153.04` units and leaves final SLA backlog `1.64`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `34.25` units while average forecast error is `30.22`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 9 | 200 | 190.80 | shortage=9.20; default_flags=1 |
| 10 | 198 | 191.17 | shortage=6.83; transfer=0.13; default_flags=1 |
| 5 | 182 | 177.60 | shortage=4.40; transfer=1.54; default_flags=1 |
| 4 | 193 | 187.76 | shortage=5.24; default_flags=1 |
| 11 | 186 | 182.85 | shortage=3.15; transfer=1.43; default_flags=1 |
| 0 | 181 | 181.00 | transfer=7.66 |
| 3 | 202 | 202.00 | transfer=6.70 |
| 2 | 198 | 198.00 | transfer=6.40 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm-adaptive | 184.00 | 4.00 | 4.60 | 0.20 | 100.00 | inventory target capped quantity | adaptive state risk=0.72, price=0.68, demand=0.62, inventory=0.34, shock=0.48, rivals=0.46; last update: initial strategy prior; fallback forecast=184, price=4.60, quantity=80; final forecast=188, price=4.80, quantity=70 |
| 0 | PremiumCloud | llm-adaptive | 184.00 | -1.00 | 6.20 | -0.20 | 0.00 | sla_guard reduced quantity under SLA/reputation pressure; low reputation fallback lifted price | adaptive state risk=0.38, price=0.58, demand=0.46, inventory=0.72, shock=0.36, rivals=0.32; last update: initial strategy prior; fallback forecast=184, price=6.20, quantity=10; final forecast=183, price=6.20, quantity=0 |
| 0 | SpotBroker | llm-adaptive | 184.00 | 3.00 | 5.00 | 0.00 | 50.00 | inventory target capped quantity | adaptive state risk=0.56, price=0.44, demand=0.58, inventory=0.54, shock=0.76, rivals=0.78; last update: initial strategy prior; fallback forecast=184, price=5.00, quantity=50; final forecast=187, price=5.00, quantity=50 |
| 1 | Hyperscaler | llm-adaptive | 184.00 | 5.00 | 4.60 | 0.40 | 120.00 | inventory target capped quantity | adaptive state risk=0.77, price=0.74, demand=0.64, inventory=0.31, shock=0.48, rivals=0.49; last update: We achieved maximum profit and strong market share in the opening round. To remain a scale aggressor, we are reducing inventory caution (allowing for larger capacity buffers) and increasing price aggressiveness to lock in our throughput dominance. Risk tolerance is bumped up to absorb measured inventory risk.; fallback forecast=184, price=4.60, quantity=120; final forecast=189, price=5.00, quantity=110 |
| 1 | PremiumCloud | llm-adaptive | 184.00 | -1.00 | 6.20 | 0.00 | 30.00 | sla_guard reduced quantity under SLA/reputation pressure | adaptive state risk=0.39, price=0.57, demand=0.47, inventory=0.74, shock=0.36, rivals=0.30; last update: Maintaining strong premium discipline and excellent service reliability (100% service rate achieved). We are slightly reducing competitor reactivity to avoid overreacting or engaging in a price war, while maintaining high inventory caution to protect SLA guarantees.; fallback forecast=184, price=6.20, quantity=40; final forecast=183, price=6.20, quantity=30 |
| 1 | SpotBroker | llm-adaptive | 184.00 | 3.00 | 5.00 | 0.20 | 70.00 | inventory target capped quantity | adaptive state risk=0.60, price=0.51, demand=0.60, inventory=0.60, shock=0.81, rivals=0.88; last update: Priced lower than competitor average (5.0 vs 5.5), leaving money on the table despite selling out. Raising price aggressiveness and competitor reactivity to close the price gap, while ramping up inventory caution to maintain a highly agile, low-overhead profile.; fallback forecast=184, price=5.00, quantity=70; final forecast=187, price=5.20, quantity=70 |
| 2 | Hyperscaler | llm-adaptive | 198.00 | 23.00 | 4.60 | 0.40 | 120.00 | inventory target capped quantity | adaptive state risk=0.82, price=0.77, demand=0.69, inventory=0.28, shock=0.50, rivals=0.51; last update: Maintaining high market share dominance by keeping inventory caution low to secure capacity readiness, while slightly increasing risk tolerance and demand sensitivity to adjust for the higher true demand observed. Competitor reactivity is boosted slightly to exploit competitor price margins while remaining the high-volume value leader.; fallback forecast=198, price=4.60, quantity=120; final forecast=221, price=5.00, quantity=120 |
| 2 | PremiumCloud | llm-adaptive | 193.00 | 11.00 | 6.60 | -0.20 | 20.00 | sla_guard reduced quantity under SLA/reputation pressure; low reputation fallback lifted price | adaptive state risk=0.39, price=0.56, demand=0.49, inventory=0.73, shock=0.36, rivals=0.29; last update: Maintaining strong premium discipline and SLA reliability after a highly profitable round with a 1.0 service rate. We slightly reduce competitor reactivity and price aggressiveness to preserve our premium brand positioning and avoid overreacting to competitor pricing/market share games.; fallback forecast=193, price=6.60, quantity=30; final forecast=204, price=6.60, quantity=20 |
| 2 | SpotBroker | llm-adaptive | 200.00 | 33.00 | 5.40 | 0.00 | 80.00 | inventory target capped quantity | adaptive state risk=0.63, price=0.58, demand=0.65, inventory=0.63, shock=0.84, rivals=0.95; last update: SpotBroker led profit this round, but priced significantly below competitor average (5.2 vs 5.6) with zero leftover inventory. Raising price aggressiveness and competitor reactivity to dynamically close the margin gap. We keep inventory caution high to sustain our lean, highly responsive posture.; fallback forecast=200, price=5.40, quantity=70; final forecast=233, price=5.40, quantity=80 |
| 3 | Hyperscaler | llm-adaptive | 198.00 | 24.00 | 4.60 | 0.40 | 120.00 | inventory target capped quantity | adaptive state risk=0.85, price=0.82, demand=0.70, inventory=0.27, shock=0.50, rivals=0.50; last update: Maintaining strong momentum from dominant market share (52%) and best-in-market profit. Slightly increasing price aggressiveness and risk tolerance to lock in throughput leadership, while keeping inventory caution low to ensure capacity readiness.; fallback forecast=198, price=4.60, quantity=120; final forecast=222, price=5.00, quantity=120 |
| 3 | PremiumCloud | llm-adaptive | 195.00 | 12.00 | 6.60 | -0.20 | 20.00 | sla_guard reduced quantity under SLA/reputation pressure; low reputation fallback lifted price | adaptive state risk=0.39, price=0.55, demand=0.49, inventory=0.74, shock=0.35, rivals=0.28; last update: Sustaining a perfect service rate (1.0) and high premium margins. Restricting competitor reactivity and price aggressiveness to preserve premium brand positioning, while slightly increasing inventory caution to shield our reputation and guarantee uptime.; fallback forecast=195, price=6.60, quantity=30; final forecast=207, price=6.60, quantity=20 |
| 3 | SpotBroker | llm-adaptive | 200.00 | 37.00 | 5.40 | 0.20 | 60.00 | none | adaptive state risk=0.61, price=0.65, demand=0.70, inventory=0.69, shock=0.86, rivals=0.99; last update: Priced too low compared to competitor average (5.4 vs 5.8). Increasing price aggressiveness and competitor reactivity to capture missed margin. Raising inventory caution and demand sensitivity to correct the over-forecast and maintain a lean, highly flexible spot profile.; fallback forecast=200, price=5.40, quantity=60; final forecast=237, price=5.60, quantity=60 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | Scale aggressor | 0.06 | -0.03 | 0.05 | 0.74 | 0.31 | 0.77 | We achieved maximum profit and strong market share in the opening round. To remain a scale aggressor, we are reducing inventory caution (allowing for larger capacity buffers) and increasing price aggressiveness to lock in our throughput dominance. Risk tolerance is bumped up to absorb measured inventory risk. |
| 0 | PremiumCloud | Reputation guardian | -0.01 | 0.02 | 0.01 | 0.57 | 0.74 | 0.39 | Maintaining strong premium discipline and excellent service reliability (100% service rate achieved). We are slightly reducing competitor reactivity to avoid overreacting or engaging in a price war, while maintaining high inventory caution to protect SLA guarantees. |
| 0 | SpotBroker | Agile spread hunter | 0.07 | 0.06 | 0.04 | 0.51 | 0.60 | 0.60 | Priced lower than competitor average (5.0 vs 5.5), leaving money on the table despite selling out. Raising price aggressiveness and competitor reactivity to close the price gap, while ramping up inventory caution to maintain a highly agile, low-overhead profile. |
| 1 | Hyperscaler | Scale aggressor | 0.03 | -0.03 | 0.05 | 0.77 | 0.28 | 0.82 | Maintaining high market share dominance by keeping inventory caution low to secure capacity readiness, while slightly increasing risk tolerance and demand sensitivity to adjust for the higher true demand observed. Competitor reactivity is boosted slightly to exploit competitor price margins while remaining the high-volume value leader. |
| 1 | PremiumCloud | Reputation guardian | -0.01 | -0.01 | 0.01 | 0.56 | 0.73 | 0.39 | Maintaining strong premium discipline and SLA reliability after a highly profitable round with a 1.0 service rate. We slightly reduce competitor reactivity and price aggressiveness to preserve our premium brand positioning and avoid overreacting to competitor pricing/market share games. |
| 1 | SpotBroker | Agile spread hunter | 0.07 | 0.03 | 0.04 | 0.58 | 0.63 | 0.63 | SpotBroker led profit this round, but priced significantly below competitor average (5.2 vs 5.6) with zero leftover inventory. Raising price aggressiveness and competitor reactivity to dynamically close the margin gap. We keep inventory caution high to sustain our lean, highly responsive posture. |
| 2 | Hyperscaler | Scale aggressor | 0.05 | -0.01 | 0.04 | 0.82 | 0.27 | 0.85 | Maintaining strong momentum from dominant market share (52%) and best-in-market profit. Slightly increasing price aggressiveness and risk tolerance to lock in throughput leadership, while keeping inventory caution low to ensure capacity readiness. |
| 2 | PremiumCloud | Reputation guardian | -0.01 | 0.01 | -0.01 | 0.55 | 0.74 | 0.39 | Sustaining a perfect service rate (1.0) and high premium margins. Restricting competitor reactivity and price aggressiveness to preserve premium brand positioning, while slightly increasing inventory caution to shield our reputation and guarantee uptime. |
| 2 | SpotBroker | Agile spread hunter | 0.06 | 0.06 | -0.03 | 0.65 | 0.69 | 0.61 | Priced too low compared to competitor average (5.4 vs 5.8). Increasing price aggressiveness and competitor reactivity to capture missed margin. Raising inventory caution and demand sensitivity to correct the over-forecast and maintain a lean, highly flexible spot profile. |
| 3 | Hyperscaler | Scale aggressor | 0.02 | -0.01 | 0.02 | 0.84 | 0.25 | 0.88 | Maintaining scale aggression and securing market share dominance (currently at 55%). Slightly lowered inventory caution and competitor reactivity to stay focused on our high-volume, high-availability posture rather than chasing competitors' higher pricing, ensuring strong capacity readiness. |
| 3 | PremiumCloud | Reputation guardian | 0.01 | 0.01 | 0.01 | 0.57 | 0.76 | 0.39 | Maintaining premium price discipline after successfully clearing all inventory at a premium rate with a 100% service level. We decrease competitor reactivity to avoid chasing lower-margin strategies, while slightly boosting inventory caution to guarantee SLA preservation. |
| 3 | SpotBroker | Agile spread hunter | 0.05 | 0.03 | 0.02 | 0.69 | 0.72 | 0.62 | Profited as the top performing agent. Decreasing gap with competitor prices by raising aggressiveness, keeping inventory lean with slightly higher inventory caution, and maintaining high shock responsiveness to capture sudden volatility. |

## Conclusion Notes

- **Winner:** `Hyperscaler` ends with cumulative profit `1390.36`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.70`.
- **Market fulfillment:** the run sells `2264.43` units against `2298.00` true demand for a fulfillment ratio of `98.54%`.
- **Operational stress:** peer transfers total `34.25` units, customer reallocation totals `153.04`, final SLA backlog is `1.64`, with `0` dump flags and `5` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 100 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
