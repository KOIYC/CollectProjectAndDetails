---
type: "corpus"
item_id: "a381727dba9ef6ce"
title: "Show HN: CheckOwners to find your repo's hidden single points of failure"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50330601"
project_url: "https://github.com/smusali/checkOwners"
author: "smusali"
published_at: "2026-11-01T22:29:45Z"
captured_at: "2026-11-02T09:37:22+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-02"
pub_day: "2026-11-01"
tags:
  - 语料
  - hn_show
  - author_smusali
  - story_50330601
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: CheckOwners to find your repo's hidden single points of failure

> [!info] 一句话导读
> Hey HN Community!I created checkOwners to solve a problem by many engineering teams: who knows your codebase, and what will happen when they go away?This is an …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50330601>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：smusali　|　发布：2026-11-01T22:29:45Z
> 项目链接：<https://github.com/smusali/checkOwners>
> 采集：2026-11-02T09:37:22+08:00　|　id：`a381727dba9ef6ce`

## 正文

Hey HN Community!I created checkOwners to solve a problem by many engineering teams: who knows your codebase, and what will happen when they go away?This is an open-source, local-first tool which performs analysis based on Git history in order to find hidden knowledge risk in repositories.It is able to recognize true experts, recognize out-of-date ownership definitions, find knowledge bottlenecks, propose review candidates, and model what would happen when contributors go away.All the magic happens on your own local system without uploading source code or an LLM. It also works within GitHub Actions.Try it:
```
pip install checkowners
checkowners audit
checkowners risk
```Would appreciate any feedback from maintainers and platform engineers regarding the accuracy of Git history reflection of expertise and findings of risk analysis.

## 导航

- 项目页：[[10-项目/github.com_ac150ff6]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
