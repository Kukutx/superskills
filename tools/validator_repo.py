"""Repository-level validation for Superskills."""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

if __package__:
    from .validator_markdown import (
        CODE_SPAN_RE,
        ROUTE_FIND_RE,
        extract_catalog_routes,
        frontmatter,
        markdown_targets,
        normalize_markdown_target,
        reference_discovery_targets,
        resolve_markdown_path,
        routing_cases_from_text,
        strip_html_comments,
    )
else:
    from validator_markdown import (
        CODE_SPAN_RE,
        ROUTE_FIND_RE,
        extract_catalog_routes,
        frontmatter,
        markdown_targets,
        normalize_markdown_target,
        reference_discovery_targets,
        resolve_markdown_path,
        routing_cases_from_text,
        strip_html_comments,
    )

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
ALLOWED_SKILL_ENTRIES = {"skill.md", "references", "maintenance"}
MAINTENANCE_HEADINGS = ("## Source synthesis", "## Upstream inspiration")
MAINTENANCE_ONLY_REFERENCE_NAMES = {
    "sources.md",
    "behavioral-evals.md",
    "routing-tests.md",
    "quality-tests.md",
    "changelog.md",
    "decisions.md",
}
LEGACY_MAINTENANCE_NAMES = {"routing-tests.md", "changelog.md"}
ENTRYPOINT_ADVISORY_BYTES = 6500
REFERENCE_ADVISORY_BYTES = 8000
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


@dataclass
class ValidationResult:
    errors: list[str]
    warnings: list[str]
    skill_count: int

    @property
    def ok(self) -> bool:
        return not self.errors


def _validate_skill_tree(skills_root: Path, root: Path, errors: list[str]) -> list[Path]:
    for category in sorted(skills_root.iterdir()):
        if not category.is_dir():
            errors.append(f"skills/{category.name}: category entries must be directories")
            continue
        if not SLUG_RE.fullmatch(category.name):
            errors.append(f"skills/{category.name}: invalid category slug")
        for candidate in sorted(category.iterdir()):
            if not candidate.is_dir():
                errors.append(f"{candidate.relative_to(root)}: Skill entries must be directories")
            elif not (candidate / "skill.md").is_file():
                errors.append(f"{candidate.relative_to(root)}: Skill directory missing skill.md")

    valid: list[Path] = []
    for path in sorted(skills_root.rglob("skill.md")):
        relative = path.relative_to(root)
        parts = relative.parts
        if len(parts) != 4 or parts[0] != "skills" or parts[-1] != "skill.md":
            errors.append(
                f"{relative}: malformed Skill entrypoint; expected skills/<category>/<skill>/skill.md"
            )
        elif not SLUG_RE.fullmatch(parts[1]) or not SLUG_RE.fullmatch(parts[2]):
            errors.append(f"{relative}: category and Skill folders must use lowercase kebab-case")
        else:
            valid.append(path)
    if not valid:
        errors.append("No valid skills found")
    return valid


def _validate_references(
    skill_file: Path,
    skill_text: str,
    root: Path,
    errors: list[str],
    warnings: list[str],
) -> list[Path]:
    references = skill_file.parent / "references"
    if references.exists() and not references.is_dir():
        errors.append(f"{references.relative_to(root)}: references must be a directory")
        return []
    if not references.is_dir():
        return []

    files: list[Path] = []
    discoverable = reference_discovery_targets(skill_file, skill_text, root)
    for path in sorted(references.iterdir()):
        relative = path.relative_to(root)
        if path.is_dir():
            errors.append(f"{relative}: nested reference directories are not supported")
            continue
        if path.suffix != ".md":
            errors.append(f"{relative}: runtime reference must be Markdown")
            continue
        files.append(path)
        if path.name in MAINTENANCE_ONLY_REFERENCE_NAMES:
            errors.append(f"{relative}: maintenance material is in references/")
        text = path.read_text(encoding="utf-8")
        for heading in MAINTENANCE_HEADINGS:
            if heading in text:
                errors.append(f"{relative}: maintenance source note '{heading}' is in runtime reference")
        if path.resolve() not in discoverable:
            errors.append(
                f"{relative}: orphan runtime reference; link it from {skill_file.relative_to(root)} "
                "using a Markdown link or code path"
            )
        if path.stat().st_size > REFERENCE_ADVISORY_BYTES:
            warnings.append(f"{relative}: large runtime reference; review whether it has multiple owners")
    return files


