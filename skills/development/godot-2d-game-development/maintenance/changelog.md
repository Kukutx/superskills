# Godot 2D SuperSkill history

## v0.6 — 2026-08-15

Second noise-reduction pass:

- removed the static third-party tool catalog from runtime references;
- split overlapping performance/runtime-validation guidance into focused `performance.md` and `verification-testing.md`;
- removed export concerns from performance guidance;
- generalized addon/tool selection so current candidates are re-verified instead of stored in runtime knowledge;
- compressed AI/input/world/save/dialogue/asset references by removing tool-specific catalogs and source-synthesis boilerplate;
- updated routing regression tests to the new reference names and single-catalog architecture;
- kept source/tool history under `maintenance/` only.

## v0.5 — 2026-08-15

- trimmed the main file to routing + cross-domain invariants;
- kept detailed domain knowledge in focused runtime references;
- removed legacy compatibility reference stubs;
- moved sources and routing tests to `maintenance/`;
- aligned with the repository's minimal-file Skill architecture.

## v0.4 — 2026-08-15

- added explicit scope boundary and routing precedence;
- separated combat correctness from game feel and input from movement;
- strengthened runtime evidence and addon restraint.

## v0.3 — 2026-08-15

- split broad Godot guidance into focused domain references;
- added authored-vs-generated asset pipelines, runtime validation and release/CI guidance.

## v0.2 — 2026-08-15

- expanded into a progressive-disclosure Godot 2D router.

## v0.1 — 2026-08-15

- initial Godot 2D skill.
