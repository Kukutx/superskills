# Skill evaluation

How to tell whether a Skill is good, and how to improve one with evidence
instead of taste. The Skill Builder entrypoint owns creating and restructuring
Skills; this file owns measuring them.

Method distilled from `alibaba/skill-up` (Apache-2.0). The upstream ships an
evaluation CLI; this repo keeps only the method — no tool is bundled, and the
existing behavioral-eval tables plus live replay are the evaluation harness.

## What to measure

| Dimension | What good looks like |
| --- | --- |
| Routing | the Skill fires for its own tasks and stays quiet for its neighbours; near-miss prompts route elsewhere |
| Boundary | the Skill refuses or escalates at its real blockers and does not invent a gate where none exists |
| Output shape | the deliverable matches the shape the Skill promises, with nothing missing and no padded sections |
| Evidence | every consequential claim names what was checked; nothing is asserted from memory as if verified |
| Cost | the Skill loads only what the task needs; references stay unloaded until their boundary is reached |

## Evidence-based iteration

1. **Collect observations first.** Real runs, real prompts, real failures —
   not imagined ones. Each observation records the prompt, what the Skill did,
   and what should have happened instead.
2. **Turn one observation into one regression case.** Add it to the Skill's
   behavioral-evals table (route/ownership/autonomy) or, when the rule exists
   because a plain model gets the behavior wrong, as an authored case under
   the Skill's maintenance evals directory. One case per failure; a case that
   passes with and without the Skill proves nothing.
3. **Change one thing.** One description edit, one rule, one reference split —
   never several at once, or the result cannot be attributed.
4. **Re-run the affected cases only.** Full-suite replay is a billed model
   session per case; replay what the change touches, and record model, host
   and result per case.
5. **Keep tuning cases and acceptance cases separate.** The cases used to
   decide the change and the cases used to judge it must not be the same set:
   a change that only improves the cases it was tuned against has not been
   shown to help.

## Scoring a change

- **Better**: acceptance cases improve and nothing regresses.
- **Flat**: no acceptance case changes. Flat is not better; do not accept a
  change on flat results.
- **Worse**: any acceptance case regresses. Revert first, diagnose second.
- **Noisy**: the same case flips between runs. Measure the noise floor
  (repeat one case, count flips) before claiming an improvement smaller than it.

A recorded failure is never erased by a later passing re-run; both runs stay
in the record.

## When not to iterate

Do not evaluate a Skill into existence for a one-off task, and do not add eval
cases for keywords the Skill already routes correctly. The Growth rule in the
README decides whether the Skill deserves to exist at all; evaluation decides
whether it works.
