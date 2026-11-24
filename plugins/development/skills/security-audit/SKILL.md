---
name: security-audit
description: Audit a codebase for security vulnerabilities, with verified findings, severity and smallest fixes. Use when an explicit security audit or pen test is requested, not for general code review.
---

# Security Audit

Find vulnerabilities that violate a real trust boundary, then give the owner the
source evidence, a safe reproduction, a priority and the smallest effective fix.
A candidate without a concrete affected principal, resource or security outcome
is not a confirmed finding. This Skill describes findings; it never modifies
target source.

Adapted from `cloudflare/security-audit-skill` (MIT); see `maintenance` `sources.md`
for attribution and what was left out.

## Use

Use when the user explicitly asks to audit or pen-test a codebase, asks for a full,
comprehensive or end-to-end security review, or requests a report artifact.

Not this Skill:

- a security question, a focused review of one finding, or triage of a known issue
  -> answer from the relevant section below without running the full workflow;
- a general review of a diff for correctness, style or performance
  -> `development/code-review`;
- an observed failure with an unknown cause -> `development/bug-diagnosis`;
- legal privacy compliance (DPA, data-subject requests) -> `legal/privacy-compliance-check`.

If the request could mean a quick question or a full audit, ask one focused question
before creating files or starting the workflow.

## Modes

**Guidance mode** (default): answer the question or review the named finding using
only the relevant sections below. Do not run all six phases, create an output
directory, or write audit artifacts.

**Full audit mode**: only for an explicit audit request. Run all six phases in order
and write the artifacts listed under Workflow. A scoped run (named paths, one
subsystem, or a diff between two refs) seeds coverage only for what is in scope and
records everything else as `out_of_scope`, never as `covered`.

## Safety boundaries

- Source inspection is read-only. Never probe deployed endpoints, external services,
  shared infrastructure, production identities, other users' data, or live control
  planes. Never publish artifacts, alter releases, or spend paid API quota.
- Any target-controlled execution (builds, tests, fuzzers, fixture processing) runs
  only inside a sandbox with no external network, an empty allowlisted environment,
  a read-only target, writes confined to one scratch directory, and explicit CPU,
  memory, process, file-size, disk and wall-clock limits. If any control cannot be
  enforced, do not execute target code: report the missing control as a blocker and
  give a safe validation plan.
- Use dummy principals, fixtures and secrets. Do not retain target-controlled files
  in guidance mode. In full audit mode, only the coordinating agent promotes the
  minimum non-secret result from scratch to the retained artifacts directory, after
  validating path, file type, link count and size; never promote a symlink, archive,
  FIFO, socket, device or oversized file.
- A decisive fact that lives outside source or the sandboxed fixture is reported as
  `needs_validation` with the exact missing fact and a safe owner-observed or local
  plan, never guessed.

## The evidence bar

For every candidate, name the lower-trust principal, the accepted input or action,
the intended control, the crossed boundary, the affected principal or resource, and
the concrete observed (or owner-observable) result. Do not elevate a missing best
practice, a guessed deployment behavior, a generic parser crash, or self-impact
into a security finding. Deployment controls, proxy behavior, provider settings,
browser headers, identity policy and topology are real controls: if they are
required and absent from the repository, assume neither presence nor absence.

Static analysis establishes the source path. Sandboxed local tests resolve behavior:
a minimal function harness, an existing unit test, a small parser fixture, a
dummy-tenant integration test, or a locally rendered configuration. Stop at the
minimum boundary result (a wrong return value, an unauthorized dummy record, a
sanitizer finding, a policy difference). Do not extend the check into persistence,
post-fault or concealment material.

## Severity

Only `confirmed` records receive severity. Likelihood and impact must reflect the
demonstrated conditions; overall severity cannot exceed demonstrated impact.
`needs_validation` has no severity: it is a blocked hypothesis, not a
low-confidence vulnerability.

- **critical**: an unauthenticated actor gains code execution, full data-store
  access, or takeover of arbitrary accounts.
- **high**: an actor fully defeats an explicit security control with real
  consequences: authentication bypass, cross-tenant read or write, stored script
  execution affecting other users, authenticated code execution, or an
  unauthenticated remote stop of a shared service.
- **medium**: a real boundary violation with limited blast radius, uncommon
  preconditions, or consequences confined to a narrow resource set.
- **low**: disclosure of non-secret internals, or an effect requiring sustained
  effort for minimal gain.
- **informational**: a confirmed but minimal-impact observation, useful mainly as
  a prerequisite inside a larger finding.

The high/medium discriminator: does the demonstrated result fully defeat an
explicit control for an action with real consequences, or only weaken it? If the
concrete damage cannot be stated, the severity is lower than it feels.

## Workflow (full audit mode)

1. **Reconnaissance**: map the source, trust boundaries, local build paths, prior
   runs, and a deterministic coverage ledger of surfaces x boundaries x attack
   classes. Read every prior run's ledger and findings first; a prior `confirmed`
   record carries over only when its source and conditions are unchanged and its
   evidence still meets the bar, and it still goes through fresh verification.
2. **Coverage-led hunting**: assign isolated hunters from the ledger, one per
   coverage unit, and collect structured candidate results. Re-plan coverage after
   every wave; a critic pass after each wave accepts discoveries and reassigns
   gaps as `deferred`.
3. **Candidate validation**: consolidate fingerprints and give every candidate to
   a fresh verifier that did not hunt it.
4. **Structured output**: write final `confirmed`, `needs_validation` and
   `rejected` records to `findings.json` and validate the file against its schema.
5. **Independent record verification**: fresh agents verify the final source claims
   and reconcile corrections or state changes.
6. **Report**: derive `REPORT.md`, `FINDINGS-DETAIL.md` and `NEEDS-VALIDATION.md`
   from the final records, with no live-probe instructions.

Profiles change breadth and redundancy, never the evidence bar: `quick` (one hunter
wave, one critic pass, one verifier per candidate), `standard` (the workflow as
written), `deep` (units split per subsystem, critic waves to a clean pass, separate
candidate and record verifiers). When the user sets a budget in agent invocations,
reserve the reconnaissance calls, the critic calls and at least one verifier call
before assigning any hunter; if the budget cannot fund that minimum, launch nothing
and report the run incomplete with its exact reason.

End only in one of two terminal states: all Phase 6 artifacts written and both
validators passing, or `run_status: "incomplete"` recorded with its exact reason
and the gap disclosed in the report. Never stop mid-phase, and never imply that
one run exhausts the target.

## Attack classes

The classes to cover are in [references/attack-classes.md](references/attack-classes.md). Load it when planning coverage in full audit mode; guidance mode only needs the classes relevant to the question at hand.

## Output

For each confirmed finding: severity, the boundary and result in one paragraph,
the source path (file and line), the minimal safe reproduction, the invariant the
code must enforce, and the smallest source change that enforces it at the last
trusted decision point, plus a regression test. For `needs_validation`: the
hypothesis, the exact missing fact, and the safe validation plan. The report opens
with the profile, scope, source ref, coverage statement (what was covered, what
was explicitly out of scope, what is deferred) and the count of confirmed findings
by severity.

## Constraints

- Do not present checklist deviations as vulnerabilities, or defense-in-depth
  advice with no reachable boundary violation.
- Do not assign severity to `needs_validation` records.
- Do not write the report before independent verification, and do not let prose
  and `findings.json` disagree.
- Do not re-report a carried same-source prior confirmed record as a new finding.
- Do not claim safety for code paths that were not covered.
