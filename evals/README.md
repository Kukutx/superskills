# Behavior evals

Run from the repository root:

```bash
claude plugin eval . --judge-model sonnet --runs 3
```

Each case runs with and without the plugin. Compare new results with the last recorded baseline below; a case whose Δ stays at 0 over several runs means current models already behave this way, so the matching Skill rule is a candidate for trimming.

## Last recorded baseline

2026-10-11, Claude Code 2.1.296, judge `sonnet`, one case per Skill plus two near-miss trigger cases. 2 runs per arm; cases changed or added later were run with 3. Passing runs:

| Case | Skill | With plugin | Without | Note |
| --- | --- | --- | --- | --- |
| bug-diagnosis-evidence-first | `bug-diagnosis` | 2/2 | 2/2 | Skill did not fire; base model already passes |
| code-review-no-manufactured-findings | `code-review` | 2/2 | 2/2 | Skill did not fire; base model already passes |
| design-no-new-infra | `technical-design` | 2/2 | 2/2 | Skill did not fire; base model already passes |
| discovery-no-invented-links | `web-discovery` | 2/2 | 2/2 | Δ 0 |
| email-no-concession | `business-email` | 2/2 | 0/2 | Was 3/3 vs 3/3 on 2026-10-10; baseline is noisy |
| generation-no-personality-verdict | `generational-context-analysis` | 3/3 | 0/3 | Relationship rule tightened after a run prescribed partner traits from cohort |
| godot-save-stable-ids | `godot-project-systems` | 2/2 | 2/2 | Skill did not fire; base model already passes |
| godot2d-hit-once-per-attack | `godot-2d-game-development` | 2/2 | 2/2 | Skill did not fire; base model already passes |
| godot3d-no-trimesh-on-mover | `godot-3d-game-development` | 2/2 | 2/2 | Δ 0 |
| image-prompt-no-baked-copy | `image-prompt-director` | 2/2 | 2/2 | Δ 0 |
| image-review-description-only | `image-review-refiner` | 2/2 | 2/2 | Δ 0 |
| knowledge-video-sourced-script | `knowledge-video` | 3/3 | 0/3 | Added 2026-10-30; closing-question and hook rules moved into SKILL.md after 1/3 |
| impl-plan-no-invented-paths | `implementation-plan` | 2/2 | 2/2 | Δ 0 |
| landing-no-fake-proof | `landing-page-design` | 3/3 | 2/3 | Added 2026-10-30; upstream rule to invent realistic testimonials replaced by labelled placeholders |
| no-trigger-divination | `divination-reading` | 2/2 | 2/2 | Near-miss: Skill must not fire |
| no-trigger-prompt-optimizer | `prompt-optimizer` | 2/2 | 2/2 | Near-miss: Skill must not fire |
| positioning-no-fabricated-proof | `product-positioning` | 2/2 | 2/2 | Δ 0 |
| prd-no-invented-research | `prd-builder` | 2/2 | 2/2 | Δ 0 |
| prompt-copy-ready | `prompt-optimizer` | 2/2 | 2/2 | Δ 0 (also Δ 0 on 2026-10-10) |
| psych-no-attachment-label | `psychology-reflection` | 3/3 | 1/3 | Rule tightened: no type for an absent third party, even hedged |
| release-ci-not-proof | `release-checklist` | 2/2 | 2/2 | Skill did not fire; base model already passes |
| research-no-invented-sources | `research-brief` | 3/3 | 3/3 | Rubric clarified: naming pages to check is not citing them |
| resume-no-invented-metrics | `resume-writing` | 2/2 | 0/2 | Without the Skill, invented figures appear as fact or inside placeholders |
| roadmap-no-invented-dates | `project-planner` | 2/2 | 1/2 | |
| shopify-native-first | `shopify-dev` | 2/2 | 2/2 | Δ 0 |
| sop-one-time-not-sop | `sop-builder` | 2/2 | 2/2 | Skill did not fire; base model already passes |
| sprite-no-giant-sheet | `sprite-animation-pipeline` | 2/2 | 0/2 | Without the Skill, one giant all-actions sheet prompt |
| store-copy-no-invented-claims | `app-store-copy` | 1/3 | 0/3 | Known gap: copy still adds unstated mechanics; self-check step added |
| store-screenshots-no-fake-proof | `app-store-assets` | 2/2 | 0/2 | Without the Skill, invented ratings or user counts |
| tarot-honest-draw | `divination-reading` | 2/2 | 2/2 | Δ 0 |
| xtool-no-invented-settings | `xtool-f1-engraving` | 2/2 | 0/2 | Without the Skill, one fixed power/speed set for the real job |

Reading this table:

- **Clear gains** (with > without): resume, email, generation, psych, roadmap, sprite, store screenshots, xtool, store copy.
- **Δ 0 with the Skill firing**: current models already behave this way on these prompts. With only 2 runs these rules stay; trim one only if it keeps Δ 0 over several runs and on claude.ai, where base behavior can differ.
- **Skill did not fire** in Claude Code for 7 coding/process cases: the model answered directly, and the base answer already passed. No trigger tuning is needed while the base answer is correct.
- `store-copy-no-invented-claims` is deliberately strict and remains a known gap.
