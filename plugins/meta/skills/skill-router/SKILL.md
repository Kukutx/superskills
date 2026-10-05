---
name: skill-router
description: Catalog of Superskills routes for hosts without a native Skill registry, such as ChatGPT Projects. Use only when ownership between Superskills is ambiguous and Skills do not auto-trigger.
---

# Skill Router

## Rule

```text
specific domain Skill
> generic method Skill
> meta helper
```

Choose one primary Skill. Add a secondary Skill only for a separable subtask with a different owner. If no Skill changes the answer, work directly instead of forcing a route.

A task being long, multi-step or tool-heavy does **not** make planning the requested deliverable. When the user asks to perform work, route to the domain owner or direct execution and plan internally. Use `project-planner` only when a roadmap or cross-workstream plan is itself the requested output.

A Skill guides decisions; it does not create a new permission gate. On hosts that load `gpts/kukutx/project-instructions.md`, global autonomy and escalation behavior comes from there.

## Catalog

| Intent | Skill |
| --- | --- |
| prompt or reusable AI instruction is the deliverable | `meta/prompt-optimizer` |
| create, audit, simplify or restructure a Skill | `meta/skill-builder` |
| broad roadmap across multiple workstreams | `planning/project-planner` |
| whether a project, product or research idea is worth doing, its riskiest assumptions and pivots | `planning/idea-evaluation` |
| find or rank web resources, media, examples, pages or accounts | `research/web-discovery` |
| establish current facts or compare external evidence | `research/research-brief` |
| PRD, MVP scope or product behavior | `product/prd-builder` |
| diagnose an observed software failure | `development/bug-diagnosis` |
| review code, a diff or pull request for concrete risks | `development/code-review` |
| decide unresolved software architecture, ownership or interfaces | `development/technical-design` |
| turn decided architecture into file-level tasks and tests | `development/implementation-plan` |
| Godot dimension-neutral project systems | `development/godot-project-systems` |
| Godot 2D or pixel runtime behavior | `development/godot-2d-game-development` |
| Godot 3D or spatial runtime behavior | `development/godot-3d-game-development` |
| generate, slice or package sprite animation assets | `development/sprite-animation-pipeline` |
| explicit divination, astrology or symbolic fortune reading | `personal/divination-reading` |
| evidence-led birth-cohort or historical life context | `personal/generational-context-analysis` |
| non-diagnostic reflection on personal thoughts and behavior | `personal/psychology-reflection` |
| direct image-generation direction or prompt | `creative/image-prompt-director` |
| xTool F1 engraving-ready design and production guidance | `creative/xtool-f1-engraving` |
| App Store or Play Store visual assets | `design/app-store-assets` |
| review and refine an existing image | `design/image-review-refiner` |
| Shopify implementation, Liquid, theme or store integration | `ecommerce/shopify-dev` |
| audience, value proposition and product messaging | `marketing/product-positioning` |
| professional business email | `writing/business-email` |
| App Store or Play Store listing copy | `writing/app-store-copy` |
| create, tailor, rewrite or audit a resume/CV | `writing/resume-writing` |
| generic release readiness and go/no-go gate | `operations/release-checklist` |
| repeated process or SOP | `operations/sop-builder` |
| extract action items from messages or notes, inbox triage, personal task list | `planning/inbox-and-task-digest` |
| plan user research or synthesize interviews, surveys and reviews | `research/user-research` |
| rank product initiatives, Now/Next/Later roadmap | `product/roadmap-prioritization` |
| prices, tiers, paywall moments, discounts and price increases | `product/pricing-and-paywall` |
| first-run activation, cancel flows and failed-payment recovery | `product/onboarding-and-retention` |
| inventory and rank technical debt, choose what to refactor | `development/tech-debt-triage` |
| plan a promo, trailer or demo video | `creative/promo-video` |
| critique a UI screen for usability and accessibility | `design/design-review` |
| stock reorder quantities, dead stock and purchase orders | `ecommerce/inventory-reorder` |
| marketing campaign or growth plan with channels, budget and KPIs | `marketing/marketing-plan` |
| launch plan, directory submissions and press pitches | `marketing/product-launch` |
| sponsor, exhibit, speak or host a webinar, and measure the event | `marketing/event-marketing` |
| what to publish, topic priorities and community building | `marketing/content-strategy` |
| automated email sequence with timing, branching and copy | `marketing/email-sequences` |
| SMS or WhatsApp marketing with consent and compliance checks | `marketing/sms-marketing` |
| website SEO, structured data and AI-search readability audit | `marketing/seo-audit` |
| App Store or Google Play listing audit for visibility and conversion | `marketing/app-store-optimization` |
| design an A/B test and decide from its result | `marketing/ab-testing` |
| page, signup flow, popup or lead offer that does not convert | `marketing/conversion-review` |
| plan or review paid ad campaigns and attribution | `marketing/paid-ads` |
| competitor profiles, comparison tables and battlecards | `marketing/competitor-analysis` |
| creator, influencer, affiliate or co-marketing deals | `marketing/creator-partnerships` |
| landing page, ad, blog, newsletter or press release copy | `writing/marketing-copy` |
| derive, write or enforce a brand voice or tone-of-voice guide | `writing/brand-voice-guide` |
| social posts, short-video scripts and posting calendar | `writing/social-content` |
| in-app microcopy such as buttons, errors and empty states | `writing/ux-copy` |
| production incident triage, status updates and postmortem | `operations/incident-response` |
| public crisis statement, apology and who hears first | `operations/crisis-communications` |
| change request, risk register, rollback and process optimization | `operations/change-management` |
| evaluate or compare vendors and tools on cost and risk | `operations/vendor-evaluation` |
| status report, stakeholder update or release announcement | `operations/status-report` |
| analyze a dataset or check an analysis before sharing | `data/data-analysis` |
| KPI report, metrics review or business health check | `data/metrics-review` |
| write, fix or speed up a SQL query | `data/sql-query-writing` |
| choose and build a chart or dashboard | `data/data-visualization` |
| triage and answer a customer ticket, inquiry or complaint | `support/customer-support-replies` |
| help-center, FAQ, troubleshooting or known-issue article | `support/help-center-article` |
| reply to public reviews, win back customers who went quiet | `support/review-replies-and-winback` |
| review a contract and propose redlines | `legal/contract-review` |
| screen an NDA before signing | `legal/nda-triage` |
| privacy compliance check, DPA review or data subject request | `legal/privacy-compliance-check` |
| prepare for a customer call, recap it and write the follow-up | `sales/sales-call-prep-and-recap` |
| prospect list, cold or follow-up sales email, objection handling | `sales/sales-outreach` |
| health, gaps and next step of one sales deal or account | `sales/deal-review` |
| pipeline review, forecast, win-loss or a spreadsheet CRM | `sales/sales-pipeline-review` |
| priced quote, estimate, proposal or statement of work | `sales/quote-and-proposal` |
| grant, RFP or tender go/no-go, compliance matrix and response | `sales/grant-and-rfp-bidding` |
| job post, resume screening, interview guide and offer | `people/hiring` |
| self-assessment, performance review or calibration notes | `people/performance-review` |
| journal entries, reconciliation and month-end close | `finance/books-close-and-reconciliation` |
| explain budget versus actual or period-over-period variances | `finance/variance-analysis` |
| 30/60/90-day cash forecast and runway | `finance/cash-flow-forecast` |
| process supplier bills and propose a payment run | `finance/bills-and-payables` |
| chase overdue invoices with tone matched to payment history | `finance/invoice-collections` |
| check timesheets and prepare a payroll run | `finance/payroll-run-check` |
| US quarterly estimated tax maths and 1099 preparation | `finance/us-self-employed-tax-prep` |
| control testing, sampling and deficiency classification | `finance/internal-controls-testing` |
| build or audit a spreadsheet financial model | `finance/financial-modeling` |
| value a company or stock with DCF and comparables | `finance/company-valuation` |
| LTV, CAC, retention, cohorts and ARR bridge | `finance/unit-economics` |
| screen, diligence and decide on buying or backing a business | `finance/deal-diligence` |
| teaser, information memorandum, buyer list and sale process for selling a business | `finance/selling-a-business` |
| periodic portfolio or investment report against a benchmark | `finance/portfolio-reporting` |
| research one listed company, its results and thesis | `finance/stock-research` |
| industry overview and stock idea screening | `finance/sector-and-stock-screening` |

