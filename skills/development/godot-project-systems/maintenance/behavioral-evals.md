# Godot Project Systems behavioral evals

Maintenance-only. Protect the boundary between dimension-neutral Godot project systems and 2D/3D runtime knowledge.

## Routing cases

| Prompt | Expected route | Must avoid |
| --- | --- | --- |
| “Godot 3D 项目的 pause menu 手柄 focus 断了” | `ui-ux.md` + `input-controls-accessibility.md` | loading Camera3D/physics just because the project is 3D |
| “Godot 2D 重映射按键，重启后丢失” | input + `save-persistence.md` as needed | rewriting CharacterBody2D movement |
| “v2 存档 item ID 改名后加载失败” | `save-persistence.md` | changing inventory transactions unless evidence points there |
| “背包 stack/equip 逻辑本身错了” | `inventory-progression.md` | treating persistence as the runtime owner |
| “branching dialogue 的日文按钮溢出且手柄无法选” | `dialogue-localization.md` + `ui-ux.md` + input as needed | loading 2D/3D world runtime |
| “Godot 项目 SFX bus 和 UI 音量设置混在一起” | `audio.md` | introducing a dimensional audio architecture without need |
| “GitHub Actions clean export” | `release-export-ci.md` | routing through Godot 2D merely because its old ref used to own export |
| “修完菜单后怎么证明 gamepad 真能操作？” | `verification-testing.md` + UI/input | claiming success from static inspection only |
| “CharacterBody2D dash 穿墙” | outside this Skill -> `development/godot-2d-game-development` | generic project-system advice replacing 2D physics |
| “CharacterBody3D camera 穿墙” | outside this Skill -> `development/godot-3d-game-development` | generic project-system advice replacing 3D spatial rules |

## Ownership cases

### Combat vs Health/Vitals

Prompt: `攻击命中了，谁负责扣血、无敌帧和死亡？`

Pass: conceptual ownership is explicit: attack/combat resolver owns hit validity and damage result calculation; Health/Vitals owns current HP, invulnerability state and alive/dead result. A small project may combine them in one node, but there must not be competing truths.

### UI is not domain state

Prompt: `Inventory GridContainer 里现在有几个格子，就拿它当实际背包数量。`

Pass: reject UI-as-data ownership; inventory data owns state and UI renders it.

### Save is representation

Prompt: `存档文件写了 hp=0，所以加载前直接让 SaveManager 决定角色死亡。`

Pass: save provides durable representation; load/apply passes data to the owning runtime domain rather than creating a second gameplay authority.

## Regression rule

Add a shared reference only when the behavior is genuinely dimension-neutral and is required in both 2D and 3D projects. If spatial or 2D semantics materially change implementation, keep ownership in the matching dimensional Skill.
