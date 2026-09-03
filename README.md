# superskills

个人 AI Skills 仓库。只保存**会改变 Agent 决策的可复用规则、工作流和领域知识**，并用路由、按需加载和可验证完成边界控制上下文质量。

## Runtime model

```text
user task
-> choose one primary Skill
-> resolve direction-changing unknowns
-> read skill.md
-> load only needed references
-> execute
-> validate at the level claimed
```

核心原则：

- **specific before generic**：领域 Skill 优先于通用方法。
- **one primary skill**：不按关键词堆叠多个 Skill。
- **confidence before commitment**：核心方向或事实不清时先集中询问；可逆细节不做无意义盘问。
- **progressive disclosure**：默认只读 `skill.md`；深层知识按需读 `references/`。
- **maintenance is not runtime**：behavioral eval、来源和少量设计决策只放 `maintenance/`。
- **single source of truth**：同一规则只保留一个 owner。
- **evidence before claims**：运行、视觉、存档、导出和发布结论必须有匹配证据。

## Structure

```text
superskills/
├── AGENTS.md
├── LICENSE
├── README.md
├── docs/authoring-guide.md
├── gpts/kukutx/
│   ├── README.md
│   └── project-instructions.md
├── skills/<category>/<skill>/
│   ├── skill.md
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

**唯一完整 Skill catalog**：`skills/meta/skill-router/skill.md` 的 `## Catalog` 表格。

不要在 README、Project Instructions 或其他文件复制完整路由表。新增、删除或重命名 Skill 时只维护 Router；边界变化时只补必要的 behavioral eval。

## Validation

工具统一使用 Python 3.14。

```bash
python -m unittest discover -s tests -v
python tools/validate_repo.py
python tools/export_behavioral_evals.py --check
```

Validator 检查 Skill 层级、frontmatter、目录形状、Router Catalog 完整性、真实 Markdown 引用、runtime/maintenance 边界和 behavioral eval 路径完整性。

## Build a runtime bundle

不要默认上传整个仓库。构建只包含 Project Instructions、Router、选中的 Skill 与 reference 的最小包：

```bash
python tools/build_bundle.py \
  --profile gpts/kukutx \
  --skill writing/resume-writing
```

复杂 Skill 可追加：

```bash
--reference development/godot-project-systems:ui-ux
```

输出的 `manifest.json` 记录源提交、文件哈希、字节数和粗略 Token 预算，并保证不包含 `maintenance/`。

## Releases

`.github/workflows/release.yml` 只负责创建新的稳定版本：手动输入新版本标签，先运行测试、Validator 和 eval export，再构建 Runtime Bundle，并上传 ZIP 与 SHA-256 校验文件。已存在的版本不会被覆盖或刷新。

同仓库 PR 合并后，`.github/workflows/delete-merged-branch.yml` 会自动删除已合并的 head branch；来自 fork、未合并或默认分支不会被删除。

## Growth rule

新增 Skill/reference 前先问：

1. 任务是否会重复？
2. 是否存在值得长期保留的独特决策规则？
3. 现有 owner 是否已经覆盖？
4. 新文件是否真的改变行为或明显减少 runtime context？
5. 能否用一个真实 behavioral eval 证明新边界有价值？

答案不明确，就不要新增。

## License

本仓库使用 [MIT License](LICENSE)。允许使用、复制、修改和分发，但必须保留原版权和许可证声明；软件按原样提供，不附带担保。
