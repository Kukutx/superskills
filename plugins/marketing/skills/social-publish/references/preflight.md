# Preflight

Run this before any publish, including a dry run.

- Check every content file is readable. For video also record duration and resolution and check it plays, the aspect matches the target platforms, and the cover exists or a frame time is given. For images report dimensions and check the aspect against [platforms.md](platforms.md); the platform page wins over the table. When a file cannot be read, treat it as unusable and ask the user for a new file instead of publishing it.
- Record each file's content hash and size; the hash is what the ledger matches on.
- Check the ledger for the same hash and platform. When the same content already published to that platform, stop and ask the user before publishing again.
- Check the content type is supported by each platform in the list. YouTube, Bilibili and TikTok take video only. Skip a platform that does not support the content type, with the reason in the receipt.
- Check the brief is complete and the originality and promotion declarations match reality.
- Check the copy for private information: phone numbers, email addresses and home addresses the user did not mean to publish. When you find one, stop and ask the user.
- Check copy length against [platforms.md](platforms.md) when the copy is long. When it is over the limit, shorten it first and publish only after the user confirms the change.

## Runbook: one publish run

Use this for every run, in order.

1. Fill the brief in [publish-brief.md](publish-brief.md): content type, files, platforms, account, language, declarations.
2. Run the preflight above on all files. Fix every failure before going on.
3. Check the ledger for each file and platform. Skip anything already published.
4. Check copy length when the copy is long. For images, check dimensions against [platforms.md](platforms.md) for each target platform.
5. Run the login health check for the platforms in this run only.
6. Publish one platform at a time, in the order the user gave. Record the link or status right after each one, and append a ledger line right after each one.
7. If a run stops, follow the resume section below. Do not restart from the beginning.
8. Archive each published file named `YYYY-MM-DD_<first 8 chars of hash>_<original filename>`.
9. Send one receipt when all platforms are done.

Time estimate: a single-platform run is about 5 to 10 minutes including preflight. A 9-platform run is about 45 to 90 minutes. Do not promise a faster time.

## Resume after an interruption

When a run stops in the middle, do not restart from the beginning.

- Read the ledger and list the platforms already marked published or submitted.
- Skip every platform already published or submitted. Do not republish them.
- For a platform marked failed, check first whether it already made a draft or a published post, then follow [troubleshooting.md](troubleshooting.md).
- Continue with the remaining platforms in the original order.
- Append new ledger lines only for the platforms run in the resumed run.
- Send one receipt for the resumed run that lists only the platforms in that run, and note which platforms were already done in the earlier run.

## Failure categories

Use only these six categories in receipts and in the ledger. Do not invent new ones.

- login_expired: the platform logged the user out.
- verification_blocked: captcha, SMS code or human check stopped the publish.
- upload_failed: upload or transcoding interrupted or failed.
- review_rejected: the platform rejected the content in review.
- copy_over_limit: title, body or tags exceeded the platform limit.
- other: anything else, with a one-line reason.
