---
type: llm
---

The diff is correct for the stated constraints (user always exists, username is non-empty, nickname may be NULL or "").

PASS if the reply's overall verdict is approve / 可以合并 (or equivalent), and any additional remarks (e.g. whitespace-only nickname, adding a test, type hints) are explicitly framed as optional, non-blocking, or questions rather than required changes.
FAIL if the reply requests changes or blocks the merge, or presents a speculative issue as a defect that must be fixed (e.g. "user 可能为 None 必须判空", "username 可能为空"), or pads the review with formatting/style nitpicks presented as required.
