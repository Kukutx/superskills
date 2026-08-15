---
name: godot-2d-game-development
description: Godot 4.x 2D game-development router and execution guide. Use for 2D/pixel-art games involving player movement, physics, TileMapLayer worlds, animation, combat, game feel, VFX/shaders, camera, UI, audio, AI/navigation, save/data/dialogue, asset pipelines, performance, testing or export. Prefer focused references and runtime validation; do not preload every reference.
---

# Godot 2D Game Development Skill

## Status

- Version: v0.2
- Category: `development`
- Maturity: `production-oriented`
- Owner: `Kukutx`
- Last updated: 2026-08-15
- Focus: Godot 4.x, 2D-first, pixel art, action feel, production-ready assets

## Purpose

帮助 Agent 用 **简单、可维护、可验证** 的方式开发 Godot 2D 游戏。

默认顺序：

1. 先让玩法机制正确。
2. 再保证状态、动画、碰撞和事件同步。
3. 再加入镜头、音频、VFX、UI 和打击感。
4. 最后做性能、测试和发布检查。

不要为了“专业”而提前堆框架。不要把表现层当作玩法真源。

## When to use

用于：

- Godot 2D / pixel-art 项目。
- platformer、top-down、ARPG、roguelike、RPG、tower defense、puzzle 等 2D 游戏。
- CharacterBody2D、Area2D、TileMapLayer、Camera2D、AnimationPlayer、AnimationTree、AnimatedSprite2D。
- combat、hitbox/hurtbox、combo、i-frame、knockback、hit-stop、screen shake。
- pixel animation、spritesheet、tileset、map、FX、UI art。
- HUD/menu、gamepad focus、responsive UI。
- AI/navigation、save/load、dialogue、inventory/data-driven systems。
- shader/particles/2D lighting、audio feedback。
- profiling、debugging、tests、export。

## When not to use

- 明确的 3D 游戏任务。
- 普通插画、海报、营销视觉。
- 纯通用代码审查或 Bug 诊断且与游戏领域无关。
- 只做 spritesheet 切分时，优先 `development/game-dev-spritesheet-slicer`。

## First rule: inspect before changing

现有项目先确认：

- `project.godot` 与实际 Godot 版本。
- GDScript / C#；不要擅自换语言。
- scene tree 与场景拆分方式。
- Input Map。
- collision layers / masks。
- signals、Resources、autoloads。
- animation、sprites、tiles、UI theme、audio buses、shaders。
- 当前任务最小修改范围。

**沿用合理的现有结构。** 只有结构确实阻碍当前任务时才建议调整。

## Progressive disclosure

不要一次加载全部 reference。根据任务只读取最小集合，通常 1–3 个。

| User intent | Read |
| --- | --- |
| scene ownership、signals、Resources、state/FSM、GDScript 结构 | `references/core-architecture.md` |
| movement、input、physics、dash/jump、Camera2D | `references/movement-input-camera.md` |
| TileMapLayer、top-down depth、parallax、collision、level layout | `references/world-tilemap-level-design.md` |
| sprite/cel animation、AnimatedSprite2D、AnimationPlayer/Tree、pixel timing | `references/animation-pixel.md` |
| hitbox/hurtbox、combat、hit-stop、shake、recoil、impact feedback | `references/combat-game-feel.md` |
| particles、CanvasItem shader、outline/flash/dissolve、2D lighting | `references/rendering-vfx-shaders.md` |
| HUD/menu、Control、Container、Theme、focus、safe area | `references/ui-ux.md` |
| SFX、music、bus、ducking、variation、2D positional audio | `references/audio.md` |
| enemy AI、FSM、NavigationAgent2D、steering、procedural generation | `references/ai-navigation-procedural.md` |
| Resources、inventory data、save migration、dialogue、localization | `references/data-save-dialogue.md` |
| sprite/FX/map/tiles/UI asset generation and Godot handoff | `references/asset-pipeline.md` |
| profiler、debug、tests、runtime QA、export | `references/performance-testing-debugging.md` |
| optional MCP/Aseprite/asset-generation companions | `references/companion-tools.md` |
| upstream sources and maintenance notes | `references/sources.md` |
| maintain/test this SuperSkill's routing | `references/quality-tests.md` |
| spritesheet layout/slicing/naming | `../game-dev-spritesheet-slicer/skill.md` |

`references/godot-2d.md` is a compatibility index for older prompts; prefer the focused files above.

## Common compositions

### Player controller

Read:

```text
core-architecture
+ movement-input-camera
+ animation-pixel
```

Add `combat-game-feel` only if the controller includes combat/juice.

### Top-down combat

Read:

```text
movement-input-camera
+ animation-pixel
+ combat-game-feel
```

Add `rendering-vfx-shaders` for effects.

### Pixel-art content production

Read:

```text
asset-pipeline
+ animation-pixel
+ game-dev-spritesheet-slicer
```

### Map / level

Read:

```text
world-tilemap-level-design
+ asset-pipeline
```

Add `ai-navigation-procedural` only when navigation/procedural layout is needed.

### HUD / menus

Read:

