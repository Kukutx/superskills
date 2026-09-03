# Skill Router behavioral evals

Maintenance-only. Test task ownership, scope fidelity and clarification behavior rather than keyword matching.

## Core routing cases

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| router-001 | “帮我优化这段 prompt。” | `meta/prompt-optimizer` | domain constraints only when needed | executing the downstream task instead |
| router-002 | “精简这个现有 Skill 并修路由。” | `meta/skill-builder` | none by default | prompt-optimizer merely because instructions are edited |
| router-003 | “从需求验证到上线，排整个项目。” | `planning/project-planner` | domain owner for a concrete workstream | a file-level implementation plan for the whole project |
| router-004 | “找 5 个最适合 10 秒剪辑的跳伞视频。” | `research/web-discovery` | research only for a distinct factual question | inventing unrequested filters |
| router-005 | “比较三个平台当前的下载政策和证据。” | `research/research-brief` | web discovery only if actual clips/pages are separately requested | ranking media relevance instead of answering the policy question |
| router-006 | “API ownership 和数据模型还没定。” | `development/technical-design` | research only if current evidence changes the design | implementation-plan before architecture is fixed |
| router-007 | “架构定了，按仓库告诉我改哪些文件。” | `development/implementation-plan` | domain owner for implementation rules | reopening settled architecture without a blocker |
| router-008 | “线上报错，为什么？” | `development/bug-diagnosis` | specific domain owner when one exists | code-review as a substitute for reproduction |
| router-009 | “Review 这个 PR 有没有阻塞合并的问题。” | `development/code-review` | domain owner for domain invariants | inventing an observed runtime failure |
| router-010 | “写一个 MVP PRD，不要先设计后端。” | `product/prd-builder` | positioning only if audience/value is unresolved | speculative architecture |
| router-011 | “每天重复发布这批内容，整理 SOP。” | `operations/sop-builder` | domain owner for domain steps | project-planner for a stable repeated process |
| router-012 | “这一次发布前做 go/no-go 检查。” | `operations/release-checklist` | domain release owner when available | turning one release into an SOP |
| router-013 | “根据我的真实经历写一份后端工程师简历。” | `writing/resume-writing` | research only for a distinct current market fact | inventing employers, metrics or technologies |
| router-014 | “根据简历写一封给招聘经理的邮件。” | `writing/business-email` | resume-writing only if the resume itself also changes | returning another resume |

## Clarification and confidence cases

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| clarify-001 | “帮我做一个完整简历。”用户没有提供目标岗位、经历、公司或日期。 | `writing/resume-writing` | none | producing a polished factual resume from guesses instead of asking grouped questions |
| clarify-002 | 用户已经上传完整简历和 JD，并要求直接定制。 | `writing/resume-writing` | none | repeating questions whose answers are already in the supplied material |
| clarify-003 | “把这个仓库的按钮圆角从 8 改成 10。”路径和组件已明确。 | matching domain owner or direct execution | none | blocking a reversible local edit with unnecessary preference questions |
| clarify-004 | “重做整个权限系统。”当前角色、数据边界和迁移要求未知。 | `development/technical-design` | implementation-plan after decisions are fixed | guessing core ownership or silently choosing destructive migration behavior |
| clarify-005 | 用户明确说“先给我一个可逆的初稿，未知项标出来”。 | matching domain owner | none | refusing all progress or presenting placeholders as verified facts |

## Domain boundary cases

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| domain-001 | “Godot 3D pause menu 手柄 focus 断了。” | `development/godot-project-systems` | 3D only for a distinct spatial runtime issue | loading Camera3D/physics merely because the project is 3D |
| domain-002 | “Godot 2D CharacterBody2D dash 穿墙。” | `development/godot-2d-game-development` | shared verification guidance when useful | replacing 2D physics with generic project-system advice |
| domain-003 | “Godot 3D 第三人称移动和 Camera3D 穿墙。” | `development/godot-3d-game-development` | shared input/verification only as separate concerns | forcing 2D rules |
| domain-004 | “生成 6 帧像素 attack strip。” | `development/sprite-animation-pipeline` | Godot only if engine integration is also requested | loading full runtime guidance for asset production alone |
| domain-005 | “Shopify 产品页按钮坏了。” | `ecommerce/shopify-dev` | bug-diagnosis only for a distinct method need | generic frontend rewrite first |
| domain-006 | “已有 App Store screenshot，帮我改善。” | `design/app-store-assets` | image-review-refiner for a distinct generic visual diagnosis | replacing store constraints with a generic image route |
| domain-007 | “产品到底卖给谁、核心价值是什么？” | `marketing/product-positioning` | downstream copy after positioning is fixed | polishing listing copy first |
| domain-008 | “我重要工作总拖到最后，想理解并改变这个循环。” | `personal/psychology-reflection` | research only for a separate evidence question | casual diagnosis or invented childhood causes |
| domain-009 | “1992 年生，按八字看事业。” | `personal/divination-reading` | none by default | presenting symbolic interpretation as empirical evidence |
| domain-010 | “1992 年生，结合经济和互联网环境分析成长背景。” | `personal/generational-context-analysis` | research for distinct evidence synthesis | divination merely because a birth date appears |

## Pass criteria

1. One primary Skill owns the requested deliverable.
2. Secondary Skills handle genuinely separable subtasks only.
3. Domain ownership beats generic methods.
4. Questions are asked for direction-changing or factual unknowns, not for information already available or harmless reversible details.
5. Explicit user criteria remain the selection criteria.
6. Maintenance content is never loaded during normal execution.
