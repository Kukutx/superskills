# Verification before completion

Evidence before claims, always. If the verification command has not been run
in this session, the claim cannot be made — not from a previous run, not from
"should pass", not from a clean linter, not from an agent's report of success.

Distilled from `obra/superpowers` skill `verification-before-completion`
(MIT). Only the completion gate is adopted here; the rest of that collection
overlaps existing Skills and was not imported.

## The gate

Before claiming any status or expressing satisfaction:

1. **Identify**: what command proves this claim?
2. **Run**: execute the full command, fresh and complete.
3. **Read**: the full output — exit code, failure count, not the summary line.
4. **Verify**: does the output confirm the claim? If no, state the actual
   status with evidence. If yes, state the claim with the evidence.
5. **Only then**: make the claim.

Skipping any step is not verifying.

## What proves what

| Claim | Requires | Not sufficient |
| --- | --- | --- |
| Tests pass | test command output: 0 failures | previous run, "should pass" |
| Linter clean | linter output: 0 errors | partial check, extrapolation |
| Build succeeds | build command: exit 0 | linter passing, logs look good |
| Bug fixed | the original symptom reproduces as fixed | code changed, assumed fixed |
| Regression test works | the red-green cycle was observed | the test passes once |
| Requirements met | line-by-line checklist against the requirement | tests passing |

## Red flags — stop

- Using "should", "probably", "seems to" in a completion claim.
- Expressing satisfaction before verification ("Done!", "Perfect!").
- About to commit, push or open a PR without verification.
- Trusting a subagent's success report instead of the diff and the command
  output.
- Relying on partial verification, or thinking "just this once".

A review finding is reported the same way: the finding stands only with its
evidence (file and line, or the quoted requirement) attached. A finding whose
evidence was not re-opened before reporting is dropped, not softened.
