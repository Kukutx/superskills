# Knowledge file selection

Do not upload the whole repository by default.

## Minimum

```text
gpts/kukutx/knowledge-pack.md
```

This is enough for routing and shared defaults.

## Add a domain

Add that domain's `skill.md`. Add `references/` only for areas you actually use.

Examples:

### General software work

```text
skills/development/bug-diagnosis/skill.md
skills/development/code-review/skill.md
skills/development/technical-design/skill.md
skills/development/implementation-plan/skill.md
```

### Godot 2D action / pixel project

Start with:

```text
skills/development/godot-2d-game-development/skill.md
skills/development/game-dev-spritesheet-slicer/skill.md
```

Then add only relevant references, e.g.:

```text
.../references/movement-physics-camera.md
.../references/input-controls-accessibility.md
.../references/animation-pixel.md
.../references/combat-system.md
.../references/game-feel.md
.../references/rendering-vfx-shaders.md
.../references/ui-ux.md
.../references/asset-pipeline.md
.../references/runtime-agent-validation.md
```

AI/save/dialogue/release references should be added only when the project needs them.

### Visual / App Store work

```text
skills/creative/image-prompt-director/skill.md
skills/design/image-review-refiner/skill.md
skills/design/app-store-assets/skill.md
skills/writing/app-store-copy/skill.md
```

## Do not upload as runtime knowledge

Normally exclude:

- `maintenance/`
- repository authoring docs
- old/retired files
- duplicate examples/templates
- references unrelated to the current domain

When behavior is weak, fix routing or the selected Skill before adding more context.