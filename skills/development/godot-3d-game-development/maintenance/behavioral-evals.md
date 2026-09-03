# Godot 3D behavioral evals

Maintenance-only. Verify the Agent chooses the **smallest useful 3D reference set**, preserves spatial ownership and hands dimension-neutral concerns to `development/godot-project-systems`.

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| godot3d-001 | “Godot 3D 第三人称移动，Camera3D 穿墙” | `spatial-movement-camera.md` | none | loading rendering/AI/shared refs without need |
| godot3d-002 | “CharacterBody3D 直接用了 trimesh collision” | `collision-interaction.md` | none | preserving concave dynamic collision for visual accuracy |
| godot3d-003 | “准星射线总是选到墙后面的物体” | `collision-interaction.md` | camera context only if needed | UI highlight as interaction truth |
| godot3d-004 | “Blender 角色导入后比例、朝向和动画都乱了” | `animation-assets.md` | none | patching runtime scripts with scattered scale/rotation offsets |
| godot3d-005 | “AnimationTree root motion 让角色穿墙” | `animation-assets.md` | `spatial-movement-camera.md` | applying animated root transform directly to collision body |
| godot3d-006 | “夜景很好看但开阴影/GI 后 FPS 掉很多” | `rendering-lighting-world.md` | none | fixed magic light/shadow budgets without profiling |
| godot3d-007 | “NavigationAgent3D 到目标附近抖动” | `navigation-ai.md` | none | throttling required path-following update with AI reasoning |
| godot3d-008 | “几十个敌人 AI sensing 很重，但移动还要顺” | `navigation-ai.md` | none | assuming perception and path-following must share one cadence |
| godot3d-009 | “Godot 3D pause/settings 菜单手柄 focus” | `development/godot-project-systems` | none | loading 3D movement/rendering for Control UI |
| godot3d-010 | “Godot 3D 存档迁移 / inventory / dialogue / audio bus / export CI” | `development/godot-project-systems` | none | manufacturing 3D-specific versions of shared systems |
| godot3d-011 | “Godot 2D platformer camera” | `development/godot-2d-game-development` | none | adapting Camera3D/CharacterBody3D guidance |
| godot3d-012 | “Godot 3D rollback networking” | `development/godot-3d-game-development` | networking architecture elsewhere | pretending these refs cover netcode |

## Pressure cases

### Physics vs visual rig

If animation visually moves the character, do not copy the animated model/root transform directly into the collision authority. Root-motion data must be reconciled through the controller when collision matters.

### Imported asset ownership

If manual edits to imported assets disappear on re-import, keep DCC/import as source of truth and put persistent gameplay changes in a wrapper/inherited/import workflow.

### Collision fidelity

For moving actors, do not choose full detailed mesh collision merely for visual accuracy. Primitive/convex gameplay shapes remain the default unless evidence justifies more complexity.

### Rendering restraint

A small stylized scene does not need GI, occlusion, MultiMesh and LOD just because those features exist. Start simple, measure, and add only relevant tools.

### Shared systems boundary

`Godot 3D 项目要做存档和 pause menu。` -> shared project-systems owns persistence/UI. Do not create a 3D-specific save/UI architecture.

## Regression rule

Before expanding the 3D Skill, answer:

1. Is this knowledge materially different from dimension-neutral Godot work?
2. Does 3D change a real implementation decision?
3. Can it live in an existing 3D reference without creating a second owner?
4. Is the rule durable across Godot 4.x, or should it be re-verified at execution time?
5. What behavioral case demonstrates the failure it prevents?

If those answers are weak, use the shared project-systems owner or keep the current structure.
