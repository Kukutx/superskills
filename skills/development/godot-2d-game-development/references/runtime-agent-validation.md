# Runtime Agent Validation Reference

用于 Agent 修改 Godot 后的 **evidence-driven verification**：scene inspection、run/stop、runtime input、screenshots、errors/output、UI flow、visual regression 与可重复 smoke tests。

它不是 MCP 安装指南。没有 live tooling 时仍然给出 editor/CLI/manual fallback。

## 1. Core loop

优先：

```text
inspect actual project
-> make smallest change
-> run relevant scene/game
-> exercise the changed behavior
-> capture errors/output + visible result
-> compare with expected behavior
-> fix
```

不要“代码编译/parse 通过”就宣布视觉或交互任务完成。

## 2. Match evidence to the claim

| Claim | Useful evidence |
| --- | --- |
| scene/resource loads | no parse/resource errors |
| button works | focus/click/input causes expected transition |
| animation looks correct | runtime observation/screenshot sequence/preview |
| collision fixed | controlled gameplay reproduction |
| shader/VFX correct | screenshot/video-like observation + no shader errors |
| save fixed | write -> restart/load -> compare state |
| performance fixed | profiler/frame-time evidence |

证据要能验证用户实际关心的结果。

## 3. Use the smallest executable surface

优先运行：

- isolated test scene；
- affected level；
- focused UI screen；
- small reproduction；

只有必须经过完整 game flow 时才从主菜单走全流程。

## 4. Runtime input

如果工具支持 input simulation：

- 用 project actions/expected player input；
- 不依赖脆弱 screen coordinates when semantic controls are available；
- 测试 press/release，而不是只发一个“click-like”抽象；
- gamepad/UI focus 要验证方向导航和 confirm/back；
- repeated/held input only when behavior needs it。

自动化 input 不应改写 gameplay logic 只为了测试方便。

## 5. Screenshots

Screenshot 适合验证：

- UI alignment；
- visible state；
- sprite/animation pose；
- shader/lighting；
- camera framing；
- generated/imported asset handoff。

截图不是 physics correctness 的充分证据。需要 interaction 时配合 runtime action/output。

## 6. Error capture

修改后检查：

- parse errors；
- invalid get/set/call；
- missing node/resource；
- shader compile errors；
- repeated runtime warnings if relevant；
- addon/import failures。

不要因为画面看起来正确就忽略新错误。

## 7. Visual iteration

对 UI/VFX/game-feel：

```text
run baseline if useful
-> change one dimension
-> replay same event
-> compare
```

一次同时改 shake、hit-stop、particles、audio、scale、camera 会让原因不可判断。

## 8. State reset

自动重复测试前确保场景能回到可预测状态：

- reload isolated scene；
- restart game；
- explicit debug reset if project already has one；
- controlled save fixture。

不要靠手工残留 state 得出结论。

## 9. Godot MCP selection

如果环境已有 live Godot bridge，优先复用。

当前可选生态大致分三类：

- editor/project/run/debug oriented MCP；
- rich editor + live bridge MCP；
- runtime-focused zero-footprint input/screenshot bridge。

具体候选见 `companion-tools.md`。

不要为了一个简单 code change 自动安装 MCP；也不要同时连接多个功能高度重叠的 MCP。

## 10. Erodenn/godot-mcp-runtime

这是可选的 runtime-focused 方案，适合 Agent 需要在 Godot 4.x 中做实际 runtime interaction/validation 且不想长期把 plugin 留在项目时评估。

它是较新的工具，采用前必须先检查当前 feature set、版本、security model 和项目允许的 tooling policy；不要仅凭“zero-footprint”自动选择。

## 11. Fallback without MCP

没有 live bridge 时：

```text
Godot editor/CLI parse/run
+ existing tests
+ targeted manual reproduction instructions
+ screenshots/logs supplied by user when needed
```

Agent 应明确说明“已静态验证”与“已实际运行验证”的区别。

## 12. Runtime QA by domain

### Player movement

- movement starts/stops as intended；
- diagonal/edge/corner；
- dash/jump/state exit；
- camera bounds。

### Combat

- expected hit count；
- active window；
- repeated hits；
- death/interruption；
- feedback returns to rest。

### UI

- open/close；
- focus；
- keyboard/gamepad；
- resize/aspect；
- back navigation。

### Assets

- correct imported production file；
- scale/anchor；
- filtering；
- animation timing；
- transparency。

### Save

- write；
- restart；
- load；
- migration fixture。

## 13. Completion rule

回答完成状态时区分：

```text
implemented
static checks passed
runtime checks passed
visual checks passed
not verified: <specific reason>
```

不要把无法执行的 runtime test 描述成已经通过。

## Source synthesis

基于 agentic game playtesting workflows、Godot MCP/runtime bridge patterns 与传统 Godot editor/CLI validation。目标是让 Agent 用最低成本获得与声明相匹配的真实证据。