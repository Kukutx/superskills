"""Markdown/frontmatter parsing shared by Superskills repository tools."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

ROOT_PREFIXES = ("docs/", "gpts/", "skills/", "templates/", "tools/", "tests/", ".github/")
ROUTE_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*/[a-z0-9]+(?:-[a-z0-9]+)*$")
ROUTE_FIND_RE = re.compile(
    r"(?<![a-z0-9-])([a-z0-9]+(?:-[a-z0-9]+)*/[a-z0-9]+(?:-[a-z0-9]+)*)(?![a-z0-9-])"
)
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
CODE_SPAN_RE = re.compile(r"`([^`\n]+)`")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
TABLE_SEPARATOR_CELL_RE = re.compile(r"^:?-{3,}:?$")
CANONICAL_ROUTING_HEADERS = ("id", "prompt", "primary", "secondary", "must avoid")


@dataclass(frozen=True)
class MarkdownTable:
    headers: tuple[str, ...]
    rows: tuple[tuple[str, ...], ...]
    start_line: int


@dataclass(frozen=True)
class RoutingCase:
    prompt: str
    primary: str
    secondary: str
    must_avoid: str
    case_id: str
    line: int


def strip_html_comments(text: str) -> str:
    return HTML_COMMENT_RE.sub("", text)


def frontmatter(text: str) -> tuple[dict[str, str], list[str]]:
    """Parse the intentionally small frontmatter subset used by this repository."""
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, ["missing opening frontmatter delimiter"]
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, ["missing closing frontmatter delimiter"]

    data: dict[str, str] = {}
    for line_number, raw in enumerate(text[4:end].splitlines(), start=2):
        line = raw.strip()
        if not line:
            continue
        if ":" not in line:
            errors.append(f"frontmatter line {line_number} is not key: value")
            continue
        key, value = (part.strip() for part in line.split(":", 1))
        if not key:
            errors.append(f"frontmatter line {line_number} has an empty key")
            continue
        if key in data:
            errors.append(f"duplicate frontmatter key '{key}'")
        data[key] = value
    return data, errors


def split_table_row(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped.startswith("|"):
        return []
    stripped = stripped[1:-1] if stripped.endswith("|") else stripped[1:]

    cells: list[str] = []
    current: list[str] = []
    escaped = False
    for char in stripped:
        if escaped:
            current.append(char)
            escaped = False
        elif char == "\\":
            current.append(char)
            escaped = True
        elif char == "|":
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(char)
    cells.append("".join(current).strip())
    return cells


def normalize_header(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().lower().replace("`", ""))


def parse_markdown_tables(text: str) -> list[MarkdownTable]:
    lines = text.splitlines()
    tables: list[MarkdownTable] = []
    index = 0
    while index + 1 < len(lines):
        headers = split_table_row(lines[index])
        separator = split_table_row(lines[index + 1])
        separator_ok = separator and all(
            TABLE_SEPARATOR_CELL_RE.fullmatch(cell.replace(" ", "")) for cell in separator
        )
        if not headers or len(headers) != len(separator) or not separator_ok:
            index += 1
            continue

        rows: list[tuple[str, ...]] = []
        row_index = index + 2
        while row_index < len(lines):
            cells = split_table_row(lines[row_index])
            if not cells:
                break
            cells = (cells + [""] * len(headers))[: len(headers)]
            rows.append(tuple(cells))
            row_index += 1
        tables.append(
            MarkdownTable(
                headers=tuple(normalize_header(cell) for cell in headers),
                rows=tuple(rows),
                start_line=index + 1,
            )
        )
        index = max(row_index, index + 2)
    return tables


def _plain_cell(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"`", '"', "'", "“", "”"}:
        value = value[1:-1].strip()
    return value.replace("`", "").strip()


def routing_cases_from_text(text: str) -> list[RoutingCase]:
    cases: list[RoutingCase] = []
    for table in parse_markdown_tables(strip_html_comments(text)):
        if table.headers != CANONICAL_ROUTING_HEADERS:
            continue
        for row_offset, row in enumerate(table.rows, start=2):
            cases.append(
                RoutingCase(
                    prompt=_plain_cell(row[1]),
                    primary=_plain_cell(row[2]),
                    secondary=_plain_cell(row[3]),
                    must_avoid=_plain_cell(row[4]),
                    case_id=_plain_cell(row[0]),
                    line=table.start_line + row_offset,
                )
            )
    return cases


def extract_catalog_routes(router_text: str) -> tuple[list[str], list[str]]:
    """Read routes only from the first Skill table under the Router Catalog section."""
    section = re.search(
        r"(?ms)^## Catalog\s*$\n(.*?)(?=^##\s|\Z)", strip_html_comments(router_text)
    )
    if not section:
        return [], ["skill-router: missing '## Catalog' section"]
    table = next((table for table in parse_markdown_tables(section.group(1)) if "skill" in table.headers), None)
    if table is None:
        return [], ["skill-router: Catalog section has no table with a Skill column"]

    errors: list[str] = []
    routes: list[str] = []
    skill_index = table.headers.index("skill")
    for row_number, row in enumerate(table.rows, start=table.start_line + 2):
        matches = ROUTE_FIND_RE.findall(row[skill_index])
        if len(matches) != 1:
            errors.append(
                f"skill-router Catalog row {row_number}: expected exactly one category/skill route, "
                f"found {matches or 'none'}"
            )
        elif ROUTE_RE.fullmatch(matches[0]):
            routes.append(matches[0])
        else:
            errors.append(f"skill-router Catalog row {row_number}: invalid route '{matches[0]}'")
    return routes, errors


def normalize_markdown_target(raw: str) -> str | None:
    target = raw.strip()
    if not target:
        return None
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    if " " in target and not target.startswith(("http://", "https://")):
        target = target.split(None, 1)[0]
    if target.lower().startswith(("http://", "https://", "mailto:", "tel:")):
        return None
    target = target.split("#", 1)[0].split("?", 1)[0]
    return target if target.endswith(".md") else None


def markdown_targets(text: str, *, include_bare_code: bool) -> list[str]:
    clean = strip_html_comments(text)
    targets = [
        target
        for match in MARKDOWN_LINK_RE.finditer(clean)
        if (target := normalize_markdown_target(match.group(1)))
    ]
    for match in CODE_SPAN_RE.finditer(clean):
        target = normalize_markdown_target(match.group(1))
        if target and (include_bare_code or "/" in target or target.startswith(".")):
            targets.append(target)
    return targets


def resolve_markdown_path(root: Path, markdown_file: Path, raw: str) -> Path:
    normalized = raw[2:] if raw.startswith("./") else raw
    if normalized.startswith(ROOT_PREFIXES):
        return (root / normalized).resolve()
    return (markdown_file.parent / raw).resolve()


def reference_discovery_targets(skill_file: Path, text: str, root: Path) -> set[Path]:
    targets: set[Path] = set()
    for raw in markdown_targets(text, include_bare_code=True):
        if "/" not in raw and not raw.startswith("."):
            targets.add((skill_file.parent / "references" / raw).resolve())
        else:
            targets.add(resolve_markdown_path(root, skill_file, raw))
    return targets
