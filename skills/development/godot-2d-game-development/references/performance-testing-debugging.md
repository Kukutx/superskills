# Performance, Testing, Debugging and Export Reference

用于 profiler、runtime bugs、automated tests、visual/runtime QA 和 export readiness。

## 1. Profile first

不要凭感觉优化。

先分类：

```text
CPU/script
physics
render/GPU/overdraw
memory/allocation
asset loading
UI
audio
navigation/AI
```

再定位。

## 2. Common 2D bottlenecks

常见：

- too many `_process`/`_physics_process` callbacks；
- large transparent sprites；
- particle overdraw；
- screen-reading/fullscreen shaders；
- runtime spawn/free churn；
- pathfinding/raycast every frame；
- huge textures；
- UI polling；
- repeated tree lookups；
- synchronous heavy loading。

不要因为“node 多”就自动 ECS/MultiMesh。

## 3. Optimization order

通常：

1. remove unnecessary work；
2. lower update frequency；
3. cache/reuse；
4. simplify asset/effect；
5. batch/pool when measured；
6. specialized GPU/MultiMesh only when justified。

## 4. Debugging loop

推荐：

```text
reproduce
-> observe exact error/behavior
-> isolate subsystem
-> inspect state/event timing
-> smallest fix
-> rerun same reproduction
-> regression check
```

不要一次改 5 个可能原因。

## 5. Godot runtime evidence

优先收集：

- Output/Debugger errors；
- stack trace；
- scene tree；
- node state；
- collision debug；
- profiler；
- monitor values；
- screenshot/video；
- minimal reproduction。

如果已有 live Godot MCP/bridge，可以自动 run/input/screenshot/error capture；没有也要保持同样证据循环。

## 6. Unit vs integration vs playtest

### Unit-ish tests

适合：

- damage formulas；
- inventory rules；
- save migration；
- procedural generation invariants；
- state transitions；
- utility/data logic。

### Scene/integration tests

适合：

- signal wiring；
- collisions；
- spawned scene setup；
- UI flow；
- save/load application。

### Runtime/playtest

必须覆盖：

- movement feel；
- camera；
- animation timing；
- combat feel；
- visual readability；
- controller focus；
- performance under actual load。

游戏不能只靠 unit tests 证明“好玩/正常”。

## 7. Test frameworks

如果项目已有：

- GUT；
- GdUnit4；
- custom test harness；
- CI scripts；

沿用，不要为了“更标准”换框架。

新项目需要自动化测试时：

- **GUT**：成熟的 GDScript-focused 方案，支持 CLI、assertions、doubling/stubs/spies、parameterized tests 和 JUnit XML。
- **GdUnit4**：适合 GDScript/C#、scene runner、mocking/spying、IDE/CI workflows。

**版本兼容优先于“最新版”。** 两者都按 Godot 版本发布兼容分支/版本；安装前先查项目 Godot 版本和对应 release。

不要为了给一个纯视觉/手感改动“加测试”而安装新框架。运动手感、camera、VFX 仍需要 runtime/playtest。

## 8. Visual regression / runtime automation

如果环境支持 screenshot/input automation：

- run scene；
- navigate menu/play action；
- capture screenshot；
- inspect errors；
- compare expected state；
- repeat after fix。

重要的是可重复流程，不是特定工具品牌。

## 9. Performance test scenarios

不要只测空场景。

至少构造真实压力：

- expected max enemies；
- particles during combat；
- HUD visible；
- worst map room；
- camera movement；
- spawning/despawning；
- low-end target if available。

## 10. Memory/lifecycle checks

检查：

- freed nodes still referenced；
- signal leaks；
- pooled object reset；
- temporary FX/timer cleanup；
- shared Resource mutation；
- texture/audio asset size；
- scene transitions retaining stale global state。

## 11. Export readiness

发布前确认：

- export preset；
- input；
- save path；
- resolution/stretch；
- fullscreen/window；
- audio；
- controller；
- asset case-sensitive paths；
- platform-specific APIs；
- debug-only code disabled；
- build starts from clean environment。

## 12. Web/mobile considerations

仅目标平台需要时读取/处理：

- mobile safe area/touch/battery；
- web file/access limitations；
- texture/audio memory；
- startup size/loading；
- controller browser/platform behavior。

不要让平台优化污染不相关 desktop MVP。

## 13. Definition of done

一个功能不是“代码写完”：

- runtime works；
- no new errors；
- edge case checked；
- repeated use stable；
- visual/audio readable；
- performance acceptable for target；
- small regression check passes。

## Source synthesis

主要吸收 GodotPrompter `godot-debugging`/`godot-testing`/`godot-optimization`/`export-pipeline`、GD-Agentic-Skills performance/testing、awesome-gamedev-agent-skills performance-optimization，以及 Godot MCP / GdUnit4 / runtime automation 项目的 evidence-driven QA 思路。
