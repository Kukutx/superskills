# Customer Support Replies behavioral evals

Maintenance-only. Protect the boundary against review-replies-and-winback (public reviews) and business-email (one-off email).

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| customer-support-replies-001 | “有个客户发工单说收不到验证码，帮我分流并写一封回复，判断要不要升级给工程。” | `support/customer-support-replies` | none | answering as if it were a public review |
| customer-support-replies-002 | “客户在 Google 上给了我们一星差评，说配送太慢，帮我回一下。” | `support/review-replies-and-winback` | none | invoking customer-support-replies for a public review reply |
| customer-support-replies-003 | “帮我写一封邮件给供应商，问一下这批货什么时候到。” | `writing/business-email` | none | treating a one-off business email as a support ticket |
