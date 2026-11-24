# Expo Development behavioral evals

Maintenance-only. Protect the Expo/plain-React-Native boundary.

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| expo-development-001 | “用 Expo 做一个待办 App，要能上架 App Store。” | `development/expo-development` | none | restructuring an existing app to match the new-project layout |
| expo-development-002 | “写一下这个 App 的上架文案和截图清单。” | `writing/app-store-copy` | `design/app-store-assets` | invoking expo-development for store copy or visual assets |
