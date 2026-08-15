# Godot 2D SuperSkill Routing Quality Tests

维护/评审 SuperSkill 时使用。普通游戏开发任务不要加载。

目标：验证 Agent 能 **选对最小 reference 集合**，而不是关键词一出现就加载全部。

## Pass criteria

每个场景应满足：

- 主路由正确；
- 通常只加载 1–3 个 reference；
- 不自动安装 addon/MCP；
- 不把表现层当 gameplay truth；
- 不引入无关 3D；
- 有明确 runtime/QA 路径。

## Routing cases

| Prompt | Expected primary references | Must avoid |
| --- | --- | --- |
| “做一个 8 向 top-down 移动，带加减速和顺滑 Camera2D” | `movement-input-camera` + optional `core-architecture` | combat/VFX/data 全加载 |
| “剑打中敌人没感觉，帮我增强打击感” | `combat-game-feel` + optional `rendering-vfx-shaders` / `audio` | 重写 combat architecture |
| “AI 生成角色 attack 像素动画并导入 Godot” | `animation-pixel` + `asset-pipeline` + spritesheet slicer | 逐帧独立生成 |
| “做可编辑 top-down 森林地图，树能遮挡玩家” | `world-tilemap-level-design` + `asset-pipeline` | 把 collision/spawn 烤进一张 PNG |
| “敌人巡逻、发现玩家、追逐、攻击” | `ai-navigation-procedural` + optional `core-architecture` | 默认安装 behavior tree plugin |
| “复杂 boss 有并行状态和多层 phase，当前 FSM 已失控” | `core-architecture` + `ai-navigation-procedural` | 继续堆 bool；也不要无条件指定插件 |
| “存档升级后旧档打不开” | `data-save-dialogue` + `performance-testing-debugging` | 保存 SceneTree snapshot |
| “Godot 4.6 项目要加自动化测试” | `performance-testing-debugging` | 不查版本就安装最新测试框架 |
| “大量 hit particles 时 FPS 掉” | `performance-testing-debugging` + `rendering-vfx-shaders` | 未 profile 就重写 ECS/MultiMesh |
| “手柄打开暂停菜单无法操作” | `ui-ux` | gameplay/combat refs |
| “敌人受击做 white flash shader” | `rendering-vfx-shaders` + `combat-game-feel` | shader 决定伤害 |
| “场景切换音乐 crossfade，战斗时压低 BGM” | `audio` | camera/VFX |
| “对话很多、分支和条件复杂，想选成熟 addon” | `data-save-dialogue` + `companion-tools` | 自动安装或锁死版本 |
| “多个虚拟 camera 之间做 authored transitions” | `movement-input-camera` + `companion-tools` | 简单 follow 也强制 Phantom Camera |
| “只把 64x64 角色 sheet 切成动作帧” | spritesheet slicer | 主 Godot 全域 refs |
| “做 Godot 3D 第三人称角色” | route outside this skill | 套用 2D skill |

## Behavioral pressure tests

### Existing-project respect

Prompt:

```text
这个项目已经用一个简单 enum FSM，可以跑。只帮我加 dash。
```

Pass:

- 沿用现有 FSM；
- 只改 dash 所需状态/输入/移动；
- 不引入 State Charts/LimboAI；
- 验证 cooldown、collision、animation exit。

### Presentation ownership

Prompt:

```text
攻击第 4 帧显示 slash FX，所以我想直接在 FX 出现时扣血。
```

Pass:

- 指出 FX 不是伤害真源；
- 共享 authoritative attack/frame event；
- combat resolves damage；
- FX reacts to confirmed/timed event。

### Pixel asset consistency

Prompt:

```text
给同一个角色分别生成 8 张 attack frame。
```

Pass:

- 优先建议 approved seed + whole action strip；
- shared scale/anchor；
- preview before import；
- 用户坚持独立帧时才接受并说明 drift 风险。

### Tool restraint

Prompt:

```text
帮我把敌人追踪做好。
```

Pass:

- 先用简单 state + NavigationAgent2D/steering 判断需求；
- 不因为存在 LimboAI 就自动安装；
- 只有复杂可复用行为树需求才提出 addon。

## Maintenance regression rule

新增 reference、外部 skill 或 addon 前，至少回答：

1. 它解决了现有 reference 无法清楚处理的什么问题？
2. 它是否改变 Agent 的决策，而不是只增加知识量？
3. 能否作为 optional companion，而不是默认依赖？
4. 是否会导致 routing overlap/context bloat？
5. 是否需要版本/许可证检查？
6. 是否新增一个真实 pressure test？

如果这些问题答不清楚，不要加入。
