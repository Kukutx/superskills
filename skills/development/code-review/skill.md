---
name: code-review
description: Review general code, diffs or pull requests for concrete correctness, security, data, performance and integration risks. Prefer domain-specific review skills when available.
---

# Code Review

## Review order

1. Understand the intended behavior and changed surface.
2. Look first for production-impacting defects: data loss, auth/permission, broken contracts, concurrency, migrations, lifecycle, error handling.
3. Check edge cases and integration assumptions.
4. Consider performance only where the change creates a credible bottleneck.
5. Treat readability/style as non-blocking unless it obscures correctness or future changes.

## Output

Lead with a verdict: **approve / request changes / needs context**.

Then report findings ordered by severity. Each finding should include:

- concrete location or behavior;
- impact;
- why it can happen;
- smallest useful fix;
- validation when not obvious.

If there are no meaningful findings, say so. Do not create empty security/performance sections.

## Constraints

- Do not nitpick formatting or personal style by default.
- Do not claim safety for code paths that were not visible.
- Do not recommend broad rewrites when a local fix addresses the risk.
- Separate proven defects from questions or speculative concerns.
- For version-sensitive APIs/framework behavior, verify current primary documentation when needed.