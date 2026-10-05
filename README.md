# superskills

个人 AI Skills 仓库。只保存**会改变 Agent 决策的可复用规则、工作流和领域知识**，并用路由、按需加载和可验证完成边界控制上下文质量。

## Runtime model

```text
user task
-> inspect available context and tools
-> choose one primary Skill
-> read SKILL.md and only needed references
-> execute authorized, reversible work
-> verify and self-correct
-> escalate only a true blocker or consequential final step
-> report the outcome
```

核心原则：

- **specific before generic**：领域 Skill 优先于通用方法。
- **one primary skill**：不按关键词堆叠多个 Skill。
- **action before interrogation**：先读取现有资料、使用可用工具并完成已授权的可逆工作；只把真正需要用户决定的阻塞点升级给用户。
- **approval at the boundary**：需要批准的不可逆或高影响动作，先准备好可审查结果，再在最后边界请求批准。
- **execution is not planning**：任务很长或步骤很多，不代表 `project-planner` 是交付物；用户要求执行时，应由领域 owner 执行并在内部规划。
- **progressive disclosure**：默认只读 `SKILL.md`；深层知识按需读 `references/`。
- **maintenance is not runtime**：behavioral eval、来源和少量设计决策只放 `maintenance/`，不随任何安装包分发。
- **single source of truth**：同一规则只保留一个 owner。
- **evidence before claims**：运行、视觉、存档、导出和发布结论必须有匹配证据，验证强度与改动风险相匹配。

## Structure

```text
superskills/
├── plugins/<category>/
│   ├── plugin.json                  # 该分类的名称、版本、描述（唯一手写处）
│   └── skills/<skill>/
│       ├── SKILL.md
│       └── references/              # optional runtime depth
├── maintenance/<category>/<skill>/  # optional evals/sources/decisions，不进任何安装包
├── .claude-plugin/marketplace.json  # 生成：Claude Code
├── .agents/plugins/marketplace.json # 生成：Codex / ChatGPT
├── gpts/kukutx/                     # ChatGPT Project / GPT 的指令与打包入口
├── docs/authoring-guide.md
├── templates/skill-template.md
├── tools/
├── tests/
└── .github/workflows/
```

分类是安装单位：每个 `plugins/<category>/` 是一个标准插件，Skill 位于它的 `skills/<skill>/SKILL.md`。这是 Claude Code、Codex 和 `skills` 安装器都能默认发现的结构，宿主直接从仓库安装，没有导出副本。Skill 仍用 `category/skill` 作为路由 ID。

**唯一完整 Skill catalog**：`plugins/meta/skills/skill-router/SKILL.md` 的 `## Catalog` 表格。不要在 README、Project Instructions 或其他文件复制完整路由表。

## Install

按分类安装，只装当前项目或工作区用得到的分类；不要把全部分类装进每个项目。`<category>` 是 `plugins/` 下的目录名。

