# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | high_volatility | 12 | llm-adaptive | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit |
| --- | --- | --- | --- | --- |
| 2279 | 2262.28 | 0.99 | 5.84 | 3618.77 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 1329.97 | 110.83 | 37.08 | 4.98 | 1307.65 | 1.00 | 0.00 | 36.42 | 0 | 0 | 27.53 | 0.90 | 0.00 |
| PremiumCloud | premium | 1175.47 | 97.96 | 22.92 | 6.77 | 347.88 | 0.95 | 43.29 | 0.00 | 0 | 2 | 0.00 | 0.85 | 16.72 |
| SpotBroker | spot | 1113.33 | 92.78 | 59.58 | 5.77 | 606.75 | 1.00 | 0.00 | 6.87 | 0 | 0 | 19.50 | 0.93 | 0.00 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 179 | 184 | 179.00 | 5.47 | 572.70 | 0.00 | 0.00 | 23.65 | 0.00 |
| 1 | 200 | 197 | 200.00 | 5.53 | 246.21 | 0.00 | 8.03 | 13.32 | 0.00 |
| 2 | 195 | 193 | 195.00 | 5.80 | 287.53 | 0.00 | 6.80 | 21.92 | 0.00 |
| 3 | 211 | 215 | 211.00 | 5.80 | 374.29 | 0.00 | 8.05 | 22.51 | 0.00 |
| 4 | 202 | 204 | 202.00 | 5.87 | 265.58 | 0.00 | 4.13 | 14.00 | 0.00 |
| 5 | 184 | 186 | 181.07 | 5.87 | 225.65 | 2.93 | 0.00 | 9.78 | 1.92 |
| 6 | 155 | 164 | 153.08 | 5.87 | 87.88 | 1.92 | 1.34 | 4.45 | 1.10 |
| 7 | 193 | 198 | 191.90 | 5.93 | 411.09 | 1.10 | 5.38 | 19.03 | 0.96 |
| 8 | 186 | 169 | 185.04 | 5.93 | 286.75 | 0.96 | 4.83 | 17.19 | 0.81 |
| 9 | 191 | 186 | 186.81 | 5.93 | 326.64 | 4.19 | 1.56 | 17.65 | 3.55 |
| 10 | 197 | 197 | 193.45 | 6.00 | 283.83 | 3.55 | 2.00 | 7.34 | 2.08 |
| 11 | 186 | 180 | 183.92 | 6.07 | 250.63 | 2.08 | 1.18 | 4.11 | 1.06 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `high_volatility`, `Hyperscaler` ends first with cumulative profit `1329.97` and reputation `90.02%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `174.96` units and leaves final SLA backlog `1.06`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `43.29` units while average forecast error is `39.86`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 9 | 191 | 186.81 | shortage=4.19; transfer=1.56; default_flags=1 |
| 10 | 197 | 193.45 | shortage=3.55; transfer=2.00; default_flags=1 |
| 3 | 211 | 211.00 | transfer=8.05 |
| 1 | 200 | 200.00 | transfer=8.03 |
| 2 | 195 | 195.00 | transfer=6.80 |
| 7 | 193 | 191.90 | shortage=1.10; transfer=5.38 |
| 8 | 186 | 185.04 | shortage=0.96; transfer=4.83 |
| 4 | 202 | 202.00 | transfer=4.13 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm-adaptive | 184.00 | 4.00 | 4.60 | 0.20 | 90.00 | inventory target capped quantity | adaptive state risk=0.72, price=0.68, demand=0.62, inventory=0.34, shock=0.48, rivals=0.46; last update: initial strategy prior; fallback forecast=184, price=4.60, quantity=70; final forecast=188, price=4.80, quantity=70 |
| 0 | PremiumCloud | llm-adaptive | 184.00 | -1.00 | 6.80 | -0.20 | 0.00 | none | adaptive state risk=0.38, price=0.58, demand=0.46, inventory=0.72, shock=0.36, rivals=0.32; last update: initial strategy prior; fallback forecast=184, price=6.80, quantity=0; final forecast=183, price=6.60, quantity=0 |
| 0 | SpotBroker | llm-adaptive | 184.00 | 3.00 | 5.00 | 0.00 | 30.00 | none | adaptive state risk=0.56, price=0.44, demand=0.58, inventory=0.54, shock=0.76, rivals=0.78; last update: initial strategy prior; fallback forecast=184, price=5.00, quantity=30; final forecast=187, price=5.00, quantity=30 |
| 1 | Hyperscaler | llm-adaptive | 184.00 | 4.00 | 4.60 | 0.20 | 120.00 | inventory target capped quantity | adaptive state risk=0.75, price=0.70, demand=0.63, inventory=0.32, shock=0.48, rivals=0.48; last update: Maintained dominant market share (55%) and achieved a high service rate. Slightly reduced inventory caution to bolster capacity readiness and prevent future shortages under high demand, while marginally increasing risk tolerance and competitor reactivity to defend our volume leadership against premium competitors.; fallback forecast=184, price=4.60, quantity=120; final forecast=188, price=4.80, quantity=120 |
| 1 | PremiumCloud | llm-adaptive | 184.00 | -1.00 | 6.80 | -0.20 | 30.00 | none | adaptive state risk=0.39, price=0.56, demand=0.47, inventory=0.74, shock=0.36, rivals=0.30; last update: PremiumCloud achieved the highest profit in Round 0 with perfect SLA performance. To preserve our premium brand discipline and excellent service rates under high margins, we slightly decrease competitor reactivity and price aggressiveness, while maintaining robust inventory caution.; fallback forecast=184, price=6.80, quantity=40; final forecast=183, price=6.60, quantity=30 |
| 1 | SpotBroker | llm-adaptive | 184.00 | 3.00 | 5.00 | 0.20 | 70.00 | inventory target capped quantity | adaptive state risk=0.60, price=0.51, demand=0.60, inventory=0.57, shock=0.77, rivals=0.84; last update: Priced below the competitor average of 5.70 at 5.00, leading to zero ending inventory but leaving money on the table. Increasing price aggressiveness and competitor reactivity to close the price gap, while slightly raising inventory caution to remain agile.; fallback forecast=184, price=5.00, quantity=60; final forecast=187, price=5.20, quantity=60 |
| 2 | Hyperscaler | llm-adaptive | 200.00 | 25.00 | 4.60 | 0.40 | 120.00 | none | adaptive state risk=0.78, price=0.71, demand=0.66, inventory=0.30, shock=0.49, rivals=0.51; last update: We successfully captured over 50% market share but under-forecasted demand and left money on the table compared to PremiumCloud. To maintain scale dominance and capacity readiness, we are decreasing inventory caution to build a better safety buffer, increasing demand sensitivity to correct our under-forecasting, and boosting competitor reactivity to carefully close the margin gap while retaining our dominant volume position.; fallback forecast=200, price=4.60, quantity=120; final forecast=225, price=5.00, quantity=120 |
| 2 | PremiumCloud | llm-adaptive | 195.00 | 13.00 | 7.00 | -0.20 | 20.00 | none | adaptive state risk=0.39, price=0.57, demand=0.48, inventory=0.75, shock=0.36, rivals=0.30; last update: Secured the highest profit in the market with a perfect 100% service rate. We will maintain our high price discipline and inventory caution to protect premium margins and SLA, while reducing competitor reactivity to avoid being dragged into downmarket price adjustments.; fallback forecast=195, price=7.00, quantity=30; final forecast=208, price=6.80, quantity=20 |
| 2 | SpotBroker | llm-adaptive | 203.00 | 36.00 | 5.60 | 0.00 | 70.00 | inventory target capped quantity | adaptive state risk=0.62, price=0.57, demand=0.62, inventory=0.61, shock=0.79, rivals=0.87; last update: Competitors priced significantly higher than us, meaning we left margin on the table despite clearing all inventory. Increasing price aggressiveness and competitor reactivity to tactically capture higher spreads, while raising inventory caution to remain nimble.; fallback forecast=203, price=5.60, quantity=60; final forecast=239, price=5.60, quantity=60 |
| 3 | Hyperscaler | llm-adaptive | 195.00 | 21.00 | 4.60 | 0.40 | 120.00 | none | adaptive state risk=0.80, price=0.74, demand=0.67, inventory=0.29, shock=0.48, rivals=0.52; last update: Dominant performance in round 2 with top profit and 56.8% market share. We will continue our scale-aggressive posture by slightly increasing risk tolerance and price aggressiveness, while lowering inventory caution to ensure we maintain massive capacity readiness and avoid stockouts.; fallback forecast=195, price=4.60, quantity=120; final forecast=216, price=5.00, quantity=120 |
| 3 | PremiumCloud | llm-adaptive | 193.00 | 11.00 | 7.00 | -0.20 | 20.00 | none | adaptive state risk=0.39, price=0.57, demand=0.49, inventory=0.77, shock=0.36, rivals=0.29; last update: Maintained a perfect 100% service rate and solid premium positioning while selling out all inventory. Slightly increased inventory caution to preserve SLA reliability against future demand fluctuations, and reduced competitor reactivity to avoid getting dragged into price wars, staying true to our reputation-first brand discipline.; fallback forecast=193, price=7.00, quantity=30; final forecast=204, price=6.80, quantity=20 |
| 3 | SpotBroker | llm-adaptive | 197.00 | 30.00 | 5.60 | 0.00 | 60.00 | none | adaptive state risk=0.63, price=0.61, demand=0.65, inventory=0.65, shock=0.78, rivals=0.90; last update: Increasing competitor reactivity and price aggressiveness to close the margin gap with competitors (avg $5.90 vs our $5.60). Raising inventory caution and demand sensitivity to optimize our forecast accuracy while maintaining a highly flexible, low-inventory profile.; fallback forecast=197, price=5.60, quantity=50; final forecast=227, price=5.60, quantity=60 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | Scale aggressor | 0.02 | -0.02 | 0.03 | 0.70 | 0.32 | 0.75 | Maintained dominant market share (55%) and achieved a high service rate. Slightly reduced inventory caution to bolster capacity readiness and prevent future shortages under high demand, while marginally increasing risk tolerance and competitor reactivity to defend our volume leadership against premium competitors. |
| 0 | PremiumCloud | Reputation guardian | -0.01 | 0.02 | 0.01 | 0.56 | 0.74 | 0.39 | PremiumCloud achieved the highest profit in Round 0 with perfect SLA performance. To preserve our premium brand discipline and excellent service rates under high margins, we slightly decrease competitor reactivity and price aggressiveness, while maintaining robust inventory caution. |
| 0 | SpotBroker | Agile spread hunter | 0.07 | 0.03 | 0.04 | 0.51 | 0.57 | 0.60 | Priced below the competitor average of 5.70 at 5.00, leading to zero ending inventory but leaving money on the table. Increasing price aggressiveness and competitor reactivity to close the price gap, while slightly raising inventory caution to remain agile. |
| 1 | Hyperscaler | Scale aggressor | 0.01 | -0.01 | 0.02 | 0.71 | 0.30 | 0.78 | We successfully captured over 50% market share but under-forecasted demand and left money on the table compared to PremiumCloud. To maintain scale dominance and capacity readiness, we are decreasing inventory caution to build a better safety buffer, increasing demand sensitivity to correct our under-forecasting, and boosting competitor reactivity to carefully close the margin gap while retaining our dominant volume position. |
| 1 | PremiumCloud | Reputation guardian | 0.01 | 0.01 | 0.00 | 0.57 | 0.75 | 0.39 | Secured the highest profit in the market with a perfect 100% service rate. We will maintain our high price discipline and inventory caution to protect premium margins and SLA, while reducing competitor reactivity to avoid being dragged into downmarket price adjustments. |
| 1 | SpotBroker | Agile spread hunter | 0.05 | 0.04 | 0.03 | 0.57 | 0.61 | 0.62 | Competitors priced significantly higher than us, meaning we left margin on the table despite clearing all inventory. Increasing price aggressiveness and competitor reactivity to tactically capture higher spreads, while raising inventory caution to remain nimble. |
| 2 | Hyperscaler | Scale aggressor | 0.02 | -0.01 | 0.02 | 0.74 | 0.29 | 0.80 | Dominant performance in round 2 with top profit and 56.8% market share. We will continue our scale-aggressive posture by slightly increasing risk tolerance and price aggressiveness, while lowering inventory caution to ensure we maintain massive capacity readiness and avoid stockouts. |
| 2 | PremiumCloud | Reputation guardian | -0.00 | 0.01 | 0.00 | 0.57 | 0.77 | 0.39 | Maintained a perfect 100% service rate and solid premium positioning while selling out all inventory. Slightly increased inventory caution to preserve SLA reliability against future demand fluctuations, and reduced competitor reactivity to avoid getting dragged into price wars, staying true to our reputation-first brand discipline. |
| 2 | SpotBroker | Agile spread hunter | 0.05 | 0.04 | 0.01 | 0.61 | 0.65 | 0.63 | Increasing competitor reactivity and price aggressiveness to close the margin gap with competitors (avg $5.90 vs our $5.60). Raising inventory caution and demand sensitivity to optimize our forecast accuracy while maintaining a highly flexible, low-inventory profile. |
| 3 | Hyperscaler | Scale aggressor | 0.01 | -0.01 | 0.01 | 0.75 | 0.27 | 0.82 | Maintaining strong market dominance and excellent service rate from the previous round. Slightly increasing risk tolerance and lowering inventory caution to ensure high capacity readiness and continue capturing market share while keeping price competitiveness high. |
| 3 | PremiumCloud | Reputation guardian | 0.01 | -0.02 | 0.01 | 0.58 | 0.75 | 0.40 | Maintained a perfect 1.0 service rate and successfully sold out all inventory. Slightly decreasing competitor reactivity to remain shielded from lower-tier pricing battles, while marginally nudging price aggressiveness and risk tolerance up to capture disciplined premium yields. |
| 3 | SpotBroker | Agile spread hunter | 0.05 | 0.03 | 0.02 | 0.67 | 0.68 | 0.65 | Cleared all inventory successfully but priced slightly below the competitor average ($5.6 vs $5.9). Nudging price aggressiveness and competitor reactivity upward to close this gap and extract more margin, while increasing inventory caution to maintain a light, agile posture. |

## Conclusion Notes

- **Winner:** `Hyperscaler` ends with cumulative profit `1329.97`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.77`.
- **Market fulfillment:** the run sells `2262.28` units against `2279.00` true demand for a fulfillment ratio of `99.27%`.
- **Operational stress:** peer transfers total `43.29` units, customer reallocation totals `174.96`, final SLA backlog is `1.06`, with `0` dump flags and `2` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
