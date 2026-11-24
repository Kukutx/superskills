#!/usr/bin/env python3
"""Report behavioral-eval coverage: which Skills have no maintenance/ dir
and which have no behavioral-evals rows.

This is a non-blocking report, not a gate: a Skill without eval rows is a
gap to fill when its boundary changes, not a validation failure. CI runs it
as an advisory step and it always exits 0::

    python tools/eval_coverage.py
    python tools/eval_coverage.py --root <repo>
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from pathlib import Path
from typing import Sequence

if __package__:
    from .layout import MAINTENANCE_DIR, maintenance_dir, route_of, skill_dirs
    from .validator_markdown import routing_cases_from_text
else:
    from layout import MAINTENANCE_DIR, maintenance_dir, route_of, skill_dirs
    from validator_markdown import routing_cases_from_text

DEFAULT_ROOT = Path(__file__).resolve().parents[1]


@dataclass
class CoverageReport:
    total_skills: int = 0
    with_maintenance: int = 0
    with_eval_rows: int = 0
    total_eval_rows: int = 0
    no_maintenance: list[str] = field(default_factory=list)
    no_eval_rows: list[str] = field(default_factory=list)
    categories_without_evals: list[str] = field(default_factory=list)


def coverage_report(root: Path) -> CoverageReport:
    root = Path(root).resolve()
    report = CoverageReport()
    categories: dict[str, dict[str, int]] = {}
    for directory in skill_dirs(root):
        route = route_of(directory)
        category = route.split("/", 1)[0]
        stats = categories.setdefault(category, {"skills": 0, "with_rows": 0})
        stats["skills"] += 1
        report.total_skills += 1
        maintenance = maintenance_dir(root, route)
        eval_file = maintenance / "behavioral-evals.md"
        if maintenance.is_dir():
            report.with_maintenance += 1
        else:
            report.no_maintenance.append(route)
        rows = 0
        if eval_file.is_file():
            rows = len(routing_cases_from_text(eval_file.read_text(encoding="utf-8")))
        if rows:
            report.with_eval_rows += 1
            report.total_eval_rows += rows
            stats["with_rows"] += 1
        else:
            report.no_eval_rows.append(route)
    report.no_maintenance.sort()
    report.no_eval_rows.sort()
    report.categories_without_evals = sorted(
        category for category, stats in categories.items() if stats["with_rows"] == 0
    )
    return report


def format_report(report: CoverageReport) -> str:
    lines = [
        f"behavioral-eval coverage: {report.with_eval_rows}/{report.total_skills} skills "
        f"have eval rows ({report.total_eval_rows} rows); "
        f"{report.with_maintenance}/{report.total_skills} have a maintenance/ dir",
    ]
    if report.categories_without_evals:
        lines.append(
            "categories with zero behavioral-evals rows: "
            + ", ".join(report.categories_without_evals)
        )
    if report.no_maintenance:
        lines.append(
            f"skills with no maintenance/ dir ({len(report.no_maintenance)}): "
            + ", ".join(report.no_maintenance)
        )
    if report.no_eval_rows:
        lines.append(
            f"skills with no behavioral-evals rows ({len(report.no_eval_rows)}): "
            + ", ".join(report.no_eval_rows)
        )
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    print(format_report(coverage_report(args.root)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
