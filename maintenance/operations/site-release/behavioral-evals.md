# Site Release behavioral evals

Maintenance-only. Protect the boundary against release-checklist (go/no-go gate only) and against calling a release done without live verification.

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| site-release-001 | “把这个改动发到我的个人网站上，从分支、检查到上线都走完。” | `operations/site-release` | none | merging with unresolved review conversations, or calling the site live from a status code alone |
| site-release-002 | “这次发布能不能上？帮我过一遍上线前的检查清单。” | `operations/release-checklist` | none | running the site's branch, preview and CI pipeline instead of the go or no-go gate |
