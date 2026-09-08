# Skill Authoring Guide

只保存**会改变 Agent 决策、执行或验证方式**的内容。

## Default structure

普通 Skill：

```text
skills/<category>/<skill>/skill.md
```

只有复杂 Skill 才增加：

```text
references/    # runtime 按需读取
maintenance/   # runtime 不加载
```

不要默认创建 prompt template、examples、changelog、compatibility stub 或重复 README。

## Minimal `skill.md`

通常只需要：

1. YAML `name` + routing-quality `description`
2. Scope / Use：它真正拥有哪类任务
3. Durable decision rules / invariants
4. Domain inputs / true blockers
5. Reference routing：复杂 Skill 才需要
6. Constraints / anti-patterns
7. Validation / completion boundary

不要用 Purpose、Role、System Prompt 多次表达同一件事。

## Agentic baseline

新的高能力 Agent 不需要每个 Skill 都重复教它“先计划、先询问、先确认、再执行”。这类通用行为由 `gpts/kukutx/project-instructions.md` 统一拥有。

Skill 应优先保存：

```text
requested outcome ownership
domain invariants / source of truth
what facts materially change the decision
what the agent may safely infer or discover
real blocker / irreversible boundary
what evidence proves completion
```

而不是：

```text
generic plan-first ritual
generic permission checks
generic tool-use instructions
step-by-step prose that a capable agent can infer
```

如果用户要求执行，Skill 应帮助 Agent 执行，不应因为任务复杂就把交付物偷偷改成计划。多步骤工作本身不是 `project-planner` 的路由条件。

模型、API、工具和平台能力会变化。只有当它们会改变当前决策时才在执行阶段验证；不要把短期模型行为、版本号或固定工具清单写成长期 runtime truth。

## Routing

唯一完整 Skill catalog：

```text
skills/meta/skill-router/skill.md
```

原则：

- specific domain > generic method > meta helper；
- 一次先选一个 primary Skill；
- secondary Skill/reference 只处理可分离子问题；
- 不按关键词机械匹配；
- prompt optimizer 只在 prompt 本身是交付物时使用；
- execution request 不因为“步骤很多”自动变成 planning request。

Catalog 只维护在 Router 的 `## Catalog` 表格中。新增、删除或重命名 Skill 时，每个非 Router Skill 必须在该表格**恰好出现一次**。

## Autonomy and escalation ownership

全局的自治、询问、批准和 scope 规则由 `gpts/kukutx/project-instructions.md` 持有。普通 Skill 不要复制一套通用的“信息不足就询问”或“执行前先确认”长文。

领域 Skill 只补充该领域真正会改变结果的输入和阻塞条件，例如：

- 简历需要真实职位、日期、经历和目标岗位；
- 技术设计需要数据所有权、一致性和迁移约束；
- 雕刻需要材料、尺寸和实际工艺。

按缺口类型处理：

```text
supplied/discoverable fact -> inspect or retrieve it
harmless reversible choice -> choose the smallest convention-aligned default
user-only truth / preference -> ask only when it materially blocks correctness or direction
consequential irreversible action -> prepare the concrete result first, then escalate at the boundary
```

好的边界应同时避免：

```text
核心事实完全未知却伪造
公开/已提供信息仍让用户重复提供
可逆工作明明能继续却停在询问或计划
真正不可逆的高影响动作却静默替用户决定
```

剩余不确定性如果不会合理地改变主方向、事实正确性或不可逆操作，就继续执行，不追求无意义的绝对确定。

## When to split a reference

只有存在真实 decision boundary 才拆。例如：

```text
combat correctness != game feel
movement/physics != camera framing
AI/navigation != procedural generation
save/migration != inventory runtime mechanics
sprite asset production != engine runtime animation
verification != performance != release
```

Reference 至少应满足一项：

- 只有部分任务需要，拆分明显减少 runtime context；
- 有独立 owner/validation；
- 合并会让路由或 source-of-truth 模糊。

**拆分是移动 ownership，不是复制内容。** 主 `skill.md` 只保留路由和跨域 invariant。每个 runtime reference 必须通过正式 Markdown 链接或明确的 Markdown code path 从主入口可发现。

不要嵌套 `references/` 子目录；保持一层、可路由、可验证。

## Maintenance standard

Runtime 不加载 `maintenance/`。

只使用：

```text
behavioral-evals.md   # routing/ownership/autonomy review fixtures
sources.md            # substantial upstream/source inventory
decisions.md          # only when current rationale cannot be inferred
```

