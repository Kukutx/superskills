---
type: llm
---

The Designers Italia validator recognises the model's components through `data-element="..."` attributes in the HTML. The base theme's template carried them; the rewritten template dropped them.

PASS if the reply's main diagnosis is that the validator detects service-page sections and contacts through specific HTML attributes (`data-element` attributes, named as such) that were in the base template and were lost in the rewrite, and the fix is to put those attributes back on the corresponding elements (for example by diffing against the base template or the model's documentation) and to re-run the validator. Mentioning the required order of service-page sections as a second check is fine.

FAIL if the reply does not identify the `data-element` attributes as the cause; if its main explanation is caching, missing field content, Schema.org metadata alone or a validator bug; or if the only fix is to revert to the base template without explaining what the validator reads.
