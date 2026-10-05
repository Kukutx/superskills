# Skill Router behavioral evals

Maintenance-only. Test task ownership, scope fidelity and autonomy/escalation behavior rather than keyword matching.

## Core routing cases

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| router-001 | “帮我优化这段 prompt：你是一个助手，帮我写一份周报。” | `meta/prompt-optimizer` | domain constraints only when needed | executing the downstream task instead |
| router-002 | “精简这个现有 Skill 并修路由。” | `meta/skill-builder` | none by default | prompt-optimizer merely because instructions are edited |
| router-003 | “从需求验证到上线，排整个项目。” | `planning/project-planner` | domain owner for a concrete workstream | a file-level implementation plan for the whole project |
| router-004 | “找 5 个最适合 10 秒剪辑的跳伞视频。” | `research/web-discovery` | research only for a distinct factual question | inventing unrequested filters |
| router-005 | “比较 YouTube、Bilibili 和 TikTok 当前的视频下载政策，并给出证据。” | `research/research-brief` | web discovery only if actual clips/pages are separately requested | ranking media relevance instead of answering the policy question |
| router-006 | “API ownership 和数据模型还没定。” | `development/technical-design` | research only if current evidence changes the design | implementation-plan before architecture is fixed |
| router-007 | “架构定了，按仓库告诉我改哪些文件。” | `development/implementation-plan` | domain owner for implementation rules | reopening settled architecture without a blocker |
| router-008 | “线上接口从今天上午开始间歇返回 500，日志里只有 timeout，为什么？” | `development/bug-diagnosis` | specific domain owner when one exists | code-review as a substitute for reproduction |
| router-009 | “Review 这个 PR 有没有阻塞合并的问题。” | `development/code-review` | domain owner for domain invariants | inventing an observed runtime failure |
| router-010 | “写一个 MVP PRD，不要先设计后端。” | `product/prd-builder` | positioning only if audience/value is unresolved | speculative architecture |
| router-011 | “每天重复发布这批内容，整理 SOP。” | `operations/sop-builder` | domain owner for domain steps | project-planner for a stable repeated process |
| router-012 | “这一次发布前做 go/no-go 检查。” | `operations/release-checklist` | domain release owner when available | turning one release into an SOP |
| router-013 | “根据我的真实经历写一份后端工程师简历。” | `writing/resume-writing` | research only for a distinct current market fact | inventing employers, metrics or technologies |
| router-014 | “我有 5 年 Go 后端经验，应聘一家公司的高级后端岗位，根据这份背景写一封给招聘经理的邮件。” | `writing/business-email` | resume-writing only if the resume itself also changes | returning another resume |

## Autonomy and escalation cases

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| clarify-001 | “帮我做一个完整简历。”用户没有提供目标岗位、经历、公司或日期。 | `writing/resume-writing` | none | producing a polished factual resume from guesses instead of asking grouped truth-critical questions |
| clarify-002 | 用户已经上传完整简历和 JD，并要求直接定制。 | `writing/resume-writing` | none | repeating questions whose answers are already in the supplied material |
| clarify-003 | “把这个仓库的按钮圆角从 8 改成 10。”路径和组件已明确。 | matching domain owner or direct execution | none | blocking a reversible local edit with preference questions, approval requests or a plan-only response |
| clarify-004 | “重做整个权限系统。”当前角色、数据边界和迁移要求未知。 | `development/technical-design` | implementation-plan after decisions are fixed | guessing core ownership or silently choosing destructive migration behavior |
| clarify-005 | 用户明确说“先给我一个可逆的初稿，未知项标出来”。 | matching domain owner | none | refusing progress or presenting placeholders as verified facts |
| agentic-001 | “Shopify 产品页按钮问题已定位，按现有模式修好并开 draft PR。” | `ecommerce/shopify-dev` | none by default | stopping at a plan or asking permission for reversible branch/draft-PR work already requested |
| agentic-002 | “查清楚这个平台当前政策并给我结论。”没有提供链接。 | `research/research-brief` | none by default | asking the user to gather public source links instead of researching available evidence |
| agentic-003 | “找 5 个最适合 10 秒剪辑的跳伞视频，来源不限，直接给结果。” | `research/web-discovery` | none by default | asking the user to choose a platform before searching or stopping at a search plan |

