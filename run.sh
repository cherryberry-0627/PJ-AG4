#!/usr/bin/env bash
set -euo pipefail

SEED="${SEED:-7}"
ROUNDS="${ROUNDS:-12}"
OUTPUT_ROOT="${OUTPUT_ROOT:-${OUTPUT_DIR:-outputs/reproduce}}"
SCENARIOS="${SCENARIOS:-}"
AGENT_MODES="${AGENT_MODES:-}"
FIGURES="${FIGURES:-0}"

python3 -m pip install -e . --no-build-isolation

args=(
  --seed "$SEED"
  --rounds "$ROUNDS"
  --output-root "$OUTPUT_ROOT"
)

if [[ -n "$SCENARIOS" ]]; then
  args+=(--scenarios "$SCENARIOS")
fi

if [[ -n "$AGENT_MODES" ]]; then
  args+=(--agent-modes "$AGENT_MODES")
fi

if [[ "$FIGURES" == "1" ]]; then
  args+=(--figures)
fi

python3 main.py "${args[@]}"
