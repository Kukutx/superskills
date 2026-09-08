---
name: prompt-optimizer
description: Turn rough intent into a precise, copy-ready prompt or reusable prompt template. Use only when the user explicitly wants a prompt, prompt improvement, or reusable AI instruction.
---

# Prompt Optimizer

## Use

Use when the requested deliverable is the **prompt itself**.

Do not use as automatic preprocessing when the user wants the final task result directly.

## Core principle

For capable agents, write a **delegation contract**, not a pseudo-workflow engine. State the desired outcome, boundaries and completion evidence; let the model handle routine planning and tool sequencing unless a specific procedure is itself part of the requirement.

Keep only instructions that materially improve the target result or prevent a realistic failure mode.

## Workflow

1. Preserve the user's real goal, source of truth and explicit constraints.
2. Identify the target model/tool/harness only when its current capabilities materially affect the prompt; verify current official behavior instead of hardcoding stale version assumptions.
3. Define the objective and observable success criteria.
4. Specify only the context, inputs and constraints that change the result.
5. For action-oriented agents, define the authority boundary: continue through safe/reversible work and escalate only user-only decisions, truth-critical gaps or consequential actions not already authorized.
6. Define verification and the completion boundary so the agent can self-correct instead of stopping at a plausible draft.
7. Specify output style or schema only as tightly as the downstream use requires.
8. Remove redundant roles, repeated rules, forced planning and unnecessary sections.

## Agentic prompt shape

Use only the fields the task actually needs:

```text
Objective
Context / source of truth
Success criteria
Constraints
Authority / escalation boundary
Verification / definition of done
Output format
```

For simpler tasks, collapse this into natural language rather than emitting a template mechanically.

## Tuning decisions

When current model behavior matters, tune the smallest observed weakness instead of copying an old prompt stack forward. Examples:

- if the agent stops too early, strengthen initiative and follow-through;
- if it asks too many questions, tell it to finish authorized/reversible work before escalating;
- if Skill files create conflicts, make current user instructions and source-of-truth precedence explicit;
- if verification becomes excessive, calibrate tests to risk and changed behavior;
- if a multi-agent harness should parallelize work, specify when delegation is useful.

Verify version-specific syntax and capabilities at execution time rather than storing them as permanent runtime truth.

## Output

Default:

1. **Optimized prompt** — copy-ready.
2. **Reusable template** — only when repeat use is useful.
3. **Variants** — only when genuinely different strategies are valuable; max 3.

Do not add a “why this works” essay unless requested.

## Constraints

- Do not turn a simple request into a long pseudo-system specification.
- Do not force chain-of-thought, visible reasoning or a plan-first ritual.
- Do not micromanage tool order unless the order is a real requirement.
- Do not add roles, sections, restrictions or approval gates that do not improve the target result.
- Do not reinterpret or broaden the user's intent.
- If the target tool is unknown, write tool-neutral instructions unless tool-specific syntax matters.
- Ask only when a missing detail cannot be inferred safely and would materially change the prompt contract; otherwise choose the smallest reasonable default.
