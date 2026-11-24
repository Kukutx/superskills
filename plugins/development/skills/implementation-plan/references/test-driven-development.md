# Test-driven development

Write the test first. Watch it fail. Write the minimal code to pass. Then
refactor. A feature or bugfix implemented without a failing test first has not
been shown to be tested at all.

Distilled from `obra/superpowers` skill `test-driven-development` (MIT). Only
the TDD workflow is adopted here; the rest of that collection overlaps existing
Skills and was not imported.

## The rule

No production code without a failing test first. Code written before the test
is deleted and written again from the test — not kept as reference, not adapted
while writing tests.

Exceptions, agreed with the user first: throwaway prototypes, generated code,
configuration files.

## Red-green-refactor

1. **Red**: write one test for the next behavior. Run it and watch it fail
   for the right reason: the behavior is missing, not because the test is
   broken. If it fails for the wrong reason, fix the test.
2. **Green**: write the smallest code that makes the test pass. Nothing more.
3. **Refactor**: clean up the code just written, with the test guarding the
   behavior. Re-run after every refactor step.

One behavior per cycle. A test that covers five behaviors at once cannot say
which one broke.

## Bugfixes

A bugfix starts with a test that reproduces the bug and fails. The fix is done
when that test passes and the existing suite still passes. A fix whose
reproduction test was never seen failing is an unproven fix: the test may pass
for a reason unrelated to the fix.

## What counts as a test

A test asserts observable behavior with a deterministic outcome: given this
input, this output or state change. A test that only asserts the code runs, or
that mirrors the implementation line by line, does not count. For a plan, each
task's test is named in the plan itself (see the Implementation Plan
entrypoint); a task without a named test is a task without a completion check.
