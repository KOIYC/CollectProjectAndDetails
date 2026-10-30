---
type: "corpus"
item_id: "0f9497907d07c339"
title: "Show HN: Wanim – Manim in the browser, but 1/20 smaller"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50291932"
project_url: "https://github.com/Acfboy/Wanim"
author: "Acfboy"
published_at: "2026-10-29T16:41:27Z"
captured_at: "2026-10-30T09:46:09+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-30"
pub_day: "2026-10-29"
tags:
  - 语料
  - hn_show
  - author_Acfboy
  - story_50291932
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Wanim – Manim in the browser, but 1/20 smaller

> [!info] 一句话导读
> Hi HN, I really like Manim, but when I tried to use it to make interactive small demos on the web, I found that no project can simultaneously satisfy running or…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50291932>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：Acfboy　|　发布：2026-10-29T16:41:27Z
> 项目链接：<https://github.com/Acfboy/Wanim>
> 采集：2026-10-30T09:46:09+08:00　|　id：`0f9497907d07c339`

## 正文

Hi HN, I really like Manim, but when I tried to use it to make interactive small demos on the web, I found that no project can simultaneously satisfy running original manim python code without carrying the bulky pyodide which makes it impossible to embed. So I made one. My idea is to rewrite a js library that is almost completely identical to manim, and then patch rapydscript-ng to translate the original code to js, and support numpy syntax. It looks surprisingly good, supports the vast majority of syntax, and the size is only about 1M (1/20 of pyodide)! You can try it at https://wanim.org/playground, and there is an interactive courseware example at https://wanim.org/blog.

## 关联链接

- https://wanim.org/blog.
- https://wanim.org/playground,

## 导航

- 项目页：[[10-项目/github.com_c28cc1d8]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
