---
name: social-engagement
description: Reply to fan comments and DMs and triage the inbox across social accounts, draft-first, never auto-reply, auto-follow or auto-unfollow. Use for fan replies and DM checks, not publishing.
---

# Social Engagement

## Scope

This Skill handles what comes back after publishing: replies to fan comments, DMs, follower and mention management, and a daily engagement summary. Publishing new content belongs to `marketing/social-publish`; writing the content belongs to `writing/social-content`.

## Routes

| Platform | Read | Write | Route |
| --- | --- | --- | --- |
| Instagram | comments, likers, post data | reply to comments, hide comments | connected account |
| Instagram DMs | inbox, pending requests, spam | send DMs, accept or decline requests, react | connected account (separate connection) |
| Threads | post replies, pending replies | reply, hide, approve or ignore pending | connected account |
| Threads DMs | conversations, pending requests | send DMs, accept, hide or delete requests | connected account (separate connection) |
| Facebook | posts, comments, reactions, Page | reply, react, Page comment management, group moderation | connected account |
| Messenger | conversations, messages, call history | send, react, edit, unsend own messages | connected account |
| X / YouTube / TikTok / Bilibili / Xiaohongshu / LinkedIn | comments, DMs, mentions | reply, DM | user's logged-in browser, no connector |

- Each connection is independent: when one is not connected, report only that one, not the whole platform.
- A failed command points at its connector's docs first, for the connection and rate-limit rules; when the account changed or authentication errors, re-check the account before reusing a stored ID.
- No connector exists for the browser-route platforms; use the user's logged-in browser, never a browser that does not share the user's logins. Stop at a login wall, captcha or SMS check and hand the user one concrete action; never enter a password or verification code.

## Workflow

1. Collect: read comments and DMs, then triage by [references/inbox-triage.md](references/inbox-triage.md).
2. Filter: spam and advertising first — never reply to it.
3. Draft: write reply drafts by [references/reply-policy.md](references/reply-policy.md).
4. Confirm: show drafts to the user and send only after confirmation in the current conversation. A batch goes one by one, or all at once only when the user explicitly says so in that conversation.
5. Send: one at a time, and check the returned result (a reply or message ID, or a success status) before calling it sent.
6. Record: one line per interaction — platform, other party, summary of the original, summary of the reply, status, link. Never bulk-export, save, archive or mirror DM history, especially disappearing or view-once messages.

## Hard rules

- Outbound replies are draft-first, sent only after the user confirms in the current conversation. Never auto-reply, auto-follow or auto-unfollow.
- Complaints, refunds, compensation and legal questions go to the user for a response line first; never argue, apologise on the user's behalf or promise anything.
- Commercial and recruitment messages are summarised for the user; never negotiate price, accept work or agree to an interview.
- Reply in the other party's language; do not translate meaning on your own. Do not invent facts, numbers, dates or links — leave a placeholder for the user to fill.
- Do not publish the user's phone, email, address, itinerary, income or contract details, or another fan's private information.
- No profiling: do not infer race, sexual orientation, political views, finances, mental health or relationship status from interactions, and do not rank fans by tone.
- On a 429 or a daily limit, stop immediately and do not retry; report what is left for tomorrow. When a send result is uncertain, read back first instead of sending again.
- Auto-reply, if the user ever wants it, is only a rule the user named in advance (named conversation, check frequency, fixed reply text); anything involving a meeting, pickup, price or payment is never auto-replied and goes to the user.

## Capabilities and limits per platform

- Instagram: reply to and hide comments on the user's own posts; read likers and post insights. Cannot follow, unfollow, remove followers, block, like, post top-level comments, delete or archive posts, pin posts, or read other people's follow lists — say so plainly when asked.
- Instagram DMs: read the inbox, pending and spam folders; read one conversation; accept or decline requests only when the user explicitly asks; send text and files within the size limits; react only with an emoji the user confirmed. Do not poll the same inbox frequently.
- Threads: reply to posts (about 500 characters), hide replies on the user's own posts, approve or ignore pending replies one at a time. Rate limits are strict: a 429 ends the run for that action until the next day.
- Threads DMs: text and shares of published Threads posts only, no file upload; confirm the recipient from inbox evidence, never guess from a handle.
- Facebook: reply to comments, add reactions, manage Page comments (reply, hide, delete) on Pages the user manages, moderate groups the user administers. Cannot edit posts or comments, delete personal posts or comments (Page comments excepted), or bulk-scrape friends or posts.
- Messenger: sync before reading (recent 30 days); show the user a preview (recipient plus the quoted original) and wait for explicit confirmation before sending, one at a time.
- Browser-route platforms: read, draft, confirm, then send, in that order, same as everywhere else.

## Daily summary

Only when the user asks for one. One section per platform, listing only what needs the user, plus one-line suggested replies; spam reported as a count only, without content. Summaries never paste full DM text.

```
Engagement summary (YYYY-MM-DD, user's timezone)
Instagram: new comments X (Y to reply), new DMs X (Y to reply)
Threads: new replies X, pending review X
Facebook: new comments X, groups pending X items
Messenger: unread conversations X
X / YouTube / TikTok / Bilibili / Xiaohongshu / LinkedIn: new interactions X (browser route, login as checked)

Needs you:
- <platform> <person>: <one-line original> → suggested reply: <one-line draft>
Spam filtered: X (content not listed)
```
