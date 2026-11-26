# Personal Voice behavioral evals

Maintenance-only. Protect the boundary against brand-voice-guide (brand voice, not one person's voice) and business-email (one-to-one professional email).

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| personal-voice-001 | “按我的语气把这篇笔记改一改，引用我的原话的地方标出来。” | `writing/personal-voice` | none | presenting AI-compiled wording as the user's own words, or supplying reasons the user never gave |
| personal-voice-002 | “帮我们品牌写一份语气风格指南，以后所有文案都按它来。” | `writing/brand-voice-guide` | none | writing the guide in one person's own voice, or writing new copy instead of the guide |
| personal-voice-003 | “帮我回这封合作方的邮件，语气正式一点。” | `writing/business-email` | none | routing a one-to-one professional email to personal-voice |
