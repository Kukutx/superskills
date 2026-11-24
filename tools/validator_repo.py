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
        EVAL_GRADERS,
        EVAL_PROMPT,
        EVALS_DIR,
        MAINTENANCE_DIR,
        PLUGIN_MANIFEST,
        PLUGIN_PREFIX,
        PLUGINS_DIR,
        ROUTER_ROUTE,
        SKILLS_DIR,
        authored_eval_dirs,
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
        EVAL_GRADERS,
        EVAL_PROMPT,
        EVALS_DIR,
        MAINTENANCE_DIR,
        PLUGIN_MANIFEST,
        PLUGIN_PREFIX,
        PLUGINS_DIR,
        ROUTER_ROUTE,
        SKILLS_DIR,
        authored_eval_dirs,
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
ALLOWED_SKILL_ENTRIES = {ENTRYPOINT, "references", "skill.yaml"}
ALLOWED_FRONTMATTER = {"name", "description"}
ALLOWED_MAINTENANCE_FILES = {"behavioral-evals.md", "sources.md", "decisions.md"}
MAINTENANCE_HEADINGS = ("## Source synthesis", "## Upstream inspiration")
ENTRYPOINT_ADVISORY_BYTES = 6500
REFERENCE_ADVISORY_BYTES = 8000
# Agent Skills specification (https://agentskills.io/specification) limits; claude.ai uploads
# apply the stricter description limit.
NAME_MAX_CHARS = 64
RESERVED_NAME_WORDS = ("anthropic", "claude")
DESCRIPTION_MAX_CHARS = 200
ENTRYPOINT_ADVISORY_LINES = 500
XML_TAG_RE = re.compile(r"<[A-Za-z/][^>]*>")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
# Hosts parse frontmatter as real YAML; these make an unquoted value invalid or change its meaning.
YAML_UNSAFE_RE = re.compile(r": | #|^[\[\]{}>|*&!%@`'\"]")
# The Skill a `tool_used: Skill` grader matches is the last name in its input_match pattern.
GRADER_SKILL_RE = re.compile(r"([a-z0-9]+(?:-[a-z0-9]+)*)\"'?$")


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


def _parse_skill_yaml(text: str) -> tuple[dict[str, object], list[str]]:
    """Parse the small YAML subset the skill.yaml generator writes.

    Uses PyYAML when installed; otherwise a minimal parser for flat
    ``key: value`` lines and ``key:`` followed by ``- item`` lines.
    """
    try:
        import yaml  # type: ignore[import-not-found]

        data = yaml.safe_load(text)
    except ImportError:
        data, errors = {}, []
        current: str | None = None
        for raw in text.splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("- ") and current:
                value = data.setdefault(current, [])
                if isinstance(value, list):
                    value.append(line[2:].strip())
                continue
            if ":" not in line:
                errors.append(f"skill.yaml line is not key: value: {raw!r}")
                continue
            key, value = (part.strip() for part in line.split(":", 1))
            if value:
                data[key] = value
            else:
                data[key] = []
                current = key
        return data, errors
    except Exception as error:  # yaml.YAMLError and friends
        return {}, [f"skill.yaml is not valid YAML ({error})"]
    if not isinstance(data, dict):
        return {}, ["skill.yaml must be a mapping"]
    return data, []


def _validate_skill_yaml(
    skill_file: Path,
    name: str | None,
    description: str | None,
    root: Path,
    errors: list[str],
) -> None:
    """skill.yaml is generated from SKILL.md; it must exist and agree with it."""
    skill_yaml = skill_file.parent / "skill.yaml"
    relative = skill_yaml.relative_to(root).as_posix()
    if not skill_yaml.is_file():
        errors.append(
            f"{relative}: missing skill.yaml; run python tools/generate_skill_yaml.py"
        )
        return
    data, parse_errors = _parse_skill_yaml(skill_yaml.read_text(encoding="utf-8"))
    errors.extend(f"{relative}: {error}" for error in parse_errors)
    if parse_errors:
        return
    category = skill_file.parent.parent.parent.name
    if data.get("name") != name:
        errors.append(f"{relative}: name '{data.get('name')}' != SKILL.md name '{name}'")
    if data.get("description") != description:
        errors.append(f"{relative}: description drifted from SKILL.md; regenerate it")
    if data.get("category") != category:
        errors.append(f"{relative}: category '{data.get('category')}' != plugin '{category}'")
    if data.get("include_in_prompt") is not False:
        errors.append(f"{relative}: include_in_prompt must be false")
    triggers = data.get("triggers")
    if not isinstance(triggers, list) or not triggers or not all(
        isinstance(trigger, str) and trigger.strip() for trigger in triggers
    ):
        errors.append(f"{relative}: triggers must be a non-empty list of phrases")


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
            if path.name != EVALS_DIR:
                errors.append(
                    f"{relative}: nested maintenance directories are not supported except {EVALS_DIR}/"
                )
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


