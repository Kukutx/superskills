#!/usr/bin/env python3
"""Build a reproducible, minimal Superskills bundle for a ChatGPT/GPT profile."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
BUNDLE_FORMAT = "superskills.bundle.v1"


class BundleError(ValueError):
    """Raised when a requested bundle is invalid or unsafe to build."""


@dataclass(frozen=True)
class BundleSummary:
    output: Path
    file_count: int
    total_bytes: int
    approx_tokens: int
    source_commit: str | None


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def approx_tokens(byte_count: int) -> int:
    # A deliberately coarse, clearly labelled context-budget estimate.
    return math.ceil(byte_count / 4)


def git_commit(root: Path) -> str | None:
    try:
        completed = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
            timeout=3,
        )
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return None
    value = completed.stdout.strip()
    return value or None


def ensure_relative_directory(root: Path, raw: str, label: str) -> Path:
    path = (root / raw).resolve()
    try:
        path.relative_to(root.resolve())
    except ValueError as exc:
        raise BundleError(f"{label} escapes the repository: {raw}") from exc
    if not path.is_dir():
        raise BundleError(f"{label} directory does not exist: {raw}")
    return path


def normalize_skill_route(raw: str) -> str:
    route = raw.strip().strip("/")
    parts = route.split("/")
    if len(parts) != 2 or any(not part for part in parts):
        raise BundleError(f"invalid Skill route '{raw}'; expected category/skill")
    return route


def parse_reference(raw: str) -> tuple[str, str]:
    if ":" not in raw:
        raise BundleError(
            f"invalid reference '{raw}'; expected category/skill:reference-name"
        )
    owner_raw, name_raw = raw.rsplit(":", 1)
    owner = normalize_skill_route(owner_raw)
    name = name_raw.strip()
    if not name:
        raise BundleError(f"reference name is empty in '{raw}'")
    if "/" in name or "\\" in name or name in {".", ".."}:
        raise BundleError(f"reference must be a direct filename, not a path: '{raw}'")
    if not name.endswith(".md"):
        name += ".md"
    return owner, name


def safe_replace_directory(output: Path) -> None:
    if not output.exists():
        return
    manifest = output / "manifest.json"
    if not output.is_dir() or not manifest.is_file():
        raise BundleError(
            f"refusing to replace non-bundle output '{output}'; choose another --output"
        )
    try:
        payload = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise BundleError(f"refusing to replace output with an invalid manifest: {output}") from exc
    if payload.get("format") != BUNDLE_FORMAT:
        raise BundleError(f"refusing to replace an unknown directory: {output}")
    shutil.rmtree(output)


def build_bundle(
    *,
    root: Path | str,
    profile: str,
    skills: Sequence[str],
    references: Sequence[str] = (),
    output: Path | str | None = None,
) -> BundleSummary:
    root = Path(root).resolve()
    profile_dir = ensure_relative_directory(root, profile, "profile")
    profile_instructions = profile_dir / "project-instructions.md"
    if not profile_instructions.is_file():
        raise BundleError(f"profile is missing project-instructions.md: {profile}")

    selected_skills = sorted({normalize_skill_route(route) for route in skills})
    if not selected_skills:
        raise BundleError("select at least one --skill")

    source_files: list[Path] = [
        profile_instructions,
        root / "skills" / "meta" / "skill-router" / "skill.md",
    ]
    if not source_files[1].is_file():
        raise BundleError("authoritative Skill Router is missing")

    for route in selected_skills:
        entrypoint = root / "skills" / route / "skill.md"
        if not entrypoint.is_file():
            raise BundleError(f"Skill does not exist: {route}")
        source_files.append(entrypoint)

    selected_references: list[str] = []
    for raw in references:
        owner, name = parse_reference(raw)
        if owner not in selected_skills:
            raise BundleError(
                f"reference owner '{owner}' is not selected; add --skill {owner}"
            )
        path = root / "skills" / owner / "references" / name
        if not path.is_file():
            raise BundleError(f"reference does not exist: {owner}:{name}")
        source_files.append(path)
        selected_references.append(f"{owner}:{name}")

    unique_sources = sorted({path.resolve() for path in source_files}, key=lambda path: path.relative_to(root).as_posix())
    for path in unique_sources:
        relative = path.relative_to(root).as_posix()
        if "/maintenance/" in f"/{relative}/":
            raise BundleError(f"maintenance content cannot enter runtime bundles: {relative}")

    if output is None:
        output_path = root / "dist" / profile_dir.name
    else:
        output_path = Path(output)
        if not output_path.is_absolute():
            output_path = root / output_path
    output_path = output_path.resolve()
    if output_path == root or output_path in root.parents:
        raise BundleError("output cannot be the repository root or one of its ancestors")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = Path(tempfile.mkdtemp(prefix=f".{output_path.name}-", dir=output_path.parent))
    try:
        manifest_files: list[dict[str, object]] = []
        total_bytes = 0
        for source in unique_sources:
            relative = source.relative_to(root)
            destination = temp_path / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            data = source.read_bytes()
            destination.write_bytes(data)
            size = len(data)
            total_bytes += size
            manifest_files.append(
                {
                    "path": relative.as_posix(),
                    "bytes": size,
                    "sha256": sha256_bytes(data),
                    "approx_tokens": approx_tokens(size),
                }
            )

        commit = git_commit(root)
        manifest = {
            "format": BUNDLE_FORMAT,
            "profile": profile_dir.relative_to(root).as_posix(),
            "source_commit": commit,
            "skills": selected_skills,
            "references": sorted(set(selected_references)),
            "files": manifest_files,
            "totals": {
                "files": len(manifest_files),
                "bytes": total_bytes,
                "approx_tokens": approx_tokens(total_bytes),
            },
        }
        (temp_path / "manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

        safe_replace_directory(output_path)
        temp_path.replace(output_path)
    except Exception:
        shutil.rmtree(temp_path, ignore_errors=True)
        raise

    return BundleSummary(
        output=output_path,
        file_count=len(manifest_files),
        total_bytes=total_bytes,
        approx_tokens=approx_tokens(total_bytes),
        source_commit=commit,
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--profile", required=True, help="Profile directory, for example gpts/kukutx")
    parser.add_argument("--skill", action="append", default=[], help="Skill route category/skill; repeat as needed")
    parser.add_argument(
        "--reference",
        action="append",
        default=[],
        help="Focused reference category/skill:reference-name; repeat as needed",
    )
    parser.add_argument("--output", type=Path, help="Output directory; default dist/<profile-name>")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        summary = build_bundle(
            root=args.root,
            profile=args.profile,
            skills=args.skill,
            references=args.reference,
            output=args.output,
        )
    except BundleError as exc:
        print(f"bundle build failed: {exc}", file=sys.stderr)
        return 1

    commit = summary.source_commit or "unknown"
    print(
        "bundle built: "
        f"{summary.output} | {summary.file_count} files | {summary.total_bytes} bytes | "
        f"~{summary.approx_tokens} tokens | source {commit}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
