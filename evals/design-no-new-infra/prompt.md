---
description: technical-design does not add queues/brokers/services without demonstrated need
runs: 2
max_turns: 6
allowed_tools: [Skill]
---

我们内部报销系统是 Django + PostgreSQL 单体，部署在一台服务器上，每天大约 200 张报销单。现在要加个功能：报销单审批通过后，给申请人发一封邮件通知，同时往财务的共享盘写一条记录（CSV 追加）。邮件服务或共享盘偶尔会挂。后面可能还会加别的通知方式，想设计得好一点，你给个技术方案。
