# Kukutx Superskills Knowledge Pack

Compact catalog for routing. Detailed behavior lives in each `skill.md`.

## Runtime rules

1. Pick the most specific domain skill.
2. Load one primary skill first.
3. Load references only when that skill explicitly needs them.
4. Generic engineering skills supplement domain skills; they do not replace them.
5. Do not load maintenance/history/source files for normal execution.
6. Do not turn every request into a prompt-optimization step.
7. Prefer existing project conventions and minimal changes.
8. Validate at the level of the claim.

## Skill catalog

| Task | Primary skill |
| --- | --- |
| Improve/create a reusable prompt | `meta/prompt-optimizer` |
| Create/audit/refactor a skill | `meta/skill-builder` |
| Ambiguous skill selection | `meta/skill-router` |
| Project roadmap / task breakdown | `planning/project-planner` |
| Research / comparison / evidence brief | `research/research-brief` |
| PRD / MVP / acceptance criteria | `product/prd-builder` |
| General bug diagnosis | `development/bug-diagnosis` |
| General code/diff/PR review | `development/code-review` |
| General technical design | `development/technical-design` |
| General implementation breakdown | `development/implementation-plan` |
| Godot 4.x 2D / pixel game | `development/godot-2d-game-development` |
| Sprite strip / spritesheet geometry and packaging | `development/game-dev-spritesheet-slicer` |
| Image-generation direction / prompt | `creative/image-prompt-director` |
| xTool F1 engraving | `creative/xtool-f1-engraving` |
| App Store / Google Play visual assets | `design/app-store-assets` |
| Review/refine an image | `design/image-review-refiner` |
| Shopify implementation | `ecommerce/shopify-dev` |
| Product positioning / messaging | `marketing/product-positioning` |
| Business email | `writing/business-email` |
| App Store / Google Play copy | `writing/app-store-copy` |
| Generic release readiness | `operations/release-checklist` |
| Repeated process / SOP | `operations/sop-builder` |

## Important precedence

- Godot 2D bug/review/performance/UI/implementation -> Godot skill first.
- Shopify bug/theme/config -> Shopify skill first.
- App Store visual task -> app-store-assets; copy is a separate subtask.
- Exact spritesheet slicing/layout only -> spritesheet skill; Godot gameplay + asset work -> Godot primary, slicer secondary.
- User asks for final result directly -> execute; do not invoke prompt optimizer merely because a prompt could be written.

## Shared defaults

- Chinese for normal answers; artifact language follows audience/task.
- Concise, practical, low-filler output.
- No invented facts, capabilities, links, metrics or external rules.
- Domain/project context overrides generic preferences.
- For changing external facts or APIs, verify current information.
- For code, state modification location and validation path.
