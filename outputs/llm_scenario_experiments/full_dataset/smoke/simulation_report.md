# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | baseline | 2 | llm-adaptive | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit |
| --- | --- | --- | --- | --- |
| 378 | 357.47 | 0.95 | 5.33 | 550.07 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 206.90 | 103.45 | 7.50 | 4.80 | 189.23 | 1.00 | 0.00 | 3.31 | 0 | 0 | 23.34 | 0.79 | 0.00 |
| PremiumCloud | premium | 204.40 | 102.20 | 7.50 | 6.40 | 48.78 | 0.84 | 3.31 | 0.00 | 0 | 2 | 0.00 | 0.73 | 9.06 |
| SpotBroker | spot | 138.76 | 69.38 | 7.00 | 4.80 | 119.45 | 0.90 | 0.00 | 0.00 | 0 | 1 | 2.62 | 0.64 | 11.47 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 165.00 | 5.40 | 452.92 | 16.00 | 0.00 | 24.11 | 7.09 |
| 1 | 197 | 195 | 192.47 | 5.27 | 97.15 | 4.53 | 3.31 | 9.94 | 3.07 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `baseline`, `Hyperscaler` ends first with cumulative profit `206.90` and reputation `79.00%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `34.06` units and leaves final SLA backlog `3.07`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `3.31` units while average forecast error is `7.33`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 0 | 181 | 165.00 | shortage=16.00; default_flags=2 |
| 1 | 197 | 192.47 | shortage=4.53; transfer=3.31; default_flags=1 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm-adaptive | 184.00 | 4.00 | 4.60 | 0.20 | 100.00 | inventory target capped quantity | adaptive state risk=0.72, price=0.68, demand=0.62, inventory=0.34, shock=0.48, rivals=0.46; last update: initial strategy prior; fallback forecast=184, price=4.60, quantity=80; final forecast=188, price=4.80, quantity=70 |
| 0 | PremiumCloud | llm-adaptive | 184.00 | -1.00 | 6.60 | -0.20 | 0.00 | sla_guard reduced quantity under SLA/reputation pressure | adaptive state risk=0.38, price=0.58, demand=0.46, inventory=0.72, shock=0.36, rivals=0.32; last update: initial strategy prior; fallback forecast=184, price=6.60, quantity=10; final forecast=183, price=6.40, quantity=0 |
| 0 | SpotBroker | llm-adaptive | 184.00 | 3.00 | 5.00 | 0.00 | 30.00 | none | adaptive state risk=0.56, price=0.44, demand=0.58, inventory=0.54, shock=0.76, rivals=0.78; last update: initial strategy prior; fallback forecast=184, price=5.00, quantity=30; final forecast=187, price=5.00, quantity=30 |
| 1 | Hyperscaler | llm-adaptive | 184.00 | 5.00 | 4.60 | 0.20 | 120.00 | none | adaptive state risk=0.78, price=0.73, demand=0.64, inventory=0.32, shock=0.49, rivals=0.43; last update: Maintaining scale dominance and market share by increasing risk tolerance and price competitiveness, while lowering inventory caution to ensure high capacity readiness and prevent potential shortages after zero ending inventory.; fallback forecast=184, price=4.60, quantity=120; final forecast=189, price=4.80, quantity=120 |
| 1 | PremiumCloud | llm-adaptive | 184.00 | 0.00 | 6.60 | -0.20 | 30.00 | sla_guard reduced quantity under SLA/reputation pressure | adaptive state risk=0.35, price=0.59, demand=0.49, inventory=0.79, shock=0.36, rivals=0.30; last update: Prioritizing SLA recovery after a low 81.5% service rate and minor shortage. We increase inventory caution and demand sensitivity to secure reliable capacity, whilst maintaining premium price discipline and ignoring competitor price-cutting.; fallback forecast=184, price=6.60, quantity=40; final forecast=184, price=6.40, quantity=30 |
| 1 | SpotBroker | llm-adaptive | 184.00 | 5.00 | 4.20 | 0.40 | 80.00 | inventory target capped quantity | adaptive state risk=0.60, price=0.51, demand=0.64, inventory=0.50, shock=0.80, rivals=0.87; last update: Increasing price aggressiveness and competitor reactivity to close the margin gap against competitor averages, while slightly easing inventory caution to address the previous round's capacity shortage.; fallback forecast=184, price=4.20, quantity=80; final forecast=189, price=4.60, quantity=80 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | Scale aggressor | 0.05 | -0.02 | 0.06 | 0.73 | 0.32 | 0.78 | Maintaining scale dominance and market share by increasing risk tolerance and price competitiveness, while lowering inventory caution to ensure high capacity readiness and prevent potential shortages after zero ending inventory. |
| 0 | PremiumCloud | Reputation guardian | 0.01 | 0.07 | -0.03 | 0.59 | 0.79 | 0.35 | Prioritizing SLA recovery after a low 81.5% service rate and minor shortage. We increase inventory caution and demand sensitivity to secure reliable capacity, whilst maintaining premium price discipline and ignoring competitor price-cutting. |
| 0 | SpotBroker | Agile spread hunter | 0.07 | -0.04 | 0.04 | 0.51 | 0.50 | 0.60 | Increasing price aggressiveness and competitor reactivity to close the margin gap against competitor averages, while slightly easing inventory caution to address the previous round's capacity shortage. |
| 1 | Hyperscaler | Scale aggressor | -0.05 | -0.04 | 0.04 | 0.68 | 0.28 | 0.82 | Maintaining scale dominance and market share (45%) while recovering from a negative profit round. Decided not to pivot to an inventory-light stance (lowered inventory caution) or become overly premium. Slighly reduced price aggressiveness and increased competitor reactivity to capture better margin without losing our scale advantage. |
| 1 | PremiumCloud | Reputation guardian | 0.00 | 0.05 | -0.02 | 0.59 | 0.84 | 0.33 | Although we achieved the highest profit, our service rate of 86.4% fell below premium SLA standards due to a slight capacity shortage. We decrease risk tolerance and increase inventory caution to secure stellar uptime and protect our brand reputation, while maintaining strict price discipline. |
| 1 | SpotBroker | Agile spread hunter | 0.07 | 0.02 | 0.05 | 0.58 | 0.52 | 0.64 | Increasing price aggressiveness and competitor reactivity to capture the significant margin left on the table compared to competitor averages, while maintaining highly flexible inventory controls. |

## Conclusion Notes

- **Winner:** `Hyperscaler` ends with cumulative profit `206.90`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.40`.
- **Market fulfillment:** the run sells `357.47` units against `378.00` true demand for a fulfillment ratio of `94.57%`.
- **Operational stress:** peer transfers total `3.31` units, customer reallocation totals `34.06`, final SLA backlog is `3.07`, with `0` dump flags and `3` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 100 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
