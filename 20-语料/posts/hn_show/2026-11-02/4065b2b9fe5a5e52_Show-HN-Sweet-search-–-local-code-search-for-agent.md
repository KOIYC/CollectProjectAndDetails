---
type: "corpus"
item_id: "4065b2b9fe5a5e52"
title: "Show HN: Sweet-search – local code search for agents (5–33% cheaper runs)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50326635"
project_url: "https://github.com/mrsladoje/sweet-search"
author: "mrsladoje"
published_at: "2026-11-01T15:36:02Z"
captured_at: "2026-11-02T09:37:22+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-02"
pub_day: "2026-11-01"
tags:
  - 语料
  - hn_show
  - author_mrsladoje
  - story_50326635
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Sweet-search – local code search for agents (5–33% cheaper runs)

> [!info] 一句话导读
> Hi everyone :)After almost a year of fighting windmills, I am proud to say I built sweet-search, a local code search tool for Claude Code, Codex and Opencode.It…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50326635>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：mrsladoje　|　发布：2026-11-01T15:36:02Z
> 项目链接：<https://github.com/mrsladoje/sweet-search>
> 采集：2026-11-02T09:37:22+08:00　|　id：`4065b2b9fe5a5e52`

## 正文

Hi everyone :)After almost a year of fighting windmills, I am proud to say I built sweet-search, a local code search tool for Claude Code, Codex and Opencode.It delivers 5-33% cheaper agentic runs with Sol 6.1 and Opus 5.5 with Claude Code, Codex and Opencode, with pooled solved tasks equal vs native (both 481 of 1,000 tasks pooled on 5 model*harness combos).
Measured on 200 held-out SWE-rebench tasks.
Detailed bench results are in the README.It consists of 6 tools: hybrid search with late interaction reranking, my version of grep, and others.
It also has GPU accelerated indexing (for embedding and late interaction models) and low footprint incremental indexing.Some highlights:
1. The ANN kernel is custom and very competitive with FAISS and USearch.
2. The custom MaxSim kernel is 1.4–7.3× faster than NumPy and PyTorch (reranking on CPU).
3. My hybrid-search tool is SOTA on M2CRB and zero-shot SOTA on CoSQA.
4. My custom grep tool is 2.46x faster e2e than ripgrep and ranks hits in a specific way (inspired by Sainte-Laguë).Here is the promo video I built with fframes and Opus 5.5: https://www.youtube.com/watch?v=lJzgXRQprs4Would love to hear your opinions,
Marko :)

## 关联链接

- https://www.youtube.com/watch?v=lJzgXRQprs4Would

## 导航

- 项目页：[[10-项目/github.com_97372818]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
