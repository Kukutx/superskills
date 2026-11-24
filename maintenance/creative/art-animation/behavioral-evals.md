# Art Animation behavioral evals

Maintenance-only. Protect the boundary against knowledge-video (script package only) and promo-video (marketing video).

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| art-animation-001 | “用梵高的画风做一段 60 秒的解说动画，讲印象派是怎么来的，画面本身要动起来。” | `creative/art-animation` | none | delivering a script package only, or changing art style mid-film |
| art-animation-002 | “按我的口播稿做一段艺术动画，先给我镜头表，每镜写清楚画面里的物和动作。” | `creative/art-animation` | none | starting to render before the shot list is locked |
| art-animation-003 | “帮我写一个知识视频的脚本和分镜，不用真的渲染成片。” | `creative/knowledge-video` | none | invoking art-animation for a script-only deliverable |
