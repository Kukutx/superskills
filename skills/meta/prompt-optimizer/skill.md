---
name: prompt-optimizer
description: Turn rough intent into a precise, copy-ready prompt or reusable prompt template. Use only when the user explicitly wants a prompt, prompt improvement, or reusable AI instruction.
---

# Prompt Optimizer

## Use

Use when the requested deliverable is the **prompt itself**.

Do not use as automatic preprocessing when the user wants the final task result directly.

## Workflow

1. Preserve the user's real goal and constraints.
2. Identify the target tool only when its capabilities materially affect the prompt.
3. Remove ambiguity that would change output quality; do not add invented requirements.
4. Specify required inputs, expected output and important avoid rules.
5. Keep the prompt as short as possible while still controlling the important failure modes.

## Output

Default:

1. **Optimized prompt** — copy-ready.
2. **Reusable template** — only when repeat use is useful.
3. **Variants** — only when genuinely different strategies are valuable; max 3.

Do not add a “why this works” essay unless requested.

## Constraints

- Do not turn a simple request into a long pseudo-system specification.
- Do not add roles, sections or constraints that do not improve the target result.
- Do not reinterpret or broaden the user's intent.
- If the target tool is unknown, write tool-neutral instructions unless tool-specific syntax matters.
- Ask only when one missing detail would materially change the prompt.