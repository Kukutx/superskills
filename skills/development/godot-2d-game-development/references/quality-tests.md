# Godot 2D SuperSkill Routing Quality Tests

维护/评审 SuperSkill 时使用。普通游戏开发任务不要加载。

目标：验证 Agent 选对 **最小 reference 集合**，并避免 addon/tool overreach。

## Pass criteria

- 主路由正确；
- 通常只加载 1–3 个 reference；
- gameplay truth ownership 清楚；
- correctness 优先于 polish；
- 不自动安装 addon/MCP/template/test framework；
- 不引入无关 3D；
- 版本敏感内容先确认 Godot version；
- 外部 authoring/importer 不产生双 source of truth；
- 有与声明匹配的 runtime/QA 路径。

## Routing matrix

| Prompt | Expected primary references | Must avoid |
| --- | --- | --- |
| “8 向 top-down 移动 + 顺滑 Camera2D” | `movement-physics-camera` | input/addon/combat refs 全加载 |
| “键鼠切手柄时提示自动换，允许重映射” | `input-controls-accessibility` + `ui-ux` | 为 movement 重写 controller |
| “手柄 drift 导致 UI 一直切图标” | `input-controls-accessibility` | camera/game-feel |
| “dash 在 attack recovery 后吞输入” | `input-controls-accessibility` + `movement-physics-camera` | 默认安装 input addon |
| “一个挥砍扣了三次血” | `combat-system` | 先调 screen shake |
| “攻击第 4 帧才激活 hitbox” | `combat-system` + `animation-pixel` | 独立 Timer 猜 timing |
| “伤害都对，但砍起来很软” | `game-feel` + optional `audio`/`rendering-vfx-shaders` | 重写 damage architecture |
| “有时一刀扣两次血，而且打击感也很软” | `combat-system` first; `game-feel` only after correctness | 一开始同时改伤害和全部 polish |
| “大量 hit particles FPS 掉” | `performance-testing-debugging` + `rendering-vfx-shaders` after profile | 未 profile 就 ECS/MultiMesh |
| “Aseprite 已有 tags/timing，要进 Godot” | `animation-pixel` + `asset-pipeline` + optional `companion-tools` | 当 AI strip 重生成 |
| “AI 生成 attack strip 并导入 Godot” | `animation-pixel` + `asset-pipeline` + slicer | 默认装 Aseprite importer |
| “Godot 原生 terrain 已经能画地图” | `world-tilemap-level-design` | 因为发现 Better Terrain 就替换 |
| “terrain connection authoring 一直成为制作瓶颈” | `world-tilemap-level-design` + optional `companion-tools` | 无比较就自动迁移 addon |
| “我们用 LDtk 做关卡，想导入 Godot” | `world-tilemap-level-design` + `companion-tools` | Godot generated map 与 LDtk 双边手改 |
| “可编辑 top-down 森林地图，树遮挡玩家” | `world-tilemap-level-design` + `asset-pipeline` | collision/spawn 烤进 PNG |
| “敌人巡逻、发现、追逐、攻击” | `ai-navigation-procedural` | 默认 BT addon |
| “很多敌人共享 condition/action/subtree” | `ai-navigation-procedural` + optional `companion-tools` | 直接最重 AI framework |
| “Boss parallel shield/attack + locomotion state” | `core-architecture` + optional `ai-navigation-procedural` | bool soup / 无条件插件 |
| “简单 20 格 inventory + stack” | `save-inventory-progression` | 默认引入 GLoot |
| “多个容器、装备、转移、stack/split 逻辑重复很多” | `save-inventory-progression` + optional `companion-tools` | plugin state 变长期 save truth |
| “旧存档升级后 inventory 丢了” | `save-inventory-progression` | SceneTree snapshot workaround |
| “对话有复杂条件、选择、多语言” | `dialogue-localization` | story logic 塞 Button callback |
| “对话选择给物品且永久保存” | `dialogue-localization` + `save-inventory-progression` | dialogue plugin 变 inventory truth |
| “Godot 4.x GitHub Actions clean export” | `release-export-ci` | `latest` toolchain / local cache 依赖 |
| “Agent 改暂停菜单，验证手柄真的能操作” | `runtime-agent-validation` + `ui-ux` + optional input ref | 只说代码看起来正确 |
| “新项目要 menu/options/pause/credits” | `ui-ux` + optional `companion-tools` | 成熟项目硬套完整 template |
| “只切 64x64 sprite sheet” | spritesheet slicer | 主 Godot 全域 refs |
| “Godot 3D 第三人称” | route outside this skill | 套 2D reference |
| “Godot 2D 联机权威服务器和 rollback netcode” | Godot skill handles 2D gameplay only; networking architecture routes outside | 假装现有 references 覆盖 netcode |

## Behavioral pressure tests

### Existing project respect

Prompt: `这个项目已有简单 enum FSM，可以跑。只加 dash。`

Pass:
- 沿用 enum FSM；
- movement/input only；
- 不引入 State Charts/LimboAI/Beehave；
- 验证 cooldown/collision/state exit。

### Native-first input

Prompt: `我只有键盘控制，jump 从 Space 改成 J。`

Pass:
- InputMap 即可；
- 不建议 Input Helper；
- 不造新 input abstraction。

### Input Helper justified

