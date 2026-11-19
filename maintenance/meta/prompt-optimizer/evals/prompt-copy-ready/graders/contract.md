---
type: llm
---

PASS if the reply leads with one copy-ready prompt (for example in a code block) that states the objective, the input it expects, what the minutes must contain (such as decisions, action items with owners and deadlines), and an output format, and the reply adds at most a few short lines outside the prompt.
FAIL if the prompt tells the target model to show step-by-step reasoning or chain-of-thought, if the reply includes a long "why this works" explanation, or if it gives more than three alternative prompts.
