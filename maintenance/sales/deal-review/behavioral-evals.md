# Deal Review behavioral evals

Maintenance-only. Protect the boundary against sales-pipeline-review (the whole pipeline, not one deal).

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| deal-review-001 | “这个单子卡在谈判三周了，帮我看一下这一个 deal 的健康度、风险和下一步。” | `sales/deal-review` | none | reviewing the whole pipeline instead of this one deal |
| deal-review-002 | “这个客户的决策人换了，预算也没批，我该怎么推进这一单？” | `sales/deal-review` | none | treating a single-deal question as a pipeline forecast |
| deal-review-003 | “帮我看一下这个季度 pipeline 健不健康，预测能成多少？” | `sales/sales-pipeline-review` | none | invoking deal-review for a whole-pipeline forecast |
