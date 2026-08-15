# Upstream Sources and Maintenance Notes

维护本 SuperSkill 时使用。普通开发任务不要加载。

原则：**synthesis, not bulk copy**。

- 抽取 decision rules、anti-patterns、validation loops、2D-specific knowledge。
- 精确 API 以项目实际 Godot 版本和官方文档为准。
- 外部 addon/tool 不作为隐式 dependency。
- 不复制外部仓库大段文本或脚本；需要代码时先检查 license。

## First-party Godot sources

### Godot official documentation

最高优先级的 API/version source。

### godotengine/godot-demo-projects

- URL: `https://github.com/godotengine/godot-demo-projects`
- License: MIT

Native 2D physics/navigation/tilemaps/animation/shaders/UI/input/save 等 working examples。

```text
uncertain native pattern
-> matching official docs
-> matching official demo
-> third-party pattern
```

### godotengine/awesome-godot

- URL: `https://github.com/godotengine/awesome-godot`
- License: CC-BY-4.0 for the list

只作为 candidate discovery index。找到项目后打开其 primary repo/docs 检查 Godot version、license、maintenance、overlap。

## Primary agent-skill sources

### thedivergentai/GD-Agentic-Skills
- URL: `https://github.com/thedivergentai/GD-Agentic-Skills`
- License: LGPL-3.0
- Use: narrow Godot physics/animation/combat/camera/Tween/shader/resources/audio/performance/testing knowledge。

### jame581/GodotPrompter
- URL: `https://github.com/jame581/GodotPrompter`
- License: MIT
- Use: Godot 4.x domain decomposition and agent routing。

### gamedev-skills/awesome-gamedev-agent-skills
- URL: `https://github.com/gamedev-skills/awesome-gamedev-agent-skills`
- Use: engine-neutral game feel/UI/input/camera/audio/AI/level/save/dialogue/performance principles。

### openai/plugins — sprite-pipeline
- URL: `https://github.com/openai/plugins`
- Use: approved seed -> whole strip -> shared scale/anchor -> normalize -> preview。

### 0x0funky/agent-sprite-forge
- URL: `https://github.com/0x0funky/agent-sprite-forge`
- License: MIT
- Use: game-ready sprite/FX/map production and deterministic handoff。

### willibrandon/pixel-plugin
- URL: `https://github.com/willibrandon/pixel-plugin`
- License: MIT
- Use: Aseprite timing/tags/linked cels/pixel editing/export concepts。

## Runtime / MCP candidates

### Coding-Solo/godot-mcp
- URL: `https://github.com/Coding-Solo/godot-mcp`
- Use: general project/run/debug MCP; inspect current tools before claiming capabilities。

### alexmeckes/godot-mcp
- URL: `https://github.com/alexmeckes/godot-mcp`
- Use: richer editor/file + optional live bridge candidate。

### Erodenn/godot-mcp-runtime
- URL: `https://github.com/Erodenn/godot-mcp-runtime`
- License: MIT
- Use: newer runtime-focused zero-footprint validation candidate; evaluate maturity/security/policy before use。

## Input

### nathanhoad/godot_input_helper
- URL: `https://github.com/nathanhoad/godot_input_helper`
- License: MIT
- Use: device detection、binding query/change、joypad differences、rumble when native plumbing becomes repetitive。

## AI / state

### bitbrain/beehave
- URL: `https://github.com/bitbrain/beehave`
- License: MIT
- Use: medium-complex reusable Behavior Trees。

### limbonaut/limboai
- URL: `https://github.com/limbonaut/limboai`
- Use: complex BT + HSM + blackboard/debugger; check Godot compatibility。

### derkork/godot-statecharts
- URL: `https://github.com/derkork/godot-statecharts`
- License: MIT
- Use: hierarchical/parallel gameplay states。

## Pixel / raster import

### viniciusgerevini/godot-aseprite-wizard
- URL: `https://github.com/viniciusgerevini/godot-aseprite-wizard`
- License: MIT
- Use: Aseprite-centric animation import to Godot assets。

### nklbdev/godot-4-importality
- URL: `https://github.com/nklbdev/godot-4-importality`
- License: MIT
- Use: multi-editor raster/animation importer workflow。

## Level / terrain authoring

### Portponky/better-terrain
- URL: `https://github.com/Portponky/better-terrain`
- License: Unlicense
- Use: optional Godot 4 terrain authoring when native terrain workflow is a demonstrated production bottleneck。

### heygleeson/godot-ldtk-importer
- URL: `https://github.com/heygleeson/godot-ldtk-importer`
- License: MIT
- Use: projects that deliberately use LDtk as level source; check current Godot/LDtk compatibility and generated-file ownership。

## Inventory

### peter-kish/gloot
- URL: `https://github.com/peter-kish/gloot`
- License: MIT
- Use: larger/repetitive inventory domain; not needed for simple item lists/stacks。

## Dialogue

### nathanhoad/godot_dialogue_manager
- URL: `https://github.com/nathanhoad/godot_dialogue_manager`
- License: MIT
- Use: mature branching/conditions/mutations/translation authoring; match release to project Godot version, do not default to preview next-major。

### dialogic-godot/dialogic
- URL: `https://github.com/dialogic-godot/dialogic`
- Use: feature-heavier narrative/visual-novel workflow; check current compatibility。

## Camera

### ramokz/phantom-camera
- URL: `https://github.com/ramokz/phantom-camera`
- License: MIT
- Use: authored multi-camera priority/transitions/group/path/framed follow beyond simple Camera2D。

## Testing

### bitwes/Gut
- URL: `https://github.com/bitwes/Gut`
- License: MIT
- Use: GDScript-focused tests/CLI/assertions/stubs/spies/JUnit。

### godot-gdunit-labs/gdUnit4
- URL: `https://github.com/godot-gdunit-labs/gdUnit4`
- License: MIT
- Use: GDScript+C# tests/scenes/mocking/CI; version must match Godot。

## Project shell

### Maaack/Godot-Game-Template
- URL: `https://github.com/Maaack/Godot-Game-Template`
- License: MIT
- Use: new project standard menu/options/pause/credits/loading/settings shell; don't transplant wholesale into mature projects。

## Export / CI

### firebelley/godot-export
- URL: `https://github.com/firebelley/godot-export`
- License: MIT
- Use: GitHub Action-oriented export workflow。

### abarichello/godot-ci
- URL: `https://github.com/abarichello/godot-ci`
- Use: Docker/CI export/deploy option; direct Godot CLI is often simpler。

## Candidate rejection / restraint

“包含很多 skills”或“宣称支持最新 Godot”本身不是纳入理由。低采用、信息重复、维护不明确、只包装官方文档但不改变 Agent 决策的库，可以作为临时研究材料，但不进入 primary source list。

## Maintenance policy

新增 source/addon 前回答：

1. first-party、broadly used 或 uniquely useful 吗？
2. 改变哪个具体 Agent decision？
3. 现有 reference 是否已覆盖？
4. 能否保持 optional？
5. Godot version / license / maintenance / security 是否检查？
6. 会不会形成双 source of truth？
7. 是否新增 routing pressure test？

答不清楚就不加入。

## Licensing note

不粘贴 substantial upstream text/code。优先独立撰写 synthesis + attribution；若未来导入代码/脚本，先遵守 upstream license。