def _validate_authored_evals(root: Path, skill_names: set[str], errors: list[str]) -> list[str]:
    """Check each maintenance/<category>/<skill>/evals/<case>/ against the `claude plugin eval` case shape."""
    case_ids: list[str] = []
    for case in authored_eval_dirs(root):
        label = case.relative_to(root).as_posix()
        case_ids.append(case.name)
        if not SLUG_RE.fullmatch(case.name):
            errors.append(f"{label}: eval case folders must use lowercase kebab-case")
        unexpected = _names(case) - {EVAL_PROMPT, EVAL_GRADERS}
        if unexpected:
            errors.append(
                f"{label}: unexpected entries {sorted(unexpected)}; allowed: {EVAL_PROMPT}, {EVAL_GRADERS}/"
            )
        prompt = case / EVAL_PROMPT
        if not prompt.is_file():
            errors.append(f"{label}: eval case is missing {EVAL_PROMPT}")
        else:
            text = prompt.read_text(encoding="utf-8")
            _, prompt_errors = frontmatter(text)
            errors.extend(f"{label}/{EVAL_PROMPT}: {error}" for error in prompt_errors)
            if not prompt_errors and not text.split("\n---\n", 1)[1].strip():
                errors.append(f"{label}/{EVAL_PROMPT}: the prompt body is empty")
        graders = case / EVAL_GRADERS
        files = sorted(graders.iterdir()) if graders.is_dir() else []
        if not files:
            errors.append(f"{label}: eval case needs at least one grader in {EVAL_GRADERS}/")
        for grader in files:
            grader_label = grader.relative_to(root).as_posix()
            if grader.is_dir() or grader.suffix != ".md":
                errors.append(f"{grader_label}: a grader must be a Markdown file")
                continue
            metadata, grader_errors = frontmatter(grader.read_text(encoding="utf-8"))
            errors.extend(f"{grader_label}: {error}" for error in grader_errors)
            if not grader_errors and not metadata.get("type"):
                errors.append(f"{grader_label}: grader frontmatter needs a type")
            if metadata.get("tool") == "Skill":
                match = GRADER_SKILL_RE.search(metadata.get("input_match", ""))
                if not match or match.group(1) not in skill_names:
                    errors.append(f"{grader_label}: input_match does not name an existing Skill")
    return case_ids


def _validate_eval_ids(root: Path, authored_ids: list[str], errors: list[str]) -> None:
    """Authored and table cases share one ID space, because both become dist/live-evals/evals/<id>."""
    table_ids = {
        case.case_id
        for path in sorted((root / MAINTENANCE_DIR).glob("*/*/behavioral-evals.md"))
        for case in routing_cases_from_text(path.read_text(encoding="utf-8"))
        if case.case_id
    }
    duplicates = sorted(case_id for case_id, count in Counter(authored_ids).items() if count > 1)
    if duplicates:
        errors.append(f"duplicate authored eval case IDs: {duplicates}")
    clashes = sorted(set(authored_ids) & table_ids)
    if clashes:
        errors.append(f"authored eval case IDs also used by behavioral eval tables: {clashes}")


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
            if any(word in name.split("-") for word in RESERVED_NAME_WORDS):
                errors.append(f"{relative}: frontmatter name uses a reserved word {RESERVED_NAME_WORDS}")
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
        elif XML_TAG_RE.search(description):
            errors.append(f"{relative}: frontmatter description must not contain XML tags")

        unexpected = _names(skill_file.parent) - ALLOWED_SKILL_ENTRIES
        if unexpected:
            errors.append(
                f"{skill_file.parent.relative_to(root).as_posix()}: unexpected entries {sorted(unexpected)}"
            )
        _validate_skill_yaml(skill_file, name, description, root, errors)
        if text.count("\n") > ENTRYPOINT_ADVISORY_LINES:
            warnings.append(
                f"{relative}: entrypoint exceeds {ENTRYPOINT_ADVISORY_LINES} lines; "
                "move task-dependent depth into references/"
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
    authored_ids = _validate_authored_evals(root, {route.split("/", 1)[1] for route in skill_paths}, errors)
    _validate_eval_ids(root, authored_ids, errors)

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
