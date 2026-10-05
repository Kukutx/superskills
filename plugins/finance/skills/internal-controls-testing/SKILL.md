---
name: internal-controls-testing
description: Plan and document internal control testing for SOX 404 or an audit, with control matrices, sample selection, workpapers and deficiency classification. Use for controls and audit prep, not bookkeeping.
---

# Internal Controls Testing

## Use

Use when a control over financial reporting has to be described, tested or evaluated: scoping which accounts matter, writing a control matrix, choosing a sample, filling a workpaper, or classifying a deficiency.

Reconciling the accounts themselves belongs to `finance/books-close-and-reconciliation`. A repeatable procedure document belongs to `operations/sop-builder`.

This prepares the work. Materiality and the final rating of a deficiency are judged by the auditor, and the sample sizes below are a common starting table that the auditor's own methodology overrides. Say both in the output.

## Domain inputs and blockers

- The control: who does what, how often, with which evidence, and which risk it addresses.
- The period it must cover.
- The complete population of occurrences. A sample drawn from an incomplete list proves nothing, so a missing or partial population is the one true blocker for sampling.
- For a system report used as evidence, how its completeness and accuracy are known.

## Scoping

An account is significant when a material misstatement is more than remotely possible. Quantitative signals: a balance above roughly 3% to 5% of the benchmark, high transaction volume, heavy estimation. Qualitative signals: complex accounting, exposure to fraud (cash, revenue, related parties), a history of adjustments, management judgement, a new process.

Assertions that usually matter:

| Area | Assertions |
| --- | --- |
| revenue | occurrence, completeness, accuracy, cut-off |
| receivables | existence, valuation, rights |
| inventory, fixed assets | existence, valuation, completeness |
| payables | completeness, accuracy, existence |
| accrued liabilities | completeness, valuation |
| close and reporting | presentation, accuracy, completeness |

## Testing

- **Design** is tested by a walkthrough of one transaction end to end, at least yearly and whenever the process changes.
- **Operation** is tested by inspection, observation, re-performance or inquiry. Inquiry alone is never enough.
- **Selection**: random by default; targeted (large, unusual, period-end, related-party, manual override) with the reason recorded; systematic with interval = population ÷ sample size and a random start.
- **Sample size by frequency**, low to high risk: annual 1; quarterly 2 to 3; monthly 2 to 4; weekly 5 to 15; daily 20 to 40; per transaction 25 to 60. Increase it when inherent risk is high, the control is the only one covering the risk, it failed last year, it is new, or the external auditor relies on this testing.
- An automated control whose configuration has not changed can be tested once, provided change management over the system is tested too. A manual control that depends on a system report needs both the review and the report's completeness and accuracy tested.

Evidence that stands: a screenshot showing the system enforcing the rule, a signed or system-logged approval with an identifiable approver and date, an audit log, a recalculation that agrees. Evidence that does not: a verbal confirmation, an undated document, an approval nobody can attribute, a report with no timestamp.

## Evaluating deficiencies

- **Deficiency**: a design or operating gap that falls below the two levels that follow.
- **Significant deficiency**: less severe than a material weakness, important enough for those charged with governance.
- **Material weakness**: a reasonable possibility that a material misstatement would not be prevented or detected in time.

Indicators of a material weakness: fraud by senior management of any amount, restatement of issued statements, a material misstatement found by the auditor that the company's controls missed, ineffective oversight by the audit committee, a pervasive failure in entity-level or IT general controls.

Deficiencies touching the same process or assertion are evaluated together, and a failed compensating control aggravates the result. A remediation records the root cause (design gap, execution, staffing, training, system), the fix, the owner, the date, and how it will be retested.

## Output

- **Control matrix**: control number, description, type (preventive or detective, manual or automated), frequency, key or non-key, risk, assertion.
- **Sample table**: sample number, date, reference, amount, basis of selection.
- **Workpaper**: objective, steps, expected evidence, population and sampling rationale, result per sample with exceptions, conclusion and its basis, tester and reviewer with dates.

## Constraints

- A test with an exception is reported with the exception; an unexplained failure is not re-sampled away.
- Do not rate a deficiency as final; give the proposed level and the reasoning for the auditor.
- Evidence that could not be inspected is listed as not inspected.
- This is not audit or legal advice.
