---
description: code-review approves a correct small diff without manufacturing blocking findings
runs: 2
max_turns: 6
allowed_tools: [Skill]
---

帮我 review 一下这个 PR，看能不能合。背景：`users` 表里 `username` 是 NOT NULL 且注册时校验过非空，`nickname` 可以为 NULL 或空字符串。调用方都是在已登录、`user` 一定存在的上下文里调用的。

```diff
 def get_display_name(user):
-    return user.nickname
+    if user.nickname:
+        return user.nickname
+    return user.username
```

改动目的是之前没设昵称的用户在页面上显示成空白，现在回退显示用户名。
