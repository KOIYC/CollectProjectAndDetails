---
type: "corpus"
item_id: "b1f64c90a4886849"
title: "Show HN: Jevopt: Making intelligent compiler optimisation decisions with Jev"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49795171"
project_url: "https://github.com/Ramneet-Singh/jevopt"
author: "ramneet_singh"
published_at: "2026-09-22T00:11:59Z"
captured_at: "2026-09-22T12:53:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-22"
pub_day: "2026-09-22"
tags:
  - 语料
  - hn_show
  - author_ramneet_singh
  - story_49795171
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Jevopt: Making intelligent compiler optimisation decisions with Jev

> [!info] 一句话导读
> Can Jev optimise the size of compiled binaries better than clang -Oz?Turns out it can (sometimes)! Introducing jevopt: making intelligent compiler optimisation …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49795171>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：ramneet_singh　|　发布：2026-09-22T00:11:59Z
> 项目链接：<https://github.com/Ramneet-Singh/jevopt>
> 采集：2026-09-22T12:53:31+08:00　|　id：`b1f64c90a4886849`

## 正文

Can Jev optimise the size of compiled binaries better than clang -Oz?Turns out it can (sometimes)! Introducing jevopt: making intelligent compiler optimisation decisions with Jev. I used Jev to make intelligent inlining decisions at each LLVM IR call-site. Here’s why and how I did it.Everywhere I looked, I saw cool Jev demos, so I thought I'd apply it to my area: systems programming and compilers. When optimising binary size (e.g. in embedded systems), choosing whether to inline a function call is tricky, because while it can duplicate code, it can also enable optimisations that ultimately eliminate code!Jevopt uses Jev's "intelligence" to make this choice. At each discretionary call site, Jev sees the current caller/callee LLVM IR, original C/C++ source, build context, and 7 structural facts about the program. It returns one choice: inline or keep out of line.So how well does it work? I evaluated jevopt on all 19 Embench 1.0 programs. Aggregated with geometric mean, the .text in its programs is 7.87% larger than clang -Oz, meaning that jevopt loses in aggregate. However, it sometimes achieves big wins over the mature clang heuristic.E.g., on Statemate, jevopt produces a .text of 2382B vs 5698B for clang -Oz, achieving a whopping 58% reduction! In total, it beats clang -Oz on 7/19 programs.(Clearly) jevopt is not production software, but it shows that intelligent model judgements sometimes beat heuristics. Despite the overall negative result, there are two reasons why I find it exciting:1. Measuring code size, unlike runtime, is essentially free. So if one compiles with both jevopt and -Oz, there are real gains to be had at the cost of just 1 extra compilation (and a few cents in Jev API calls)!2. As wonderfully intelligent as Jev is, I am fairly certain this is not a use case the author had in mind :) Finetuning a Jev-like model specifically for this task should improve jevopt's performance even more and might even get us an aggregate win over clang -Oz.The code is open source (github.com/Ramneet-Singh/…), and a full dashboard with the details of my Embench run is hosted at ramneet-singh.github.io/jevopt/.I plan to keep doing cool stuff at the intersection of AI and compilers, so please reach out if you're interested in this too!

## 导航

- 项目页：[[10-项目/github.com_2036b04f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
