# Social Publish sources

Maintenance-only.

| Source | Canonical URL | Used for | Last reviewed |
| --- | --- | --- | --- |
| YouTube Studio | https://studio.youtube.com/ | Browser publish route, video only, declarations | 2026-11 |
| TikTok Studio | https://www.tiktok.com/tiktokstudio/ | Browser publish route, video only | 2026-11 |
| X | https://x.com/ | Browser publish route, text, image, video | 2026-11 |
| Bilibili Creator Center | https://member.bilibili.com/platform/home | Browser publish route, video only | 2026-11 |
| Xiaohongshu Creator Center | https://creator.rednote.com/new/home | Browser publish route; creator.xiaohongshu.com redirects to SMS login and is not used | 2026-11 |
| LinkedIn | https://www.linkedin.com/ | Browser publish route, professional posts | 2026-11 |
| WhatsApp Web | https://web.whatsapp.com/ | Private route, Channel, group, Status, web size limits | 2026-11 |
| Discord | https://discord.com/app | Private route, server channel, free 20 MB file limit | 2026-11 |
| Telegram Web | https://web.telegram.org/ | Private route, channel, group, free 2 GB file limit | 2026-11 |

Method adapted from the author's own social-publish skill (v3.4, local, no public URL): scope modes, brief, preflight, ledger, resume and failure categories. The author's deterministic check scripts (preflight-content, check-copy, check-image-size, ledger-check, check-consistency, transcode) and platforms.yaml were deliberately not ported: this pack has no script convention, so the checks are written as steps. Per-platform limits are approximate and checked against the platform page at publish time.
