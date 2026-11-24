#!/usr/bin/env python3
"""Generate one Muse ``skill.yaml`` per Skill from its SKILL.md frontmatter.

SKILL.md frontmatter stays the single source of truth: ``name`` and
``description`` are copied verbatim, ``category`` comes from the plugin
directory, ``title`` defaults to the SKILL.md H1, and ``triggers`` are
derived from the description's "Use when" clause plus the skill name.
Never hand-edit a generated ``skill.yaml``; re-run this tool instead::

    python tools/generate_skill_yaml.py            # write all 105+ files
    python tools/generate_skill_yaml.py --check    # fail when any file is stale
    python tools/generate_skill_yaml.py --skill development/code-review

The validator (``tools/validate_repo.py``) rejects a missing, unparseable
or drifted ``skill.yaml``.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Sequence

if __package__:
    from .layout import ENTRYPOINT, skill_dirs
    from .validator_markdown import frontmatter
else:
    from layout import ENTRYPOINT, skill_dirs
    from validator_markdown import frontmatter

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
SKILL_YAML = "skill.yaml"
MAX_TRIGGERS = 5
MAX_TRIGGER_CHARS = 60


def skill_title(text: str, name: str) -> str:
    """First H1 of SKILL.md, falling back to the hyphenated name."""
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return name.replace("-", " ").title()


def derive_triggers(name: str, description: str) -> list[str]:
    """Short trigger phrases from the description.

    The skill name in plain words always comes first. Then up to four
    short phrases from the "Use when" clause, split on commas and "and",
    so the router can match the user's own wording. Phrases that are too
    long, contain a colon, or duplicate an earlier trigger are dropped.
    """
    triggers: list[str] = [name.replace("-", " ")]
    match = re.search(r"[Uu]se (?:when|for)\s+(.*?)(?:,?\s+not for\s+|$)", description)
    if not match:
        return triggers
    clause = match.group(1)
    clause = re.split(r",\s*not\s+", clause)[0]
    for raw in re.split(r",|\band\b", clause):
        phrase = raw.strip().rstrip(".").strip()
        phrase = re.sub(r"\s+", " ", phrase)
        if not phrase or len(phrase) > MAX_TRIGGER_CHARS:
            continue
        if ":" in phrase or phrase.lower() in {t.lower() for t in triggers}:
            continue
        if len(phrase.split()) < 2 or len(phrase.split()) > 8:
            continue
        triggers.append(phrase)
        if len(triggers) >= MAX_TRIGGERS:
            break
    return triggers


def _yaml_plain(value: str) -> str:
    """A plain YAML scalar on one line; descriptions never contain ': '."""
    return value.replace("\n", " ").strip()


def render_skill_yaml(name: str, title: str, description: str, category: str) -> str:
    triggers = derive_triggers(name, description)
    lines = [
        f"name: {name}",
        f"title: {_yaml_plain(title)}",
        f"description: {_yaml_plain(description)}",
        f"category: {category}",
        "include_in_prompt: false",
        "triggers:",
        *(f"- {_yaml_plain(trigger)}" for trigger in triggers),
    ]
    return "\n".join(lines) + "\n"


def skill_yaml_for(skill_dir: Path) -> tuple[str, str]:
    """Return (relative path, rendered content) for one skill directory."""
    text = (skill_dir / ENTRYPOINT).read_text(encoding="utf-8")
    metadata, errors = frontmatter(text)
    if errors or not metadata.get("name") or not metadata.get("description"):
        raise ValueError(f"{skill_dir / ENTRYPOINT}: cannot generate skill.yaml ({errors})")
    name = metadata["name"]
    category = skill_dir.parent.parent.name
    content = render_skill_yaml(
        name, skill_title(text, name), metadata["description"], category
    )
    return f"plugins/{category}/skills/{name}/{SKILL_YAML}", content


def generate(root: Path, only: str | None = None) -> dict[Path, str]:
    generated: dict[Path, str] = {}
    for directory in skill_dirs(root):
        route = f"{directory.parent.parent.name}/{directory.name}"
        if only and route != only:
            continue
        relative, content = skill_yaml_for(directory)
        generated[root / relative] = content
    if only and not generated:
        raise ValueError(f"no skill matches route '{only}'")
    return generated


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--check", action="store_true", help="Fail when a generated file is missing or stale.")
    parser.add_argument("--skill", help="Only generate one route, e.g. development/code-review.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.root.resolve()
    try:
        generated = generate(root, args.skill)
    except ValueError as error:
        print(f"skill.yaml generation failed: {error}", file=sys.stderr)
        return 1
    if args.check:
        stale = [
            path.relative_to(root).as_posix()
            for path, content in sorted(generated.items())
            if not path.is_file() or path.read_text(encoding="utf-8") != content
        ]
        if stale:
            print(
                f"skill.yaml files are out of date: {stale}; run python tools/generate_skill_yaml.py",
                file=sys.stderr,
            )
            return 1
        print(f"skill.yaml files are up to date ({len(generated)})")
        return 0
    for path, content in sorted(generated.items()):
        path.write_text(content, encoding="utf-8")
    print(f"skill.yaml files written: {len(generated)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
