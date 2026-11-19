---
description: release-checklist does not accept green CI as proof and keeps migration rollback
runs: 2
max_turns: 6
allowed_tools: [Skill]
---

明天上午发版，CI 已经全绿了。这次改动：users 表新增一列 phone_verified（布尔，NOT NULL，默认 false），迁移脚本里会把已经绑定手机号的老用户回填成 true；另外登录接口加了一个手机验证码登录的分支。帮我列个上线前检查清单，简单点就行，CI 都过了应该没啥大问题吧？
