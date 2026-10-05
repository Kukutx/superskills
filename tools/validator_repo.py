"""Repository-level validation for Superskills."""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

if __package__:
    from .build_manifests import VERSION_RE, ManifestError, read_plugins, stale_manifests
    from .layout import (
        ENTRYPOINT,
        MAINTENANCE_DIR,
        PLUGIN_MANIFEST,
        PLUGIN_PREFIX,
        PLUGINS_DIR,
        ROUTER_ROUTE,
        SKILLS_DIR,
        maintenance_dir,
        route_of,
        skill_dir,
    )
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
    from build_manifests import VERSION_RE, ManifestError, read_plugins, stale_manifests
    from layout import (
        ENTRYPOINT,
        MAINTENANCE_DIR,
        PLUGIN_MANIFEST,
        PLUGIN_PREFIX,
        PLUGINS_DIR,
        ROUTER_ROUTE,
        SKILLS_DIR,
        maintenance_dir,
        route_of,
        skill_dir,
    )
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
ALLOWED_PLUGIN_ENTRIES = {PLUGIN_MANIFEST, SKILLS_DIR}
ALLOWED_SKILL_ENTRIES = {ENTRYPOINT, "references"}
ALLOWED_FRONTMATTER = {"name", "description"}
ALLOWED_MAINTENANCE_FILES = {"behavioral-evals.md", "sources.md", "decisions.md"}
MAINTENANCE_HEADINGS = ("## Source synthesis", "## Upstream inspiration")
ENTRYPOINT_ADVISORY_BYTES = 6500
REFERENCE_ADVISORY_BYTES = 8000
# Agent Skills specification limit; claude.ai uploads apply the stricter description limit.
NAME_MAX_CHARS = 64
DESCRIPTION_MAX_CHARS = 200
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
# Hosts parse frontmatter as real YAML; these make an unquoted value invalid or change its meaning.
YAML_UNSAFE_RE = re.compile(r": | #|^[\[\]{}>|*&!%@`'\"]")


@dataclass
class ValidationResult:
    errors: list[str]
    warnings: list[str]
    skill_count: int

    @property
    def ok(self) -> bool:
        return not self.errors


def _names(directory: Path) -> set[str]:
    # Real names, so a case-insensitive filesystem cannot hide skill.md behind SKILL.md.
    return {entry.name for entry in directory.iterdir()}


def _validate_plugin_tree(root: Path, errors: list[str]) -> list[Path]:
    plugins_root = root / PLUGINS_DIR
    for path in sorted(plugins_root.rglob("*")):
        if path.is_file() and path.name.lower() == ENTRYPOINT.lower():
            parts = path.relative_to(root).parts
            if len(parts) != 5 or parts[2] != SKILLS_DIR or path.name != ENTRYPOINT:
                errors.append(
                    f"{path.relative_to(root).as_posix()}: malformed Skill entrypoint; "
                    f"expected {PLUGINS_DIR}/<category>/{SKILLS_DIR}/<skill>/{ENTRYPOINT}"
                )

    valid: list[Path] = []
    for category in sorted(plugins_root.iterdir()):
        label = category.relative_to(root).as_posix()
        if not category.is_dir():
            errors.append(f"{label}: plugin entries must be directories")
            continue
        if not SLUG_RE.fullmatch(category.name):
            errors.append(f"{label}: category folders must use lowercase kebab-case")
        unexpected = _names(category) - ALLOWED_PLUGIN_ENTRIES
        if unexpected:
            errors.append(f"{label}: unexpected entries {sorted(unexpected)}")
        skills = category / SKILLS_DIR
        if not skills.is_dir():
            errors.append(f"{label}: plugin has no {SKILLS_DIR}/ directory")
            continue
        for candidate in sorted(skills.iterdir()):
            relative = candidate.relative_to(root).as_posix()
            if not candidate.is_dir():
                errors.append(f"{relative}: Skill entries must be directories")
            elif not SLUG_RE.fullmatch(candidate.name):
                errors.append(f"{relative}: Skill folders must use lowercase kebab-case")
            elif ENTRYPOINT not in _names(candidate):
                errors.append(f"{relative}: Skill directory missing {ENTRYPOINT}")
            else:
                valid.append(candidate / ENTRYPOINT)
    if not valid:
        errors.append("No valid skills found")
    return valid


def _validate_plugin_manifests(root: Path, errors: list[str]) -> None:
    try:
        plugins = read_plugins(root)
    except ManifestError as error:
        errors.append(str(error))
        return
    for category, manifest in plugins:
        label = f"{PLUGINS_DIR}/{category}/{PLUGIN_MANIFEST}"
        if manifest.get("name") != f"{PLUGIN_PREFIX}{category}":
            errors.append(f"{label}: name must be '{PLUGIN_PREFIX}{category}'")
        if not manifest.get("description"):
            errors.append(f"{label}: missing description")
        if not VERSION_RE.fullmatch(str(manifest.get("version", ""))):
            errors.append(f"{label}: version must be MAJOR.MINOR.PATCH")
    versions = sorted({str(manifest.get("version")) for _, manifest in plugins})
    if len(versions) > 1:
        errors.append(
            f"plugins must share one version, found {versions}; "
            "run python tools/build_manifests.py --version <x.y.z>"
        )
    stale = stale_manifests(root)
    if stale:
        errors.append(f"marketplace manifests are out of date: {stale}; run python tools/build_manifests.py")