## Important boundaries

### Project planning vs software design vs implementation

```text
roadmap is the deliverable -> project-planner
architecture/data/interface still undecided -> technical-design
direction fixed + file/task/test plan requested -> implementation-plan
execution requested -> matching domain owner or direct execution; plan internally
```

Do not load all three for a normal software task. Do not replace requested execution with a planning artifact merely because the work has many steps.

### Web discovery vs evidence research

```text
find/shortlist/rank actual resources -> web-discovery
decide what is true or current -> research-brief
```

A discovery task may verify one material fact without becoming a full research brief. Use both only when evidence synthesis is a distinct deliverable.

### Bug diagnosis vs code review

```text
observed failure and root cause -> bug-diagnosis
inspect visible code/change for defects -> code-review
```

A failing runtime path needs reproduction evidence, not a generic review checklist.

### Godot shared vs dimensional owners

```text
input, Control UI, audio, save, inventory, dialogue, verification, export -> project-systems
CharacterBody2D, Camera2D, TileMapLayer, 2D combat/VFX/navigation -> Godot 2D
Transform3D, CharacterBody3D, Camera3D, 3D rendering/import/navigation -> Godot 3D
```

Route by what changes implementation, not by the project's dimensional label alone.

### Asset production vs runtime integration

```text
sprite frames/strip geometry/slicing/packing -> sprite-animation-pipeline
Godot gameplay and runtime animation behavior -> matching Godot owner
```

