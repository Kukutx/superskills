# Skill Builder maintenance sources

Maintenance-only. These sources back the repository's structure, `description` standard and distribution rules. Do not load for normal Skill work.

## Policy

- Host behavior is verified on the installed host before a rule changes: `codex debug prompt-input` for Codex's real Skill registry, `claude plugin validate` / `claude plugin details` for Claude Code.
- A limit recorded here is the strictest one any supported host documents. Re-check every row before loosening a Validator rule.
- The GitHub repositories in the register were read in full in 2026-10: every Markdown file and every script or config inside a Skill folder, 4,190 files in 96 batches. Not read: XML schema files, repository tooling outside Skill folders, binaries, and the marketplaces' full listings. A later review reads what changed since then; a repository being reachable is not a review.
- The three industry repositories added for the professional-domain round (Anthropic knowledge-work plugins, Anthropic financial-services plugins, Marketing Skills) were read in 2026-10 in 31 batches: 1,028 files and 163,803 lines, every listed file from first line to last, with the list of files kept per batch. Not read, 1,135 files and 174,331 lines: the Zoom developer plugin (694 files, 114,091 lines of SDK and API documentation for building on one vendor's platform); Marketing Skills' command-line clients and per-tool integration guides (162 files, 31,343 lines of code and vendor API notes that a web chat cannot call); the financial-services `agent-plugins` folders (72 files, 14,136 lines that are byte-identical copies of files read under `vertical-plugins`); its managed-agent cookbooks and Microsoft 365 installer (86 files, about 4,500 lines of deployment configuration and scripts); one HTML dashboard application and one HTML example; repository tooling, CI workflows, licence texts and binaries. None of the unread material was used for any Skill.
- Marketplaces and third-party Skill repositories are discovery inputs. Popularity is not evidence of quality or safety, and nothing from them is installed or copied without reading it first.

## Source register

| Source | Canonical URL | Used for | Last reviewed |
| --- | --- | --- | --- |
| Agent Skills specification | https://agentskills.io/specification | `SKILL.md` entrypoint, `name` equals folder, frontmatter fields | 2026-10 |
| claude.ai custom Skills | https://support.claude.com/en/articles/12512198-how-to-create-custom-skills | 200-character `description` limit, one ZIP per Skill with the folder as its root | 2026-10 |
| Claude Code Skills | https://code.claude.com/docs/en/skills | discovery paths, frontmatter, Skill listing budget | 2026-10 |
| Claude Code plugins | https://code.claude.com/docs/en/plugins | plugin layout, `skills/<skill>/SKILL.md` discovery | 2026-10 |
| Claude Code plugin marketplaces | https://code.claude.com/docs/en/plugin-marketplaces | `.claude-plugin/marketplace.json` entries | 2026-10 |
| Codex Skills | https://learn.chatgpt.com/docs/build-skills | Skill roots, description truncation under the listing budget, plugin Skills in ChatGPT | 2026-10 |
| Codex plugins | https://developers.openai.com/plugins/build/plugins | portable `plugin.json`, `.agents/plugins/marketplace.json`, version-keyed cache | 2026-10 |
| skills installer | https://github.com/vercel-labs/skills | discovery of `SKILL.md` in a repository, per-host install paths, lock files | 2026-10 |
| Anthropic Skills | https://github.com/anthropics/skills | multi-plugin marketplace layout, skill-creator eval approach | 2026-10 |
| Docker Skills | https://github.com/docker/skills | repository governance and cross-host manifest generation, as a comparison | 2026-10 |
| SkillSpector | https://github.com/NVIDIA/SkillSpector | scanning a third-party Skill before it is installed | 2026-10 |
| Matt Pocock Skills | https://github.com/mattpocock/skills | widely adopted engineering Skills, as a comparison for new candidates | 2026-10 |
| agentskills reference | https://github.com/agentskills/agentskills | reference validator behaviour for frontmatter | 2026-10 |
| SkillOpt | https://github.com/microsoft/SkillOpt | description optimisation and eval-task design, mostly as counter-examples | 2026-10 |
| taste-skill | https://github.com/Leonxlnx/taste-skill | visual quality rules for UI work | 2026-10 |
| .NET Skills | https://github.com/dotnet/skills | backend, EF Core, build and test rules, as a comparison; stack-specific, no Skill added from it | 2026-10 |
| Stripe agent toolkit | https://github.com/stripe/ai | payment integration rules, as a comparison; provider-specific, no Skill added from it | 2026-10 |
| Supabase Agent Skills | https://github.com/supabase/agent-skills | PostgreSQL rules, as a comparison | 2026-10 |
| Firebase Agent Skills | https://github.com/firebase/agent-skills | Firebase setup facts; setup flows not adopted | 2026-10 |
| Flutter agent plugins | https://github.com/flutter/agent-plugins | Flutter testing and tooling facts; architecture Skills not adopted | 2026-10 |
| Vercel agent Skills | https://github.com/vercel-labs/agent-skills | React and Next.js rules; its deploy script is not to be used | 2026-10 |
| agent-browser | https://github.com/vercel-labs/agent-browser | browser verification practice, as a comparison | 2026-10 |
| Google Skills | https://github.com/google/skills | cloud operations rules, as a comparison; provider-specific, no Skill added from it | 2026-10 |
| Cloudflare Skills | https://github.com/cloudflare/skills | reference-file structure (task-to-docs routing) | 2026-10 |
| HashiCorp Agent Skills | https://github.com/hashicorp/agent-skills | check and test design, as a comparison | 2026-10 |
| inference.sh Skills | https://github.com/inference-sh/skills | content, image and research method rules; platform usage not adopted | 2026-10 |
| Azure Skills | https://github.com/microsoft/azure-skills | cloud operations and third-party review cases | 2026-10 |
| Anthropic knowledge-work plugins | https://github.com/anthropics/knowledge-work-plugins | domain rules for the support, data, design, finance, legal, people, operations, marketing, product, sales and small-business Skills | 2026-10 |
| Anthropic financial-services plugins | https://github.com/anthropics/financial-services | valuation, modelling, diligence, reconciliation and equity research rules | 2026-10 |
| Marketing Skills | https://github.com/coreyhaines31/marketingskills | marketing, growth, pricing, retention and store optimisation rules | 2026-10 |
| SkillsMP | https://skillsmp.com/zh/skills | ecosystem discovery only; not a quality or safety review | 2026-10 |
| Claude Marketplaces | https://claudemarketplaces.com/skills | adoption signals for candidate Skills; not a quality or safety review | 2026-10 |
