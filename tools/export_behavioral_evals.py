#!/usr/bin/env python3
"""Export parseable Superskills routing eval tables as deterministic JSONL."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Sequence

if __package__:
    from .validate_repo import routing_cases_from_text
else:
    from validate_repo import routing_cases_from_text

DEFAULT_ROOT = Path(__file__).resolve().parents[1]


class EvalExportError(ValueError):
    """Raised when behavioral evals cannot be exported safely."""


def source_skill_for(path: Path, root: Path) -> str:
    relative = path.relative_to(root)
    parts = relative.parts
    if len(parts) < 5 or parts[0] != "skills":
        raise EvalExportError(f"unexpected behavioral eval path: {relative}")
    return f"{parts[1]}/{parts[2]}"


def export_cases(root: Path | str) -> list[dict[str, object]]:
    root = Path(root).resolve()
    files = sorted(root.glob("skills/*/*/maintenance/behavioral-evals.md"))
    records: list[dict[str, object]] = []

    for path in files:
        relative = path.relative_to(root).as_posix()
        source_skill = source_skill_for(path, root)
        cases = routing_cases_from_text(path.read_text(encoding="utf-8"))
        for index, case in enumerate(cases, start=1):
            if not case.prompt or not case.primary:
                raise EvalExportError(
                    f"{relative}:{case.line}: routing cases require prompt and primary"
                )
            records.append(
                {
                    "id": case.case_id or f"{source_skill}:{index:03d}",
                    "source": relative,
                    "source_skill": source_skill,
                    "line": case.line,
                    "prompt": case.prompt,
                    "primary": case.primary,
                    "secondary": case.secondary,
                    "must_avoid": case.must_avoid,
                }
            )

    if not records:
        raise EvalExportError("no parseable routing eval tables found")

    records.sort(key=lambda record: (str(record["source"]), int(record["line"]), str(record["id"])))
    id_counts = Counter(str(record["id"]) for record in records)
    duplicates = sorted(case_id for case_id, count in id_counts.items() if count > 1)
    if duplicates:
        raise EvalExportError(f"duplicate behavioral eval IDs: {duplicates}")
    return records


def write_jsonl(records: Sequence[dict[str, object]], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    content = "".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records)
    output.write_text(content, encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--output", type=Path, default=Path("dist/behavioral-evals.jsonl"))
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate and count cases without writing an output file.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        records = export_cases(args.root)
    except EvalExportError as exc:
        print(f"behavioral eval export failed: {exc}", file=sys.stderr)
        return 1

    source_count = len({str(record["source"]) for record in records})
    if args.check:
        print(f"behavioral eval export passed: {len(records)} cases from {source_count} files")
        return 0

    output = args.output
    if not output.is_absolute():
        output = Path(args.root).resolve() / output
    write_jsonl(records, output)
    print(f"behavioral evals exported: {len(records)} cases from {source_count} files -> {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
