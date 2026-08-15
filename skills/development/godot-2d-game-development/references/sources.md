# Upstream Sources and Maintenance Notes

维护本 SuperSkill 时使用。普通开发任务不要加载。

原则：**synthesis, not bulk copy**。

- 抽取 decision rules、anti-patterns、validation loops、2D-specific knowledge。
- 精确 API 以项目实际 Godot 版本和官方文档为准。
- 外部 addon/tool 不作为隐式 dependency。
- 不复制外部仓库大段文本或脚本；需要代码时先检查 license。

## First-party Godot sources

### Godot official documentation

最高优先级的 API/version source。实施版本敏感行为前查与项目 Godot 版本匹配的文档。

### godotengine/godot-demo-projects

- URL: `https://github.com/godotengine/godot-demo-projects`
- License: MIT

Use for canonical working examples of native Godot behavior, including 2D physics/navigation/tilemaps/animation/shaders/UI/input/saving and other engine features.

Maintenance rule:

```text
uncertain native pattern
-> official docs
-> matching official demo
-> third-party pattern
```

不要为了复制 demo architecture 而覆盖项目已有合理结构。

### godotengine/awesome-godot

- URL: `https://github.com/godotengine/awesome-godot`
- License: CC-BY-4.0 for the list

这是 **candidate discovery index**，不是 addon quality/compatibility guarantee。

发现候选后必须打开该 addon 自己的 repo/docs，检查 Godot version、license、maintenance、overlap。

## Primary agent-skill sources

### thedivergentai/GD-Agentic-Skills

- URL: `https://github.com/thedivergentai/GD-Agentic-Skills`
- License: LGPL-3.0 — importing substantial text/code requires license review

Use selectively for Godot-specific physics、animation、combat、camera、Tween、shader、resources、audio、performance/testing 等窄领域实践。

库很大，不 preload 全部。

### jame581/GodotPrompter

- URL: `https://github.com/jame581/GodotPrompter`
- License: MIT

Use for concise Godot domain decomposition and agent routing across project/scene/resource/input/UI/save/AI/testing/export topics.

### gamedev-skills/awesome-gamedev-agent-skills

- URL: `https://github.com/gamedev-skills/awesome-gamedev-agent-skills`
- License: check repository/current file

Use for engine-neutral game feel、UI/UX、input、camera、audio、AI、level design、save/dialogue、performance principles。

### openai/plugins — game-studio sprite-pipeline

- URL: `https://github.com/openai/plugins`
- Relevant path: `plugins/game-studio/skills/sprite-pipeline/`

Use for approved seed -> whole strip -> shared scale/anchor -> normalize -> preview workflow。

### 0x0funky/agent-sprite-forge

- URL: `https://github.com/0x0funky/agent-sprite-forge`
- License: MIT

Use for game-ready sprite/FX/map asset production, deterministic cleanup and engine handoff。

### willibrandon/pixel-plugin

- URL: `https://github.com/willibrandon/pixel-plugin`
- License: MIT

Use for Aseprite-oriented frame timing/tags/linked cels/pixel editing/export concepts。

## Optional runtime / MCP tools

### Coding-Solo/godot-mcp

- URL: `https://github.com/Coding-Solo/godot-mcp`

General Godot project/run/debug MCP candidate. Check current tool set before claiming runtime capabilities.

### alexmeckes/godot-mcp

- URL: `https://github.com/alexmeckes/godot-mcp`

Candidate for richer editor/file + optional live bridge workflows.

### Erodenn/godot-mcp-runtime

- URL: `https://github.com/Erodenn/godot-mcp-runtime`
- License: MIT

Newer runtime-focused zero-footprint candidate. Evaluate feature/security/tooling-policy fit before use; maturity is lower than older Godot tooling.

## Optional input ecosystem

### nathanhoad/godot_input_helper

- URL: `https://github.com/nathanhoad/godot_input_helper`
- License: MIT

Use when native InputMap plumbing becomes repetitive for device detection、binding queries/changes、joypads、rumble。Not a default dependency.

## Optional AI / state ecosystem

### bitbrain/beehave

- URL: `https://github.com/bitbrain/beehave`
- License: MIT

Behavior-tree addon. Good middle step when handwritten state is too limited but a larger BT+HSM stack is unnecessary.

### limbonaut/limboai

- URL: `https://github.com/limbonaut/limboai`

Behavior Trees + HSM + blackboard/debugger for genuinely complex behavior sets. Check Godot-version compatibility.

### derkork/godot-statecharts

- URL: `https://github.com/derkork/godot-statecharts`
- License: MIT

Hierarchical/parallel gameplay states when simple FSM state explosion becomes a real problem。

## Optional pixel-source importers

### viniciusgerevini/godot-aseprite-wizard

- URL: `https://github.com/viniciusgerevini/godot-aseprite-wizard`
- License: MIT

Aseprite-centric Godot importer workflow for animation assets。

### nklbdev/godot-4-importality

- URL: `https://github.com/nklbdev/godot-4-importality`
- License: MIT

Universal raster/animation importer pack across Aseprite/LibreSprite and other editors. Useful when project source formats are broader than Aseprite alone。

## Optional dialogue ecosystem

### nathanhoad/godot_dialogue_manager

- URL: `https://github.com/nathanhoad/godot_dialogue_manager`
- License: MIT

Mature dialogue authoring/runtime option. **Match release to project Godot version; do not default to an unreleased/preview major.**

### dialogic-godot/dialogic

- URL: `https://github.com/dialogic-godot/dialogic`

Feature-heavier narrative/visual-novel-oriented option. Check current Godot compatibility before choosing。

## Optional camera ecosystem

### ramokz/phantom-camera

- URL: `https://github.com/ramokz/phantom-camera`
- License: MIT

Use when authored multi-camera priority/transitions/group/path/framed follow justify more than native Camera2D。

## Optional testing ecosystem

### bitwes/Gut

- URL: `https://github.com/bitwes/Gut`
- License: MIT

GDScript-focused tests/CLI/assertions/stubs/spies/JUnit。

### godot-gdunit-labs/gdUnit4

- URL: `https://github.com/godot-gdunit-labs/gdUnit4`
- License: MIT

GDScript + C# tests, scenes, mocking/spying, CLI/CI. **Version must match Godot version.**

## Optional project-shell/template

### Maaack/Godot-Game-Template

- URL: `https://github.com/Maaack/Godot-Game-Template`
- License: MIT

Useful for a new project that wants common menu/options/pause/credits/loading/settings shell. Do not transplant a whole template into a mature project just to standardize it。

## Optional export / CI

### firebelley/godot-export

- URL: `https://github.com/firebelley/godot-export`
- License: MIT

GitHub Action-oriented Godot export workflow。

### abarichello/godot-ci

- URL: `https://github.com/abarichello/godot-ci`

Docker/CI Godot export/deploy option. Direct Godot CLI remains valid when simpler。

## Maintenance policy

Before adding a new source/addon:

1. Is it first-party, broadly used, or uniquely useful?
2. What concrete Agent decision changes because of it?
3. Does an existing reference already solve the same problem?
4. Is it optional rather than a default dependency?
5. Is Godot-version compatibility explicit?
6. Have license/maintenance/security implications been checked?
7. Is there a routing pressure test for it?

If not, do not add it.

## Licensing note

Do not paste substantial upstream text/code without checking and complying with its license. Prefer independently written synthesis with source attribution。