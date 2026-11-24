# Core profile

A curated bundle of the most-used skills, for ChatGPT Projects and GPTs
where the full bundle is too large. It reuses the default profile's
`project-instructions.md` (one copy, in `gpts/default/`); this directory
only holds the skill list.

## Build

```bash
python tools/build_bundle.py \
  --profile gpts/default \
  --profile-file gpts/core/skills.txt \
  --output dist/core
```

CI builds this profile on every run and fails it if it exceeds
**100 files or 120,000 tokens**. Those are our own budgets, not a confirmed
ChatGPT Project limit; no ChatGPT file or token ceiling has been verified.

## Skills (34)

From `skills.txt`, in order:

- development: bug-diagnosis, code-review, technical-design, implementation-plan, security-audit, godot-project-systems, spec-driven-development
- meta: prompt-optimizer, skill-builder
- writing: resume-writing, marketing-copy, business-email, social-content, ux-copy, multilingual-docs
- marketing: marketing-plan, content-strategy, seo-audit, paid-ads, conversion-review, email-sequences, marketing-attribution, product-positioning, product-launch
- design: design-review, landing-page-design, diagram-design
- product: prd-builder, roadmap-prioritization, pricing-and-paywall
- planning: project-planner, idea-evaluation
- research: research-brief, web-discovery

The Router is always included by the bundle builder, so the bundle also
answers for skills it does not carry by saying they are not loaded.

## Measured sizes (2026-11-24, commit 87e1090 base + deep-dive changes)

| Bundle | Files | Bytes | Approx. tokens |
| --- | --- | --- | --- |
| Core profile (`gpts/core/skills.txt`) | 36 | 243,012 | ~60,753 |
| Full bundle (`--all-skills`, 115 skills) | 214 | 1,106,899 | ~276,725 |

Token counts are the builder's coarse estimate (bytes / 4), not a host
measurement. To change the core set, edit `skills.txt` and re-run the build;
a route that does not exist fails the build instead of silently shrinking it.
