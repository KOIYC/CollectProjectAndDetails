---
type: "corpus"
item_id: "43c3df25295972e9"
title: "Show HN: Straum – PostgreSQL Group by in Microseconds"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50510687"
project_url: "https://github.com/janbjorge/straum"
author: "jeeybee"
published_at: "2026-11-15T20:58:35Z"
captured_at: "2026-11-16T10:00:05+08:00"
lang: "en"
kind: "post"
topic: "教育/学习"
shard: "2026-11-16"
pub_day: "2026-11-15"
tags:
  - 语料
  - hn_show
  - author_jeeybee
  - story_50510687
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Straum – PostgreSQL Group by in Microseconds

> [!info] 一句话导读
> I've seen too many slow-log queries with a GROUP BY that makes Postgres blow up, so for the last two weeks or so I've been working on Straum. You declare the ag…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50510687>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：jeeybee　|　发布：2026-11-15T20:58:35Z
> 项目链接：<https://github.com/janbjorge/straum>
> 采集：2026-11-16T10:00:05+08:00　|　id：`43c3df25295972e9`

## 正文

I've seen too many slow-log queries with a GROUP BY that makes Postgres blow up, so for the last two weeks or so I've been working on Straum. You declare the aggregates as a view, and Straum answers over HTTP (other transports might be added). I've been using the New York taxi dataset as a benchmark. On the heavier GROUP BYs I see about 1,000x to 5,000x. It's written in Rust (of course).It leans on Postgres replication slots, logical or physical, to get its data. Postgres stays the source of truth.What do you think?Benchmark: https://janbjorge.github.io/straum/benchmark.html
Repo: https://github.com/janbjorge/straum

## 关联链接

- https://janbjorge.github.io/straum/benchmark.html

## 导航

- 项目页：[[10-项目/github.com_b93a55db]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`教育/学习`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
