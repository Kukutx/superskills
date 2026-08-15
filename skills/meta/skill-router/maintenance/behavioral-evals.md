# Skill Router behavioral evals

Maintenance-only. Test **task ownership**, not keyword matching. A pass selects the smallest useful route and avoids unrelated Skills.

## Core cases

| User task | Expected primary | Secondary only when | Must avoid |
| --- | --- | --- | --- |
| “帮我优化这段 prompt” | `meta/prompt-optimizer` | domain constraints must be preserved | executing the downstream task instead |
| “精简这个现有 Skill 并修路由” | `meta/skill-builder` | none by default | prompt-optimizer just because instructions are edited |
| “从验证需求到上线，排整个项目” | `planning/project-planner` | domain Skill for a concrete workstream | file-level plan for the whole project |
| “API ownership 和数据模型还没定” | `development/technical-design` | research if current external evidence changes the decision | implementation-plan before architecture is fixed |
| “架构定了，按仓库告诉我改哪些文件” | `development/implementation-plan` | domain Skill for implementation rules | reopening architecture without a blocker |
| “线上报错，为什么？” | `development/bug-diagnosis` | domain Skill if one owns the system | code-review as a substitute for reproduction |
| “Review 这个 PR 有没有阻塞合并的问题” | `development/code-review` | domain Skill for domain invariants | inventing a runtime failure |
| “查当前几个库的维护状态和证据” | `research/research-brief` | technical-design if evidence feeds architecture | popularity as architecture truth |
| “Redis 还是数据库该谁拥有这个状态？” | `development/technical-design` | research only if current evidence is material | research merely because options are compared |
| “写一个 MVP PRD，不要先设计后端” | `product/prd-builder` | positioning if audience/value is unresolved | speculative architecture |
| “每天重复发布这批内容，整理 SOP” | `operations/sop-builder` | domain Skill for domain steps | project-planner for a stable process |
| “这一次发布前做 go/no-go 检查” | `operations/release-checklist` | domain release Skill where available | turning one release into an SOP |

## Domain precedence

| User task | Expected primary | Secondary only when | Must avoid |
| --- | --- | --- | --- |
| “Godot 2D 攻击偶尔重复扣血” | `development/godot-2d-game-development` | generic debug method adds distinct value | replacing domain combat ownership |
| “Godot 2D scene ownership/state architecture” | `development/godot-2d-game-development` | technical-design only for a distinct cross-system method | generic architecture replacing Godot conventions |
| “架构已定，直接改 Godot 2D 现有项目里的文件” | `development/godot-2d-game-development` | implementation-plan only when a plan artifact is explicitly useful | generic file planning replacing domain implementation |
| “Godot 3D 第三人称移动和 Camera3D 穿墙” | `development/godot-3d-game-development` | generic debug method adds distinct value | forcing 2D camera/movement references |
| “Godot 3D Blender 模型导入后骨骼和动画异常” | `development/godot-3d-game-development` | research only if a current importer/version fact is material | generic asset advice replacing Godot import semantics |
| “生成 6 帧像素 attack strip” | `development/sprite-animation-pipeline` | Godot only if engine import/runtime is also requested | loading full Godot runtime for asset generation |
| “把已有 64x64 sheet 切成稳定命名并打包” | `development/sprite-animation-pipeline` | engine Skill for actual handoff | image-generation Skill |
| “Godot 2D 已有 sprite，配置 runtime attack timing” | `development/godot-2d-game-development` | sprite pipeline only if source geometry must change | regenerating art unnecessarily |
| “Shopify 产品页按钮坏了” | `ecommerce/shopify-dev` | bug-diagnosis for distinct methodology | generic frontend rewrite first |
| “Shopify theme release 前检查” | `ecommerce/shopify-dev` | release-checklist for broader org gates | generic release ceremony replacing platform rules |
| “Godot export 到 CI 前检查” | matching Godot 2D/3D Skill | release-checklist for broader release gates | replacing Godot export rules with generic checklist |

## Creative / store boundaries

| User task | Expected primary | Secondary only when | Must avoid |
| --- | --- | --- | --- |
| “设计一组 App Store 截图版式和顺序” | `design/app-store-assets` | app-store-copy for substantial wording | isolated-poster thinking |
| “已有 App Store screenshot，帮我改善” | `design/app-store-assets` | image-review-refiner for generic visual diagnosis | generic image route replacing store constraints |
| “只重写 subtitle 和 description” | `writing/app-store-copy` | positioning if value/audience is unresolved | loading visual design |
| “产品到底卖给谁、核心价值是什么” | `marketing/product-positioning` | downstream copy after positioning is fixed | polishing store copy first |
| “这个生成图哪里最该改” | `design/image-review-refiner` | domain Skill for production constraints | restarting from scratch by default |
| “从零生成营销主视觉 prompt” | `creative/image-prompt-director` | domain visual Skill when it owns production | image-review without an existing image |
| “给 xTool F1 做可实际雕刻的小徽章” | `creative/xtool-f1-engraving` | image-prompt-director for a distinct generation subtask | generic illustration overriding engraving constraints |

## Mixed-task pressure cases

### Godot gameplay + sprite asset

Prompt: `做 Godot 2D sword attack，同时生成对应 6 帧 attack strip。`

Pass: Godot 2D owns gameplay/combat/runtime animation; sprite pipeline owns strip generation/geometry/packaging; do not add a third image Skill unless visual direction is genuinely unresolved.

### Godot dimension boundary

Prompt: `这是 Godot 3D 项目，但只是改 pause menu 的 Control focus。`

Pass: choose the 3D domain owner/project conventions if domain context matters, but do not load 2D runtime references merely because they contain generic UI knowledge. The dimension-neutral subproblem must not trigger a fake 2D dependency.

### Architecture then implementation

Prompt: `先决定 save schema 和 migration boundary，再给文件级改法。`

Pass: technical-design first; implementation-plan only after decisions are fixed; keep the two outputs distinct.

### Domain bug

Prompt: `Shopify theme mobile menu 偶发打不开。`

Pass: Shopify remains primary; generic bug-diagnosis is at most supporting methodology.

### Direct-result request

Prompt: `直接帮我完成这个任务，不需要 prompt。`

Pass: actual domain/task owner; never prompt-optimizer as preprocessing.

## Pass criteria

1. One primary Skill owns the task.
2. Secondary Skills handle separable subtasks only.
3. Domain ownership beats generic methods.
4. “compare”, “plan”, “review” and “prompt” words do not route by themselves.
5. Godot 2D and 3D stay separate when dimension changes implementation.
6. Asset production and engine runtime remain separate owners.
7. Maintenance content is not loaded during normal execution.

When a real task fails, fix the smallest ownership rule first. Do not add a new Skill unless existing owners cannot cleanly represent the missing decision.
