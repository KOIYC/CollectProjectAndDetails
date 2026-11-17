---
type: "corpus"
item_id: "3b3c61b26c9a76b3"
title: "Show HN: T'Pico, a classless CSS library for modern browsers"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50522950"
project_url: "https://github.com/dday9/t-pico"
author: "dday9"
published_at: "2026-11-16T20:40:58Z"
captured_at: "2026-11-17T11:09:12+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-17"
pub_day: "2026-11-16"
tags:
  - 语料
  - hn_show
  - author_dday9
  - story_50522950
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: T'Pico, a classless CSS library for modern browsers

> [!info] 一句话导读
> Lucas Larroche declared on Oct 4, 2026 that he was archiving PicoCSS and it really upset me. Here was a library that I promoted, used in several websites, and r…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50522950>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：dday9　|　发布：2026-11-16T20:40:58Z
> 项目链接：<https://github.com/dday9/t-pico>
> 采集：2026-11-17T11:09:12+08:00　|　id：`3b3c61b26c9a76b3`

## 正文

Lucas Larroche declared on Oct 4, 2026 that he was archiving PicoCSS and it really upset me. Here was a library that I promoted, used in several websites, and really saw as the future of minimalistic web development.Starting last month sometime, I decided that I would rewrite the library to not only address some of the issues Lucas outlined such as using OKLCH colors, cascade layers, and the Popover API, but to also make some architectural decisions that I didn't agree. Last week, I finally pushed everything up on GitHub. There is a full demo on jsfiddle too: https://jsfiddle.net/bLpsf2jd/The name I decided to go with is T'Pico, which is a double entendre not only representing the minimalistic nature of Pico's original vision but also as a play on the Cajun norm of putting "T" in front of people's names (like father "Bob" and son "T'Bob"); in a sense T'Pico is a child born out of PicoCSS.T'Pico wasn't a one-to-one rewrite of PicoCSS, it is a complete rewrite, not a drop-in replacement. Outside of adding a few new components such as the offcanvas, classless version of the dropdown component, the toolbar component, etc., there were some things I left out entirely. For example, rather than hijacking the RTL attribute to manage visual appearances of components, I felt like it was better left out entirely and allow the native RTL browser rendering do its thing.I am looking for feedback on improving the library. I have been going through the original Pico discussions to look for what people were talking about there and even implemented a bit of it when doing the initial rewrite.Full disclaimer if you decide to check out the repository: I basically gave ChatGPT my source code for T'Pico and told it to write the documentation for me. This saved me hours in building out the documentation. I know some will poo-poo on that, but it really helped me with the tedious stuff that I'm not really good at. In case you can't tell by this post, I cant spel are grammur goodly.Anyways, I look forward to hearing y'all's feedback and let's keep the move to more minimalistic web development going!

## 关联链接

- https://jsfiddle.net/bLpsf2jd/The

## 导航

- 项目页：[[10-项目/github.com_8689e85e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
