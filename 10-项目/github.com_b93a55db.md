---
type: "project"
title: "Show HN: Straum – PostgreSQL Group by in Microseconds"
project_url: "https://github.com/janbjorge/straum"
first_seen: "2026-11-16T10:00:05+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_jeeybee
  - story_50510687
  - show_hn
lang: "en"
---

# Show HN: Straum – PostgreSQL Group by in Microseconds

> [!info] 一句话导读
> I've seen too many slow-log queries with a GROUP BY that makes Postgres blow up, so for the last two weeks or so I've been working on Straum. You declare the ag…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/janbjorge/straum>
> 首次收录：2026-11-16T10:00:05+08:00
> 来源渠道：HN Show HN
> 标签：author_jeeybee, story_50510687, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-16T10:00:05+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-16/43c3df25295972e9_Show-HN-Straum-–-PostgreSQL-Group-by-in-Microsecon]] |

## 摘要正文

I've seen too many slow-log queries with a GROUP BY that makes Postgres blow up, so for the last two weeks or so I've been working on Straum. You declare the aggregates as a view, and Straum answers over HTTP (other transports might be added). I've been using the New York taxi dataset as a benchmark. On the heavier GROUP BYs I see about 1,000x to 5,000x. It's written in Rust (of course).It leans on Postgres replication slots, logical or physical, to get its data. Postgres stays the source of truth.What do you think?Benchmark: https://janbjorge.github.io/straum/benchmark.html Repo: https://github.com/janbjorge/straum
