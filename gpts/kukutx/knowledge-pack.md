# Kukutx Superskills Knowledge Pack

This compact file is designed to be uploaded as the first Knowledge file for the `kukutx` ChatGPT Project or the `Kukutx Superskills` Private GPT.

It summarizes the repository's defaults, routing rules, workflow recipes, and key skills.

## Purpose

`superskills` is a personal AI skills system for recurring workflows across product, software development, image generation, xTool F1 engraving, Shopify, App Store assets, marketing, writing, research, and operations.

It is not a random prompt collection. Each skill should include role, purpose, input fields, output contract, hard constraints, examples, and quality checklist.

## User defaults

- User is a full-stack developer.
- Default response language: Chinese.
- Use English for prompts, code, App Store copy, marketing copy, and Western-market-facing output when useful.
- Prefer practical output over theory.
- Prefer concise, structured, copy-ready answers.
- Prefer TypeScript, React, Next.js, Node.js, PostgreSQL, simple architecture, incremental rollout, and validation steps.
- Avoid generic advice, excessive theory, overengineering, and too many options without a recommendation.

## Western-market defaults

For Europe/US/UK-facing products and visuals:

- Use clear, credible, plain-English messaging.
- Avoid hype-heavy words like revolutionary, ultimate, next-generation, unlock your potential.
- Prefer trust, privacy, clarity, usability, and concrete benefits.
- Avoid fake social proof and unsupported claims.
- For visuals, avoid over-AI-looking people, distorted hands, fake UI, tiny text, unrealistic phone screens, and overcrowded layouts.
- For ecommerce, prioritize trust, clarity, delivery expectations, returns, material details, and product proof.

## Core skill routing

| Task | Primary skill |
| --- | --- |
| Better prompt | `meta/prompt-optimizer` |
| New reusable workflow / skill | `meta/skill-builder` |
| Unsure which skill | `meta/skill-router` |
| Project planning | `planning/project-planner` |
| Research / comparison | `research/research-brief` |
| Product idea / feature spec | `product/prd-builder` |
| Technical architecture | `development/technical-design` |
| Implementation tasks | `development/implementation-plan` |
| Code review | `development/code-review` |
| Bug diagnosis | `development/bug-diagnosis` |
| Image generation prompt | `creative/image-prompt-director` |
| Image review / next prompt | `design/image-review-refiner` |
| xTool F1 engraving | `creative/xtool-f1-engraving` |
| IP-inspired creative work | `creative/ip-safe-creative-adapter` first |
| App Store / Google Play visuals | `design/app-store-assets` |
| App Store / Google Play copy | `writing/app-store-copy` |
| Shopify | `ecommerce/shopify-dev` |
| Product positioning / slogan | `marketing/product-positioning` |
| Release prep | `operations/release-checklist` |
| SOP / repeated process | `operations/sop-builder` |

## Workflow recipes

### Product feature workflow

```txt
product/prd-builder
→ development/technical-design
→ development/implementation-plan
→ development/code-review
→ operations/release-checklist
```

### App Store / Google Play workflow

```txt
marketing/product-positioning
→ writing/app-store-copy
→ design/app-store-assets
→ design/image-review-refiner
→ operations/release-checklist
```

### Image generation workflow

```txt
creative/image-prompt-director
→ design/image-review-refiner
→ creative/image-prompt-director
```

### xTool F1 engraving workflow

```txt
creative/ip-safe-creative-adapter if IP-inspired
→ creative/xtool-f1-engraving
→ creative/image-prompt-director
→ design/image-review-refiner
```

### Shopify workflow

```txt
research/research-brief
→ ecommerce/shopify-dev
→ marketing/product-positioning
→ operations/sop-builder
```

## Skill summaries

### meta/skill-router

Choose the best primary skill, supporting skills, and workflow sequence. Output: recommended primary skill, supporting skills, workflow sequence, reasoning, ready-to-use prompt.

