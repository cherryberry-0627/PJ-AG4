# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | high_volatility | 12 | llm-adaptive | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit |
| --- | --- | --- | --- | --- |
| 2279 | 2225.85 | 0.98 | 5.84 | 3461.82 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 1497.72 | 124.81 | 39.75 | 5.05 | 1335.84 | 1.00 | 0.00 | 21.99 | 0 | 0 | 12.88 | 0.91 | 0.00 |
| PremiumCloud | premium | 778.63 | 64.89 | 23.67 | 6.73 | 229.92 | 0.83 | 29.50 | 0.00 | 0 | 9 | 0.00 | 0.62 | 42.31 |
| SpotBroker | spot | 1185.47 | 98.79 | 67.67 | 5.73 | 660.08 | 0.98 | 0.00 | 7.51 | 0 | 1 | 14.08 | 0.89 | 10.85 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 179 | 184 | 165.00 | 5.40 | 455.79 | 14.00 | 0.00 | 24.95 | 5.58 |
| 1 | 200 | 197 | 196.85 | 5.27 | 113.52 | 3.15 | 3.59 | 10.78 | 2.18 |
| 2 | 195 | 193 | 192.82 | 5.73 | 244.56 | 2.18 | 2.84 | 8.99 | 1.43 |
| 3 | 211 | 215 | 209.57 | 5.80 | 388.34 | 1.43 | 3.54 | 11.65 | 0.97 |
| 4 | 202 | 204 | 195.69 | 5.87 | 281.08 | 6.31 | 0.00 | 18.38 | 5.44 |
| 5 | 184 | 186 | 178.56 | 5.87 | 221.36 | 5.44 | 3.28 | 11.15 | 3.90 |
| 6 | 155 | 164 | 151.10 | 5.93 | 112.40 | 3.90 | 1.42 | 4.93 | 2.23 |
| 7 | 193 | 198 | 190.77 | 6.00 | 413.74 | 2.23 | 4.99 | 16.53 | 2.07 |
| 8 | 186 | 169 | 183.93 | 6.00 | 294.92 | 2.07 | 4.23 | 14.09 | 1.78 |
| 9 | 191 | 186 | 189.22 | 6.07 | 331.98 | 1.78 | 4.34 | 14.84 | 1.53 |
| 10 | 197 | 197 | 191.22 | 6.07 | 330.34 | 5.78 | 0.00 | 14.64 | 4.89 |
| 11 | 186 | 180 | 181.11 | 6.07 | 273.79 | 4.89 | 1.27 | 4.36 | 2.40 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `high_volatility`, `Hyperscaler` ends first with cumulative profit `1497.72` and reputation `91.40%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `155.29` units and leaves final SLA backlog `2.40`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `29.50` units while average forecast error is `43.69`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 0 | 179 | 165.00 | shortage=14.00; default_flags=2 |
| 5 | 184 | 178.56 | shortage=5.44; transfer=3.28; default_flags=1 |
| 7 | 193 | 190.77 | shortage=2.23; transfer=4.99; default_flags=1 |
| 4 | 202 | 195.69 | shortage=6.31; default_flags=1 |
| 8 | 186 | 183.93 | shortage=2.07; transfer=4.23; default_flags=1 |
| 11 | 186 | 181.11 | shortage=4.89; transfer=1.27; default_flags=1 |
| 9 | 191 | 189.22 | shortage=1.78; transfer=4.34; default_flags=1 |
| 10 | 197 | 191.22 | shortage=5.78; default_flags=1 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm-adaptive | 184.00 | 4.00 | 4.60 | 0.20 | 100.00 | inventory target capped quantity | adaptive state risk=0.72, price=0.68, demand=0.62, inventory=0.34, shock=0.48, rivals=0.46; last update: initial strategy prior; fallback forecast=184, price=4.60, quantity=80; final forecast=188, price=4.80, quantity=70 |
| 0 | PremiumCloud | llm-adaptive | 184.00 | -1.00 | 6.60 | -0.20 | 0.00 | sla_guard reduced quantity under SLA/reputation pressure | adaptive state risk=0.38, price=0.58, demand=0.46, inventory=0.72, shock=0.36, rivals=0.32; last update: initial strategy prior; fallback forecast=184, price=6.60, quantity=10; final forecast=183, price=6.40, quantity=0 |
| 0 | SpotBroker | llm-adaptive | 184.00 | 3.00 | 5.00 | 0.00 | 30.00 | none | adaptive state risk=0.56, price=0.44, demand=0.58, inventory=0.54, shock=0.76, rivals=0.78; last update: initial strategy prior; fallback forecast=184, price=5.00, quantity=30; final forecast=187, price=5.00, quantity=30 |
| 1 | Hyperscaler | llm-adaptive | 184.00 | 5.00 | 4.60 | 0.20 | 120.00 | none | adaptive state risk=0.78, price=0.71, demand=0.64, inventory=0.31, shock=0.49, rivals=0.48; last update: Secured dominant market share and top profit in Round 0 with zero remaining inventory. Decreasing inventory caution and increasing risk tolerance to aggressively expand capacity readiness, ensuring we capture maximum demand while maintaining highly competitive pricing.; fallback forecast=184, price=4.60, quantity=120; final forecast=189, price=4.80, quantity=120 |
| 1 | PremiumCloud | llm-adaptive | 184.00 | -1.00 | 6.60 | -0.20 | 30.00 | sla_guard reduced quantity under SLA/reputation pressure | adaptive state risk=0.36, price=0.57, demand=0.48, inventory=0.78, shock=0.36, rivals=0.31; last update: Service rate of 0.86 indicates a small shortage. To preserve premium SLA reliability, we slightly lower risk tolerance and increase inventory caution to buffer against stockouts. We maintain our high-price discipline and avoid reacting to lower-priced competitors.; fallback forecast=184, price=6.60, quantity=40; final forecast=183, price=6.40, quantity=30 |
| 1 | SpotBroker | llm-adaptive | 184.00 | 4.00 | 4.20 | 0.40 | 80.00 | inventory target capped quantity | adaptive state risk=0.58, price=0.51, demand=0.62, inventory=0.52, shock=0.79, rivals=0.85; last update: Increasing price aggressiveness and competitor reactivity to exploit the price gap against the competitor average while raising demand sensitivity to capture the observed shortage.; fallback forecast=184, price=4.20, quantity=80; final forecast=188, price=4.60, quantity=80 |
| 2 | Hyperscaler | llm-adaptive | 200.00 | 26.00 | 4.60 | 0.40 | 120.00 | inventory target capped quantity | adaptive state risk=0.84, price=0.74, demand=0.68, inventory=0.27, shock=0.50, rivals=0.49; last update: Maintaining our scale-dominant focus despite a weak initial round. We decrease inventory caution to avoid going inventory-light and ensure capacity readiness, while slightly increasing risk tolerance and price aggressiveness to secure market share and recover quickly.; fallback forecast=200, price=4.60, quantity=120; final forecast=226, price=5.00, quantity=120 |
| 2 | PremiumCloud | llm-adaptive | 195.00 | 14.00 | 7.00 | -0.20 | 30.00 | sla_guard reduced quantity under SLA/reputation pressure | adaptive state risk=0.35, price=0.58, demand=0.50, inventory=0.83, shock=0.36, rivals=0.30; last update: Secured top profit but experienced a minor shortage impacting our SLA (90.6% service rate). Increasing inventory caution and demand sensitivity to protect service reliability, while reducing competitor reactivity to maintain our premium price discipline.; fallback forecast=195, price=7.00, quantity=40; final forecast=209, price=6.80, quantity=30 |
| 2 | SpotBroker | llm-adaptive | 203.00 | 38.00 | 5.40 | 0.00 | 60.00 | inventory target capped quantity | adaptive state risk=0.62, price=0.58, demand=0.66, inventory=0.55, shock=0.81, rivals=0.93; last update: Competitors are pricing significantly higher at 5.6 compared to our 4.6. Increasing price aggressiveness and competitor reactivity to aggressively close the price gap and boost profitability. Slighting increasing inventory caution to maintain a highly flexible, low-inventory profile.; fallback forecast=203, price=5.40, quantity=50; final forecast=241, price=5.40, quantity=60 |
| 3 | Hyperscaler | llm-adaptive | 195.00 | 24.00 | 4.60 | 0.40 | 120.00 | inventory target capped quantity | adaptive state risk=0.90, price=0.76, demand=0.73, inventory=0.23, shock=0.51, rivals=0.52; last update: Secured dominant 53% market share but left profit on the table. Keeping pricing aggressive to capture share while lowering inventory caution to ensure high capacity readiness. Slightly increasing demand sensitivity to calibrate forecast error.; fallback forecast=195, price=4.60, quantity=110; final forecast=219, price=5.00, quantity=110 |
| 3 | PremiumCloud | llm-adaptive | 193.00 | 11.00 | 7.00 | -0.20 | 30.00 | sla_guard reduced quantity under SLA/reputation pressure | adaptive state risk=0.33, price=0.59, demand=0.49, inventory=0.88, shock=0.35, rivals=0.29; last update: Adjusting inventory caution upward to address the minor shortage and restore SLA reliability to 100%. Maintaining premium price discipline and lowering competitor reactivity to focus on margins over market share.; fallback forecast=193, price=7.00, quantity=40; final forecast=204, price=6.80, quantity=30 |
| 3 | SpotBroker | llm-adaptive | 197.00 | 31.00 | 5.40 | 0.20 | 60.00 | inventory target capped quantity | adaptive state risk=0.64, price=0.64, demand=0.64, inventory=0.60, shock=0.82, rivals=0.97; last update: Increasing price aggressiveness and competitor reactivity to close the margin gap with the higher competitor average price, while raising inventory caution to maintain a lean posture following a demand over-forecast.; fallback forecast=197, price=5.40, quantity=50; final forecast=228, price=5.60, quantity=60 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | Scale aggressor | 0.03 | -0.03 | 0.06 | 0.71 | 0.31 | 0.78 | Secured dominant market share and top profit in Round 0 with zero remaining inventory. Decreasing inventory caution and increasing risk tolerance to aggressively expand capacity readiness, ensuring we capture maximum demand while maintaining highly competitive pricing. |
| 0 | PremiumCloud | Reputation guardian | -0.01 | 0.06 | -0.02 | 0.57 | 0.78 | 0.36 | Service rate of 0.86 indicates a small shortage. To preserve premium SLA reliability, we slightly lower risk tolerance and increase inventory caution to buffer against stockouts. We maintain our high-price discipline and avoid reacting to lower-priced competitors. |
| 0 | SpotBroker | Agile spread hunter | 0.07 | -0.02 | 0.02 | 0.51 | 0.52 | 0.58 | Increasing price aggressiveness and competitor reactivity to exploit the price gap against the competitor average while raising demand sensitivity to capture the observed shortage. |
| 1 | Hyperscaler | Scale aggressor | 0.02 | -0.04 | 0.06 | 0.74 | 0.27 | 0.84 | Maintaining our scale-dominant focus despite a weak initial round. We decrease inventory caution to avoid going inventory-light and ensure capacity readiness, while slightly increasing risk tolerance and price aggressiveness to secure market share and recover quickly. |
| 1 | PremiumCloud | Reputation guardian | 0.01 | 0.05 | -0.01 | 0.58 | 0.83 | 0.35 | Secured top profit but experienced a minor shortage impacting our SLA (90.6% service rate). Increasing inventory caution and demand sensitivity to protect service reliability, while reducing competitor reactivity to maintain our premium price discipline. |
| 1 | SpotBroker | Agile spread hunter | 0.07 | 0.03 | 0.05 | 0.58 | 0.55 | 0.62 | Competitors are pricing significantly higher at 5.6 compared to our 4.6. Increasing price aggressiveness and competitor reactivity to aggressively close the price gap and boost profitability. Slighting increasing inventory caution to maintain a highly flexible, low-inventory profile. |
| 2 | Hyperscaler | Scale aggressor | 0.02 | -0.04 | 0.06 | 0.76 | 0.23 | 0.90 | Secured dominant 53% market share but left profit on the table. Keeping pricing aggressive to capture share while lowering inventory caution to ensure high capacity readiness. Slightly increasing demand sensitivity to calibrate forecast error. |
| 2 | PremiumCloud | Reputation guardian | 0.01 | 0.05 | -0.01 | 0.59 | 0.88 | 0.33 | Adjusting inventory caution upward to address the minor shortage and restore SLA reliability to 100%. Maintaining premium price discipline and lowering competitor reactivity to focus on margins over market share. |
| 2 | SpotBroker | Agile spread hunter | 0.05 | 0.05 | 0.02 | 0.64 | 0.60 | 0.64 | Increasing price aggressiveness and competitor reactivity to close the margin gap with the higher competitor average price, while raising inventory caution to maintain a lean posture following a demand over-forecast. |
| 3 | Hyperscaler | Scale aggressor | 0.03 | -0.02 | 0.02 | 0.80 | 0.21 | 0.92 | Maintaining scale dominance and market share leadership after a highly profitable round with 100% service rate. Lowering inventory caution further to guarantee capacity readiness, while increasing price aggressiveness to leverage our cost/scale advantage against the competitor's premium pricing. |
| 3 | PremiumCloud | Reputation guardian | -0.01 | 0.04 | -0.01 | 0.57 | 0.92 | 0.32 | Adjusted parameters to prioritize SLA reliability and protect our premium brand. Increased inventory caution slightly to eliminate the minor shortage and restore a perfect service rate. Reduced competitor reactivity and price aggressiveness to maintain disciplined premium pricing and avoid overreacting to cheaper competitor averages. |
| 3 | SpotBroker | Agile spread hunter | 0.07 | 0.05 | 0.04 | 0.71 | 0.65 | 0.68 | Competitor prices (5.9) and market average (5.8) are higher than our price (5.6). Increasing price aggressiveness and competitor reactivity to close the price gap and capture higher margins. Raising inventory caution to maintain a lean, flexible posture while adjusting demand sensitivity to correct the slight forecast overestimation. |

## Conclusion Notes

- **Winner:** `Hyperscaler` ends with cumulative profit `1497.72`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.73`.
- **Market fulfillment:** the run sells `2225.85` units against `2279.00` true demand for a fulfillment ratio of `97.67%`.
- **Operational stress:** peer transfers total `29.50` units, customer reallocation totals `155.29`, final SLA backlog is `2.40`, with `0` dump flags and `10` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 100 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
