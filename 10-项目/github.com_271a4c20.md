---
type: "project"
title: "Show HN: Dayfile.app – Append-only log for your scripts and agents"
project_url: "https://github.com/dayfile/dayfile"
first_seen: "2026-11-20T09:45:52+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_gilad
  - story_50561824
  - show_hn
lang: "en"
---

# Show HN: Dayfile.app – Append-only log for your scripts and agents

> [!info] 一句话导读
> Hi HN, I'm Gilad.dayfile.app is a "git log for scripts and agents", with ordered history, append-only logging as foundational characteristics. The service is cu…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/dayfile/dayfile>
> 首次收录：2026-11-20T09:45:52+08:00
> 来源渠道：HN Show HN
> 标签：author_gilad, story_50561824, show_hn
> 最新指标：点赞=4 · 评论=2 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-20T09:45:52+08:00 | HN Show HN | 点赞=4 · 评论=2 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-11-20/eff112c26c267741_Show-HN-Dayfile.app-–-Append-only-log-for-your-scr]] |

## 摘要正文

Hi HN, I'm Gilad.dayfile.app is a "git log for scripts and agents", with ordered history, append-only logging as foundational characteristics. The service is currently in beta, AGPL-licensed.As I was looking at various ways to record and retrieve a day's to-dos, automation and operational outputs (update successes and failures), the idea of a running event log. dayfile.app's primary use case is DevOps tracking and event logging. Building this, I've emphasized simplifying posting - one HTTP request with a title and optional tags (used for filtering when reading the log), AI access via MCP server (an assistant can read, post or close to-dos) and self-hosting as a first-class citizen (`pip install dayfile`, SQLite database is local in this mode).A demo is available at https://dayfile.app/demo. If using the cloud service and after generating a write token on the site, an example of posting an entry would be: curl -X POST https://USERNAME.dayfile.cloud/events \  -H "Authorization: Bearer WRITE_TOKEN" \  -H "content-type: application/json" \  -d '{"title":"Nightly backup finished","tags":["backup"]}'  To read back (filtering using tag): curl -H "Authorization: Bearer READ_TOKEN" \  "http…
