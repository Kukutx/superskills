# superskills

个人 AI Skills 仓库。只保存**会改变 Agent 决策的可复用规则、工作流和领域知识**，并用路由、按需加载和可验证完成边界控制上下文质量。

## Runtime model

```text
user task
-> inspect available context and tools
-> choose one primary Skill
-> read SKILL.md and only needed references
-> execute authorized, reversible work
-> verify and self-correct
-> escalate only a true blocker or consequential final step
-> report the outcome
```

核心原则：

- **specific before generic**：领域 Skill 优先于通用方法。
- **one primary skill**：不按关键词堆叠多个 Skill。
- **action before interrogation**：先读取现有资料、使用可用工具并完成已授权的可逆工作；只把真正需要用户决定的阻塞点升级给用户。
- **approval at the boundary**：需要批准的不可逆或高影响动作，先准备好可审查结果，再在最后边界请求批准。
- **execution is not planning**：任务很长或步骤很多，不代表 `project-planner` 是交付物；用户要求执行时，应由领域 owner 执行并在内部规划。
- **progressive disclosure**：默认只读 `SKILL.md`；深层知识按需读 `references/`。
- **maintenance is not runtime**：behavioral eval、来源和少量设计决策只放 `maintenance/`。
- **single source of truth**：同一规则只保留一个 owner。
- **evidence before claims**：运行、视觉、存档、导出和发布结论必须有匹配证据，验证强度与改动风险相匹配。

## Structure

```text
superskills/
├── .claude-plugin/
│   ├── plugin.json          # Claude Code plugin manifest
│   └── marketplace.json     # one-plugin marketplace for /plugin install
├── AGENTS.md
├── LICENSE
├── README.md
├── docs/authoring-guide.md
├── gpts/kukutx/
│   ├── README.md
│   └── project-instructions.md
├── skills/<skill>/
│   ├── SKILL.md
│   ├── references/          # optional runtime depth
│   └── maintenance/         # optional evals/sources/decisions
├── templates/skill-template.md
├── tools/
│   ├── validate_repo.py
│   ├── build_bundle.py
│   └── export_behavioral_evals.py
├── tests/
└── .github/workflows/
    ├── validate.yml
    ├── release.yml
    └── delete-merged-branch.yml
```

**唯一完整 Skill catalog**：`skills/skill-router/SKILL.md` 的 `## Catalog` 表格。

不要在 README、Project Instructions 或其他文件复制完整路由表。新增、删除或重命名 Skill 时只维护 Router；边界变化时只补必要的 behavioral eval。

## Install

Skill 目录遵循开放的 [Agent Skills 规范](https://agentskills.io/specification)：每个 Skill 是 `skills/<skill>/SKILL.md`，仓库根目录同时是一个 Claude 插件 marketplace。

**claude.ai 网页版 / 桌面版（推荐，无需下载）**：在 [Customize > Plugins](https://claude.ai/customize/plugins) 选择 **Add > Add marketplace**，填入 `https://github.com/Kukutx/superskills`，再安装 `superskills`。全部 Skill 会挂到账号上，聊天时 Claude 按 description 自动调用；同一账号的 Cowork 和 Claude Code 也会同步出现。

**Claude Code**：

```text
/plugin marketplace add Kukutx/superskills
/plugin install superskills@kukutx-superskills
```

**ChatGPT Project / GPT**：没有原生 Skill 加载机制，使用下面的 runtime bundle 和 `gpts/kukutx/`。

## Validation

工具统一使用 Python 3.14。

```bash
python -m unittest discover -s tests -v
python tools/validate_repo.py
python tools/export_behavioral_evals.py --check
```

Validator 检查 Skill 层级、frontmatter（含 Agent Skills 规范约束）、目录形状、Router Catalog 完整性、真实 Markdown 引用、runtime/maintenance 边界和 behavioral eval 路径完整性。

## Build a runtime bundle

不要默认上传整个仓库。构建只包含 Project Instructions、Router、选中的 Skill 与 reference 的最小包：

```bash
python tools/build_bundle.py \
  --profile gpts/kukutx \
  --skill resume-writing
```

复杂 Skill 可追加：

```bash
--reference godot-project-systems:ui-ux
```

输出的 `manifest.json` 记录源提交、文件哈希、字节数和粗略 Token 预算，并保证不包含 `maintenance/`。

## Releases

`.github/workflows/release.yml` 只负责创建新的稳定版本：手动输入新版本标签，先运行测试、Validator 和 eval export，再构建 Runtime Bundle，并上传 ZIP 与 SHA-256 校验文件。已存在的版本不会被覆盖或刷新。

同仓库 PR 合并后，`.github/workflows/delete-merged-branch.yml` 会自动删除已合并的 head branch；来自 fork、未合并或默认分支不会被删除。

## Growth rule

新增 Skill/reference 前先检查：

1. 任务是否会重复？
2. 是否存在值得长期保留的独特决策规则？
3. 现有 owner 是否已经覆盖？
4. 新文件是否真的改变行为或明显减少 runtime context？
5. 能否用一个真实 behavioral eval 证明新边界有价值？
6. 新规则是否只是重复全局的规划、询问、批准或工具使用行为？

答案不明确，就不要新增。

## License

本仓库使用 [MIT License](LICENSE)。允许使用、复制、修改和分发，但必须保留原版权和许可证声明；软件按原样提供，不附带担保。
