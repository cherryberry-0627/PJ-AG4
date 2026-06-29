# PJ-AG4 Simulation Report

## Run Parameters

| Seed | Scenario | Rounds | Agent Mode | Agents | Demand Window |
| --- | --- | --- | --- | --- | --- |
| 7 | baseline | 12 | llm-adaptive | 3 | 5 |

## Market Summary

| Total Demand | Total Sales | Fulfillment | Average Market Price | Total Profit |
| --- | --- | --- | --- | --- |
| 2298 | 2280.61 | 0.99 | 5.85 | 3741.30 |

## Agent Strategy Comparison

| Agent | Role | Final Cum Profit | Avg Profit | Avg Forecast Error | Avg Price | Total Sales | Avg Service Rate | Transfer In | Transfer Out | Dump Flags | Default Flags | Final Inventory | Final Reputation | Total Shortage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | hyperscaler | 1445.92 | 120.49 | 24.75 | 5.00 | 1346.12 | 1.00 | 0.00 | 24.56 | 0 | 0 | 22.21 | 0.93 | 0.00 |
| PremiumCloud | premium | 1098.92 | 91.58 | 14.58 | 6.77 | 323.38 | 0.95 | 37.92 | 0.00 | 0 | 2 | 0.00 | 0.90 | 15.21 |
| SpotBroker | spot | 1196.45 | 99.70 | 44.33 | 5.78 | 611.10 | 1.00 | 0.00 | 13.37 | 0 | 0 | 10.05 | 0.93 | 2.18 |

## Round-Level Timeline

| Round | True Demand | Observed Demand | Sales | Avg Price | Profit | Shortage | Transfers | Reallocated | Backlog |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 181 | 184 | 180.00 | 5.47 | 576.32 | 1.00 | 0.00 | 23.81 | 0.27 |
| 1 | 197 | 195 | 196.73 | 5.53 | 228.69 | 0.27 | 6.63 | 14.03 | 0.06 |
| 2 | 198 | 197 | 198.00 | 5.80 | 303.81 | 0.00 | 6.99 | 22.56 | 0.00 |
| 3 | 202 | 204 | 201.09 | 5.80 | 343.21 | 0.91 | 0.00 | 31.91 | 0.25 |
| 4 | 193 | 194 | 193.00 | 5.87 | 243.13 | 0.00 | 6.01 | 20.30 | 0.00 |
| 5 | 182 | 183 | 182.00 | 5.87 | 264.74 | 0.00 | 5.20 | 17.32 | 0.00 |
| 6 | 171 | 175 | 166.56 | 5.93 | 171.13 | 4.44 | 0.00 | 15.70 | 3.65 |
| 7 | 194 | 196 | 190.35 | 5.93 | 342.60 | 3.65 | 2.16 | 7.57 | 2.19 |
| 8 | 196 | 187 | 193.81 | 5.93 | 273.03 | 2.19 | 1.18 | 4.17 | 1.17 |
| 9 | 200 | 198 | 198.83 | 6.00 | 365.75 | 1.17 | 3.83 | 14.58 | 0.90 |
| 10 | 198 | 198 | 195.87 | 6.00 | 373.33 | 2.13 | 3.52 | 15.78 | 1.63 |
| 11 | 186 | 183 | 184.37 | 6.07 | 255.56 | 1.63 | 2.40 | 8.17 | 0.96 |

## Findings

- **Finding 1: Reputation-weighted SLA posture can beat pure price cutting.** In scenario `baseline`, `Hyperscaler` ends first with cumulative profit `1445.92` and reputation `93.08%`.
- **Finding 2: Capacity pressure is now visible as customer migration and backlog.** Two-stage allocation reallocates `195.91` units and leaves final SLA backlog `0.96`.
- **Finding 3: Peer transfer is a stress valve, not the whole market.** Transfer volume totals `37.92` units while average forecast error is `27.89`, linking prediction quality to shortage/default risk.

## Key Events

| Round | True Demand | Sales | Signals |
| --- | --- | --- | --- |
| 7 | 194 | 190.35 | shortage=3.65; transfer=2.16; default_flags=1 |
| 6 | 171 | 166.56 | shortage=4.44; default_flags=1 |
| 2 | 198 | 198.00 | transfer=6.99 |
| 1 | 197 | 196.73 | shortage=0.27; transfer=6.63 |
| 4 | 193 | 193.00 | transfer=6.01 |
| 10 | 198 | 195.87 | shortage=2.13; transfer=3.52 |
| 5 | 182 | 182.00 | transfer=5.20 |
| 9 | 200 | 198.83 | shortage=1.17; transfer=3.83 |

