---
name: godot-2d-game-development
description: Godot 4.x 2D game-development router and execution guide. Use for 2D/pixel-art games involving architecture, movement/physics/camera, input/remapping/accessibility, TileMapLayer worlds, animation, combat, game feel, VFX/shaders, UI, audio, AI/navigation, save/inventory/progression, dialogue/localization, asset pipelines, runtime validation, performance/testing, export or CI. Load only the focused references needed for the task.
---

# Godot 2D Game Development Skill

## Status

- Version: v0.3
- Category: `development`
- Maturity: `production-oriented`
- Owner: `Kukutx`
- Last updated: 2026-08-15
- Focus: Godot 4.x, 2D-first, pixel art, responsive controls, game feel, production assets and runtime verification

## Purpose

帮助 Agent 用 **简单、可维护、可验证** 的方式开发 Godot 2D 游戏。

默认顺序：

1. 明确玩家能感知的目标。
2. 确定 gameplay truth 和 owner。
3. 先让机制、输入、物理、数据正确。
4. 再同步 animation / UI / audio / VFX / camera。
5. 最后做 game feel、性能、测试和发布验证。

不要为了“专业”提前堆框架；不要把表现层当玩法真源。

## First rule: inspect before changing

现有项目先确认：

- `project.godot` 与实际 Godot 版本。
- GDScript / C#；不要擅自换语言。
- scene tree、autoload、Resource、signal 使用方式。
- Input Map、collision layers/masks。
- animation、sprites、tiles、Theme、audio buses、shaders。
- 已安装 addons / MCP / test framework。
- 当前任务最小修改范围。

沿用合理结构。只有现状确实阻碍当前任务时才建议调整。

## Progressive disclosure

通常只读 **1–3 个** reference。

| User intent | Read |
| --- | --- |
| scene ownership、signals、Resources、state/FSM、GDScript 结构 | `references/core-architecture.md` |
| CharacterBody2D、movement、physics、jump/dash、Camera2D、pixel camera | `references/movement-physics-camera.md` |
| Input Map、键鼠/手柄/触控、remap、device switching、rumble、input accessibility | `references/input-controls-accessibility.md` |
| TileMapLayer、top-down depth、parallax、collision、level layout | `references/world-tilemap-level-design.md` |
| sprite/cel animation、AnimatedSprite2D、AnimationPlayer/Tree、pixel timing | `references/animation-pixel.md` |
| hitbox/hurtbox、damage、i-frame、combo、attack windows | `references/combat-system.md` |
| hit-stop、shake、flash、recoil、squash、impact feedback | `references/game-feel.md` |
| particles、CanvasItem shader、outline/flash/dissolve、2D lighting | `references/rendering-vfx-shaders.md` |
| HUD/menu、Control、Container、Theme、focus、safe area | `references/ui-ux.md` |
| SFX、music、bus、ducking、variation、2D positional audio | `references/audio.md` |
| enemy AI、NavigationAgent2D、steering、behavior complexity、procedural generation | `references/ai-navigation-procedural.md` |
| inventory、persistent IDs、save/load、migration、settings、progression | `references/save-inventory-progression.md` |
| branching dialogue、conditions/effects、localization、dialogue UI | `references/dialogue-localization.md` |
| sprite/FX/map/tiles/UI asset production and Godot handoff | `references/asset-pipeline.md` |
| profiler、runtime debugging、automated tests | `references/performance-testing-debugging.md` |
| Agent inspect -> edit -> run -> screenshot/input/errors -> verify loop | `references/runtime-agent-validation.md` |
| export presets、clean CI、version pinning、build artifacts | `references/release-export-ci.md` |
| optional MCP/addons/importers/templates | `references/companion-tools.md` |
| upstream sources / maintenance | `references/sources.md` |
| routing regression tests | `references/quality-tests.md` |
| spritesheet geometry/slicing/naming | `../game-dev-spritesheet-slicer/skill.md` |

Compatibility indexes remain for older prompts:

- `references/movement-input-camera.md`
- `references/combat-game-feel.md`
- `references/data-save-dialogue.md`
- `references/godot-2d.md`

## Common compositions

### Player controller

```text
movement-physics-camera
+ input-controls-accessibility   # only when controls/device/remap matter
+ animation-pixel               # when presentation is included
```

### Combat bug

```text
combat-system
+ animation-pixel                # if timing/window related
```

Do **not** load game-feel just because the task contains the word “attack”.

### “Combat works but feels weak”

```text
game-feel
+ optional rendering-vfx-shaders
+ optional audio
```

Do not rewrite damage architecture unless evidence shows it is wrong.

### Pixel-art content

```text
asset-pipeline
+ animation-pixel
+ game-dev-spritesheet-slicer when exact sheet geometry is needed
```

### HUD / menus / controls

```text
ui-ux
+ input-controls-accessibility when keyboard/gamepad/touch/remap matters
```

### Enemy AI