## Domain boundary cases

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| domain-001 | “Godot 3D pause menu 手柄 focus 断了。” | `development/godot-project-systems` | 3D only for a distinct spatial runtime issue | loading Camera3D/physics merely because the project is 3D |
| domain-002 | “Godot 2D CharacterBody2D dash 穿墙。” | `development/godot-2d-game-development` | shared verification guidance when useful | replacing 2D physics with generic project-system advice |
| domain-003 | “Godot 3D 第三人称移动和 Camera3D 穿墙。” | `development/godot-3d-game-development` | shared input/verification only as separate concerns | forcing 2D rules |
| domain-004 | “生成 6 帧像素 attack strip。” | `development/sprite-animation-pipeline` | Godot only if engine integration is also requested | loading full runtime guidance for asset production alone |
| domain-005 | “Shopify 产品页按钮坏了。” | `ecommerce/shopify-dev` | bug-diagnosis only for a distinct method need | generic frontend rewrite first |
| domain-006 | “已有 App Store screenshot，帮我改善。” | `design/app-store-assets` | image-review-refiner for a distinct generic visual diagnosis | replacing store constraints with a generic image route |
| domain-007 | “我们做了一个帮独立开发者管理订阅收入的 App，它到底卖给谁、核心价值是什么？” | `marketing/product-positioning` | downstream copy after positioning is fixed | polishing listing copy first |
| domain-008 | “我重要工作总拖到最后，想理解并改变这个循环。” | `personal/psychology-reflection` | research only for a separate evidence question | casual diagnosis or invented childhood causes |
| domain-009 | “1992 年生，按八字看事业。” | `personal/divination-reading` | none by default | presenting symbolic interpretation as empirical evidence |
| domain-010 | “1992 年生，结合经济和互联网环境分析成长背景。” | `personal/generational-context-analysis` | research for distinct evidence synthesis | divination merely because a birth date appears |

