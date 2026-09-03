# Kukutx setup

ChatGPT Project 和 GPT 使用同一份核心配置，避免重复维护。

## Recommended: reproducible bundle

```bash
python tools/build_bundle.py \
  --profile gpts/kukutx \
  --skill writing/resume-writing
```

复杂 Skill 只追加当前任务需要的 reference：

```bash
python tools/build_bundle.py \
  --profile gpts/kukutx \
  --skill development/godot-project-systems \
  --reference development/godot-project-systems:ui-ux \
  --reference development/godot-project-systems:input-controls-accessibility
```

默认输出到 `dist/kukutx/`。`manifest.json` 记录源提交、包含文件、SHA-256、字节数和粗略 Token 预算。构建器只接受已选择 Skill 的 reference，并拒绝把 `maintenance/` 放入 runtime bundle。

## Manual setup

1. Instructions：`gpts/kukutx/project-instructions.md`
2. Knowledge：`skills/meta/skill-router/skill.md`
3. 再加入当前项目真正会用到的 domain `skill.md`
4. 复杂 Skill 只加入需要的 `references/`

不要默认上传整个仓库，也不要上传 `maintenance/`。

## Maintenance

- shared behavior 变化 -> 更新 `project-instructions.md`
- Skill catalog 变化 -> 只更新 Router `## Catalog`
- domain behavior 变化 -> 更新对应 `skill.md` / reference
- routing/ownership 边界变化 -> 更新最小 behavioral eval 集
- 更新后运行测试、Validator 和 eval export check

如果回答变弱，优先修 routing、澄清边界或对应 Skill，不要靠继续堆 Knowledge 文件解决。
