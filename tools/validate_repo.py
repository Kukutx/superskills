#!/usr/bin/env python3
"""Lightweight structural checks for the superskills repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
ROUTER = SKILLS / "meta" / "skill-router" / "skill.md"
ALLOWED_SKILL_ENTRIES = {"skill.md", "references", "maintenance"}
PATH_RE = re.compile(r"`([a-z0-9-]+/[a-z0-9-]+)`")
MD_PATH_RE = re.compile(r"`((?:\.\.?/)?[^`\n]+\.md)`")


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data


def main() -> int:
    errors: list[str] = []
    skill_files = sorted(SKILLS.glob("*/*/skill.md"))
    skill_paths = {f"{p.parent.parent.name}/{p.parent.name}" for p in skill_files}

    if not skill_files:
        errors.append("No skills found")

    for skill_file in skill_files:
        skill_dir = skill_file.parent
        rel = skill_file.relative_to(ROOT)
        meta = frontmatter(skill_file.read_text(encoding="utf-8"))

        if not meta.get("name"):
            errors.append(f"{rel}: missing frontmatter name")
        elif meta["name"] != skill_dir.name:
            errors.append(
                f"{rel}: frontmatter name '{meta['name']}' != folder '{skill_dir.name}'"
            )
        if not meta.get("description"):
            errors.append(f"{rel}: missing frontmatter description")

        unexpected = {p.name for p in skill_dir.iterdir()} - ALLOWED_SKILL_ENTRIES
        if unexpected:
            errors.append(f"{skill_dir.relative_to(ROOT)}: unexpected entries {sorted(unexpected)}")

        refs = skill_dir / "references"
        if refs.exists():
            for p in refs.iterdir():
                if p.is_file() and p.suffix != ".md":
                    errors.append(f"{p.relative_to(ROOT)}: runtime reference must be Markdown")
                if p.name in {"sources.md", "changelog.md", "routing-tests.md", "quality-tests.md"}:
                    errors.append(f"{p.relative_to(ROOT)}: maintenance material is in references/")

    router_text = ROUTER.read_text(encoding="utf-8")
    catalog_paths = set(PATH_RE.findall(router_text))
    expected = skill_paths - {"meta/skill-router"}

    missing = sorted(expected - catalog_paths)
    stale = sorted(catalog_paths - skill_paths)
    if missing:
        errors.append(f"skill-router catalog missing: {missing}")
    if stale:
        errors.append(f"skill-router catalog references missing skills: {stale}")

    # Check explicit relative Markdown paths written in runtime skill/reference files.
    runtime_files = list(skill_files)
    runtime_files += list(SKILLS.glob("*/*/references/*.md"))
    for md in runtime_files:
        text = md.read_text(encoding="utf-8")
        for raw in MD_PATH_RE.findall(text):
            if raw.startswith("http"):
                continue
            # Plain filename mentions such as `combat-system.md` are routing labels,
            # not necessarily relative links. Only validate paths containing '/'.
            if "/" not in raw:
                continue
            target = (md.parent / raw).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{md.relative_to(ROOT)}: path escapes repository: {raw}")
                continue
            if not target.exists():
                errors.append(f"{md.relative_to(ROOT)}: broken Markdown path {raw}")

    if errors:
        print("superskills validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"superskills validation passed: {len(skill_files)} skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
