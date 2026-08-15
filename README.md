# superskills

个人 AI Skills 仓库。目标是把**真正可复用的决策规则、工作流和领域知识**沉淀下来，而不是积累 prompt 文档。

## Runtime model

```text
user task
-> choose one primary skill
-> read its skill.md
-> load only needed references
-> execute
-> validate
```

核心原则：

- **specific before generic**：有领域 Skill 时优先领域 Skill。
- **one primary skill**：不要因为多个关键词同时加载多个 Skill。
- **progressive disclosure**：默认只读 `skill.md`；深层知识按需读 `references/`。
- **no boilerplate files**：普通 Skill 不再强制 `prompt-template.md`、`examples.md`、`changelog.md`。
- **maintenance is not runtime context**：来源、回归测试、历史放 `maintenance/`，不默认加载。
- **evidence before claims**：生产、运行、视觉或发布任务需要与结论匹配的验证。

## Repository structure

```text
superskills/
├── README.md
├── docs/
│   └── authoring-guide.md
├── gpts/kukutx/
│   ├── README.md
│   ├── project-instructions.md
│   ├── knowledge-pack.md
│   ├── knowledge-files.md
│   └── conversation-starters.md
├── skills/
│   └── <category>/<skill>/
│       ├── skill.md
│       ├── references/      # optional: runtime domain depth
│       └── maintenance/     # optional: sources/tests/history
└── templates/
    └── skill-template.md
```

## Active skills

| Skill | Purpose |
| --- | --- |
| `meta/prompt-optimizer` | 用户明确需要 prompt/template 时优化提示词 |
| `meta/skill-builder` | 创建、审计或重构可复用 Skill |
| `meta/skill-router` | 不确定任务归属时选择最小 Skill 集合 |
| `planning/project-planner` | 项目阶段、依赖、风险和下一步 |
| `research/research-brief` | 有来源、有不确定性的决策型研究 |
| `product/prd-builder` | MVP、用户故事、验收标准、out-of-scope |
| `development/bug-diagnosis` | 通用软件故障诊断 |
| `development/code-review` | 通用代码 / diff / PR 审查 |
| `development/technical-design` | 通用技术方案与系统边界 |
| `development/implementation-plan` | 文件级实施步骤与验证计划 |
| `development/godot-2d-game-development` | Godot 4.x 2D / pixel game production router |
| `development/game-dev-spritesheet-slicer` | animation strip / spritesheet 生产与切分 |
| `creative/image-prompt-director` | 图像生成方向与 production-ready prompt |
| `creative/xtool-f1-engraving` | xTool F1 雕刻设计与生产约束 |
| `design/app-store-assets` | App Store / Google Play 视觉素材 |
| `design/image-review-refiner` | 图像评审与下一轮修改指令 |
| `ecommerce/shopify-dev` | Shopify 开发与实施 |
| `marketing/product-positioning` | 产品定位与可信 messaging |
| `writing/business-email` | 简洁专业商务邮件 |
| `writing/app-store-copy` | App Store / Google Play 文案 |
| `operations/release-checklist` | 通用发布 gate / rollback / monitoring |
| `operations/sop-builder` | 可执行 SOP |

## Growth rule

新增或拆分 Skill 前先问：

1. 这个任务是否会重复？
2. 是否存在值得长期保留的**独特决策规则**？
3. 现有 Skill 是否已经能处理？
4. 新文件是否会改变 Agent 行为，而不是重复说明？

如果答案不明确，就不要新增 Skill 或 reference。

详细维护规范见 `docs/authoring-guide.md`。