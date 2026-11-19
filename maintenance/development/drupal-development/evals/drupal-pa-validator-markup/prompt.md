---
description: drupal-development traces a failed comuni conformity check to markup lost in a template override
runs: 2
max_turns: 6
allowed_tools: [Skill]
---

我们给一个 comune 做的 Drupal 11 网站，前台主题是 bootstrap_italia 的 italiagov 子主题。客户想让服务页（内容类型 `servizio`）换个排版，我把基础主题里的 `node--servizio--full.html.twig` 复制到子主题，重写成了更简洁的结构：字段都还在，顺序也没变，样式是我们自己写的 Bootstrap 类，页面看起来完全正常。

但是用 pa-website-validator-ng 按 municipality 跑检测，服务页那几项（C.SI.1.3 服务页内容、C.SI.2.2 办公室联系方式）从之前的通过变成了不合格。缓存清过了，内容也没动过。可能是什么原因？要怎么改才能再通过？
