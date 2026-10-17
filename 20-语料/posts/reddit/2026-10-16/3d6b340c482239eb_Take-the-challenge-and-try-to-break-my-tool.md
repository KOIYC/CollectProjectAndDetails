---
type: "corpus"
item_id: "3d6b340c482239eb"
title: "Take the challenge and try to break my tool."
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1wykzal/take_the_challenge_and_try_to_break_my_tool/"
project_url: "https://burst.epure.sh/"
author: "Suitable-Ad5348"
published_at: "2026-10-06T05:33:47+08:00"
captured_at: "2026-10-16T09:36:29+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-16"
pub_day: "2026-10-06"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 5, "comments": 3, "upvote_ratio": 0.86}
comments_count: 2
comments_total: 3
discovered_via: "reddit:14d+settle10"
---

# Take the challenge and try to break my tool.

> [!info] 一句话导读
> I work on Epure , a lightweight self-hosted error tracking for production apps, same Sentry SDK, change the DSN, two containers (Rust + Postgres).

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1wykzal/take_the_challenge_and_try_to_break_my_tool/>
> 指标：得分=5 · 评论=3 · 赞踩比=0.86
> 作者：Suitable-Ad5348　|　发布：2026-10-06T05:33:47+08:00
> 项目链接：<https://burst.epure.sh/>
> 采集：2026-10-16T09:36:29+08:00　|　id：`3d6b340c482239eb`

## 正文

Hi everyone.

I work on Epure , a lightweight self-hosted error tracking for production apps, same Sentry SDK, change the DSN, two containers (Rust + Postgres).

I want real floods, not synthetic load scripts, so I opened a public box:

[https://burst.epure.sh](https://burst.epure.sh)

One button sends errors from your browser for about 7 seconds. Or copy the DSN / curl and hit it from your own client. Goal is to kill the ingester container. The VM and the dashboard stay up.

Box is sized like a small VPS (2 GB RAM, 2 vCPU). There is a spike valve so duplicate spam does not instantly win , still curious how far it goes when a lot of people click at once.

Send what you can. Let's see what breaks first.

## 评论（2/3）

> **Total-Reasonable**（2 分） · 2026-10-06T16:32:39+08:00　
> The likely failure mode isn't raw ingest but cardinality: send unique tags, transaction names, exception messages, and stack frames on every event. If those are indexed or held in aggregation maps before the spike valve dedupes, memory can climb much faster than event throughput suggests.

---

> **Suitable-Ad5348**（1 分） · 2026-10-06T19:33:35+08:00　
> sure épure handles it as well. but this is just a showcase to understand and see how far the ingester (not source map decoding etc ) can go

## 关联链接

- https://burst.epure.sh

## 导航

- 项目页：[[10-项目/burst.epure.sh_a5fd1e68]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
