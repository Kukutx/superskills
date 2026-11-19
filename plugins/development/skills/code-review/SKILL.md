---
name: code-review
description: Review code, a diff or a pull request for concrete correctness, security, data, performance and integration risks. Not for explaining an observed failure, which is bug diagnosis.
---

# Code Review

## Workflow

1. Pin what is under review: the diff against a stated base (merge-base, commit or branch), or the named files. Say whether uncommitted changes are included, so nothing falls outside the review unnoticed. Confirm the base resolves and the diff is not empty before reviewing.
2. Find what the change was meant to do. Look, in order, at issue references in the commit messages, a path the user gave, a spec or plan in the repository that matches the branch or feature, then ask. Review on two separate axes, because a change can pass one and fail the other:
   - **Intent**: requirements that are missing or partial, behavior that was not asked for, and requirements that look implemented but are wrong. Quote the requirement each finding refers to. When no statement of intent exists, say so instead of inferring one.
   - **Code**: production-impacting defects first: data loss, auth/permission, broken contracts, concurrency, migrations, lifecycle and error handling.
3. Check edge cases and integration assumptions that can make the visible change fail outside the happy path.
4. Consider performance only where the change creates a credible bottleneck.
5. Judge conventions against the repository's own documented standards; they override general preference. Leave to tooling whatever a linter, formatter or type checker already enforces.
6. Treat readability and design smells as labelled judgement calls, non-blocking unless they obscure correctness or materially raise the risk of future change. When the review reaches design quality and the repository documents no standard for it, use `references/smells.md` as the baseline.
7. Check a claim in the PR description by running the relevant check or test, when that is possible, before accepting it.

If the request is primarily “why is this failing?”, route to `development/bug-diagnosis` rather than turning debugging into a review checklist.

## Output

For a PR/diff, lead with **approve / request changes / needs context**.

For a stand-alone code audit, use **no material findings / changes required / needs context** instead of pretending there is a PR approval decision.

Then report findings ordered by severity, keeping intent findings and code findings in separate groups so neither masks the other. Each meaningful finding should include:

- concrete location or behavior;
- impact;
- why it can happen;
- smallest useful fix;
- validation when not obvious.

If there are no meaningful findings, say so. Do not manufacture style/security/performance findings to fill sections.

## Constraints

- Do not nitpick formatting or personal style by default.
- Do not claim safety for code paths that were not visible.
- Do not recommend broad rewrites when a local fix addresses the risk.
- Separate proven defects from questions or speculative concerns.
- Any count in the summary equals the number of findings listed; keep the number of findings apart from the number of places affected. When the change is clean, say so instead of padding the list.
- Before reporting a finding, answer four questions: what input or situation triggers it, which changed line causes it, what chain of evidence leads there, and whether the existing tests or CI already contradict it. Drop the finding when any answer is missing.
- Give every finding a reference that can be checked: file and line, or the quoted requirement. Reopen the source for the findings that matter before reporting them.
- Code written earlier in the same session deserves a review from a fresh context; when that is not possible, say the review was not independent. An independent reviewer gets the change and the standard to judge it by, not the author's explanation or other reviewers' conclusions.
- After fixes, re-check the fixed findings only; do not loop a broad review until it comes back clean.
- Do not convert an observed runtime bug into a generic code review when a focused reproduction path is more useful.
- For version-sensitive APIs/framework behavior, verify current primary documentation when needed.
