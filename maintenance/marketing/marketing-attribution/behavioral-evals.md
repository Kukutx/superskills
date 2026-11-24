# Marketing Attribution behavioral evals

Maintenance-only. Protect the boundary against paid-ads (reconciliation only) and ab-testing (experiments on pages, not channels).

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| marketing-attribution-001 | “Google 说 50 单，Meta 说 40 单，GA 说 60 单，CRM 说 35 单，到底哪个渠道真正带来了收入？” | `marketing/marketing-attribution` | none | summing platform-reported conversions, or handing the question to paid-ads as a spend review |
| marketing-attribution-002 | “播客和私域带来的客户在数据里完全看不到，怎么评估这部分的效果？” | `marketing/marketing-attribution` | none | claiming the channel is failing because tracking cannot see it |
| marketing-attribution-003 | “这批广告花得值不值，要不要暂停这个系列？” | `marketing/paid-ads` | none | invoking marketing-attribution for a campaign pause decision |
