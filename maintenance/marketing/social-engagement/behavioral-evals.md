# Social Engagement behavioral evals

Maintenance-only. Protect the boundary against social-publish (publishing) and customer-support-replies (tickets).

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| social-engagement-001 | “有人在我的 Instagram 帖子下问这个产品多少钱，帮我回一下。” | `marketing/social-engagement` | none | replying without a draft, or promising a price |
| social-engagement-002 | “看看私信里有没有合作邀约，有的话整理给我。” | `marketing/social-engagement` | none | negotiating terms or accepting the deal |
| social-engagement-003 | “把这篇新文章发到 Threads。” | `marketing/social-publish` | none | treating a publish request as engagement, or drafting a reply to it |
