---
name: us-self-employed-tax-prep
description: Prepare US federal quarterly estimated tax maths and a 1099-NEC contractor list as notes for an accountant. Use for US self-employment tax, 1099s and W-9s, not for filing or non-US tax.
---

# US Self-Employed Tax Prep

## Use

Use for a US sole proprietor, freelancer or small business preparing two things for their accountant: how much to set aside or pay as quarterly estimated federal tax, and who needs a Form 1099 for the year.

Closing the books first belongs to `finance/books-close-and-reconciliation`. Any other country's tax is outside this Skill: for a non-US business, say so and offer only a clean set of closed books for their own adviser; do not run the US arithmetic under another name.

Every deliverable opens with "Prepared for review by your accountant — not tax advice" and closes with the accountant's checklist. Nothing is filed from here.

## Domain inputs and blockers

- **Country and business structure.** Self-employment tax applies to a sole proprietor or single-member LLC and, generally, to partners on their earnings. Owners of S and C corporations are paid through payroll instead, so this arithmetic does not fit them. With no answer, assume sole proprietor and state it.
- **The tax year**, shown in the header.
- Year-to-date net profit from closed books, estimated tax already paid this year, and whether the business is seasonal.
- For 1099s: payments by payee with dates, and each payee's W-9 status.

**Year-specific figures are never recalled.** Brackets, the Social Security wage base, reporting thresholds and exact due dates change every year. Take each from the IRS page or instructions for the year in question, opened in this session or supplied by the user, and note the source and date; when that is not possible, leave the figure as a labelled input for the accountant. An invented bracket table looks exactly like a real one.

Books that are not closed produce a wrong estimate. When items are still unresolved, quantify what they could do to the result and write it into the body as an assumption.

## Quarterly estimate

1. **Annualize first.** Annualized net = year-to-date net ÷ months elapsed × 12, and show both figures labelled. For a seasonal business ask for the owner's full-year estimate instead and label it as theirs.
2. **Self-employment tax** = net earnings × 92.35% × 15.3%. The 15.3% is 12.4% Social Security plus 2.9% Medicare; the Social Security part stops at the year's wage base. Half of the self-employment tax is deductible in arriving at adjusted gross income.
3. **Income tax** is computed on net profit less that half, never on gross revenue. With no better information use a single stated effective rate and say that it is an assumption, or apply the year's brackets taken from the IRS.
4. **Payment per remaining period** = (total estimated liability − estimated tax already paid) ÷ periods remaining.
5. **Due dates** follow four periods that are not calendar quarters: January–March, April–May, June–August, September–December, due in mid-April, mid-June, mid-September and mid-January of the following year, moved to the next business day when they fall on a weekend or holiday. Take the exact dates for the year from the IRS.
6. **A missed period** is named with its amount and date, and the catch-up is shown on its own line beside the next regular payment. The penalty is not estimated; it depends on prior-year data and is the accountant's to compute.
7. **Avoiding the underpayment penalty**: generally, payments must reach the smaller of 90% of this year's tax or 100% of last year's. Higher-income taxpayers face a stricter prior-year test; take the current rule from IRS Publication 505 and have the accountant confirm last year's figure.

List what the estimate leaves out so nobody mistakes it for the full picture: state and local tax, the qualified business income deduction, home office, vehicle, depreciation, retirement contributions, self-employed health insurance, and losses carried forward.

## 1099 preparation

- Total the year's payments for **services** to each individual or business, by the date paid, not the invoice date. Goods, refunds and internal transfers are excluded.
- **Reporting threshold.** For payments made through 2025 the threshold for nonemployee compensation was 600 dollars. For tax years beginning after 2025 the IRS instructions set it at 2,000 dollars, adjustable for inflation from 2027. Confirm the figure in the current Form 1099-NEC instructions for the year being prepared, and keep a "near the threshold" list for the accountant.
- Pull every payee above the threshold, not only those tagged as 1099 vendors in the bookkeeping software; many businesses never set the tag.
- Payments to corporations are generally not reportable, with exceptions such as attorneys' fees. Mark corporate payees; do not drop them.
- Similar names (John Smith and John A. Smith) are listed side by side with their totals, not merged.
- Payments made through a card or third-party payment network may be reported by that network on its own form. Flag the overlap for the accountant instead of deciding which form applies.
- **W-9 status** per payee: on file, missing, or unknown. Missing ones lead the action list because they block filing; Form 1099-NEC is due to recipients and the IRS by January 31.
- Name any payment source that could not provide payee-level detail, instead of silently leaving its payees out.

## Output

- **Estimate**: tax year, year-to-date snapshot, self-employment tax, income tax estimate, total liability, payment per remaining period with dates, the penalty-avoidance test, the assumptions, the exclusions, and the accountant's checklist.
- **1099 package**: summary counts, candidate table (payee, total, source, W-9 status, notes), missing W-9 actions, near-threshold list, payment-network overlaps, and the accountant's checklist.

## Constraints

- No Social Security number, full bank or card number appears in any output; a business's employer identification number is the one exception.
- Advice is phrased as a question for the accountant ("ask whether a retirement plan contribution would reduce this"), never as an instruction to the user.
- Which form applies, whether a payee is exempt, and any penalty are the accountant's decisions.
