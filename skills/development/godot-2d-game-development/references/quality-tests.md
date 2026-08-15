# Godot 2D SuperSkill Routing Quality Tests

维护/评审 SuperSkill 时使用。普通游戏开发任务不要加载。

目标：验证 Agent 选对 **最小 reference 集合**，并避免 addon/tool overreach。

## Pass criteria

每个场景应满足：

- 主路由正确；
- 通常只加载 1–3 个 reference；
- gameplay truth ownership 清楚；
- 不自动安装 addon/MCP/template/test framework；
- 不引入无关 3D；
- 版本敏感内容先确认 Godot version；
- 有与声明匹配的 runtime/QA 路径。

## Routing matrix

| Prompt | Expected primary references | Must avoid |
| --- | --- | --- |
| “8 向 top-down 移动 + 顺滑 Camera2D” | `movement-physics-camera` | input/addon/combat refs 全加载 |
| “键鼠切手柄时提示自动换，允许重映射” | `input-controls-accessibility` + `ui-ux` | 为 movement 重写 controller |
| “手柄 drift 导致 UI 一直切图标” | `input-controls-accessibility` | camera/game-feel |
| “dash 在 attack recovery 后经常吞输入” | `input-controls-accessibility` + `movement-physics-camera` | 默认安装 input addon |
| “一个挥砍扣了三次血” | `combat-system` | 先调 screen shake |
| “攻击第 4 帧才激活 hitbox” | `combat-system` + `animation-pixel` | 独立 Timer 猜 timing |
| “伤害都对，但砍起来很软” | `game-feel` + optional `audio`/`rendering-vfx-shaders` | 重写 damage architecture |
| “大量 hit particles FPS 掉” | `performance-testing-debugging` + `rendering-vfx-shaders` | 未 profile 就 ECS/MultiMesh 重写 |
| “Aseprite 文件已有 tags/timing，要进 Godot” | `animation-pixel` + `asset-pipeline` + optional `companion-tools` | 当成 AI-generated strip 重新生成 |
| “AI 生成 attack strip 并导入 Godot” | `animation-pixel` + `asset-pipeline` + slicer | 默认装 Aseprite importer |
| “可编辑 top-down 森林地图，树遮挡玩家” | `world-tilemap-level-design` + `asset-pipeline` | collision/spawn 烤进 PNG |
| “敌人巡逻、发现、追逐、攻击” | `ai-navigation-procedural` | 默认 BT addon |
| “20 种敌人共享很多 condition/action，FSM 重复” | `ai-navigation-procedural` + optional `companion-tools` | 直接指定最重 AI framework |
| “Boss 同时有 movement phase 和 parallel shield/attack state” | `core-architecture` + optional `ai-navigation-procedural` | bool soup；也不无条件装 State Charts |
| “旧存档升级后 inventory 丢了” | `save-inventory-progression` | SceneTree snapshot workaround |
| “对话有复杂条件、选择、多语言” | `dialogue-localization` | 把 story logic 塞 Button callback |
| “对话选择给物品且永久保存” | `dialogue-localization` + `save-inventory-progression` | 插件变量成为 inventory truth |
| “Godot 4.x GitHub Actions clean export” | `release-export-ci` | `latest` toolchain / local cache 依赖 |
| “Agent 改了暂停菜单，验证手柄真的能操作” | `runtime-agent-validation` + `ui-ux` + optional `input-controls-accessibility` | 只说代码看起来正确 |
| “新项目要 main menu/options/pause/credits” | `ui-ux` + optional `companion-tools` | 成熟项目也硬套完整 template |
| “只切 64x64 sprite sheet” | spritesheet slicer | 主 Godot 全域 refs |
| “Godot 3D 第三人称” | route outside this skill | 套 2D reference |

## Behavioral pressure tests

### Existing project respect

Prompt:

```text
这个项目已有简单 enum FSM，可以跑。只加 dash。
```

Pass:

- 沿用 enum FSM；
- movement/input only；
- 不引入 State Charts/LimboAI/Beehave；
- 验证 cooldown/collision/state exit。

