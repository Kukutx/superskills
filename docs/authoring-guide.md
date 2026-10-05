# Skill Authoring Guide

只保存**会改变 Agent 决策、执行或验证方式**的内容。

## Default structure

普通 Skill：

```text
plugins/<category>/skills/<skill>/SKILL.md
```

只有复杂 Skill 才增加：

```text
plugins/<category>/skills/<skill>/references/   # runtime 按需读取
maintenance/<category>/<skill>/                 # 不随任何安装包分发
```

不要默认创建 prompt template、examples、changelog、compatibility stub 或重复 README。

入口文件名固定为大写 `SKILL.md`，`name` 必须等于目录名，并且在整个仓库唯一：宿主按裸名注册 Skill，分类只是安装单位，不是命名空间。frontmatter 只用 `name` 和 `description`。

## Description

多数宿主在触发前只看到 `description`，它决定 Skill 会不会被用到。写法固定为三段，按重要性排序：

```text
<能力，把用户会说的关键词放在最前面>. Use when <真正需要它的任务>, not for <最容易误触发的相邻任务>.
```

- 不超过 200 字符：这是 claude.ai 上传自定义 Skill 的上限，也是所有宿主里最严的一个。
- 关键词前置：Codex 在 Skill 列表超出预算时会先截短描述，被截掉的应当是排除条件而不是能力本身。
- 只写纯文本，不出现 `: ` 和 ` #`：宿主用真正的 YAML 解析 frontmatter，这两种写法会让整个 Skill 加载失败。
- 写触发边界，不写正文里的工作方式；不堆同义词，也不写“任何相关任务都必须使用”。
- 根据没触发的例子改 description 时，把它们归纳成意图类别，不把那些原话逐条写进去；用来改写的例子和用来验收的例子分开。
- 每条排除都对照这个 Skill 本来该服务的任务检查一遍，防止排除条款把自己该接的任务也挡在外面；相邻的两个 Skill，排除要两边对称地写。
- 中文场景的 Skill 可以直接写用户会说的中文词。

改了 `description` 就回放受影响的 `route` 用例（见 Behavioral evals）；没有回放时，只能说结构通过，不能说触发行为已验证。

## Distribution

分类是安装单位。每个 `plugins/<category>/` 是一个标准插件：`plugin.json` 是它的名称（`superskills-<category>`）、版本和描述的唯一手写处，`skills/` 下一层就是 Skill。所有插件共用一个版本。

`.claude-plugin/marketplace.json`（Claude Code）和 `.agents/plugins/marketplace.json`（Codex / ChatGPT）由 `python tools/build_manifests.py` 生成，不手改；新增、删除分类或改了 `plugin.json` 后重新生成，Validator 会拒绝过期的清单。发布前用 `python tools/build_manifests.py --version <x.y.z>` 统一提升版本。

claude.ai 网页端用 `python tools/package_web_skills.py` 为每个 Skill 生成一个上传用 ZIP。ChatGPT Project / GPT 没有原生注册表，继续用 runtime bundle 加 Router。

有原生 Skill 注册表的宿主不会加载 Router 或 `gpts/` 下的 Project Instructions，网页端上传的也只有 Skill 自己的目录。因此 Skill 正文必须自足：不能写“按全局规则处理”，也不能依赖同一分类里的另一个 Skill 一定已安装。

## Minimal `SKILL.md`

通常只需要：

1. YAML `name` + routing-quality `description`
2. Scope / Use：它真正拥有哪类任务
3. Durable decision rules / invariants
4. Domain inputs / true blockers
5. Reference routing：复杂 Skill 才需要
6. Constraints / anti-patterns
7. Validation / completion boundary

不要用 Purpose、Role、System Prompt 多次表达同一件事。

## Agentic baseline

新的高能力 Agent 不需要每个 Skill 都重复教它“先计划、先询问、先确认、再执行”。这类通用行为由 `gpts/kukutx/project-instructions.md` 统一拥有。

Skill 应优先保存：

```text
requested outcome ownership
domain invariants / source of truth
what facts materially change the decision
what the agent may safely infer or discover
real blocker / irreversible boundary
what evidence proves completion
```

而不是：

