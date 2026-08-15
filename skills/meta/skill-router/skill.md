---
name: skill-router
description: Select the smallest useful Superskills route when task ownership is ambiguous. Prefer specific domain skills over generic methods and avoid loading skills by keyword alone.
---

# Skill Router

## Rule

```text
specific domain skill
> generic method skill
> meta helper
```

Choose one primary skill first. Add a secondary skill only when it contributes a distinct subtask.

## Catalog

| Intent | Skill |
| --- | --- |
| prompt/template itself | `meta/prompt-optimizer` |
| create/audit a skill | `meta/skill-builder` |
| project roadmap | `planning/project-planner` |
| research/comparison | `research/research-brief` |
| PRD/MVP | `product/prd-builder` |
| general bug | `development/bug-diagnosis` |
| general code/diff review | `development/code-review` |
| general technical design | `development/technical-design` |
| general implementation plan | `development/implementation-plan` |
| Godot 2D / pixel game | `development/godot-2d-game-development` |
| spritesheet/animation-strip production | `development/game-dev-spritesheet-slicer` |
| image-generation direction/prompt | `creative/image-prompt-director` |
| xTool F1 | `creative/xtool-f1-engraving` |
| App Store / Play visuals | `design/app-store-assets` |
| image refinement | `design/image-review-refiner` |
| Shopify | `ecommerce/shopify-dev` |
| positioning/messaging | `marketing/product-positioning` |
| business email | `writing/business-email` |
| App Store / Play copy | `writing/app-store-copy` |
| generic release readiness | `operations/release-checklist` |
| SOP/repeated process | `operations/sop-builder` |

## Precedence examples

- Godot UI bug -> Godot skill, not generic bug + generic design.
- Shopify theme bug -> Shopify skill; use bug-diagnosis only if general debugging methodology is additionally useful.
- Godot gameplay + spritesheet -> Godot primary, slicer only for the asset subtask.
- App Store screenshot artwork + copy -> app-store-assets primary, app-store-copy secondary.
- User asks “do X” -> execute X; do not route through prompt-optimizer unless they asked for a prompt.

## Restraint

- Do not load every skill whose keywords appear in the prompt.
- Do not announce a long routing analysis before doing the task.
- Once a focused domain/reference is selected, stay there unless the actual task changes.
- If no Skill adds meaningful value, answer directly rather than forcing a route.