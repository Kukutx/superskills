# 2D Asset Pipeline Reference

用于生成、清理、组织和导入 2D game assets：sprites、animation strips、FX、tiles、maps、props、UI art。

## 1. Production asset contract

不是“好看就行”。Game-ready asset 需要：

- exact/known dimensions；
- alpha/background policy；
- scale；
- anchor/pivot；
- naming；
- timing metadata if animated；
- deterministic export；
- engine import settings；
- in-engine QA。

## 2. Separate asset roles

先定义类型：

```text
character sprite
animation strip
enemy/boss
weapon
projectile
impact FX
spell/trail
tileset
map base
transparent prop
UI icon/panel
portrait
```

Concept sheet != spritesheet。
Decorative map image != editable gameplay map。

## 3. Character pipeline

推荐：

```text
approved seed frame
-> lock silhouette/palette/proportions/outfit/weapon
-> define action + direction
-> generate whole action strip
-> deterministic cleanup
-> split
-> shared scale/anchor normalize
-> preview
-> approve
-> engine import
```

不要默认逐帧独立生成。

详细 layout/slicing 转 `game-dev-spritesheet-slicer`。

## 4. One action per generation unit

比起一次生成巨大：

```text
idle + run + 5 attacks + hurt + death × 8 directions
```

更稳妥的是按 action/direction strip 分批，并以同一个 approved seed/reference 约束 identity。

最后再 deterministic pack 成 atlas/sheet。

## 5. Character FX separation

大型 slash/projectile/impact effect 最好与 body sprite 分离，特别是：

- effect range exceeds body canvas；
- effect needs independent timing/scale/color；
- projectile persists after pose；
- same attack reuses different FX variant。

Character animation 保持 body readability，external FX 由 gameplay event/timeline spawn。

## 6. FX bundle

例如 fire ability：

```text
cast pose/hand FX
projectile
impact
optional residue/smoke
HUD icon if needed
```

Bundle 共享 palette/shape language，但每个 runtime asset 有明确 origin/anchor。

## 7. Pixel-art constraints

- crisp pixel clusters；
- consistent source resolution；
- readable silhouette；
- palette consistent with project；
- no accidental antialias blur；
- clean alpha；
- actual game-size review；
- do not mix pseudo-high-res AI illustration with low-res sprite language。

## 8. Tileset pipeline

定义：

- tile size；
- atlas grid；
- terrain edge/corner；
- variants；
- animation；
- collision/navigation policy；
- padding/spacing；
- light direction/palette。

必须在真实 tile combinations 测，不只看 showcase atlas。

## 9. Editable map handoff

分离：

```text
ground/base
repeatable tiles
props
foreground
collision
navigation
spawn
triggers
exits
```

Godot 可用 TileMapLayer + Sprite2D/scenes + StaticBody2D + Area2D + markers。

不要把 enemy/collision/exit 烤进唯一背景图。

## 10. Props

- transparent PNG；
- consistent ground anchor；
- scale consistent；
- optional separated shadow；
- collision simpler than artwork when appropriate；
- padding enough but not huge empty texture。

Top-down y-sort 以 ground contact anchor 为准。

## 11. UI art

Separate：

- icons；
- panels/frames；
- buttons/states；
- badges；
- cursor/focus；
- resource symbols。

动态文本/数值不要烤进图。
Pixel panels 设计可 stretch/9-slice 区域。

## 12. Deterministic cleanup

能脚本处理的几何问题不要继续 prompt 猜：

- chroma/background remove；
- crop/pad；
- resize when appropriate；
- shared scale normalize；
- anchor align；
- strip split；
- atlas compose；
- alpha inspect；
- preview GIF/sheet；
- naming/batch export。

## 13. Source vs derived

区分：

```text
approved source/reference
raw generation
normalized production frames
preview/GIF
engine-ready file
```

不要拿 processed derivative 覆盖唯一 approved source。

## 14. Godot handoff

确认：

- filter/mipmap；
- repeat for tiles；
- SpriteFrames/action names；
- frame timing；
- pivot/anchor；
- material/shader；
- scene references production file；
- collision/gameplay metadata remains editable。

## 15. Asset QA

- matches existing art direction；
- silhouette readable；
- scale/anchor stable；
- alpha clean；
- identity stable through animation；
- tile combinations connect；
- prop y-sort correct；
- FX does not cover telegraph；
- naming predictable；
- correct in engine, not just image viewer。

## Source synthesis

主要吸收 Agent Sprite Forge、OpenAI sprite-pipeline、Aseprite-oriented pixel workflows 与本仓库 spritesheet slicer。核心：creative generation + deterministic normalization + in-engine validation。
