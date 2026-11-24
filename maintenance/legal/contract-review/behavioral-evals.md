# Contract Review behavioral evals

Maintenance-only. Protect the boundary against nda-triage (an NDA alone is a screen, not a full review).

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| contract-review-001 | “这份供应商合同里有没有坑？帮我逐条看一下，标出要改的地方。” | `legal/contract-review` | none | screening it as an NDA only |
| contract-review-002 | “对方发来一份 NDA，能签吗？” | `legal/nda-triage` | none | running a full contract review on an NDA alone |
