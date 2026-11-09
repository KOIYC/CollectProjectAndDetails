---
type: "project"
title: "Show HN: Nino – Fastest C# serializer, safe on untrusted input, also TS/Go/Rust"
project_url: "https://github.com/JasonXuDeveloper/Nino"
first_seen: "2026-11-09T09:39:29+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_jnx11
  - story_50413601
  - show_hn
lang: "en"
---

# Show HN: Nino – Fastest C# serializer, safe on untrusted input, also TS/Go/Rust

> [!info] 一句话导读
> Nino is a source-generated binary serializer for C#, and as far as we know the fastest one. In the same BenchmarkDotNet run on GitHub runners against MemoryPack…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/JasonXuDeveloper/Nino>
> 首次收录：2026-11-09T09:39:29+08:00
> 来源渠道：HN Show HN
> 标签：author_jnx11, story_50413601, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-09T09:39:29+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-11-09/130d03f6e17e1760_Show-HN-Nino-–-Fastest-C-serializer,-safe-on-untru]] |

## 摘要正文

Nino is a source-generated binary serializer for C#, and as far as we know the fastest one. In the same BenchmarkDotNet run on GitHub runners against MemoryPack 1.21.4, it serializes classes and polymorphic types 3.5–7.2x faster and deserializes them 1.7–2.1x faster (arrays of unmanaged structs are on par). Deserializing into existing objects allocates nothing. Reproduce: https://nino.xgamedev.net/en/docs/v4/benchmarksIt is built to read bytes you do not trust: lengths are checked before allocating, depth is bounded, hash flooding is limited, and the read paths are fuzzed in CI.The bytes are a spec, not a memory dump, so CoreCLR, Mono, IL2CPP and 32-bit hosts write the same bytes, and runtimes for TypeScript, Go and Rust pass the same conformance corpus.Trade-offs: positional by default (VersionTolerant or Keyed for stored data), a 4-byte type id on polymorphic values, no System.Type, needs C# 9 and Roslyn 4.3+.Docs: https://nino.xgamedev.net
