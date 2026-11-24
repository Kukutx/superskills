# RevOps behavioral evals

Maintenance-only. Protect the boundary against sales-pipeline-review (reviewing an existing pipeline) and marketing-plan (planning the campaign).

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| revops-001 | “市场部说的 MQL 销售根本不认，怎么定一个两边都认的 MQL 标准和交接流程？” | `sales/revops` | none | writing outreach copy, or reviewing a single pipeline snapshot instead of defining the handoff |
| revops-002 | “线索评分怎么做？哪些行为算购买意向，多少分才算 MQL？” | `sales/revops` | none | treating content downloads as buying intent without negative scoring |
| revops-003 | “帮我看一下这个季度 pipeline 健不健康，有哪些单子要丢了？” | `sales/sales-pipeline-review` | none | invoking revops to redefine lifecycle stages for a pipeline health review |
