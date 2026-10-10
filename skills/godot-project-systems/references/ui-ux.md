# Godot UI / UX Reference

Use for HUD, menus, overlays, `Control`/`Container`/`Theme`, responsive layout, keyboard/gamepad focus, safe area and UI feedback in either 2D or 3D projects.

## Control owns UI

Normal game UI should use a `Control` hierarchy.

Prefer anchors, Containers, MarginContainer, Theme/theme overrides, signals/events and explicit screen flow. Do not use world-space Node2D/Node3D coordinates as a substitute for screen UI layout unless the UI is intentionally world-space.

## Layout before styling

Order work roughly as:

1. root anchors;
2. container hierarchy;
3. minimum size/spacing;
4. stretch/reference policy;
5. aspect-ratio checks;
6. theme/art;
7. motion/polish.

A layout that only works at one aspect ratio is not complete when other ratios are supported.

## Anchor vs container

Anchors express where a region belongs on screen. Containers express how children are arranged.

Examples:

```text
health/status -> top-left + VBox/HBox
currency/objective -> top-right
hotbar -> bottom-center + HBox
pause -> centered PanelContainer + VBox
inventory -> outer margin + grid/list
```

Avoid manually positioning every repeated item when a Container describes the relationship.

## Scaling / aspect

Define one project-level policy for:

- base/reference resolution;
- stretch mode;
- aspect behavior;
- pixel UI sampling when relevant;
- use of extra width/height.

Test the aspect ratios and device classes the project actually supports.

## Safe area

When mobile notches, rounded corners or TV overscan matter, read the platform safe area near the screen root and keep critical UI inside it. Do not make every button maintain its own independent safe-area offset logic.

## Controller / keyboard focus

For each screen:

- opening establishes a sensible focus target;
- directional navigation is predictable;
- focused state is visible;
- confirm/cancel/back work;
- returning from a child screen restores reasonable focus;
- mouse/touch/controller switching does not strand the user.

A gamepad menu with no reachable focused control is broken UI.

## Screen flow

A simple project can use a small screen controller. Multiple overlays often benefit from explicit stack-like ownership:

```text
Game
-> push Pause
-> push Settings
-> pop Settings
-> pop Pause
```

The top relevant screen owns menu input. Avoid many overlapping booleans that can describe impossible screen states.

## Event-driven HUD

Gameplay/domain systems own truth; HUD displays it:

```text
health_changed -> update bar
ammo_changed -> update count
cooldown_changed -> update fill
objective_changed -> update text
```

Avoid polling stable domain state every frame when an event/change path already exists.

## UI feedback

Hover/focus, press feedback, short fades/slides, HP loss feedback, cooldown fill, currency increments and confirm/cancel SFX are presentation. Re-triggered Tweens should replace/restart when they own the same property rather than fight each other.

## Pixel UI

When pixel art is used, keep icon resolution/sampling intentional, protect 9-slice/stylebox corners and validate fractional scaling in motion. Text readability matters more than forcing all text into an artificially tiny pixel grid.

## Localization-ready layout

- keep normal dynamic text out of baked button images;
- allow longer translated strings;
- gameplay IDs differ from displayed labels;
- do not assume English-only fixed widths;
- provide required font/fallback coverage.

Dialogue-specific localization rules are in `dialogue-localization.md`.

## Accessibility

As required by the project, consider text size, contrast, focus indicators, remappable controls, reduced shake/flashes and non-color-only cues. Core gameplay information should not rely on one sensory channel when the target accessibility requirement says otherwise.

Input/remap/device behavior is in `input-controls-accessibility.md`.

## Validation

Test the relevant subset: supported aspect ratios, keyboard-only, gamepad-only, mouse/touch when targeted, open/close/back, focus restore, long localized strings, rapid HUD updates, pause/time-scale, bright/dark backgrounds and no stale HUD after scene reload.
