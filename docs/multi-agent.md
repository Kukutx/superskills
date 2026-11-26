# Multi-agent adapters

一份 `SKILL.md`，多个宿主。`SKILL.md` frontmatter 只保留 `name` + `description`
（Agent Skills 规范），不加任何厂商字段；每个宿主的特殊配置放在它自己的
adapter sidecar 里，由生成器从 `SKILL.md` 派生。`SKILL.md` 是唯一事实来源，
sidecar 永远不手改。

生态现状（2026-11-26 核查）：Agent Skills 已是开放标准——Anthropic 2025-12
在 agentskills.io 发布规范，2026-10-22 把规范、域名与 GitHub 组织捐给 Linux
基金会 Agentic AI Foundation（与 MCP 同一家）；Anthropic 称已有 70 多个平台
接入，包括 ChatGPT、Codex、Cursor、GitHub Copilot、VS Code（该数字来自
Anthropic，未独立验证）。Skills 与 MCP 是互补关系，不是替代关系：OpenAI
官方文档的说法是 "A skill complements your MCP server"——MCP 给连接与工具，
Skill 给使用方法；本仓库 124 个 Skill 目前没有任何一个需要 MCP 依赖，
`openai.yaml` 的 `dependencies` 保持 `[]`。下面三条 adapter 下注（`skill.yaml`
sidecar、`agents/openai.yaml`、marketplace 清单）与这一现状一致，没有一条已死。

## 状态总表

| 宿主 | 优先级 | 安装 | 触发 | Adapter | 状态 |
| --- | --- | --- | --- | --- | --- |
| Claude Code | 高 | `claude plugin marketplace add Kukutx/superskills`，再 `claude plugin install superskills-<category>@superskills`；或复制到 `~/.claude/skills/` | description 自动触发，`/<skill>`，插件内 `/superskills-<category>:<skill>` | 几乎无；仓库本身就是按 Claude 插件结构建的 | ✅ 已验证安装 |
| Codex | 高 | `codex plugin marketplace add Kukutx/superskills`，再 `codex plugin add superskills-<category>@superskills`；或 `.agents/skills/` | description 自动触发，`/skills` 选择器，`$<skill>` | `agents/<category>/<skill>/openai.yaml`（与 ChatGPT Skills/插件共用） | ✅ CLI 已验证；124 个描述合计 22,792 字符（name+description 24,886），约 8,000 字符默认目录预算的 2.9–3.1 倍，按分类安装（见 Codex 一节） |
| ChatGPT | 高 | Plugins > Skills 上传单个 Skill，或提交公开插件目录（ZIP + 审核）；无本地文件夹 | description 自动触发，`@<skill>` | 同上 `agents/.../openai.yaml`；按分类的 portable `plugin.json`（`"skills": "./skills/"`） | ◐/❌ **未验证**：网页端启用流程从未实测；套餐门槛已松动——定价页 2026-11-25 起把 Skills 列在 Free / Go / Plus / Pro 下，但 Help Center 仍只写 workplace 套餐，个人套餐能否装自建插件仍未验证 |
| Muse | 高 | 无官方安装流程；本地把 `plugins/<category>/skills/<skill>/`（`SKILL.md` + `skill.yaml`）复制到 `~/workspace/custom-skills/<skill>/` | 对话中按 description + `triggers:` 匹配；无斜杠命令 | `tools/generate_skill_yaml.py` 生成 `skill.yaml`（name/title/description/category/include_in_prompt/triggers） | ✅ 124 个已全部导入（2026-11-26，round 4）：122 个与仓库字节一致，仅 social-publish（v3.6 云端浏览器优先）与 social-engagement（本地定制）保留本地版本；全量注册对路由质量的影响仍未验证 |
| Antigravity (Gemini) | 偶尔 | 工作区 `<root>/.agents/skills/`（向上查到仓库根）；全局 `~/.gemini/config/skills/`（各界面路径不同，见 Antigravity 一节）；或 `agy plugin import claude` 从已装的 Claude Code 插件导入 | description 自动触发，`/<skill>` | 镜像/软链 `plugins/*/skills/*` → `.agents/skills/`；或 `agy plugin import claude` / `npx skills add … -a antigravity` | ◐ 官方文档已读（`agy plugin import claude` 见 Antigravity 官方插件文档），行为未实测；CLI 与 IDE 的全局路径可能不同 |
| Grok (Grok Build) | 低 | `.grok/skills/`、`~/.grok/skills/`、`~/.agents/skills/`；也读 Claude Code 的 Skill 文件夹 | `/<skill>`，默认自动触发 | 可能不需要；先用 `grok inspect` 核实 | ◐/❌ **未验证**：路径有据可查（xAI 官方文档，经 2026-11 二手来源核对），但本仓库未实测，`grok` CLI 未安装；“直接读 Claude Code marketplace”的说法仍无依据；最低优先级 |

