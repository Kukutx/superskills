# Optional Companion Tools

这是 **选择索引，不是安装清单**。默认先用 Godot 原生能力 + 项目已有工具；只有当前问题明确受益时才考虑外部依赖。

## First choice before third-party code

需要确认 Godot-native pattern/API 时：

```text
project actual version/pattern
-> matching Godot official docs
-> matching godotengine/godot-demo-projects example
-> focused third-party skill/addon
```

`godotengine/awesome-godot` 只用于发现候选。随后打开候选自己的 repo/docs 检查 version、license、maintenance、overlap。

## Candidate evaluation

不要只看 stars、README 宣称或“支持最新 Godot”。采用前至少检查：

- 最近是否仍维护；
- 是否有明确 Godot 4.x / 当前项目版本支持；
- release/tag/branch 是否清楚；
- license 是否可接受；
- docs/examples 是否足够；
- issue/compatibility 风险；
- 是否与现有 addon 重叠；
- 是否会产生新的 source of truth；
- 是否容易升级或移除。

热度是辅助信号，不是技术决策。

## 1. Agent / MCP runtime loop

### Coding-Solo/godot-mcp

通用 Godot project/run/debug/file workflow candidate。使用前确认当前 tool list，不假设 screenshot/input/live-scene 全部存在。

### alexmeckes/godot-mcp

适合更丰富的 editor/file + optional live bridge workflow，例如 scene tree、runtime input、screenshots、errors/output。

### Erodenn/godot-mcp-runtime

较新的 runtime-focused、zero-footprint 方向。适合临时 runtime interaction/screenshot/input validation；采用前检查当前版本、feature/security model 和项目 tooling policy。

Selection:

```text
existing bridge -> reuse it
basic project/run/debug -> evaluate Coding-Solo
rich editor + live bridge -> evaluate alexmeckes
runtime-focused temporary validation -> evaluate Erodenn
no runtime need -> no MCP
```

不要同时接多个高度重叠 MCP。

## 2. Godot skill/reference ecosystems

- **GD-Agentic-Skills**：深 Godot 窄领域 reference；只读当前 domain。
- **GodotPrompter**：Godot 4.x domain decomposition / agent routing reference。
- **awesome-gamedev-agent-skills**：engine-neutral game feel、UI、input、camera、audio、AI、level design、save/dialogue/performance。

这些是知识来源，不是项目 dependency。

## 3. AI / state tools

### Beehave

适合行为已经需要 reusable Behavior Tree、可视化/debug，但不需要更重 BT+HSM all-in-one stack。

### LimboAI

适合复杂 BT + hierarchical state machines + blackboard/debugger。

### Godot State Charts

适合 hierarchical/parallel gameplay state、guards/delayed transitions、手写 FSM state explosion。

```text
idle/chase/attack -> handwritten state
medium reusable BT -> Beehave candidate
complex BT + HSM/blackboard -> LimboAI candidate
hierarchical/parallel gameplay state -> State Charts candidate
```

已有一个就沿用，不建第二套 state framework。

## 4. Input Helper

`nathanhoad/godot_input_helper` 适合 active device detection、binding lookup/change、joypad differences、rumble、GDScript/C# helper workflow。

原生 InputMap 足够就不加；已有 input abstraction 就不再叠第二套。

## 5. Pixel / authored asset import

### Aseprite Wizard

Aseprite-centric pipeline，把 authored animation 导入 SpriteFrames / AnimatedSprite2D / AnimationPlayer 等。

### Importality

多 raster-animation source editor 的统一 importer candidate，例如 Aseprite/LibreSprite、Krita、Pencil2D、Piskel、Pixelorama。

```text
AI-generated PNG strip -> deterministic normalize/slice
Aseprite-only source -> Aseprite Wizard candidate
multiple raster source editors -> Importality candidate
```

不要同时装重叠 importer。

## 6. AI sprite / map generation

- **Agent Sprite Forge**：sprites、action strips、FX、maps、props、cleanup、Godot handoff。
- **OpenAI sprite-pipeline**：approved seed -> full strip -> normalize -> preview。
- **Aseprite Pixel Plugin**：如果 Agent 已有 Aseprite toolchain，可做实际 pixel edits/timing/tags/palette/export。
- **SpriteCook**：项目已经使用该服务/tooling 时再接。

## 7. Deterministic image tools

ImageMagick / Python / project scripts 适合 crop/pad、alpha cleanup、normalize、split/compose、preview、naming/batch。

几何/格式能 deterministic 处理时，不让 image model 反复猜。

## 8. Level / terrain authoring

### Better Terrain

`Portponky/better-terrain` 是 Godot 4 terrain addon candidate。

只在 native TileSet terrain authoring 已经成为持续 production pain 时评估：

```text
native terrain works -> keep native
terrain connection/painting repeatedly slows production -> evaluate Better Terrain
```

不要同时维护两套 terrain authoring truth。

### LDtk importer

如果团队明确用 LDtk 作为 level source，可评估 Godot 4 LDtk importer。

原则：

```text
LDtk editable source -> importer -> generated Godot representation
```

不要 source 和 generated TileMap 两边手改形成双真源。先检查当前 Godot/LDtk/importer compatibility。

## 9. Inventory

### GLoot

`peter-kish/gloot` 是成熟的 Godot inventory system candidate。

适合 inventory domain 已经包含大量通用 container/stack/transfer/equipment 逻辑，项目自写方案开始重复复杂。

简单 item list + stack/equip 继续项目原生 data structure 通常更透明。

使用 addon 也不改变：stable project IDs、save migration、UI-not-truth 等边界。

## 10. Testing

### GUT

GDScript-oriented tests/CLI/assertions/stubs/spies/JUnit。

### GdUnit4

GDScript + C#、scene tests、mocking/spying、CLI/CI。

```text
project already has one -> keep it
new project -> choose by language + scene-test needs + Godot version
visual-only task -> do not install testing framework for ceremony
```

测试框架版本必须匹配项目 Godot 版本。

## 11. Dialogue

### Dialogue Manager

适合 branching/conditions/mutations/translation/editor/runtime workflow。按项目 Godot version 选兼容 release，不把 preview next-major 自动当生产默认。

### Dialogic

更适合 visual-novel / character-heavy / timeline-oriented narrative tooling。简单 dialogue 不需要这么重。

已有 narrative framework 就沿用。

## 12. Camera

### Phantom Camera

当原生 Camera2D 因 multiple authored virtual cameras、priority/transitions、group/path/framed follow 等需求开始难维护时考虑。

普通 follow/smoothing/shake 用 Camera2D。

## 13. Game shell / bootstrap

### Maaack/Godot-Game-Template

适合**新项目**快速获得 main menu、options、pause、credits、scene/loading flow 等标准 shell。

不要把完整 template 强行移植进成熟项目；只借鉴需要的 pattern/component。

## 14. Export / CI

- **firebelley/godot-export**：GitHub Actions-oriented Godot export candidate。
- **godot-ci**：Docker/CI export/deploy candidate。
- **Direct Godot CLI**：简单 pipeline 常常最透明、依赖最少。

见 `release-export-ci.md`。

## Global selection rule

加入 addon/tool 前回答：

1. 原生/已有方案具体哪里不够？
2. 它减少什么真实复杂度？
3. Godot version 兼容吗？
4. license/maintenance/security 状态可接受吗？
5. 是否和现有 addon 重叠？
6. 删除/升级成本是什么？
7. 是否产生 source-of-truth 双写？
8. 用户允许新增依赖了吗？

答不清楚就不要安装。