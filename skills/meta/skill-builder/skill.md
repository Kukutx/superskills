---
name: skill-builder
description: Create, audit, simplify or restructure reusable skills in the superskills repository. Use when a workflow deserves persistent agent guidance rather than a one-off answer.
---

# Skill Builder

## First decision: does this deserve a Skill?

Create/expand a Skill only when the task repeats and there are **durable decision rules, constraints or domain knowledge** worth preserving.

Do not create one for a one-off prompt, generic global behavior, a renamed duplicate owner or notes that do not change Agent decisions.

## Workflow

1. Inspect existing Skills, references and routing first.
2. Define the exact owner and nearest overlap.
3. Prefer improving/renaming/splitting an existing owner over creating a parallel one.
4. Write one concise `skill.md` first.
5. Add `references/` only for task-dependent depth with a clear decision boundary.
6. When splitting, **move ownership rather than copy it**.
7. Ensure every runtime reference is discoverable from `skill.md` and keep references one directory level deep.
8. Use `behavioral-evals.md` under maintenance/ for real routing/ownership regressions and `sources.md` only for substantial source inventories.
9. Do not create changelog files; Git stores history. Use `decisions.md` only when current design rationale is genuinely needed.
10. Update the global Router only when task selection changes.
11. Run `python tools/validate_repo.py` and fix structural/orphan/stale-route failures.

## Default shape

```text
skills/<category>/<skill>/
└── skill.md
```

Add only when justified:

```text
references/    # runtime domain depth
maintenance/   # behavioral evals / sources / rare current design rationale
```

## `skill.md` quality bar

Keep only content that changes behavior:

- `name` + routing-quality `description`;
- scope / not-scope;
- workflow or decision rules;
- reference routing boundaries;
- important constraints;
- validation/completion boundary.

Avoid repeated Purpose/Role/System Prompt prose.

## Reference quality bar

A reference needs one semantic owner and one task-dependent question the entrypoint should not preload.

Before adding/splitting, ask:

```text
What decisions live here?
When should it load?
What neighboring owner must not duplicate it?
Does the split reduce real context or clarify truth ownership?
What behavioral eval proves the boundary matters?
```

If content must appear twice, keep the authoritative rule once and cross-reference it elsewhere.

## Output

When designing/auditing a Skill, implement or provide only what is needed:

1. recommended owner/path;
2. overlap decision: create / rename / split / merge / keep;
3. runtime content changes;
4. routing changes only when needed;
5. behavioral regression cases for changed boundaries;
6. validator result.

Repository-wide rules live in `docs/authoring-guide.md`.
