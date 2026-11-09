---
type: "corpus"
item_id: "130d03f6e17e1760"
title: "Show HN: Nino – Fastest C# serializer, safe on untrusted input, also TS/Go/Rust"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50413601"
project_url: "https://github.com/JasonXuDeveloper/Nino"
author: "jnx11"
published_at: "2026-11-08T14:20:43Z"
captured_at: "2026-11-09T09:39:29+08:00"
lang: "en"
kind: "post"
topic: "游戏"
shard: "2026-11-09"
pub_day: "2026-11-08"
tags:
  - 语料
  - hn_show
  - author_jnx11
  - story_50413601
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Nino – Fastest C# serializer, safe on untrusted input, also TS/Go/Rust

> [!info] 一句话导读
> Nino is a source-generated binary serializer for C#, and as far as we know the fastest one. In the same BenchmarkDotNet run on GitHub runners against MemoryPack…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50413601>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：jnx11　|　发布：2026-11-08T14:20:43Z
> 项目链接：<https://github.com/JasonXuDeveloper/Nino>
> 采集：2026-11-09T09:39:29+08:00　|　id：`130d03f6e17e1760`

## 正文

Nino is a source-generated binary serializer for C#, and as far as we know the fastest one. In the same BenchmarkDotNet run on GitHub runners against MemoryPack 1.21.4, it serializes classes and polymorphic types 3.5–7.2x faster and deserializes them 1.7–2.1x faster (arrays of unmanaged structs are on par). Deserializing into existing objects allocates nothing. Reproduce: https://nino.xgamedev.net/en/docs/v4/benchmarksIt is built to read bytes you do not trust: lengths are checked before allocating, depth is bounded, hash flooding is limited, and the read paths are fuzzed in CI.The bytes are a spec, not a memory dump, so CoreCLR, Mono, IL2CPP and 32-bit hosts write the same bytes, and runtimes for TypeScript, Go and Rust pass the same conformance corpus.Trade-offs: positional by default (VersionTolerant or Keyed for stored data), a 4-byte type id on polymorphic values, no System.Type, needs C# 9 and Roslyn 4.3+.Docs: https://nino.xgamedev.net

## 关联链接

- https://nino.xgamedev.net
- https://nino.xgamedev.net/en/docs/v4/benchmarksIt

## 导航

- 项目页：[[10-项目/github.com_b36dbea1]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`游戏`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
