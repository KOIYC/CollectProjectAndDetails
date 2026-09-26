---
type: "corpus"
item_id: "23abe73de8e10d58"
title: "Show HN: Obsidian Plugin for OpenModelica"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49848452"
project_url: "https://community.obsidian.md/plugins/modelica-studio"
author: "cs3f16"
published_at: "2026-09-25T18:53:10Z"
captured_at: "2026-09-26T09:41:08+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-26"
pub_day: "2026-09-25"
tags:
  - 语料
  - hn_show
  - author_cs3f16
  - story_49848452
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Obsidian Plugin for OpenModelica

> [!info] 一句话导读
> I created an Obsidian plugin that serves as a front-end for OpenModelica that allows you to model and simulate cyber-physical systems (mechanical, fluid, magnet…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49848452>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：cs3f16　|　发布：2026-09-25T18:53:10Z
> 项目链接：<https://community.obsidian.md/plugins/modelica-studio>
> 采集：2026-09-26T09:41:08+08:00　|　id：`23abe73de8e10d58`

## 正文

I created an Obsidian plugin that serves as a front-end for OpenModelica that allows you to model and simulate cyber-physical systems (mechanical, fluid, magnetic, thermal, etc.) or a mix of all these systems all inside Obsidian.What is special about Modelica is that it is acausal: components do not have fixed input/output roles. You describe physical relationships with equations and connections, and the equations do not need to be written in a step-by-step order. Modelica (language) or OpenModelica (software) flattens the model into a simultaneous equation system (a system of differential algebraic equations (DAEs)) and then determines the computational causality and order needed to simulate it.As a disclaimer, I used AI to build it but not in a sloppy way. I have spent a lot of time testing it and making sure it's functional and accurate. And I hope it may help others to utilize such an underrated tool for learning/researching, as this is my main usage for it.

## 导航

- 项目页：[[10-项目/community.obsidian.md_b3180dc5]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
