# Selling a Business behavioral evals

Maintenance-only. Protect the buy-versus-value-versus-sell triangle: selling-a-business sells, deal-diligence buys, company-valuation values.

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| selling-a-business-001 | “我想把公司卖掉，帮我准备出售流程、买家清单和信息备忘录。” | `finance/selling-a-business` | none | valuing the company in isolation without a sale process |
| selling-a-business-002 | “有个买家出价了，这个报价合不合理？我该怎么谈？” | `finance/selling-a-business` | none | running a buy-side diligence on the seller's own business |
| selling-a-business-003 | “我想收购这家公司，帮我尽调一下值不值得买。” | `finance/deal-diligence` | none | invoking selling-a-business for a buy-side decision |
