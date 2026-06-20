# superskills

`superskills` 是一个个人 AI Skills 仓库，用来沉淀可复用的提示词、工作流、输出规范和领域知识。

这个仓库的目标不是收集零散 prompt，而是把每个高价值场景整理成一个可以长期迭代的 **skill**：有明确目标、输入要求、输出格式、约束规则、示例和反例。

## 核心定位

`superskills` 是你的个人 AI 工作流资产库。它适合存放：

- 可重复使用的 ChatGPT / Claude / Cursor 提示词
- 特定领域的 AI 工作规范
- 生成图、写作、开发、研究、规划、电商等场景的输出契约
- 常用任务的 examples、checklists、anti-patterns
- 面向欧美市场的产品、设计、营销、发布流程
- 未来可以持续升级的个人知识型 workflow

## 设计原则

- **可复用**：每个 skill 都应该能被复制到 ChatGPT、Claude、Cursor 或其他 AI 工具中使用。
- **可执行**：输出格式明确，避免泛泛而谈。
- **可迭代**：每个 skill 都可以通过 examples、changelog 和版本记录持续优化。
- **领域化**：按照场景分类，而不是按照模型或工具分类。
- **少废话**：skill 应该让 AI 更专注，不输出无用内容。
- **有约束**：每个 skill 都必须说明不能做什么。
- **有质量标准**：每个成熟 skill 都应该有 examples 和 checklist。
- **欧美市场友好**：默认避免夸张、AI 感、低信任感和不适合欧美用户的表达。

## 当前目录结构

```txt
superskills/
├── README.md
├── docs/
│   ├── skill-writing-guide.md
│   ├── maturity-model.md
│   ├── skill-taxonomy.md
│   ├── personal-defaults.md
│   ├── western-market-guidelines.md
│   ├── workflow-recipes.md
│   └── v0.3-upgrade-notes.md
├── templates/
│   ├── skill-template.md
│   ├── prompt-template.md
│   ├── examples-template.md
│   └── changelog-template.md
└── skills/
    ├── meta/
    │   ├── prompt-optimizer/
    │   ├── skill-builder/
    │   └── skill-router/
    ├── planning/
    │   └── project-planner/
    ├── research/
    │   └── research-brief/
    ├── product/
    │   └── prd-builder/
    ├── development/
    │   ├── code-review/
    │   ├── bug-diagnosis/
    │   ├── technical-design/
    │   └── implementation-plan/
    ├── creative/
    │   ├── xtool-f1-engraving/
    │   ├── image-prompt-director/
    │   └── ip-safe-creative-adapter/
    ├── design/
    │   ├── app-store-assets/
    │   └── image-review-refiner/
    ├── marketing/
    │   └── product-positioning/
    ├── ecommerce/
    │   └── shopify-dev/
    ├── writing/
    │   ├── business-email/
    │   └── app-store-copy/
    └── operations/
        ├── sop-builder/
        └── release-checklist/
```

## Skill 分类

| 分类 | 用途 |
| --- | --- |
| `meta` | 提示词优化、创建新 skill、skill 路由、AI 工作流控制 |
| `planning` | 项目规划、任务拆解、优先级、执行计划 |
| `research` | 研究简报、资料分析、竞品/工具对比 |
| `product` | PRD、MVP 范围、用户故事、验收标准 |
| `development` | 编程、代码审查、架构设计、Debug、技术方案、实施计划 |
| `creative` | 创意、手工、雕刻、图像生成、IP 安全改写、产品礼品设计 |
| `design` | App 素材、品牌视觉、应用商店截图、图像 review、落地页 |
| `marketing` | 产品定位、卖点、slogan、欧美市场表达 |
| `ecommerce` | Shopify、电商运营、商品页、转化率优化 |
| `writing` | 邮件、商务沟通、App Store 文案、说明文档、短文案 |
| `operations` | SOP、发布检查清单、重复流程、内部操作规范 |

## 当前已初始化的 skills

| Skill | 成熟度 | 用途 |
| --- | --- | --- |
| `meta/prompt-optimizer` | refined | 把粗糙想法优化成可复制提示词 |
| `meta/skill-builder` | refined | 把重复工作流变成结构化 skill |
| `meta/skill-router` | refined | 根据任务自动选择合适 skill 或组合流程 |
| `planning/project-planner` | refined | 把目标拆成阶段、任务、风险和下一步 |
| `research/research-brief` | refined | 生成带证据意识的研究简报 |
| `product/prd-builder` | refined | 把产品/功能想法变成 PRD、MVP、用户故事和验收标准 |
| `development/code-review` | refined | 审查代码正确性、安全、性能和可维护性 |
| `development/bug-diagnosis` | refined | 根据症状、日志、代码定位 bug 根因 |
| `development/technical-design` | refined | 设计简单可落地的技术方案 |
| `development/implementation-plan` | refined | 把技术方案拆成文件级任务、实现步骤和测试点 |
| `creative/xtool-f1-engraving` | refined | 生成适合 xTool F1 的雕刻图案方案 |
| `creative/image-prompt-director` | refined | 生成高质量图像生成提示词 |
| `creative/ip-safe-creative-adapter` | refined | 把受版权/IP 启发的想法改写成原创安全方向 |
| `design/app-store-assets` | refined | 设计 App Store / Google Play 素材方向 |
| `design/image-review-refiner` | refined | 评审生成图片并给下一轮优化 prompt |
| `marketing/product-positioning` | refined | 生成欧美市场友好的定位、卖点、slogan 和信息架构 |
| `ecommerce/shopify-dev` | refined | 解决 Shopify 开发和实施问题 |
| `writing/business-email` | refined | 写简洁专业的商务邮件 |
| `writing/app-store-copy` | refined | 写 App Store / Google Play 标题、副标题、描述和更新说明 |
| `operations/sop-builder` | refined | 把重复流程整理成 SOP |
| `operations/release-checklist` | refined | 为 App / Web / Shopify 上线准备发布检查清单 |

## 如何使用一个 skill

1. 打开对应目录下的 `skill.md`。
2. 复制「System Prompt」部分到 AI 工具的系统提示词、项目说明或自定义指令中。
3. 使用 `prompt-template.md` 填写当前任务。
4. 如果输出效果好，把案例补充到 `examples.md`。
5. 每次明显优化后，在 `changelog.md` 记录变化。

## 推荐工作流

### 1. 不知道用哪个 skill

```txt
skills/meta/skill-router/
```

### 2. 只有模糊想法

```txt
skills/meta/prompt-optimizer/
```

### 3. 高频任务变成 skill

如果一个 prompt 使用超过 3 次，就考虑用：

```txt
skills/meta/skill-builder/
```

把它沉淀成正式 skill。

### 4. 做欧美市场产品/素材

先阅读：

```txt
docs/personal-defaults.md
docs/western-market-guidelines.md
docs/workflow-recipes.md
```

再使用对应 skill。

### 5. 每个成熟 skill 保持 4 个文件

```txt
skill-name/
├── skill.md
├── prompt-template.md
├── examples.md
└── changelog.md
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
- `v0.3`：加入个人默认配置、欧美市场规范、skill router、组合工作流、产品/营销/发布/图像 review 主力技能。
- `v0.4`：加入更多真实 examples 和个人项目案例。
- `v1.0`：形成稳定的个人 AI 工作流系统。
