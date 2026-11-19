#!/usr/bin/env python3
"""Package each Skill as an uploadable ZIP for claude.ai (Customize > Skills).

One ZIP per Skill, with the Skill folder as the single root entry and only runtime
files inside. Archives are byte-reproducible for the same source.
"""

from __future__ import annotations

import argparse
import os
import sys
import zipfile
from pathlib import Path
from typing import Sequence

if __package__:
    from .layout import route_of, skill_dir, skill_dirs
else:
    from layout import route_of, skill_dir, skill_dirs

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = Path("dist/claude-web")
FIXED_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


class PackageError(ValueError):
    """Raised when a web package cannot be built."""


def package_skill(source: Path, output: Path) -> Path:
    archive = output / f"{source.name}.zip"
    # Build next to the target and rename, so a failed run never leaves a truncated archive behind.
    partial = output / f"{source.name}.zip.partial"
    files = sorted(path for path in source.rglob("*") if path.is_file())
    try:
        with zipfile.ZipFile(partial, "w", zipfile.ZIP_DEFLATED) as bundle:
            for path in files:
                name = f"{source.name}/{path.relative_to(source).as_posix()}"
                info = zipfile.ZipInfo(name, FIXED_TIMESTAMP)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                bundle.writestr(info, path.read_bytes())
        os.replace(partial, archive)
    except BaseException:
        partial.unlink(missing_ok=True)
        raise
    return archive


def package(root: Path | str = DEFAULT_ROOT, output: Path | str = DEFAULT_OUTPUT, routes: Sequence[str] = ()) -> list[Path]:
    root = Path(root).resolve()
    output_path = Path(output)
    if not output_path.is_absolute():
        output_path = root / output_path
    available = {route_of(path): path for path in skill_dirs(root)}
    unknown = sorted(set(routes) - set(available))
    if unknown:
        raise PackageError(f"unknown Skill routes: {unknown}")
    selected = sorted(routes) if routes else sorted(available)
    output_path.mkdir(parents=True, exist_ok=True)
    # Replace only archives this tool produces; the directory may hold unrelated files.
    for name in (path.name for path in available.values()):
        (output_path / f"{name}.zip").unlink(missing_ok=True)
    return [package_skill(skill_dir(root, route), output_path) for route in selected]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--skill", action="append", default=[], help="category/skill; repeat as needed (default: all)")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        archives = package(args.root, args.output, args.skill)
    except PackageError as exc:
        print(f"web package build failed: {exc}", file=sys.stderr)
        return 1
    print(f"web packages built: {len(archives)} Skill ZIPs -> {args.output.as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
