# Troubleshooting

- Login expired: ask the user to log in again in the browser and resume from that platform. Do not republish platforms that already succeeded.
- Captcha or SMS verification: stop at that platform and hand the user one concrete action. Resume only after the user says it is done.
- Upload interrupted or transcoding failed: check first whether the platform already made a draft or a published post. Confirm there is no duplicate before retrying, and retry only after the user confirms.
- Review rejected: record the reason the platform gave and fix only the issue it names. Do not change content on platforms that already published.
- Wrong platform or wrong copy: tell the user the platform and the change needed. Edit online when the platform allows it. Delete and republish only after the user explicitly confirms that exact post.
- One platform fails: finish the other platforms in the list first, then return to the failed one. Report it as failed with its reason in the receipt.
- Browser disconnects in the middle: do not restart the run. Read the ledger to see which platforms already finished, check the current platform for a draft or a published post, then follow the resume section in [preflight.md](preflight.md). When the browser session drops, ask the user to reopen the browser and confirm the tab is back before continuing.

## Login health check

Run this before a publish day, for the platforms in the current list only.

- Open each browser platform's entry and confirm the account is still logged in.
- Check the connected accounts are still connected before publishing to Instagram, Facebook or Threads.
- Record the check date and any platform that needs relogin. Do not publish to a platform that failed this check.
- When a platform needs relogin, hand the user one concrete action and skip that platform in the receipt with reason login_expired.

## Adding a platform

Use this checklist when the user names a new platform. Do not publish to it before all steps pass.

- Ask the user for the platform name and the account that should publish.
- Open the platform in the user's logged-in browser and confirm the account is logged in.
- Find the publish entry point and record its exact URL.
- Check whether the platform has a connected-account route or needs the browser route.
- Note the content types the platform supports, the format, the copy fields, the tag handling and the cover handling.
- Test with one single-platform publish or with a draft when the platform supports it.
- Add the platform to [platforms.md](platforms.md) with its route, entry and notes, and to the publish brief when it needs its own copy field.
- Publish to the new platform in a multi-platform run only after the single-platform test succeeds.