Git history 已经是 changelog；不要维护版本流水账。

时效性 API、插件、版本、模型行为和市场快照在执行时重新验证，不写成永久 runtime truth。

较重要的来源记录应包含：

```text
canonical URL
它支持的决策或边界
最后复查年月
```

来源清单用于可追踪维护，不是运行时推荐榜单。

## Behavioral evals

当新增或修改 ownership、autonomy 或 blocker boundary 时，加**最少量**能防真实回归的例子。测试应证明“为什么这个边界存在”，而不是给每个关键词写一个例子。

唯一格式：

```markdown
| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| example-001 | 用户任务 | `category/skill` | 可选 | 禁止行为 |
```

列名必须严格使用 `ID`、`Prompt`、`Primary`、`Secondary`、`Must avoid`。不维护旧列名兼容。显式 `ID` 在整个仓库中必须唯一。

导出为机器可读 JSONL：

```bash
python tools/export_behavioral_evals.py --check
python tools/export_behavioral_evals.py --output dist/behavioral-evals.jsonl
```

这些文件仍是人工/Agent review fixtures，CI 只验证结构、路径和可导出性；它不等于真实模型已经通过语义评测。实际模型评测应消费导出的 JSONL，并把模型、配置和结果分开记录。

优先测试：

- 最容易混淆的相邻 Skill/reference；
- domain vs generic method；
- correctness vs polish；
- asset/source vs runtime truth；
- 核心事实不足应询问 vs 信息已提供/可发现不应重复询问；
- 已授权可逆工作应继续 vs 真正不可逆边界应升级；
- execution request vs roadmap deliverable；
- 小改动的必要验证 vs 无意义的过度测试；
- 一次性任务 vs repeated SOP/process。

## Dependencies

优先：

```text
existing project pattern
-> native platform/framework capability
-> focused dependency only if recurring pain remains
```

采用第三方前检查当前 compatibility、maintenance、license、overlap、source-of-truth、upgrade/removal cost。

## Anti-noise

不要为了“更完整”加入：

- 重复 System Prompt / role prose；
- 重复的 plan/ask/confirm/tool-use 通用循环；
- 一次性普通 examples file；
- changelog；
- retired/compatibility stub；
- runtime 中的 source/tool inventory；
- 同一规则在多个 reference 复制维护；
- 容易过期且不改变长期决策的版本、模型或工具列表。

## Validation

仓库工具统一使用 Python 3.14。修改后运行：

```bash
python -m unittest discover -s tests -v
python tools/validate_repo.py
python tools/export_behavioral_evals.py --check
```

Validator 负责：

- 扫描所有 `skill.md`，并拒绝错误层级；
- frontmatter、folder naming、duplicate Skill names；
- Skill 目录形状；
- runtime reference 必须是一层 Markdown，并通过真实链接/code path 从入口可发现；
- maintenance 只允许当前规范文件，并且不混入 runtime；
- 只解析 Router `## Catalog` 表格，检查完整、重复和 stale route；
- behavioral eval 必须使用唯一 canonical 表格格式；
- behavioral eval 中显式 Skill route 与本地 reference 仍存在；
- 标准 Markdown 链接及 code path 无 dead link 或仓库逃逸；
- 对异常大的 runtime entrypoint/reference 给出非阻塞 advisory。

结构规则能自动检查时优先写进 Validator，并同时增加 Validator 自身的回归测试。

## Runtime bundle

不要手工复制整仓库到 GPT Knowledge。使用可重复构建：

```bash
python tools/build_bundle.py \
  --profile gpts/kukutx \
  --skill development/godot-project-systems \
  --reference development/godot-project-systems:ui-ux \
  --reference development/godot-project-systems:input-controls-accessibility
```

Bundle 自动包含 Project Instructions、Router、选中的 Skill 和 reference，并拒绝 `maintenance/`。`manifest.json` 记录源提交、文件哈希、字节数和粗略 Token 预算。

## Review test

提交前只检查：

```text
Does this change behavior?
Is ownership unambiguous?
Can the agent use available context/tools and make reversible progress before asking?
Does any pause/approval rule correspond to a real domain blocker or consequential boundary?
Does requested execution remain execution rather than becoming a plan?
Can less runtime context solve the same task?
Is source-of-truth singular?
Is maintenance separated from runtime?
Is verification proportional to the completion claim and risk?
```

如果改动只是“看起来更完整”，通常应该删除或留在 maintenance。
