---
name: threejs-game-development
description: Build a Three.js browser game end to end, from core loop and gameplay systems to graphics, UI, audio and release QA. Use when building a web game with Three.js, not for a Godot or native game.
---

# Three.js Game Development

Build a Three.js browser game end to end: a playable loop first, then the
visual and interface depth the request actually asked for, then browser evidence
that it works. The user's own words set the bar: "a small arcade game" is not a
request for the premium pipeline, while "premium", "AAA", "polished" or
"release-ready" is.

Adapted from `majidmanzarpour/threejs-game-skills` (MIT, 9 skills folded into
one); see `maintenance` `sources.md` for attribution and what was left out.

## Use

Use for any request to build, upgrade, polish or ship a Three.js browser game,
at any scope from a small arcade prototype to a premium release.

Not this Skill:

- a Godot game -> `development/godot-2d-game-development`,
  `development/godot-3d-game-development`, `development/godot-project-systems`;
- sprite asset production -> `development/sprite-animation-pipeline`;
- a landing or marketing page with a 3D hero -> `design/landing-page-design`;
- a diagram or data visualization in 3D -> `design/diagram-design`,
  `data/data-visualization`.

A narrow edit to a premium game remains a narrow edit; do not rebuild the game
around it.

## Workflow

1. **Design brief first**: core loop, level plan, entities, input, camera,
   physics and game feel, before any asset work. Define art direction, camera
   scale and readability targets early.
2. **Playable loop before polish**: a working loop with placeholder art beats a
   beautiful scene that cannot be played. Assess a representative playable scene
   with real assets before multiplying levels, waves or enemy variants.
3. **Systems**: gameplay, graphics, UI and audio in parallel where they do not
   share files; the lead owns shared interfaces, integration and the final
   verification pass.
4. **Verify in the browser**: production build, real-input progression and retry,
   target-viewport captures, renderer diagnostics, and the premium scorecard
   when that bar was requested. Small edits need only the affected behavior
   and layout checks.

## Gameplay systems

The core loop is the contract: what the player does every few seconds, what
progresses, and what ends the run. Build movement, physics, camera, enemy and
progression systems against that contract, not against a feature list. Combat
correctness and game feel are separate checks: a system can be correct and still
feel bad (input latency, camera framing, feedback timing). Save, inventory and
progression state must survive a reload; a game that forgets progress on refresh
has a save bug, not a feature gap.

## Graphics

Every visible surface that exists in the design is authored, not just the hero:
player, obstacles and enemies, interactables, ground and world kit, HUD and menu
states, lighting and materials, feel, and target-device performance. Unrefined
primitives, empty arenas, box skylines, generic stat-card HUDs and glow-or-fog-only
detail are prototype placeholders unless the user explicitly chose that style.
Keep a render budget (draw calls, triangles, texture memory) and measure it on
the target device; a scene that runs on a desktop GPU has not been shown to run
on a phone. Prefer procedural kits for repeated props, decals, collision proxies
and instanced volume; reserve generated assets for hero surfaces (player, boss,
signature building). Inspect generated model previews before their dependent
generation or rigging stages.

## UI

HUD, menus and overlays: responsive and touch-first, readable at the target
viewport, with every state the game can reach (pause, game over, victory,
settings, loading). A menu the player cannot navigate with touch, or a HUD that
hides the playfield on a phone, is a blocking defect. Keep UI state and game
state in one interface so the two cannot disagree.

## Audio

Event-driven audio: sound effects, music, ambience, UI sounds, and announcer
or dialogue where the game has them. Audio starts only after a user gesture
(browser autoplay policy); a game that stays silent because audio was wired to
page load has an integration bug, not a missing asset.

## Debugging and performance

When the canvas is blank, a render or runtime bug is the first suspect, not the
art: check renderer diagnostics, console errors, and whether the scene graph
actually contains the expected objects. Profile on the target device (frame
time, draw calls, memory); mobile input issues are reproduced with touch, not
with a mouse. Keep a progress log for substantial builds: intent, decisions, completed work, pending jobs, defects, next actions.

## Release QA

Before calling a game done: production build succeeds, the full loop is
playable with real input (including retry after failure), captures exist at the
target viewports, no console errors appear during a full playthrough, and the
premium scorecard (10 categories: no category below 2, average at least 2.3)
passes when the premium bar was requested. A bot playtest or scripted run is
evidence for reachability, not a substitute for a human playthrough of the core
loop.

## Constraints

- Do not announce a next step, offer to continue, or list unblocking decisions
  while the requested bar is unmet; take the next step instead. End the turn
  when the work is done, or when only the user can unblock it.
- Do not spend on generated assets twice: preserve completed assets and mark
  obsolete pending outputs instead of regenerating them.
- Do not claim a game is release-ready without browser evidence.
