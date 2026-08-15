# Godot 3D behavioral evals

Maintenance-only. Verify the Agent chooses the **smallest useful 3D reference set**, preserves physics/import ownership and does not leak 2D assumptions into 3D work.

## Routing matrix

| Prompt | Expected route | Must avoid |
| --- | --- | --- |
| “Godot 3D 第三人称移动，Camera3D 穿墙” | `spatial-movement-camera.md` | loading rendering/AI refs without need |
| “CharacterBody3D 直接用了 trimesh collision” | `collision-interaction.md` | preserving concave dynamic collision for visual accuracy |
| “准星射线总是选到墙后面的物体” | `collision-interaction.md` + camera context only if needed | UI highlight as interaction truth |
| “Blender 角色导入后比例、朝向和动画都乱了” | `animation-assets.md` | patching each runtime script with magic scale/rotation |
| “AnimationTree root motion 让角色穿墙” | `animation-assets.md` + `spatial-movement-camera.md` | applying animated root transform directly to collision body |
| “夜景很好看但开阴影/GI 后 FPS 掉很多” | `rendering-lighting-world.md` | fixed magic light/shadow budgets without profiling |
| “NavigationAgent3D 到目标附近抖动” | `navigation-ai.md` | throttling required path-following update with AI reasoning |
| “几十个敌人 AI sensing 很重，但移动还要顺” | `navigation-ai.md` | assuming perception and path-following must share one cadence |
| “Godot 3D pause/settings 菜单手柄 focus” | 3D Skill entry + actual project/UI conventions | loading Godot 2D references just to get generic Control knowledge |
| “Godot 2D platformer camera” | outside this Skill -> `development/godot-2d-game-development` | adapting Camera3D/CharacterBody3D guidance |
| “Godot 3D rollback networking” | 3D owns local runtime only; networking architecture elsewhere | pretending these refs cover netcode |

## Pressure cases

### 3D-specific delta only

Prompt: `Godot 3D 项目要做存档。`

Pass: inspect the real project's save/data conventions and use appropriate general design/persistence reasoning; do not manufacture a 3D-specific save architecture or borrow 2D runtime references just because they contain save guidance.

### Physics vs visual rig

Prompt: `动画里的角色向前走了，所以直接把 CharacterBody3D transform 跟着 Skeleton root 走。`

Pass: identify collision-bypass risk; use animation/root-motion delta as controller input when gameplay collision matters.

### Imported asset ownership

Prompt: `我在 Godot 里手改 imported GLB 的骨骼层级，Blender 一保存就丢。`

Pass: keep DCC/import as source of truth and put persistent gameplay changes in a wrapper/inherited/import workflow rather than competing manual edits.

### Collision fidelity

Prompt: `动态角色想直接用完整 mesh 做最准确碰撞。`

Pass: reject visual-fidelity-first collision; choose primitive/convex gameplay shapes unless evidence justifies extra complexity.

### Rendering restraint

Prompt: `这是一个小型 stylized 场景，要不要把 GI、occlusion、MultiMesh、LOD 全开？`

Pass: no. Start with the simplest rendering stack that meets the look, measure the real scene and add only relevant features.

## Regression rule

Before expanding the 3D Skill, answer:

1. Is this knowledge materially different from 2D/general Godot work?
2. Does it change a real 3D implementation decision?
3. Can it live in an existing 3D reference without creating a second owner?
4. Is the rule durable across Godot 4.x, or should it be re-verified at execution time?
5. What behavioral case demonstrates the failure it prevents?

If those answers are weak, do not expand the Skill.
