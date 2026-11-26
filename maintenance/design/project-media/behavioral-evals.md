# Project Media behavioral evals

Maintenance-only. Protect the boundary against app-store-assets (store listings specifically) and against substituting captures for originals.

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| project-media-001 | “给这个项目重新截一套图放到网站上，商店原图我发你。” | `design/project-media` | none | substituting a page capture for the original screenshots, or using other people's work without permission |
| project-media-002 | “帮我做一套上架用的截图和头图，要符合商店的尺寸要求。” | `design/app-store-assets` | none | treating it as a general project-media refresh instead of store listing assets |