| 宿主 | 安装方式 |
| --- | --- |
| Claude Code | `claude plugin marketplace add Kukutx/superskills`，再 `claude plugin install superskills-<category>@superskills` |
| Codex（CLI / App / IDE） | `codex plugin marketplace add Kukutx/superskills`，再 `codex plugin add superskills-<category>@superskills` |
| Cursor、Gemini CLI、Copilot 等 | `npx skills add Kukutx/superskills --skill <skill>`（[`skills`](https://github.com/vercel-labs/skills) 安装器，按 Skill 名称选择） |
| claude.ai 网页 / 桌面 | `python tools/package_web_skills.py` 生成 `dist/claude-web/<skill>.zip`，在 Customize > Skills 逐个上传；每个 Release 也附带这些 ZIP |
| ChatGPT Project / GPT | 没有原生 Skill 注册表，使用下面的 runtime bundle 和 Router |

有原生注册表的宿主只按 `description` 触发 Skill，不加载 Router 和 `gpts/` 下的 Project Instructions。OpenAI 文档说明打包在插件里的 Skill 也能在 ChatGPT 的 Chat 和 Work 中使用；本仓库只验证过 Codex 侧的安装，ChatGPT 网页端的启用流程以官方当前说明为准。

更新：Claude Code 先 `claude plugin marketplace update superskills`，再卸载并重新安装对应插件（本地文件夹源实测 `claude plugin update` 会切到旧快照）；Codex 用 `codex plugin marketplace upgrade`，本地源同样移除后重新添加；`skills` 安装器用 `npx skills update`。Codex 按 `plugin.json` 的 `version` 缓存，发布新内容前先提升版本。

## Validation

工具统一使用 Python 3.14。

```bash
python -m unittest discover -s tests -v
python tools/validate_repo.py
python tools/export_behavioral_evals.py --check
```

Validator 检查目录形状、入口文件名、frontmatter（只允许 `name` 和 `description`；`description` 不超过 200 字符且是合法的 YAML 纯文本）、Skill 名称全仓唯一、插件清单与版本一致、两份 marketplace 是否过期、Router Catalog 完整性、真实 Markdown 引用、runtime 不引用 maintenance，以及 behavioral eval 路径完整性。

新增或删除分类、修改 `plugin.json` 后重新生成 marketplace：

```bash
python tools/build_manifests.py
```

## Live replay

上面的检查只证明结构。要看真实模型的行为，把 behavioral eval 表格构建成可回放套件，再交给 Claude Code 自带的 eval 运行：

```bash
python tools/build_live_evals.py
claude plugin eval dist/live-evals --ablation none --runs 1 --max-cost-usd 2 --no-publish --case "<glob>"
```

`dist/live-evals/` 是生成物：全部 Skill 组成的一个插件加上每个可回放用例。只有 Prompt 是单句引用的行会生成用例，分三类：

| tag | 来源 | 断言 |
| --- | --- | --- |
| `route` | Router 表格里的行，或 Primary 指向另一个 Skill 的行 | 只给原话，预期 Skill 被调用，`Must avoid` 点名的相邻 Skill 未被调用 |
| `behavior` | Primary 就是该表格所属 Skill 的行 | 提示里点名 Skill，由评审模型按 `Must avoid` 判定回答 |
| `reference` | Primary 是 reference 文件的行 | 提示里点名 Skill，预期 reference 被读取 |

Primary 属于 `research` 分类的 `route` 用例另带 `web` tag 和联网工具：没有搜索能力的会话不会把“找东西”路由给调研类 Skill，所以回放它们时要加 `--allow-tools WebSearch WebFetch`，否则结果只能记为未验证。

每个用例是一次真实模型会话，消耗运行者自己的 Claude 用量（订阅额度或 API 费用）。只回放受改动影响的用例（`--case` 只接受一个 glob，`--tag` 可重复），不要把全量回放当作日常检查。结果按模型和宿主分别记录，一次已观测到的失败不因为重跑通过而抹掉。

## Staying current

`python tools/check_sources.py --online` 读取所有 `maintenance/**/sources.md`，报告超过复查期限、页面已不存在或仓库已归档的来源。`.github/workflows/freshness.yml` 每月运行一次，有结果时创建或更新一条维护 issue，全部处理后自动关闭；它只提醒复查，不自动改写任何 Skill。

## Build a ChatGPT runtime bundle

不要默认上传整个仓库。构建只包含 Project Instructions、Router、选中的 Skill 与 reference 的最小包：

```bash
python tools/build_bundle.py \
  --profile gpts/kukutx \
  --skill writing/resume-writing \
  --reference development/godot-project-systems:ui-ux
```

输出的 `manifest.json` 记录源提交、文件哈希、字节数和粗略 Token 预算，并保证不包含 `maintenance/`。

## Releases

发布前把所有插件提升到同一个新版本并重新生成 marketplace：

```bash
python tools/build_manifests.py --version 1.2.0
```

`.github/workflows/release.yml` 手动输入的版本标签必须与该版本一致（`v1.2.0`）。它先运行测试、Validator 和 eval export，再构建 claude.ai 上传用的 Skill ZIP 和一个 ChatGPT Runtime Bundle，连同 SHA-256 校验文件一起发布。已存在的版本不会被覆盖。

同仓库 PR 合并后，`.github/workflows/delete-merged-branch.yml` 会自动删除已合并的 head branch。

## Growth rule

新增 Skill/reference 前先检查：

1. 任务是否会重复？
2. 是否存在值得长期保留的独特决策规则？
3. 现有 owner 是否已经覆盖？
4. 新文件是否真的改变行为或明显减少 runtime context？
5. 能否用一个真实 behavioral eval 证明新边界有价值？
6. 新规则是否只是重复全局的规划、询问、批准或工具使用行为？

答案不明确，就不要新增。

## License

本仓库使用 [MIT License](LICENSE)。允许使用、复制、修改和分发，但必须保留原版权和许可证声明；软件按原样提供，不附带担保。
