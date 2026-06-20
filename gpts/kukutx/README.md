# kukutx GPT Setup

This folder contains the ready-to-use configuration for the user's private ChatGPT setup.

Use it for two related but different things:

1. **ChatGPT Project: `kukutx`**
   - Best for long-running work, files, project memory, and ongoing chats.
   - Use `project-instructions.md` as the Project Instructions.
   - Upload `knowledge-pack.md` or selected files from `knowledge-files.md` as Project files.

2. **Private Custom GPT: `Kukutx Superskills`**
   - Best as a one-click assistant entry point.
   - Use `private-gpt-instructions.md` as the GPT Instructions.
   - Use `conversation-starters.md` as starter prompts.
   - Use `knowledge-files.md` to choose knowledge files.

## Recommended first setup

For the current `kukutx` Project:

1. Open the project settings.
2. Paste `project-instructions.md` into Project Instructions.
3. Upload `knowledge-pack.md` first.
4. Start a new chat with:

```text
用 skill-router 帮我判断这个任务该用哪个 skill，并直接执行：
[你的任务]
```

## Recommended later setup

Create a Private Custom GPT named:

```text
Kukutx Superskills
```

Use:

- `private-gpt-instructions.md` for Instructions.
- `knowledge-pack.md` as the first Knowledge file.
- Add more skill files from `knowledge-files.md` if needed.

## Maintenance rule

When `superskills` changes meaningfully:

1. Update the relevant skill files.
2. Update `knowledge-pack.md` if routing or defaults changed.
3. Update the GPT Knowledge files.
4. Test with the prompts in `conversation-starters.md`.