## Decision Trace Samples

| Round | Agent | Source | Forecast Base | Forecast Adj | Price Base | Price Adj | Qty Target | Risk Gate | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | llm-adaptive | 184.00 | 4.00 | 4.60 | 0.20 | 90.00 | inventory target capped quantity | adaptive state risk=0.72, price=0.68, demand=0.62, inventory=0.34, shock=0.48, rivals=0.46; last update: initial strategy prior; fallback forecast=184, price=4.60, quantity=70; final forecast=188, price=4.80, quantity=70 |
| 0 | PremiumCloud | llm-adaptive | 184.00 | -1.00 | 6.80 | -0.20 | 0.00 | none | adaptive state risk=0.38, price=0.58, demand=0.46, inventory=0.72, shock=0.36, rivals=0.32; last update: initial strategy prior; fallback forecast=184, price=6.80, quantity=0; final forecast=183, price=6.60, quantity=0 |
| 0 | SpotBroker | llm-adaptive | 184.00 | 3.00 | 5.00 | 0.00 | 30.00 | none | adaptive state risk=0.56, price=0.44, demand=0.58, inventory=0.54, shock=0.76, rivals=0.78; last update: initial strategy prior; fallback forecast=184, price=5.00, quantity=30; final forecast=187, price=5.00, quantity=30 |
| 1 | Hyperscaler | llm-adaptive | 184.00 | 4.00 | 4.60 | 0.20 | 120.00 | none | adaptive state risk=0.75, price=0.70, demand=0.63, inventory=0.32, shock=0.48, rivals=0.48; last update: Secured dominant market share and top profit in Round 0 with zero remaining inventory. To maintain capacity readiness and capture potential demand spikes, we marginally increase risk tolerance and reduce inventory caution, ensuring we do not run into capacity bottlenecks while preserving our competitive pricing edge.; fallback forecast=184, price=4.60, quantity=120; final forecast=188, price=4.80, quantity=120 |
| 1 | PremiumCloud | llm-adaptive | 184.00 | -2.00 | 6.80 | -0.20 | 30.00 | none | adaptive state risk=0.37, price=0.59, demand=0.45, inventory=0.74, shock=0.36, rivals=0.31; last update: Round 0 profit was highly optimal with a perfect 1.0 service rate at our premium price point. I am marginally increasing inventory caution to secure our high-uptime commitment, slightly raising price aggressiveness to sustain our premium positioning, and reducing competitor reactivity to ignore lower-priced rivals.; fallback forecast=184, price=6.80, quantity=40; final forecast=182, price=6.60, quantity=30 |
| 1 | SpotBroker | llm-adaptive | 184.00 | 4.00 | 5.00 | 0.20 | 70.00 | inventory target capped quantity | adaptive state risk=0.60, price=0.51, demand=0.63, inventory=0.57, shock=0.78, rivals=0.83; last update: Reacting to the competitor price gap (our 5.0 vs competitor average 5.7) by increasing price aggressiveness and competitor reactivity. Tuning demand sensitivity upward to resolve the slight shortage while reinforcing inventory caution to stay lean and flexible.; fallback forecast=184, price=5.00, quantity=60; final forecast=188, price=5.20, quantity=60 |
| 2 | Hyperscaler | llm-adaptive | 198.00 | 21.00 | 4.60 | 0.40 | 120.00 | none | adaptive state risk=0.78, price=0.73, demand=0.65, inventory=0.29, shock=0.48, rivals=0.49; last update: Secured strong market share (>50%) but lagging in profit compared to premium competitors. Decreased inventory caution and increased risk tolerance to ensure capacity readiness and prevent future shortages. Aggressive pricing and slightly higher competitor reactivity allow us to leverage our scale advantage while cautiously absorbing margin potential.; fallback forecast=198, price=4.60, quantity=120; final forecast=219, price=5.00, quantity=120 |
| 2 | PremiumCloud | llm-adaptive | 193.00 | 10.00 | 7.00 | -0.20 | 20.00 | none | adaptive state risk=0.37, price=0.59, demand=0.46, inventory=0.75, shock=0.36, rivals=0.30; last update: Achieved the best profit along with a perfect 1.0 service rate in Round 1. We maintain our premium price discipline. We slightly increase inventory caution and demand sensitivity to safeguard our premium SLA reliability against strong demand, while reducing reactivity to lower-priced competitors.; fallback forecast=193, price=7.00, quantity=30; final forecast=203, price=6.80, quantity=20 |
| 2 | SpotBroker | llm-adaptive | 200.00 | 33.00 | 5.60 | 0.00 | 60.00 | inventory target capped quantity | adaptive state risk=0.61, price=0.57, demand=0.67, inventory=0.59, shock=0.80, rivals=0.87; last update: Competitors averaged 5.70 while we priced at 5.20, leading to zero ending inventory and a minor shortage. We are increasing competitor reactivity and price aggressiveness to close the margin gap, while slightly boosting inventory caution to remain light and flexible.; fallback forecast=200, price=5.60, quantity=50; final forecast=233, price=5.60, quantity=60 |
| 3 | Hyperscaler | llm-adaptive | 198.00 | 22.00 | 4.60 | 0.40 | 120.00 | none | adaptive state risk=0.80, price=0.74, demand=0.66, inventory=0.28, shock=0.48, rivals=0.51; last update: Strong performance in round 2 achieving the highest profitability and a dominant 57% market share. To maintain this market lead and prioritize capacity continuity, we slightly increase our risk tolerance and price aggressiveness while reducing inventory caution to guarantee high service rates and continuous throughput.; fallback forecast=198, price=4.60, quantity=120; final forecast=220, price=5.00, quantity=120 |
| 3 | PremiumCloud | llm-adaptive | 195.00 | 11.00 | 7.00 | -0.20 | 20.00 | none | adaptive state risk=0.38, price=0.58, demand=0.46, inventory=0.77, shock=0.36, rivals=0.29; last update: Maintained a perfect 100% service rate with strong profitability. Restricting price aggressiveness and competitor reactivity to protect our premium positioning and price discipline, while slightly raising inventory caution to maintain impeccable SLA standards.; fallback forecast=195, price=7.00, quantity=30; final forecast=206, price=6.80, quantity=20 |
| 3 | SpotBroker | llm-adaptive | 200.00 | 35.00 | 5.60 | 0.00 | 50.00 | none | adaptive state risk=0.60, price=0.61, demand=0.70, inventory=0.63, shock=0.82, rivals=0.89; last update: Increasing competitor reactivity and price aggressiveness to exploit the gap with the competitor average price (5.9 vs our 5.6). Raising inventory caution and demand sensitivity to correct the overforecast and maintain a highly flexible, low-inventory stance.; fallback forecast=200, price=5.60, quantity=50; final forecast=235, price=5.60, quantity=50 |