```text
generic plan-first ritual
generic permission checks
generic tool-use instructions
step-by-step prose that a capable agent can infer
```

如果用户要求执行，Skill 应帮助 Agent 执行，不应因为任务复杂就把交付物偷偷改成计划。多步骤工作本身不是 `project-planner` 的路由条件。

模型、API、工具和平台能力会变化。只有当它们会改变当前决策时才在执行阶段验证；不要把短期模型行为、版本号或固定工具清单写成长期 runtime truth。

## Writing

- **正向写目标行为。** 禁令会把被禁止的行为带进上下文，反而更容易被做出来。先写“要做成什么样”；只有无法正向表达的硬护栏才写成禁令，并且和正向目标放在一起。
- **写原因，不堆大写的 MUST / NEVER。** 模型知道一条规则为什么存在，才能处理规则没列到的情况；满篇强制词只会让每一条都失去分量。
- **完成条件既要能判定，又要有力度。** “每个被改动的模型都已核对”会逼出彻底的工作，“给出改动清单”不会。需要穷尽时，把“每一个”写进条件；条件含糊就会提前收工。
- **成本来自被触发的动作，不来自字数。** “再核对一遍”“尽可能全面”这类措辞会让模型重复读取和检查；常驻加载的内容（`description`、Project Instructions）要能说出它避免了什么具体问题。
- **逐句做 no-op 检验。** 删掉这句，模型的默认行为会变吗？不会就整句删掉。两个人对此有分歧，说明对默认行为的判断不同，用回放解决，不靠争论。
- **只写环境里查不到的东西。** 脚本名、配置项、目录结构能直接查到，写进 Skill 只是一份会过期的副本。值得写的是未成文的约定、取舍的原因、配置不会承认的坑。
- **用一个现成的词承载一整类行为。** 例如用 `tight` 表示“快、确定、开销小”，全文重复这个词而不是重复整句解释；自造词要先定义，成本更高。
- **一个概念的定义、规则和例外放在同一个标题下。** 每个分支都要用的内容留在入口，只有部分分支用到的才放进 reference。
- **改进来自读运行轨迹，不只看最终输出。** 多次运行里模型都在重复做同一件机械的事，说明它应该变成脚本；某段规则让模型绕远路，就删掉那段再看结果。
- **外部工具的事实要带出处。** 记录某个工具或平台行为的内容，写明来源和核对时的版本；文档和实际运行结果不一致时，以实际结果为准并更新记录。
- **过期内容要标出来。** 已知过期但暂时保留的内容，写明过期的范围并指向权威来源；没有资料支持的用法写“未核实”并指明去哪查，不从相近的语言、平台或版本外推。
- **通读草稿找“没写的决定”。** 模型遇到没写的地方会自己选一个；每个这样的空白要么明确填上，要么写成一个真实的分支。
- **出了问题先分类再动手。** 先排除和规则无关的偶发问题，以及模型没有读到必要证据的情况。规则缺失或写错了，改规则；规则是对的但没有被执行，调整它的措辞和位置，或做成确定性检查，不再叠一条新规则。
- **同一类错误反复出现时，先问能不能做成确定性检查。** 能写成 lint、测试、CI 或 hook 的就不写成规则文字；只有真正需要判断的才写进 Skill。
- **需要另一个 Skill 时写明确的调用，一次一个。** 正文必须自足：只有缺了就做不下去的硬依赖才点名另一个 Skill，其余只说明需要哪种能力。
- **派给子代理的说明里写明它已经是子代理。** 要它直接完成任务，不再调用同名 Skill 或派生新的代理；不写死某个宿主的工具名或代理类型。

## Routing

唯一完整 Skill catalog：

```text
plugins/meta/skills/skill-router/SKILL.md
```

Router 服务于没有原生注册表的宿主（ChatGPT Project / GPT）。有注册表的宿主靠每个 Skill 的 `description` 自行触发，所以路由边界必须同时体现在相关 Skill 的 `description` 里，而不只写在 Router。

原则：

- specific domain > generic method > meta helper；
- 一次先选一个 primary Skill；
- secondary Skill/reference 只处理可分离子问题；
- 不按关键词机械匹配；
- prompt optimizer 只在 prompt 本身是交付物时使用；
- execution request 不因为“步骤很多”自动变成 planning request。

