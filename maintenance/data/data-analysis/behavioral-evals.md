# Data Analysis behavioral evals

Maintenance-only. Protect the boundary against metrics-review (a recurring KPI report) and sql-query-writing (writing the query).

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| data-analysis-001 | “这是上个月的用户行为数据，帮我探索一下流失和什么因素有关。” | `data/data-analysis` | none | writing a SQL query instead of analysing the data |
| data-analysis-002 | “帮我写一个 SQL 查询，查出上个月每个渠道的新增用户数。” | `data/sql-query-writing` | none | invoking data-analysis to explore when the ask is a query |
| data-analysis-003 | “帮我出一份这个月的 KPI 月报，看看各指标和上个月比怎么样。” | `data/metrics-review` | none | treating a recurring KPI report as an open-ended exploration |
