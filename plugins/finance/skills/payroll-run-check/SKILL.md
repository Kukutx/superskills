---
name: payroll-run-check
description: Prepare a payroll run from timesheets, turning hours into a per-person sheet and flagging missed punches, unusual overtime, rate changes and gaps before pay is released. Not for tax filing.
---

# Payroll Run Check

## Use

Use when hours have to become pay: checking timesheets before a run, building the per-person run sheet, explaining why this period costs more than the last, or drafting the ledger entry afterwards.

Whether there is cash to cover the run belongs to `finance/cash-flow-forecast`. Hiring and pay-setting belong to `people/hiring`.

This prepares and checks. The employer releases pay; a released run is hard to reverse and the reversal is visible to employees, so the step between prepared and released is the last free chance to catch an error.

## Domain inputs and blockers

Period start and end, pay date and frequency; who is on the run and whether hourly or salaried; the timesheets; pay rates from the payroll records; last period's totals.

Ask once, because each silently changes every result:

- **Are meal breaks already deducted** in the sheet? Deducting twice, or not at all, is half an hour per person per day.
- **Which overtime rule applies.** Overtime law varies by jurisdiction and worker classification. Use the rule the employer states; with none stated, default to weekly overtime with no rounding and say that this default was used.
- Twice a month (24 runs) or every two weeks (26)? The two are often confused.

Rates come from payroll records. A rate written on a timesheet is a note, not the rate.

## Rules that are never bent

1. **A shift with a missing punch has unknown hours.** It is not filled with the usual end time: a completed sheet looks normal, nobody rechecks it, and an over- or underpayment goes unnoticed. The person's line says that gross pay excludes that shift.
2. **Anomalies are reported, never corrected**, however obvious the fix looks.
3. **Employer taxes are not estimated.** They are shown only when the payroll system supplies them; otherwise they are "not available", totals are labelled gross, and the employer is reminded to add their usual employer share.
4. With punch-level data, recompute hours from the punches even if the sheet has totals. With totals only, use them and say which checks could not run.

## What to flag

Each flag carries four things: who, which day, the two numbers being compared, and the money effect. If the money effect cannot be computed, write "unknown"; an invented amount is worse than none.

Without any history:

- a single shift longer than 12 hours.

With a baseline or schedule:

- more than 16 hours in a day, or seven days worked in a row;
- overtime above 125% of the person's average over the last four periods, or overtime for someone who normally has none;
- total hours more than 10% over the schedule;
- zero hours for someone who normally works.

Pay setup:

- a rate different from last period, up or down, with both rates and the effective date;
- a changed employment type; a new person with no onboarding record; a person present last period and absent now;
- leave taken beyond the balance held in the payroll system.

Group flags by person, unknown hours first and then the largest deviations, and ask about each one separately. "Three small issues, continue?" gets one yes and no review.

Default handling for overtime detail, each stated when used: a rate change within the week uses the weighted average rate; a shift crossing midnight belongs to the day it started; paid leave does not count towards overtime hours; a holiday premium applies only under a written policy.

## Output

Per person: regular, overtime, leave, gross, with flags beneath. Then a summary: period, pay date, headcount, hours by type, gross, employer taxes or "not available", total cash needed, the change from last period with its driver in one sentence when it exceeds 10% (or a plain statement that no driver was found), and the number of open flags. End with one approval question that states the number of people, hours, amount, date and open flags.

After the run is actually released, the ledger entry uses the actual figures: debit wage expense and employer tax expense; credit withheld-tax liabilities, employer-tax liabilities and cash for net pay. Cash is recorded on the pay date. If it does not balance, stop and report; nothing goes to a suspense account. Labour allocated to jobs uses raw wages unless the employer supplies a burden rate, and unallocated hours are shown separately.

## Constraints

- No identity number, date of birth, home address or bank account appears in any output.
- A statement about what overtime law requires is the employer's or an adviser's to make; state the rule applied, not the law.
- Nothing is submitted, released or described as paid.
