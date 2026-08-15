# Performance Reference

用于 Godot 2D 的 profiler、frame-time、memory/allocation、render/physics/script bottleneck 和 measured optimization。

## Profile first

不要凭感觉优化。先分类：

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

再定位具体热点。

## Common 2D bottlenecks

常见：

- unnecessary `_process` / `_physics_process` work;
- expensive work every frame that can run less often;
- pathfinding/raycast every frame;
- large transparent sprites and particle overdraw;
- fullscreen/screen-reading shaders;
- repeated spawn/free churn;
- huge textures/audio or synchronous loading;
- UI polling/repeated tree lookups;
- shared Resource misuse causing unexpected duplication/state.

不要因为“node 多”就自动引入 ECS、pooling 或 MultiMesh。

## Optimization order

通常按这个顺序：

1. remove unnecessary work;
2. lower update frequency;
3. cache/reuse stable results;
4. simplify expensive asset/effect;
5. batch/pool only when measurements justify it;
6. specialized GPU/MultiMesh approaches only when the bottleneck actually matches.

## Realistic scenarios

不要只测空场景。构造真实压力：

- expected max enemies/agents;
- combat particles/VFX active;
- HUD visible;
- worst representative room/map;
- camera movement;
- spawn/despawn load;
- target low-end hardware when relevant.

比较修改前后同一场景、同一条件。

## Memory and lifecycle

检查：

- freed nodes still referenced;
- signal/lifecycle leaks;
- pooled object reset;
- temporary FX/timer cleanup;
- scene transitions retaining stale global state;
- asset size and duplicate loading;
- avoidable allocation spikes.

## Platform-specific work

只有目标平台需要时再处理 mobile/web constraints，例如 safe area、touch/battery、browser limitations、startup/download size 和 texture/audio memory。

不要让平台优化污染不相关的 desktop MVP。

## Validation

性能改动必须回答：

- 原始 bottleneck 是什么？
- 用什么 profiler/monitor 证明确认？
- 修改前后的 measurement/scenario 是否可比？
- correctness/visual quality 是否退化？
- 改动是否值得新增的复杂度？

没有 measurement，就不要把优化结论写成已验证。
