---
name: promo-video
description: Plan a promo, trailer or demo video for an app, game or product with screen capture, footage or AI shots, a script, shot list and captions. Use for video planning, not still images or social posts.
---

# Promo Video

## Use

Use when a video has to be planned before anything is recorded or generated: a product demo, an app or game trailer, an explainer, a launch clip, a batch of templated videos, or a video that should follow the editing style of a reference.

Prompts for still images belong to `creative/image-prompt-director`. The format rules for an app store's preview video belong to `design/app-store-assets`, which checks the store's current specification. The wording of a short social clip and its caption belongs to `writing/social-content`.

## Domain inputs and blockers

- **What the video is for and where it will play.** This comes before any choice of tool; choosing the tool first is the most common mistake.
- **Target length**, and whether one video or a repeatable template is wanted.
- **Whether a person appears on camera**, and who.
- **What already exists**: screen recordings, gameplay capture, footage, brand assets, a voice.
- **Budget and the user's editing skill.**

Nothing is rendered or generated here. The deliverable is the plan, the script, the shot list and the prompts. Which generation or editing tool to use, what it costs and what its licence allows for commercial work change quickly: the user confirms them on the vendor's own pages, and this Skill names no model, price or licence.

## Choosing the approach per shot

Decide shot by shot; most promo videos combine two or three of these.

| Approach | Use it for |
| --- | --- |
| Screen or gameplay capture | Anything that shows the real product, interface or game |
| Filming a real person | A founder speaking for themselves |
| Templated, code- or data-driven video | Batches, data-driven variants, titles and callouts laid over capture |
| AI-generated shots | Cutaway scenes that are imagined and cannot be filmed, in one consistent style |
| AI presenter | Recurring content with no one on camera, the same script in several languages, personalised outreach at scale |
| Cutting down a long recording | Short clips from a talk, stream or interview |

AI-generated shots do not fit the real product, a specific brand or a real location. An AI presenter does not fit a founder's own message, a product demo or artistic work.

Three rules behind the table:

- **The real product is captured, never generated.** A generation model invents interface details and misdraws a specific product, and a trailer that shows features that do not exist misleads.
- **Readable text is added as an overlay in editing.** Titles, prices, button labels and captions do not come out of a video model legibly.
- **More production is not automatically better.** On short-video feeds, a plain, honest clip often does better than a polished one.

## Script and shot list

A product demo is built in this order: write the script; record the screen or gameplay to match it; lay titles and callouts over the capture; add generated or filmed cutaways where the screen alone is dull; add the voice (recorded or synthetic); export one version per platform. A demo that will be re-recorded after each release is worth scripting as a repeatable capture, so the same path can be recorded again.

The shot list has one row per shot: time range, what is seen, the source (capture, footage, template, generated), what is said, the overlay text, and the asset still missing.

A prompt for a generated shot states five things: the subject, the action, the camera (framing and movement), the visual style and the mood. A vague subject, no camera movement and no style are the three usual reasons for an unusable result.

## Format and captions

- **Aspect ratio follows the placement**: vertical 9:16 for short-video feeds, horizontal 16:9 for video sites and web pages, square 1:1 for some in-feed placements. Confirm sizes, maximum lengths and file limits against the platform's current specification.
- **Captions are always included**, because many viewers watch without sound; treat that as a planning assumption, not a statistic. The video must make sense muted.
- A video that plays in more than one placement gets one export per placement, each listed in the plan.

## Matching a reference edit

When the user wants "a video like this one":

1. Break the reference into a beat-by-beat edit sheet: for each beat, what is shown, for how long, and how it cuts to the next.
2. Name three to five signature techniques that make the style recognisable.
3. Reuse the editing grammar only. The footage, the script and the music of the reference are not copied.
4. Show the edit sheet to the user before planning the new video against it.

Without the ability to watch the reference, work from the user's description or a pasted transcript and screenshots, and say that the sheet was built from a description.

## Output

- **Plan**: purpose, placement, length, the approach per shot with the reason, and what the user must supply or record.
- **Script**: the spoken or on-screen words against time.
- **Shot list**: the table described above.
- **Generation prompts** for each generated shot, and the list of overlay texts to add in editing.
- **Export list**: one line per platform with aspect ratio and length, marked "confirm against the current specification".

## Constraints

- Do not show interface, features, gameplay or results the product does not have, in capture or in generated shots.
- Do not copy another creator's footage, script or music; a reference supplies structure only.
- Music, fonts, stock clips and any person who appears need rights or consent the user holds; flag each one that is not clearly cleared.
- Do not name a tool's price, limits or licence terms from memory; the user checks the vendor's current terms before commercial use.
