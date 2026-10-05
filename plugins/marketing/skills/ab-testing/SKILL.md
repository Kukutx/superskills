---
name: ab-testing
description: Design an A/B test with hypothesis, sample size, primary and guardrail metrics, and read the result without peeking errors. Use for experiments and which version wins, not for auditing a page.
---

# A/B Testing

## Use

Use for "which of these two versions is better", "should we test this", "how long does it have to run", writing the test plan, and deciding what to do with a finished test. It applies to pages, emails, prices, onboarding steps and store listings alike.

This Skill owns the design of the experiment and the decision taken from it. Recomputing the statistics from a raw export, or checking a dataset for errors, belongs to `data/data-analysis`. Finding what is wrong with a page and which ideas are worth testing belongs to `marketing/conversion-review`.

## Domain inputs and blockers

- **Baseline conversion rate** of the thing being changed and **how many eligible visitors, users or recipients it gets per week**. These two decide whether a test is possible at all.
- **The change and the reason for it**, and the smallest improvement that would be worth shipping (the minimum detectable effect). The last one is the user's business judgement; ask for it, and when they cannot say, show the cost in duration of two or three candidate values.
- The tool that will split traffic and report results, when there is one.
- When traffic is unknown, still compute the sample needed per variant and express the duration as a function of weekly traffic, so the user can judge.

## Designing the test

1. **Hypothesis in five parts**: because [observation or data], we believe [change] will cause [expected outcome] for [audience], measured by [metric]. "Try a different button colour and see" has no observation and no expected outcome, so nothing is learned whichever way it goes.
2. **One variable, and a change large enough to detect.** Several changes at once cannot be told apart afterwards; a tiny change needs more traffic than most sites have.
3. **Three layers of metrics, fixed before the start:**
   - *Primary*: the one number that decides the test.
   - *Secondary*: numbers that explain why the primary moved.
   - *Guardrails*: numbers that must not get worse. A guardrail that is significantly worse stops the test.
   A checkout change, for instance, is decided on completed orders per visitor, with refund rate and support contacts as guardrails.
4. **Sample size before launch.** Give a sample-size calculator these inputs and report them with the answer: the baseline rate, the minimum detectable effect and whether it is relative or absolute, the confidence level (95% is the conventional threshold), the statistical power the calculator asks for, and the number of variants. Do not quote a required sample from memory or from a lookup table. The direction to expect: a lower baseline or a smaller effect to detect raises the requirement steeply.
5. **Duration** = sample per variant × number of variants ÷ eligible traffic per week, and never shorter than one full business cycle (often a week), so the test does not sample only part of the cycle.
6. **Allocation.** 50/50 by default. Use 90/10 or 80/20 when a bad variant could do real harm, and a gradual ramp when the risk is technical. A returning user always sees the version they saw first.
7. **When the duration is impractical**, say so before the test starts. The options are a bolder change with a larger expected effect, or more traffic to the tested step. An underpowered test that is run anyway produces noise that gets read as a result.

## While it runs

Do not stop early because one version is ahead, and do not check the result in order to decide whether to stop: looking repeatedly and stopping at the first good moment manufactures false winners. Do not change a variant, and do not add a new traffic source, in the middle of the run; either one makes the two periods incomparable.

## Reading the result

Go through these in order; a later check does not rescue an earlier one that failed:

1. **Was the planned sample reached?** If not, there is no result yet.
2. **Is the difference significant at the threshold set in advance?** A p-value under 0.05 is the conventional cut-off for calling a difference significant. It is a threshold, not a guarantee, and it is not the probability that the result came from chance; do not describe it that way.
3. **Is the effect at least the minimum that was worth detecting?** Report the effect with its confidence interval, not the percentage alone.
4. **Do the secondary metrics tell the same story?**
5. **Did every guardrail hold?**
6. **Do segments differ?** Only segments named in the plan count as findings; a segment discovered afterwards is a hypothesis for the next test.

| Result | Decision |
| --- | --- |
| significant winner, guardrails intact | ship it, and record the pattern and where else it could apply |
| significant loser | keep the control and work out why the hypothesis was wrong |
| no significant difference | the change was too small or the traffic too thin; say which, and do not read a direction into it |
| mixed signals | look at the planned segments, then design a narrower follow-up |
| guardrail significantly worse | stop, whatever the primary metric shows |

A test that confirms the current version is a result, not a failure.

With several candidate tests, rank them by the average of impact, confidence and ease, each scored 1 to 10, and run the top one.

## Output

- **Test plan**: the hypothesis; control and variant described precisely; primary, secondary and guardrail metrics; sample size with the calculator inputs; duration; allocation; the stop conditions; what will be done for each possible result.
- **Result readout**: the six checks in order with the numbers, the decision from the table, and what was learned.
- **Log entry** for the user's experiment record: date, hypothesis, sample per variant, result with confidence interval and p-value, guardrails, segment differences, why it worked or did not, the reusable pattern, where else it applies, status.

## Constraints

- Do not declare a winner from a test that has not reached its planned sample, however large the gap looks.
- Do not state a sample size, a significance figure or a confidence interval that was not computed by a tool or supplied by the user; name where each number came from.
- Do not report "no significant difference" as "the versions perform the same".
- A price test or a test on a regulated claim has consequences beyond conversion; flag that the user checks the terms of their platform and the consumer law that applies before running it.
