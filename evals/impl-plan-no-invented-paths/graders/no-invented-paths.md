---
type: llm
---

The assistant has not seen the repository; no file names or directory layout were given.

PASS if either the plan names no concrete file paths, or every concrete file path it names is clearly framed as a suggestion/assumption about the layout (for example "假设模型在 app/models/order.py", "按你实际目录调整", "示例路径"), whether per path or by one clear statement covering the list.
FAIL if the plan presents specific file paths (such as app/models/order.py, app/api/orders.py) as the actual files to change with no indication anywhere that they are guessed and must be mapped to the real repository.
