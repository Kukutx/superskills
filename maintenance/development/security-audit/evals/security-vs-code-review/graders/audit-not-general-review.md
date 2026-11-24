---
type: llm
---

The user explicitly requested a full security audit with a report artifact, so the reply must run the audit workflow rather than a general code review.

PASS if the reply frames the work as a security audit (threat-focused, with findings given severity and evidence) and names at least two of the concrete issues in the login code (SQL string concatenation with user input, MD5 password hashing, session fixation or missing session regeneration, verbose error handling) with a smallest-fix direction for each.
FAIL if the reply is a general code review (style, naming, correctness, performance) without severity-graded security findings, or if it modifies the target source, or if it claims the code is safe.
