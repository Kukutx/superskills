# Chinese Novel Writing behavioral evals

Maintenance-only. Protect the novel/business-copy boundary and the plan-before-writing rule.

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| chinese-novel-001 | “帮我写一部 20 章的悬疑小说，主角是个法医。” | `writing/chinese-novel-writing` | none | starting Chapter 1 before the three-layer questions and the confirmed plan |
| chinese-novel-002 | “写一段产品宣传文案，突出新功能。” | `writing/marketing-copy` | none | invoking chinese-novel-writing for business copy |