```text
ui-ux
```

Add `audio` or `combat-game-feel` only for feedback/polish.

### Enemy AI

Read:

```text
ai-navigation-procedural
+ core-architecture
```

Add movement/combat references only for those behaviors.

### Performance or broken runtime behavior

Read:

```text
performance-testing-debugging
```

Then load the domain reference for the actual bottleneck/bug.

## Core execution workflow

### 1. Define the player-visible result

先描述玩家应该感受到什么，而不是先设计 manager/class。

Examples:

- “按攻击键立即起手，第 3 帧命中，敌人后退并短暂停顿。”
- “角色落地有轻微 squash 和尘土，但控制不被锁住。”
- “手柄打开暂停菜单时永远有一个明确焦点。”

### 2. Establish ownership

每个事实只能有清楚的 owner。

Typical ownership:

```text
Input -> player intent
Character/state -> allowed action + gameplay state
Physics -> movement/collision result
Combat -> hit/damage result
Animation -> presentation timeline
Camera/VFX/Audio/UI -> react to events
Save data -> persistent state
```

不要让多个系统同时改同一个状态而没有明确优先级。

### 3. Implement the mechanic first

最小闭环：

```text
input
-> gameplay decision/state
-> physics/combat/data result
-> signal/event
```

先确认这一层正确，再加表现。

### 4. Synchronize presentation

需要同步的内容尽量共用同一事件或时间线：

- animation/frame event
- hitbox active window
- projectile spawn
- SFX
- particles
- shader flash
- camera feedback
- HUD feedback

不要用多个互不相关 timer 猜同一时刻。

### 5. Add polish in layers

从少到多：

```text
sound
-> readable visual FX
-> recoil/knockback
-> short hit-stop
-> camera shake
-> secondary polish
```

低重要度事件不要使用 boss 级反馈。

### 6. Validate in runtime

优先真实运行，而不是只看代码。

至少验证：

- input 仍然及时；
- physics/collision 正确；
- state 能正常进入和退出；
- animation/hitbox/SFX/VFX 同步；
- repeated triggers 不会无限叠 Tween/timer/node；
- UI 多分辨率和手柄可用；
- pixel assets 在实际游戏尺度清晰；
- 没有明显 runtime error/warning。

如果项目已配置 Godot MCP / live-editor automation，优先使用 inspect -> edit -> run -> capture errors/screenshot -> fix 的闭环；没有就使用 Godot CLI/editor 与项目现有测试工具。

## Architecture defaults

这些是默认选择，不是必须套用的框架：

- `CharacterBody2D`: 玩家/敌人主动移动主体。
- `Area2D`: hitbox、hurtbox、trigger、pickup、detection。
- `Resource`: 可复用配置、item/attack/stats/content 数据。
- `AnimatedSprite2D`: 纯 sprite-frame animation。
- `AnimationPlayer`: property/method/SFX/hitbox timeline。
- `AnimationTree`: blending / complex transition 真正需要时再上。
- `Tween`: short, dynamic, interruptible visual/UI feedback。
- `Control` + `Container` + `Theme`: UI。
- signals: one event -> multiple listeners 或需要解耦时。
- direct calls: simple owner-child/direct dependency 时通常更清楚。

## Hard constraints

- 不做无任务价值的 manager/service/event-bus/ECS/FSM 抽象。
- 不把 Gameplay 真源放在粒子、UI、camera 或 shader。
- 不把 CharacterBody2D 的关键运动放在 `_process()`。
- 不用 groups 替代高频 physics layer/mask filtering。
- 不让 hitbox 永久开启。
- 不让 HUD 每帧轮询本可事件驱动的数据。
- 不让多个 Tween 争夺同一 property。
- 不用阻塞 sleep/delay 实现 hit-stop。
- 不通过移动真实 player transform 模拟 screen shake。
- 不逐帧独立生成同一角色动画，除非接受较高 drift。
- 不在没 profiling 的情况下先做复杂 pooling/MultiMesh/架构重写。
- 不自动安装外部工具、MCP 或依赖；仅在用户需要且环境支持时建议/使用。

## Output contract

默认输出：

1. **结论 / 问题**
2. **修改位置**
3. **具体修改**
4. **原因**
5. **最小验证**

用户要求直接实现时，直接实现；不要先生成长篇设计文档。

## Quality bar

完成前确认：

- responsibilities 清楚；
- project convention 被尊重；
- code/API 与实际 Godot 版本匹配；
- 2D/pixel 项目没有被引入无意义 3D 方案；
- input responsiveness 没被 polish 破坏；
- visuals/audio/UI 与 gameplay event 对齐；
- runtime/visual behavior 有实际验证路径；
- 改动没有超出用户请求范围。

## Maintenance rule

这个 SuperSkill **吸收原则，不机械复制外部 Skill**。保留高价值决策、anti-pattern、验证方法与 2D-specific knowledge；删除营销文案、重复教程和与当前任务无关的引擎内容。

外部来源、许可证和各来源适合承担的知识范围见 `references/sources.md`。修改路由或新增领域后，用 `references/quality-tests.md` 做回归检查。
