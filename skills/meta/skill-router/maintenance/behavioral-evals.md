# Skill Router behavioral evals

Maintenance-only. Test **task ownership**, not keyword matching. A pass selects the smallest useful route and avoids unrelated Skills.

## Core cases

| User task | Expected primary | Secondary only when | Must avoid |
| --- | --- | --- | --- |
| “帮我优化这段 prompt” | `meta/prompt-optimizer` | domain constraints must be preserved | executing the downstream task instead |
| “精简这个现有 Skill 并修路由” | `meta/skill-builder` | none by default | prompt-optimizer just because instructions are edited |
| “从验证需求到上线，排整个项目” | `planning/project-planner` | domain Skill for a concrete workstream | file-level plan for the whole project |
| “找 5 个最适合 10 秒剪辑的跳伞视频，主流平台，能下载” | `research/web-discovery` | research only for a distinct factual policy question | inventing free/commercial-use/copyright-safe filters |
| “给我 TikTok / Instagram 上最好的滑雪素材，不要素材站” | `research/web-discovery` | none by default | substituting stock/aggregator sites or reintroducing rejected filters |
| “比较 TikTok、Instagram、YouTube 当前的下载或授权政策” | `research/research-brief` | web-discovery only if the user separately asks for actual clips/pages | treating media relevance as the policy question |
| “API ownership 和数据模型还没定” | `development/technical-design` | research if current external evidence changes the decision | implementation-plan before architecture is fixed |
| “架构定了，按仓库告诉我改哪些文件” | `development/implementation-plan` | domain Skill for implementation rules | reopening architecture without a blocker |
| “线上报错，为什么？” | `development/bug-diagnosis` | domain Skill if one owns the system | code-review as a substitute for reproduction |
| “Review 这个 PR 有没有阻塞合并的问题” | `development/code-review` | domain Skill for domain invariants | inventing a runtime failure |
| “查当前几个库的维护状态和证据” | `research/research-brief` | technical-design if evidence feeds architecture | popularity as architecture truth |
| “Redis 还是数据库该谁拥有这个状态？” | `development/technical-design` | research only if current evidence is material | research merely because options are compared |
| “写一个 MVP PRD，不要先设计后端” | `product/prd-builder` | positioning if audience/value is unresolved | speculative architecture |
| “每天重复发布这批内容，整理 SOP” | `operations/sop-builder` | domain Skill for domain steps | project-planner for a stable process |
| “这一次发布前做 go/no-go 检查” | `operations/release-checklist` | domain release Skill where available | turning one release into an SOP |

## Personal-analysis boundaries

| User task | Expected primary | Secondary only when | Must avoid |
| --- | --- | --- | --- |
| “1992 年生，按八字看事业和近三年运势” | `personal/divination-reading` | research only for a genuinely external calendrical/current fact | presenting symbolic interpretation as empirical evidence |
| “我没指定方法，只想占一下这个 offer 值不值得接” | `personal/divination-reading` | none by default | stacking every divination system |
| “1992 年生，在中国长大，结合互联网和就业环境分析成长背景” | `personal/generational-context-analysis` | research for a distinct evidence brief | divination merely because a birth date appears |
| “出生在 1995 年的人是不是都回避型依恋？” | `personal/generational-context-analysis` | research for cohort evidence | claiming attachment style from birth year |
| “我每次重要工作都拖到最后，想理解这个模式并改变” | `personal/psychology-reflection` | research only for a distinct evidence question | diagnosing ADHD or explaining the user's whole personality from procrastination |
| “我一有冲突就沉默，之后又后悔，帮我看看这个循环” | `personal/psychology-reflection` | none by default | assigning a fixed attachment type or inventing childhood trauma |
| “我对象最近很冷淡，他是不是 NPD？” | `personal/psychology-reflection` | current clinical evidence only if the user shifts to a genuine diagnostic-information question | diagnosing another person or mind-reading motives |
| “我是不是 ADHD / 抑郁症？” | current clinical/medical guidance, not ordinary psychology reflection | psychology reflection only for a separate non-diagnostic coping/pattern subtask | casual diagnosis from chat |
| “先给我做八字，再单独用历史数据分析我这一代” | divination and generational Skills as two explicit subproblems | research for evidence-heavy cohort section | blending symbolic and empirical claims into one confidence score |
| “先从心理学分析我的拖延，再单独按八字看这个主题” | psychology and divination as separate explicit lenses | none by default | using either lens as proof for the other |

## Godot ownership boundaries

