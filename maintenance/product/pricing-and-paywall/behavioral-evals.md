# Pricing and Paywall behavioral evals

Maintenance-only. Protect the boundary against unit-economics (judging revenue quality, not setting prices).

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| pricing-and-paywall-001 | “我们的免费版和付费版怎么分？定价多少，什么时候弹 paywall？” | `product/pricing-and-paywall` | none | judging revenue quality with LTV and CAC instead of setting prices |
| pricing-and-paywall-002 | “算一下我们的 LTV、CAC 和回本周期，收入质量怎么样？” | `finance/unit-economics` | none | setting prices or paywall moments |
