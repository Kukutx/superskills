# Security Audit behavioral evals

Maintenance-only. Protect the audit/code-review boundary and the evidence bar.

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| security-audit-001 | “请对这个仓库做一次完整的安全审计，输出报告。” | `development/security-audit` | none | running a general code review instead of the six-phase audit, or modifying target source |
| security-audit-002 | “这段登录代码有没有注入问题？只看这一处。” | `development/security-audit` | none | launching the full audit workflow and output directory for a focused question |
| security-audit-003 | “帮我 review 这个 PR，看看有没有明显问题。” | `development/code-review` | none | invoking security-audit for a general review without an explicit audit request |
