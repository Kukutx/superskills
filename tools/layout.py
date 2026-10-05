"""Repository layout shared by Superskills tools.

plugins/<category>/plugin.json                 installable unit (one plugin per category)
plugins/<category>/skills/<skill>/SKILL.md     runtime entrypoint, plus one-level references/
maintenance/<category>/<skill>/                evals, sources and decisions; never shipped
"""

from __future__ import annotations

from pathlib import Path

PLUGINS_DIR = "plugins"
SKILLS_DIR = "skills"
MAINTENANCE_DIR = "maintenance"
ENTRYPOINT = "SKILL.md"
PLUGIN_MANIFEST = "plugin.json"
PLUGIN_PREFIX = "superskills-"
ROUTER_ROUTE = "meta/skill-router"


def categories(root: Path) -> list[str]:
    plugins = root / PLUGINS_DIR
    return sorted(path.name for path in plugins.iterdir() if path.is_dir()) if plugins.is_dir() else []


def skill_dir(root: Path, route: str) -> Path:
    category, name = route.split("/", 1)
    return root / PLUGINS_DIR / category / SKILLS_DIR / name


def maintenance_dir(root: Path, route: str) -> Path:
    return root / MAINTENANCE_DIR / route


def route_of(directory: Path) -> str:
    """Route of a plugins/<category>/skills/<skill> directory."""
    return f"{directory.parent.parent.name}/{directory.name}"


def skill_dirs(root: Path) -> list[Path]:
    """Every directory that really contains an exactly-named SKILL.md."""
    found = (root / PLUGINS_DIR).glob(f"*/{SKILLS_DIR}/*")
    return sorted(path for path in found if path.is_dir() and ENTRYPOINT in {entry.name for entry in path.iterdir()})
