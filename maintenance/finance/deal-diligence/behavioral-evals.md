# Deal Diligence behavioral evals

Maintenance-only. Protect the buy-versus-value-versus-sell triangle: deal-diligence buys, company-valuation values, selling-a-business sells.

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| deal-diligence-001 | “我想收购这家小公司，帮我尽调一下：财务、客户、合同和风险，值不值得买？” | `finance/deal-diligence` | none | valuing the company in isolation without a buy decision |
| deal-diligence-002 | “这家公司财报有水分吗？有哪些隐藏负债和法律风险？” | `finance/deal-diligence` | none | producing a valuation report instead of a buy-or-not diligence verdict |
| deal-diligence-003 | “这家公司现在值多少钱？用 DCF 和可比公司算一下。” | `finance/company-valuation` | none | invoking deal-diligence for a standalone valuation with no acquisition in view |
