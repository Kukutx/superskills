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
| create/audit/simplify a skill | `meta/skill-builder` |
| cross-workstream project roadmap | `planning/project-planner` |
| research/comparison/current evidence | `research/research-brief` |
| PRD/MVP/product behavior | `product/prd-builder` |
| general observed software bug | `development/bug-diagnosis` |
| general code/diff/PR review | `development/code-review` |
| unresolved software architecture/interfaces | `development/technical-design` |
| decided software direction -> file/task breakdown | `development/implementation-plan` |
| Godot 2D / pixel game | `development/godot-2d-game-development` |
| spritesheet/animation-strip generation or packaging | `development/game-dev-spritesheet-slicer` |
| image-generation direction/prompt | `creative/image-prompt-director` |
| xTool F1 | `creative/xtool-f1-engraving` |
| App Store / Play visuals | `design/app-store-assets` |
| existing image refinement | `design/image-review-refiner` |
| Shopify | `ecommerce/shopify-dev` |
| positioning/messaging | `marketing/product-positioning` |
| business email | `writing/business-email` |
| App Store / Play copy | `writing/app-store-copy` |
| generic release readiness | `operations/release-checklist` |
| SOP/repeated process | `operations/sop-builder` |

## Important boundaries

### Project planner vs technical design vs implementation plan

```text
broad goal + several workstreams + sequencing
-> project-planner

software ownership/data/interface/architecture still undecided
-> technical-design

behavior + architecture already decided, need files/tasks/tests
-> implementation-plan
```

Do not load all three for a normal software task.

### Bug diagnosis vs code review

```text
observed failure: "why is this broken?"
-> bug-diagnosis

inspect code/diff for defects/risks
-> code-review
```

A bug may later need code review, but review is not a substitute for reproduction/diagnosis.

## Precedence examples

- Godot UI bug -> Godot skill, not generic bug + generic design.
- Shopify theme bug -> Shopify skill; generic bug-diagnosis only if its debugging method adds distinct value.
- Godot gameplay + spritesheet -> Godot primary, slicer only for the asset subtask.
- App Store screenshot artwork + copy -> app-store-assets primary, app-store-copy secondary.
- “Design the data model/API ownership” -> technical-design.
- “Architecture is approved; tell me exactly which files/tasks to change” -> implementation-plan.
- “Plan the whole app from validation through launch” -> project-planner.
- User asks “do X” -> execute X; do not route through prompt-optimizer unless they asked for a prompt.

## Restraint

- Do not load every skill whose keywords appear in the prompt.
- Do not announce a long routing analysis before doing the task.
- Once a focused domain/reference is selected, stay there unless the actual task changes.
- If no Skill adds meaningful value, answer directly rather than forcing a route.
