# Verification and Testing Reference

用于 Godot runtime bug、行为验证、automated tests、visual/runtime QA 和 Agent 修改后的 evidence-driven verification。

## Core loop

```text
reproduce exact behavior
-> inspect relevant state/errors
-> isolate subsystem
-> make smallest change
-> rerun the same reproduction
-> compare with expected result
-> regression check
```

不要一次修改多个可能原因，也不要因为 parse/build 通过就宣布交互或视觉问题完成。

## Match evidence to the claim

| Claim | Evidence |
| --- | --- |
| scene/resource loads | no relevant parse/resource errors |
| button/input works | actual input causes expected transition |
| collision fixed | controlled gameplay reproduction |
| animation/VFX correct | runtime observation / frame preview |
| save fixed | write -> restart/load -> compare state |
| performance fixed | profiler/frame-time evidence |
| export fixed | clean export + artifact smoke check |

证据必须验证用户实际关心的结果。

## Smallest executable surface

优先：

- isolated test scene;
- affected level;
- focused UI screen;
- minimal reproduction.

只有必须经过完整 flow 时才从主菜单走全流程。

## Test layers

### Logic tests

适合 damage formulas、inventory rules、save migration、state transitions、procedural invariants 和纯数据逻辑。

### Scene/integration tests

适合 signal wiring、collision、spawned scene setup、UI flow 和 save/load application。

### Runtime/playtest

用于 movement/camera feel、animation timing、combat feel、visual readability、controller focus 和其他需要真实交互的结果。

项目已有 test framework/harness 就沿用；不要为了形式完整自动安装新的测试框架。

## Runtime automation

如果环境已经支持 run/input/screenshot/error capture：

- 复用已有工具；
- 优先使用 project action/semantic input，而不是脆弱坐标；
- press/hold/release 要符合真实行为；
- UI 验证 keyboard/gamepad focus、confirm/back；
- screenshot 只能证明可见状态，不能单独证明 physics/combat correctness。

不要修改 gameplay logic 只为方便自动化工具操作。

## Error capture

修改后检查相关的：

- parse/runtime errors;
- invalid get/set/call;
- missing node/resource;
- shader/import/addon failures;
- 新出现的相关 warning.

画面看起来正确也不能忽略新增错误。

## Stable reruns

重复测试前回到可预测状态：reload scene、restart game、existing debug reset 或 controlled save fixture。

不要依赖上一次运行残留 state。

## Without live tooling

使用可获得的最强证据：

```text
Godot editor/CLI checks
+ existing tests
+ targeted manual reproduction steps
+ user-provided screenshot/log when required
```

明确区分：

- `implemented`
- `static checks passed`
- `runtime checks passed`
- `visual checks passed`
- `not verified: <reason>`

不能执行的测试不得描述成已经通过。

## Domain smoke checks

- movement: start/stop, edge/corner, dash/jump exit, camera bounds
- combat: hit count, active window, interruption/death, feedback reset
- UI: open/close, focus, input devices, resize/aspect, back navigation
- assets: referenced production file, scale/anchor/filtering/timing/transparency
- save: write, restart, load, migration fixture

## Completion rule

验证状态必须与证据等级一致。避免“应该好了”或把静态检查包装成 runtime confirmation。