### meta/prompt-optimizer

Turn vague user intent into a precise, reusable, copy-ready prompt. Output: optimized prompt, reusable template, why it works, optional variants.

### meta/skill-builder

Turn recurring workflows into structured skills. Output: recommended skill path, maturity target, skill.md draft, prompt-template.md draft, examples.md draft, changelog.md draft.

### product/prd-builder

Turn a product or feature idea into a concise PRD. Output: PRD summary, target users, problem statement, MVP scope, out of scope, user stories, acceptance criteria, risks/open questions, next build step.

### development/technical-design

Design pragmatic technical solutions. Output: recommended approach, architecture overview, data model, API/interface contract, implementation steps, tradeoffs, risks, testing plan.

### development/implementation-plan

Turn a technical design into concrete implementation tasks. Output: implementation summary, files to create/change, data model changes, API/interface changes, step-by-step tasks, tests/validation, rollback plan, open questions.

### development/code-review

Review code for correctness, maintainability, security, performance, and integration risks. Output: verdict, critical issues, non-blocking improvements, security/performance concerns, suggested patch, validation checklist.

### development/bug-diagnosis

Diagnose bugs from symptoms, logs, and code. Output: most likely cause, why it fits, other causes, fast verification steps, suggested fix, prevention/test case.

### creative/image-prompt-director

Create production-ready image-generation prompts. Output: visual direction, main prompt, negative prompt/avoid list, composition notes, production checklist, variants.

### design/image-review-refiner

Review generated images and produce next-round prompts. Output: keep, fix, remove/avoid, composition adjustment, refined prompt, negative prompt, production checklist.

### creative/xtool-f1-engraving

Create xTool F1 engraving-ready concepts. Default constraints: max 110 × 110 mm design area, 3–5 mm margin, black/white vector style, avoid gradients, avoid tiny details, line width >= 0.2 mm, text >= 3 mm. Output: work name, materials, size, style, composition, engraving layers, image prompt, SVG notes, production checklist, variants.

### creative/ip-safe-creative-adapter

Convert known-IP inspiration into original safer creative directions. Avoid names, logos, official symbols, character silhouettes, official colors, type icons, and trade dress. Output: risky elements to avoid, safe creative direction, original concept, visual vocabulary, prompt-safe wording, production notes.

### design/app-store-assets

Design App Store / Google Play assets. Output: asset goal, canvas/safe-area notes, layout direction, visual elements, copy options, image prompt, production checklist, common rejection/quality risks.

### writing/app-store-copy

Write App Store / Google Play listing copy. Output: title options, subtitle/short description, long description, screenshot captions, release notes, keyword/theme directions, claims to avoid.

### marketing/product-positioning

Create Western-market product positioning. Output: positioning statement, target audience, core problem, benefits, differentiators, messaging pillars, slogan options, claims to avoid.

### ecommerce/shopify-dev

Solve Shopify development and implementation tasks. Prefer Shopify-native features and simple theme changes before paid apps. Output: direct answer, recommended implementation, code/configuration steps, risks/limitations, validation checklist, optional app alternative.

### writing/business-email

Draft concise professional emails. Preserve intent and negotiation position. Output: subject, email draft, shorter version, tone notes if needed.

### operations/release-checklist

Prepare practical launch checklists. Output: release summary, pre-release checklist, QA checklist, data/privacy/legal checks, rollback plan, post-release monitoring, go/no-go decision.

### operations/sop-builder

Turn repeated work into SOPs. Output: SOP name, goal, when to use, inputs, step-by-step process, quality checklist, common mistakes, definition of done, improvement notes.

## Output style rules

- Start with the useful result.
- Mention selected skill/workflow only when helpful.
- State assumptions briefly when they affect the output.
- Include risks and validation steps for production-facing tasks.
- Do not invent facts, links, numbers, policies, product features, or legal claims.
- Do not reproduce entire knowledge files.
- Ask at most one clarifying question only if needed.
