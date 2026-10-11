---
type: "corpus"
item_id: "8f9e04d19d9e0974"
title: "LibreDB Studio: a self-hosted SQL IDE that runs in your browser, for 46 databases"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/buildinpublic/comments/1wudku8/libredb_studio_a_selfhosted_sql_ide_that_runs_in/"
project_url: "https://app.libredb.org/"
author: "Green_Competition_21"
published_at: "2026-10-01T03:00:03+08:00"
captured_at: "2026-10-11T09:45:33+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-11"
pub_day: "2026-10-01"
tags:
  - 语料
  - reddit
  - r/buildinpublic
metrics: {"score": 6, "comments": 6, "upvote_ratio": 0.8}
comments_count: 6
comments_total: 6
discovered_via: "reddit:14d+settle10"
---

# LibreDB Studio: a self-hosted SQL IDE that runs in your browser, for 46 databases

> [!info] 一句话导读
> Repo: [https://github.com/libredb/libredb-studio](https://github.com/libredb/libredb-studio)

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/buildinpublic/comments/1wudku8/libredb_studio_a_selfhosted_sql_ide_that_runs_in/>
> 指标：得分=6 · 评论=6 · 赞踩比=0.8
> 作者：Green_Competition_21　|　发布：2026-10-01T03:00:03+08:00
> 项目链接：<https://app.libredb.org/>
> 采集：2026-10-11T09:45:33+08:00　|　id：`8f9e04d19d9e0974`

## 正文

Repo: [https://github.com/libredb/libredb-studio](https://github.com/libredb/libredb-studio)

Demo: [https://app.libredb.org](https://app.libredb.org/)

Youtube : [https://www.youtube.com/watch?v=rWANKEDszs4](https://www.youtube.com/watch?v=rWANKEDszs4)

Deploy it next to your database with Docker or Helm and open it in the browser. No SSH tunnels, no desktop client on every laptop.

Postgres, MySQL, Oracle, SQL Server, MongoDB, Redis, ClickHouse, DuckDB, Cassandra and more. MIT licensed, SSO and the AI assistant included.

Resource : [https://libredb.org/blog/twelve-database-projects-list-libredb-studio/](https://libredb.org/blog/twelve-database-projects-list-libredb-studio/)

## 评论（6/6）

> **Lanky-Prompt6519**（1 分） · 2026-10-01T03:10:32+08:00　
> That hexagonal logo is nice, geometric patterns always catch my eye. The list of databases it supports is huge, having Redis and Cassandra in same tool is not something you see every day. I will try the demo later, the Docker deploy sounds convenient for quick setup.

---

> **QuanTradin**（1 分） · 2026-10-01T07:30:05+08:00　
> does it have a per-connection read-only switch? that's the first thing I'd want before pointing a browser IDE at prod.

---

> **Green_Competition_21**（1 分） · 2026-10-01T08:05:23+08:00　
> Not yet as a per-connection toggle in the editor. Today you get an environment tag per connection (prod shows a red PROD badge) and a confirm step before DROP/DELETE/UPDATE/TRUNCATE, but that's a UI guard, not a hard lock.
>
> The part that is enforced by the database itself is the AI agent and MCP path: on Postgres, SQLite, DuckDB and SQL Server those run inside a read-only transaction/session, so writes get rejected by the engine, not by us parsing SQL. Details here: [https://github.com/libredb/libredb-studio/blob/main/docs/FEATURES.md#18-the-database-agent-read-only-investigation-runs](https://github.com/libredb/libredb-studio/blob/main/docs/FEATURES.md#18-the-database-agent-read-only-investigation-runs)
>
> For pointing it at prod right now, the honest answer is the same as with any client: connect with a read-only DB role (e.g. a Postgres role with only SELECT grants, or default\_transaction\_read\_only = on for that user). That holds no matter what the UI does.

---

> **QuanTradin**（1 分） · 2026-10-01T08:21:53+08:00　
> enforcing it in the database on the agent path is the right half to make hard. a confirm dialog on DROP is fine for people, but everyone clicks through those inside a week.

---

> **Green_Competition_21**（1 分） · 2026-10-01T08:27:48+08:00　
> Agreed, confirm dialogs turn into muscle memory fast. That's why the advice for prod is still a read-only role: the database says no, not the UI.

---

> **QuanTradin**（1 分） · 2026-10-01T09:06:48+08:00　
> yeah, the role is the only check that still holds at 2am. I made the same call on a paper trading desk I built, Quantradin (quantradin.com): the agent's key is read-only on the server, so no client-side prompt decides whether a new order goes in.

## 关联链接

- https://app.libredb.org
- https://github.com/libredb/libredb-studio
- https://libredb.org/blog/twelve-database-projects-list-libredb-studio/
- https://www.youtube.com/watch?v=rWANKEDszs4

## 导航

- 项目页：[[10-项目/app.libredb.org_747f245d]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
