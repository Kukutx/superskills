# superskills

`superskills` 是个人 AI Skills 仓库，用来沉淀可复用的提示词、工作流、输出规范和领域知识。

目标：让 ChatGPT、Claude、Cursor 等 AI 工具更稳定地处理产品、开发、图片生成、xTool F1、Shopify、App Store 素材、营销、写作、研究和运营任务。

## 设计原则

- **可复用**：每个 skill 都能复制到 AI 工具中使用。
- **可执行**：输出格式明确，避免泛泛而谈。
- **可迭代**：通过 examples、changelog 和版本记录持续优化。
- **领域化**：按照任务场景分类。
- **少废话**：让 AI 更专注，不输出无用内容。
- **创作自由**：图片、角色、主题、雕刻和视觉任务默认按用户要求执行，不额外添加限制性说明。
- **生产可用**：面向真实项目时保留尺寸、格式、质量、导出和验证检查。

## 当前目录结构

```txt
superskills/
├── README.md
├── docs/
├── templates/
└── skills/
    ├── meta/
    ├── planning/
    ├── research/
    ├── product/
    ├── development/
    ├── creative/
    │   ├── xtool-f1-engraving/
    │   └── image-prompt-director/
    ├── design/
    ├── marketing/
    ├── ecommerce/
    ├── writing/
    └── operations/
```

## 当前核心 skills

| Skill | 用途 |
| --- | --- |
| `meta/prompt-optimizer` | 把粗糙想法优化成可复制提示词 |
| `meta/skill-builder` | 把重复工作流变成结构化 skill |
| `meta/skill-router` | 根据任务自动选择合适 skill 或组合流程 |
| `planning/project-planner` | 项目规划和任务拆解 |
| `research/research-brief` | 研究简报和资料分析 |
| `product/prd-builder` | PRD、MVP、用户故事和验收标准 |
| `development/code-review` | 代码审查 |
| `development/bug-diagnosis` | Bug 诊断 |
| `development/technical-design` | 技术方案设计 |
| `development/implementation-plan` | 实施计划 |
| `creative/xtool-f1-engraving` | xTool F1 雕刻图案方案 |
| `creative/image-prompt-director` | 图片生成提示词 |
| `design/app-store-assets` | App Store / Google Play 素材方向 |
| `design/image-review-refiner` | 图片评审和下一轮优化 prompt |
| `marketing/product-positioning` | 产品定位和欧美市场表达 |
| `ecommerce/shopify-dev` | Shopify 开发和实施 |
| `writing/business-email` | 商务邮件 |
| `writing/app-store-copy` | App Store / Google Play 文案 |
| `operations/sop-builder` | SOP |
| `operations/release-checklist` | 发布检查清单 |

## 推荐使用方式

```txt
先帮我选 skill，再执行：
[你的任务]
```

或者：

```txt
用 superskills 处理这个任务：
[你的任务]
```

## 维护规则

- 新增高频任务时，先用 `meta/prompt-optimizer` 优化提示词。
- 如果同一类任务重复 3 次以上，用 `meta/skill-builder` 沉淀成 skill。
- 生成图片、视觉、雕刻、角色、主题作品时，优先使用 `creative/image-prompt-director` 或 `creative/xtool-f1-engraving`。
- 面向上线或发布的任务，补充 QA、导出、验证和回滚步骤。
