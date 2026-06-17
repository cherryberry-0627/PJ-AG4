#!/usr/bin/env python3
"""
Generate a detailed round-level report with AI reasoning and three figures
from a simulation_results.csv file.

Usage:
    PYTHONPATH=src python3 scripts/generate_detailed_report.py \
        --csv outputs/three_modes/llm-adaptive/simulation_results.csv \
        --output-dir outputs/three_modes/llm-adaptive
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def _parse_csv(csv_path: Path) -> list[dict[str, str]]:
    with csv_path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _format_value(value: object) -> str:
    try:
        return f"{float(value):.4f}"
    except (TypeError, ValueError):
        return str(value)


def _generate_markdown(rows: list[dict[str, str]], output_dir: Path) -> Path:
    lines: list[str] = []
    lines.append("# Simulation Detailed Log")
    lines.append("")
    lines.append("**Source**: `simulation_results.csv`")
    lines.append("")
    lines.append("---")
    lines.append("")

    for row in rows:
        name = row["agent_name"]
        round_index = row["round"]
        lines.append(f"## Round {round_index} - {name}")
        lines.append("")

        lines.append("### Decision Parameters")
        lines.append(f"- **Forecast demand**: {row['forecast_demand']}")
        lines.append(f"- **Price**: {row['price']}")
        lines.append(f"- **Quantity**: {row['quantity']}")
        lines.append(f"- **Decision source**: {row['decision_source']}")
        lines.append("")

        state_raw = row.get("strategy_state", "")
        if state_raw:
            try:
                state = json.loads(state_raw)
                lines.append("### Strategy State")
                for key, value in state.items():
                    lines.append(f"- **{key}**: {_format_value(value)}")
                lines.append("")
            except json.JSONDecodeError:
                pass

        reason = row.get("strategy_update_reason", "")
        if reason:
            lines.append("### AI Strategy Update Reason")
            lines.append(f"> {reason}")
            lines.append("")

        trace_raw = row.get("strategy_update_trace", "")
        if trace_raw:
            try:
                trace = json.loads(trace_raw)
                lines.append("### AI Raw Output")
                lines.append(f"- **Raw delta**: {trace.get('raw_delta', {})}")
                lines.append(f"- **Bounded delta**: {trace.get('bounded_delta', {})}")
                lines.append(f"- **Reason**: {trace.get('reason', '')}")
                lines.append("")
            except json.JSONDecodeError:
                lines.append("### AI Raw Output")
                lines.append(f"```\n{trace_raw[:300]}\n```")
                lines.append("")

        decision_trace = row.get("decision_trace", "")
        if decision_trace:
            lines.append("### Decision Trace")
            lines.append(f"```\n{decision_trace}\n```")
            lines.append("")

        lines.append("### Market Outcome")
        lines.append(f"- **True demand**: {row['demand_true']}")
        lines.append(f"- **Allocated demand**: {float(row['allocated_demand']):.1f}")
        lines.append(f"- **Realized sales**: {float(row['realized_sales']):.1f}")
        lines.append(f"- **Market share**: {float(row['demand_share']):.2%}")
        lines.append(f"- **Profit**: {float(row['profit']):.2f}")
        lines.append(f"- **Cumulative profit**: {float(row['cum_profit']):.2f}")
        lines.append(f"- **Inventory end**: {row['inventory_end']}")
        lines.append(f"- **Shortage**: {row['shortage_post_transfer']}")
        lines.append(f"- **Service rate**: {float(row['service_rate']):.2%}")
        lines.append(f"- **Reputation end**: {float(row['reputation_end']):.3f}")
        lines.append(f"- **Dump flag**: {row['dump_flag']}")
        lines.append(f"- **Default flag**: {row['default_flag']}")
        lines.append("")

        lines.append("### Cost Breakdown")
        lines.append(f"- **Revenue**: {float(row['revenue']):.2f}")
        lines.append(f"- **Production cost**: {float(row['prod_cost']):.2f}")
        lines.append(f"- **Holding cost**: {float(row['holding_cost']):.2f}")
        lines.append(f"- **Obsolescence cost**: {float(row['obsolescence_cost']):.2f}")
        lines.append(f"- **SLA penalty**: {float(row['sla_penalty']):.2f}")
        lines.append(f"- **Menu cost**: {float(row['menu_cost']):.2f}")
        if float(row["transfer_cost"]) > 0:
            lines.append(f"- **Transfer cost**: {float(row['transfer_cost']):.2f}")
        if float(row["transfer_revenue"]) > 0:
            lines.append(f"- **Transfer revenue**: {float(row['transfer_revenue']):.2f}")
        lines.append("")

        lines.append("---")
        lines.append("")

    lines.append("## Summary")
    lines.append("")
    final_profits: dict[str, float] = {}
    for row in rows:
        final_profits[row["agent_name"]] = float(row["cum_profit"])
    for name, profit in sorted(final_profits.items(), key=lambda item: -item[1]):
        lines.append(f"- **{name}**: cumulative profit {profit:.2f}")
    lines.append("")

    out_path = output_dir / "detailed_log.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path


def _generate_figures(rows: list[dict[str, str]], output_dir: Path) -> list[Path]:
    agents = sorted({row["agent_name"] for row in rows})
    colors = {"Hyperscaler": "#e74c3c", "PremiumCloud": "#3498db", "SpotBroker": "#2ecc71"}

    fig1, ax1 = plt.subplots(figsize=(10, 6))
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    ax2_twin = ax2.twinx()
    fig3, ax3 = plt.subplots(figsize=(10, 6))

    for name in agents:
        agent_rows = sorted((row for row in rows if row["agent_name"] == name), key=lambda row: int(row["round"]))
        agent_rounds = [int(row["round"]) for row in agent_rows]
        profits = [float(row["profit"]) for row in agent_rows]
        cum_profits = [float(row["cum_profit"]) for row in agent_rows]
        prices = [float(row["price"]) for row in agent_rows]
        quantities = [int(row["quantity"]) for row in agent_rows]
        reputations = [float(row["reputation_end"]) for row in agent_rows]

        ax1.plot(agent_rounds, profits, "o--", color=colors.get(name, "#333"), label=f"{name} (round)")
        ax1.plot(
            agent_rounds,
            cum_profits,
            "s-",
            color=colors.get(name, "#333"),
            label=f"{name} (cumulative)",
            linewidth=2,
        )

        offset = (agents.index(name) - 1) * 0.25
        ax2.plot(agent_rounds, prices, "o-", color=colors.get(name, "#333"), label=f"{name} price")
        ax2_twin.bar(
            [round_index + offset for round_index in agent_rounds],
            quantities,
            width=0.2,
            color=colors.get(name, "#333"),
            alpha=0.25,
            label=f"{name} quantity",
        )

        ax3.plot(agent_rounds, reputations, "o-", color=colors.get(name, "#333"), label=name, linewidth=2)

    ax1.set_xlabel("Round")
    ax1.set_ylabel("Profit")
    ax1.set_title("Profit & Cumulative Profit by Agent")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.set_xlabel("Round")
    ax2.set_ylabel("Price")
    ax2_twin.set_ylabel("Quantity")
    ax2.set_title("Price & Quantity by Agent")
    ax2.legend(loc="upper left")
    ax2_twin.legend(loc="upper right")
    ax2.grid(True, alpha=0.3)

    ax3.set_xlabel("Round")
    ax3.set_ylabel("Reputation")
    ax3.set_title("Reputation Evolution by Agent")
    ax3.legend()
    ax3.grid(True, alpha=0.3)

    paths: list[Path] = []
    for idx, fig in enumerate([fig1, fig2, fig3], 1):
        figure_path = output_dir / f"fig{idx}_detailed.png"
        fig.savefig(figure_path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        paths.append(figure_path)

    return paths


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate detailed report and figures from simulation CSV.")
    parser.add_argument("--csv", type=Path, required=True, help="Path to simulation_results.csv")
    parser.add_argument("--output-dir", type=Path, required=True, help="Output directory")
    args = parser.parse_args()

    rows = _parse_csv(args.csv)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    md_path = _generate_markdown(rows, args.output_dir)
    fig_paths = _generate_figures(rows, args.output_dir)

    print(f"Detailed log: {md_path}")
    for path in fig_paths:
        print(f"Figure: {path}")


if __name__ == "__main__":
    main()
