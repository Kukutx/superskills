# Skill Builder decisions

Maintenance-only. Current rationale that cannot be inferred from the repository.

## Candidates evaluated and not added

- **Agent handoff** (2026-10): a dedicated Skill was drafted and replayed against a no-Skill baseline on three cases (unverified work, pointing to existing artifacts, perishable facts). The baseline passed the same criteria, so no behavior change was demonstrated and the Skill was not added. Revisit only with a case the baseline fails.
- **Vendor setup Skills** (2026-10): setup-style Skills written to scaffold a new project (add the `http` package, hand-write JSON serialization) assume there are no conventions yet and contradict the ones an existing codebase already has. None was added here; a vendor Skill repository is a reference source to read, not something to install where it auto-triggers.
- **Content-format Skills** (2026-10): social posts, video scripts, press releases, case studies, newsletters and SEO articles were each considered after reading inference.sh's Skills, and none was added as a Skill of its own. Later in the same month the professional-domain round (below) added `writing/marketing-copy`, `writing/social-content` and `creative/promo-video`, which own these formats as groups; one Skill per format is still not wanted. Audio, speech and SDK-calling Skills are bound to a paid platform and were not adopted.
- **Vendor deploy and setup scripts** (2026-10): Vercel's `deploy.sh` uploads an archive with four exclusions to a hard-coded third-party endpoint, has no request timeout, treats any 4xx as ready and exits 0 on poll timeout. Not to be used. Anthropic's document Skills (docx, pptx, pdf, xlsx) are under a proprietary licence: practices may be learned, text and code may not be copied.
- **User-invoked Skills via `disable-model-invocation`** (2026-10): Claude Code can hide a Skill from the model so only the user can invoke it, at zero always-on cost. Not adopted: the field is specific to one host, the Agent Skills reference validator rejects unknown frontmatter, and every Skill here is meant to trigger on its own. The Router is kept out of registry hosts by not installing the `meta` plugin there instead.

## Professional-domain round (2026-10)

The owner asked for breadth: Skills that make everyday tasks in other professions workable on web hosts, usable rather than company-specific. Sixty Skills were added in `data`, `design`, `finance`, `legal`, `marketing`, `operations`, `people`, `planning`, `product`, `research`, `sales`, `support`, `writing`, `creative`, `development` and `ecommerce`, and eleven existing Skills gained rules.

- **How they were written.** Upstream plugins were read file by file into notes, the notes were merged across sources into one owner per task, and each Skill was written from the notes in new words. Connector-dependent steps were replaced by what can be done from pasted material. No Skill was replayed against a no-Skill baseline, so their effect on behaviour is unverified; the routing cases added to the Router's evals are structural until replayed.
- **Unsourced numbers.** Benchmarks the upstream material gave without a source are either left out or written as labelled defaults that the user's data replaces. Contradictions between upstream files were resolved towards the stricter value or left to the user.
- **Facts checked against official pages**, recorded in each Skill's `sources.md`. Corrections to the upstream material: WCAG 2.5.5 (44 px targets) is level AAA, the AA criterion is 2.5.8 at 24 px; the 1099-NEC reporting threshold is 2,000 dollars for tax years beginning after 2025, not 600; Apple's keyword field is 100 characters, not bytes; a Google Play preview video may autoplay muted; Google removed FAQ rich results in 2026; Google states no length limit for titles or meta descriptions.
- **Merged instead of added.** Internal-material synthesis went into `research-brief`; capacity planning into `project-planner`; process documents and runbooks into `sop-builder`; specification rules into `prd-builder`; architecture decision consequences into `technical-design`; voice matching into `business-email`; customer-research evidence rules into `user-research`; policy, refund and inquiry handling into `customer-support-replies`; deck number consistency into `financial-modeling`; personal task lists, glossary and message digests into `inbox-and-task-digest`.
- **Evaluated and not added.**
  - KYC onboarding checks: the upstream gives only a factor framework and defers every threshold to an institution's own rule table, so there is nothing to carry.
  - LBO modelling: bound to a spreadsheet template that was not part of the material; its few general rules are in `financial-modeling` and `deal-diligence`.
  - Morning notes and catalyst calendars as their own Skills: they need live market data; the judgement rules are in `stock-research`.
  - Compliance-framework tracking (SOC 2, ISO 27001, HIPAA, PCI): one line per framework upstream, not enough to support any conclusion.
  - Org planning and people analytics: the benchmarks have no source and contradict each other.
  - Design handoff and design-system documentation, stand-ups, generic documentation, brainstorming frameworks: templates a capable model already produces.
  - Team-lead sales views, lead routing, CRM write-back, daily and weekly briefings, connector setup and builder Skills: they depend on connectors or company-internal data that a web chat does not have.
  - Canva and scheduling-API orchestration: tool calls, not decision rules; the length and caption rules went into `social-content`.
  - A suspicious-request Skill: the rule (requests for money, credentials or changed bank details are flagged, never drafted) is carried inside the Skills that read inbound messages.
