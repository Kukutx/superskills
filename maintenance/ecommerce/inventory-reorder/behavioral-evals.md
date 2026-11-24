# Inventory Reorder behavioral evals

Maintenance-only. Protect the boundary against shopify-dev (storefront work, not stock decisions).

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| inventory-reorder-001 | “根据上个月的销量和现在的库存，告诉我该补哪些货、补多少。” | `ecommerce/inventory-reorder` | none | proposing a storefront change or a theme fix |
| inventory-reorder-002 | “帮我改一下店铺首页的横幅和商品分类。” | `ecommerce/shopify-dev` | none | treating a storefront task as an inventory decision |
