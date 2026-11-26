# Multi-agent adapters

一份 `SKILL.md`，多个宿主。`SKILL.md` frontmatter 只保留 `name` + `description`
（Agent Skills 规范），不加任何厂商字段；每个宿主的特殊配置放在它自己的
adapter sidecar 里，由生成器从 `SKILL.md` 派生。`SKILL.md` 是唯一事实来源，
sidecar 永远不手改。

## 状态总表

| 宿主 | 优先级 | 安装 | 触发 | Adapter | 状态 |
| --- | --- | --- | --- | --- | --- |
| Claude Code | 高 | `claude plugin marketplace add Kukutx/superskills`，再 `claude plugin install superskills-<category>@superskills`；或复制到 `~/.claude/skills/` | description 自动触发，`/<skill>`，插件内 `/superskills-<category>:<skill>` | 几乎无；仓库本身就是按 Claude 插件结构建的 | ✅ 已验证安装 |
| Codex | 高 | `codex plugin marketplace add Kukutx/superskills`，再 `codex plugin add superskills-<category>@superskills`；或 `.agents/skills/` | description 自动触发，`/skills` 选择器，`$<skill>` | `agents/<category>/<skill>/openai.yaml`（与 ChatGPT Skills/插件共用） | ✅ CLI 已验证；全量 105 个描述约 20,000 字符，超过约 8,000 字符的目录预算，按分类安装 |
| ChatGPT | 高 | Plugins > Skills 上传单个 Skill，或提交公开插件目录（ZIP + 审核）；无本地文件夹 | description 自动触发，`@<skill>` | 同上 `agents/.../openai.yaml`；按分类的 portable `plugin.json`（`"skills": "./skills/"`） | ◐/❌ **未验证**：网页端启用流程从未实测；自建 Skill 只列在 Business / Enterprise / Healthcare / Edu 套餐下，需先确认用户套餐 |
| Muse | 高 | 无官方安装流程；本地把 `plugins/<category>/skills/<skill>/`（`SKILL.md` + `skill.yaml`）复制到 `~/workspace/custom-skills/<skill>/` | 对话中按 description + `triggers:` 匹配；无斜杠命令 | `tools/generate_skill_yaml.py` 生成 `skill.yaml`（name/title/description/category/include_in_prompt/triggers） | ◐ 已导入 development + personal + meta（17 个）；其余 88 个批量导入未验证 |
| Antigravity (Gemini) | 偶尔 | 工作区 `<root>/.agents/skills/`（向上查到仓库根）；全局 `~/.gemini/config/skills/`；或 `agy plugin import claude` | description 自动触发，`/<skill>` | 镜像/软链 `plugins/*/skills/*` → `.agents/skills/`；先试 `agy plugin import claude`，可能不需要镜像 | ◐ 官方文档已读，`agy plugin import claude` 行为未验证；CLI 与 IDE 的全局路径可能不同 |
| Grok (Grok Build) | 低 | `.grok/skills/`、`~/.grok/skills/`、`~/.agents/skills/`；据称可直接读 Claude Code marketplace | `/<skill>`，默认自动触发 | 可能不需要；先用 `grok inspect` 核实 passthrough 是否属实 | ❌ **未验证**：无官方文档核对，`grok` CLI 未安装；最低优先级 |

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

与 ChatGPT Skills/插件共用 `agents/openai.yaml`。OpenAI 官方 Skills 文档确认：Skill 就是一个含 `SKILL.md` 的文件夹，`agents/openai.yaml` 是可选的展示、策略与依赖 sidecar；Codex 从 `.agents/skills/`（项目/用户级）等位置扫描 Skill，`$<skill>` 显式调用或按 description 自动触发。描述目录预算约 2% 上下文或 8,000 字符（窗口未知时），105 个 Skill 的描述合计约 20,000 字符，全装大概率会被静默丢弃一部分；按分类安装，不要一次装全部。`codex plugin marketplace upgrade` 刷新 Git 快照；是否必须先升 `plugin.json` 的版本才能让更新生效，未验证。

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
**先确认用户的 ChatGPT 套餐**：自建 Skill 只列在 Business /
Enterprise / Healthcare / Edu 套餐下，Free / Go / Plus / Pro 未列入。

ChatGPT Project 没有原生 Skill 注册表：手动上传需要的 `SKILL.md`、相关
`references/` 和 Router，不要上传整个仓库或 `maintenance/`。

## Muse

没有官方安装流程、商店或版本管理。`~/workspace/custom-skills/` 是构建输出，
不是编辑目标：改 `SKILL.md` 后重新生成 `skill.yaml` 再复制过去。
`skill.yaml` 与 `SKILL.md` 各存一份 description，有漂移风险——Validator 会比对
两者，不一致就报错。全量 105 个一次注册是否影响路由质量未验证；目前只导入了
development + personal + meta 三类（17 个），扩到全量前先试点 1–2 个 Skill。
Muse 的工具名与 Claude/Codex 不同，某个 Skill 点名了 Claude/Codex 专属工具时，
先在失败时补一条 Muse 备注，不要提前给 105 个 Skill 都写映射。

## Antigravity

文件夹式发现，无需 marketplace 文件。先试 `agy plugin import claude` 对现有
`.claude-plugin/marketplace.json` 是否生效；不行再做 `.agents/skills/` 镜像
（复制或软链，软链是否被 `agy` 跟随未验证）。全局路径按界面不同而不同
（App 是 `~/.gemini/config/skills/`，CLI/IDE 可能不同），以实测为准。
`references/` 在 Antigravity 文档里对应 `examples/` + `resources/`，同名文件
是否被加载未验证；先抽 2–3 个 Skill（含一个带 `references/` 的）实测。

## Grok

只针对 Grok Build（终端 agent，`grok` CLI）。Grok Bot（网页/桌面 Bot）没有
SKILL.md 上传入口，不在本文范围。**什么都没验证过**：官方文档未打开，
`grok` CLI 未安装。先装 CLI 跑 `grok inspect`，确认“自动读 Claude Code
marketplace”是否属实；属实则 adapter 是零文件 + 一条验证记录；不属实则按
Antigravity 的镜像方式做 `.grok/skills/`（或共用的 `~/.agents/skills/`）。

## 跨宿主共性

- **描述预算**：105 个描述合计约 20,000 字符，平均 190/个。按分类安装是主要
  缓解手段；不要为凑预算缩短 `SKILL.md` 的 description，除非实测证明某宿主
  在丢弃 Skill。
- **Router 是特殊的**：`skill-router` 的 Catalog 用 `category/skill` 命名；各宿主
  的调用拼写不同（Claude 命名空间、Codex `$name`、ChatGPT `@name`、Muse 裸名），
  适配器改了调用拼写就要同步更新 Router 的说明。
- **版本**：只有 `plugins/<category>/plugin.json` 带版本。某宿主是否要求升版本
  才拾取更新，各宿主都未验证；安全做法是每次改 Skill 都统一升版本。
- **未验证清单（不要当事实讲）**：个人套餐能否装
  目录插件；Codex 8,000 字符预算与 portable/compat `plugin.json` 接受度；
  Claude 1% 列表预算与 claude.ai 多余字段硬失败；Muse 的 `skill.yaml` schema
  与全量注册预算；Antigravity 各界面全局路径与 `references/` 加载；
  Grok 的全部内容；用户的 ChatGPT 套餐。
