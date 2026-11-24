# Accessibility Craft

Craft rules for accessible interfaces, adapted and rewritten from `jakubkrehel/skills` better-accessibility (MIT). The review-level checks (contrast table, WCAG criteria) stay in the design-review entrypoint; this file is the build-side detail.

## Criteria, not conventions

Judge against WCAG criteria, not against habit. An automated scan finds only a minority of accessibility problems; a keyboard-only pass and a screen-reader pass on the real build are still needed.

## Native elements first

Use the native element before building a custom one: a button for an action, a link for navigation, an input with its label. Custom controls must expose name, role and value, and must work with the keyboard exactly as the native one does.

## Keyboard and focus

- Every function is operable by keyboard, with no trap: a user can tab in and tab out of every component.
- Focus order follows the visual order, and the focus indicator is always visible. Never remove a focus ring without replacing it with an equally visible one.
- Modal dialogs trap focus while open and restore it to the trigger on close.
- Skip links, landmarks and heading structure are navigation: a screen-reader user moves through them the way a sighted user scans the page.

## Targets and labels

- Minimum hit area 24×24 CSS pixels (44×44 is the enhanced level). Adjacent targets never overlap.
- Label and type every control: inputs have visible labels, buttons have accessible names, icons that act alone have names. A placeholder is not a label.
- Errors are identified in text, described in text, and announced; an error shown only by colour is invisible to many users. Announce dynamic content (toasts, live counts, validation results) through a live region.
- Alt text follows purpose: a meaningful image gets a text alternative describing its content, a decorative image gets an empty alt, and a functional image gets the action it performs.

## Colour and motion

- Never let colour be the only carrier of meaning. Pair colour with an icon, a label, or a second cue such as shape or text. Colour rules are in [colors.md](colors.md).
- Honour `prefers-reduced-motion`: travel, blur and entrance or exit scale are gated behind it and replaced with an opacity cross-fade. Motion rules are in [motion.md](motion.md).

## Time, zoom and resize

- Nothing the user needs runs on a timer that cannot be paused, extended or turned off. Auto-playing media has controls.
- The interface survives 200% zoom and text resize without loss of content or function. Text containers size with `max-width` and `min-height`, never a fixed width or height; layout rules are in [layout.md](layout.md).

## Common faults

| Pattern | Fix |
| --- | --- |
| A button built from a `div` with a click handler | Use the native button; it brings keyboard behaviour, focus and semantics for free |
| A focus ring removed with no replacement | Replace it with an equally visible indicator; never leave focus invisible |
| A modal that lets focus escape to the page behind it | Trap focus while open and restore it to the trigger on close |
| A form input with a placeholder and no label | Give every input a visible label; a placeholder is not a label |
| An error shown only by red colour | Identify and describe the error in text, and announce it |
| An icon-only button with no accessible name | Name it by what it does |
| A meaningful image with empty alt text | Describe its content; empty alt is only for decorative images |
| A data table built from `div`s | Use table semantics so a screen reader can navigate rows and columns |
| A status change announced nowhere | Announce dynamic content through a live region |
| Motion that plays under reduced-motion preference | Gate travel, blur and entrance or exit scale behind the preference |
| Text that clips or overlaps at 200% zoom | Size containers with `max-width` and `min-height`, never fixed dimensions |

## Verification

A review from a picture is a starting point. A keyboard-only pass and a screen-reader pass on the real build are still needed, and the report says so. An automated scan finds only a minority of accessibility problems; the checks above are the manual complement.

Walk the keyboard path yourself: tab from the top of the page to the primary action without a mouse, open every menu and dialog, submit the form with an error, and confirm that focus is always visible and never lost. Then run a screen reader through the same path and confirm that every control announces its name and its state, and that dynamic changes are announced rather than silently appearing.

## Source

Adapted and rewritten from `jakubkrehel/skills` skills/better-accessibility/SKILL.md, https://github.com/jakubkrehel/skills (MIT).
