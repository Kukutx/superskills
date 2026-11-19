# Release, Export and CI Reference

用于 Godot export presets、clean build、CI、toolchain pinning、artifacts、platform credentials 与发布前 smoke validation。

普通 runtime bug/test 见 `verification-testing.md`。性能诊断属于匹配的维度 owner：2D 见 `../../godot-2d-game-development/references/performance.md`；3D 见 `../../godot-3d-game-development/references/rendering-lighting-world.md`。Release 只负责把需要的性能门槛纳入发布验证，不重复维护性能规则。

## Pin the toolchain

CI 明确：

```text
Godot editor version
export templates version
GDScript vs .NET build
addon/test-framework compatible versions
```

不要用模糊 `latest` 作为生产发布基础。Editor 与 export templates 应匹配。

## `export_presets.cfg` is the export source of truth

优先使用项目已有 export preset，不在 CI 里再造一套平台配置。

确认 preset name、target architecture、platform features 和 output path。Secrets/signing credentials 不进入 repo。

## Clean-checkout principle

发布可靠性应在干净环境证明：

```text
checkout
-> fetch required source assets/submodules/LFS
-> install exact Godot + templates
-> import project/resources
-> static/selected tests
-> export preset
-> inspect/run artifact where feasible
```

不要依赖本地 `.godot/` cache。Cache 可以加速，但 cache miss 不能破坏 correctness。

## Import before export

新增 sprites/fonts/audio/importers 后，headless export 可能暴露本地缓存掩盖的问题。

确保 clean environment 能完成需要的 import/scan，再 export。

## Test before packaging

按风险选择：

- parse/project load;
- existing unit/integration tests;
- selected scene/runtime smoke;
- critical save migration test;
- export smoke.

不要为了“CI 完整”自动安装测试 framework。

## Artifact validation

至少检查：

- output exists and non-empty;
- required companion files present;
- no relevant export errors;
- version/build metadata correct;
- executable/web build 可启动时做最小 smoke run.

Command exit 0 不等于所有 release behavior 已验证。

## CI implementation choice

优先沿用项目现有 CI。简单 pipeline 直接调用 Godot CLI 往往最透明。

只有现有 workflow 已经出现明确维护复杂度时，才评估第三方 action/image；采用前重新验证 maintenance、security、Godot compatibility 和 pinning policy。Runtime reference 不固定某个 action 名称。

## Platform credentials

Android/iOS/store signing：

- credentials 使用 CI secret / secure store;
- 不 commit password/token/certificate secret;
- dev/test 与 production signing 分清;
- workflow 权限最小化;
- 用户只要求本地 export 时，不擅自增加 store publishing automation.

## Web exports

需要发布 Web 时额外检查 hosting requirements、compression/cache、base path、browser input/audio restrictions 和 actual hosted smoke test。

不要假设本地 `file://` 等价生产 hosting。

## Release gates

最小 gate 按项目风险缩放，例如：

```text
no relevant parse/import errors
critical tests pass
clean export succeeds
artifact launches/loads
save compatibility considered
input/menu critical path works
version metadata correct
```

每个 gate 都应有真实价值。

## CI-only failure diagnosis

优先比较：

1. Godot/editor/templates version;
2. missing source/imported asset;
3. case-sensitive path;
4. LFS/submodule;
5. addon/import initialization;
6. environment/secret;
7. export preset difference;
8. .NET/platform SDK requirements.

不要第一步就重装所有依赖。

## Validation

修改 release pipeline 后至少验证：

- clean checkout path;
- exact target preset;
- cache miss path when feasible;
- artifact contents;
- failed critical test blocks release;
- secrets not printed;
- deployment/publish 只在用户明确要求的 event/branch/tag 发生.
