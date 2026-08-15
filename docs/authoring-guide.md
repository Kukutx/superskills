# Skill Authoring Guide

只保存**会改变 Agent 决策或验证方式**的内容。

## Default structure

普通 Skill：

```text
skills/<category>/<skill>/skill.md
```

复杂 Skill 才增加：

```text
references/    # runtime 按需读取
maintenance/   # sources/tests/history；runtime 不加载
```

不要默认创建 prompt template、examples、changelog 或 compatibility stub。

## Minimal `skill.md`

通常只需要：

1. YAML `name` + `description`
2. **Scope / Use**：什么时候属于它
3. **Workflow / decision rules**：真正影响决策的规则
4. **Reference routing**：什么时候才读哪个深层文件
5. **Output**：默认交付物
6. **Constraints**：高概率错误
7. **Validation**：怎样证明完成

不要用 `Purpose + Role + One-line purpose + System Prompt` 重复表达同一件事。

## Routing

唯一完整 Skill catalog：

```text
skills/meta/skill-router/skill.md
```

不要在 README、Project Instructions、knowledge manifest 等位置复制整张路由表。

原则：

- specific domain > generic method > meta helper;
- 一次先选一个 primary Skill;
- secondary Skill/reference 只处理明确子问题;
- 用户要结果时直接执行，不先展示路由过程;
- prompt optimizer 只在用户真正需要 prompt 时使用。

## When to split a reference

只有满足明确 decision boundary 才拆，例如：

```text
combat correctness != game feel
generated sprite workflow != existing-sheet packaging
runtime verification != performance profiling != release/export
```

Reference 至少应满足一项：

- 只有部分任务需要，拆分能明显减少 context；
- 内容足够独立且可复用；
- 合并后会让主 Skill 路由/职责不清。

拆分时遵守：

```text
move ownership, do not duplicate ownership
skill.md keeps routing/summary
reference keeps the detailed rule
```

每个 runtime reference 都必须从所属 `skill.md` 可发现，并能解释**什么时候加载、什么时候不要加载**。如果删除 reference 几乎不会改变 Agent 决策，就不要单独存在。

## Runtime vs maintenance

Runtime (`skill.md` / `references/`) 只保留稳定执行知识。

`maintenance/` 放：

- upstream/source/tool inventory;
- routing/regression tests;
- complex Skill history;
- license/review notes.

不要把 `Source synthesis`、工具市场快照、版本历史塞进 runtime reference。时效性 API/平台/插件信息在实际任务时重新验证。

## Dependencies

优先：

```text
existing project pattern
-> native platform/framework capability
-> focused external dependency only if real pain remains
```

第三方工具不是“知识更完整”的默认答案。采用前检查当前 compatibility、maintenance、license、overlap、source-of-truth 和 removal cost。

## Anti-noise

不要为了完整加入：

- 重复 System Prompt;
- 几行 changelog;
- 输入字段的另一种格式;
- 单个普通 example file;
- retired/compatibility stub;
- maintenance source notes in runtime;
- 具体但容易过期、且不影响长期决策的工具/version 列表。

## Validation

修改后运行：

```bash
python tools/validate_repo.py
```

CI 也会运行相同检查。目前 validator 负责：

- Skill frontmatter / folder naming;
- Skill 目录只允许 `skill.md`, `references/`, `maintenance/`;
- maintenance material 不进入 runtime references;
- 每个 runtime reference 都能从所属 `skill.md` 被发现;
- Router catalog 不漏 Skill、没有 stale Skill;
- runtime 中显式 Markdown 路径不存在 dead link。

结构规则新增时优先加 validator，而不是只写一句文档提醒。

## Review test

提交前只问：

```text
Does this content change behavior?
Is ownership/routing unambiguous?
Can less context solve the same task?
Is runtime separated from maintenance?
Can the claim be validated?
```

如果答案只是“更完整”，通常应删除或留在 maintenance，而不是扩写 runtime。
