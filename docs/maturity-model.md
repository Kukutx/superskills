# Skill Maturity Model

This document defines how mature a skill is inside `superskills`.

## Levels

| Level | Meaning | Requirements |
| --- | --- | --- |
| `draft` | Rough but useful starting point | Has role, purpose, output format |
| `usable` | Can be used for real tasks | Has input fields, constraints, default assumptions |
| `refined` | Reliable across common scenarios | Has examples, anti-patterns, quality checklist |
| `stable` | Mature workflow | Has changelog, edge cases, tested examples, low ambiguity |

## Promotion rules

### draft → usable

A skill can be marked `usable` when it has:

- Clear role
- Clear use cases
- Input fields
- Output contract
- Hard constraints
- Default assumptions

### usable → refined

A skill can be marked `refined` when it has:

- At least 2 good examples
- At least 1 bad example
- Edge case handling
- Quality checklist
- Known limitations

### refined → stable

A skill can be marked `stable` when:

- It has been used successfully in multiple real tasks.
- Its output format rarely needs correction.
- It handles missing information well.
- Its examples reflect real workflows.

## Quality signals

A mature skill should produce answers that are:

- Directly usable
- Structurally consistent
- Clear about assumptions
- Low on filler
- Explicit about tradeoffs
- Easy to copy into another tool or workflow

## Common failure modes

| Failure | Fix |
| --- | --- |
| Too much generic advice | Add hard output contract and anti-patterns |
| Too many clarifying questions | Add default assumptions |
| Output is not actionable | Add required fields and checklist |
| Skill overlaps with another skill | Add `When not to use` section |
| Results are inconsistent | Add examples and expected output patterns |
