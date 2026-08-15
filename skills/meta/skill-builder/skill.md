---
name: skill-builder
description: Create, audit, simplify or restructure reusable skills in the superskills repository. Use when a workflow deserves persistent agent guidance rather than a one-off answer.
---

# Skill Builder

## First decision: does this deserve a Skill?

Create or expand a Skill only when the task repeats and there are **durable decision rules, constraints or domain knowledge** worth preserving.

Do not create a Skill for:

- one-off prompts;
- generic model behavior already handled by global instructions;
- a renamed copy of an existing Skill;
- a few notes that do not change Agent decisions.

## Workflow

1. Inspect existing skills and routing before adding anything.
2. Define the exact task boundary and nearest overlapping Skill.
3. Prefer improving an existing Skill over creating a parallel one.
4. Write one concise `skill.md` first.
5. Add `references/` only when task-dependent domain depth justifies progressive loading.
6. Add `maintenance/` only for substantial sources, regression tests or complex history.
7. Update global routing only if the new Skill changes how tasks should be selected.
8. Test realistic prompts for correct routing and overreach.

## Default file shape

```text
skills/<category>/<skill>/
└── skill.md
```

Do **not** create `prompt-template.md`, `examples.md` or `changelog.md` by default. Git already stores history, and small examples/templates belong in `skill.md` when they add value.

## skill.md quality bar

Keep only content that changes behavior:

- `name` + `description` frontmatter;
- when to use / not use;
- workflow or decision rules;
- output contract when useful;
- hard constraints / anti-patterns;
- validation.

Avoid repeating the same instruction as Purpose + Role + System Prompt.

## Output

When asked to design a Skill, provide or implement:

1. recommended path;
2. overlap decision: create / merge / keep existing;
3. `skill.md`;
4. optional reference/maintenance file plan only if justified;
5. routing changes only if needed;
6. tests that would catch wrong routing or overengineering.

Repository-wide authoring rules live in `docs/authoring-guide.md`.