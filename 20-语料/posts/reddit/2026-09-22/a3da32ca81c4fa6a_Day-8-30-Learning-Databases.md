---
type: "corpus"
item_id: "a3da32ca81c4fa6a"
title: "Day 8/30: Learning Databases"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/microsaas/comments/1wk7kvm/day_830_learning_databases/"
author: "Shashank_Mishra011"
published_at: "2026-09-19T08:41:11+08:00"
captured_at: "2026-09-22T12:54:29+08:00"
lang: "en"
kind: "post"
topic: 开发者工具
shard: "2026-09-22"
pub_day: "2026-09-19"
tags:
  - 语料
  - reddit
  - r/microsaas
metrics: {"score": 3, "comments": 6, "upvote_ratio": 0.8}
comments_count: 6
comments_total: 6
discovered_via: "reddit:7d+settle3"
---

# Day 8/30: Learning Databases

> [!info] 一句话导读
> Day 8 of my startup-building journey.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/microsaas/comments/1wk7kvm/day_830_learning_databases/>
> 指标：得分=3 · 评论=6 · 赞踩比=0.8
> 作者：Shashank_Mishra011　|　发布：2026-09-19T08:41:11+08:00
> 项目链接：—
> 采集：2026-09-22T12:54:29+08:00　|　id：`a3da32ca81c4fa6a`

## 正文

Day 8 of my startup-building journey.

Today I focused on databases.

Before today, I knew apps stored information somewhere, but I never really understood how.

I learned about:

SQL vs NoSQL

PostgreSQL

MySQL

MongoDB

Supabase

One thing that stood out:

The more I learn about software, the more I realize that users only see the surface.

Behind every simple app is a huge amount of infrastructure managing data.

For developers:

If you were starting from scratch today, which database would you learn first and why?

## 评论（6/6）

> **Valuable-Bobcat-3601**（3 分） · 2026-09-19T08:55:48+08:00　
> Listing Postgres, MySQL, Mongo and Supabase is knowing five names, not learning databases. What did you actually build with one of them today? The answer to your own question is Postgres by the way, and it has been for about a decade.

---

> **Wooden_Astronomer718**（3 分） · 2026-09-19T09:37:27+08:00　
> Postgres is the right first pick. It handles relational data cleanly, and once you understand foreign keys, joins, and indexes there, NoSQL concepts make a lot more sense by comparison instead of feeling like a totally separate world. MySQL will teach you almost the same lessons, so the real fork in the road is relational versus document based, not which relational flavor.
>
> A concrete next step: take one of the comparisons you just read and rebuild the same small feature both ways, like a comments system with replies. Model it in Postgres with a parent id column and a recursive query, then model it in Mongo with nested documents. You will feel where each one gets awkward, which teaches more than any article does.
>
> Supabase is just Postgres with extras, so learning raw Postgres first means you are not locked into its abstractions later. Once one relational database clicks, MySQL and the rest are mostly syntax differences.

---

> **ryanisdriven**（2 分） · 2026-09-19T12:49:12+08:00　
> I think you skipped the most important part of “learning databases”: the actual database models. Relational, document, key-value, graph, time-series, columnar, etc. SQL vs NoSQL barely scratches that surface.
>
> PostgreSQL and MySQL are relational database systems. MongoDB is a document database. Supabase is a BaaS built around PostgreSQL.
>
> Learn the concepts before the logos. Otherwise you’re memorizing products instead of understanding databases.

---

> **Shashank_Mishra011**（1 分） · 2026-09-19T20:35:21+08:00　
> Ohkay

---

> **Shashank_Mishra011**（1 分） · 2026-09-19T20:35:41+08:00　
> Thanks for telling me that

---

> **Shashank_Mishra011**（1 分） · 2026-09-19T20:35:56+08:00　
> Ya

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
