# superskills

个人 AI Skills 仓库。只保存**会改变 Agent 决策的可复用规则、工作流和领域知识**。

## Runtime model

```text
user task
-> choose one primary skill
-> read skill.md
-> load only needed references
-> execute
-> validate
```

核心原则：

- **specific before generic**：领域 Skill 优先于通用方法。
- **one primary skill**：不按关键词堆叠多个 Skill。
- **progressive disclosure**：默认只读 `skill.md`；深层知识按需读 `references/`。
- **maintenance is not runtime**：来源、回归测试、历史只放 `maintenance/`。
- **no boilerplate files**：普通 Skill 默认只有 `skill.md`。
- **evidence before claims**：运行、视觉、发布等结论必须有匹配的验证。

## Structure

```text
superskills/
├── README.md
├── docs/authoring-guide.md
├── gpts/kukutx/
│   ├── README.md
│   └── project-instructions.md
├── skills/<category>/<skill>/
│   ├── skill.md
│   ├── references/      # optional runtime depth
│   └── maintenance/     # optional sources/tests/history
├── templates/skill-template.md
├── tools/validate_repo.py
└── .github/workflows/validate.yml
```

**唯一 Skill catalog**：`skills/meta/skill-router/skill.md`。

不要在 README、Project Instructions 或其他 knowledge 文件复制同一份路由表。新增/删除 Skill 时只维护 Router，并运行仓库校验。

## Growth rule

新增 Skill/reference 前先问：

1. 任务是否会重复？
2. 是否存在值得长期保留的独特决策规则？
3. 现有 Skill 是否已经覆盖？
4. 新文件是否真的改变行为，而不是重复说明？

答案不明确，就不要新增。

维护规范见 `docs/authoring-guide.md`。