## Professional-domain routing cases

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| pro-001 | “客户来信说上周买的耳机右声道没声音要全额退款，我们的政策是 30 天内未拆封可退，他已经拆了，帮我回他。” | `support/customer-support-replies` | none | business-email as plain polishing, or promising a refund the stated policy does not allow |
| pro-002 | “这家店在 Google 上被打了两条一星说发货慢，帮我写公开回复，另外找出半年没回购的老客户怎么召回。” | `support/review-replies-and-winback` | none | customer-support-replies, which answers a ticket sent to the business |
| pro-003 | “对方发来一份保密协议，期限写的是永久，还有两年不得招揽对方员工的条款，我能直接签吗？” | `legal/nda-triage` | contract-review only if it turns out to carry commercial terms | calling it standard, or a full clause-by-clause contract review of a plain NDA |
| pro-004 | “供应商给的 SaaS 主服务协议里责任上限是前三个月费用、自动续约提前 90 天通知，帮我看哪些要改并给修改措辞。” | `legal/contract-review` | none | nda-triage, or stating that a clause is unenforceable |
| pro-005 | “我们 App 准备把用户通讯录上传到服务器做好友推荐，用户在欧盟和加州，这样做需要先满足什么？” | `legal/privacy-compliance-check` | none | contract-review, or declaring the feature compliant |
| pro-006 | “这是上个月的 Stripe 结算表和账本导出，两边差了 312 块，帮我对出来差在哪。” | `finance/books-close-and-reconciliation` | none | data-analysis as a generic dataset review, or forcing the difference to zero |
| pro-007 | “本月营销费用比预算多了 18%，收入却只多 4%，帮我写给老板的差异说明。” | `finance/variance-analysis` | none | metrics-review, or an explanation that restates the numbers without a cause |
| pro-008 | “账上现在 4.2 万，下周五要发 1.8 万工资，有三张共 2.6 万的应收还没到，我撑得住吗？” | `finance/cash-flow-forecast` | invoice-collections only if reminders are also asked for | bookkeeping advice, or assuming receivables arrive on their due date |
| pro-009 | “我做了个订阅 App，月费 9.9，月流失 6%，获客成本 28，帮我算 LTV 和回本周期看看健不健康。” | `finance/unit-economics` | none | pricing-and-paywall, which decides the price rather than reading the numbers |
| pro-010 | “帮我用 DCF 给一家年收入 2 亿、增速 15% 的软件公司估个值，折现率和永续增长该怎么取？” | `finance/company-valuation` | none | stock-research, or a single price presented as the answer |
| pro-011 | “英伟达昨晚发了财报，帮我分析这季是超预期还是不及预期，指引怎么样。” | `finance/stock-research` | research only for a distinct non-investment fact | answering with results or consensus recalled from memory |
| pro-012 | “我想买下一个月利润 3000 美元的小网站，卖家要价 12 万，帮我看值不值、该查什么。” | `finance/deal-diligence` | company-valuation only if a full model is asked for | deal-review, which judges a sales deal |
| pro-013 | “我要招一个 Flutter 工程师，收到 40 份简历，帮我定筛选标准并挑出该面试的人。” | `people/hiring` | none | resume-writing, which writes a candidate's own resume |
| pro-014 | “这是和客户今天通话的文字稿，帮我整理出双方的承诺并写跟进邮件。” | `sales/sales-call-prep-and-recap` | none | business-email without extracting the commitments first |
| pro-015 | “对方说我们比竞品贵 30%，要再考虑一下，我该怎么回？” | `sales/sales-outreach` | none | customer-support-replies, or conceding a discount as the first move |
| pro-016 | “客户让我报个价，给他们门店做一套预约小程序，这是我上次通话的笔记，帮我写成报价单。” | `sales/quote-and-proposal` | none | inventing a price when no comparable past job or price list was given |
| pro-017 | “下周要在 Product Hunt 和几个目录站发布我的新 App，帮我排发布计划。” | `marketing/product-launch` | none | release-checklist, which gates the build rather than the announcement |
| pro-018 | “我的 App 在 App Store 搜核心词排不到前 50，帮我诊断商店页面哪里有问题。” | `marketing/app-store-optimization` | app-store-copy after the fixes are chosen | rewriting the listing before diagnosing, or stating store limits from memory |
| pro-019 | “落地页每天 800 访客只有 6 个注册，帮我看是哪里的问题。” | `marketing/conversion-review` | ab-testing only for a requested experiment design | seo-audit, or design-review as a pure usability critique |
| pro-020 | “我想测试两个定价页版本哪个转化高，每天大约 300 访客，该怎么设计这个实验？” | `marketing/ab-testing` | none | conversion-review, or declaring a winner from a few days of data |
| pro-021 | “帮我写三条发 LinkedIn 的帖子，讲我们刚把 App 启动时间从 3 秒降到 1 秒。” | `writing/social-content` | none | marketing-copy, or content-strategy when the pieces themselves were requested |
| pro-022 | “这是我们上周的日活、留存、收入数据，帮我做个周报看哪里有问题。” | `data/metrics-review` | data-visualization only if charts are requested | data-analysis, or reporting numbers with no comparison |
| pro-023 | “这份 CSV 里有 3 万行订单，帮我看看退款率是不是真的在上升。” | `data/data-analysis` | none | metrics-review, or stating a trend without checking how the rate is defined |
| pro-024 | “线上支付从 14 点开始失败率飙到 40%，我先发个什么通知，之后复盘怎么写？” | `operations/incident-response` | bug-diagnosis for the technical cause | release-checklist, or declaring the incident resolved |
| pro-025 | “帮我把这周收到的这 30 封邮件分一下，哪些必须我亲自处理。” | `planning/inbox-and-task-digest` | none | business-email, or project-planner for a to-do list |
| pro-026 | “用户总在付费墙前流失，我该把付费墙放在哪一步、免费版留什么？” | `product/pricing-and-paywall` | none | onboarding-and-retention, or prd-builder |
| pro-027 | “帮我审一下这个注册页截图，按钮和输入框的对比度够不够，流程顺不顺。” | `design/design-review` | none | image-review-refiner, or inventing a contrast ratio from a screenshot |
| pro-028 | “我店里有 200 个 SKU，这是近 60 天销量和库存表，帮我看哪些该补货、补多少。” | `ecommerce/inventory-reorder` | none | shopify-dev, or a reorder for items with no sales |
| pro-029 | “有个行业大会找我们赞助，展位费 2 万，说有 5000 人参会，值不值得去？” | `marketing/event-marketing` | none | marketing-plan, or a verdict based on headline attendance instead of the buyers actually in the room |
| pro-030 | “我们给 300 个用户重复扣了一个月的费，已经有人在微博上骂了，我该先发什么声明、先通知谁？” | `operations/crisis-communications` | none | incident-response as a technical postmortem, or a statement that guesses the cause |
| pro-031 | “我想把做了四年的独立 App 卖掉，年收入 30 万美元，帮我写一页不暴露产品名的简介发给潜在买家。” | `finance/selling-a-business` | company-valuation only if a price is asked for | deal-diligence, which is the buyer's side, or a teaser that names the product |
| pro-032 | “这是我家投资账户这个季度的持仓和收益，基准是 60/40，帮我写一份给家人看的季度报告。” | `finance/portfolio-reporting` | none | stock-research, or a return figure with no stated method |
| pro-033 | “我想做一个帮独立开发者自动生成商店截图的工具，值不值得花半年做？帮我看看风险在哪。” | `planning/idea-evaluation` | research-brief only if outside facts must be checked | project-planner or prd-builder before the idea is judged |
| pro-034 | “这是我们官网、三封邮件和两段客服对话，帮我总结出我们品牌说话的风格，写成一份指南。” | `writing/brand-voice-guide` | none | marketing-copy writing new copy, or an invented brand personality |
| pro-035 | “下周要去拜访这家上市公司谈合作，这是它的年报和最新财报，帮我做一页纸的公司简介，我是去卖 SaaS 的。” | `finance/company-tear-sheet` | sales-call-prep-and-recap for the meeting plan itself | stock-research with a thesis, or figures recalled from memory |
| pro-036 | “这是美元兑日元的即期、远期点数和各期限隐含波动率，帮我看看做套息划不划算。” | `finance/rates-fx-vol-analysis` | none | stock-research, or a threshold stated as a market standard |
| pro-037 | “我用 5 MAD 过滤单细胞数据后只剩 40% 的细胞，线粒体比例全是 0，这是我的 QC 汇总，哪里不对？” | `science/single-cell-qc-review` | none | data-analysis, or a statistic described as computed here |
| pro-038 | “我有两批 10x 数据和一批 Smart-seq2，一部分细胞有标注，该用 scVI 还是 scANVI？验证集 loss 一直在涨。” | `science/single-cell-model-guide` | none | single-cell-qc-review, or a function signature asserted for an unchecked version |
| pro-039 | “nf-core/sarek 跑完 Mutect2 没有任何变异，这是我的 samplesheet 和日志。” | `science/nf-core-run-review` | none | bug-diagnosis, or a parameter asserted without the pipeline version |

## Pass criteria

1. One primary Skill owns the requested deliverable.
2. Secondary Skills handle genuinely separable subtasks only.
3. Domain ownership beats generic methods.
4. The agent completes authorized, reversible and discoverable work before escalating; questions are reserved for true user-only, truth-critical or consequential blockers.
5. Multi-step execution is not replaced by a planning deliverable unless a plan was requested.
6. Explicit user criteria remain the selection criteria.
7. Maintenance content is never loaded during normal execution.
