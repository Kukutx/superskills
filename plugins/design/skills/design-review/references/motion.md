# Motion Craft

Craft rules for interface motion, adapted and rewritten from `jakubkrehel/skills` better-motion (MIT).

## Whether to animate at all

The first question is whether to animate, and the answer is often no. Add motion where the request asks for it or a principle here calls for it. Removing an animation is a valid fix.

The press scale, the icon cross-fade, the stagger and the spring bounce are exact values: 0.96 is not 0.95. The duration, scale and distance tables are starting points for desktop web; adjust them by eye for the element's size and the distance it travels. Full-screen transitions on mobile run longer and travel farther. Keep the project's motion library, tokens and curves, and match its motion language wherever no principle here gives a value.

## Frequency decides

Keystrokes, row hovers and the content behind a tab change instantly, or with a transition of 150ms or less on opacity or background colour. A menu people open many times a day skips its opening animation and animates only as it closes. Reserve expressive motion for infrequent moments such as a view's first load, a success state or an empty state.

Every animated state change also leaves a static cue in the form of a colour, icon or label. Motion is never the only feedback channel.

## Transitions, not keyframes

Drive interactive state changes with CSS transitions or a motion library's springs, which retarget when the user reverses mid-flight. Keyframes run a fixed timeline and cannot reverse, so reserve them for sequences that run once.

## Duration follows size

| Element | Enter |
| --- | --- |
| Tooltips and other small elements | 150ms |
| Dropdowns and menus | 250ms |
| Modals, drawers and panels | 350–450ms |

An exit runs shorter than its enter: a dropdown that opens in 250ms closes in 150ms.

## Easing and springs

Enters, exits and state changes take `ease-out`. Loading indicators and other continuous loops take `linear`. A sheet opening, a shape morphing, a drag settling and a slider thumb take a spring, because they imitate a physical object. A colour or opacity change never takes a spring, since nobody can see the difference. Without a motion library, stand in with `cubic-bezier(0.2, 0, 0, 1)` at the same duration.

Write a spring as a duration with bounce 0 (0.3 for small swaps, 0.4 for a tab indicator, 0.45 for a drawer). Where one surface shares a spring, set it once on the surface and leave transitions off the children.

## Scale and travel

- Scale shrinks as the element grows: a tooltip or dropdown enters from 0.96 or 0.97; a modal or panel enters from 0.98 or 0.99 and exits to 0.99.
- Scale from the trigger: set `transform-origin` toward the element that opened the popup, never the default centre. A dialog centred on the screen keeps the centre.
- Travel only far enough to show direction: a text swap 4px, a page transition 8px, dropdowns and tooltips 8–32px, sheets and side panels up to 70% of their own width or height. A dropdown moves away from its trigger; a panel enters from the side it was opened from.
- A pressed button scales to 0.96 over 150ms with `ease-out`; a disabled one never scales. Give the button an opt-out where the motion would distract.

## Entrances, exits and shared elements

- Stagger infrequent entrances by 100ms, in semantic chunks (title, description, actions), each entering with opacity, 4px of blur and 12px of vertical movement over 300ms with `ease-out`. Never stagger routine interactions.
- Exit with opacity, 4px of blur and a fixed −12px vertical movement over 150ms with `ease-out`. Slide fully out only where the destination carries meaning, such as a drawer closing. Remove the element instantly where motion adds no information.
- Skip state animations on first render, so the default state does not animate in on mount. Never skip an intentional entrance such as a staggered hero.
- Cross-fade contextual icons (play to pause, copy to copied): scale 0.25 to 1, opacity 0 to 1, blur 4px to 0, over 300ms.
- One shared-element id per pair. Unrelated elements that share one animate into each other.

## Drags and performance

A row that snaps open and closed lands on a snap point, never where velocity throws it. On release, animate to the nearest snap point with a spring; the commit threshold is half the distance to that point.

Transition only what changes: name the exact properties, never `all`. Animate `transform`, `opacity`, `filter` and `clip-path`, which skip layout; measured height is the one layout property worth animating. Add `will-change` only after seeing the first frame stutter or a 1–2px shift as the animation starts or settles, and name the property it covers. Load only the motion features in use.

## Reduced motion and theme

Gate motion behind the reduced-motion preference; the requirement itself is in [accessibility.md](accessibility.md). Under reduced motion, replace travel, blur and entrance or exit scale with an opacity cross-fade. The press scale stays, because it is brief feedback and not travel.

Suppress transitions on theme switch, or every colour transition fires at once and the switch smears. Slow the motion down before calling it done: a timing problem invisible at full speed shows up at half speed.

## Source

Adapted and rewritten from `jakubkrehel/skills` skills/better-motion/SKILL.md, https://github.com/jakubkrehel/skills (MIT).
