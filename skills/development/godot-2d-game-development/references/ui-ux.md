# Game UI / UX Reference

Use this reference for Godot 2D HUDs, menus, overlays, responsive layout, input navigation and UI feedback.

## 1. UI architecture

Use Godot `Control` nodes for UI.

Prefer:

- anchors for screen-relative placement;
- `Container` nodes for flow/layout;
- `MarginContainer` for consistent insets;
- `Theme` / theme overrides for visual consistency;
- signals/events for UI updates;
- explicit screen/menu flow.

Avoid building normal UI with Node2D coordinates or hundreds of hardcoded pixel positions.

## 2. Layout first, decoration second

Before styling, make sure the UI works at multiple window sizes.

Recommended order:

1. establish root anchors;
2. choose container hierarchy;
3. set minimum sizes and spacing;
4. define reference/stretch behavior;
5. verify different aspect ratios;
6. then add theme, art, transitions and polish.

A beautiful 16:9-only layout that breaks elsewhere is not finished UI.

## 3. Anchors and containers

Use anchors to express **where the UI belongs** and containers to express **how children flow**.

Examples:

- health/score cluster: anchored top-left + VBox/HBox;
- currency/objectives: top-right;
- hotbar: bottom-center + HBox;
- centered pause dialog: center anchor + PanelContainer/VBox;
- inventory: responsive outer margin + grid/list container.

Do not manually position every heart, item or menu row.

## 4. Resolution and aspect ratio

Define one clear scaling policy for the project.

Check at minimum:

- project reference resolution;
- narrow window/mobile-like ratio if relevant;
- 16:9;
- ultrawide or wider desktop ratio if relevant.

Extra width/height should be handled intentionally: expand layout, preserve a content region, or letterbox according to the game design.

For pixel-art UI, verify the scaling strategy does not blur icons/textures unexpectedly.

## 5. Safe area

Critical UI must not sit under phone notches, rounded corners or TV overscan.

When targeting devices that need it, use the platform/display safe area to drive an outer margin/inset container.

Do not apply safe-area offsets independently to every control. Centralize the inset near the screen root when possible.

## 6. Keyboard and gamepad focus

Every non-trivial menu should work without a mouse.

For each screen:

- set one sensible default focused control when opened;
- ensure directional focus order is predictable;
- show a visible focus state;
- support confirm/cancel/back actions;
- restore focus sensibly when returning from a child screen;
- ensure mouse/touch use does not permanently break controller navigation.

Never open a controller-driven menu with nothing focused.

## 7. Screen flow

For multiple menus/overlays, use a clear screen-flow model instead of boolean soup.

Typical behavior:

```text
Game
  -> push Pause
      -> push Settings
      -> pop Settings
  -> pop Pause
```

Only the active/top screen should own relevant UI input.

A small explicit screen stack or state controller is often enough; do not build a framework if the game only has two simple screens.

## 8. Event-driven HUD

Gameplay owns state. HUD displays it.

Prefer:

```text
HealthComponent emits health_changed
-> HUD updates health bar
```

instead of:

```text
HUD._process()
-> read player.hp every frame
```

Common events:

```text
health_changed
ammo_changed
score_changed
currency_changed
objective_changed
cooldown_changed
boss_phase_changed
```

Do not let a health bar mutate player health.

## 9. UI feedback

UI should respond immediately but not distract from gameplay.

Useful feedback:

- button hover/focus state;
- press scale/pop;
- short panel fade/slide;
- health loss flash;
- cooldown radial/fill movement;
- damage number rise/fade;
- pickup/currency increment pop;
- confirm/cancel SFX.

Use short Tweens with clear easing. If an element can retrigger rapidly, replace/restart the old Tween instead of piling up effects.

## 10. HUD readability

Prioritize information hierarchy:

1. immediate survival/action state;
2. current objective / critical resource;
3. secondary information;
4. decorative detail.

Do not make every widget equally bright or animated.

For combat HUD:

- player HP must remain readable during VFX-heavy moments;
- boss HP should not compete with menus or damage popups;
- temporary alerts should disappear when no longer relevant;
- damage numbers should not cover enemy telegraphs.

## 11. Pixel-art UI

For pixel UI assets:

- keep icon source resolution consistent;
- use crisp sampling where appropriate;
- avoid arbitrary non-integer scaling when it visibly blurs the art;
- design borders/panels so 9-slice or equivalent scaling does not distort corners;
- validate text alongside pixel graphics; do not sacrifice legibility to mimic low resolution.

UI can be pixel-styled without forcing every font or control into unreadably tiny dimensions.

## 12. Localization readiness

Even if localization is not implemented yet:

- avoid baking normal text into button images;
- let containers expand for longer labels;
- avoid fixed-width controls sized only for one English word;
- separate displayed strings from gameplay IDs.

## 13. Accessibility basics

When relevant to the game/platform, consider:

- readable text size;
- sufficient contrast;
- reduced screen shake;
- reduced flashes;
- remappable controls;
- clear focus indicator;
- non-color-only status cues.

Do not bury core accessibility options behind visual polish.

## 14. UI QA

Verify:

- resize/aspect changes do not overlap or clip important elements;
- safe-area handling works on supported targets;
- every menu can be completed with keyboard/gamepad only;
- opening a screen gives sensible focus;
- back/cancel returns to the correct previous screen;
- HUD reacts to events without per-frame polling where avoidable;
- rapid updates do not create overlapping Tweens or stale labels;
- UI remains readable over bright/dark gameplay backgrounds;
- mouse, touch and controller states do not strand the user.

## Upstream inspiration

Condensed from `game-ui-ux` in `gamedev-skills/awesome-gamedev-agent-skills` and Godot UI/container/theming practices from `thedivergentai/GD-Agentic-Skills`. The retained core is anchors + containers, explicit scaling/safe-area policy, controller focus, screen-flow discipline and event-driven HUD updates.