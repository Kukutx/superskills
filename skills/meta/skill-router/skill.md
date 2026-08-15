# Skill Router Skill

Routes tasks to the best available skill.

## Skills

- `meta/prompt-optimizer`
- `meta/skill-builder`
- `product/prd-builder`
- `development/technical-design`
- `development/implementation-plan`
- `development/code-review`
- `development/bug-diagnosis`
- `development/game-dev-spritesheet-slicer`
- `development/godot-2d-game-development`
- `creative/image-prompt-director`
- `creative/xtool-f1-engraving`
- `design/image-review-refiner`
- `design/app-store-assets`
- `writing/app-store-copy`
- `ecommerce/shopify-dev`
- `marketing/product-positioning`
- `operations/release-checklist`
- `operations/sop-builder`

## Game development routing

- Godot 2D、pixel art、角色动画、UI、战斗、打击感、Camera2D、particles、2D shader、audio feedback：优先 `development/godot-2d-game-development`。
- 只需要角色 spritesheet 规划、frame layout、切图、命名或导入前检查：优先 `development/game-dev-spritesheet-slicer`。
- 一个 Godot 2D 任务同时包含代码和 spritesheet 时，以 `godot-2d-game-development` 为主，只在资产规格/切图阶段读取 `game-dev-spritesheet-slicer`。
- 不要因为是游戏项目就自动加载所有 game references；按任务只加载必要部分。
