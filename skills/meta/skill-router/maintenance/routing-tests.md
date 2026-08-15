# Global Superskills Routing Pressure Tests

Maintenance-only. These cases protect the repository's most important routing boundaries without adding runtime context.

## Pass criteria

- choose one primary skill first;
- specific domain skill beats generic method skill;
- secondary skill is added only for a genuinely distinct subtask;
- project planning, technical design and implementation planning remain separate;
- bug diagnosis and code review remain separate;
- prompt optimization is used only when the prompt itself is the deliverable;
- no route is forced when no Skill adds meaningful value.

## Routing matrix

| Prompt | Expected primary route | Must avoid |
| --- | --- | --- |
| “从想法验证、设计、开发到上线，帮我排整个 app 项目” | `planning/project-planner` | 直接写 file-level implementation plan |
| “这个支付模块谁拥有 transaction state？API 和 DB 怎么设计？” | `development/technical-design` | `project-planner` + `implementation-plan` 全加载 |
| “架构已经定了，按现有 repo 告诉我改哪些文件、什么顺序、怎么测” | `development/implementation-plan` | 重新设计架构 |
| “线上偶发 500，日志在这里，为什么？” | `development/bug-diagnosis` | 把 debugging 变成泛化 code review |
| “review 这个 PR，找 correctness/security regression” | `development/code-review` | 先假设存在 runtime bug |
| “比较这三个数据库方案，给我当前证据和推荐” | `research/research-brief` | project roadmap |
| “把这个 feature idea 整理成 MVP 和验收标准” | `product/prd-builder` | technical architecture first |
| “这个 Godot 2D attack 一刀扣三次血” | `development/godot-2d-game-development` | generic bug-diagnosis as primary |
| “Godot 2D 的命中正确，但 hit-stop/shake 太弱” | `development/godot-2d-game-development` | combat rewrite |
| “把这张 64×64、6 帧一行的 PNG 切成 attack_00..05” | `development/game-dev-spritesheet-slicer` | full Godot runtime skill |
| “用这个角色 seed 生成 8 向 run strips，并保持 anchor 一致” | `development/game-dev-spritesheet-slicer` | generic image prompt only |
| “Shopify 产品页 variant 切换后价格不更新” | `ecommerce/shopify-dev` | generic frontend route as primary |
| “做 App Store screenshot 的整套视觉顺序” | `design/app-store-assets` | generic image direction as primary |
| “只帮我写 App Store subtitle” | `writing/app-store-copy` | app-store-assets |
| “这张已经生成的商店图哪里不对，给下一轮修改” | `design/image-review-refiner` | restart with image-prompt-director |
| “我要从零生成一张产品 hero image，帮我定构图和 prompt” | `creative/image-prompt-director` | image-review-refiner |
| “我们的产品到底应该主打什么用户价值？” | `marketing/product-positioning` | app-store-copy |
| “帮我写一封催合作方确认时间的邮件” | `writing/business-email` | prompt-optimizer |
| “把每周数据发布流程整理成 SOP” | `operations/sop-builder` | project-planner |
| “给这个普通 SaaS release 做 go/no-go、rollback 和监控清单” | `operations/release-checklist` | domain release skill when none exists |
| “帮我把这段 prompt 改得更稳定” | `meta/prompt-optimizer` | execute the downstream task instead |
| “帮我创建一个反复可用的新 Skill” | `meta/skill-builder` | prompt-optimizer |
| “直接帮我完成这个任务，不需要 prompt” | actual domain/task route | `meta/prompt-optimizer` |

## Mixed-task pressure tests

### App Store visual + copy

Prompt: `设计 5 张 App Store screenshots，并给每张一句短标题。`

Pass:
- `design/app-store-assets` primary;
- `writing/app-store-copy` secondary only for copy quality;
- no separate image-prompt skill unless external imagery is actually needed.

### Godot gameplay + sprite production

Prompt: `做一个 Godot 2D sword attack，同时需要生成对应 6 帧 attack strip。`

Pass:
- Godot skill owns gameplay/combat/animation integration;
- spritesheet slicer owns generated strip geometry/packaging;
- image prompt director is not independently loaded unless it adds a distinct visual-direction problem.

### Architecture followed by implementation

Prompt: `先决定 save schema 和 migration boundary，再给我文件级改法。`

Pass:
- technical-design first because architecture is explicitly unresolved;
- implementation-plan may follow after decisions are fixed;
- do not mix both outputs into one vague architecture/task dump.

### Bug in a domain project

Prompt: `Shopify theme 上 mobile menu 偶发打不开，帮我定位。`

Pass:
- Shopify remains primary because platform/theme constraints matter;
- generic bug-diagnosis is at most supporting methodology;
- do not route away from the domain because the user used the word “bug”.

## Maintenance rule

When a new Skill is added or a description changes, add a pressure case only if it protects a real ambiguity with an existing route. Do not grow this into one example per keyword.
