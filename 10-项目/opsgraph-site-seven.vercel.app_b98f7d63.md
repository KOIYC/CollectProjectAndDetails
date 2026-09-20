---
type: "project"
title: "Show HN: OpsGraph – evidence-first PostgreSQL investigations"
project_url: "https://opsgraph-site-seven.vercel.app/"
first_seen: "2026-09-20T09:36:40+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_arittrabag
  - story_49753339
  - show_hn
lang: "en"
---

# Show HN: OpsGraph – evidence-first PostgreSQL investigations

> [!info] 一句话导读
> OpsGraph — Evidence-first PostgreSQL investigations

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://opsgraph-site-seven.vercel.app/>
> 首次收录：2026-09-20T09:36:40+08:00
> 来源渠道：HN Show HN
> 标签：author_arittrabag, story_49753339, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/dd959b5eb29ce0ad_Show-HN-OpsGraph-–-evidence-first-PostgreSQL-inves]] |
| 2026-09-20T09:36:40+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/dd959b5eb29ce0ad_Show-HN-OpsGraph-–-evidence-first-PostgreSQL-inves]] |

## 摘要正文

OpsGraph — Evidence-first PostgreSQL investigations  # Ask PostgreSQL. Inspect the evidence.   OpsGraph is a self-hosted investigation workspace for one operator. Your model plans bounded, read-only queries. Application policy controls their execution.  Built for evaluation on an authorized, non-sensitive PostgreSQL test database. Not production-ready.   Self-hosted Read-only PostgreSQL External inference off by default One operator  Policy-controlled investigation   Recorded execution inspectable  1. 01  Scope checked Approved tables + playbook 2. 02  Query planned Model proposes bounded SQL 3. 03  Policy enforced Read-only limits before execution 4. 04  Evidence retained SQL, rows, source + limits   SELECT … LIMIT 100 5s timeout   MODEL PROPOSES• APP VALIDATES• POSTGRESQL STAYS READ-ONLY• EVIDENCE REMAINS INSPECTABLE• OPERATOR DECIDES  ## Evidence before certainty.  A citation does not make a conclusion true. OpsGraph keeps the work inspectable so you can review what was actually queried and captured before you act.  ### See what happened  Open referenced evidence to inspect the query, source, collection time, captured rows and limits behind a finding.  Recorded execution  ### Ke…
