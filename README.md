# superskills

`superskills` 是一个个人 AI Skills 仓库，用来沉淀可复用的提示词、工作流、输出规范和领域知识。

这个仓库的目标不是收集零散 prompt，而是把每个高价值场景整理成一个可以长期迭代的 **skill**：有明确目标、输入要求、输出格式、约束规则、示例和反例。

## 核心定位

`superskills` 是你的个人 AI 工作流资产库。它适合存放：

- 可重复使用的 ChatGPT / Claude / Cursor 提示词
- 特定领域的 AI 工作规范
- 生成图、写作、开发、研究、规划、电商等场景的输出契约
- 常用任务的 examples、checklists、anti-patterns
- 未来可以持续升级的个人知识型 workflow

## 设计原则

- **可复用**：每个 skill 都应该能被复制到 ChatGPT、Claude、Cursor 或其他 AI 工具中使用。
- **可执行**：输出格式明确，避免泛泛而谈。
- **可迭代**：每个 skill 都可以通过 examples、changelog 和版本记录持续优化。
- **领域化**：按照场景分类，而不是按照模型或工具分类。
- **少废话**：skill 应该让 AI 更专注，不输出无用内容。
- **有约束**：每个 skill 都必须说明不能做什么。
- **有质量标准**：每个成熟 skill 都应该有 examples 和 checklist。

## 当前目录结构

```txt
superskills/
├── README.md
├── docs/
│   ├── skill-writing-guide.md
│   ├── maturity-model.md
│   └── skill-taxonomy.md
├── templates/
│   ├── skill-template.md
│   ├── prompt-template.md
│   ├── examples-template.md
│   └── changelog-template.md
└── skills/
    ├── meta/
    │   ├── prompt-optimizer/
    │   └── skill-builder/
    ├── planning/
    │   └── project-planner/
    ├── research/
    │   └── research-brief/
    ├── development/
    │   ├── code-review/
    │   ├── bug-diagnosis/
    │   └── technical-design/
    ├── creative/
    │   ├── xtool-f1-engraving/
    │   └── image-prompt-director/
    ├── design/
    │   └── app-store-assets/
    ├── ecommerce/
    │   └── shopify-dev/
    ├── writing/
    │   └── business-email/
    └── operations/
        └── sop-builder/
```

## Skill 分类

| 分类 | 用途 |
| --- | --- |
| `meta` | 提示词优化、创建新 skill、AI 工作流控制 |
| `planning` | 项目规划、任务拆解、优先级、执行计划 |
| `research` | 研究简报、资料分析、竞品/工具对比 |
| `development` | 编程、代码审查、架构设计、Debug、技术方案 |
| `creative` | 创意、手工、雕刻、图像生成、产品礼品设计 |
| `design` | App 素材、品牌视觉、应用商店截图、落地页 |
| `ecommerce` | Shopify、电商运营、商品页、转化率优化 |
| `writing` | 邮件、商务沟通、说明文档、短文案 |
| `operations` | SOP、清单、重复流程、内部操作规范 |

## 当前已初始化的 skills

| Skill | 成熟度 | 用途 |
| --- | --- | --- |
| `meta/prompt-optimizer` | refined | 把粗糙想法优化成可复制提示词 |
| `meta/skill-builder` | refined | 把重复工作流变成结构化 skill |
| `planning/project-planner` | refined | 把目标拆成阶段、任务、风险和下一步 |
| `research/research-brief` | refined | 生成带证据意识的研究简报 |
| `development/code-review` | refined | 审查代码正确性、安全、性能和可维护性 |
| `development/bug-diagnosis` | refined | 根据症状、日志、代码定位 bug 根因 |
| `development/technical-design` | refined | 设计简单可落地的技术方案 |
| `creative/xtool-f1-engraving` | refined | 生成适合 xTool F1 的雕刻图案方案 |
| `creative/image-prompt-director` | refined | 生成高质量图像生成提示词 |
| `design/app-store-assets` | refined | 设计 App Store / Google Play 素材方向 |
| `ecommerce/shopify-dev` | refined | 解决 Shopify 开发和实施问题 |
| `writing/business-email` | refined | 写简洁专业的商务邮件 |
| `operations/sop-builder` | refined | 把重复流程整理成 SOP |

## 如何使用一个 skill

1. 打开对应目录下的 `skill.md`。
2. 复制「System Prompt」部分到 AI 工具的系统提示词、项目说明或自定义指令中。
3. 使用 `prompt-template.md` 填写当前任务。
4. 如果输出效果好，把案例补充到 `examples.md`。
5. 每次明显优化后，在 `changelog.md` 记录变化。

## 推荐工作流

### 1. 先优化 prompt

当你只有模糊想法时，先使用：

```txt
skills/meta/prompt-optimizer/
```

### 2. 高频任务变成 skill

如果一个 prompt 使用超过 3 次，就考虑用：

```txt
skills/meta/skill-builder/
```

把它沉淀成正式 skill。

### 3. 每个成熟 skill 保持 4 个文件

```txt
skill-name/
├── skill.md             # 核心规则、角色、约束、输出格式
├── prompt-template.md   # 每次使用时填写的输入模板
├── examples.md          # 好案例、差案例、可复用样例
└── changelog.md         # 版本记录
```

## Skill 成熟度

| 等级 | 含义 |
| --- | --- |
| `draft` | 初稿，可用但不稳定 |
| `usable` | 能用于真实任务 |
| `refined` | 有 examples、constraints、checklist，可适应多数常见场景 |
| `stable` | 多次实战验证，结构基本稳定 |

## 版本规划

- `v0.1`：建立仓库结构和第一个可用 skill。
- `v0.2`：补齐元技能、规划、研究、开发、设计、电商、写作、运营主力场景。
- `v0.3`：加入更多真实 examples 和个人项目案例。
- `v0.4`：增加跨 skill 的组合工作流。
- `v1.0`：形成稳定的个人 AI 工作流系统。
