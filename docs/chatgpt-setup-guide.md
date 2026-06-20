# ChatGPT Setup Guide for kukutx

This guide explains how to use `superskills` inside the user's `kukutx` ChatGPT Project and later as a Private Custom GPT.

## Why use both Project and Private GPT

Use both, but for different purposes:

| Tool | Best for |
| --- | --- |
| GitHub `superskills` | Source of truth, versioning, long-term maintenance |
| ChatGPT Project `kukutx` | Long-running work, files, chats, project memory |
| Private Custom GPT | One-click assistant entry point |

Projects are smart workspaces that keep chats, uploaded files, and custom instructions together for long-running work. They also support tools like Canvas, image generation, web search, and more depending on plan and settings.

Private GPTs are better as a reusable assistant interface with fixed instructions, knowledge, conversation starters, and optional capabilities.

## Step 1: Configure the `kukutx` Project

Open the `kukutx` Project in ChatGPT.

Then:

1. Open the project menu.
2. Go to Project settings.
3. Paste the contents of:

```txt
gpts/kukutx/project-instructions.md
```

into Project Instructions.

4. Upload at least this file as a project source:

```txt
gpts/kukutx/knowledge-pack.md
```

5. Start a new chat with:

```text
用 skill-router 帮我判断这个任务该用哪个 skill，并直接执行：
[你的任务]
```

## Step 2: Optional but recommended files for Project

If your plan allows more files, add:

```txt
README.md
skills/README.md
docs/personal-defaults.md
docs/western-market-guidelines.md
docs/workflow-recipes.md
```

Then add high-frequency skill files as needed.

## Step 3: Create the Private Custom GPT

Name:

```txt
Kukutx Superskills
```

Description:

```txt
A private AI workflow assistant for product, development, design, marketing, Shopify, image generation, app store assets, xTool F1 engraving, and reusable skill-based work.
```

Instructions:

```txt
gpts/kukutx/private-gpt-instructions.md
```

Conversation starters:

```txt
gpts/kukutx/conversation-starters.md
```

Knowledge:

Start with:

```txt
gpts/kukutx/knowledge-pack.md
```

Then add files from:

```txt
gpts/kukutx/knowledge-files.md
```

## Recommended GPT capabilities

Enable:

- Web search
- Image generation
- Canvas
- Code Interpreter & Data Analysis

Do not enable Actions yet unless the GPT needs to call external APIs.

## Test prompts

After setup, test these:

```text
先帮我选 skill，再执行：我要做一个欧美市场的 App 素材。
```

```text
用 xTool F1 workflow 帮我设计一个原创、安全、适合雕刻的礼物图案。
```

```text
帮我把这个功能做 PRD、技术方案和 implementation plan。
```

```text
帮我 review 这张生成图，并给我下一轮优化 prompt。
```

## Maintenance workflow

When `superskills` changes:

1. Commit changes to GitHub.
2. Update `gpts/kukutx/knowledge-pack.md` if global rules changed.
3. Re-upload changed files to Project / GPT Knowledge.
4. Test the same starter prompts again.

## Practical rule

If the Project or GPT starts giving generic answers:

1. Tighten Instructions first.
2. Add examples second.
3. Add more Knowledge files last.

Do not solve behavior problems by uploading too many files at once.
