# Recommended Knowledge Files for Kukutx Superskills

GPT Knowledge has file limits, so do not upload the entire repository at first. Start with the compact pack, then add individual skills only when needed.

## Minimum setup: 1 file

Upload:

```txt
gpts/kukutx/knowledge-pack.md
```

This is the fastest setup and contains the global routing summary, including Godot 2D and spritesheet routing.

## Recommended general setup

```txt
README.md
skills/README.md
docs/personal-defaults.md
skills/meta/skill-router/skill.md
skills/meta/prompt-optimizer/skill.md
skills/meta/skill-builder/skill.md
skills/creative/image-prompt-director/skill.md
skills/design/image-review-refiner/skill.md
skills/creative/xtool-f1-engraving/skill.md
skills/product/prd-builder/skill.md
skills/development/technical-design/skill.md
skills/development/implementation-plan/skill.md
skills/development/godot-2d-game-development/skill.md
skills/development/game-dev-spritesheet-slicer/skill.md
skills/ecommerce/shopify-dev/skill.md
skills/writing/app-store-copy/skill.md
skills/design/app-store-assets/skill.md
skills/marketing/product-positioning/skill.md
```

`docs/workflow-recipes.md` is retired and should not be uploaded as active knowledge.

## Godot 2D-heavy setup

Do **not** upload every reference by default. Add the main router first:

```txt
skills/development/godot-2d-game-development/skill.md
```

Then add only the references relevant to the kind of project/work you are doing.

A useful 2D action/pixel-art subset is:

```txt
skills/development/godot-2d-game-development/references/movement-physics-camera.md
skills/development/godot-2d-game-development/references/input-controls-accessibility.md
skills/development/godot-2d-game-development/references/animation-pixel.md
skills/development/godot-2d-game-development/references/combat-system.md
skills/development/godot-2d-game-development/references/game-feel.md
skills/development/godot-2d-game-development/references/rendering-vfx-shaders.md
skills/development/godot-2d-game-development/references/ui-ux.md
skills/development/godot-2d-game-development/references/asset-pipeline.md
skills/development/godot-2d-game-development/references/runtime-agent-validation.md
```

Add AI/save/dialogue/CI references only when the project actually needs them.

Maintenance-only files such as `sources.md` and `quality-tests.md` normally do not belong in runtime GPT Knowledge.

## What not to upload initially

Avoid uploading everything at first, especially:

- Every reference file regardless of task;
- Every examples file;
- Every changelog file;
- Compatibility indexes for old prompts;
- Old drafts;
- Large exported images;
- Duplicate docs.

Add depth later only when behavior in that domain needs stronger guidance.

## Update workflow

When repository files change:

1. Update `knowledge-pack.md` if global routing/defaults changed.
2. Re-upload the changed active skill/reference file in GPT Knowledge.
3. Test with realistic conversation starters.
4. If behavior is poor, fix routing/instructions before adding more files.
5. Avoid solving weak routing by uploading the whole repository.
