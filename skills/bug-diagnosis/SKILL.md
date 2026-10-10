---
name: bug-diagnosis
description: Diagnose general software bugs from symptoms, logs, code and recent changes. Use when no more specific domain skill owns the problem.
---

# Bug Diagnosis

## Workflow

1. State the observed facts: expected behavior, actual behavior, errors and environment.
2. Rank likely causes by **fit to evidence × verification cost**.
3. Use recent changes as regression clues, not automatic proof.
4. Verify the highest-value hypothesis with the smallest reproducible check.
5. Fix the cause, not only the symptom.
6. Add a regression test or observable guard when practical.

If logs/evidence are missing, propose instrumentation or a reproduction path before deep speculation.

## Output

Default:

- **Most likely cause** + confidence
- **Why it fits**
- **Fast verification**
- **Fix**
- **Regression check**

List alternative causes only when they are plausible enough to change the debug path.

## Constraints

- Do not pretend certainty without evidence.
- Do not start with cache clearing, dependency reinstall or rewrite unless evidence points there.
- Do not ask the user to gather everything before giving a useful first diagnostic path.
- Do not ignore production/local environment differences.
- A successful parse/build is not proof that runtime behavior is fixed.