Catalog 只维护在 Router 的 `## Catalog` 表格中。新增、删除或重命名 Skill 时，每个非 Router Skill 必须在该表格**恰好出现一次**。

## Autonomy and escalation ownership

全局的自治、询问、批准和 scope 规则由 `gpts/kukutx/project-instructions.md` 持有。普通 Skill 不要复制一套通用的“信息不足就询问”或“执行前先确认”长文。

领域 Skill 只补充该领域真正会改变结果的输入和阻塞条件，例如：

- 简历需要真实职位、日期、经历和目标岗位；
- 技术设计需要数据所有权、一致性和迁移约束；
- 雕刻需要材料、尺寸和实际工艺。

按缺口类型处理：

```text
supplied/discoverable fact -> inspect or retrieve it
harmless reversible choice -> choose the smallest convention-aligned default
user-only truth / preference -> ask only when it materially blocks correctness or direction
consequential irreversible action -> prepare the concrete result first, then escalate at the boundary
```

好的边界应同时避免：

```text
核心事实完全未知却伪造
公开/已提供信息仍让用户重复提供
可逆工作明明能继续却停在询问或计划
真正不可逆的高影响动作却静默替用户决定
```

剩余不确定性如果不会合理地改变主方向、事实正确性或不可逆操作，就继续执行，不追求无意义的绝对确定。

## When to split a reference

只有存在真实 decision boundary 才拆。例如：

```text
combat correctness != game feel
movement/physics != camera framing
AI/navigation != procedural generation
save/migration != inventory runtime mechanics
sprite asset production != engine runtime animation
verification != performance != release
```

Reference 至少应满足一项：

- 只有部分任务需要，拆分明显减少 runtime context；
- 有独立 owner/validation；
- 合并会让路由或 source-of-truth 模糊。

**拆分是移动 ownership，不是复制内容。** 主 `SKILL.md` 只保留路由和跨域 invariant。每个 runtime reference 必须通过正式 Markdown 链接或明确的 Markdown code path 从主入口可发现。

不要嵌套 `references/` 子目录；保持一层、可路由、可验证。

## Maintenance standard

Runtime 不加载 `maintenance/`。它与 `plugins/` 平级，按 `maintenance/<category>/<skill>/` 对应到 Skill，所以不会进入插件缓存、网页端 ZIP 或 runtime bundle；runtime 文件也不得链接到它。

只使用：

```text
behavioral-evals.md   # routing/ownership/autonomy review fixtures
sources.md            # substantial upstream/source inventory
decisions.md          # only when current rationale cannot be inferred
```

Git history 已经是 changelog；不要维护版本流水账。

时效性 API、插件、版本、模型行为和市场快照在执行时重新验证，不写成永久 runtime truth。

较重要的来源记录应包含：

```text
canonical URL
它支持的决策或边界
最后复查年月
```

登记表使用 `Source | Canonical URL | Used for | Last reviewed` 列，`Last reviewed` 写 `YYYY-MM`。`tools/check_sources.py` 和每月的 freshness workflow 据此提醒复查；复查后只在决策确实变化时改 Skill，再更新年月。

来源清单用于可追踪维护，不是运行时推荐榜单。

## Behavioral evals

当新增或修改 ownership、autonomy 或 blocker boundary 时，加**最少量**能防真实回归的例子。测试应证明“为什么这个边界存在”，而不是给每个关键词写一个例子。

唯一格式：

```markdown
| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| example-001 | 用户任务 | `category/skill` | 可选 | 禁止行为 |
```

列名必须严格使用 `ID`、`Prompt`、`Primary`、`Secondary`、`Must avoid`。不维护旧列名兼容。显式 `ID` 在整个仓库中必须唯一。

导出为机器可读 JSONL：

```bash
python tools/export_behavioral_evals.py --check
python tools/export_behavioral_evals.py --output dist/behavioral-evals.jsonl
```

这些文件仍是人工/Agent review fixtures，CI 只验证结构、路径和可导出性；它不等于真实模型已经通过语义评测。

