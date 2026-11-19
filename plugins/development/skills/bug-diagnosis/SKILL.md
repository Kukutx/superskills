---
name: bug-diagnosis
description: Diagnose a software bug, error, crash or failing behavior from symptoms, logs, code and recent changes, even when evidence is thin. Not for reviewing code that has no observed failure.
---

# Bug Diagnosis

## First: a check that goes red on this bug

When the evidence already at hand answers the question, answer it; a reproduction is for bugs whose cause is not yet established.

For those, a diagnosis is only as good as the check it is tested against. Before building a theory from reading code, get one command or procedure that reproduces the user's exact symptom and would pass once the bug is fixed. Prefer, in this order:

1. a failing test at the seam that reaches the bug;
2. a request or CLI script with a fixture input, compared against a known-good result;
3. a replay of a captured request, payload, event log or trace;
4. a minimal harness around the failing code path;
5. a bisection or old-versus-new differential run when the bug appeared between two known states.

The check exists only once it has been run at least once and its output, with secrets replaced, has been shown. Make the check tight: seconds rather than minutes, asserting the specific symptom rather than "did not crash", and deterministic (pin time, seed and data). For an intermittent bug, raise the reproduction rate by looping, adding load or narrowing the timing window until it fails often enough to test against.

When no such check can be built, say so, list what was tried and name what would make one possible: access to the environment where it reproduces, a captured artifact such as logs or a HAR file, or permission to add temporary instrumentation. Still give the most useful first diagnostic path with what is available.

## Workflow

1. State the observed facts: expected behavior, actual behavior, exact error and environment. Confirm the reproduction shows the user's symptom and not a neighbouring failure.
2. Minimise the reproduction: remove inputs, callers, configuration and steps one at a time while it stays red, until every remaining element is needed for the failure.
3. List three to five ranked hypotheses by **fit to evidence × verification cost** before testing any, each with the prediction that would falsify it: "if X is the cause, changing Y makes it disappear". A hypothesis without a prediction is a guess. Recent changes are regression clues, not proof.
4. Test one variable at a time, each probe tied to one prediction. Prefer a debugger or targeted logs at the boundary that separates the hypotheses. Tag temporary logs with one unique prefix so they can all be found and removed in a single search. For a performance regression, measure a baseline first and bisect from it.
5. Fix the cause, not only the symptom. Turn the minimised reproduction into a regression test at a seam that exercises the real failing path: see it fail, apply the fix, see it pass. When no seam can reach the real failure, report that as a finding instead of adding a shallow test that gives false confidence.
6. Finish: rerun the original reproduction, remove the tagged instrumentation and throwaway harnesses, and state the cause that was confirmed, in the commit or PR description when there is one, so the next person to debug this area learns it.

## Output

Default:

- **Most likely cause** + confidence
- **Why it fits**
- **Fast verification**
- **Fix**
- **Regression check**

List alternative causes only when they are plausible enough to change the debug path.

## Constraints

- State confidence that matches the evidence; a cause is confirmed only when its prediction was tested.
- Start from the evidence. Cache clearing, dependency reinstalls and rewrites come in only when evidence points there.
- Explain the failing point itself first: the first faulting frame or the first real error. Something nearby that looks related is context, not evidence of cause.
- Give a useful first diagnostic path before asking the user to gather more.
- When the same fix fails a third time, stop repeating it. Write down only what has been verified and one hypothesis that has not been tested yet, and make the next step a different one. Discard the theory, not a diff that was correct on its own.
- Account for differences between production and local environments.
- When the same error appears for every valid input, suspect an account, environment or configuration gate before changing the payload. "Not found" and "not allowed" can be the same response, so confirm the identity and scope in use first.
- A successful parse or build is not proof that runtime behavior is fixed. A check proves only its own layer: one piece valid, the combination valid, or the behavior in effect at runtime. Say which layer each check covered.
- Replace secrets with a placeholder in every command, log and captured artifact that is shown, and ask for redacted versions when requesting logs, HAR files or dumps.