✅ = 对官方文档或本地 CLI 核对过；◐ = 二手来源；❌ = 未验证，不要当事实用。

## 生成器

```bash
python tools/generate_skill_yaml.py    # Muse：每个 Skill 一个 skill.yaml
python tools/generate_openai_yaml.py   # OpenAI（ChatGPT Skills/插件 + Codex）：agents/<category>/<skill>/openai.yaml
python tools/generate_skill_yaml.py --check   # 检查是否过期（Validator 也会查）
```

`skill.yaml` 字段：`name`、`title`（SKILL.md 的 H1）、`description`（原文照抄）、
`category`、`include_in_prompt: false`、`triggers:`（Skill 名 + description 的
"Use when / Use for" 从句里拆出的短语，最多 5 条）。

`openai.yaml` 字段：`display_name`、`short_description`（原文照抄）、
`policy.allow_implicit_invocation: true`、`dependencies: []`。目前没有任何 Skill
需要 MCP/应用依赖，不编造依赖。将来某个 Skill 明确需要显式调用时，再把对应的
`allow_implicit_invocation` 改为 `false`。

## Claude

参考实现。仓库已带 `.claude-plugin/marketplace.json`（19 个插件）和每分类
`plugin.json`。注意插件内调用要加命名空间（`/superskills-development:code-review`），
而文件夹安装用裸名（`/code-review`）；Router 的 `category/skill` 写法与两者都不同，
三者不要混用。claude.ai 上只接受规范的 6 个 frontmatter 字段，多余字段会硬失败——
仓库保持 SKILL.md 只有 `name` + `description`，正好避开这个坑。

## Codex

与 ChatGPT Skills/插件共用 `agents/openai.yaml`。OpenAI 官方 Skills 文档确认：Skill 就是一个含 `SKILL.md` 的文件夹，`agents/openai.yaml` 是可选的展示、策略与依赖 sidecar；Codex 从 `.agents/skills/`（项目/用户级）等位置扫描 Skill，`$<skill>` 显式调用或按 description 自动触发。描述目录预算约 2% 上下文或 8,000 字符（窗口未知时），超了先缩短描述、再省略 Skill 并给出警告；可用 `skills.max_context_tokens`（上限 10,000 tokens）调高（OpenAI 文档，经 2026-10-15 与 2026-11 二手来源核对）。实测数（2026-11-26，对 124 个 `SKILL.md` 的 frontmatter `description` 求和，脚本见 round 5 报告）：描述合计 **22,792 字符**（平均 184/个，159–190，无一超 200 字符上限），name+description 合计 **24,886 字符**，再加 Codex 相对路径（`.agents/skills/<name>/SKILL.md`）合计 **29,956 字符**——默认 8,000 字符预算的 **2.9–3.7 倍**，全装大概率会被缩短或省略一部分；按分类安装，不要一次装全部。按分类的实际数：每个分类单独都装得下（最大 finance 18 个，name+description 3,676 字符；marketing 17 个，3,397；development 16 个，3,261）；finance + marketing 两类合装 7,073 字符，仍在预算内，再加第三个大类就超。`codex plugin marketplace upgrade` 刷新 Git 快照；是否必须先升 `plugin.json` 的版本才能让更新生效，未验证。

## ChatGPT

