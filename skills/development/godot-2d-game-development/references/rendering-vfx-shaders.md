# Rendering, VFX and Shaders Reference

用于 CanvasItem shaders、particles、2D lights、post effects、trails、outlines、hit flash、dissolve 与 visual readability。

## 1. VFX serves readability

先问效果表达什么：

- hit；
- damage type；
- charge；
- danger；
- invulnerability；
- interactable；
- selection；
- movement speed；
- status effect。

没有 gameplay/visual purpose 的效果不要因为“酷”就堆。

## 2. Layer order

明确：

```text
background
world
actors
actor-local FX
foreground
screen-space FX
HUD
menus
```

Damage flash/weapon trail 不应盖住关键 telegraph。
Screen-space effect 不应让 HUD 失读。

## 3. Particles

选择 GPU/CPU 以项目实际目标和 profile 为准。

常用 2D particle：

- dust；
- impact sparks；
- smoke；
- magic burst；
- debris；
- ambient motes；
- trails。

关键参数：

- amount；
- lifetime；
- explosiveness；
- direction/spread；
- velocity；
- gravity；
- scale/color curve；
- one-shot；
- visibility bounds。

短特效必须自己结束/回收。

## 4. Burst vs continuous

Impact 通常是 burst/one-shot。
环境雾尘/火焰可 continuous。

不要用 continuous emitter 模拟每次 hit，造成不可控 overdraw。

## 5. CanvasItem shader

适合：

- hit flash；
- outline；
- palette swap；
- dissolve；
- ghost/invuln tint；
- water/fire distortion；
- UI highlight；
- transition。

Gameplay 只驱动少量参数：

```text
flash_amount
dissolve
outline_width
tint
```

不要把 combat rules 写进 shader。

## 6. Material sharing

Godot Resource 可能被共享。

如果每个 enemy 的 flash/dissolve 要独立：

- 确认 material 是否 local/duplicated；
- 或用适合实例级参数的方式。

避免一个敌人受击导致全部同材质敌人一起闪。

## 7. Pixel-art shader rules

谨慎使用：

- blur；
- fractional scaling；
- smooth UV distortion；
- glow；
- texture filtering。

可用但必须检查实际像素风是否被破坏。

常见 pixel-friendly：

- palette swap；
- hard-threshold flash；
- small hard-edged outline sized to the project's pixel scale；
- dither dissolve；
- indexed-color-like ramps。

## 8. 2D lighting

使用 PointLight2D/相关 2D lighting 时先确认：

- game art 是否真的依赖 dynamic light；
- normal maps 是否存在；
- shadow cost；
- light layers/masks；
- mobile/web budget；
- pixel art 是否视觉一致。

不要为了“高级”把原本清楚的 pixel art 全部压暗再靠灯照亮。

## 9. Trails

武器/dash/projectile trail 需要：

- clear start/end；
- short lifetime；
- direction readable；
- 不覆盖 hitbox truth；
- action stop 时正确清理。

Trail 是 presentation，不决定 weapon reach。

## 10. Screen-space effects

适合：

- scene transition；
- damage vignette；
- pause dim；
- short boss impact；
- CRT/palette stylization。

避免长时间高强度 chromatic aberration/shake/flash 影响舒适度。

## 11. Overdraw

2D 常见性能问题来自大透明 quad 与粒子叠层。

Profile 前先观察：

- full-screen transparent FX；
- huge empty sprite bounds；
- many additive particles；
- multiple screen-reading shaders；
- giant offscreen textures。

不要只盯 node count。

## 12. VFX event contract

推荐统一事件接口思想：

```text
event name
world position
direction
intensity tier
optional element/type
```

Presentation layer 决定具体 FX bundle。

不要把每种 attack 都硬编码到 Camera/Particles singleton。

## 13. Validation

- hit/FX spawn 在正确位置；
- material instance 不串值；
- repeated hits 能 cleanly restart；
- effect returns/frees；
- silhouette/telegraph 仍可见；
- pixel art 不 blur/shimmer；
- low-end target 上无明显 overdraw spike；
- reduced flashing/shake option 不破坏 gameplay info。
