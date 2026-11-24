# Three.js Game Development behavioral evals

Maintenance-only. Protect the Three.js/Godot boundary and the playable-loop-first rule.

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| threejs-game-001 | “用 Three.js 做一个浏览器小游戏，能玩、能通关。” | `development/threejs-game-development` | none | polishing visuals before the core loop is playable, or routing to a Godot skill |
| threejs-game-002 | “用 Godot 做一个 2D 平台跳跃游戏。” | `development/godot-2d-game-development` | none | invoking threejs-game-development for a Godot game |