```text
ai-navigation-procedural
+ core-architecture only if state ownership needs work
```

### Save / inventory

```text
save-inventory-progression
```

Add `dialogue-localization` only if dialogue/translated content depends on those flags/items.

### Release / CI

```text
release-export-ci
+ performance-testing-debugging if tests/smoke checks are part of the pipeline
```

### Agentic visual/runtime iteration

```text
runtime-agent-validation
+ the domain reference being changed
```

## Core execution workflow

### 1. Define the player-visible result

Examples:

- “按攻击键立即起手，第 3 帧命中，敌人后退并短暂停顿。”
- “键鼠切到手柄后提示图标立即更新，暂停菜单仍有焦点。”
- “旧存档升级后能迁移，不丢 inventory。”

不要先从 manager/class 名开始设计。

### 2. Establish ownership

```text
physical input -> input intent
character/state -> allowed action + gameplay state
physics -> movement/collision result
combat -> hit/damage result
animation -> presentation timeline
camera/VFX/audio/UI -> react to events
save system -> persistent state
```

每个事实有清楚 owner；避免多系统同时写同一状态。

### 3. Implement truth before presentation

最小闭环：

```text
input/event
-> gameplay decision
-> physics/combat/data result
-> explicit event/signal
```

### 4. Synchronize presentation

需要同步的东西共用明确事件或时间线：

- animation/frame event
- hitbox active window
- projectile spawn
- SFX
- particles/shader
- camera feedback
- HUD feedback

不要多个独立 timer 猜同一个时刻。

### 5. Add polish proportionally

```text
sound/readability
-> recoil/knockback
-> flash/particles
-> short hit-stop
-> camera shake
-> secondary polish
```

先少量，再根据实际 playtest 加。

### 6. Validate with evidence

优先：

```text
inspect
-> edit
-> run
-> observe errors + behavior + screenshot/input where available
-> fix
-> repeat
```

没有 live bridge 时，使用 Godot editor/CLI、项目测试和人工可验证步骤。不要把“代码看起来对”当成完成。

## Architecture defaults

默认选择，不是强制框架：

- `CharacterBody2D`: 主动角色运动。
- `Area2D`: hitbox/hurtbox/trigger/pickup/detection。
- `Resource`: definitions/config/content data。
- `AnimatedSprite2D`: 纯逐帧动画。
- `AnimationPlayer`: property/method/SFX/hitbox timeline。
- `AnimationTree`: blending/transition 复杂度真正需要时。
- `Tween`: 短暂、动态、可中断的视觉/UI反馈。
- `Control` + `Container` + `Theme`: UI。
- signal: one event -> multiple listeners 或需要解耦时。
- direct call: 简单明确依赖通常更清楚。

## Dependency rule

外部 addon/tool 只在以下条件满足时考虑：

1. 当前问题已经超过原生方案的合理复杂度；
2. 项目 Godot 版本兼容；
3. addon 解决的是明确问题，而不是“看起来更专业”；
4. 用户允许新增依赖；
5. 能说明迁移/维护成本。

已有项目优先复用现有依赖，不并行引入两个重叠工具。

## Hard constraints

- 不做无任务价值的 manager/service/event-bus/ECS/FSM 抽象。
- 不把 gameplay truth 放在粒子、UI、camera、shader 或音效。
- 不把 CharacterBody2D 关键运动放 `_process()`。
- 不用 groups 替代高频 physics layers/masks。
- 不让 hitbox 永久开启。
- 不让 HUD 每帧轮询本可事件驱动的数据。
- 不让多个 Tween 争夺同一 property。
- 不用阻塞 sleep/delay 做 hit-stop。
- 不移动真实 player body 模拟 screen shake。
- 不逐帧独立生成同一 AI 角色动画，除非接受 drift。
- 不在未 profiling 前先做复杂 pooling/MultiMesh/架构重写。
- 不自动安装 addon/MCP/test framework/template。
- 不把第三方示例/API 视为高于当前 Godot 官方文档与项目版本。

## Output contract

默认：

1. **结论 / 问题**
2. **修改位置**
3. **具体修改**
4. **原因**
5. **最小验证**

用户要求直接实现时直接实现，不先输出长篇设计文档。

## Quality bar

完成前确认：

- ownership 清楚；
- project convention 被尊重；
- API 与项目 Godot 版本匹配；
- input responsiveness 没被 polish 破坏；
- visuals/audio/UI 与 gameplay event 对齐；
- save/import/export 不是只在开发机偶然工作；
- runtime/visual behavior 有实际验证证据或明确验证路径；
- 没有无关 3D、依赖或重构。

## Maintenance rule

本 SuperSkill **synthesizes decisions, not bulk copies**。新增内容必须改变 Agent 的实际决策、避免真实错误或明显提升验证质量。来源与许可证见 `references/sources.md`；路由改动后运行 `references/quality-tests.md` 的压力测试。