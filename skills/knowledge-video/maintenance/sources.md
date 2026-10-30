# Knowledge Video sources

Maintenance-only.

## Upstream inspiration

- [andyhuo520/vibe-knowledge](https://github.com/andyhuo520/vibe-knowledge) (Berryxia), snapshot received 2026-10-30, MIT.
  - Adapted and condensed: the six script templates, duration tiers and complexity scoring, fact-list format and source tiers, narration/visual sync rules, premium checklist, style catalog (one-line descriptions), publish pack, render-stage rules.
  - Changed for this repo: the three confirmation gates became "pick the recommended default and say which", except paid generation and voice consent; the forced default BGM rule, machine-specific paths and campaign-specific publish rules were dropped; a script-package level was added for hosts without the render pipeline.
  - Not included: the render engine, tools, fonts, icon sets, default BGM, default voice, style stills and sample media. Reasons: about 92 MB, unusable on claude.ai web, and the upstream NOTICE.md restricts redistribution of the BGM and demo media separately from the MIT code.

Upstream license (applies to the adapted portions):

```text
MIT License

Copyright (c) 2026 Berryxia (andyhuo520)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
