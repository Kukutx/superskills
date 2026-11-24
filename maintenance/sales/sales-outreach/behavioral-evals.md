# Sales Outreach behavioral evals

Maintenance-only. Protect the boundary against sales-call-prep-and-recap (a call that is already booked) and revops (the system that routes and scores leads).

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| sales-outreach-001 | “给我写一封 cold email 给一家 SaaS 公司的运营负责人，介绍我们的报表工具，并准备两封跟进邮件。” | `sales/sales-outreach` | none | routing the request to revops as a lifecycle design task |
| sales-outreach-002 | “有个客户回我说‘现在没预算’，帮我写一封回信处理这个异议。” | `sales/sales-outreach` | none | treating the objection as a call prep task for a booked meeting |
| sales-outreach-003 | “下周二要跟一个客户开电话会，帮我准备一下要问的问题和会后跟进。” | `sales/sales-call-prep-and-recap` | none | invoking sales-outreach to write cold outreach for a meeting that is already booked |
