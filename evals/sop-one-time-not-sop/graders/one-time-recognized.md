---
type: llm
---

The user describes a migration that happens once and will not be repeated.

PASS if the reply explicitly recognizes that this is one-time work (for example says a reusable SOP is not really warranted, or that it will give a one-off migration plan/checklist instead), and then gives a concise, ordered migration checklist or plan. It may still reuse an SOP-like structure (steps, checks, done criteria) as long as it acknowledges the one-time nature.
FAIL if the reply produces a reusable SOP document (trigger, roles, recurring execution, versioning or review cadence, "每次迁移时" style wording) without any acknowledgment that the work is one-time.
