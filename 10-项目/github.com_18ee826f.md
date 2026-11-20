---
type: "project"
title: "Show HN: ZXC 1.0 – Asymmetric compression codec in C, now in ClickHouse beta"
project_url: "https://github.com/hellobertrand/zxc/releases/tag/v1.0.0"
first_seen: "2026-11-20T09:45:52+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_pollop_
  - story_50560067
  - show_hn
lang: "en"
---

# Show HN: ZXC 1.0 – Asymmetric compression codec in C, now in ClickHouse beta

> [!info] 一句话导读
> ZXC v1.0.0 - Hydrogen

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/hellobertrand/zxc/releases/tag/v1.0.0>
> 首次收录：2026-11-20T09:45:52+08:00
> 来源渠道：HN Show HN
> 标签：author_pollop_, story_50560067, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-20T09:45:52+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-11-20/9334d19cc38c23c0_Show-HN-ZXC-1.0-–-Asymmetric-compression-codec-in]] |

## 摘要正文

# ZXC v1.0.0 - Hydrogen  - Tag: v1.0.0 - Repository: hellobertrand/zxc - Published: 2026-11-11T08:01:51Z - Author: hellobertrand  ---  # Release Notes  v1.0.0 is a major release, and the stability release: the format is frozen, the C API is settled, and the compressed bytes do not change.  Its codename is **Hydrogen**, element 1. Each later major or minor releases will take their codenames from the next elements of Mendeleev's periodic table. Patch releases keep the codename of their series.  **Format v9 is frozen. Archives written by v0.15.0 decode as they are, and v1.0.0 writes byte-identical archives at levels 1 to 7. Any later format change is additive: newer readers keep reading older archives.**  What does change is the surface around those bytes. Settings move from option structs to parameters set on a context, which lets the API grow without breaking the ABI. The CLI now keeps its input files by default, and the bindings verify checksums by default when decoding.  > ⚠️ **Breaking change (API, ABI, CLI and bindings). No archive migration from v0.15.x.** The **soname moves to `libzxc.so.6`**, so programs linked against `libzxc.so.5` must be rebuilt, and C callers must update …
