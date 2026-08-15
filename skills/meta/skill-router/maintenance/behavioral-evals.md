# Skill Router behavioral evals

Maintenance-only. Use these cases to test **ownership**, not keyword matching. A pass selects the smallest useful route and avoids loading unrelated Skills.

## Core routing cases

| User task | Expected primary | Secondary only when | Must avoid |
| --- | --- | --- | --- |
| “帮我优化这段 prompt” | `meta/prompt-optimizer` | another domain is needed to preserve domain constraints | executing the final task instead of returning the prompt |
| “帮我把这个现有 Skill 精简并修路由” | `meta/skill-builder` | none by default | prompt-optimizer just because instructions are being edited |
| “从验证需求到上线，帮我排整个项目” | `planning/project-planner` | domain Skill for a concrete sub-workstream | file-level implementation plan for the whole project |
| “API ownership 和数据模型还没定，怎么设计？” | `development/technical-design` | research when an external/current fact changes the decision | implementation-plan before architecture is fixed |
| “架构已经定了，按仓库告诉我改哪些文件” | `development/implementation-plan` | domain Skill for implementation rules | reopening architecture without a blocker |
| “这个功能线上报错，为什么？” | `development/bug-diagnosis` | domain Skill if one owns the system | generic code-review as a substitute for reproduction |
| “Review 这个 PR 有没有阻塞合并的问题” | `development/code-review` | domain Skill for domain-specific invariants | debugging an unobserved failure |
| “查当前几个库的维护状态和证据，帮我比较” | `research/research-brief` | technical-design if evidence feeds an architecture decision | treating popularity as architecture truth |
| “在已有项目里 Redis 还是数据库该谁拥有这个状态？” | `development/technical-design` | research only if current external evidence is material | research-brief merely because two options are compared |
| “写一个 MVP PRD，不要先设计后端” | `product/prd-builder` | positioning only if audience/value is unresolved | speculative technical architecture |
| “每天重复发布这批内容，整理 SOP” | `operations/sop-builder` | domain Skill for domain-specific execution steps | project-planner for a stable repeated process |
| “这一次发布前做 go/no-go 检查” | `operations/release-checklist` | domain release Skill where available | turning it into a generic SOP |

## Domain precedence cases

| User task | Expected primary | Secondary only when | Must avoid |
| --- | --- | --- | --- |
| “Godot 2D 攻击偶尔重复扣血” | `development/godot-2d-game-development` | generic bug method only if it adds a distinct diagnostic technique | replacing domain combat ownership with generic debugging |
| “生成 6 帧像素 attack strip” | `development/game-dev-spritesheet-slicer` | Godot Skill only when engine import/runtime behavior is also requested | loading the full Godot domain for asset generation alone |
| “Godot 里已有 sprite，配置 AnimationTree 和 attack timing” | `development/godot-2d-game-development` | slicer only if source geometry/assets must change | regenerating art because runtime animation is being configured |
| “Shopify 主题里产品页按钮坏了” | `ecommerce/shopify-dev` | bug-diagnosis only for a distinct generic diagnostic subtask | generic frontend rewrite first |
| “Godot export 到 CI 前检查” | `development/godot-2d-game-development` | generic release-checklist only for broader organization release gates | replacing Godot export rules with generic release ceremony |

## Creative / store boundary cases

| User task | Expected primary | Secondary only when | Must avoid |
| --- | --- | --- | --- |
| “给我设计一组 App Store 截图版式和顺序” | `design/app-store-assets` | app-store-copy for substantial wording work | treating each screenshot as an isolated poster |
| “只重写 App Store subtitle 和 description” | `writing/app-store-copy` | positioning if core value/audience is genuinely unresolved | loading visual asset design |
| “产品定位还不清楚，先确定卖给谁、核心价值是什么” | `marketing/product-positioning` | app-store-copy after positioning is fixed | prematurely polishing store copy |
| “这个生成图已经有了，帮我指出最该改的地方” | `design/image-review-refiner` | domain Skill if the image has domain production constraints | restarting through image-prompt-director by default |
| “我要生成一张新营销主视觉，先给 production-ready prompt” | `creative/image-prompt-director` | domain visual Skill when its constraints own production | image-review-refiner without an existing image |
| “给 xTool F1 做一个能实际雕刻的小徽章” | `creative/xtool-f1-engraving` | image-prompt-director only for a visual-generation subtask | generic illustration rules overriding engraving constraints |

## Pass criteria

A route passes when:

1. one primary Skill owns the task;
2. secondary Skills are added only for separable subtasks;
3. domain ownership beats generic method Skills;
4. comparison wording alone does not force `research-brief`;
5. “plan” wording alone does not force `project-planner`;
6. “review” wording alone does not force `code-review`;
7. direct-result requests do not get routed through prompt optimization;
8. no route loads maintenance material during normal execution.

When a real task fails one of these cases, fix the smallest ownership rule first. Do not add more Skills unless the missing decision cannot be owned cleanly by an existing one.