def _validate_maintenance(
    skill_file: Path,
    references: list[Path],
    skill_paths: set[str],
    skill_categories: set[str],
    root: Path,
    errors: list[str],
) -> None:
    maintenance = skill_file.parent / "maintenance"
    if maintenance.exists() and not maintenance.is_dir():
        errors.append(f"{maintenance.relative_to(root)}: maintenance must be a directory")
        return
    if not maintenance.is_dir():
        return

    for path in sorted(maintenance.iterdir()):
        relative = path.relative_to(root)
        if path.is_dir():
            errors.append(f"{relative}: nested maintenance directories are not supported")
        elif path.suffix != ".md":
            errors.append(f"{relative}: maintenance files must be Markdown")
        elif path.name in LEGACY_MAINTENANCE_NAMES:
            errors.append(f"{relative}: legacy maintenance filename; use behavioral-evals.md or Git history")

    eval_file = maintenance / "behavioral-evals.md"
    if not eval_file.is_file():
        return
    text = eval_file.read_text(encoding="utf-8")
    valid_local_md = {"skill.md", *(path.name for path in references)}
    valid_local_md.update(path.name for path in maintenance.glob("*.md"))
    for raw in CODE_SPAN_RE.findall(strip_html_comments(text)):
        target = normalize_markdown_target(raw)
        if target and "/" not in target and target not in valid_local_md:
            errors.append(f"{eval_file.relative_to(root)}: behavioral eval references missing local file {target}")

    for case in routing_cases_from_text(text):
        if not case.prompt:
            errors.append(f"{eval_file.relative_to(root)}:{case.line}: routing case has an empty prompt")
        if not case.primary:
            errors.append(f"{eval_file.relative_to(root)}:{case.line}: routing case has an empty primary route")
        for cell in (case.primary, case.secondary, case.must_avoid):
            for route in ROUTE_FIND_RE.findall(cell):
                if route.split("/", 1)[0] in skill_categories and route not in skill_paths:
                    errors.append(
                        f"{eval_file.relative_to(root)}:{case.line}: references missing local Skill {route}"
                    )


def _validate_runtime_links(
    files: list[Path], root: Path, errors: list[str]
) -> None:
    root_resolved = root.resolve()
    for markdown_file in files:
        text = markdown_file.read_text(encoding="utf-8")
        include_bare_code = markdown_file.parent.name == "references"
        for raw in markdown_targets(text, include_bare_code=include_bare_code):
            target = resolve_markdown_path(root, markdown_file, raw)
            try:
                target.relative_to(root_resolved)
            except ValueError:
                errors.append(f"{markdown_file.relative_to(root)}: path escapes repository: {raw}")
                continue
            if not target.exists():
                errors.append(f"{markdown_file.relative_to(root)}: broken Markdown path {raw}")


def validate_repository(root: Path | str = DEFAULT_ROOT) -> ValidationResult:
    root = Path(root).resolve()
    skills_root = root / "skills"
    errors: list[str] = []
    warnings: list[str] = []
    if not skills_root.is_dir():
        return ValidationResult(["skills/ directory does not exist"], [], 0)

    skill_files = _validate_skill_tree(skills_root, root, errors)
    skill_paths = {f"{path.parent.parent.name}/{path.parent.name}" for path in skill_files}
    skill_categories = {route.split("/", 1)[0] for route in skill_paths}
    skill_names: dict[str, list[str]] = defaultdict(list)
    reference_files: list[Path] = []

    for skill_file in skill_files:
        relative = skill_file.relative_to(root)
        text = skill_file.read_text(encoding="utf-8")
        metadata, metadata_errors = frontmatter(text)
        errors.extend(f"{relative}: {error}" for error in metadata_errors)
        name = metadata.get("name")
        if not name:
            errors.append(f"{relative}: missing frontmatter name")
        else:
            skill_names[name].append(str(relative))
            if name != skill_file.parent.name:
                errors.append(f"{relative}: frontmatter name '{name}' != folder '{skill_file.parent.name}'")
        if not metadata.get("description"):
            errors.append(f"{relative}: missing frontmatter description")

        unexpected = {path.name for path in skill_file.parent.iterdir()} - ALLOWED_SKILL_ENTRIES
        if unexpected:
            errors.append(f"{skill_file.parent.relative_to(root)}: unexpected entries {sorted(unexpected)}")
        if len(text.encode("utf-8")) > ENTRYPOINT_ADVISORY_BYTES:
            warnings.append(
                f"{relative}: large entrypoint; review whether it contains multiple owners or task-dependent detail"
            )

        references = _validate_references(skill_file, text, root, errors, warnings)
        reference_files.extend(references)
        _validate_maintenance(
            skill_file, references, skill_paths, skill_categories, root, errors
        )

    for name, paths in sorted(skill_names.items()):
        if len(paths) > 1:
            errors.append(f"duplicate frontmatter skill name '{name}': {paths}")

    router = skills_root / "meta" / "skill-router" / "skill.md"
    if not router.is_file():
        errors.append("skills/meta/skill-router/skill.md: missing authoritative Router")
    else:
        catalog_routes, catalog_errors = extract_catalog_routes(router.read_text(encoding="utf-8"))
        errors.extend(catalog_errors)
        counts = Counter(catalog_routes)
        duplicates = sorted(route for route, count in counts.items() if count > 1)
        if duplicates:
            errors.append(f"skill-router Catalog duplicates: {duplicates}")
        expected = skill_paths - {"meta/skill-router"}
        catalog = set(catalog_routes)
        missing = sorted(expected - catalog)
        stale = sorted(catalog - expected)
        if missing:
            errors.append(f"skill-router Catalog missing: {missing}")
        if stale:
            errors.append(f"skill-router Catalog references missing or self routes: {stale}")

    _validate_runtime_links(skill_files + reference_files, root, errors)
    return ValidationResult(errors, warnings, len(skill_files))
