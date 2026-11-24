# Parallel division

When several independent failures or tasks are on the table, investigate them
in parallel — one agent per independent problem domain — instead of working
through them one by one. Sequential work wastes the time the independent work
could have run in.

Distilled from `obra/superpowers` skill `dispatching-parallel-agents` (MIT).
Only the division pattern is adopted here; the rest of that collection
overlaps existing Skills and was not imported.

## When to divide

Use when there are 2 or more independent problems: different test files failing
for different root causes, different subsystems broken independently, or tasks
that can each be understood without context from the others. Do not divide when
the failures may be related (fixing one might fix the others), when the full
system state must be understood first, or when agents would interfere through
shared state. Related failures are investigated as one problem.

## The pattern

1. **Group by what is broken.** Each group is one domain: one file's tests,
   one subsystem, one bug. A group that mixes two root causes is two groups.
2. **Give each agent a focused task.** The task names the failure, the files
   and commands it may use, the expected output (root cause plus evidence, or
   the fix plus its test), and what it must not touch. Agents never inherit
   the lead session's context; they get exactly the context their task needs.
   That also preserves the lead's context for coordination.
3. **Keep shared work with the lead.** The blocking integration, the merge of
   results, and the final verification pass stay with the lead — they are not
   delegated.
4. **Verify centrally.** Each agent's result is checked against the same
   evidence bar as a single-agent result: the reproduction, the failing test,
   the command output. An agent's report of success is not evidence.

## When not to divide

One failure, one agent. A diagnosis that is still at "what is even failing"
does not divide yet — divide after the failures are separated into domains,
not before.
