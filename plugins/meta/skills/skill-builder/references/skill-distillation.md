# Skill Distillation

How to grow a new Skill out of real work sessions, adapted and rewritten from `tigerless-labs/autoharness` skills/learn (MIT). Method only: the source's `stage_skill` toolchain and its deterministic promoter are not ported.

Use this reference when a session produced something worth keeping, not after every session. Most sessions produce nothing worth keeping, and that is the correct outcome.

## The bar

A lesson is kept only when it is class-level and reusable: a corrected approach, a non-trivial technique, or a durable user preference. One-off narratives and environment-specific failures are skipped. If nothing meets the bar, stage nothing and say so.

## The four steps

1. **Take class-level lessons only.** Ask of each candidate: would this change the behaviour of a future session on a different task? If it only explains what happened this once, drop it.
2. **Compare before creating.** Read the existing skill index first. If an existing Skill covers the topic, prefer a patch or an update to that Skill over creating a near-duplicate. A new Skill is the last resort, not the default.
3. **Reconcile old with new, repo-wide.** When a lesson supersedes an earlier rule, search the managed skill trees for contradicting statements and update them all so the new version wins everywhere. A new rule that contradicts an old one left standing is worse than no rule.
4. **Attach verbatim evidence.** Every lesson carries a verbatim quote from the session it came from: what was tried, what happened, and why the lesson follows. A lesson with no evidence is an opinion; do not keep it.

## How a lesson is staged

Each lesson is staged as one intent: the change it proposes, the reason, and the verbatim evidence quote. One intent per lesson, so a rejection of one does not block the others. The landing is validated before it lands: a staged change that contradicts an existing rule, duplicates an owner, or lacks evidence is rejected, and the rejection is reported rather than silently dropped.

## Worked example

A session fixes a routing mistake: the model sent a pricing question to the billing skill when the question was really about price tiers. The class-level lesson is not "this session routed wrong" but "pricing questions (what a tier costs, when a paywall appears) belong to the pricing owner, while billing questions (an invoice, a charge, a refund) belong to the billing owner". Evidence, verbatim: the user's question, the wrong route taken, and the correction.

Staging that lesson means: first check whether the pricing and billing skills already state the boundary. If the pricing skill already says it, the lesson is a patch to the billing skill's exclusion line, not a new skill. If both state it and the model still routed wrong, the lesson is a wording fix or an eval case, not a new rule. If neither states it, the lesson is added once, to the skill that owns the decision, with the verbatim evidence attached, and the neighbouring skill gets the symmetric exclusion.

## Distilling a whole session

At the end of a long session, run the four steps once over the whole transcript:

1. List every candidate lesson, then strike the one-off narratives and environment-specific failures.
2. For each survivor, name the existing owner it belongs to, or justify a new one.
3. Search for contradictions repo-wide for each lesson that supersedes an earlier rule.
4. Attach the verbatim evidence quote to each surviving lesson.

If the list is empty after step one, say so and stage nothing. An empty result is a successful distillation, not a failure to find lessons. The most common outcome of a good session is zero new lessons: the work went well because the existing skills already covered it.

## What good looks like

A distilled lesson is short enough to state in one sentence, specific enough to change a decision, and evidenced enough to survive a challenge. "Prefer the pricing owner for tier questions" passes all three. "Be careful with routing" passes none of them: it states no decision, names no owner, and carries no evidence.

Keep the distilled set small. A skill library that grows by one lesson per session is a library nobody reads; a library that grows by one lesson per ten sessions is a library that earns its keep.

## What this is not

- Not a session summary. A summary retells what happened; distillation keeps only what changes future behaviour.
- Not a changelog. Git history already records what changed.
- Not a place for tooling. The source repository's staging tool and promoter are its own harness; this Skill's landing path is a normal repository change, reviewed like any other.

## Source

Adapted and rewritten from `tigerless-labs/autoharness` skills/learn/SKILL.md, https://github.com/tigerless-labs/autoharness (MIT). Only the four-step method is taken; the source's toolchain is not ported.
