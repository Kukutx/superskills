---
type: llm
---

The user asks for one prompt that generates all 5 actions x 4 directions in a single image.

PASS if the reply does not offer a single all-actions/all-directions generation as the recommended production path, and instead plans generation per action and direction (one strip at a time from a fixed reference/seed), with a step to normalize scale/anchor or preview before importing. It may still show a combined prompt as a concept/reference, as long as it is clearly not the production sheet.
FAIL if the main deliverable is one prompt meant to produce the whole 5x4 sheet in one generation for direct import, even if it adds a warning that results may vary.
