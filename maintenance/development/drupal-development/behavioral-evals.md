# Drupal Development behavioral evals

Maintenance-only. Protect the reference split, the Drupal/WordPress boundary, and the decisions a plain model gets wrong: cacheability metadata instead of `max-age: 0`, configuration as code, one major upgrade at a time, and the validator's markup on public-sector sites.

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| drupal-001 | “Drupal 11 的自定义区块显示当前登录用户的预约数量，结果每个人看到的都是第一个访问者的数字，怎么修？” | `caching.md` | `modules-and-hooks.md` | setting max-age to 0 or killing the page cache instead of adding the user context and the bookings' cache tags |
| drupal-002 | “编辑在生产环境后台改了几个 webform，昨天部署跑了 drush deploy，改动全没了，以后怎么避免？” | `config-and-deploy.md` | none | telling editors never to use the admin UI without deciding who owns that config (Config Ignore or ship it as code) |
| drupal-003 | “我们的市政府网站还在 Drupal 9.5，想一步把 core-recommended 改成 ^11 升上去，行不行？” | `upgrades.md` | none | one Composer step across two majors, or stopping at Drupal 10 as the target |
| drupal-004 | “comune 网站的服务页我用 Twig 重写了 node--servizio--full，页面看着没问题，但官方检测工具说服务页不合格。” | `italian-public-sector.md` | `theming.md` | blaming the validator, or fixing only the visible layout without restoring the model's data-element attributes |
| drupal-005 | “写个 Drupal 11 模块，加一个链接，点击后把这篇新闻标记为已审核。” | `security.md` | `modules-and-hooks.md` | a state-changing GET route without a permission requirement and `_csrf_token` |
| drupal-006 | “旧的 Drupal 7 区政府网站有 3000 篇新闻和附件，要导入新的 Drupal 站。” | `content-and-migrate.md` | `upgrades.md` | a one-off SQL import script, or planning the Drupal 7 migration on Drupal 12 |
| drupal-007 | “给我们的自定义模块配上 PHPStan、PHPCS 和测试，放进 CI。” | `quality-and-testing.md` | none | existing-site tests that assert total counts or run against production |
| drupal-008 | “下周三 Drupal 有个高危核心安全更新，我们还有两个 Drupal 9 站点，怎么办？” | `development/drupal-development` | none | presenting a hand-patched Drupal 9 site as secure, or omitting that the upgrade is the remedy |
| drupal-009 | “WooCommerce 结账页加一个税号字段。” | `development/wordpress-development` | none | invoking drupal-development for a WordPress store |
| drupal-010 | “用 PHP 写一个命令行脚本，读 CSV 统计每个月的订单数。” | none | none | invoking drupal-development or wordpress-development for framework-free PHP |

## Pressure cases

### Cache bug versus disabling the cache

Prompt: `区块里显示“你好，某某”，匿名用户也看到了别人的名字。`

Pass: the piece varies per user, so it gets the `user` context (or a lazy builder placeholder) and the tags of the data it shows; the rest of the page stays cached. Turning off caching for the page or block is not the fix.

### Production config edits

Prompt: `客户说他们自己在线上改了几个 block 的位置，我们这周要发版。`

Pass: say before the deploy that the import will overwrite those changes; export them from production into the branch first, or decide they are editor-owned and exclude them.

### End-of-life core

Prompt: `Drupal 10 的站点明年再升级可以吗？`

Pass: give the Drupal 10 end-of-life date from a re-checked source and what stops after it; do not promise security releases for an end-of-life major.

## Regression rule

Add a case only when it protects a real ownership boundary or a decision a plain model gets wrong. Version facts are re-verified at execution time, not frozen into cases.
