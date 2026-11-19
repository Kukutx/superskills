---
name: ux-copy
description: Write or review interface microcopy such as button labels, error messages, empty states, confirmation dialogs, tooltips and onboarding text. Use for in-app wording, not store listings or emails.
---

# UX Copy

## Use

Use for the words inside a product: buttons, labels, errors, empty and loading states, dialogs, tooltips, onboarding and notifications.

Store listing text belongs to `writing/app-store-copy`; help-center articles belong to `support/help-center-article`.

## Domain inputs and blockers

Three facts decide the wording: where the text appears (which screen and element), what the user was trying to do when they see it, and any hard limit (character count, platform convention, existing terminology). Use a neutral, friendly voice when none is given. Existing product terms win over better-sounding synonyms.

## Patterns

- **Button or call to action**: starts with a verb and names the outcome ("Create account", "Save changes"). The label matches what happens next.
- **Error**: what happened, why, and how to fix it. "Payment declined. Your bank rejected the card. Try another card or contact your bank."
- **Empty state**: what belongs here, why it is empty, and the first action to take.
- **Confirmation dialog**: the title names the action and the amount ("Delete 3 files?"), the body states the consequence ("This cannot be undone"), and the buttons are named after the actions ("Delete files" / "Keep files"), not "OK" / "Cancel".
- **Loading**: sets an expectation of what is happening or how long.
- **Tooltip**: adds something the label does not already say.
- **Onboarding**: one concept at a time, at the moment it is needed.

## Rules

1. One thing has one name everywhere. A "workspace" does not become a "project" on the next screen.
2. Tone follows the moment: success is warm but brief, an error is calm and helpful, a warning says what to do, everything else is plain information.
3. Blame is never placed on the user; describe the state and the way out.
4. Write for translation: no idioms or wordplay, room for text that gets longer in other languages, no meaning that depends on a cultural reference.
5. Every word helps the user finish the task; anything that only sounds friendly is cut.

## Output

The recommended copy per element, then up to two alternatives with the tone and the situation each suits, a one-line rationale, and localization notes when the text will be translated. For a review of existing copy, list each problem with its replacement.

## Constraints

- Do not describe behaviour the product does not have; the copy follows the real flow.
- Do not exceed a stated length limit; when the message does not fit, say what was dropped.
- Legal, pricing and consent wording keeps its required meaning; flag it for the owner instead of simplifying it.
