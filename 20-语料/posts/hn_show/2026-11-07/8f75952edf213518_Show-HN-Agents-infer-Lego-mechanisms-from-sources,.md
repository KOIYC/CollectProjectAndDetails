---
type: "corpus"
item_id: "8f75952edf213518"
title: "Show HN: Agents infer Lego mechanisms from sources, then animate them"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50397325"
project_url: "https://github.com/anteloc/ldraw-mecha/tree/v0.5.0"
author: "antelocnova"
published_at: "2026-11-06T19:41:20Z"
captured_at: "2026-11-07T09:43:25+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-07"
pub_day: "2026-11-06"
tags:
  - 语料
  - hn_show
  - author_antelocnova
  - story_50397325
  - show_hn
metrics: {"points": 24, "comments": 1, "engagement_velocity": 24}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Agents infer Lego mechanisms from sources, then animate them

> [!info] 一句话导读
> Hi there :)Around a month ago, I released LDraw Nova, an agentic toolset for assembling LEGO CAD models by generating LDraw source code files.For more details, …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50397325>
> 指标：点赞=24 · 评论=1 · engagement_velocity=24
> 作者：antelocnova　|　发布：2026-11-06T19:41:20Z
> 项目链接：<https://github.com/anteloc/ldraw-mecha/tree/v0.5.0>
> 采集：2026-11-07T09:43:25+08:00　|　id：`8f75952edf213518`

## 正文

Hi there :)Around a month ago, I released LDraw Nova, an agentic toolset for assembling LEGO CAD models by generating LDraw source code files.For more details, here's the Show HN post:https://news.ycombinator.com/item?id=49937916From the comments, I got the impression that there was quite an interest in seeing not only AI-generated LEGO models, but also AI-animated LEGO ones.I took a look at results from past experiments, and found it feasible to use agentic LLMs for:- analyzing the LDraw source code for LEGO models
- reverse-engineer! the mechanisms present by reading the descriptions and sequence for the parts there
- and then, animate them via Blender!This new project I'm presenting, LDraw Mecha, is the end result and proof that can be done:- Read specially annotated LDraw LEGO models .mpd source files
- Infer the model structure in terms of submodels
- Select from those the ones that are mechanisms
- Plan animations
- Execute them in BlenderIn summary, from an initial .mpd source file, get a rigged and animated version for the model as a Blender (.blend) file.See the results here:- Repo (v0.5.0): https://github.com/anteloc/ldraw-mecha/tree/v0.5.0
- Gallery: https://github.com/anteloc/ldraw-mecha/blob/v0.5.0/GALLERY.m...
- Process: https://github.com/anteloc/ldraw-mecha/blob/v0.5.0/PROCESS.m...This project is very unusual, I'd really appreciate some feedback from the community.Cheers!

## 评论（1/1）

> **hmartin** · 2026-11-06T22:49:41.000Z　
> Hi anteloc, congrats on some cool projects! Look forward to playing with them over the weekend.pyldraw3 creator here btw... would love to find a forum where we (i.e. the handful of us trying to push lego tooling forward) can collaborate and communicate better.My current main effort is deterministic model/instructions building but I've been thinking a lot about how to incorporate agents: https://github.com/hbmartin/legolization

## 关联链接

- https://github.com/anteloc/ldraw-mecha/blob/v0.5.0/GALLERY.m...
- https://github.com/anteloc/ldraw-mecha/blob/v0.5.0/PROCESS.m...This
- https://news.ycombinator.com/item?id=49937916From

## 导航

- 项目页：[[10-项目/github.com_add023bd]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
