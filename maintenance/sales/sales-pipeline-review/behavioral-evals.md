# Sales Pipeline Review behavioral evals

Maintenance-only. Protect the boundary against deal-review (one deal) and revops (designing the pipeline system).

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| sales-pipeline-review-001 | “帮我看一下这个季度 pipeline 健不健康，覆盖率够不够，哪些阶段在漏单？” | `sales/sales-pipeline-review` | none | reviewing one deal in depth instead of the whole pipeline |
| sales-pipeline-review-002 | “预测一下这个季度能完成多少，哪些单子最可能丢？” | `sales/sales-pipeline-review` | none | redesigning lifecycle stages instead of reviewing the current pipeline |
| sales-pipeline-review-003 | “帮我设计一下 MQL 到 SQL 的交接标准和评分规则。” | `sales/revops` | none | invoking sales-pipeline-review to design the revenue system |
