---
name: product-launch
description: Plan a product, app, game or store launch with readiness gates, phased rollout, Product Hunt and directory submissions and press pitches. Use for launches, not ongoing marketing.
---

# Product Launch

## Use

Use when something is about to be made public and the work is to decide whether it is ready, in what phases it opens, where it is announced and to whom it is pitched: a new product, a major feature, an app or game release, a shop opening, a Product Hunt day, a round of directory submissions, a press pitch.

The technical go/no-go gate for the release artifact (smoke path, rollback, monitoring) belongs to `operations/release-checklist`. The ongoing campaign after launch belongs to `marketing/marketing-plan`. Store listing text belongs to `writing/app-store-copy` and store visuals to `design/app-store-assets`. If who the product is for is still open, `marketing/product-positioning` comes first.

## Domain inputs and blockers

- **What is launching**: a new product, a major update or a minor one. It sets the size of the effort (see the tiers below).
- **Owned audience today**: email list size, community, followers. A launch with no owned audience plans the pre-launch around building one.
- **The date and what is fixed about it.**
- **Where visitors will land**, and whether that page exists yet.
- **For press**: what is new and true that a journalist could report.

Store-specific launch mechanics (beta distribution, pre-registration, review times) are taken from the store's current documentation, not filled in from memory.

Nothing can be submitted, checked or sent from here. Whether a directory is still live, whether a listing's link is followed, and who a journalist is are checked by the user or reported as not checked.

## Readiness gates

**Is the product ready to be shown?** Three tests:

- **Simple**: it does one thing.
- **Lovable**: someone would choose it; if nobody would be sorry to lose it, it is not there yet.
- **Complete**: within the scope chosen, the experience is whole.

Past that line, two delays look like diligence and are not: polishing in private, and adding one more feature. Name whichever is happening and recommend launching.

**Is there somewhere to send people?** Before any directory or press outreach, these are hard blockers, because a listing or article is only a link and needs a page that converts:

1. the product is publicly reachable;
2. a page states the price, even if the price is "free during beta";
3. a privacy policy and terms exist;
4. a logo in the formats listings ask for, real screenshots and a short demo video;
5. a page that states plainly what the product is and for whom, with one main heading;
6. for a directory campaign, honest comparison pages and use-case pages to link to (three of each is a working minimum).

Soft blockers: a template or resource library, and a group of early users willing to write reviews. For a business review site the reviews are a hard condition: a listing with none is worth little, so claim the page, collect reviews from users who have really used the product (a personal email each, a direct link, one reminder), and submit properly once around ten are within reach. Whether the site allows an incentive for a review is checked in its own rules.

### Technical go-live checklist

For a product that is an app, the technical half of going live — hosting, database, domain/DNS, email, auth, payments — is in [references/go-live-checklist.md](references/go-live-checklist.md). A handoff there is closed only by a passing check, and no provider write happens until the user approves the plan.

## Phases and channels

| Phase | What happens |
| --- | --- |
| Internal | Used inside the team only |
| Alpha | A landing page with an early-access form |
| Beta | A teaser and a waiting list |
| Early access | Invite the list in batches of 5 to 10%, or open to all at once |
| Full launch | Self-serve sign-up opens, charging starts, every channel announces |

Each phase has one stated goal; skipping phases is fine when the goal of the skipped phase is already met.

**Channels come in three kinds.** Owned (email, blog, own community, website) is where everything leads. Rented (social platforms, app stores, video sites, forums): pick one or two and point them back to an owned channel. Borrowed (guest content, partners, talks, creators): use for reach the user does not have.

**Size the announcement to the change**: a major update goes to every channel; a medium one to a segmented email and an in-app banner; a minor one to the changelog. Spacing small updates out shows the product is alive.

**After launch day**: an onboarding email to new sign-ups, a second mention in the regular newsletter, a comparison page, a section on the website, and follow-up with everyone who engaged.

**Borrowed reach is arranged long before the date**: podcast guest slots, a partner with a complementary product, creators, the communities the audience already uses, guest articles and cross-promotion all take weeks to line up.

**A launch that happened and produced little** is diagnosed, not repeated: too small an audience built beforehand, the wrong channel, a weak statement of value, poor execution on the day, or the wrong people reached. Find where the signups that did come arrived from, put more into that channel, turn the first users into testimonials, and set a 30-day recovery plan.

Product Hunt and directory submissions are in [references/product-hunt-and-directories.md](references/product-hunt-and-directories.md).

## Press

Press amplifies distribution; it rarely converts directly. Its value is links, legitimacy and material to quote.

- **Worth doing when** there is a real story (data only the user has, a point of view, a milestone, a customer's before and after), founder time for four to eight weeks, and a page to land on. Without a story, do not pitch. Building the media list, the pitch and follow-up rules, embargoes and exclusives, reacting to news and podcast preparation are in [references/press.md](references/press.md).
- **The story is not the product.** It is a trend, a number, a conflict or a person. Three angles that work: the founding story, small against large, and a named enemy that is a broken system and not a competitor.
- **Send a pitch only if every answer is yes**: the journalist's last five pieces cover this field; there is something new; the email alone is enough to write the article (data, a quote, a customer name, contact details); the subject line could be the headline; it is under 150 words; it contains none of "revolutionary", "game-changing", "disruptive"; the ask is clear.
- **A press page** holds a one-paragraph description, founder photo and bio, a logo pack for light and dark backgrounds, screenshots, recent coverage, founding date and team size, and an email address, with replies promised within a day.
- **Measure** pieces published, the quality of the sites, referral traffic and the rise in brand searches. Advertising-value equivalents are a vanity figure.
- **If the launch goes wrong in public**: establish the facts, tell the affected people before anyone else, name one spokesperson, and publish a short holding statement that says when the next update comes and nothing yet about cause or scope, all within the first hour. A larger crisis is handled with `operations/crisis-communications`.

## Output

- **Launch plan**: the readiness verdict with each failed gate, the phases with a goal and date each, the channel list by kind, and three checklists (before, launch day, after).
- **Product Hunt or directory plan**: fit verdict, the listing kit, the order of submissions by week, the pages to build first, and a tracking table (site, tier, category, date submitted, status, live URL, link type and whether it was verified, the positioning variant and tags used, the account used). Submitting is not the strategy: after the peak, results come from the pages built to receive visitors, reviews and continued content. Review weekly what the listings produced (referring sites, indexed pages, organic clicks, signups from directories), and when nothing moves, find out why before submitting more.
- **Press**: the angle, the pitch under 150 words with its subject line, the quality-line check, and the press-page list.

## Constraints

- Do not state a platform's launch rules, ranking behaviour or a directory's policies as fact; label conventions as conventions and point to the platform.
- Do not write a pitch around a story that is not true or data the user does not have.
- A public statement that involves a data breach, injury, a lawsuit or a regulator goes to a lawyer before anything is admitted or published.
- Do not plan paid votes, fake reviews or coordinated upvoting.
