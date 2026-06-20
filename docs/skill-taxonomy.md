# Skill Taxonomy

`superskills` uses domain-based categories. The goal is to make skills easy to find and easy to evolve.

## Core categories

| Category | Scope |
| --- | --- |
| `meta` | Prompt optimization, skill creation, skill review, AI workflow control |
| `planning` | Project breakdown, decision making, prioritization, execution plans |
| `research` | Research briefs, source analysis, market/competitor scans |
| `development` | Code review, bug diagnosis, technical design, implementation plans |
| `creative` | Physical products, engraving, illustration, image generation, creative direction |
| `design` | App store assets, UI visuals, brand materials, landing pages |
| `ecommerce` | Shopify, product pages, conversion, operations, store workflows |
| `writing` | Business emails, copywriting, documentation, professional communication |
| `operations` | Checklists, SOPs, recurring workflows, internal processes |

## Naming convention

Use:

```txt
skills/<category>/<domain-task>/
```

Examples:

```txt
skills/meta/prompt-optimizer/
skills/development/code-review/
skills/creative/xtool-f1-engraving/
skills/design/app-store-assets/
skills/ecommerce/shopify-dev/
```

## Skill selection rule

When a task can match multiple skills, choose the skill based on the expected final output:

| User wants | Use |
| --- | --- |
| Better prompt | `meta/prompt-optimizer` |
| New reusable skill | `meta/skill-builder` |
| Task execution plan | `planning/project-planner` |
| Technical diagnosis | `development/bug-diagnosis` |
| PR feedback | `development/code-review` |
| Visual store assets | `design/app-store-assets` |
| Physical engraving design | `creative/xtool-f1-engraving` |
| Professional email | `writing/business-email` |

## Repository growth rule

Add a new skill only when:

- The task repeats often.
- The output needs a stable structure.
- Existing skills do not cover it well.
- There are useful constraints or examples worth preserving.

Do not add a new skill for one-off prompts unless the workflow is likely to repeat.
