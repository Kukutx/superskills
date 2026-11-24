# Publish Brief

Copy this block for every request and fill it with the user. Fields marked with * are required.

```
Publish instruction: publish / prepare only
Publish mode: single platform / specified multi-platform / all platforms / product promotion
Platforms: the platforms for this request; product promotion may say "as recommended" or list platforms
Product: (product promotion only, name and one-line selling point)
Publish time: now / scheduled (date and time, with timezone)

Content files*: (video / image / text, file names; several files are preflighted one by one)
Content type*: video / image / image+text / text only / mixed
Account: (when several accounts exist, the account per platform; otherwise the default)
Language: the language of the copy
Alt text: (for images, when supplied)
Video type: horizontal long video / vertical short video (9:16), video only
Generic title*:
Generic description:
Generic tags: (comma-separated, at most 10)
Cover: supplied with the content / a frame from the video (give the time) / first image / none
Original: yes / no
Contains promotion or partnership: no / yes (name the brand)
Pinned comment: (may be empty)

Per-platform overrides (only the platforms in this request, leave the rest empty):
- YouTube title:
- YouTube description:
- Bilibili category:
- Bilibili title:
- Xiaohongshu title:
- Xiaohongshu body:
- TikTok copy:
- X copy:
- Instagram / Facebook copy:
- Threads copy:
- LinkedIn copy:
- WhatsApp destination (Channel / group / Status, exact name):
- Discord destination (server + channel):
- Telegram destination (channel / group):
```

## Receipt

Send one receipt after the run. List only the platforms in the current list. Use only four states: published, submitted for review, failed, skipped. Give a reason for every failed or skipped platform.

```
Publish receipt (YYYY-MM-DD HH:MM, user's timezone)
Publish mode: single platform / specified multi-platform / all platforms / product promotion
Content: <file name or title>

Published: Instagram <link>
Submitted for review: TikTok
Failed: X — <reason>
Skipped: Xiaohongshu — <reason>

Summary: X published, X submitted, X failed, X skipped
Needs you: <none, or one line per item with platform and what to do>
```

## Dry-run receipt

Send this when the user asks for a dry run. Publish nothing.

```
Dry-run receipt (YYYY-MM-DD HH:MM, user's timezone)
Publish mode: single platform / specified multi-platform / all platforms / product promotion
Content: <file name or title>

Can publish: Instagram
Skipped: YouTube — content type is image, YouTube takes video only
Skipped: X — copy is 301 characters, over the 280 limit

Summary: X can publish, X skipped
Needs you: <none, or one line per item>
```

## Content templates

Pick one and fill it. Do not copy the example wording; fill it with the real content.

### Product promotion

- Content type: video, image, or image+text
- Title: product name + one benefit
- Body: what it does, who it is for, one proof point, where to get it
- Promotion declaration: yes, name the brand
- Recommended platforms first: Xiaohongshu, Instagram, TikTok, then YouTube and LinkedIn when the product is work related

### Work update

- Content type: text, image, or video
- Title: what changed, in one line
- Body: what you did, what changed, what is next
- Recommended platforms first: LinkedIn, X, Threads

### Personal share

- Content type: image, video, or text
- Title: one line, no clickbait
- Body: what happened, what you thought, one line at the end
- Recommended platforms first: Instagram, Xiaohongshu, Threads