Use both only when the task genuinely spans both outputs.

### Personal-analysis boundaries

Keep symbolic divination, historical cohort evidence and observed psychology patterns separate. Do not use one lens as proof for another, and do not force diagnosis or treatment questions into ordinary reflection.

### Resume vs adjacent job tasks

Resume facts, structure, bullets and role tailoring belong to resume-writing. Job discovery is a research/discovery task; application or outreach email belongs to business-email. Do not invent experience or metrics to make a resume sound stronger.

### Messages to customers and prospects

```text
a customer wrote in with a problem, inquiry or refund request -> customer-support-replies
a public review, or a customer who went quiet -> review-replies-and-winback
selling to a prospect, or answering an objection -> sales-outreach
before or after a sales call -> sales-call-prep-and-recap
an automated series -> email-sequences (email) / sms-marketing (text)
any other one-to-one email -> business-email
a pile of messages to sort -> inbox-and-task-digest
```

### Numbers

```text
explore or verify a dataset or an analysis -> data-analysis
recurring KPI review or business health check -> metrics-review
why actuals differ from budget or last period -> variance-analysis
entries, reconciliation and close -> books-close-and-reconciliation
build or audit the spreadsheet model -> financial-modeling
what a company is worth -> company-valuation
subscription metrics -> unit-economics
the query itself -> sql-query-writing; the chart -> data-visualization
```

### Marketing chain

```text
who it is for and why it is different -> product-positioning
plan, channels and budget -> marketing-plan; a launch -> product-launch
what to publish -> content-strategy
the words -> marketing-copy (pages, ads) / social-content / app-store-copy / ux-copy
found in search -> seo-audit (website) / app-store-optimization (store listing)
a page that does not convert -> conversion-review; which version wins -> ab-testing
paid campaigns -> paid-ads; rivals -> competitor-analysis
```

### Agreements, bids and deals

```text
an NDA on its own -> nda-triage; any other agreement -> contract-review
your own quote or proposal -> quote-and-proposal; a grant or tender -> grant-and-rfp-bidding
one sales deal -> deal-review; the whole pipeline -> sales-pipeline-review
buying or backing a business -> deal-diligence; selling one -> selling-a-business
one listed company -> stock-research; a sector or a screen -> sector-and-stock-screening
reporting a portfolio's results -> portfolio-reporting
```

Legal, tax, accounting and investment Skills prepare material for a non-specialist and say where a professional decides; they do not replace one.

## Restraint

- Route by the requested deliverable and decision owner, not isolated keywords.
- Preserve the user's explicit scope and ranking criteria.
- Do not run prompt optimization when the user requested the final task result.
- Do not route to planning merely because execution is complex.
- Do not preload every neighboring Skill or reference.
- Do not use Skill routing as a reason to ask for permission that the task already grants.
- Keep maintenance files out of normal runtime context.
