# Release, Export and CI Reference

用于 Godot export presets、clean build、GitHub Actions/CI、version pinning、artifacts、platform credentials 与发布前 smoke validation。

普通 runtime bug/test 请读 `performance-testing-debugging.md`。

## 1. Pin the toolchain

CI 必须明确：

```text
Godot editor version
export templates version
GDScript vs .NET build
addon/test-framework compatible versions
```

不要使用模糊 `latest` 作为生产发布基础。Editor 与 export templates 应匹配。

## 2. `export_presets.cfg` is the export source of truth

优先让 CI 使用项目已有 export preset，而不是在 workflow 中再造一套平台配置。

检查：

- preset name；
- target architecture；
- texture/features；
- web/mobile/desktop-specific options；
- export path only as CI output concern。

Secrets/signing credentials 不进入 repo。

## 3. Clean-checkout principle

发布是否可靠，应在干净环境证明：

```text
checkout
-> submodules/LFS/assets if used
-> install exact Godot + templates
-> import project/resources
-> parse/headless smoke
-> run tests
-> export preset
-> inspect/run artifact where feasible
```

不要因为本地 `.godot/` cache 让缺失 import/source 偶然通过。

## 4. Import before export

新增 sprites/fonts/audio/importers 后，headless export 可能暴露本地编辑器已经缓存过的问题。

CI 应显式确保资源 import/scan 已完成，再 export。

Cache 可以加速，但 cache miss 不能让 build 失败；cache 不是 correctness source。

## 5. Test before packaging

按项目风险选择：

- parse/project load；
- unit/integration tests；
- selected scene tests；
- critical save migration tests；
- export smoke test。

不要为了“CI 完整”自动安装测试框架；项目已经有 GUT/GdUnit4 时沿用。

## 6. Export artifact validation

至少检查：

- output file exists and non-empty；
- expected companion files present；
- no obvious export error；
- version/build metadata correct；
- executable/web build 能启动时做最小 smoke run；
- artifact name includes target/version when useful。

“Godot export command returned 0”不是所有项目的唯一发布证据。

## 7. GitHub Actions choices

可选工具包括：

- `firebelley/godot-export`: GitHub Action-oriented Godot exports；
- `abarichello/godot-ci`: Docker/CI workflow for Godot export/deploy；
- direct Godot CLI: pipeline 简单时通常最透明。

选择规则：

```text
existing CI works -> keep it
simple one-platform pipeline -> direct CLI can be enough
many export presets / convenience needed -> evaluate maintained action/image
```

任何第三方 action 都 pin 合理版本/commit according to project policy，不盲跟 latest。

## 8. GdUnit4 CI

项目已使用 GdUnit4 时，可评估其官方/maintained GitHub Action workflow；GUT 同理沿用项目官方推荐 CLI。

关键不是 action 名称，而是 **Godot version + test framework version** 对齐。

## 9. Platform credentials

Android/iOS/store signing：

- credentials 用 CI secret / secure store；
- 不 commit keystore password/token/certificate secret；
- dev/test signing 与 production signing 分清；
- release workflow 的权限最小化。

如果用户只要求本地 export，不擅自增加 store publish automation。

## 10. Web exports

Web build 额外检查：

- hosting headers/features required by current Godot export options；
- compression/caching policy；
- path/base URL；
- browser input/audio restrictions；
- actual hosted smoke test when publishing。

不要假设本地 file:// 打开等价于生产 hosting。

## 11. Release gates

发布前建议最小 gate：

```text
no parse/import errors
critical tests pass
clean export succeeds
artifact launches/loads
save compatibility considered
input/menu path works
version metadata correct
```

项目很小时 gate 可以更小；关键是每一项都有真实价值。

## 12. Failure diagnosis

CI-only failure 优先比较：

1. Godot/editor/templates version；
2. missing source/imported asset；
3. case-sensitive path；
4. LFS/submodule；
5. addon initialization；
6. environment/secret；
7. export preset differences；
8. .NET/platform SDK requirements。

不要第一步就“重装所有依赖”。

## Validation

修改 release pipeline 后至少验证：

- from clean checkout；
- exact target preset；
- cache disabled/miss path at least once when feasible；
- artifact contents；
- failed test blocks release as intended；
- secrets not printed to logs；
- deployment/publish 只在用户明确要求的 branch/tag/event 发生。

## Source synthesis

基于 Godot CLI/export workflow、`firebelley/godot-export`、`godot-ci`、GdUnit4 CI patterns。具体命令和平台要求随 Godot 版本变化，实施时优先查对应版本官方文档。