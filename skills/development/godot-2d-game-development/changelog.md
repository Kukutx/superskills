# Godot 2D Game Development Changelog

## v0.4 — 2026-08-15

- Added explicit scope boundaries so 3D, networking architecture and unrelated engineering do not get pulled into the 2D skill.
- Added routing precedence: correctness -> input/interaction -> presentation -> feel -> performance -> release.
- Clarified that one primary reference should be loaded first; secondary references are added only when needed.
- Clarified AnimationTree + AnimationPlayer ownership and animation/combat synchronization.
- Simplified runtime validation so tool-specific MCP details live only in `companion-tools.md`.
- Tightened addon/tool evaluation around version compatibility, maintenance, license, overlap, source-of-truth and removal cost.
- Added source-review metadata and verified upstream maintenance snapshot.
- Added distribution-level routing to Kukutx `project-instructions.md`, `knowledge-pack.md`, `knowledge-files.md` and `skill-router`.
- Added integration/precedence regression cases to `quality-tests.md`.

### Why

v0.3 already had enough domain coverage. The main remaining risk was not missing knowledge, but routing ambiguity, duplicated maintenance and incomplete integration into the Kukutx knowledge-distribution layer.

## v0.3 — 2026-08-15

- Split broad references into focused domains: movement/physics/camera, input/accessibility, combat correctness, game feel, save/inventory, dialogue/localization, runtime validation and release/CI.
- Added stronger addon-selection boundaries and production-oriented companion-tool guidance.
- Added authored-vs-generated pixel asset pipelines.
- Added routing pressure tests and external source tracking.

## v0.2 — 2026-08-15

- Expanded from a small Godot 2D guide into a progressive-disclosure router with focused references.
- Added AI/navigation, save/data/dialogue, audio, world/TileMap, performance/testing and companion tools.
- Strengthened runtime verification and dependency restraint.

## v0.1 — 2026-08-15

- Initial Godot 2D SuperSkill.
- Covered Godot 2D fundamentals, pixel animation, combat/game feel, UI/UX and asset production.
