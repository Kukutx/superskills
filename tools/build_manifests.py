#!/usr/bin/env python3
"""Generate both plugin marketplace manifests from plugins/<category>/plugin.json.

.claude-plugin/marketplace.json     Claude Code
.agents/plugins/marketplace.json    Codex and ChatGPT

Each plugin.json is the only authored copy of a plugin's name, version and description.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Sequence

if __package__:
    from .layout import PLUGIN_MANIFEST, PLUGINS_DIR, categories
else:
    from layout import PLUGIN_MANIFEST, PLUGINS_DIR, categories

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
CLAUDE_MARKETPLACE = Path(".claude-plugin") / "marketplace.json"
CODEX_MARKETPLACE = Path(".agents") / "plugins" / "marketplace.json"
MARKETPLACE_NAME = "superskills"
MARKETPLACE_DESCRIPTION = (
    "Personal cross-domain Agent Skills. One plugin per category; "
    "install only the categories a project or workspace needs."
)
OWNER = {"name": "Kukutx", "url": "https://github.com/Kukutx"}
CODING_CATEGORIES = {"development", "ecommerce", "meta"}
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")


class ManifestError(ValueError):
    """Raised when plugin manifests cannot be read or generated."""


def read_plugins(root: Path) -> list[tuple[str, dict[str, str]]]:
    plugins: list[tuple[str, dict[str, str]]] = []
    for category in categories(root):
        path = root / PLUGINS_DIR / category / PLUGIN_MANIFEST
        try:
            plugins.append((category, json.loads(path.read_text(encoding="utf-8"))))
        except (OSError, json.JSONDecodeError) as error:
            raise ManifestError(f"{path.relative_to(root).as_posix()}: unreadable plugin manifest ({error})") from error
    if not plugins:
        raise ManifestError("no plugins found")
    return plugins


def render(payload: dict[str, object]) -> str:
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def expected_manifests(root: Path) -> dict[Path, str]:
    plugins = read_plugins(root)
    claude = {
        "name": MARKETPLACE_NAME,
        "owner": OWNER,
        "metadata": {"description": MARKETPLACE_DESCRIPTION},
        "plugins": [
            {
                "name": manifest["name"],
                "description": manifest["description"],
                "source": f"./{PLUGINS_DIR}/{category}",
                "strict": False,
            }
            for category, manifest in plugins
        ],
    }
    codex = {
        "name": MARKETPLACE_NAME,
        "interface": {"displayName": "Superskills"},
        "plugins": [
            {
                "name": manifest["name"],
                "source": {"source": "local", "path": f"./{PLUGINS_DIR}/{category}"},
                "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
                "category": "Coding" if category in CODING_CATEGORIES else "Productivity",
            }
            for category, manifest in plugins
        ],
    }
    return {CLAUDE_MARKETPLACE: render(claude), CODEX_MARKETPLACE: render(codex)}


def stale_manifests(root: Path) -> list[str]:
    stale: list[str] = []
    for relative, content in expected_manifests(root).items():
        path = root / relative
        if not path.is_file() or path.read_text(encoding="utf-8") != content:
            stale.append(relative.as_posix())
    return stale


def set_version(root: Path, version: str) -> None:
    if not VERSION_RE.fullmatch(version):
        raise ManifestError(f"version must be MAJOR.MINOR.PATCH, got '{version}'")
    for category, manifest in read_plugins(root):
        manifest["version"] = version
        (root / PLUGINS_DIR / category / PLUGIN_MANIFEST).write_text(render(manifest), encoding="utf-8")


def write_manifests(root: Path) -> None:
    for relative, content in expected_manifests(root).items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--version", help="Set this version on every plugin before generating.")
    parser.add_argument("--check", action="store_true", help="Fail when a generated manifest is out of date.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.root.resolve()
    try:
        if args.check:
            stale = stale_manifests(root)
            if stale:
                print(f"marketplace manifests are out of date: {stale}; run python tools/build_manifests.py", file=sys.stderr)
                return 1
            print("marketplace manifests are up to date")
            return 0
        if args.version:
            set_version(root, args.version)
        write_manifests(root)
    except ManifestError as exc:
        print(f"manifest build failed: {exc}", file=sys.stderr)
        return 1
    print(f"marketplace manifests written for {len(read_plugins(root))} plugins")
    return 0


if __name__ == "__main__":
    sys.exit(main())
