# Code Review Examples

## Example 1: API handler review

### Input

```text
Use the Code Review Skill.

Language/framework: TypeScript / Next.js
Risk area: auth and database writes
Code or diff:
[handler code]
```

### Expected output pattern

```text
Verdict: request changes

Critical issues:
- [Critical] Missing ownership check before updating record.
  Impact: any authenticated user could update another user's data.
  Fix: filter update by both id and userId.

Suggested patch:
...

Validation checklist:
- Add test for cross-user update denial.
- Add test for valid owner update.
```

## Bad output

```text
The code looks good. Maybe improve readability and add comments.
```

Why bad:

- Does not evaluate auth or data risk.
- No concrete impact.
- No validation checklist.