def _validate_references(
    skill_file: Path,
    skill_text: str,
    root: Path,
    errors: list[str],
    warnings: list[str],
) -> list[Path]:
    references = skill_file.parent / "references"
    if references.exists() and not references.is_dir():
        errors.append(f"{references.relative_to(root).as_posix()}: references must be a directory")
        return []
    if not references.is_dir():
        return []

    files: list[Path] = []
    discoverable = reference_discovery_targets(skill_file, skill_text, root)
    for path in sorted(references.iterdir()):
        relative = path.relative_to(root).as_posix()
        if path.is_dir():
            errors.append(f"{relative}: nested reference directories are not supported")
            continue
        if path.suffix != ".md":
            errors.append(f"{relative}: runtime reference must be Markdown")
            continue
        files.append(path)
        if path.name in ALLOWED_MAINTENANCE_FILES:
            errors.append(f"{relative}: maintenance material is in references/")
        text = path.read_text(encoding="utf-8")
        for heading in MAINTENANCE_HEADINGS:
            if heading in text:
                errors.append(f"{relative}: maintenance source note '{heading}' is in runtime reference")
        if path.resolve() not in discoverable:
            errors.append(
                f"{relative}: orphan runtime reference; link it from "
                f"{skill_file.relative_to(root).as_posix()} using a Markdown link or code path"
            )
        if path.stat().st_size > REFERENCE_ADVISORY_BYTES:
            warnings.append(f"{relative}: large runtime reference; review whether it has multiple owners")
    return files


def _validate_maintenance(
    root: Path,
    skill_paths: set[str],
    skill_categories: set[str],
    references_by_route: dict[str, list[Path]],
    errors: list[str],
) -> None:
    maintenance_root = root / MAINTENANCE_DIR
    if not maintenance_root.is_dir():
        return
    for category in sorted(maintenance_root.iterdir()):
        if not category.is_dir():
            errors.append(
                f"{category.relative_to(root).as_posix()}: maintenance entries must be category directories"
            )
            continue
        for owner in sorted(category.iterdir()):
            route = f"{category.name}/{owner.name}"
            if not owner.is_dir() or route not in skill_paths:
                errors.append(f"{owner.relative_to(root).as_posix()}: maintenance has no matching Skill {route}")
                continue
            _validate_maintenance_files(root, route, skill_paths, skill_categories, references_by_route, errors)


def _validate_maintenance_files(
    root: Path,
    route: str,
    skill_paths: set[str],
    skill_categories: set[str],
    references_by_route: dict[str, list[Path]],
    errors: list[str],
) -> None:
    maintenance = maintenance_dir(root, route)
    for path in sorted(maintenance.iterdir()):
        relative = path.relative_to(root).as_posix()
        if path.is_dir():
            errors.append(f"{relative}: nested maintenance directories are not supported")
        elif path.name not in ALLOWED_MAINTENANCE_FILES:
            errors.append(
                f"{relative}: unsupported maintenance file; allowed: {sorted(ALLOWED_MAINTENANCE_FILES)}"
            )

    eval_file = maintenance / "behavioral-evals.md"
    if not eval_file.is_file():
        return
    label = eval_file.relative_to(root).as_posix()
    text = eval_file.read_text(encoding="utf-8")
    valid_local_md = {ENTRYPOINT, *(path.name for path in references_by_route.get(route, []))}
    valid_local_md.update(path.name for path in maintenance.glob("*.md"))
    for raw in CODE_SPAN_RE.findall(strip_html_comments(text)):
        target = normalize_markdown_target(raw)
        if target and "/" not in target and target not in valid_local_md:
            errors.append(f"{label}: behavioral eval references missing local file {target}")

    cases = routing_cases_from_text(text)
    if not cases:
        errors.append(
            f"{label}: behavioral eval must contain a canonical "
            "ID | Prompt | Primary | Secondary | Must avoid table"
        )
        return

    for case in cases:
        if not case.case_id:
            errors.append(f"{label}:{case.line}: routing case has an empty ID")
        if not case.prompt:
            errors.append(f"{label}:{case.line}: routing case has an empty prompt")
        if not case.primary:
            errors.append(f"{label}:{case.line}: routing case has an empty primary route")
        for cell in (case.primary, case.secondary, case.must_avoid):
            for found in ROUTE_FIND_RE.findall(cell):
                if found.split("/", 1)[0] in skill_categories and found not in skill_paths:
                    errors.append(f"{label}:{case.line}: references missing local Skill {found}")


