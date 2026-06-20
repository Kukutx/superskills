# superskills

`superskills` 是一个个人 AI Skills 仓库，用来沉淀可复用的提示词、工作流、输出规范和领域知识。

这个仓库的目标不是收集零散 prompt，而是把每个高价值场景整理成一个可以长期迭代的 **skill**：有明确目标、输入要求、输出格式、约束规则、示例和反例。

## 设计原则

- **可复用**：每个 skill 都应该能被复制到 ChatGPT、Claude、Cursor 或其他 AI 工具中使用。
- **可执行**：输出格式明确，避免泛泛而谈。
- **可迭代**：每个 skill 都可以通过 examples、changelog 和版本记录持续优化。
- **领域化**：按照场景分类，而不是按照模型或工具分类。
- **少废话**：skill 应该让 AI 更专注，不输出无用内容。

## 目录结构

```txt
superskills/
├── README.md
├── docs/
│   └── skill-writing-guide.md
├── templates/
│   ├── skill-template.md
│   └── prompt-template.md
└── skills/
    ├── creative/
    │   └── xtool-f1-engraving/
    ├── development/
    │   └── code-review/
    ├── ecommerce/
    │   └── shopify-dev/
    ├── design/
    │   └── app-store-assets/
    └── writing/
        └── business-email/
```

## Skill 分类

| 分类 | 用途 |
| --- | --- |
| `creative` | 创意、手工、雕刻、图像生成、产品礼品设计 |
| `development` | 编程、代码审查、架构设计、Debug、DevOps |
| `ecommerce` | Shopify、电商运营、商品页、转化率优化 |
| `design` | App 素材、品牌视觉、应用商店截图、落地页 |
| `writing` | 邮件、商务沟通、说明文档、短文案 |

## 如何使用一个 skill

1. 打开对应目录下的 `skill.md`。
2. 复制「System Prompt」部分到 AI 工具的系统提示词、项目说明或自定义指令中。
3. 使用 `prompt-template.md` 填写当前任务。
4. 将新的好案例补充到 `examples.md`。
5. 每次明显优化后，在 `changelog.md` 记录变化。

## Skill 标准文件

一个完整 skill 建议包含：

```txt
skill-name/
├── skill.md             # 核心规则、角色、约束、输出格式
├── prompt-template.md   # 每次使用时填写的输入模板
├── examples.md          # 好案例、差案例、可复用样例
└── changelog.md         # 版本记录
```

## 当前已初始化的 skills

- `creative/xtool-f1-engraving`：xTool F1 激光雕刻创意设计师
- `development/code-review`：代码审查助手
- `ecommerce/shopify-dev`：Shopify 开发与运营助手
- `design/app-store-assets`：App Store / Google Play 素材设计助手
- `writing/business-email`：商务邮件写作助手

## 版本规划

- `v0.1`：建立仓库结构和第一个可用 skill。
- `v0.2`：补充更多真实 examples。
- `v0.3`：增加 reusable snippets、checklists 和评估标准。
- `v1.0`：形成稳定的个人 AI 工作流库。
