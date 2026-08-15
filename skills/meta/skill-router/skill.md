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

Choose one primary Skill first. Add a secondary Skill only for a genuinely distinct subtask.

## Catalog

| Intent | Skill |
| --- | --- |
| prompt/template itself | `meta/prompt-optimizer` |
| create/audit/simplify a skill | `meta/skill-builder` |
| cross-workstream project roadmap | `planning/project-planner` |
| external evidence / current factual comparison | `research/research-brief` |
| PRD/MVP/product behavior | `product/prd-builder` |
| general observed software bug | `development/bug-diagnosis` |
| general code/diff/PR review | `development/code-review` |
| unresolved software architecture/interfaces | `development/technical-design` |
| decided software direction -> file/task breakdown | `development/implementation-plan` |
| Godot dimension-neutral project systems | `development/godot-project-systems` |
| Godot 2D / pixel runtime | `development/godot-2d-game-development` |
| Godot 3D / spatial runtime | `development/godot-3d-game-development` |
| sprite animation generation/slicing/packaging | `development/sprite-animation-pipeline` |
| explicit divination / astrology / fortune-telling reading | `personal/divination-reading` |
| evidence-led birth-cohort / historical life context | `personal/generational-context-analysis` |
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

### Planner vs technical design vs implementation plan

```text
broad goal + several workstreams + sequencing
-> project-planner

software ownership/data/interface/architecture still undecided
-> technical-design

behavior + architecture already decided, need files/tasks/tests
-> implementation-plan
```

Do not load all three for a normal software task.

### Research vs internal decision

Use `research-brief` when the answer materially depends on external evidence, current facts, source quality or uncertainty.

If the real question is architecture/ownership inside an already-known project, `technical-design` remains primary even when alternatives are compared.

### Divination vs generational context

A birth date is not itself a routing signal. Route by epistemic intent:

```text
八字 / 紫微 / 六爻 / 奇门 / Tarot / Jyotiṣa / astrology / symbolic fortune reading
-> personal/divination-reading

historical events / economy / technology / cohort psychology / evidence-led life context
-> personal/generational-context-analysis
```

Do not mix them unless explicitly requested. Symbolic interpretation is not empirical evidence; cohort analysis must not infer individual personality from date alone.

### Bug diagnosis vs code review

```text
observed failure: "why is this broken?"
-> bug-diagnosis

inspect code/diff for defects/risks
-> code-review
```

### Positioning vs store copy/assets

```text
audience/value/differentiation unresolved
-> product-positioning

words are the main deliverable
-> app-store-copy

visual sequence/composition is the main deliverable
-> app-store-assets
```

### Godot project systems vs 2D vs 3D

Route by what actually changes implementation, not by the project's dimensional label alone:

```text
scene/data ownership, Resources/signals/autoloads,
InputMap/remapping, Control UI, audio,
save/inventory/dialogue, verification, export/CI
-> godot-project-systems

CharacterBody2D / Camera2D / TileMapLayer /
2D animation-combat-VFX-navigation
-> godot-2d-game-development

Node3D / CharacterBody3D / Camera3D /
3D collision-rendering-import-navigation
-> godot-3d-game-development
```

For a mixed task, choose the owner of the primary behavior and add one neighboring Godot Skill only for the distinct subproblem. Do not recreate shared project-system knowledge inside both dimensional Skills.

### Domain runtime vs asset production

```text
Godot gameplay/runtime integration
-> matching Godot owner

sprite frames/strips/geometry/slicing/packing
-> sprite-animation-pipeline
```

Use both only when the task genuinely spans runtime integration and sprite asset production.

## Precedence examples

- “1990 年出生，按八字看事业” -> divination-reading.
- “1990 年出生，结合中国经济和互联网发展分析职业环境” -> generational-context-analysis unless symbolic analysis is requested.
- “出生日期相同的人是否都有焦虑型依恋？” -> generational-context-analysis should reject unsupported individual inference.
- Godot 2D movement/combat/camera bug -> Godot 2D Skill before generic development methods.
- Godot 3D camera/physics/import bug -> Godot 3D Skill before generic development methods.
- Godot 2D/3D pause menu, remapping, save migration or clean export -> Godot project-systems first.
- Shopify theme/store issue -> Shopify Skill before generic frontend/debugging.
- Godot 2D gameplay + new attack strip -> Godot 2D primary; sprite pipeline owns the asset subtask.
- New sprite strip without engine work -> sprite pipeline only.
- App Store screenshot artwork + short captions -> app-store-assets primary; app-store-copy only for substantial wording work.
- Existing App Store screenshot critique -> app-store-assets primary; image-review-refiner only if its visual-review method adds value.
- “Compare current maintenance/security of three libraries” -> research-brief.
- “Which component owns this state?” -> technical-design.
- “Architecture is approved; tell me which files/tasks to change” -> implementation-plan.
- “Plan the whole app from validation through launch” -> project-planner.
- User asks “do X” -> execute X; do not route through prompt-optimizer unless the prompt itself is requested.

## Restraint

- Do not load every Skill whose keywords appear in the prompt.
- Do not announce a long routing analysis before doing the task.
- Stay with the focused owner unless the actual task changes.
- If no Skill adds meaningful value, answer directly rather than forcing a route.
