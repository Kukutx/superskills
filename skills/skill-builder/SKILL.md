---
name: skill-builder
description: Create, audit, simplify or restructure reusable skills in the superskills repository. Use when a workflow deserves persistent agent guidance rather than a one-off answer.
---

# Skill Builder

## First decision: does this deserve a Skill?

Create or expand a Skill only when the task repeats and there are **durable decision rules, constraints or domain knowledge** worth preserving.

Do not create one for a one-off prompt, generic global behavior, a renamed duplicate owner or notes that do not change Agent decisions.

## Intake: a prompt or Skill found elsewhere

When the user shares an interesting prompt, Skill or workflow to collect:

1. Extract the durable decision rules it encodes; drop persona prose, formatting rituals and model-specific tricks that current models no longer need.
2. Decide one outcome: **merge** into the nearest existing owner, **new** Skill (only if the first decision above holds), or **reject** with a one-line reason. Prefer merge.
3. Never copy third-party text whose license does not allow it; rewrite the rules in your own words and record the source URL in that Skill's maintenance `sources.md` when it materially shaped the rules.
4. Give a new Skill a description that says what it does and when to use it, add it to the Router Catalog, and add an eval case under `evals/` when its value depends on behavior a plain model would get wrong.

## Workflow

1. Inspect existing Skills, references, routing and project instructions first.
2. Define the exact owner and nearest overlap.
3. Prefer improving, renaming, splitting or merging an existing owner over creating a parallel one.
4. Remove duplicated global behavior before adding new guidance.
5. Write one concise `SKILL.md` first.
6. Add `references/` only for task-dependent depth with a clear decision boundary.
7. When splitting, **move ownership rather than copy it**.
8. Ensure every runtime reference is discoverable from `SKILL.md` and keep references one directory level deep.
9. Use `behavioral-evals.md` under maintenance/ for real routing, ownership, autonomy or blocker regressions and `sources.md` only for substantial source inventories.
10. Do not create changelog files; Git stores history. Use `decisions.md` only when current design rationale is genuinely needed.
11. Update the global Router only when task selection changes.
12. Run `python tools/validate_repo.py` and fix structural, orphan or stale-route failures.

## Default shape

```text
skills/<skill>/
└── SKILL.md
```

Add only when justified:

```text
references/    # runtime domain depth
maintenance/   # behavioral evals / sources / rare current design rationale
```

## `SKILL.md` quality bar

Keep only content that changes behavior:

- `name` + third-person `description` that says what the Skill does and when to use it, with the trigger words users actually say; it is the only text an agent sees before loading the Skill;
- scope / not-scope;
- durable domain decisions or invariants;
- domain-specific inputs and true blockers;
- reference routing boundaries;
- important constraints;
- validation/completion boundary.

Prefer goals, decision boundaries and success criteria over generic step-by-step process. Avoid repeated Purpose/Role/System Prompt prose.

## Agentic quality bar

A capable agent already knows how to inspect context, plan internally, use tools, make routine reversible choices and report results. Those generic behaviors belong in `gpts/kukutx/project-instructions.md`, not in every Skill.

A domain Skill should not force the agent to pause merely because information is imperfect. Add a pause or confirmation rule only when the domain has a real user-only fact, truth boundary, irreversible action or high-impact choice that cannot be resolved from available context.

If the user asks for execution, the Skill should guide execution rather than reinterpret the task as a request for a plan. Multi-step work is not by itself a reason to route to `project-planner`.

## Reference quality bar

A reference needs one semantic owner and one task-dependent question the entrypoint should not preload.

Before adding or splitting, check:

```text
What decisions live here?
When should it load?
What neighboring owner must not duplicate it?
Does the split reduce real context or clarify truth ownership?
What behavioral eval proves the boundary matters?
```

If content must appear twice, keep the authoritative rule once and cross-reference it elsewhere.

## Output

When designing or auditing a Skill, implement or provide only what is needed:

1. recommended owner/path;
2. overlap decision: create / rename / split / merge / keep;
3. runtime content changes;
4. routing changes only when needed;
5. behavioral regression cases for changed boundaries;
6. validator result.

Repository-wide rules live in `docs/authoring-guide.md`.
