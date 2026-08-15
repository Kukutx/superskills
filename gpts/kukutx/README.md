# Kukutx setup

`superskills` 在 ChatGPT Project 和 Private GPT 中使用同一套核心配置，避免维护两份几乎相同的 instructions。

## ChatGPT Project

1. 将 `project-instructions.md` 用作 Project Instructions。
2. 先加入 `knowledge-pack.md`。
3. 高频领域再按 `knowledge-files.md` 加对应 `skill.md` / `references/`。

## Private GPT

同样使用：

- Instructions: `project-instructions.md`
- Knowledge first: `knowledge-pack.md`
- Additional knowledge: 按 `knowledge-files.md` 选择
- Starter ideas: `conversation-starters.md`

不要把整个仓库一次性塞进 Knowledge。复杂 Skill 只加入当前项目真正需要的 references。

## Maintenance

仓库更新后：

1. routing/defaults 变化 -> 更新 `knowledge-pack.md`；
2. domain behavior 变化 -> 更新对应 `skill.md` / reference；
3. 重新同步发生变化的 Knowledge 文件；
4. 用真实任务验证，不靠继续增加文件解决弱路由。
