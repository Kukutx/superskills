# Godot Project Systems behavioral evals

Maintenance-only. Protect the boundary between dimension-neutral Godot project systems and 2D/3D runtime knowledge.

## Routing cases

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| godot-shared-001 | “Godot 3D 项目的 pause menu 手柄 focus 断了” | `ui-ux.md` | `input-controls-accessibility.md` | loading Camera3D/physics just because the project is 3D |
| godot-shared-002 | “Godot 2D 重映射按键，重启后丢失” | `input-controls-accessibility.md` | `save-persistence.md` as needed | rewriting CharacterBody2D movement |
| godot-shared-003 | “v2 存档 item ID 改名后加载失败” | `save-persistence.md` | none | changing inventory transactions unless evidence points there |
| godot-shared-004 | “背包 stack/equip 逻辑本身错了” | `inventory-progression.md` | none | treating persistence as the runtime owner |
| godot-shared-005 | “branching dialogue 的日文按钮溢出且手柄无法选” | `dialogue-localization.md` | `ui-ux.md` + input as needed | loading 2D/3D world runtime |
| godot-shared-006 | “Godot 项目 SFX bus 和 UI 音量设置混在一起” | `audio.md` | none | introducing a dimensional audio architecture without need |
| godot-shared-007 | “GitHub Actions clean export” | `release-export-ci.md` | none | routing through a dimensional Skill for export |
| godot-shared-008 | “修完菜单后怎么证明 gamepad 真能操作？” | `verification-testing.md` | UI/input as needed | claiming success from static inspection only |
| godot-shared-009 | “CharacterBody2D dash 穿墙” | `development/godot-2d-game-development` | none | generic project-system advice replacing 2D physics |
| godot-shared-010 | “CharacterBody3D camera 穿墙” | `development/godot-3d-game-development` | none | generic project-system advice replacing 3D spatial rules |

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
