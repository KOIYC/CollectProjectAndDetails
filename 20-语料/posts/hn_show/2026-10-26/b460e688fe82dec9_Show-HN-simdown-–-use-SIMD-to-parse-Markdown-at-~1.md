---
type: "corpus"
item_id: "b460e688fe82dec9"
title: "Show HN: simdown – use SIMD to parse Markdown at ~1 GB/s"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50236813"
project_url: "https://github.com/trevorah/simdown"
author: "trevorah"
published_at: "2026-10-25T22:47:18Z"
captured_at: "2026-10-26T09:42:36+08:00"
lang: "en"
kind: "post"
topic: "未分类"
shard: "2026-10-26"
pub_day: "2026-10-25"
tags:
  - 语料
  - hn_show
  - author_trevorah
  - story_50236813
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: simdown – use SIMD to parse Markdown at ~1 GB/s

> [!info] 一句话导读
> The SIMD path currently needs arm64 (NEON) and GOEXPERIMENT=simd. I've only benchmarked on an Apple M4, but it should help on any arm64 chip (Graviton, Ampere, …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50236813>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：trevorah　|　发布：2026-10-25T22:47:18Z
> 项目链接：<https://github.com/trevorah/simdown>
> 采集：2026-10-26T09:42:36+08:00　|　id：`b460e688fe82dec9`

## 正文

The SIMD path currently needs arm64 (NEON) and GOEXPERIMENT=simd. I've only benchmarked on an Apple M4, but it should help on any arm64 chip (Graviton, Ampere, etc.). Elsewhere it falls back to a scalar path that does ~300 MB/s, still ahead of cmark and goldmark.If you know of a faster CommonMark parser, please tell me and I'll add it to the benchmarks.Under the hood, it borrows a lot from this paper on using simd for json parsing: https://arxiv.org/abs/1902.08318

## 关联链接

- https://arxiv.org/abs/1902.08318

## 导航

- 项目页：[[10-项目/github.com_8de7bc61]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`未分类`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
