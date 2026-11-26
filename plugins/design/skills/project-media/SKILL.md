---
name: project-media
description: Make or refresh a project's images from originals, own-page captures or own photos, with capture specs, processing and store-badge rules. Not for store listing assets.
---

# Project Media

## Scope

Use for new or refreshed images of a project for its site, resume or READMEs. Where originals and photos live, and the repository paths and tools the site uses, are configuration the user supplies. Images already on the site are the owner's and have permission; never replace one unless asked. Store listing assets specifically belong to `design/app-store-assets`.

## Where images come from, in order

1. The owner's originals. Store screenshots exactly as uploaded to the store consoles, in store order and full resolution; exports from their apps or design files. Ask them to attach the files or say where they are. A page capture never substitutes for an original screenshot.
2. The owner's own public pages, captured by script: their repositories, the product's own site, a store listing when the listing itself is the subject.
3. The owner's photographs.

Other people's work only when the owner says they have permission. Screens show fictional or the owner's own test data, never real users' names, faces or messages.

## Capturing a page

- A capture script kept in the site repository's scratch folder, so a capture can be repeated exactly.
- A fresh, logged-out context; the site's locale, light color scheme; desktop 1440x900 at device scale 2, phone 390x844 at 3. Wait for network idle and fonts ready; decline cookie banners; capture the element that matters, not the whole window.
- Repository pages: the public repository page or README section, logged out, with no notifications or other people's avatars in frame.

## Processing

- WebP, phone screens about 900 px wide, every image well under 500 KB unless the site sets other limits. Slides of one carousel share one size. Social preview 1200x630.
- File names lowercase kebab-case, in the folder the site uses for project assets.
- Alt text names what the image shows.
- Open every result at 100% next to the previous version before it goes in.

## Brand rules

- App Store badge: the platform's own artwork, unmodified, at least 40 px tall, one per layout, linked to the listing. In text the wording is "on the App Store". With the badge, the platform asks for a trademark credit line where the site's legal notices go (exact wording in the platform's marketing resources and identity guidelines).
- Google Play badge: from the platform's partner marketing hub, unmodified; "Google Play" names the store, not the app.
- Device frames only from the platform's design resources, used as they are.
- Nothing may suggest that the platform, the code host or the professional network endorse the owner's work.
- These are facts to offer; what the site already uses is the owner's decision.

## Keeping it current

- A product renamed, redesigned or with new store screens: replace icon, screens, description and listing image together, and correct the resume, LinkedIn and GitHub text that names it (see `people/career-surfaces` when installed).
- The commit message records each new image's source: the original file, or the URL, date and viewport of the capture.

Source: fused from the author's Notion skill `project-media` (2026-11), generalized; the skill's personal references folder (product list, originals, repository paths) was not used.