两个路线：单个 Skill 在 Plugins > Skills 上传（会被扫描，风险 Skill 可能被标
Needs Review / Blocked）；或按分类打包 portable 插件 ZIP（根 `plugin.json` 声明
`"skills": "./skills/"`）提交公开插件目录，需验证过的开发者身份 + 审核。
Custom GPTs 已于 2026-12-11 退役（OpenAI Help Center“GPTs in ChatGPT”，2026-09-11
公布；FedRAMP 及获批延期的 Enterprise 工作区延至 2027-02-28），替代品是插件：
GPT 的指令变成一个 Skill，知识文件变成 reference 文件。旧的 `gpts/default/`
bundle、`tools/build_bundle.py` 和 `gpts/core/` 精简包已随之删除；`gpts/default/project-instructions.md`
的全局策略不再由任何宿主加载，其内容见 authoring-guide 的 Autonomy and escalation
ownership 一节，全文见 Git 历史。ChatGPT 没有本地文件系统和 shell，
`scripts/` 无法本地执行——目前 124 个 Skill 都没有 `scripts/`，这个问题暂时不存在。
**套餐门槛已松动，不再是硬性的 workplace-only**：Skills 2026-07-09 随 ChatGPT
Work 在 Business / Enterprise / Healthcare / Edu 上 GA；但 OpenAI 定价页自
2026-11-25 起把 Skills 列在 Free / Go / Plus / Pro 下（2026-11-25 二手核查），
而 Help Center 的 Skills 文章仍只写 workplace 套餐，个人套餐的 rollout 看似
在逐步放开。佐证：2026-11-17 上线的 ChatGPT for Sales 插件在所有套餐（含 Free）
都可用。结论：不要再以“个人套餐装不了”直接排除 ChatGPT，但**自建目录插件能否
在个人套餐上安装仍未验证**——以用户账号里实际看到的 Plugins > Skills 为准。

ChatGPT Project 没有原生 Skill 注册表：手动上传需要的 `SKILL.md`、相关
`references/` 和 Router，不要上传整个仓库或 `maintenance/`。

## Muse

没有官方安装流程、商店或版本管理。`~/workspace/custom-skills/` 是构建输出，
不是编辑目标：改 `SKILL.md` 后重新生成 `skill.yaml` 再复制过去。
`skill.yaml` 与 `SKILL.md` 各存一份 description，有漂移风险——Validator 会比对
两者，不一致就报错。124 个已于 2026-11-26 全部导入（round 4）：122 个与仓库
字节一致，仅 social-publish（v3.6 云端浏览器优先）与 social-engagement（本地
定制）保留本地版本。全量 124 个一次注册是否影响路由质量未验证。
Muse 的工具名与 Claude/Codex 不同，某个 Skill 点名了 Claude/Codex 专属工具时，
先在失败时补一条 Muse 备注，不要提前给 124 个 Skill 都写映射。

## Antigravity

文件夹式发现，无需 marketplace 文件。**Gemini CLI 已死（个人用户）**：
2026-06-18 起 Gemini CLI 与 Gemini Code Assist IDE 扩展停止为免费、Pro、Ultra
个人用户服务，继任者是 Antigravity CLI（`agy`，Go 重写）；文档里再看到
Gemini CLI 安装路径，一律按 Antigravity 理解。工作区 Skill 在
`<root>/.agents/skills/`（Antigravity 也兼容旧的单数 `.agent/skills/`）。
首选导入路线是 `agy plugin import claude`——Antigravity 官方插件文档确认该
命令从 `~/.claude/plugins/` 导入已装的 Claude Code 插件（含 Skill），
`agy plugin import gemini` 转换旧 Gemini CLI 扩展；App 2.30.0（2026-11-09）
起还能从 Claude Code、Codex、Cursor 导入整套配置（MCP、Skill、命令、
subagent、指令文件）。不行再做 `.agents/skills/` 镜像（复制或软链，软链是否被
`agy` 跟随未验证）；`npx skills add <repo> -a antigravity` 也是已知的安装
路线，写到 `.agents/skills/`。全局路径按界面不同而不同（2.0 文档是
`~/.gemini/config/skills/`，IDE 文档是 `~/.gemini/antigravity/skills/`，CLI
文档是 `~/.gemini/antigravity-cli/skills/`；有实地报告称 IDE 路径实际不生效，
以实测为准）。`references/` 在 Antigravity 文档里对应 `examples/` +
`resources/`，同名文件是否被加载未验证；先抽 2–3 个 Skill（含一个带
`references/` 的）实测。注意不要把 Gemini **App** 里的 Skills（聊天内可叠加
的指令集，2026-09-30 推出，正在取代 Gems：个人账号 2026-11 起，Workspace
商业版不早于 2027-03-01，教育版不早于 2027-06-01）当成 agent SKILL.md——
两者都接受 `SKILL.md` 导入，但 App Skills 是聊天快捷方式，不是编码 agent
的运行时；本仓库面向的是 Antigravity/Gemini CLI 这类 agent 运行时。

