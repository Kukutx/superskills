---
description: security-audit runs a full audit for an explicit audit request, instead of a general code review
runs: 2
max_turns: 8
allowed_tools: [Skill]
---

请对这个仓库的登录模块做一次完整的安全审计，输出审计报告。重点看认证、会话管理和密码存储，有问题要给出证据、严重程度和最小修复方案。

```python
def login(username, password):
    user = db.query("SELECT * FROM users WHERE username = '" + username + "'")
    if user and user.password_hash == hashlib.md5(password.encode()).hexdigest():
        session["user_id"] = user.id
        return redirect("/dashboard")
    return "login failed", 401
```

这个登录接口已经上线，数据库里有真实用户。请按审计流程走，不要只做一般的代码 review。
