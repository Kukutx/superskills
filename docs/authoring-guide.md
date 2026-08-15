# Skill Authoring Guide

只保存**会改变 Agent 决策、执行或验证方式**的内容。

## Default structure

普通 Skill：

```text
skills/<category>/<skill>/skill.md
```

复杂 Skill 才增加：

```text
references/    # runtime 按需读取
maintenance/   # runtime 不加载
```

不要默认创建 prompt template、examples、changelog、compatibility stub 或重复 README。

## Minimal `skill.md`

通常只需要：

1. YAML `name` + routing-quality `description`
2. Scope / Use：它真正拥有哪类任务
3. Workflow / decision rules
4. Reference routing：复杂 Skill 才需要
5. Constraints / anti-patterns
6. Validation / completion boundary

不要用 Purpose + Role + System Prompt 多次表达同一件事。

## Routing

唯一完整 Skill catalog：

```text
skills/meta/skill-router/skill.md
```

原则：

- specific domain > generic method > meta helper;
- 一次先选一个 primary Skill;
- secondary Skill/reference 只处理可分离子问题;
- 不按关键词机械匹配；
- prompt optimizer 只在 prompt 本身是交付物时使用。

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

**拆分是移动 ownership，不是复制内容。** 主 `skill.md` 只保留路由和跨域 invariant。每个 runtime reference 必须从主入口可发现。

不要嵌套 `references/` 子目录；保持一层、可路由、可验证。

## Maintenance standard

Runtime 不加载 `maintenance/`。

推荐名称：

```text
behavioral-evals.md   # routing/ownership regression cases
sources.md            # substantial upstream/source inventory when truly useful
decisions.md          # only when current design rationale cannot be inferred from code/docs
```

Git history 已经是 changelog；不要维护版本流水账。旧 `routing-tests.md` 统一合并为 `behavioral-evals.md`。

时效性 API、插件、版本、市场快照在执行时重新验证，不写成永久 runtime truth。

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
- 一次性普通 examples file；
- changelog；
- retired/compatibility stub；
- runtime 中的 source/tool inventory；
- 同一规则在多个 reference 复制维护；
- 容易过期且不改变长期决策的具体版本/工具列表。

## Behavioral evals

当新增/修改 ownership boundary 时，加**最少量**能防真实回归的例子。测试应证明“为什么这个边界存在”，而不是给每个关键词写一个例子。

优先测试：

- 最容易混淆的相邻 Skill/reference；
- domain vs generic method；
- correctness vs polish；
- asset/source vs runtime truth；
- 一次性任务 vs repeated SOP/process。

## Validation

修改后运行：

```bash
python tools/validate_repo.py
```

Validator 负责：

- frontmatter / folder naming / duplicate Skill names；
- Skill 目录形状；
- runtime reference 必须是一层 Markdown 且从入口可发现；
- maintenance 内容不混入 runtime；
- 禁止旧 routing-tests/changelog maintenance 形状；
- Router catalog 完整且无 stale route；
- maintenance eval 中显式 Skill route 仍存在；
- runtime Markdown 路径无 dead link；
- 对异常大的 runtime entrypoint/reference 给出非阻塞 advisory。

结构规则能自动检查时优先写进 validator，而不是只靠文档提醒。

## Review test

提交前只问：

```text
Does this change behavior?
Is ownership unambiguous?
Can less runtime context solve the same task?
Is source-of-truth singular?
Is maintenance separated from runtime?
Can completion be validated?
```

如果改动只是“看起来更完整”，通常应该删掉或留在 maintenance。