## Grok

只针对 Grok Build（终端 agent，`grok` CLI）。Grok Bot（网页/桌面 Bot）没有
SKILL.md 上传入口，不在本文范围。**路径已有据可查，但本仓库什么都没实测过**：
xAI 官方文档（经 2026-11 二手来源核对）称 Grok Build 从 `./.grok/skills/`
（向上查到仓库根）、`~/.grok/skills/`、各启用插件的 `skills/` 目录、`~/.grok/config.toml`
里 `[skills] paths` 指定的额外路径以及 `~/.agents/skills/` 读 Skill，也读
Claude Code 的 Skill 文件夹；`name`/`description` 可省（`name` 默认取文件夹
名，`description` 默认取首段）。但“直接读 Claude Code marketplace”的说法
在查到的资料里没有依据——资料只说读 Claude Code 的 Skill 文件夹，没说读
marketplace；`grok inspect` 仍未跑，`grok` CLI 未安装。另据二手来源，Grok
Build 处在 beta，需要 SuperGrok 级订阅（未验证）。先装 CLI 跑 `grok inspect`，
确认 marketplace passthrough 是否属实；属实则 adapter 是零文件 + 一条验证
记录；不属实则按 Antigravity 的镜像方式做 `.grok/skills/`（或共用的
`~/.agents/skills/`）。

## 跨宿主共性

- **描述预算**：124 个描述合计 22,792 字符，平均 184/个（name+description
  24,886；含 Codex 相对路径 29,956），是 Codex 默认 8,000 字符预算的约
  2.9–3.7 倍。按分类安装是主要缓解手段：每个分类单独都装得下（最大
  finance 3,676 字符），finance + marketing 两类合装 7,073 字符仍在预算内，
  再加第三个大类就超；不要为凑预算缩短 `SKILL.md` 的 description，除非实测
  证明某宿主在丢弃 Skill。Claude Code 的列表预算是上下文 1%（每条描述上限
  1,536 字符，二手来源），本仓库描述最长 190 字符，远低于该上限。
- **Router 是特殊的**：`skill-router` 的 Catalog 用 `category/skill` 命名；各宿主
  的调用拼写不同（Claude 命名空间、Codex `$name`、ChatGPT `@name`、Muse 裸名），
  适配器改了调用拼写就要同步更新 Router 的说明。
- **版本**：只有 `plugins/<category>/plugin.json` 带版本。某宿主是否要求升版本
  才拾取更新，各宿主都未验证；安全做法是每次改 Skill 都统一升版本。
- **未验证清单（不要当事实讲）**：个人套餐能否装自建
  目录插件（定价页已列 Skills，Help Center 未跟上，见 ChatGPT 一节）；Codex
  预算的字符/Token 口径与 `skills.max_context_tokens` 拉满能否装下全量；
  portable/compat `plugin.json` 接受度；Claude 1% 列表预算与 claude.ai 多余字段硬失败；Muse 的 `skill.yaml` schema
  与全量注册对路由质量的影响；Antigravity 各界面全局路径与 `references/` 加载；
  Grok 的 marketplace passthrough 与 SuperGrok 订阅要求；用户的 ChatGPT 套餐。
