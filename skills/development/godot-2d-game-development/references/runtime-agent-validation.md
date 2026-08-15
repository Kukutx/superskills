# Runtime Agent Validation Reference

用于 Agent 修改 Godot 后的 **evidence-driven verification**：scene inspection、run/stop、runtime input、screenshots、errors/output、UI flow、visual regression 与可重复 smoke tests。

它不是 MCP 安装指南。具体工具候选只在 `companion-tools.md` 维护；这里定义验证方法。

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
-> repeat
```

不要“代码 parse/compile 通过”就宣布视觉或交互任务完成。

## 2. Match evidence to the claim

| Claim | Useful evidence |
| --- | --- |
| scene/resource loads | no parse/resource errors |
| button works | focus/click/input causes expected transition |
| animation looks correct | runtime observation / frame preview / screenshot sequence |
| collision fixed | controlled gameplay reproduction |
| shader/VFX correct | runtime visual observation + no shader errors |
| save fixed | write -> restart/load -> compare state |
| performance fixed | profiler/frame-time evidence |
| export fixed | clean export + artifact smoke check |

证据要能验证用户实际关心的结果。

## 3. Use the smallest executable surface

优先运行：

- isolated test scene；
- affected level；
- focused UI screen；
- minimal reproduction。

只有必须经过完整 game flow 时才从主菜单走全流程。

## 4. Runtime input

如果环境支持 input simulation：

- 优先使用 project actions / expected player input；
- semantic input 可用时不要依赖脆弱 screen coordinates；
- 需要时区分 press / hold / release；
- gamepad UI 要验证方向导航、confirm、back；
- repeated input 只在行为本身需要时测试。

不要改 gameplay logic 只为了让自动化工具更容易点到。

## 5. Screenshots and visual evidence

Screenshot 适合验证：

- UI alignment；
- visible state；
- sprite pose；
- shader/lighting；
- camera framing；
- imported asset handoff。

单张截图不是 physics/combat correctness 的充分证据；需要 interaction 时必须配合 runtime action、state 或 output。

## 6. Error capture

修改后检查：

- parse errors；
- invalid get/set/call；
- missing node/resource；
- shader compile errors；
- addon/import failures；
- 新出现且与任务相关的 runtime warnings。

画面看起来正确也不能忽略新增错误。

## 7. Visual iteration discipline

对 UI/VFX/game-feel：

```text
establish baseline when useful
-> change one meaningful dimension
-> replay the same event
-> compare
```

一次同时改 shake、hit-stop、particles、audio、scale、camera，会让因果不可判断。

## 8. State reset

重复测试前回到可预测状态：

- reload isolated scene；
- restart game；
- use existing debug reset；
- use controlled save fixture。

不要依赖上一次手工运行残留的 runtime state。

## 9. Live-tool selection

如果环境已有 Godot live bridge / MCP / editor automation，优先复用已有工具。

只在当前任务确实需要以下能力时才考虑额外 tooling：

- runtime input；
- screenshot；
- scene inspection；
- run/stop automation；
- errors/output capture。

具体候选与选择边界见 `companion-tools.md`。

不要为了一个简单 code change 自动安装 MCP，也不要同时连接多个高度重叠的 bridge。

## 10. Fallback without live tooling

没有 live bridge 时：

```text
Godot editor/CLI parse/run
+ existing tests
+ targeted manual reproduction steps
+ user-provided screenshot/log when visual evidence is required
```

Agent 必须区分：

```text
implemented
static checks passed
runtime checks passed
visual checks passed
not verified: <specific reason>
```

不能执行的 runtime test 不得描述成已经通过。

## 11. Runtime QA by domain

### Player movement

- starts/stops as intended；
- diagonal/edge/corner；
- dash/jump/state exit；
- camera bounds。

### Combat

- expected hit count；
- active window；
- repeated hits；
- interruption/death；
- feedback returns to rest。

### UI

- open/close；
- focus；
- keyboard/gamepad；
- resize/aspect；
- back navigation。

### Assets

- production file actually referenced；
- scale/anchor；
- filtering；
- animation timing；
- transparency。

### Save

- write；
- restart；
- load；
- migration fixture。

### Release

- clean project import；
- exact export preset；
- artifact exists/launches when feasible。

## 12. Completion rule

完成声明必须与证据等级一致：

- 只改了文件 -> `implemented`；
- 只做 parser/linter -> `static checks passed`；
- 实际运行并重现 -> `runtime checks passed`；
- 实际观察视觉结果 -> `visual checks passed`。

不要用模糊的“应该好了”代替验证状态。

## Source synthesis

基于 agentic game playtesting、Godot editor/CLI validation 与 runtime bridge workflows。目标不是绑定某个 MCP，而是让 Agent 用最低成本获得与声明相匹配的真实证据。