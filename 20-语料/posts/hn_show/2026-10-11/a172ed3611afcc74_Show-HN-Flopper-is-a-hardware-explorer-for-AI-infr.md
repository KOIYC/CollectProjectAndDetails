---
type: "corpus"
item_id: "a172ed3611afcc74"
title: "Show HN: Flopper is a hardware explorer for AI infrastructure and beyond"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50035826"
project_url: "https://flopper.io/"
author: "triwats"
published_at: "2026-10-10T18:42:44Z"
captured_at: "2026-10-11T09:43:53+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-11"
pub_day: "2026-10-10"
tags:
  - 语料
  - hn_show
  - author_triwats
  - story_50035826
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Flopper is a hardware explorer for AI infrastructure and beyond

> [!info] 一句话导读
> Hello!I built Flopper to make it easier to compare GPUs and understand the tradeoffs for workloads for AI and beyond.When researching GPUs from say Nvidia, AMD,…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50035826>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：triwats　|　发布：2026-10-10T18:42:44Z
> 项目链接：<https://flopper.io/>
> 采集：2026-10-11T09:43:53+08:00　|　id：`a172ed3611afcc74`

## 正文

Hello!I built Flopper to make it easier to compare GPUs and understand the tradeoffs for workloads for AI and beyond.When researching GPUs from say Nvidia, AMD, and Huawei, I kept running into the same problem: specs were scattered across datasheets, and matching them to available configurations, vendors, and prices was cumbersome and a bit weird and frankly annoyingggg! AMD made me make an account :(So I started a place to bring that information together.Flopper lets you compare GPU specs, including TDP and compute throughput in terms of flops/tops, alongside estimates for AI workloads or other compute workloads (say, ~FP32 based) I recently added pricing data from dozens of providers to help track how prices change over time. Getting reliable quotes for systems like the NVL72 is still particularly difficult tbh, not sure how I can tell you how much that costs easily due to them being behind large procurement contracts and big multi-nationals.One thing that's become fairlyyyy clear is the interest in consumer cards and local LLMs.The bigger challenge is connecting advertised specs to real-world performance. In our testing so far, I’ve seen roughly 85% of advertised throughput, but that’s a ballpark observation for the workloads I’ve tested, not a general rule and so variable (power, cooling, workload etc).I'm considering a CLI that lets people run benchmarks and submit results, potentially using MLPerf as an automation? That way, we can all compare quoted performance with the workload, configuration etc.I'd love feedback: what information is missing, how can I improve it? And what would you need to see to trust a community-submitted benchmark?Corrections and additions also very welcome - some of the measurements are best efforts (and simple multiplications) but I hope it's of some use.Thanks for looking :)

## 导航

- 项目页：[[10-项目/flopper.io_4206e870]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
