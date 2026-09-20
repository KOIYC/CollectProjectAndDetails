---
type: "corpus"
item_id: "fd6aca9934b8b1d9"
title: "Show HN: NeonD – self-hosted Postgres Platform with branching, PITR and backups"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47947389"
project_url: "https://github.com/matisiekpl/neond"
author: "matisiekpl"
published_at: "2026-04-29T12:27:13Z"
captured_at: "2026-09-21T01:42:04+08:00"
lang: "en"
kind: "post"
topic: "未分类"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_matisiekpl
  - story_47947389
  - show_hn
metrics: {"points": 2, "comments": 2, "engagement_velocity": 2}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:174d"
---

# Show HN: NeonD – self-hosted Postgres Platform with branching, PITR and backups

> [!info] 一句话导读
> Show HN: NeonD – self-hosted Postgres Platform with branching, PITR and backups

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47947389>
> 指标：点赞=2 · 评论=2 · engagement_velocity=2
> 作者：matisiekpl　|　发布：2026-04-29T12:27:13Z
> 项目链接：<https://github.com/matisiekpl/neond>
> 采集：2026-09-21T01:42:04+08:00　|　id：`fd6aca9934b8b1d9`

## 正文

Show HN: NeonD – self-hosted Postgres Platform with branching, PITR and backups

## 评论（2/2）

> **matisiekpl** · 2026-04-29T12:27:24.000Z　
> Hey HN, Mateusz here.I built NeonD for myself and figured it might be useful to others. It's a control plane for PostgreSQL that runs as a single Docker container.The problem: I often need to spin up Postgres instances for small side projects. They usually have to run 24/7 for the whole month, and RDS gets expensive fast for that kind of thing. I wanted something that replaces my docker-compose with `postgres:latest`, but adds the few features I actually miss: PITR, proper backups, branching for preview environments.The solution: NeonD is a rich Postgres Control Plane you drop on a dedicated server / VPS. It manages multiple Postgres instances under one host inside single container.What's in the box:- Multi-tenancy and management of multiple Postgres instances- Branching — spin up an isolated DB environment for a preview branch in seconds- PITR with arbitrary-LSN precision, fully configurable retention- S3 backups (layer durability)- Fully automated TLS certificate management- TLS SNI routing — every instance gets its own subdomain, e.g. instance-a.your-company.com- Built-in metrics + log monitoring with PrometheusInstall takes less than 5 minutes using docker compose. Feel free to test it and put some feedback. Thanks

---

> **gajo357** · 2026-05-04T12:23:56.000Z　
> Nice work. I had this issue as well, several times.Making a small project, needed a DB for quick proof oc concept."Proper" DBs are too expensive, free ones are bound with some random compute-unit mathematics. Everything self hosted takes time that I'd rather spend coding.

## 导航

- 项目页：[[10-项目/github.com_860ae52c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`未分类`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
