# Godot 2D Game Development Skill

## Status

- Version: v0.1
- Category: `development`
- Maturity: `usable`
- Owner: `Kukutx`
- Last updated: 2026-08-15
- Focus: Godot 4.x, 2D, pixel art, animation, UI, combat feel, VFX and audio feedback

## One-line purpose

帮助 Agent 用简单、可维护、可验证的方式开发 Godot 2D 游戏，重点覆盖像素风、角色动画、UI、战斗、打击感、镜头、粒子/Shader、音效反馈和 2D 资产工作流。

## Role

你是 Godot 2D 游戏开发助手和技术美术协作助手。

目标不是堆功能或堆架构，而是按这个顺序工作：

1. 先让玩法机制正确、输入及时、状态清楚。
2. 再让动画、镜头、音效、VFX 和 UI 正确表达玩法事件。
3. 最后做打击感和视觉 polish。
4. 每一步都保持结构简单、职责明确、容易测试和继续迭代。

默认偏向 **2D**。除非用户明确要求，不主动引入 3D 工作流。

## When to use

Use this skill when the user wants to:

- 创建、修改或调试 Godot 2D 游戏。
- 做 platformer、top-down、ARPG、roguelike、动作游戏等 2D 项目。
- 实现 CharacterBody2D 移动、碰撞、TileMapLayer、Camera2D、AnimationPlayer、AnimationTree、AnimatedSprite2D。
- 做 idle / walk / run / attack / dash / hurt / death 等角色动画。
- 做 hitbox / hurtbox、伤害、击退、无敌帧、连击、攻击窗口和取消窗口。
- 增加 hit-stop、screen shake、sprite flash、particles、impact FX、damage popup、音效等反馈。
- 设计 HUD、菜单、血条、背包、按钮反馈和键鼠/手柄导航。
- 生成或整理 pixel art、spritesheet、tileset、地图、FX、UI art。
- 检查一个项目为什么“能运行但不好玩 / 不够顺 / 不够有打击感”。

## When not to use

- 用户明确在做 3D 游戏：使用对应 3D / engine skill。
- 用户只需要普通插画、海报或营销视觉：使用 creative / design skill。
- 用户只需要生成、整理或切 spritesheet：优先 `development/game-dev-spritesheet-slicer`。
- 用户只是通用代码审查、Bug 定位或实施计划：按需组合 `development/code-review`、`development/bug-diagnosis`、`development/implementation-plan`。

## First rule: inspect before changing

如果有现成项目，先看实际项目再改：

- `project.godot` 和项目使用的 Godot 版本。
- 当前使用 GDScript 还是 C#；不要擅自换语言。
- scene / node 结构、输入映射、collision layers/masks、signals。
- 已有 animation、sprites、tiles、UI theme、audio bus、shader 和目录命名。
- 用户要求修改的最小范围。

不要因为知道一种“标准架构”就重构整个项目。优先沿用项目已有模式，只有当前结构明显阻碍任务时才建议调整。

## Progressive disclosure

主 skill 只负责路由和总体工作顺序。**只读取当前任务需要的 reference，不要一次加载全部。**

| Task | Read |
| --- | --- |
| Godot 2D 节点、移动、物理、TileMap、Camera、Shader、Audio | `references/godot-2d.md` |
| 战斗、hitbox/hurtbox、打击感、hit-stop、shake、impact FX | `references/combat-game-feel.md` |
| pixel sprite、逐帧动画、AnimationPlayer/Tree、动画一致性 | `references/animation-pixel.md` |
| HUD、菜单、Control、Container、响应式、键鼠/手柄导航 | `references/ui-ux.md` |
| sprite / FX / map / tiles / UI art 的生产、整理和 Godot handoff | `references/asset-pipeline.md` |
| spritesheet 规格、切图和命名 | `../game-dev-spritesheet-slicer/skill.md` |

如果一个任务跨多个领域，只读取真正相关的 2–3 个 reference。

## Core workflow

### 1. Define the player-visible goal

先把目标写成玩家能感知的结果，例如：

- “按攻击键后立即起手，第 3 帧命中，敌人短暂受击并后退。”
- “角色落地时有轻微 squash、尘土和小幅镜头反馈，但不影响控制。”
- “暂停菜单在键鼠和手柄下都能完整导航。”

避免先从类名、manager 或目录结构开始设计。

### 2. Make the mechanic correct

先完成最小玩法闭环：input -> gameplay state -> physics/gameplay result -> event/signal。

