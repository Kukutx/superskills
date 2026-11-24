# Company Valuation behavioral evals

Maintenance-only. Protect the buy-versus-value-versus-sell triangle: company-valuation values, deal-diligence buys, selling-a-business sells.

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| company-valuation-001 | “这家公司现在值多少钱？用 DCF 和可比公司算一下。” | `finance/company-valuation` | none | turning a valuation into a buy-or-not diligence verdict |
| company-valuation-002 | “这只股票贵不贵？帮我算一下内在价值。” | `finance/company-valuation` | none | writing a full stock research thesis instead of a valuation |
| company-valuation-003 | “我想把公司卖掉，帮我准备出售流程、买家清单和备忘录。” | `finance/selling-a-business` | none | invoking company-valuation for a sale process |
