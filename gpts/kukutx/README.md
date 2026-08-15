# Kukutx setup

ChatGPT Project 和 Private GPT 使用同一份核心配置，避免重复维护。

## Setup

1. Instructions：`gpts/kukutx/project-instructions.md`
2. Knowledge：先加入 `skills/meta/skill-router/skill.md`
3. 再加入当前项目真正会用到的 domain `skill.md`
4. 复杂 Skill 只加入需要的 `references/`

不要默认上传整个仓库，也不要上传 `maintenance/`。

## Maintenance

- shared behavior 变化 -> 更新 `project-instructions.md`
- Skill catalog 变化 -> 只更新 `skills/meta/skill-router/skill.md`
- domain behavior 变化 -> 更新对应 `skill.md` / reference
- 更新后运行 `python tools/validate_repo.py`

如果回答变弱，优先修 routing 或对应 Skill，不要靠继续堆 Knowledge 文件解决。