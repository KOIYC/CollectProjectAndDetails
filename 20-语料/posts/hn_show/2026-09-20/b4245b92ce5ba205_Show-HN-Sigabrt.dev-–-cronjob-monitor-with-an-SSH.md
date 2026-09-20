---
type: "corpus"
item_id: "b4245b92ce5ba205"
title: "Show HN: Sigabrt.dev – cronjob monitor with an SSH TUI"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49765354"
project_url: "https://sigabrt.dev/"
author: "4815162342"
published_at: "2026-09-19T10:47:59Z"
captured_at: "2026-09-20T09:48:16+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-19"
tags:
  - 语料
  - hn_show
  - author_4815162342
  - story_49765354
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Sigabrt.dev – cronjob monitor with an SSH TUI

> [!info] 一句话导读
> Hello HN. I built this mostly to monitor the things I host myself. I know it's nothing too exciting.Anyway, the TL;DR is: Create an endpoint, and if your script…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49765354>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：4815162342　|　发布：2026-09-19T10:47:59Z
> 项目链接：<https://sigabrt.dev/>
> 采集：2026-09-20T09:48:16+08:00　|　id：`b4245b92ce5ba205`

## 正文

Hello HN. I built this mostly to monitor the things I host myself. I know it's nothing too exciting.Anyway, the TL;DR is: Create an endpoint, and if your script/cronjob fails to regularly ping it, you get notified (by email or ntfy). E.g.: 0 * * * * ./script.sh && curl -fsS https://sigabrt.dev/pulse//beat

It also has an SSH TUI which is currently experimental and read-only, mostly because I'm not sure whether it is actually useful or just a gimmick :): ssh sigabrt.dev

To use it, simply add your SSH public key in your account settings.Yes, there are services like this already, and this is minimalistic by comparison. Feedback is welcome.

## 关联链接

- https://sigabrt.dev/pulse/

## 导航

- 项目页：[[10-项目/sigabrt.dev_2e9427d7]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
