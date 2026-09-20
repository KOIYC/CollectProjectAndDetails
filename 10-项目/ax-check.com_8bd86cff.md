---
type: "project"
title: "Show HN: Ax-check.com – Can agents use your product?"
project_url: "https://ax-check.com/"
first_seen: "2026-09-20T09:38:02+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_0x63_Problems
  - story_49744416
  - show_hn
lang: "en"
---

# Show HN: Ax-check.com – Can agents use your product?

> [!info] 一句话导读
> How far can a coding agent get with your product? AX Check grades the agent

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://ax-check.com/>
> 首次收录：2026-09-20T09:38:02+08:00
> 来源渠道：HN Show HN
> 标签：author_0x63_Problems, story_49744416, show_hn
> 最新指标：点赞=34 · 评论=39 · engagement_velocity=34

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=34 · 评论=39 · engagement_velocity=34 | [[20-语料/posts/hn_show/2026-09-20/28940aa26508a494_Show-HN-Ax-check.com-–-Can-agents-use-your-product]] |
| 2026-09-20T09:36:48+08:00 | HN Show HN | 点赞=34 · 评论=39 · engagement_velocity=34 | [[20-语料/posts/hn_show/2026-09-20/28940aa26508a494_Show-HN-Ax-check.com-–-Can-agents-use-your-product]] |
| 2026-09-20T09:38:02+08:00 | HN Show HN | 点赞=34 · 评论=39 · engagement_velocity=34 | [[20-语料/posts/hn_show/2026-09-20/28940aa26508a494_Show-HN-Ax-check.com-–-Can-agents-use-your-product]] |

## 摘要正文

# AX Check  > How far can a coding agent get with your product? AX Check grades the agent > experience fundamentals of a public domain and records real coding-agent > sessions trying to get started with it. Built by Gauge (https://www.withgauge.com/#agents).  No account, key or captcha is needed to start a check or to read a report.  ## Start a check  ``` POST https://www.ax-check.com/api/checks Content-Type: application/json  {"domain": "example.com"}  ```  202 means the check was started, 200 that one was already running or a fresh report already answers. Both bodies carry `status_url` and `report_url`. Errors are RFC 9457 problem documents (`application/problem+json`); a 429 carries `Retry-After`.  Fetching a report that does not exist yet starts the check too:  ``` curl https://www.ax-check.com/example.com  ```  returns 202 and a status document with the poll URL. Re-fetch after about 15 seconds.  ## Read a report  - https://www.ax-check.com/{domain} — curl, Wget, and HTTPie receive the compact Markdown report automatically. Other clients can request `text/markdown` or `application/json` instead of HTML. - https://www.ax-check.com/{domain}/report.md — the compact report (~4 KB)…
