# Security Audit sources

Maintenance-only.

## Upstream inspiration

- [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) (Cloudflare), snapshot reviewed 2026-11-24, MIT.
  - Adapted and condensed: guidance vs full-audit modes, the evidence bar (boundary + result), severity anchors, the six-phase workflow, sandbox and write-isolation rules, run profiles and budget gate.
  - Not included: the 13 companion domain files, the JSON report schema, the coverage-ledger and findings validator scripts, and the agent-delegation prompt blocks. Reasons: companion files are per-domain depth for a full audit run, and the scripts are harness tooling, not Skill rules.

Upstream license (applies to the adapted portions): MIT; see the upstream repository for the full license text.
