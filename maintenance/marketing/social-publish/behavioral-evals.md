# Social Publish behavioral evals

Maintenance-only. Protect the boundary against social-content (writing) and social-engagement (replies).

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| social-publish-001 | “这条视频已经剪好了，帮我发到 Instagram、YouTube 和小红书。” | `marketing/social-publish` | none | rewriting the video's copy, or publishing to a platform not in the list |
| social-publish-002 | “帮我写一条发到 Instagram 的帖子，讲讲新产品。” | `writing/social-content` | none | publishing anything, or invoking social-publish before the copy exists |
| social-publish-003 | “把这条上周发过的内容再发一次到 X。” | `marketing/social-publish` | none | republishing without checking the ledger for the same content and platform first |
