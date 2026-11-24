#!/usr/bin/env python3
"""Regenerate every host adapter from SKILL.md in one command.

SKILL.md frontmatter stays the single source of truth; the adapters are
generated sidecars. After any SKILL.md or plugin.json change, run::

    python tools/sync_adapters.py            # regenerate all adapters
    python tools/sync_adapters.py --check    # fail when any adapter is stale

This runs, in order: ``generate_skill_yaml.py`` (Muse), then
``generate_openai_yaml.py`` (ChatGPT + Codex), then ``build_manifests.py``
(the two marketplace manifests). ``--check`` runs each generator's own
``--check`` mode and reports the first failure; it writes nothing.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Sequence

DEFAULT_ROOT = Path(__file__).resolve().parents[1]

STEPS = (
    ("generate_skill_yaml.py", "Muse skill.yaml"),
    ("generate_openai_yaml.py", "ChatGPT/Codex openai.yaml"),
    ("build_manifests.py", "marketplace manifests"),
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail when any generated adapter is missing, stale or orphaned; write nothing.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.root.resolve()
    tools_dir = root / "tools"
    for script, label in STEPS:
        command = [sys.executable, str(tools_dir / script), "--root", str(root)]
        if args.check:
            command.append("--check")
        completed = subprocess.run(command, check=False)
        if completed.returncode != 0:
            print(f"sync_adapters: {label} step failed ({script})", file=sys.stderr)
            return completed.returncode or 1
    print("adapters are in sync" if args.check else "adapters regenerated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
