---
name: code-review
description: Review general code, diffs or pull requests for concrete correctness, security, data, performance and integration risks. Prefer domain-specific review skills when available; use bug-diagnosis when the primary task is explaining an observed failure.
---

# Code Review

## Workflow

1. Understand the intended behavior and the code/change surface actually visible.
2. Look first for production-impacting defects: data loss, auth/permission, broken contracts, concurrency, migrations, lifecycle and error handling.
3. Check edge cases and integration assumptions that can make the visible change fail outside the happy path.
4. Consider performance only where the change creates a credible bottleneck.
5. Treat readability/style as non-blocking unless it obscures correctness or materially increases future change risk.

If the request is primarily “why is this failing?”, route to `development/bug-diagnosis` rather than turning debugging into a review checklist.

## Output

For a PR/diff, lead with **approve / request changes / needs context**.

For a stand-alone code audit, use **no material findings / changes required / needs context** instead of pretending there is a PR approval decision.

Then report findings ordered by severity. Each meaningful finding should include:

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
- Do not convert an observed runtime bug into a generic code review when a focused reproduction path is more useful.
- For version-sensitive APIs/framework behavior, verify current primary documentation when needed.
