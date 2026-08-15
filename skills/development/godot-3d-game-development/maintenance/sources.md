# Godot 3D maintenance sources

Maintenance-only. Do not load for normal 3D tasks.

## Source policy

- The project's exact Godot version and renderer are the implementation source of truth.
- Prefer matching official Godot class/tutorial documentation and official demos before third-party patterns.
- Keep version-sensitive renderer/import/navigation facts out of runtime guidance unless they change a durable decision; re-verify them when exact behavior matters.
- Third-party sources contribute useful domain decomposition and failure cases, not mandatory architecture or performance folklore.

## First-party areas reviewed

Official Godot documentation used to establish the runtime boundaries includes:

- `CharacterBody3D` and 3D transforms;
- 3D collision shapes and physics-body constraints;
- Camera3D / SpringArm3D;
- 3D scene import and supported formats;
- AnimationTree/root motion;
- NavigationAgent3D and 3D navigation;
- renderers, StandardMaterial3D, lights/environment/GI;
- 3D performance, mesh LOD and related visibility tools.

## Upstream skill sources reviewed

Secondary sources inspected for coverage and routing ideas:

- `thedivergentai/GD-Agentic-Skills` — dedicated 3D physics, camera, 2D↔3D adaptation and genre coverage;
- `jame581/GodotPrompter` — 3D essentials, Camera3D and Godot subsystem decomposition;
- `gamedev-skills/awesome-gamedev-agent-skills` — engine-neutral game-production and game-feel patterns where applicable.

The Superskills 3D Skill is an independent synthesis; do not bulk-copy upstream prose/code.

## Explicitly reject as permanent runtime truth

Do not import rules such as:

- fixed maximum node/light/signal counts without the exact renderer/version/context;
- claims that one query API is universally "100x faster";
- mandatory global event buses/component frameworks/state-machine frameworks;
- fixed physics tick, coyote time, camera distance or shadow distance as a professional default;
- renderer choice based only on "desktop/mobile/web" labels without the actual target/capabilities;
- "always use MultiMesh/LOD/GI/root motion" checklists;
- latest-version features stored as if all Godot 4.x projects support them.

If a rule cannot survive a different project scale/renderer/version without qualification, keep it out of durable runtime guidance.

## Maintenance workflow

When updating this Skill:

1. inspect current runtime references for overlap first;
2. verify changed 3D APIs/renderer/import behavior from official docs for the relevant version;
3. preserve the 2D/3D ownership boundary rather than merging them for convenience;
4. add a reference only for a real task-dependent decision boundary;
5. update `behavioral-evals.md` when routing/ownership changes;
6. run `python tools/validate_repo.py`;
7. remove stale rules instead of preserving compatibility prose.
