---
name: social-publish
description: Publish content to one, several or all social platforms on the user's explicit instruction, with preflight, verification and a ledger. Use when content is ready, not for writing it.
---

# Social Publish

## Scope

Publishing is execution, not writing. The words come from `writing/social-content` (or the user); this Skill sends finished content out and proves each destination received it. A request to write the post stays with the writer; a request to reply to comments or DMs belongs to `marketing/social-engagement`.

Publish only on the user's explicit instruction in that conversation.

- Ask for the platform list on every request and treat it as the whole scope. Never default to all platforms.
- Single platform when the user names one; specified multi-platform when the user lists several; all-platform only when the user says all platforms in that message. All-platform means the public platforms only. Private and community destinations (WhatsApp, Discord, Telegram) are never included; each needs a named destination in that request (Channel, group or Status; server and channel; channel or group).
- Product promotion: list the recommended platforms first and publish only the list the user confirms in that conversation.
- When the user asks for a dry run, do login checks and copy adaptation only and publish nothing; send a dry-run receipt listing each platform, whether it would publish or skip, and the reason for every skip.
- For a timed publish, use the platform's own schedule feature where it supports it; never promise unattended publishing. Where there is none, save a draft and set a reminder for the publish time.
- For draft first, save a draft where the platform supports it and wait for confirmation before publishing.

## Brief

Collect one brief for all destinations before starting. Fields, receipt shapes and content templates are in [references/publish-brief.md](references/publish-brief.md).

- Record the content type first: video, image, text, or a mix. Skip a platform that does not support that type, with the reason in the receipt.
- Ask once for all missing required fields, not one field at a time.
- Record the publishing account per platform when the user has more than one there; otherwise use the default and say so in the receipt.
- Record the language of the copy. Do not translate copy between platforms without the user confirming it.
- Record alt text when the user supplies it, and pass it to platforms that accept it.
- Check the copy for private information the user did not mean to publish (phone, email, home address). When found, stop and ask before publishing.
- Record originality and promotion declarations exactly as given and pass them to each platform that asks.
- Keep one generic title and description, adapting only format and length per platform. Change wording for format only, never the meaning without asking.
- Keep the cover separate from the video when one is supplied; note the frame time when the cover comes from the video.
- When a video needs another aspect ratio, transcode with the vertical or horizontal preset instead of re-editing by hand. When a file is too big, compress it and re-run preflight on the compressed file.

## Preflight

Run the preflight in [references/preflight.md](references/preflight.md) before any publish, including a dry run: file checks, copy and image limits, a ledger check for the same content and platform, and login health for this run's platforms only.

- When the same content already published there, stop and ask before publishing again.
- When copy exceeds a limit, shorten it first and publish only after the user confirms the change.
- Do not publish to a platform that failed the login check; record it as skipped with the reason.
- Stop at a login wall, captcha, SMS code or human check and hand the user one concrete action. Never enter a password or verification code for the user.
- Platform limits change. Treat every limit as changeable: check the platform's page at publish time and follow what it shows. Per-platform routes, entry points, content types and approximate limits are in [references/platforms.md](references/platforms.md).

## Publish and verify

- Publish the platforms in the order the user gave, one by one. Wait for upload and processing to finish on a platform before moving to the next.
- Record the link or status right after each one, and append one ledger line. The ledger is the index; also archive each published file named by date, content hash and original filename, so a post can always be traced to its source file.
- A submitted-for-review state counts as submitted, never as published.
- Never retry a publish automatically. Check first whether a failed attempt already created a draft or a published post.
- Publish the same content to the same platform only once per request.
- When a run stops in the middle, follow [references/preflight.md](references/preflight.md): skip platforms already published or submitted, continue with the rest in the original order.
- Read the post back after publishing when possible and keep the returned link.
- When a platform fails, follow [references/troubleshooting.md](references/troubleshooting.md) and record the failure with one of the six failure categories. Finish the other platforms first, then return to the failed one.

## Report and maintain

- Send one receipt after all platforms in the list are done, using only the four states published, submitted for review, failed, skipped. Name every failed or skipped platform with its reason and the exact user action it needs. Never list a platform that was not in the current list.
- A single-platform run takes about 5 to 10 minutes including preflight; a 9-platform run about 45 to 90. Do not promise a faster time.
- Add a new platform only through [references/troubleshooting.md](references/troubleshooting.md): confirm login, record the entry point, note its content types and limits, test with one single-platform publish or draft before using it in a multi-platform run.
- Keep account names and login states in the user's own notes, not in this Skill. When a platform changes its entry or limits, update the platform reference first and test with a single-platform publish.
- No paid APIs and no third-party publishing service are used. Publish through connected accounts where one exists, through the user's logged-in browser otherwise; never use a browser that does not share the user's logins.
