# Optional Companion Tools

这是 **选择索引，不是安装清单**。默认先用 Godot 原生能力 + 项目已有工具；只有当前问题明确受益时才考虑外部依赖。

## First choice before third-party code

需要确认 Godot-native pattern/API 时，优先顺序：

```text
project's actual version/pattern
-> matching Godot official docs
-> matching godotengine/godot-demo-projects example
-> focused third-party skill/addon
```

`godotengine/awesome-godot` 适合发现候选，不直接作为技术真源；找到候选后再检查其自己的 repo/docs/version/license。

## 1. Agent / MCP runtime loop

### Coding-Solo/godot-mcp

适合成熟、较通用的 Godot project/run/debug/file workflow。

选择它时仍要先看当前 tool list；不要因为项目叫 MCP 就假设支持 screenshot/input/live-scene 全部能力。

### alexmeckes/godot-mcp

适合需要更丰富的 editor/file + optional live bridge workflow，例如 scene tree、runtime input、screenshots、errors/output 等。

采用其 bridge 前确认项目是否允许写入/启用相应 addon。

### Erodenn/godot-mcp-runtime

较新的 runtime-focused、zero-footprint 方向，适合需要实际 runtime input/screenshot/interaction verification，又不希望长期保留 project plugin 时评估。

它不是默认首选：使用前检查当前版本、feature set、security model 和项目 tooling policy。

### Selection

```text
existing Godot bridge -> reuse it
basic project/run/debug workflow -> evaluate Coding-Solo
rich editor + live bridge -> evaluate alexmeckes
runtime-focused temporary interaction -> evaluate Erodenn
no runtime need -> do not install MCP
```

不要同时接两个功能高度重叠的 MCP。

## 2. Godot skill/reference ecosystems

### GD-Agentic-Skills

深 Godot 领域 reference：physics、animation、combat、camera、Tween、shader、resource、performance 等。

库很大，只读当前 domain，不 preload 全部。

### GodotPrompter

活跃的 Godot 4.x agent skill framework，适合参考其 domain decomposition、project/scene/resource/input/UI/save/AI/testing/export patterns。

本 SuperSkill 吸收有用决策，不要求同时安装。

### awesome-gamedev-agent-skills

适合 engine-neutral 的 game feel、UI/UX、camera、audio、input、AI、level design、save/dialogue/performance。

Godot API 仍由 Godot source/docs 决定。

## 3. AI / state tools

默认从简单 state logic 开始。

### Beehave

`bitbrain/beehave` 是成熟的 Godot behavior-tree addon，适合：

- 行为已经需要可复用 BT；
- 希望 Godot scene-based authoring/debug；
- 不需要更重的 BT + HSM all-in-one stack。

### LimboAI

适合更复杂：

- reusable Behavior Trees；
- hierarchical state machines；
- blackboard/debugger；
- 大量复杂 enemy behavior。

### Godot State Charts

适合 gameplay/state 本身出现：

- hierarchical states；
- parallel/orthogonal states；
- guarded/delayed transitions；
- hand-written FSM state explosion。

### Selection

```text
idle/chase/attack -> handwritten state
medium reusable BT -> consider Beehave
complex BT + HSM/blackboard -> consider LimboAI
hierarchical/parallel gameplay state -> consider State Charts
```

已有项目使用其中一个就沿用，不建第二套 state framework。

## 4. Input Helper

`nathanhoad/godot_input_helper` 适合需要重复处理：

- active device detection；
- action binding lookup/change；
- joypad differences；
- rumble；
- GDScript/C# input helper workflow。

简单项目原生 InputMap 足够就不要加。

Input prompt icon addon 属于 UI convenience，不要让 glyph library 变成 gameplay input truth。

## 5. Pixel / authored asset import

### Aseprite Wizard

`viniciusgerevini/godot-aseprite-wizard` 适合 Aseprite-centric pipeline，把 Aseprite animation 导入 SpriteFrames / AnimatedSprite / AnimationPlayer 等 Godot 资产。

