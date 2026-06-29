# PJ-AG4 LLM Scenario Experiment Dataset

This directory contains the complete cleaned experiment data exported from
`outputs/llm_scenario_experiments`.

Included:

- Per-scenario `simulation_results.csv` files for all available LLM variants.
- Per-scenario `simulation_report.md` files where present.
- Cross-scenario summary CSV files.
- Comparison reports for aligned LLM modes and context-engineering variants.
- `pj_ag4_experiment_csvs_context_engineering.zip`, a compact archive of CSV data.

Excluded:

- Generated dashboard HTML files, to keep the repository clean and avoid large
  repeated visualization payloads.

Main variants:

- `direct_llm_seed7_r12`
- `llm_context_seed7_r12`
- `llm_context_engineering_seed7_r12`
- `llm_context_engineered_seed7_r12`
- `llm_context_adaptive_seed7_r12`
- `llm_context_adaptive_context_engineering_seed7_r12`
- `full_seed7_r12`
- `calibrated_seed7_r12`
- `calibrated_v2_seed7_r12`

Common setting for the aligned 12-round runs:

- Seed: `7`
- Rounds: `12`
- Scenarios: `baseline`, `price_war`, `supply_shock`,
  `high_volatility`, `no_reputation`, `no_transfer`
