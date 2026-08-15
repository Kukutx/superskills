# Skill Authoring Guide

用最少文件保存真正影响 Agent 行为的内容。

## 1. Default structure

普通 Skill 默认只有一个文件：

```text
skills/<category>/<skill>/skill.md
```

只有当 `skill.md` 已经无法保持清晰时，才增加：

```text
references/    # Agent 执行任务时按需读取的领域知识
maintenance/   # 来源、回归测试、历史；普通任务不加载
```

不要默认创建 `prompt-template.md`、`examples.md`、`changelog.md`。Git 已经保存历史；简单模板和例子应直接融入 `skill.md`，除非它们本身足够丰富并会改变行为。

## 2. Minimal skill anatomy

一个好的 `skill.md` 通常只需要：

1. YAML `name` + `description`
2. **Use**：什么时候用 / 不用
3. **Workflow / decision rules**：真正值得保留的做法
4. **Output**：默认交付物
5. **Constraints**：最容易犯的错误
6. **Validation**：怎样证明完成

不要重复写 `Purpose`、`Role`、`One-line purpose`、`System Prompt` 来表达同一件事。

## 3. Routing rules

- 领域 Skill 优先于通用方法 Skill。
- 一次先选一个 primary skill。
- secondary skill/reference 只在 primary 无法完整处理时增加。
- 用户要结果时直接执行；不要先输出一段路由说明。
- 用户明确要 prompt 时才使用 prompt optimizer；不要把所有任务先改写成 prompt。

## 4. Categories

| Category | Scope |
| --- | --- |
| `meta` | prompt / skill / routing control |
| `planning` | project execution planning |
| `research` | evidence and comparison |
| `product` | product definition / PRD |
| `development` | software engineering and game development |
| `creative` | image creation / physical creative production |
| `design` | visual product assets and review |
| `ecommerce` | commerce-platform implementation |
| `marketing` | positioning and messaging |
| `writing` | professional copy / communication |
| `operations` | SOP / release / recurring processes |

新 category 只有在现有分类持续造成歧义时才增加。

## 5. When a reference is justified

新增 reference 必须至少满足一项：

- 该领域知识量明显超过主 Skill；
- 只有部分任务需要，按需加载能显著节省 context；
- 它有独立的 decision boundary，例如 combat correctness vs game feel；
- 它包含稳定、可复用的 domain knowledge，而不是临时笔记。

如果删除该 reference 后 Agent 几乎不会改变决策，就不应单独存在。

## 6. Maintenance files

`maintenance/` 可用于：

- routing / regression tests；
- upstream sources / license notes；
- 复杂 Skill 的真实版本历史。

这些文件不应出现在普通 runtime loading path。

## 7. Quality bar

评估 Skill 不看文件数量，而看：

- 是否比通用模型知识多提供了明确决策价值；
- 是否减少错误、猜测或无关输出；
- 是否尊重已有项目结构和用户约束；
- 是否能在信息不足时合理继续，而不是不断提问；
- 是否有与声明匹配的验证路径。

## 8. Anti-noise rules

不要为了“完整”加入：

- 重复的 System Prompt；
- 只有几行的 changelog；
- 把输入字段换个格式再写一次的 prompt template；
- 只有一个普通示例的 examples 文件；
- 退休文件 / compatibility stub；
- 热门但与现有能力重复的外部 Skill；
- 会过时但没有维护价值的具体版本/平台规则。

## 9. External sources

外部资料只吸收**决策规则、anti-pattern、validation pattern**，不要机械复制。

版本敏感 API、平台规则、价格、政策等实施时重新验证。第三方工具默认是 optional dependency，不因“更完整”自动安装。

## 10. Review checklist

新增或修改后检查：

```text
Is this the most specific existing skill?
Does every section change behavior?
Can any file be deleted without losing decision value?
Are runtime references separated from maintenance?
Is one source of truth clear?
Can the result be validated?
```

如果内容只是重复，删除比扩写更好。