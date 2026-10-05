---
name: inventory-reorder
description: Decide what stock to reorder and how much from sales and inventory data, with days of cover, lead time, dead-stock flags and a draft purchase order. Not for storefront or theme development.
---

# Inventory Reorder

## Use

Use when a store or product business asks what to restock, whether something will run out, what is tying up cash on the shelf, or wants a purchase order drafted for a supplier.

Shopify themes, Liquid and store integration belong to `ecommerce/shopify-dev`. Cash available to fund the order belongs to `finance/cash-flow-forecast`.

## Domain inputs and blockers

Per SKU, at the variant level (size, colour), not rolled up by product: units sold by date, stock on hand, units already on order, unit cost, supplier, lead time, and case size or minimum order. Two files are enough: sales by SKU and date, and a stock list.

Ask for what the data cannot show:

- **The date of the stock count.** A count two weeks old puts every stockout date two weeks out; subtract the sales since or recount the fast movers.
- **Lead time**, once per supplier.
- **Seasons**: which SKUs are seasonal and when the season starts and ends. A season is stated by the user, never inferred from a quiet month.
- Anything that distorts recent sales: a bulk order, a promotion, a price change, a supplier shutdown.

Refunds and cancelled orders are not sales. With less than 28 days of history for a SKU, report that there is not enough history rather than a velocity.

## Velocity

Compute daily sales over the last 7 days and the last 28 days, counting only days the item was in stock. A stockout is suppressed demand, not zero demand; dividing by all days understates demand, which leads to a smaller order and an earlier stockout.

When the two differ by more than half, look at the orders underneath before trusting either: one wholesale order can make a slow item look like a bestseller for a week.

Use each for its own job, and label which was used on every line:

- **Stockout velocity** = the higher of the two, for days of cover and the stockout date. Better early than late.
- **Sizing velocity** = the 28-day figure, for the order quantity.

## Status

Days of cover = (on hand + on order) ÷ stockout velocity. Buffer = half the lead time, at least 7 days and at most 30; a long lead time is handled by ordering more often, not by a bigger buffer.

| Cover | Status |
| --- | --- |
| less than the lead time | too late: an order now only shortens the gap |
| less than lead time + buffer | order now |
| under 45 days | next cycle |
| 45 to 120 days | fine |
| over 120 days | overstocked |

## Order quantity

Target = (60 + lead time in days) × sizing velocity. Order = target − on hand − on order, never below zero, rounded up to the case size unless that pushes cover past 90 days, in which case round down and say so.

A minimum order usually applies to the whole supplier order, not each line. When the total falls short, show the user the shortfall in units, money and days of cover and let them choose; do not pad lines quietly.

**Zero sales in 28 days**: no cover figure, no reorder. It goes on a slow-mover list with the cash it holds. Ninety days without a sale is dead stock. The exception is an item the user names as seasonal and out of season: it goes on a dated watch list with a decision date of season start minus lead time.

**Seasonal uplift** needs more than a year of history: factor = sales in the same window last year ÷ sales in the 28 days before it last year. A factor above 3 or below 0.3 is shown to the user, not applied silently, and a window that was out of stock last year cannot be used. Without the history, use the user's own estimate and label it as theirs. When the season's end date is known, cap the order at what can sell between arrival and the end, and show both the capped and uncapped figure.

## Output

Lead with the total money to commit and the number of items about to run out. Then four groups: order now, next cycle, slow movers, not enough history. Each line shows both velocities, on hand and on order, days of cover and which velocity produced it, lead time and buffer, the target, the order quantity with its rounding, and the cost.

A purchase order is one per supplier: date and requested arrival, lines with SKU, description, quantity, unit and unit price, shipping and terms. Use the last known price with its date, or leave it blank; ask the supplier whether the price still holds.

## Constraints

- Every recommendation carries its cost; a reorder list without money is not a decision.
- Approving the list and sending a purchase order are separate; nothing is sent from here.
- A substitute item offered by a supplier is the user's decision.
- Data problems are reported, not smoothed: negative stock, sales with no stock record, the same SKU under two names.