### Importality

`nklbdev/godot-4-importality` 更适合多编辑器/多 raster-animation source，例如 Aseprite/LibreSprite、Krita、Pencil2D、Piskel、Pixelorama，并希望统一 importer workflow。

### Selection

```text
AI-generated PNG strip -> deterministic normalize/slice pipeline
Aseprite-only authored source -> consider Aseprite Wizard
multiple raster animation source editors -> consider Importality
```

不要同时装两个重叠 importer，除非项目已有明确分工。

## 6. AI sprite / map generation

### Agent Sprite Forge

适合 Codex 2D asset production：sprites、action strips、spell/projectile/impact FX、maps、props、cleanup 与 Godot handoff。

### OpenAI sprite-pipeline

适合：

```text
approved seed
-> full action strip
-> normalize shared scale/anchor
-> preview
```

### Aseprite Pixel Plugin

如果 Agent 已经有 Aseprite toolchain，可用于实际 pixel edits、frame timing、tags、linked cels、palette 和 export。

### SpriteCook

可选外部 pixel/game-asset generation companion；项目已经使用时再接。

## 7. Deterministic image tools

ImageMagick / Python / existing project tools 用于：

- crop/pad；
- alpha cleanup；
- normalize scale/anchor；
- split/compose；
- GIF/preview；
- naming/batch。

几何/格式能 deterministic 处理时，不让 image model 反复猜。

## 8. Testing

### GUT

GDScript-oriented、CLI/assertion/stub/spy/JUnit workflow。

### GdUnit4

GDScript + C#、scene tests、mocking/spying、CLI/CI workflow。

选择：

```text
project already has one -> keep it
new project -> choose by language + scene-test needs + Godot version
visual feel-only task -> do not install a framework for ceremony
```

**测试框架版本必须匹配项目 Godot 版本。**

## 9. Dialogue

### Dialogue Manager

成熟的 branching/conditions/mutations/translation/editor/runtime workflow。

按 Godot 版本选择兼容 release；不要把正在开发的 next-major/preview 自动当生产默认。

### Dialogic

更适合 visual-novel / character-heavy / timeline-oriented narrative tooling。简单对话通常不需要这么重。

已有 narrative framework 就沿用。

## 10. Camera

### Phantom Camera

当原生 Camera2D 开始因以下需求变得难维护时考虑：

- multiple authored virtual cameras；
- priority/transitions；
- group/path/framed follow；
- editor-driven camera composition。

普通 follow/smoothing/shake 继续用 Camera2D。

## 11. Game shell / bootstrap

### Maaack/Godot-Game-Template

适合**新项目**想快速获得标准 game shell：

- main menu；
- options；
- pause；
- credits；
- scene loader/loading flow；
- settings/common helpers。

不要把完整 template 强行移植进已经成型的项目。成熟项目只借鉴需要的 pattern/component。

## 12. Export / CI

### firebelley/godot-export

适合 GitHub Actions 中按 Godot export presets 构建多平台 artifact。

### godot-ci

适合 Docker/CI-based Godot export/deploy workflow。

### Direct Godot CLI

简单 pipeline 往往最透明，也最少 dependency。

具体选择见 `release-export-ci.md`。

## 13. Emerging juice/effect addons

如果项目明确想让 designer 用 graph/library authoring 大量 juice effects，可以调研当前 Godot Asset Library/awesome-godot 中的 effect tools。

默认仍使用 Tween + Camera2D + particles/shader/audio 组合，因为更透明、依赖更少。

不要因为 addon 有很多预制效果就替代项目已有清楚的 event/feedback architecture。

## Global selection rule

加入任何 addon/tool 前回答：

1. 当前原生/已有方案具体哪里不够？
2. 这个工具减少什么真实复杂度？
3. Godot 版本兼容吗？
4. license/maintenance 状态可接受吗？
5. 会不会与现有 addon 重叠？
6. 删除/升级它的成本是什么？
7. 用户明确允许新增依赖了吗？

答不清楚就不要安装。