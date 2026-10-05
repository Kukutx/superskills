---
name: release-checklist
description: Build a go/no-go release gate with blocking checks, a targeted smoke path, rollback and post-release monitoring. Use for a release that has no project or domain release workflow.
---

# Release Checklist

## Workflow

1. Define the release surface and highest-risk changes.
2. Separate **blocking go/no-go checks** from useful but non-blocking polish.
3. Verify the exact artifact/config/data migration being released, not only source code.
4. Define rollback or mitigation before launch when reversal is possible.
5. Specify the first post-release signals that would reveal failure.

## Output

Default:

- **Release scope / risk**
- **Blocking pre-release checks**
- **Targeted QA / smoke path**
- **Data/privacy/payment checks** when relevant
- **Rollback / mitigation**
- **Post-release monitoring**
- **Go / no-go conditions**

## Constraints

- Do not create a giant generic checklist unrelated to the actual release.
- Do not require ceremony that adds no risk reduction.
- Do not skip backup/migration/rollback concerns for data-changing releases.
- Domain-specific release logic (for example Godot export/CI or Shopify) belongs to that domain Skill first.
- A successful CI job is not automatically proof that the released artifact works in production.