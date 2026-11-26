# Deprecation watch

宿主格式会退休，而且退休前很少大张旗鼓。GPTs 的教训是：公告 2026-09-11
就出了，包里一直到 2026-11-26（创建已截止一个月后）才动手清理。这份文档
规定以后怎么盯、以及一旦确认退休按什么流程处理，不再事后补救。

## 盯什么

每个宿主一条，来源只认厂商自己的公告、帮助中心和 changelog，不认二手转述。
二手消息只用来提示“去核对原文”，核对前不当事实写进文档。

| 宿主 | 盯的来源 | 当前已知的待办 |
| --- | --- | --- |
| OpenAI（ChatGPT Skills/插件 + Codex） | Help Center 的 GPTs / Skills / Plugins 文章、ChatGPT 发布说明、developers.openai.com/plugins、Codex changelog | GPTs 退休收尾（见下）；`agents/openai.yaml` 的字段（`policy`、`dependencies`）有无新增；Codex 描述目录预算约 8,000 字符仍是估计值，从未实测，需重测 |
| Anthropic（Claude Code / claude.ai） | Claude Code changelog、Help Center 的 Plugins 页 | 2026-11-30 起 Enterprise 默认进统一 Plugins 页，组织关了 Skills 则插件也被禁；Claude Code 2.1.323 起插件的 `agent` 设置给 deprecation 警告；2.1.326 起 marketplace 里的 Skill 要过额外的来源与名称检查（标准不明，二手来源，待对 changelog 核实） |
| Agent Skills 开放标准 | agentskills.io 规范、Agentic AI Foundation 公告 | 2026-10-22 已捐给 Linux Foundation 下的 Agentic AI Foundation，成为开放标准；盯规范本身的字段变化（frontmatter、500 行建议），而不是某一家宿主的说法 |
| Google Antigravity / Gemini | `agy changelog`、Gemini CLI 文档 | Skill 路径（工作区 `.agents/skills/` 与全局 `~/.gemini/config/skills/`）有无变化；`agy plugin import claude` 行为仍未验证 |
| Muse | 无官方安装流程 | 一旦出现官方流程，替换本地复制安装的说明 |
| Grok | 无官方文档 | 最低优先级；有官方文档前不采信 passthrough 之类的说法 |

## 节奏

不另设值班。`planning/daily-brief` 每周一已经读 Claude Code、Codex、
Antigravity CLI 的发布说明并查官方 MCP 注册表——这份 watch 的来源清单
就是周一检查的输入。发现公告或日期变动时，当天更新本文档的“当前已知的
待办”一栏，并按下面的退休流程开工，不要等到下一轮集中处理。

## 退休流程

确认某宿主格式要退休时，按顺序做：

1. **核实。** 只认厂商自己的文档：公告日期、创建截止、退休日期、替代路
   线、迁移后哪些东西带不过去。日期注明“截至某日查询”，并写明“厂商说日
   期可能变动”。
2. **定替代路线并先验证它能用。** 先有能跑的替代安装/触发方式，再删旧
   格式；没有验证过的替代路线，旧格式先留着并在文档里标“未验证”。
3. **清理。** 删格式专属的工具、CI 任务和文档说法；`SKILL.md` 本身不动，
   只动 adapter 和文档。删掉的东西在文档里留一句话说明去向（git 历史可
   恢复），不要静默消失。
4. **更新状态表。** `docs/multi-agent.md` 的状态总表和相关安装说明同步改；
   有描述或路由变化的 Skill 才需要重跑受影响的 eval case（AGENTS.md 规则 14），
   不整套重跑。
5. **留档。** 退休的格式和日期记进本文档的“已退休”一节，供以后查。

## 已退休：Custom GPTs（worked example）

- **时间线（OpenAI Help Center “GPTs in ChatGPT”，2026-11-26 查询）：**
  2026-09-11 发布说明公告计划退休并迁移到插件；2026-10-26 起受影响的
  Enterprise 工作区停止新建 GPT（FedRAMP 除外）；标准退休日
  **2026-12-11**，此后 GPT 及其页面不可访问；FedRAMP 工作区和获批延期
  的工作区退休日 **2027-02-28**。日期厂商说可能变动。
- **替代路线：** 插件（Plugins），基于 Skills。GPT 的 instructions 变成
  Skill，knowledge 文件变成 reference 文件，已连接的应用带过去；custom
  actions、选定的模型、分享设置、未发布的草稿带不过去，需重建（actions
  可用 MCP 服务器重建）。迁移后原 GPT 只读，不可删除。
- **包里的处理（Round 4，2026-11-26）：** 删 `gpts/`、`tools/build_bundle.py`
  及其测试、CI 的 `core-bundle` 任务和 bundle 发布产物；`openai.yaml`
  从“ChatGPT + Codex”重述为“OpenAI（ChatGPT Skills/插件 + Codex）”，
  内容不变；Router 保留（ChatGPT Projects 未退休，只是没有原生 Skill
  注册表，仍走手动上传）。`project-instructions.md` 的实质已由
  `docs/authoring-guide.md` 的“Autonomy and escalation ownership”承接，
  全文留 git 历史。
- **这次晚了的原因：** 公告与动手之间隔了约 11 周，期间没有任何一个固定
  检查点会读到它。上面的周一检查 + 本文档就是补的这个缺口。
