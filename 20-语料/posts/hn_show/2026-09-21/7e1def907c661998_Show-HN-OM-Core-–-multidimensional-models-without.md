---
type: "corpus"
item_id: "7e1def907c661998"
title: "Show HN: OM Core – multidimensional models without spreadsheet cell formulas"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48733642"
project_url: "https://github.com/cloudcell/om-core"
author: "cloudcell"
published_at: "2026-06-30T14:58:10Z"
captured_at: "2026-09-21T01:44:26+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_cloudcell
  - story_48733642
  - show_hn
metrics: {"points": 14, "comments": 6, "engagement_velocity": 14}
comments_count: 6
comments_total: 6
discovered_via: "hn:show_hn:113d"
---

# Show HN: OM Core – multidimensional models without spreadsheet cell formulas

> [!info] 一句话导读
> Show HN: OM Core – multidimensional models without spreadsheet cell formulas

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48733642>
> 指标：点赞=14 · 评论=6 · engagement_velocity=14
> 作者：cloudcell　|　发布：2026-06-30T14:58:10Z
> 项目链接：<https://github.com/cloudcell/om-core>
> 采集：2026-09-21T01:44:26+08:00　|　id：`7e1def907c661998`

## 正文

Show HN: OM Core – multidimensional models without spreadsheet cell formulas

## 评论（6/6）

> **cloudcell** · 2026-06-30T14:58:26.000Z　
> I made OM Core public today.It is an early alpha multidimensional modeling engine. The main idea is to separate the model from the grid: dimensions, cubes, rules, and views instead of spreadsheet cell formulas.I am looking for feedback from people who have built or maintained spreadsheet models, especially on whether the abstraction is understandable.Docs: https://cloudcell.github.io/om-docs/

---

> **densekernel** · 2026-07-03T14:59:03.000Z　
> https://x.com/andrewchen/status/2031532980032909640 - related?"prediction re the end of spreadsheetsAI code gen means that anything that is currently modeled as a spreadsheet is better modeled in code. You get all the advantages of software - libraries, open source, AI, all the complexity and expressiveness."

---

> **whiw** · 2026-07-07T14:42:25.000Z　
> I've read the docs but I haven't tried it yet. I like the idea of storing n-dimensional data in an n-dimensional table, and I like the separation between the data ('cube') and the views and rules. I like that the rules operate on slices of the data rather than individual cells.This occupies the space between traditional spreadsheets (simple UI but limited to 2-d) python (multi-dimensional data, and python or tensors (multi-dimensional data, but coding required).I feel that the current data input is a bit cumbersome. There's a lot to type to enter just one cell value, and multi-dimensional tables contain a lot of cells. A more succinct alternative for data entry could be something like python/numpy multi-dimensional tables: [[[a, b, c], [d, e, f]], [[g, h, i], [j, k, l]]].Data entry from a view grid (to a 2-d slice of the 'cube') would be more familiar, like a spreadsheet.A data import feature (from csv, etc) would be useful too.'Cube' has 3d connotations: 'ngrid' or 'ndata' could be less confusing.I didn't see any functions like sum or product (or most other spreadsheet functions) to operate on data slices. I'm guessing that this is still proof of concept at the moment.I do hope this goes further.

---

> **cyanydeez** · 2026-07-03T20:57:02.000Z　
> the only way that's possible is if you can use a spreadsheet to test the code.

---

> **cloudcell** · 2026-07-04T15:50:33.000Z　
> “Anything that is currently modeled” would be true if we could guarantee the correctness of AI-generated code.Business people prefer the familiarity of spreadsheets, or at least some kind of grid. At the same time, I am working on this software out of frustration with spreadsheets, because users are forced to translate A1*B2-style addresses into business meaning.So I agree that code is one possible direction. But I think there is also a middle ground: business rules over dimensions. Enterprise tools like TM1 have explored this direction for decades.

---

> **cloudcell** · 2026-07-09T21:50:51.000Z　
> Thank you for you feedback!The goal of this software is to address the gap in the open source ecosystem. This multidimensional approach for modeling (and financial planning/forecasting) is over 40 years old. Systems like TM1 by IBM, Anaplan (to name just a few), have been using it for many decades.The reason for using the word 'cube' is mainly familiarity of users with the concept of OLAP cube (https://en.wikipedia.org/wiki/OLAP_cube), which is what this tech should perhaps be called.As for data input... indeed, there is some room for improvement: there are 3 ways of editing a rule: via the rule bar, directly on the grid, and modifying an existing rule using the rule panel. We need feedback to decide which way to keep and what to remove. UX/UI is extremely tricky. Oh, there's also a way to insert a rule via the terminal (text user interface command line).As for operation on slices, a slice can be defined using specific items in a dimension and omitting others (which will create a data 'slice'): for example if you have a 'cube' D with dimensions A B and C, and each dimension has items 1 2 and 3, then you can define a sum over a slice through this cube via this rule "=sum(D::a.1)" or, more explicitly, "=sum(D::a.1:b.:c.)", if written directly in a cell.You can fill the whole cube with some value, say, 1, by defining a rule `* = 1` in that particular cube via the rule bar. The rule should produce the total of 9.I hope this is helpful. Feel free to join the project's discord server (https://discord.gg/GfU5ypAbaD) I will be happy to explain.PSThe functions are documented here: https://cloudcell.github.io/om-docs/reference/functions/There's an Excel import plugin (available via menu 'Plugins') that allowed importing basic Excel files (stripping all formatting, however), but I guess it might need a few hours of work at the moment.

## 导航

- 项目页：[[10-项目/github.com_91e69c04]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
