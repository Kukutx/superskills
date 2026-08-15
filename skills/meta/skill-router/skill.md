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

### Godot 2D

以下任一情况优先 `development/godot-2d-game-development`：

- `project.godot`
- Godot 2D / pixel art
- CharacterBody2D / Area2D / TileMapLayer / Camera2D
- animation / combat / hitbox / game feel
- HUD/menu/gamepad UI
- AI/navigation/save/dialogue
- particles/shader/audio
- Godot performance/testing/export

进入后由它自己的 routing table 只读取当前任务需要的 1–3 个 reference。

### Spritesheet specialist

以下任务优先 `development/game-dev-spritesheet-slicer`：

- frame size / rows / columns
- action/direction strips
- spritesheet slicing
- frame timing/tags
- anchor/scale normalization
- naming/export/import contract

如果同一任务既有 Godot gameplay 又有 spritesheet：

```text
godot-2d-game-development = primary
game-dev-spritesheet-slicer = asset subtask only
```

### General engineering

- Pure bug diagnosis -> `development/bug-diagnosis`
- General code review -> `development/code-review`
- Architecture/implementation planning outside the Godot-specific domain -> `development/technical-design` / `development/implementation-plan`

不要因为是游戏项目就加载所有 game references。
不要在已经进入某个明确 reference 后反复重新路由，除非任务关注点发生变化。
