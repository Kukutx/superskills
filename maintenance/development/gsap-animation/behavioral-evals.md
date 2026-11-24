# GSAP Animation behavioral evals

Maintenance-only. Protect the GSAP/CSS boundary and the timeline rule.

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| gsap-animation-001 | “给首页 hero 加一个滚动触发的入场动画，用 GSAP。” | `development/gsap-animation` | none | chaining animations with delay instead of a timeline, or animating layout properties |
| gsap-animation-002 | “按钮 hover 时变个颜色，加个简单过渡。” | none | none | invoking gsap-animation for a CSS-only hover transition |
