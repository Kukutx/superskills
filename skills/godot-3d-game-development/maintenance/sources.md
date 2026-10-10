# Godot 3D maintenance sources

Maintenance-only. Do not load for normal 3D tasks.

## Policy

- The project's exact Godot version, renderer and target hardware are the implementation source of truth.
- Prefer matching official class/tutorial documentation and official demos before third-party patterns.
- Keep version-sensitive renderer, import and navigation facts out of durable runtime guidance unless they support a lasting decision rule.
- Third-party sources contribute domain decomposition and failure cases, not mandatory architecture or performance folklore.

## Source register

| Source | Canonical URL | Used for | Last reviewed |
| --- | --- | --- | --- |
| Godot documentation | https://docs.godotengine.org/ | transforms, CharacterBody3D, collision, Camera3D, import, animation, navigation and rendering behavior | 2026-09 |
| Godot demo projects | https://github.com/godotengine/godot-demo-projects | working native 3D patterns and reproducible examples | 2026-09 |
| GD-Agentic-Skills | https://github.com/thedivergentai/GD-Agentic-Skills | 3D physics/camera coverage and 2D↔3D boundary comparisons | 2026-09 |
| GodotPrompter | https://github.com/jame581/GodotPrompter | Godot subsystem decomposition and 3D routing comparisons | 2026-09 |
| awesome-gamedev-agent-skills | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | engine-neutral production and game-feel patterns where applicable | 2026-09 |

## Explicitly reject as permanent runtime truth

Do not preserve rules such as:

- fixed maximum node, light or signal counts without renderer/version/context;
- claims that one query API is universally many times faster;
- mandatory event buses, component frameworks or state-machine frameworks;
- fixed physics tick, camera distance or shadow distance as a professional default;
- renderer choice based only on desktop/mobile/web labels;
- “always use MultiMesh, LOD, GI or root motion” checklists;
- newest-version features written as if every Godot 4.x project supports them.

If a rule cannot survive a different project scale, renderer or version without material qualification, it does not belong in durable runtime guidance.

## Maintenance workflow

1. Inspect runtime references for overlap first.
2. Verify changed 3D APIs, renderer, import and navigation behavior from version-matched official sources.
3. Preserve the shared/2D/3D ownership boundary.
4. Add a reference only for a real task-dependent decision boundary.
5. Update the source register's decision use and review month when materially rechecked.
6. Update behavioral evals when routing or ownership changes.
7. Run tests, `python tools/validate_repo.py` and the behavioral eval export check.
8. Remove stale rules instead of preserving compatibility prose.

## Licensing

The Superskills 3D Skill is an independent synthesis. Do not bulk-copy upstream prose or code; verify licenses before importing code or scripts.
