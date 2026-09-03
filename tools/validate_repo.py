#!/usr/bin/env python3
"""Structural, routing, link and behavioral-eval checks for superskills."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence

if __package__:
    from .validator_markdown import routing_cases_from_text
    from .validator_repo import DEFAULT_ROOT, ValidationResult, validate_repository
else:
    from validator_markdown import routing_cases_from_text
    from validator_repo import DEFAULT_ROOT, ValidationResult, validate_repository

__all__ = ["ValidationResult", "routing_cases_from_text", "validate_repository"]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=DEFAULT_ROOT,
        help="Repository root to validate (default: repository containing this script).",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    result = validate_repository(build_parser().parse_args(argv).root)
    if result.warnings:
        print("superskills validation advisories:\n")
        for warning in result.warnings:
            print(f"- {warning}")
        print()
    if result.errors:
        print("superskills validation failed:\n")
        for error in result.errors:
            print(f"- {error}")
        return 1
    print(f"superskills validation passed: {result.skill_count} skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