## Adaptive Strategy Trace Samples

| Round | Agent | Personality | Price Delta | Inventory Delta | Risk Delta | Price State | Inventory State | Risk State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hyperscaler | Scale aggressor | 0.02 | -0.02 | 0.03 | 0.70 | 0.32 | 0.75 | Secured dominant market share and top profit in Round 0 with zero remaining inventory. To maintain capacity readiness and capture potential demand spikes, we marginally increase risk tolerance and reduce inventory caution, ensuring we do not run into capacity bottlenecks while preserving our competitive pricing edge. |
| 0 | PremiumCloud | Reputation guardian | 0.01 | 0.02 | -0.01 | 0.59 | 0.74 | 0.37 | Round 0 profit was highly optimal with a perfect 1.0 service rate at our premium price point. I am marginally increasing inventory caution to secure our high-uptime commitment, slightly raising price aggressiveness to sustain our premium positioning, and reducing competitor reactivity to ignore lower-priced rivals. |
| 0 | SpotBroker | Agile spread hunter | 0.07 | 0.03 | 0.04 | 0.51 | 0.57 | 0.60 | Reacting to the competitor price gap (our 5.0 vs competitor average 5.7) by increasing price aggressiveness and competitor reactivity. Tuning demand sensitivity upward to resolve the slight shortage while reinforcing inventory caution to stay lean and flexible. |
| 1 | Hyperscaler | Scale aggressor | 0.02 | -0.03 | 0.03 | 0.73 | 0.29 | 0.78 | Secured strong market share (>50%) but lagging in profit compared to premium competitors. Decreased inventory caution and increased risk tolerance to ensure capacity readiness and prevent future shortages. Aggressive pricing and slightly higher competitor reactivity allow us to leverage our scale advantage while cautiously absorbing margin potential. |
| 1 | PremiumCloud | Reputation guardian | 0.00 | 0.01 | 0.00 | 0.59 | 0.75 | 0.37 | Achieved the best profit along with a perfect 1.0 service rate in Round 1. We maintain our premium price discipline. We slightly increase inventory caution and demand sensitivity to safeguard our premium SLA reliability against strong demand, while reducing reactivity to lower-priced competitors. |
| 1 | SpotBroker | Agile spread hunter | 0.05 | 0.02 | 0.02 | 0.57 | 0.59 | 0.61 | Competitors averaged 5.70 while we priced at 5.20, leading to zero ending inventory and a minor shortage. We are increasing competitor reactivity and price aggressiveness to close the margin gap, while slightly boosting inventory caution to remain light and flexible. |
| 2 | Hyperscaler | Scale aggressor | 0.02 | -0.01 | 0.02 | 0.74 | 0.28 | 0.80 | Strong performance in round 2 achieving the highest profitability and a dominant 57% market share. To maintain this market lead and prioritize capacity continuity, we slightly increase our risk tolerance and price aggressiveness while reducing inventory caution to guarantee high service rates and continuous throughput. |
| 2 | PremiumCloud | Reputation guardian | -0.01 | 0.02 | 0.01 | 0.58 | 0.77 | 0.38 | Maintained a perfect 100% service rate with strong profitability. Restricting price aggressiveness and competitor reactivity to protect our premium positioning and price discipline, while slightly raising inventory caution to maintain impeccable SLA standards. |
| 2 | SpotBroker | Agile spread hunter | 0.05 | 0.04 | -0.02 | 0.61 | 0.63 | 0.60 | Increasing competitor reactivity and price aggressiveness to exploit the gap with the competitor average price (5.9 vs our 5.6). Raising inventory caution and demand sensitivity to correct the overforecast and maintain a highly flexible, low-inventory stance. |
| 3 | Hyperscaler | Scale aggressor | 0.01 | -0.01 | 0.01 | 0.75 | 0.27 | 0.81 | Secured dominant market share (64%) and maximum profit in Round 3 with zero final inventory. We slightly lower inventory caution and lift risk tolerance to secure capacity readiness against future demand spikes, while keeping price aggressiveness competitive to lock in our scale advantage. |
| 3 | PremiumCloud | Reputation guardian | -0.01 | 0.02 | 0.00 | 0.57 | 0.79 | 0.38 | Maintaining perfect SLA reliability (1.0 service rate) and stable profitability. Reducing competitor reactivity and slightly lowering price aggressiveness ensures we preserve our premium price discipline rather than reacting to cheaper competitor averages. |
| 3 | SpotBroker | Agile spread hunter | 0.05 | 0.03 | 0.02 | 0.67 | 0.66 | 0.61 | Increasing price aggressiveness and competitor reactivity to safely close the gap with the higher market average price of 5.9, while slightly adjusting inventory caution to mitigate the minor shortage from last round. |

## Conclusion Notes

- **Winner:** `Hyperscaler` ends with cumulative profit `1445.92`, the highest value in this run.
- **Service leader:** `Hyperscaler` posts the strongest average service rate at `100.00%`.
- **Pricing posture:** `PremiumCloud` maintains the highest average price at `6.77`.
- **Market fulfillment:** the run sells `2280.61` units against `2298.00` true demand for a fulfillment ratio of `99.24%`.
- **Operational stress:** peer transfers total `37.92` units, customer reallocation totals `195.91`, final SLA backlog is `0.96`, with `0` dump flags and `2` default flags.

## Appendix: Agent Configuration

| Agent | Forecast | Pricing | Allocation | Risk | Base Price | Max Quantity |
| --- | --- | --- | --- | --- | --- | --- |
| Hyperscaler | momentum_chaser | share_grabber | capacity_expander | growth_tolerant | 4.60 | 120 |
| PremiumCloud | signal_smoother | premium_keeper | buffered_allocator | sla_guard | 5.40 | 120 |
| SpotBroker | volatility_reader | spread_hunter | inventory_light | inventory_guard | 4.90 | 80 |
