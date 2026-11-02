---
type: "project"
title: "Show HN: Sweet-search – local code search for agents (5–33% cheaper runs)"
project_url: "https://github.com/mrsladoje/sweet-search"
first_seen: "2026-11-02T09:37:22+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_mrsladoje
  - story_50326635
  - show_hn
lang: "en"
---

# Show HN: Sweet-search – local code search for agents (5–33% cheaper runs)

> [!info] 一句话导读
> Hi everyone :)After almost a year of fighting windmills, I am proud to say I built sweet-search, a local code search tool for Claude Code, Codex and Opencode.It…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/mrsladoje/sweet-search>
> 首次收录：2026-11-02T09:37:22+08:00
> 来源渠道：HN Show HN
> 标签：author_mrsladoje, story_50326635, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-02T09:37:22+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-11-02/4065b2b9fe5a5e52_Show-HN-Sweet-search-–-local-code-search-for-agent]] |

## 摘要正文

Hi everyone :)After almost a year of fighting windmills, I am proud to say I built sweet-search, a local code search tool for Claude Code, Codex and Opencode.It delivers 5-33% cheaper agentic runs with Sol 6.1 and Opus 5.5 with Claude Code, Codex and Opencode, with pooled solved tasks equal vs native (both 481 of 1,000 tasks pooled on 5 model*harness combos). Measured on 200 held-out SWE-rebench tasks. Detailed bench results are in the README.It consists of 6 tools: hybrid search with late interaction reranking, my version of grep, and others. It also has GPU accelerated indexing (for embedding and late interaction models) and low footprint incremental indexing.Some highlights: 1. The ANN kernel is custom and very competitive with FAISS and USearch. 2. The custom MaxSim kernel is 1.4–7.3× faster than NumPy and PyTorch (reranking on CPU). 3. My hybrid-search tool is SOTA on M2CRB and zero-shot SOTA on CoSQA. 4. My custom grep tool is 2.46x faster e2e than ripgrep and ranks hits in a specific way (inspired by Sainte-Laguë).Here is the promo video I built with fframes and Opus 5.5: https://www.youtube.com/watch?v=lJzgXRQprs4Would love to hear your opinions, Marko :)
