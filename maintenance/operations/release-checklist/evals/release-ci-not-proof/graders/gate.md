---
type: llm
---

PASS if both hold: the reply explicitly pushes back on "CI 都过了应该没问题", saying green CI does not by itself prove the release works (and calling for something like a staging/production-data migration rehearsal, smoke test of the deployed artifact, or verification against real data); AND it includes a database backup or a concrete rollback/mitigation step for the users-table migration and backfill.
FAIL if the reply agrees CI passing is sufficient or never questions it, or if it has no backup/rollback/mitigation for the data migration.
