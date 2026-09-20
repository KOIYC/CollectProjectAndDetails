---
type: "corpus"
item_id: "a6af708e167e463b"
title: "Worlds"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SideProject/comments/1wibd4l/worlds/"
author: "Soggy-Illustrator-38"
published_at: "2026-09-17T06:05:08+08:00"
captured_at: "2026-09-20T09:24:22+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - reddit
  - r/SideProject
metrics: {"score": 6, "comments": 0, "upvote_ratio": 0.87}
comments_count: 0
comments_total: 0
discovered_via: "reddit:7d+settle3"
---

# Worlds

> [!info] 一句话导读
> Turns out both problems traced back to the same thing. We'd split the voice data correctly, but the event pipeline logging "message sent" and "reply received" w…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SideProject/comments/1wibd4l/worlds/>
> 指标：得分=6 · 评论=0 · 赞踩比=0.87
> 作者：Soggy-Illustrator-38　|　发布：2026-09-17T06:05:08+08:00
> 项目链接：—
> 采集：2026-09-20T09:24:22+08:00　|　id：`a6af708e167e463b`

## 正文

Turns out both problems traced back to the same thing. We'd split the voice data correctly, but the event pipeline logging "message sent" and "reply received" was still writing to one shared table with a client\_id column nobody had indexed. Under load, race conditions meant one client's outbound sometimes got counted toward another client's conversions.

We didn't notice because the totals looked fine on our end. It surfaced when one of our three paying businesses asked why our dashboard didn't match what they were seeing in their own inbox.

Took two days to rebuild the pipeline with hard per-client partitioning instead of a shared table with a filter, then backfill three weeks of events and recalculate everything.

The honest numbers came out better for two of the three businesses and worse for one. Worse is not a fun call to make to a paying customer, but running

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
