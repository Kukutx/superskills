# kukutx Project Instructions

Use `superskills` as a routing and domain-knowledge system, not text to repeat back.

## Behavior

- Default to Chinese unless the requested artifact should use another language.
- Be concise, concrete and directly usable.
- Choose the most specific domain Skill that matches the task.
- Start with one primary Skill; add another only for a distinct subtask.
- Route internally and execute; do not narrate routing unless useful.
- Make reasonable assumptions when safe. Ask only when one missing detail would materially change the result.
- Respect existing project conventions; avoid unrelated rewrites and dependencies.
- Verify changing facts, APIs, policies, prices and platform rules instead of relying on repository memory.
- Match completion claims to actual evidence: static, runtime, visual, external or production.

## Routing

The authoritative catalog is:

`skills/meta/skill-router/skill.md`

Use it only when ownership is ambiguous. If the task clearly belongs to a domain Skill, go there directly.

Meta Skills are explicit tools, not automatic preprocessing. In particular, do not run prompt optimization when the user asked for the final task result.

## Progressive disclosure

Read the selected `skill.md` first. Load `references/` only when needed by the current subproblem. Do not load `maintenance/` during normal execution.

For a complex domain such as Godot 2D, normally use only 1–3 focused references at a time.

## Output

Use the smallest structure that serves the task; do not emit empty template sections.

For technical changes, make clear:

- what is wrong / decided;
- where to change;
- how to change it;
- why;
- how to verify.
