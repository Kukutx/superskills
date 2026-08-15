# Upstream Sources and Maintenance Notes

这个文件只用于维护 superskill。正常开发任务不需要加载。

本 SuperSkill 采用 **synthesis, not bulk copy**：

- 抽取 decision rules、anti-patterns、validation loops、2D-specific knowledge。
- 删除营销文案、重复教程、与 Godot 2D 无关内容。
- 精确 API 以项目实际 Godot 版本和 Godot 官方文档为准。
- 外部工具不作为隐式 dependency。

## Primary skill sources

### thedivergentai/GD-Agentic-Skills

- URL: `https://github.com/thedivergentai/GD-Agentic-Skills`
- License: LGPL-3.0 (check current upstream before importing code)

Use for:

- Godot-specific architecture；
- CharacterBody2D / physics；
- animation / Tween；
- combat；
- Camera2D；
- particles / shaders；
- Resources / signals / state；
- audio；
- performance/testing。

Note: upstream is large; follow progressive disclosure. Do not copy the whole library into superskills.

### jame581/GodotPrompter

- URL: `https://github.com/jame581/GodotPrompter`
- License: MIT

Use for:

- concise Godot domain decomposition；
- project/scene/component/resource patterns；
- player/input/camera；
- UI/responsive HUD；
- save/dialogue/AI；
- debugging/testing/optimization/export。

Useful maintenance idea: keep the entry skill small and move depth to references.

### gamedev-skills/awesome-gamedev-agent-skills

- URL: `https://github.com/gamedev-skills/awesome-gamedev-agent-skills`
- License: Apache-2.0 (check the specific file/repo state when reusing material)

Use for engine-neutral concepts:

- game-feel；
- game-ui-ux；
- camera-systems；
- input-systems；
- audio-design；
- level-design；
- game-ai；
- save/dialogue；
- shader programming；
- performance optimization。

Godot API details must come from Godot-specific sources/docs.

### openai/plugins — game-studio sprite-pipeline

- URL: `https://github.com/openai/plugins`
- Relevant path: `plugins/game-studio/skills/sprite-pipeline/`

Use for:

- approved seed frame；
- whole-strip generation；
- shared scale；
- shared anchor；
- normalization；
- preview before engine import。

### 0x0funky/agent-sprite-forge

- URL: `https://github.com/0x0funky/agent-sprite-forge`
- License: MIT

Use for:

- sprites + FX；
- editable 2D maps；
- transparent props；
- deterministic cleanup；
- engine handoff。

### willibrandon/pixel-plugin

- URL: `https://github.com/willibrandon/pixel-plugin`
- License: MIT

Use for Aseprite-oriented concepts:

- frame duration；
- animation tags；
- linked cels；
- pixel palette/dithering；
- export metadata。

### Yuki001/game-dev-skills — game-architect

- URL: `https://github.com/Yuki001/game-dev-skills`

Use selectively for:

- choose architecture by problem complexity；
- system boundaries；
- effect/feedback；
- scene/UI/data architecture；
- avoid one universal paradigm。

## Optional tool sources

### Coding-Solo/godot-mcp

- URL: `https://github.com/Coding-Solo/godot-mcp`
- License: MIT

General Godot MCP for run/editor/project/debug workflows.

### alexmeckes/godot-mcp

- URL: `https://github.com/alexmeckes/godot-mcp`

Godot MCP + optional AI Bridge with live scene tree, runtime input, screenshots and errors/output.

### SpriteCook/skills

- URL: `https://github.com/SpriteCook/skills`
- License: MIT (check current upstream)

Optional external pixel/game-asset generation and Godot handoff.


## Optional Godot ecosystem references

These are **tools/addons, not knowledge dependencies**.

### bitwes/Gut

- URL: `https://github.com/bitwes/Gut`
- License: MIT

Use when a GDScript project needs automated unit/integration tests and already uses GUT or chooses it deliberately. Match GUT release/branch to the project's Godot version.

### godot-gdunit-labs/gdUnit4

- URL: `https://github.com/godot-gdunit-labs/gdUnit4`
- License: MIT

Use when GDScript/C# scene-aware testing, mocking/spying, runner tooling, or CI integration is useful. Match release to Godot version.

### nathanhoad/godot_dialogue_manager

- URL: `https://github.com/nathanhoad/godot_dialogue_manager`
- License: MIT

Optional for dialogue-heavy projects; do not make it a default dependency.

### limbonaut/limboai

- URL: `https://github.com/limbonaut/limboai`
- License: MIT-style

Optional for behavior trees + hierarchical state machines when hand-written AI becomes genuinely complex.

### derkork/godot-statecharts

- URL: `https://github.com/derkork/godot-statecharts`
- License: MIT

Optional for hierarchical/parallel state modeling when a simple FSM no longer remains clear.

### ramokz/phantom-camera

- URL: `https://github.com/ramokz/phantom-camera`
- License: MIT

Optional for authored multi-camera follow/framing/transition workflows; native Camera2D remains the default for simpler games.

## Maintenance policy

When updating:

1. Check current Godot stable docs/API.
2. Check upstream skill changes only for relevant domains.
3. Add only knowledge that changes an Agent decision or prevents a real failure.
4. Keep examples minimal.
5. Avoid duplicated guidance across references.
6. Keep routing triggers explicit.
7. Test references with realistic prompts.
8. Prefer runtime evidence over static confidence.

## Licensing note

Do not paste large upstream sections verbatim into this repository. Keep this repository's text independently written and cite upstream sources. If future maintenance imports scripts or substantial text, inspect and comply with that upstream project's license first.
