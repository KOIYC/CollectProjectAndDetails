---
type: "project"
title: "Show HN: EACL is a situated ReBAC authorization library for Datomic and Datahike"
project_url: "https://github.com/theronic/eacl"
first_seen: "2026-09-20T09:37:15+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_pgt
  - story_49712785
  - show_hn
lang: "en"
---

# Show HN: EACL is a situated ReBAC authorization library for Datomic and Datahike

> [!info] 一句话导读
> 🦅 EACL: Enterprise Access ControL is a ReBAC Authorization system based on SpiceDB, built in Clojure and backed by Datomic

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/theronic/eacl>
> 首次收录：2026-09-20T09:37:15+08:00
> 来源渠道：HN Show HN
> 标签：author_pgt, story_49712785, show_hn
> 最新指标：点赞=5 · 评论=0 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=5 · 评论=0 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-20/b3dd61e6be352b2c_Show-HN-EACL-is-a-situated-ReBAC-authorization-lib]] |
| 2026-09-20T09:37:15+08:00 | HN Show HN | 点赞=5 · 评论=0 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-20/b3dd61e6be352b2c_Show-HN-EACL-is-a-situated-ReBAC-authorization-lib]] |

## 摘要正文

# theronic/eacl  🦅 EACL: Enterprise Access ControL is a ReBAC Authorization system based on SpiceDB, built in Clojure and backed by Datomic  - Stars: 81 - Forks: 7 - Watchers: 81 - Open issues: 16 - License: Eclipse Public License 2.0 - Homepage: http://eacl.dev/ - Default branch: main - Created: 2019-11-23T11:16:36Z  ## Languages  - Clojure  ## Topics  - access-control - authorization - clojure - datalog - datomic - eacl - permissions - rebac - spicedb  ## Top Contributors  - theronic (187 contributions)  ---  ## README  # 🦅 **EACL**: Enterprise Access ControL  EACL is a _situated_ ReBAC authorization library based on SpiceDB, built in Clojure and backed by Datomic.  _Situated_ here means that your permission data lives _next to_ your application data in Datomic, which has some benefits: 1. Avoids a network hop. To leverage SpiceDB's consistency semantics, you need to hit your DB (or cache) to retrieve the latest stored ZedToken anyway, so you might as well query the DB directly, which is what EACL does. 2. One less external dependency to deploy & sync relationships. 3. Fully consistent queries – an external authz system necessitates eventual consistency.  EACL is pronounced "EE-k…
