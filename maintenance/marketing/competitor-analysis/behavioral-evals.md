# Competitor Analysis behavioral evals

Maintenance-only. Protect the sharpest boundary in the repo: comparison for a differentiation claim (product-positioning) against comparison as the deliverable (competitor-analysis).

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| competitor-analysis-001 | “帮我对着 X 定位我们的产品，找出差异化卖点。” | `marketing/product-positioning` | none | building a battlecard when the ask is a positioning claim |
| competitor-analysis-002 | “帮我做一张针对 X 的 battlecard，销售打单时用的。” | `marketing/competitor-analysis` | none | writing a positioning statement when the ask is a battlecard deliverable |
| competitor-analysis-003 | “做一页‘X 的替代品’对比页面，给正在考虑换产品的读者看。” | `marketing/competitor-analysis` | `marketing/competitor-analysis:comparison-pages.md` | handing the page to product-positioning as a messaging task |
