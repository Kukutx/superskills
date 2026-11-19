---
type: llm
---

PASS if all of these hold: the leading hypothesis is tied to the given evidence (for example API_BASE_URL / .env.local not present in the production container, or the production API response lacking `items`); the reply gives a concrete, cheap verification step before or alongside the fix (e.g. log `process.env.API_BASE_URL`, `res.status`, or the raw response body on the server); and it expresses the cause with appropriate uncertainty (a confidence level, "最可能", or conditional wording) rather than as proven fact.
FAIL if the first recommended action is clearing caches, deleting `.next`/`node_modules`, reinstalling dependencies, or rolling back Next.js without an evidence-based reason; or if the reply blames the Next 13 -> 14 upgrade as the cause without evidence; or if it states one cause as certain and gives no way to verify it.