| User task | Expected primary | Secondary only when | Must avoid |
| --- | --- | --- | --- |
| “Godot 2D 攻击偶尔重复结算” | `development/godot-2d-game-development` | shared systems for verification if useful | replacing 2D gameplay ownership with generic debug advice |
| “Godot 2D CharacterBody2D movement/camera” | `development/godot-2d-game-development` | shared systems only for a distinct input/UI/verification concern | loading 3D or shared refs by default |
| “Godot 3D 第三人称移动和 Camera3D 穿墙” | `development/godot-3d-game-development` | shared systems for input/verification if distinct | forcing 2D camera/movement references |
| “Godot 3D Blender 模型导入后骨骼和动画异常” | `development/godot-3d-game-development` | research only if a current importer/version fact is material | generic asset advice replacing Godot import semantics |
| “Godot 3D pause/settings 菜单手柄 focus” | `development/godot-project-systems` | 3D only if spatial/world interaction also matters | loading 3D movement/rendering for Control UI |
| “Godot 2D 重映射按键并持久化” | `development/godot-project-systems` | 2D only if action-to-movement behavior is also changing | keeping input/save knowledge duplicated in 2D |
| “Godot v2 存档迁移 item IDs” | `development/godot-project-systems` | dimensional Skill only if runtime world semantics also change | treating save as 2D-specific |
| “Godot GitHub Actions clean export” | `development/godot-project-systems` | matching dimensional Skill only for a distinct runtime smoke path | routing through 2D because export used to live there |
| “Godot 3D 音频 bus 和设置” | `development/godot-project-systems` | 3D only for a distinct spatial-audio behavior | recreating all audio architecture in the 3D Skill |
| “生成 6 帧像素 attack strip” | `development/sprite-animation-pipeline` | Godot only if engine import/runtime is also requested | loading full Godot runtime for asset generation |
| “Godot 2D 已有 sprite，配置 runtime timing” | `development/godot-2d-game-development` | sprite pipeline only if source geometry must change | regenerating art unnecessarily |

## Other domain precedence

| User task | Expected primary | Secondary only when | Must avoid |
| --- | --- | --- | --- |
| “Shopify 产品页按钮坏了” | `ecommerce/shopify-dev` | bug-diagnosis for distinct methodology | generic frontend rewrite first |
| “Shopify theme release 前检查” | `ecommerce/shopify-dev` | release-checklist for broader org gates | generic release ceremony replacing platform rules |
| “设计一组 App Store 截图版式和顺序” | `design/app-store-assets` | app-store-copy for substantial wording | isolated-poster thinking |
| “已有 App Store screenshot，帮我改善” | `design/app-store-assets` | image-review-refiner for generic visual diagnosis | generic image route replacing store constraints |
| “只重写 subtitle 和 description” | `writing/app-store-copy` | positioning if value/audience is unresolved | loading visual design |
| “产品到底卖给谁、核心价值是什么” | `marketing/product-positioning` | downstream copy after positioning is fixed | polishing store copy first |
| “这个生成图哪里最该改” | `design/image-review-refiner` | domain Skill for production constraints | restarting from scratch by default |
| “从零生成营销主视觉 prompt” | `creative/image-prompt-director` | domain visual Skill when it owns production | image-review without an existing image |
| “给 xTool F1 做可实际雕刻的小徽章” | `creative/xtool-f1-engraving` | image-prompt-director for a distinct generation subtask | generic illustration overriding engraving constraints |

## Mixed-task pressure cases

### Godot shared + dimensional

Prompt: `Godot 3D pause menu 手柄 focus 修好后，再确认 Camera3D 游戏里没受影响。`

Pass: project-systems owns menu/input verification; 3D joins only for the distinct camera runtime check. Do not preload every 3D reference for the UI change.

### Godot gameplay + sprite asset

Prompt: `做 Godot 2D sword attack，同时生成对应 6 帧 attack strip。`

Pass: Godot 2D owns gameplay/runtime animation; sprite pipeline owns strip generation/geometry/packaging. Add project-systems only for a genuinely separate input/UI/save/export concern.

### Personal lenses stay separate

Prompt: `我 1990 年出生。先用心理学分析我现实里的职业焦虑，再用历史环境分析这一代，最后按八字给一个象征性视角。`

Pass: psychology uses the user's observed pattern; generational context uses historical/cohort evidence; divination stays symbolic. Do not collapse the three into one causal story or shared confidence score.

### Architecture then implementation

Prompt: `先决定 save schema 和 migration boundary，再给文件级改法。`

Pass: technical-design first; implementation-plan only after decisions are fixed.

### Direct-result request

Prompt: `直接帮我完成这个任务，不需要 prompt。`

Pass: actual domain/task owner; never prompt-optimizer as preprocessing.

### Discovery constraint fidelity

Prompt: `给我最好的短视频素材。不要考虑版权或商用，优先 TikTok 和 Instagram。`

Pass: web-discovery ranks TikTok/Instagram candidates by fit to the requested edit. It must not reintroduce copyright/commercial-use as filters, replace the platforms with stock sites, or add a licensing lecture.

## Pass criteria

1. One primary Skill owns the task.
2. Secondary Skills handle separable subtasks only.
3. Domain ownership beats generic methods.
4. Words such as “compare”, “plan”, “review”, “prompt”, “Godot”, “birth date” and “psychology” do not route by themselves.
5. Discovery preserves explicit user criteria and does not invent licensing, commercial-use, price, watermark, platform or source-type filters.
6. Divination, cohort analysis and psychology reflection keep separate evidence/claim boundaries.
7. Psychology reflection does not turn casual conversation into clinical diagnosis or mind-reading.
8. Godot project systems own dimension-neutral behavior; 2D/3D own dimensional behavior.
9. Asset production and engine runtime remain separate owners.
10. Maintenance content is not loaded during normal execution.

When a real task fails, fix the smallest ownership rule first. Do not add a new Skill unless existing owners cannot cleanly represent the missing decision.
