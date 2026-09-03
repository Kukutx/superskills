# Godot 2D maintenance sources

Maintenance-only. Do not load for normal game tasks.

## Policy

- The project's exact Godot version is the implementation source of truth.
- Prefer matching official documentation and official demos before third-party patterns.
- External sources may contribute decision boundaries, failure cases and validation ideas; do not bulk-copy them into runtime guidance.
- Third-party tools and Skills are optional research inputs, never implicit dependencies.
- Re-verify current compatibility, maintenance, license and security before recommending any ecosystem tool.

## Source register

| Source | Canonical URL | Used for | Last reviewed |
| --- | --- | --- | --- |
| Godot documentation | https://docs.godotengine.org/ | version-matched engine behavior, APIs, import, navigation, rendering and migration | 2026-09 |
| Godot demo projects | https://github.com/godotengine/godot-demo-projects | working native patterns and reproducible examples | 2026-09 |
| awesome-godot | https://github.com/godotengine/awesome-godot | ecosystem discovery only; not proof of suitability | 2026-09 |
| GD-Agentic-Skills | https://github.com/thedivergentai/GD-Agentic-Skills | Godot domain decomposition and engineering failure cases | 2026-09 |
| GodotPrompter | https://github.com/jame581/GodotPrompter | subsystem decomposition and routing comparisons | 2026-09 |
| awesome-gamedev-agent-skills | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | engine-neutral production and game-feel patterns | 2026-09 |
| Agent Sprite Forge | https://github.com/0x0funky/agent-sprite-forge | sprite source-to-package handoff and asset workflow comparisons | 2026-09 |

Only sources with a confirmed canonical location remain in this register. A remembered project name without a resolvable source is not durable provenance.

## Candidate evaluation

Before adopting or recommending a tool, answer:

1. What concrete project pain does it solve?
2. Does the existing project or native Godot capability already solve it?
3. Does it support the project's exact Godot version and language?
4. Is its current maintenance, license and security posture acceptable?
5. Does it overlap an existing addon or source of truth?
6. What are the upgrade and removal costs?
7. Does it create a durable decision rule worth preserving?

Weak answers mean the candidate stays out of runtime guidance.

## Maintenance workflow

1. Inspect current runtime references for overlap before adding content.
2. Verify version-sensitive facts from primary sources.
3. Keep source/tool inventories here, not in runtime references.
4. Update the source register's decision use and review month when materially rechecked.
5. Add or adjust behavioral evals only for real routing/ownership boundaries.
6. Run tests, `python tools/validate_repo.py` and the behavioral eval export check.
7. Remove stale rules instead of keeping compatibility stubs.

## Licensing

Prefer independent synthesis and attribution. Do not copy substantial upstream prose or code. Check the upstream license before importing any code or scripts.
