---
type: "corpus"
item_id: "3da982abdde7000e"
title: "Show HN: Vanish moves heavy computation off your laptop"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49871223"
project_url: "https://vanishcompute.com/"
author: "fcesco"
published_at: "2026-09-27T21:51:29Z"
captured_at: "2026-09-28T09:47:28+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-28"
pub_day: "2026-09-27"
tags:
  - 语料
  - hn_show
  - author_fcesco
  - story_49871223
  - show_hn
metrics: {"points": 3, "comments": 2, "engagement_velocity": 3}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Vanish moves heavy computation off your laptop

> [!info] 一句话导读
> I was tired of agents draining my battery and my laptop being unusable so I made vanish, a CLI tool to run your commands in the cloud.Vanish is designed to be p…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49871223>
> 指标：点赞=3 · 评论=2 · engagement_velocity=3
> 作者：fcesco　|　发布：2026-09-27T21:51:29Z
> 项目链接：<https://vanishcompute.com/>
> 采集：2026-09-28T09:47:28+08:00　|　id：`3da982abdde7000e`

## 正文

Hi HN
I was tired of agents draining my battery and my laptop being unusable so I made vanish, a CLI tool to run your commands in the cloud.Vanish is designed to be process transparent so just prefixing any command with vanish should work, like doing `vanish cargo test`

## 评论（2/2）

> **cs1996** · 2026-09-27T22:05:57.000Z　
> trying to understand pricing. How does this compare to getting a free google cloud vm?

---

> **fcesco** · 2026-09-27T22:26:25.000Z　
> A VM you manage yourself is cheaper per hour. An 8 vCPU / 16 GiB machine costs $0.66/hr with us, versus about $0.42/hr for an on-demand EC2 c7i.2xlarge. Roughly 1.5x. GCP's free tier has 1 GB of RAM and shared CPU, afaik, so it's pretty limited for builds.The premium is for not doing the infra dance yourself.
> Forget the EC2 instance is up and it's $10.18/day.
> We bill by the second while a command runs, so against a VM you leave running all day, your break even is around 15 hours of compute.I used to run my VMs and I would forget to tear them down and got tired of rsyncing and explaining to my agents what the setup was or where to run stuff.That's what I wanted to fix. Your uncommitted working tree runs remotely, results come back to disk, exit codes and Ctrl-C work, and there's nothing to remember to shut down. Adding vanish cargo test just works as cargo testIf you keep on top of your VMs and don't mind the syncing, running your own will be cheaper.

## 导航

- 项目页：[[10-项目/vanishcompute.com_dd73d87e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
