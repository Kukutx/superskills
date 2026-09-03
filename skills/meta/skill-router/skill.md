---
name: skill-router
description: Select the smallest useful Superskills route when task ownership is ambiguous. Prefer a specific domain owner over generic methods and avoid keyword-based Skill stacking.
---

# Skill Router

## Rule

```text
specific domain Skill
> generic method Skill
> meta helper
```

Choose one primary Skill. Add a secondary Skill only for a separable subtask with a different owner. If no Skill changes the answer, work directly instead of forcing a route.

## Catalog

| Intent | Skill |
| --- | --- |
| prompt or reusable AI instruction is the deliverable | `meta/prompt-optimizer` |
| create, audit, simplify or restructure a Skill | `meta/skill-builder` |
| broad roadmap across multiple workstreams | `planning/project-planner` |
| find or rank web resources, media, examples, pages or accounts | `research/web-discovery` |
| establish current facts or compare external evidence | `research/research-brief` |
| PRD, MVP scope or product behavior | `product/prd-builder` |
| diagnose an observed software failure | `development/bug-diagnosis` |
| review code, a diff or pull request for concrete risks | `development/code-review` |
| decide unresolved software architecture, ownership or interfaces | `development/technical-design` |
| turn decided architecture into file-level tasks and tests | `development/implementation-plan` |
| Godot dimension-neutral project systems | `development/godot-project-systems` |
| Godot 2D or pixel runtime behavior | `development/godot-2d-game-development` |
| Godot 3D or spatial runtime behavior | `development/godot-3d-game-development` |
| generate, slice or package sprite animation assets | `development/sprite-animation-pipeline` |
| explicit divination, astrology or symbolic fortune reading | `personal/divination-reading` |
| evidence-led birth-cohort or historical life context | `personal/generational-context-analysis` |
| non-diagnostic reflection on personal thoughts and behavior | `personal/psychology-reflection` |
| direct image-generation direction or prompt | `creative/image-prompt-director` |
| xTool F1 engraving-ready design and production guidance | `creative/xtool-f1-engraving` |
| App Store or Play Store visual assets | `design/app-store-assets` |
| review and refine an existing image | `design/image-review-refiner` |
| Shopify implementation, Liquid, theme or store integration | `ecommerce/shopify-dev` |
| audience, value proposition and product messaging | `marketing/product-positioning` |
| professional business email | `writing/business-email` |
| App Store or Play Store listing copy | `writing/app-store-copy` |
| create, tailor, rewrite or audit a resume/CV | `writing/resume-writing` |
| generic release readiness and go/no-go gate | `operations/release-checklist` |
| repeated process or SOP | `operations/sop-builder` |

## Important boundaries

### Project planning vs software design vs implementation

```text
several workstreams + sequencing -> project-planner
architecture/data/interface still undecided -> technical-design
direction fixed + need files/tasks/tests -> implementation-plan
```

Do not load all three for a normal software task.

### Web discovery vs evidence research

```text
find/shortlist/rank actual resources -> web-discovery
decide what is true or current -> research-brief
```

A discovery task may verify one material fact without becoming a full research brief. Use both only when evidence synthesis is a distinct deliverable.

### Bug diagnosis vs code review

```text
observed failure and root cause -> bug-diagnosis
inspect visible code/change for defects -> code-review
```

A failing runtime path needs reproduction evidence, not a generic review checklist.

### Godot shared vs dimensional owners

```text
input, Control UI, audio, save, inventory, dialogue, verification, export -> project-systems
CharacterBody2D, Camera2D, TileMapLayer, 2D combat/VFX/navigation -> Godot 2D
Transform3D, CharacterBody3D, Camera3D, 3D rendering/import/navigation -> Godot 3D
```

Route by what changes implementation, not by the project's dimensional label alone.

### Asset production vs runtime integration

```text
sprite frames/strip geometry/slicing/packing -> sprite-animation-pipeline
Godot gameplay and runtime animation behavior -> matching Godot owner
```

Use both only when the task genuinely spans both outputs.

### Personal-analysis boundaries

Keep symbolic divination, historical cohort evidence and observed psychology patterns separate. Do not use one lens as proof for another, and do not force diagnosis or treatment questions into ordinary reflection.

### Resume vs adjacent job tasks

Resume facts, structure, bullets and role tailoring belong to resume-writing. Job discovery is a research/discovery task; application or outreach email belongs to business-email. Do not invent experience or metrics to make a resume sound stronger.

## Restraint

- Route by the requested deliverable and decision owner, not isolated keywords.
- Preserve the user's explicit scope and ranking criteria.
- Do not run prompt optimization when the user requested the final task result.
- Do not preload every neighboring Skill or reference.
- Keep maintenance files out of normal runtime context.
