---
type: "project"
title: "Show HN: Preview Postgres writes from AI agents with xmin checks (pg-dry-run)"
project_url: "https://github.com/polycore/pg-dry-run"
first_seen: "2026-09-21T03:11:20+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_anarkafkas
  - story_49510746
  - show_hn
lang: "en"
---

# Show HN: Preview Postgres writes from AI agents with xmin checks (pg-dry-run)

> [!info] 一句话导读
> Preview the effect of agent-generated Postgres writes before they run.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/polycore/pg-dry-run>
> 首次收录：2026-09-21T03:11:20+08:00
> 来源渠道：HN Show HN
> 标签：author_anarkafkas, story_49510746, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:33:52+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/52cd040f81c07f4c_Show-HN-Preview-Postgres-writes-from-AI-agents-wit]] |
| 2026-09-21T03:11:20+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/52cd040f81c07f4c_Show-HN-Preview-Postgres-writes-from-AI-agents-wit]] |

## 摘要正文

# polycore/pg-dry-run  Preview the effect of agent-generated Postgres writes before they run.  - Stars: 1 - Forks: 0 - Watchers: 1 - Open issues: 0 - License: MIT License - Homepage: https://docs.polycore.ai/pg-dry-run - Default branch: main - Created: 2026-08-30T13:38:50Z  ## Languages  - JavaScript - TypeScript  ## Top Contributors  - kafkas (16 contributions)  ---  ## README   Preview the effect of agent-generated Postgres writes before they run.   Turn INSERT, UPDATE, and DELETE into  row-level proposals you can inspect, approve, and apply safely.   Why  · Quick start  · How it works  · Polycore  · Safety  · API  ---  ## Why this exists  AI agents increasingly inspect schemas, generate SQL, and operate real applications. Read access can be contained with a read-only role. Writes need a way to inspect the effect before production data changes.  An agent can generate a perfectly valid statement that does something nobody intended:  ```sql UPDATE profiles SET status = 'suspended' WHERE email LIKE '%@acme.com'; ```  The SQL looks reasonable, but production data decides whether it updates one account or fourteen. Inserts can pick up defaults that never appear in the statement, and d…
