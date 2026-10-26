---
type: "project"
title: "Show HN: simdown – use SIMD to parse Markdown at ~1 GB/s"
project_url: "https://github.com/trevorah/simdown"
first_seen: "2026-10-26T09:42:36+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_trevorah
  - story_50236813
  - show_hn
lang: "en"
---

# Show HN: simdown – use SIMD to parse Markdown at ~1 GB/s

> [!info] 一句话导读
> The SIMD path currently needs arm64 (NEON) and GOEXPERIMENT=simd. I've only benchmarked on an Apple M4, but it should help on any arm64 chip (Graviton, Ampere, …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/trevorah/simdown>
> 首次收录：2026-10-26T09:42:36+08:00
> 来源渠道：HN Show HN
> 标签：author_trevorah, story_50236813, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-26T09:42:36+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-26/b460e688fe82dec9_Show-HN-simdown-–-use-SIMD-to-parse-Markdown-at-~1]] |

## 摘要正文

The SIMD path currently needs arm64 (NEON) and GOEXPERIMENT=simd. I've only benchmarked on an Apple M4, but it should help on any arm64 chip (Graviton, Ampere, etc.). Elsewhere it falls back to a scalar path that does ~300 MB/s, still ahead of cmark and goldmark.If you know of a faster CommonMark parser, please tell me and I'll add it to the benchmarks.Under the hood, it borrows a lot from this paper on using simd for json parsing: https://arxiv.org/abs/1902.08318