真实回放用 `python tools/build_live_evals.py` 生成 `dist/live-evals/`，再运行 `claude plugin eval dist/live-evals --ablation none --runs 1 --case "<glob>"`。只有 Prompt 是单句引用（`“……”`）的行会成为可回放用例，按 Primary 分三类：

```text
route      Router 表格里的行，或 Primary 是另一个 Skill
           -> 只给原话；预期 Skill 被调用，Must avoid 点名的相邻 Skill 未被调用
behavior   Primary 就是该表格所属的 Skill
           -> 提示里点名 Skill；评审模型按 Must avoid 判定回答
reference  Primary 是 reference 文件名
           -> 提示里点名 Skill；预期 reference 被读取
```

```text
negative   Primary 写 none
           -> 只给原话；Must avoid 点名的 Skill 都不应被调用
```

想让一条边界能被真实回放，就按这个形状写，并让原话自带任务所需的材料：`“帮我优化这段 prompt。”` 在回放里没有 prompt 可优化，模型只会反问，测不到路由。需要描述上下文才成立的行（已上传的文件、之前的决定）保持原样，只做人工审阅。

写用例和判定结果时注意：

- **像真人会说的话，而且有分量。** 模型只在自己不容易直接完成的任务上才去查 Skill；一句话就能答完的玩具请求，描述写得再好也不会触发。带上真实的细节：文件、背景、口语化的说法。
- **近邻反例最有价值。** `negative` 行要选和这个 Skill 共享关键词、实际上该由别处处理的请求；明显无关的请求测不出任何东西。
- **新 Skill 和新规则要有对照组失败的用例。** 用 `--ablation with-without` 加一组不装 Skill 的对照；一条标准在两组里都通过，说明它不区分有没有这个 Skill，不能作为新增的理由。
- **用例本身要经得起检查。** 每条用例独立、不改变环境；预期结果是确定的，不依赖会变化的现状；写的人先自己做一遍，并且不照着被测 Skill 的正文来出题。
- **通过率低时按顺序排查。** 先看描述是否说清了何时用，再看输入是否缺说明、返回的内容是否过多或过少、出错时的提示能否让模型知道下一步；同时看运行轨迹里模型在哪一步表现出困惑。
- **通过要有证据。** 一条用例判为通过，必须有直接证据说明任务真的完成了；无法验证的判据不算通过。判完之后再审一遍用例本身：哪些判据太弱、哪些重要结果没有任何用例覆盖。
- **多次运行的结果分五类看。** 有没有 Skill 都通过的（不区分）、都失败的、只有装了 Skill 才通过的、装了 Skill 反而失败的、时过时不过的（方差大）。只有第三类说明 Skill 有用，第四类说明它在帮倒忙。挑 `description` 时看验收用例的分数，不看调参用例的分数。
- **用例不要求模型报告它观察不到的结果。** 任务里写“假设它成功了”“填一个合理的值”，是在奖励编造。
- **判据不奖励“用了 Skill”，也不奖励产出的篇幅。** 用例的原话不使用 Skill 自己的术语；Skill 规定了输出形状时，用例要断言这个形状。`negative` 用例除了“没有触发”，还要看回答是否给出了正确的下一步。
- **验收用例至少五条、彼此能区分。** 只有分出胜负的用例才算数；增加同一用例的重复次数不能代替增加用例。用例引用的样例文件必须已被 Git 跟踪。
- **先量噪声，再谈改善。** 同一用例、同一配置重复运行时结果翻转的比例是噪声下限；改动带来的差异小于它，不能说有改善。
- **在验收用例上严格变好才接受改动。** 持平不算；跳过验收直接接受的改动要在说明里写出来。对比两个版本时按用例 ID 一一配对、用同一批用例，报告里给出最差的那条而不只是通过率。同一用例重复运行不算独立样本。
- **改已有 Skill 时用新旧版本配对回放。** 每条用例归为四类：变差、一直失败、变好、一直通过。变差的优先处理。
- **判定的一方不能先看过参考答案。** 作答或判定用例的上下文如果已经见过预期结果，验收就被污染了；需要时换一个全新的上下文来做。
- **调参用例和验收用例分开。** 改 Skill 时参照的用例和最后下结论用的用例不是同一批：前者变好、后者不变，说明改动只是贴合了那几个用例。一轮只改一个假设。
- **判据写成能从运行轨迹里直接检查的信号。** 例如“先出现复现命令和它的失败输出，之后才出现任何原因推断”；不写“是否符合 SKILL.md 的某一节”这类对文本结构的检查。