Prompt: `设置页需要 runtime remap、最近设备检测、prompt 更新、rumble 设置。`

Pass:
- input reference；
- 先检查已有 abstraction；
- Input Helper 只能是候选；
- 不成为 gameplay truth。

### Combat vs game feel

A: `一刀有时命中两次。` -> `combat-system`。

B: `命中和伤害都对，但没重量。` -> `game-feel`；不重构 damage。

C: `一刀偶尔两次伤害，而且也没重量。`
- 先修 combat correctness；
- 用固定 reproduction 证明一击一次；
- 再进入 game-feel；
- 不同时改判定、hit-stop、shake、audio 后再猜哪项有效。

### Authored vs generated pixel assets

A: `.aseprite 有 tags 和不同 frame durations。`
- preserve metadata；
- optional Aseprite Wizard/Importality；
- 不重新 AI 生成。

B: `AI 给了 6 帧透明 PNG strip。`
- deterministic normalize/slice；
- shared anchor/scale；
- 不默认装 Aseprite importer。

### Level source ownership

Prompt: `美术在 LDtk 改地图，程序也会在 Godot 里改 TileMap。`

Pass:
- 指出双真源风险；
- 选一个 editable source；
- generated side 不手改或明确生成/patch boundary；
- clean re-import test。

### Terrain addon restraint

Prompt: `原生 terrain 目前够用，但网上说 Better Terrain 更好。`

Pass:
- 不迁移；
- 只有真实 authoring pain 才评估 addon；
- “better” 名字/热度不是 migration reason。

### Inventory addon restraint

A: `只有几个 stackable item。`
- project-native data structure。

B: `inventory 已有 container transfer、equipment、stack split、多个 UI，重复逻辑很多。`
- 可评估 GLoot；
- stable IDs/save migration 仍属项目；
- 先比较迁移成本。

### AI complexity ladder

A `idle/chase/attack` -> handwritten state。

B `共享 condition/action/subtree，可视化 BT` -> Beehave candidate。

C `BT + HSM + blackboard/debugger` -> LimboAI candidate。

D `parallel weapon mode + locomotion + status` -> State Charts candidate, not enemy BT issue。

### Save migration

Prompt: `v3 把 item id 全换了，v2 存档继续能开。`

Pass:
- explicit ID mapping/migration step；
- old fixture；
- 不用 display name 猜；
- failure 不清空 save。

### Dialogue addon restraint

5 段线性文本 -> 不推荐大型 framework。

几百分支 + conditions + mutations + 多语言 + 内容编辑器 -> 可评估 Dialogue Manager/Dialogic，并检查兼容 release。

### Clean CI

Prompt: `本地 export 正常，GitHub Actions 说资源不存在。`

Pass:
- exact Godot/templates；
- LFS/submodule/case-sensitive path/import cache；
- clean import before export；
- 不先重装所有依赖。

### Runtime evidence

Prompt: `我改了 HUD，确认修好了吧？`

Pass:
- live tool 可用则 run/resize/input/screenshot；
- 无 live tool 明确 static vs runtime；
- 不虚构“已经看过画面”。

### MCP restraint

`只改一个 GDScript 常量` -> 不自动安装 MCP。

`Agent 要自动走菜单/按按钮/截图验证 UI` -> runtime validation + optional single MCP selection。

### Candidate-source restraint

Prompt: `这个新仓库写着支持 Godot 4.7，有一堆 AI skills，要不要全部收录？`

Pass:
- 检查实际采用、维护、独特价值、与现有 source overlap；
- 宣称“支持最新版本”不是收录理由；
- 无新 decision value 就拒绝纳入 primary sources。

## Distribution integration tests

这些测试用于确保 Skill 不只“文件存在”，而是能从 Kukutx 的入口被选中。

### Project instructions precedence

Prompt: `这个 Godot 2D 项目攻击会重复扣血，帮我 debug。`

Pass:
- `godot-2d-game-development` primary；
- `combat-system` primary reference；
- generic `bug-diagnosis` 最多作为补充，不抢 domain route。

### Knowledge pack routing

Prompt: `帮我做 Godot 像素角色攻击和 hit-stop。`

Pass:
- Godot 2D skill primary；
- animation/combat/game-feel 按实际问题渐进加载；
- 不因为 compact knowledge pack 缺全部 reference 就退回 generic implementation plan。

### Spritesheet-only routing

Prompt: `把这个 64x64、6 帧一行的 PNG 切成 attack_00..05。`

Pass:
- `game-dev-spritesheet-slicer` primary；
- 不加载完整 Godot 2D runtime knowledge。

### Runtime knowledge hygiene

Pass:
- `sources.md` / `quality-tests.md` / changelog 不作为普通 runtime knowledge 必选文件；
- compatibility indexes 不主动上传/加载；
- routing 不靠“把所有文件塞进上下文”解决。

## Maintenance regression rule

新增 reference/source/addon 前回答：

1. 现有 reference 处理不了的具体问题是什么？
2. 它改变哪个 Agent 决策？
3. 是 knowledge source、optional tool 还是 default dependency？
4. 会不会 routing overlap/context bloat？
5. Godot version/license/maintenance/security 是否检查？
6. 是否形成 source-of-truth 双写？
7. 是否有真实 pressure test？
8. 删除它后是否仍能用原生 Godot 做基本任务？

答不清楚就不加入。