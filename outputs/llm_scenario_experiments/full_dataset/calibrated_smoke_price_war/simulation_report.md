# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | price_war | 2 | llm-adaptive | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit |
| --- | --- | --- | --- | --- |
| 378 | 374.25 | 0.99 | 5.53 | 794.63 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 318.53 | 159.26 | 7.50 | 4.90 | 204.40 | 1.00 | 0.00 | 0.00 | 0 | 0 | 4.76 | 0.74 | 0.00 |
| PremiumCloud | premium | 322.60 | 161.30 | 8.00 | 6.60 | 55.95 | 1.00 | 0.00 | 9.05 | 0 | 0 | 0.00 | 0.92 | 0.00 |
| SpotBroker | spot | 153.50 | 76.75 | 7.50 | 5.10 | 113.90 | 0.97 | 9.05 | 0.00 | 0 | 0 | 0.00 | 0.70 | 3.75 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 180.00 | 5.47 | 544.77 | 1.00 | 8.52 | 19.53 | 0.15 |
| 1 | 197 | 195 | 194.25 | 5.60 | 249.85 | 2.75 | 0.53 | 17.17 | 0.39 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `price_war`, `PremiumCloud` ends first with cumulative profit `322.60` and reputation `91.56%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `36.70` units and leaves final SLA backlog `0.39`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `9.05` units while average forecast error is `7.67`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 0 | 181 | 180.00 | shortage=1.00; transfer=8.52 |
| 1 | 197 | 194.25 | shortage=2.75; transfer=0.53 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm-adaptive | 184.00 | 4.00 | 4.60 | 0.20 | 90.00 | inventory target capped quantity | adaptive state risk=0.72, price=0.68, demand=0.62, inventory=0.34, shock=0.48, rivals=0.46; last update: initial strategy prior; fallback forecast=184, price=4.60, quantity=70; final forecast=188, price=4.80, quantity=70 |
| 0 | PremiumCloud | llm-adaptive | 184.00 | -1.00 | 6.80 | -0.20 | 0.00 | none | adaptive state risk=0.38, price=0.58, demand=0.46, inventory=0.72, shock=0.36, rivals=0.32; last update: initial strategy prior; fallback forecast=184, price=6.80, quantity=0; final forecast=183, price=6.60, quantity=0 |
| 0 | SpotBroker | llm-adaptive | 184.00 | 3.00 | 5.00 | 0.00 | 30.00 | none | adaptive state risk=0.56, price=0.44, demand=0.58, inventory=0.54, shock=0.76, rivals=0.78; last update: initial strategy prior; fallback forecast=184, price=5.00, quantity=30; final forecast=187, price=5.00, quantity=30 |
| 1 | Hyperscaler | llm-adaptive | 184.00 | 5.00 | 4.60 | 0.40 | 120.00 | inventory target capped quantity | adaptive state risk=0.76, price=0.71, demand=0.64, inventory=0.31, shock=0.48, rivals=0.49; last update: We achieved a dominant 55% market share but cleared all inventory with zero ending stock. To guarantee capacity readiness and scale dominance in the next round, we decrease inventory caution and increase risk tolerance. We also slightly increase competitor reactivity to capture margin opportunities given the premium price gap left by rivals.; fallback forecast=184, price=4.60, quantity=120; final forecast=189, price=5.00, quantity=110 |
| 1 | PremiumCloud | llm-adaptive | 184.00 | -1.00 | 6.80 | -0.20 | 30.00 | none | adaptive state risk=0.39, price=0.59, demand=0.46, inventory=0.72, shock=0.36, rivals=0.31; last update: First round achieved best market profit and perfect SLA. Maintaining strict premium pricing discipline and slightly reducing competitor reactivity to focus on our high-margin, service-first position.; fallback forecast=184, price=6.80, quantity=40; final forecast=183, price=6.60, quantity=30 |
| 1 | SpotBroker | llm-adaptive | 184.00 | 4.00 | 5.00 | 0.20 | 70.00 | inventory target capped quantity | adaptive state risk=0.60, price=0.51, demand=0.63, inventory=0.56, shock=0.79, rivals=0.83; last update: Closing the large competitor price gap (5.0 vs 5.7) by increasing price aggressiveness and competitor reactivity, while slightly boosting demand sensitivity to address the minor shortage while maintaining high inventory caution for flexibility.; fallback forecast=184, price=5.00, quantity=60; final forecast=188, price=5.20, quantity=60 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | Scale aggressor | 0.03 | -0.03 | 0.04 | 0.71 | 0.31 | 0.76 | We achieved a dominant 55% market share but cleared all inventory with zero ending stock. To guarantee capacity readiness and scale dominance in the next round, we decrease inventory caution and increase risk tolerance. We also slightly increase competitor reactivity to capture margin opportunities given the premium price gap left by rivals. |
| 0 | PremiumCloud | Reputation guardian | 0.01 | 0.00 | 0.01 | 0.59 | 0.72 | 0.39 | First round achieved best market profit and perfect SLA. Maintaining strict premium pricing discipline and slightly reducing competitor reactivity to focus on our high-margin, service-first position. |
| 0 | SpotBroker | Agile spread hunter | 0.07 | 0.02 | 0.04 | 0.51 | 0.56 | 0.60 | Closing the large competitor price gap (5.0 vs 5.7) by increasing price aggressiveness and competitor reactivity, while slightly boosting demand sensitivity to address the minor shortage while maintaining high inventory caution for flexibility. |
| 1 | Hyperscaler | Scale aggressor | 0.02 | -0.02 | 0.03 | 0.74 | 0.29 | 0.79 | Dominant performance in Round 1 with 53% market share and top profitability. To sustain capacity readiness and avoid near-miss stockouts (ending inventory was low), we are slightly increasing risk tolerance, decreasing inventory caution to hold safer buffers, and marginally boosting demand sensitivity and price aggressiveness to lock in our scale advantage. |
| 1 | PremiumCloud | Reputation guardian | -0.01 | 0.02 | -0.01 | 0.58 | 0.74 | 0.38 | Maintained exceptionally strong premium margins and a perfect 1.0 service rate in Round 1. We pocketed solid profits without over-relying on low competitor prices. Marginally lowered competitor reactivity and price aggressiveness to preserve premium price discipline, while slightly raising demand sensitivity to minimize our minor forecast underestimation. |
| 1 | SpotBroker | Agile spread hunter | 0.05 | -0.02 | 0.03 | 0.57 | 0.54 | 0.62 | Reacting to the competitor price gap (5.8 vs our 5.2) by raising price aggressiveness and competitor reactivity. We slightly increase demand sensitivity and risk tolerance to capture missed demand (shortage of 2.7) while keeping inventory flexible. |

## Conclusion Notes

- **Winner:** `PremiumCloud` ends with cumulative profit `322.60`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.60`.
- **Market fulfillment:** the run sells `374.25` units against `378.00` true demand for a fulfillment ratio of `99.01%`.
- **Operational stress:** peer transfers total `9.05` units, customer reallocation totals `36.70`, final SLA backlog is `0.39`, with `0` dump flags and `0` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