评估后决定不加的 Skill、规则或需求，连同理由写进对应的 `decisions.md`，避免以后重复提出。

`reference` 用例断言的是“这个子问题确实需要读这份 reference”。如果入口 `SKILL.md` 已经足以回答，或者缺了数据模型只会先反问，就写成 `behavior` 用例（Primary 写 Skill 路由，reference 放进 Secondary）。

Primary 属于 `research` 分类的 `route` 用例会带 `web` tag 和联网工具，回放时加 `--allow-tools WebSearch WebFetch`；没有搜索能力的会话不会把“找东西”交给调研类 Skill，那种结果不能算作路由失败。

每个用例是一次真实模型会话，消耗运行者自己的用量。改了 `description`、路由或 reference 边界后只回放受影响的用例，把模型、宿主和结果分开记录；一次已观测到的失败不因为重跑通过而抹掉。

优先测试：

- 最容易混淆的相邻 Skill/reference；
- domain vs generic method；
- correctness vs polish；
- asset/source vs runtime truth；
- 核心事实不足应询问 vs 信息已提供/可发现不应重复询问；
- 已授权可逆工作应继续 vs 真正不可逆边界应升级；
- execution request vs roadmap deliverable；
- 小改动的必要验证 vs 无意义的过度测试；
- 一次性任务 vs repeated SOP/process。

## Dependencies

优先：

```text
existing project pattern
-> native platform/framework capability
-> focused dependency only if recurring pain remains
```

采用第三方前检查当前 compatibility、maintenance、license、overlap、source-of-truth、upgrade/removal cost。

引入第三方 Skill 前按下面的清单审查。

读完正文和脚本，确认它不与本仓库的规则相反。审查期间不运行它的任何脚本，只用只读命令；没有跑扫描工具就明说，并相应降低结论的把握。

- **藏着的内容**：frontmatter 和参数默认值里的隐藏文本（HTML 注释、零宽字符、形似字符、长串 base64）、隐藏文件和压缩包、预编译文件。
- **它会改动或接入什么**：自带的 hook 和宿主设置文件、改写依赖来源的包管理配置、持久化入口（定时任务、shell 配置、启动钩子）、往 `AGENTS.md` 这类指令文件里写内容、自动安装扩展、全局安装、按端口结束进程、运行时从远端的默认分支拉内容（没有固定到某个提交）、读取其它 Skill 或 Agent 的记忆。
- **它预先放行了什么**：frontmatter 里的 `allowed-tools` 等于预先批准这些命令，逐项看它放行了什么，放行的应当是完整的命令而不是一个命令前缀；运行时用 `npx` 之类现拉现跑的工具或 MCP 服务，等于执行没审过的代码；带遥测钩子的要看清它上报什么、怎么关；有没有环境变量能不经确认就跳过它自己写明要停下来的步骤。
- **说的和做的是否一致**：`description` 说的、它声明要用的权限、脚本实际调用的，三者是否一致；同一个脚本有多个平台版本时，各版本做的事是否一样；`description` 里堆满宽泛的触发词是在抢别的 Skill 的路由。
- **随附脚本**（逐个读完，不运行）：
  - 执行了什么：现场编译或注入原生代码；给第三方库打运行时补丁；自动安装依赖；“验证”脚本真的去调付费接口；名为“探测”“校验”的脚本会发写请求或留下副作用（判断一个请求是不是只读，看它的地址和参数，不只看方法名）；依赖本机当前登录的账号和默认项目；把外来的数据直接拼进 SQL、shell 命令或代码字符串，或者直接执行传进来的命令串和源文件；调用云账号的取密钥接口；写请求超时之后直接重发写入，而不是先回读。
  - 改了什么：往固定的共享临时路径写文件；改写本机的 CLI 配置；原地改写工程文件时有没有预览或备份、是否只改它声明的目标；递归删除远端路径之前有没有先列出对象。
  - 往外送了什么：把整个目录打包上传而没有排除项，或者排除项只有 `.env` 一类、漏掉项目自己的密钥目录；上传到写死的第三方地址；输出里带密钥明文；把令牌放在命令行参数里；凭据发往的地址能被环境变量改写。
  - 它的报告能不能信：超时被报成成功；吞掉异常；缺凭据或被拒绝时照样以成功退出；没有任何检查内容却打印“通过”；把读取出错吞成空结果，“出错”和“确实没有”就分不开了；结果被数量上限截断却不提示；命令以非零退出，只因为输出还能解析就当成功。
