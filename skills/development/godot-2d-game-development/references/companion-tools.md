# Optional Companion Tools

这是 **工具选择索引**，不是安装清单。只有环境已安装、用户要求，或当前任务明确需要时才使用/建议。

## 1. Godot MCP / live editor bridge

适合需要 Agent 真正：

- inspect scene；
- edit scene/resources；
- run/stop game；
- capture errors/output；
- simulate input；
- capture screenshot；
- iterate visually。

优先级：如果项目已有 live Godot toolchain，就用它做 evidence-driven loop，而不是只编辑文本后猜结果。

不要自动安装 MCP 或 Godot plugin。

## 2. Coding-Solo/godot-mcp

成熟、通用的 Godot MCP 选择之一。

适合：

- launch/run；
- project analysis；
- scene operations；
- debug output；
- basic screenshot/runtime tooling depending on installed version。

使用前检查实际版本和 tool list。

## 3. alexmeckes/godot-mcp + AI Bridge

更强调：

- file-based Godot manipulation；
- live scene tree；
- runtime input automation；
- screenshots；
- errors/output；
- built-in Godot docs lookup。

适合 agentic inspect -> edit -> run -> verify 闭环。

不要在一个项目里盲目同时接两个功能重叠 MCP。

## 4. GodotPrompter

适合借鉴/安装完整 Godot domain skill pack：

- project setup；
- scene architecture；
- state/components/resources；
- player/input/camera；
- animation/audio/UI；
- save/dialogue/AI；
- testing/optimization/export。

本 superskill 只吸收高价值原则，不要求用户同时安装它。

## 5. GD-Agentic-Skills

适合需要 Godot 4.7+ 深度、窄领域 reference：

- 2D physics；
- animation；
- combat；
- camera；
- Tween；
- shaders；
- resources；
- performance/tests 等。

它很大，**不要全部 preload**。需要时只打开具体 domain skill。

## 6. awesome-gamedev-agent-skills

适合跨引擎概念：

- game feel；
- UI/UX；
- camera；
- audio；
- input；
- level design；
- AI；
- save/dialogue；
- performance。

Godot API 仍以 Godot-specific reference/official docs 为准。

## 7. Agent Sprite Forge

适合 Codex 2D asset production：

- sprites；
- action strips；
- spell/projectile/impact FX；
- maps；
- props；
- transparent cleanup；
- Godot-editable map handoff。

适合“AI 生成 -> deterministic cleanup -> game-ready”。

## 8. OpenAI sprite-pipeline

适合：

```text
approved seed
-> full strip
-> normalize
-> shared anchor/scale
-> preview
```

尤其适合减少 AI animation drift。

## 9. Aseprite Pixel Plugin

适合已有 Aseprite workflow 时：

- draw/edit pixels；
- frame timing；
- animation tags；
- linked cels；
- palette/dithering；
- spritesheet/GIF export；
- Godot metadata handoff。

需要 Aseprite/MCP 环境，不要假设所有 Agent 都能调用。

## 10. SpriteCook

可选 AI pixel/game-asset generation companion，包含 Godot handoff guidance。

适合用户已经使用 SpriteCook 服务/MCP 时，不作为默认 dependency。

## 11. Deterministic image tools

ImageMagick、自有 Python script 等适合：

- crop/pad；
- alpha cleanup；
- resize；
- sheet split/compose；
- GIF preview；
- naming/batch。

几何和格式能 deterministic 处理时，不要让 image model 反复“猜”。


## 12. GUT / GdUnit4

可选测试框架：

- **GUT**：GDScript-focused、CLI、assertions、stubs/spies、JUnit XML。
- **GdUnit4**：GDScript + C#、scene runner、mocking/spying、CI integration。

选择规则：

```text
project already has one -> keep it
new project -> choose by language + Godot version + needed scene testing
pure visual/feel task -> do not install a framework just for ceremony
```

## 13. Dialogue Manager

适合 dialogue-heavy Godot 项目：

- branching dialogue；
- conditions/mutations；
- translations；
- editor/runtime workflow。

它是可选 addon，不是所有 2D 游戏的默认 dependency。
版本必须与项目 Godot 版本匹配。

## 14. LimboAI / Godot State Charts

复杂 AI/state 才考虑：

- **LimboAI**：Behavior Trees + hierarchical state machines + blackboard/debugger。
- **Godot State Charts**：hierarchical/parallel states、guards、delayed transitions、debugging。

简单 `idle/chase/attack` 不值得因此加 dependency。

## 15. Phantom Camera

当项目需要比原生 Camera2D 更复杂且可编辑的 camera workflow 时可考虑：

- multiple virtual camera setups；
- priorities/transitions；
- follow/group/path/framed behavior；
- 2D zoom；
- editor preview。

普通 follow/smoothing/shake 用原生 `Camera2D` 足够时，不要加 addon。

## Selection rule

```text
Need Godot runtime evidence?
-> Godot MCP/live tool if already available

Need AI sprite/map generation?
-> Agent Sprite Forge / image generation workflow

Need precise pixel editing/timing?
-> Aseprite toolchain

Need normalize/split/package?
-> deterministic local scripts

Need complex AI/state authoring?
-> LimboAI / State Charts only if project complexity justifies it

Need dialogue authoring?
-> Dialogue Manager only if project needs/uses it

Need automated logic/scene tests?
-> existing GUT/GdUnit4; match project Godot version

Need complex authored camera transitions?
-> Phantom Camera only if native Camera2D becomes cumbersome

Need domain knowledge only?
-> focused Skill/reference; no tool install
```
