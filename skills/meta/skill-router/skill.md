# Skill Router Skill

Routes tasks to the best available skill.

## Routing principle

Choose the **most specific domain skill first**. Generic engineering skills supplement a domain skill only when needed.

Do not load multiple skills merely because several keywords match.

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

即使用户说的是“debug”“review”“优化”“实现”，只要核心问题是 Godot 2D，仍先进入 Godot domain skill。

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

只有没有更具体 domain skill 时，才优先使用：

- Pure/general bug diagnosis -> `development/bug-diagnosis`
- General code review -> `development/code-review`
- General architecture -> `development/technical-design`
- General implementation planning -> `development/implementation-plan`

在 Godot 2D 任务中，这些可以作为补充方法论，但不要替代 Godot-specific routing。

## Routing restraint

- 不因为是游戏项目就加载所有 game references。
- 不因为一句话同时出现 `attack + animation + VFX` 就自动加载三套；先判断真正的问题是 correctness、timing 还是 feel。
- 不在已经进入明确 reference 后反复重新路由，除非任务关注点发生变化。
- 如果用户只需要直接执行，完成路由后直接做，不先输出长篇“我选择了哪些 skill”的说明。