### Native-first input

Prompt:

```text
我只有键盘控制，想把 jump 从 Space 改成 J。
```

Pass:

- 修改 InputMap/project binding 即可；
- 不建议 Input Helper；
- 不创建新的 input abstraction layer。

### Input Helper justified

Prompt:

```text
设置页需要运行时重映射、自动识别最近手柄/键盘、更新 prompts，还要 rumble 设置。
```

Pass:

- `input-controls-accessibility`；
- 先检查现有 input abstraction；
- 没有时可以把 Input Helper 作为候选；
- 说明 dependency/version check；
- 不把 addon 变成 gameplay truth。

### Combat vs game feel

Prompt A:

```text
一刀有时命中两次。
```

Pass: `combat-system`，先检查 attack instance/i-frame/window。

Prompt B:

```text
命中次数和伤害都对，但没有重量。
```

Pass: `game-feel`，从 sound/contact FX/recoil 开始，不重构 damage system。

### Authored vs generated pixel assets

Prompt A:

```text
我的 .aseprite 已经有 idle/run/attack tags 和不同 frame durations。
```

Pass:

- preserve source metadata；
- optional Aseprite Wizard/Importality only if project benefits；
- 不重新 AI 生成。

Prompt B:

```text
AI 给了我一条 6 帧透明 PNG attack strip。
```

Pass:

- deterministic normalize/slice；
- shared anchor/scale；
- 不默认安装 Aseprite importer。

### AI complexity ladder

Prompt A:

```text
敌人只要 idle/chase/attack。
```

Pass: handwritten state。

Prompt B:

```text
很多敌人共享 condition/action/subtree，想可视化 BT。
```

Pass: 可比较 Beehave；不直接升级到最重 stack。

Prompt C:

```text
需要 BT + hierarchical FSM + blackboard/debugger。
```

Pass: 可以评估 LimboAI。

Prompt D:

```text
玩家状态有平行 weapon mode + locomotion + status effects，手写 FSM 爆炸。
```

Pass: 可评估 State Charts；不要误当 enemy BT 问题。

### Save migration

Prompt:

```text
v3 把 item id 全换了，v2 存档要继续能开。
```

Pass:

- stable mapping/migration step；
- old fixture test；
- 不通过 display name 猜；
- migration failure 不静默清空 save。

### Dialogue addon restraint

Prompt:

```text
只有 5 段线性 NPC 文本。
```

Pass: 不推荐大型 dialogue framework。

Prompt:

```text
几百个分支、条件、mutations、多语言、内容人员需要编辑器。
```

Pass: 可评估 Dialogue Manager/Dialogic，并根据项目需求区分；检查 Godot compatible release。

### Clean CI

Prompt:

```text
我本地 export 正常，GitHub Actions 说资源不存在。
```

Pass:

- 比较 exact Godot/templates；
- LFS/submodule/case-sensitive path/import cache；
- clean import before export；
- 不先“清空重装所有依赖”。

### Runtime evidence

Prompt:

```text
我改了 HUD，确认修好了吧？
```

Pass:

- 有 live tool 时实际 run/resize/input/screenshot；
- 无 live tool 时明确静态 vs runtime 未验证；
- 不虚构“已经看过画面”。

### MCP restraint

Prompt:

```text
只改一个 GDScript 常量。
```

Pass: 不为了验证简单文本改动而自动安装 MCP。

Prompt:

```text
要让 Agent 自动走菜单、按按钮、截图验证 UI。
```

Pass: `runtime-agent-validation` + optional MCP selection；优先复用已安装 bridge，只选一个重叠最少的工具。

## Maintenance regression rule

新增 reference/source/addon 前回答：

1. 现有 reference 处理不了的具体问题是什么？
2. 它改变哪个 Agent 决策？
3. 是知识 source、optional tool，还是默认 dependency？
4. 会不会造成 routing overlap/context bloat？
5. Godot version/license/maintenance/security 是否需要检查？
6. 是否有真实 pressure test？
7. 删除它后是否仍能用原生 Godot 完成基本任务？

答不清楚就不要加入。