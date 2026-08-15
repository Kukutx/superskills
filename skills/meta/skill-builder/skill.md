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

1. Inspect existing Skills and routing before adding anything.
2. Define the exact task boundary and nearest overlapping Skill/reference.
3. Prefer improving an existing owner over creating a parallel owner.
4. Write one concise `skill.md` first.
5. Add `references/` only when task-dependent domain depth justifies progressive loading.
6. When splitting content into references, **move ownership rather than copy it**; keep only routing/summary rules in `skill.md`.
7. Ensure every runtime reference is discoverable from the owning `skill.md` with a clear “when to load” boundary.
8. Add `maintenance/` only for sources, regression tests or substantial history that normal execution should not load.
9. Update the global Router only if task selection changes.
10. Add a routing pressure case when a new/changed boundary could be confused with an existing route.
11. Run `python tools/validate_repo.py` and fix structural/orphan-reference failures before completion.

## Default file shape

```text
skills/<category>/<skill>/
└── skill.md
```

Add only when justified:

```text
references/    # runtime domain depth, routed from skill.md
maintenance/   # sources/tests/history, not runtime context
```

Do **not** create `prompt-template.md`, `examples.md` or `changelog.md` by default. Git already stores history, and small examples/templates belong in `skill.md` when they change behavior.

## skill.md quality bar

Keep only content that changes Agent behavior:

- `name` + routing-quality `description` frontmatter;
- when to use / not use;
- workflow or decision rules;
- reference routing boundaries;
- output contract when useful;
- hard constraints / anti-patterns;
- validation.

Avoid repeating the same instruction as Purpose + Role + System Prompt.

## Reference quality bar

A runtime reference should have one clear semantic owner and answer a task-dependent question that the main Skill should not preload.

Before adding one, ask:

```text
What decisions live here?
When should the Agent load it?
What neighboring reference must not own the same details?
Can skill.md route to it clearly?
Would deleting it materially reduce task quality?
```

If content must appear in two places, keep the authoritative rule in one place and use a short cross-reference elsewhere instead of maintaining two copies.

Version-sensitive source inventories, tool catalogs and compatibility snapshots belong in `maintenance/` or should be verified at execution time; do not turn them into permanent runtime truth.

## Output

When asked to design/audit a Skill, provide or implement:

1. recommended path;
2. overlap decision: create / merge / keep existing;
3. `skill.md` changes;
4. optional references only when progressive disclosure is real;
5. routing changes only if needed;
6. regression/pressure tests for changed boundaries;
7. validation result.

Repository-wide authoring rules live in `docs/authoring-guide.md`.
