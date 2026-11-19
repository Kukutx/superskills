---
description: implementation-plan labels unseen file paths as suggestions
runs: 2
max_turns: 6
allowed_tools: [Skill]
---

我们后端是 FastAPI + SQLAlchemy + PostgreSQL，用 Alembic 管迁移。方案已经定了：订单表改成软删除，加一个 deleted_at 字段（可为空的时间戳），删除接口改成写 deleted_at，所有订单列表和详情查询默认过滤掉已删除的，管理后台加一个"查看已删除"的开关。

帮我出一个实施计划，具体到要改哪些文件、按什么顺序做、怎么测。
