# Recommended Knowledge Files for Kukutx Superskills

GPT Knowledge has file limits, so do not upload the entire repository at first. Start with the compact pack, then add individual skills only when needed.

## Minimum setup: 1 file

Upload:

```txt
gpts/kukutx/knowledge-pack.md
```

This is the fastest setup and should be enough for routing and common workflows.

## Recommended setup: 10 files

Upload these files to the Private GPT or `kukutx` Project:

```txt
README.md
skills/README.md
docs/personal-defaults.md
docs/western-market-guidelines.md
docs/workflow-recipes.md
skills/meta/skill-router/skill.md
skills/meta/prompt-optimizer/skill.md
skills/meta/skill-builder/skill.md
skills/creative/image-prompt-director/skill.md
skills/design/image-review-refiner/skill.md
```

## Full practical setup: up to 20 files

Add these high-frequency skill files:

```txt
skills/creative/xtool-f1-engraving/skill.md
skills/creative/ip-safe-creative-adapter/skill.md
skills/product/prd-builder/skill.md
skills/development/technical-design/skill.md
skills/development/implementation-plan/skill.md
skills/development/code-review/skill.md
skills/development/bug-diagnosis/skill.md
skills/ecommerce/shopify-dev/skill.md
skills/writing/app-store-copy/skill.md
skills/design/app-store-assets/skill.md
```

## What not to upload initially

Avoid uploading everything at first, especially:

- Every examples file
- Every changelog file
- Old drafts
- Large exported images
- Duplicate docs

Add examples later only when the GPT needs stronger behavior in a specific domain.

## Update workflow

When repository files change:

1. Update `knowledge-pack.md` if global routing/defaults changed.
2. Re-upload the changed file in GPT Knowledge.
3. Test with conversation starters.
4. If behavior is poor, fix instructions before adding more files.
