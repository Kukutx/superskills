# User Research behavioral evals

Maintenance-only. Protect the boundary against research-brief (establishing external facts, not learning from users).

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| user-research-001 | “访谈了 8 个用户，录音转录在这里，帮我提炼主题和改进建议。” | `research/user-research` | none | treating interview themes as established external facts |
| user-research-002 | “帮我查一下竞品最近的价格变化，有来源。” | `research/research-brief` | none | running user interviews to answer a factual question |