def _validate_runtime_links(files: list[Path], root: Path, errors: list[str]) -> None:
    root_resolved = root.resolve()
    for markdown_file in files:
        text = markdown_file.read_text(encoding="utf-8")
        relative = markdown_file.relative_to(root).as_posix()
        include_bare_code = markdown_file.parent.name == "references"
        for raw in markdown_targets(text, include_bare_code=include_bare_code):
            target = resolve_markdown_path(root, markdown_file, raw)
            try:
                inside = target.relative_to(root_resolved)
            except ValueError:
                errors.append(f"{relative}: path escapes repository: {raw}")
                continue
            if inside.parts[:1] == (MAINTENANCE_DIR,):
                errors.append(f"{relative}: runtime file links to maintenance material: {raw}")
            elif not target.exists():
                errors.append(f"{relative}: broken Markdown path {raw}")


def validate_repository(root: Path | str = DEFAULT_ROOT) -> ValidationResult:
    root = Path(root).resolve()
    errors: list[str] = []
    warnings: list[str] = []
    if not (root / PLUGINS_DIR).is_dir():
        return ValidationResult([f"{PLUGINS_DIR}/ directory does not exist"], [], 0)

    skill_files = _validate_plugin_tree(root, errors)
    _validate_plugin_manifests(root, errors)
    skill_paths = {route_of(path.parent) for path in skill_files}
    skill_categories = {route.split("/", 1)[0] for route in skill_paths}
    skill_names: dict[str, list[str]] = defaultdict(list)
    references_by_route: dict[str, list[Path]] = {}

    for skill_file in skill_files:
        relative = skill_file.relative_to(root).as_posix()
        text = skill_file.read_text(encoding="utf-8")
        metadata, metadata_errors = frontmatter(text)
        errors.extend(f"{relative}: {error}" for error in metadata_errors)
        unknown = sorted(set(metadata) - ALLOWED_FRONTMATTER)
        if unknown:
            errors.append(f"{relative}: frontmatter only allows name and description, found {unknown}")
        name = metadata.get("name")
        if not name:
            errors.append(f"{relative}: missing frontmatter name")
        else:
            skill_names[name].append(relative)
            if name != skill_file.parent.name:
                errors.append(f"{relative}: frontmatter name '{name}' != folder '{skill_file.parent.name}'")
            if len(name) > NAME_MAX_CHARS:
                errors.append(f"{relative}: frontmatter name exceeds {NAME_MAX_CHARS} characters")
        description = metadata.get("description")
        if not description:
            errors.append(f"{relative}: missing frontmatter description")
        elif len(description) > DESCRIPTION_MAX_CHARS:
            errors.append(
                f"{relative}: frontmatter description is {len(description)} characters; "
                f"the limit is {DESCRIPTION_MAX_CHARS}"
            )
        elif YAML_UNSAFE_RE.search(description):
            errors.append(
                f"{relative}: frontmatter description must be a plain YAML scalar "
                "(no ': ', ' #' or leading quote/bracket)"
            )

        unexpected = _names(skill_file.parent) - ALLOWED_SKILL_ENTRIES
        if unexpected:
            errors.append(
                f"{skill_file.parent.relative_to(root).as_posix()}: unexpected entries {sorted(unexpected)}"
            )
        if len(text.encode("utf-8")) > ENTRYPOINT_ADVISORY_BYTES:
            warnings.append(
                f"{relative}: large entrypoint; review whether it contains multiple owners or task-dependent detail"
            )
        references_by_route[route_of(skill_file.parent)] = _validate_references(
            skill_file, text, root, errors, warnings
        )

    # Hosts register every Skill under its bare name, so names must be unique across plugins.
    for name, paths in sorted(skill_names.items()):
        if len(paths) > 1:
            errors.append(f"duplicate frontmatter skill name '{name}': {paths}")

    _validate_maintenance(root, skill_paths, skill_categories, references_by_route, errors)

    router = skill_dir(root, ROUTER_ROUTE) / ENTRYPOINT
    if not router.is_file():
        errors.append(f"{router.relative_to(root).as_posix()}: missing authoritative Router")
    else:
        catalog_routes, catalog_errors = extract_catalog_routes(router.read_text(encoding="utf-8"))
        errors.extend(catalog_errors)
        counts = Counter(catalog_routes)
        duplicates = sorted(route for route, count in counts.items() if count > 1)
        if duplicates:
            errors.append(f"skill-router Catalog duplicates: {duplicates}")
        expected = skill_paths - {ROUTER_ROUTE}
        catalog = set(catalog_routes)
        missing = sorted(expected - catalog)
        stale = sorted(catalog - expected)
        if missing:
            errors.append(f"skill-router Catalog missing: {missing}")
        if stale:
            errors.append(f"skill-router Catalog references missing or self routes: {stale}")

    reference_files = [path for files in references_by_route.values() for path in files]
    _validate_runtime_links(skill_files + reference_files, root, errors)
    return ValidationResult(errors, warnings, len(skill_files))