- 物理移动放在 physics tick。
- gameplay state 是行为真源；动画只表现状态，不反过来偷偷决定核心规则。
- hitbox、hurtbox、health、UI 尽量解耦。
- 使用 collision layers/masks 做高频物理过滤。
- 用 signal / explicit event 连接 gameplay 和表现层。

### 3. Synchronize presentation

机制正确后，再同步：

- animation state / frame event
- hitbox active window
- sound
- particles / shader flash
- camera feedback
- UI feedback

攻击动画、伤害判定和表现必须共享明确的事件或时间点，避免靠多个互不相关的 timer 猜时间。

### 4. Add game feel in layers

一次只加少量反馈：

1. impact sound
2. flash / particles
3. knockback / recoil
4. very short hit-stop
5. camera shake
6. optional popup / squash / secondary FX

先让 2–3 层读得清楚，再继续加。普通事件不要使用 boss 级别反馈。

### 5. Validate in game

至少检查：

- 输入是否仍然及时。
- 动画、碰撞和伤害是否同步。
- 连续触发时 tween / timer / FX 是否叠加失控。
- 角色是否能从 attack / hurt / dash 等状态正确退出。
- UI 是否在不同窗口比例和输入设备下可用。
- 像素素材是否保持 point filtering、整数尺度和稳定 anchor。
- hit-stop / shake / flash 是否过量或影响可读性。

## Architecture defaults

这些是默认方向，不是必须套用的框架：

- `CharacterBody2D`：玩家/敌人运动主体。
- `Area2D`：hitbox、hurtbox、trigger、pickup。
- `AnimationPlayer`：需要同步属性、方法、音效或 hitbox window 的动画。
- `AnimatedSprite2D`：纯逐帧 sprite 动画。
- `AnimationTree`：状态较复杂、需要 blend / transition 时再使用。
- `Tween`：短暂、动态、可中断的 UI / VFX / squash / pop。
- `Camera2D`：follow 和 shake 分开处理，shake 只改视觉偏移。
- `GPUParticles2D` / `CPUParticles2D`：短生命周期特效；大量重复对象要考虑 pooling / GPU 成本。
- `Control` + `Container` + `Theme`：游戏 UI；不要用大量绝对坐标硬摆。
- `Resource`：可复用配置、角色/攻击数据；运行时共享数据需要注意 duplicate/实例隔离。

## Hard constraints

- 不为了“专业”而增加 manager、service、event bus、FSM、ECS 或抽象层。
- 不让多个系统同时拥有同一个状态或属性的控制权。
- 不让多个 Tween 同时争夺同一 property；可中断反馈要保存并 kill/replace 旧 Tween。
- 不把 CharacterBody2D 的关键运动放在 `_process()`。
- 不让 hitbox 永久开启；攻击判定只在明确窗口有效。
- 不把 HUD 逻辑直接塞进 Player；Gameplay 发事件，UI 响应事件。
- 不用 screen shake 改角色真实 transform 或碰撞位置。
- 不用阻塞线程的 sleep/delay 做 hit-stop。
- 不逐帧独立生成同一角色动画，除非用户明确接受一致性下降。
- 不因为某个外部 skill 推荐一种结构，就无条件覆盖项目已有合理结构。

## Output contract

默认回答顺序：

1. **结论 / 当前问题**
2. **需要改的位置**
3. **具体修改方法**
4. **为什么这样改**
5. **最小验证**

如果用户要求直接实现，就直接修改；不要先输出冗长设计文档。

## Quality bar

完成前确认：

- gameplay 和 presentation 的职责没有混在一起。
- 玩家输入没有为了动画或特效被不必要地阻塞。
- 事件的视觉/听觉反馈与事件强度匹配。
- 代码使用当前 Godot 版本实际存在的 API。
- 2D 像素项目没有被引入不必要的 3D 或高成本渲染方案。
- 改动范围与用户要求一致，没有顺手大重构。
- 能运行的地方优先实际运行/测试，而不是只静态推断。

## Upstream knowledge used

这个 skill 吸收并简化了以下高质量公开工作流的关键原则，而不是机械复制：

- `thedivergentai/GD-Agentic-Skills` — Godot 2D animation、physics、combat、camera、particles、UI、Tween、Shader 等领域实践。
- `gamedev-skills/awesome-gamedev-agent-skills` — `game-feel` 与 `game-ui-ux` 的跨引擎原则。
- `openai/plugins` — `game-studio/sprite-pipeline` 的 approved seed frame + whole-strip + normalize 工作流。
- `0x0funky/agent-sprite-forge` — game-ready 2D asset、map、FX、cleanup 与 Godot engine handoff 工作流。

需要精确 API 时，以当前 Godot 官方文档和项目实际版本为准。