- **示例代码**：示例自身的不安全写法（跨域通配加凭据、明文令牌、不设防护属性的 Cookie）不随规则一起带进来。
- **许可**：许可是否允许复制和改写。不允许的只学做法，不拷贝内容；允许的按许可要求保留声明。许可只写“使用须遵守与某公司的协议”的，按不允许处理。

结论分三档：可用；可用但有敏感行为（必须是有文档、必要、有界、用户可控的）；不用。说不清用途的高风险行为，不因为来源名气或工具打分放行。豁免或信任的依据不能来自被审查对象的自述。

## Anti-noise

不要为了“更完整”加入：

- 重复 System Prompt / role prose；
- 重复的 plan/ask/confirm/tool-use 通用循环；
- 一次性普通 examples file；
- changelog；
- retired/compatibility stub；
- runtime 中的 source/tool inventory；
- 同一规则在多个 reference 复制维护；
- 容易过期且不改变长期决策的版本、模型或工具列表。

## Validation

仓库工具统一使用 Python 3.14。修改后运行：

```bash
python -m unittest discover -s tests -v
python tools/validate_repo.py
python tools/export_behavioral_evals.py --check
```

Validator 负责：

- 扫描所有 `SKILL.md`，并拒绝错误层级或错误大小写的入口；
- frontmatter 只有 `name` 和 `description`，`description` 不超过 200 字符且是合法 YAML 纯文本；
- folder naming，Skill 名称全仓唯一；
- 插件与 Skill 目录形状：插件目录只有 `plugin.json` 和 `skills/`，Skill 目录只有 `SKILL.md` 和 `references/`；
- `plugin.json` 的名称、描述和统一版本，以及两份 marketplace 是否过期；
- runtime reference 必须是一层 Markdown，并通过真实链接/code path 从入口可发现；
- `maintenance/<category>/<skill>/` 必须对应现存 Skill，只允许当前规范文件，runtime 文件不得链接到它；
- 只解析 Router `## Catalog` 表格，检查完整、重复和 stale route；
- behavioral eval 必须使用唯一 canonical 表格格式；
- behavioral eval 中显式 Skill route 与本地 reference 仍存在；
- 标准 Markdown 链接及 code path 无 dead link 或仓库逃逸；
- 对异常大的 runtime entrypoint/reference 给出非阻塞 advisory。

结构规则能自动检查时优先写进 Validator，并同时增加 Validator 自身的回归测试。

## Runtime bundle

不要手工复制整仓库到 GPT Knowledge。使用可重复构建：

```bash
python tools/build_bundle.py \
  --profile gpts/kukutx \
  --skill development/godot-project-systems \
  --reference development/godot-project-systems:ui-ux \
  --reference development/godot-project-systems:input-controls-accessibility
```

Bundle 自动包含 Project Instructions、Router、选中的 Skill 和 reference，并拒绝 `maintenance/`。`manifest.json` 记录源提交、文件哈希、字节数和粗略 Token 预算。

## Review test

提交前只检查：

```text
Does this change behavior?
Is ownership unambiguous?
Can the agent use available context/tools and make reversible progress before asking?
Does any pause/approval rule correspond to a real domain blocker or consequential boundary?
Does requested execution remain execution rather than becoming a plan?
Can less runtime context solve the same task?
Is source-of-truth singular?
Is maintenance separated from runtime?
Is verification proportional to the completion claim and risk?
```

如果改动只是“看起来更完整”，通常应该删除或留在 maintenance。
