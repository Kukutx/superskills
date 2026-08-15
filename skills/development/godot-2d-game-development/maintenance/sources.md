# Godot 2D maintenance sources

Maintenance-only. Do not load for normal game tasks.

## Policy

- Project Godot version is always the implementation source of truth.
- Prefer matching Godot official docs and official demos before third-party patterns.
- External sources contribute decision rules, anti-patterns and validation patterns; do not bulk-copy them into runtime references.
- Third-party tools/addons are optional candidates, never implicit dependencies.
- Candidate names and ecosystem status live only here because they age quickly.
- Before recommending a current tool, re-verify its primary repository/docs, compatibility, license, maintenance and security posture.

## First-party priority

1. Godot documentation for the project's exact version.
2. `godotengine/godot-demo-projects` for working native patterns.
3. Godot release notes/migration docs when version behavior matters.
4. Third-party sources only when they add distinct value.

`godotengine/awesome-godot` may be used for discovery, not as proof that a candidate is current or suitable.

## Knowledge sources reviewed historically

These informed the Skill's domain decomposition or workflow design and may be re-checked during maintenance:

- GD-Agentic-Skills — focused Godot engineering references
- GodotPrompter — Godot domain decomposition/routing
- awesome-gamedev-agent-skills — engine-neutral game production patterns
- OpenAI sprite-pipeline — seed -> strip -> normalize -> preview
- Agent Sprite Forge — game-ready asset handoff
- Aseprite-oriented tooling — timing/tags/editable-source concepts

Exact upstream versions/availability are intentionally not stored in runtime knowledge.

## Optional ecosystem candidates

Candidate categories that may be researched **only when the project demonstrates a need**:

- runtime/editor automation / MCP bridge;
- behavior-tree or hierarchical state tooling;
- input remap/device helper;
- authored raster/sprite importer;
- terrain or external level-editor importer;
- inventory framework;
- dialogue/narrative framework;
- advanced camera authoring;
- automated test framework;
- project shell/template;
- export/CI action or image.

Historical examples may include repositories previously reviewed for these categories, but names are not part of runtime routing. If a user asks for a current recommendation, search current primary sources rather than relying on this snapshot.

## Candidate evaluation

Before adding a source/tool, answer:

1. What concrete project pain does it solve?
2. Does existing native/project behavior already solve it?
3. Does it support the project's exact Godot version/language?
4. Is maintenance/license/security acceptable now?
5. Does it overlap an existing addon/system?
6. Does it introduce a second source of truth?
7. What is the upgrade/removal cost?
8. Does adopting it require a new routing/behavior rule worth preserving?

If these answers are weak, do not add it to runtime guidance.

## Maintenance workflow

When updating the Godot Skill:

1. inspect current runtime references for overlap before adding a file;
2. verify version-sensitive facts from primary sources;
3. keep source/tool inventory here, not in runtime references;
4. add or adjust behavioral evals only for real decision boundaries;
5. run `python tools/validate_repo.py`;
6. remove stale references rather than preserving compatibility stubs.

## Licensing

Prefer independent synthesis and attribution. Do not copy substantial upstream text/code. Before importing code/scripts, check and comply with the upstream license.
