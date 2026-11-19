---
description: sprite-animation-pipeline splits generation per action/direction instead of one giant sheet
runs: 2
max_turns: 6
allowed_tools: [Skill]
---

我有一张 64x64 的像素风主角立绘（俯视角，右手拿剑）。想用 AI 生图做 idle、walk、run、attack、die 五个动作，上下左右 4 个方向，每个动作统一 8 帧。帮我写一个提示词，一次性把整张 spritesheet 生成出来，我直接导进 Godot。
