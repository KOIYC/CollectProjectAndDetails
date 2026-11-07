---
type: "corpus"
item_id: "ad8d0e4592b30736"
title: "Show HN: Botel – always reachable agents you pay for only while they're working"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50393793"
project_url: "https://botel.dev/"
author: "4ver"
published_at: "2026-11-06T15:46:21Z"
captured_at: "2026-11-07T09:43:25+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-07"
pub_day: "2026-11-06"
tags:
  - 语料
  - hn_show
  - author_4ver
  - story_50393793
  - show_hn
metrics: {"points": 4, "comments": 3, "engagement_velocity": 4}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:3d"
---

# Show HN: Botel – always reachable agents you pay for only while they're working

> [!info] 一句话导读
> I built a pay-as-you-go two star hotel for bots that you’re only charged for while it’s active. Typically wakes in under a second, runs on a vm, and costs very …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50393793>
> 指标：点赞=4 · 评论=3 · engagement_velocity=4
> 作者：4ver　|　发布：2026-11-06T15:46:21Z
> 项目链接：<https://botel.dev/>
> 采集：2026-11-07T09:43:25+08:00　|　id：`ad8d0e4592b30736`

## 正文

I built a pay-as-you-go two star hotel for bots that you’re only charged for while it’s active. Typically wakes in under a second, runs on a vm, and costs very little while it’s paused.In my free time I’ve been building a firecracker based vm orchestration platform. In order to dogfood the thing I put together a place to run agent harnesses (openclaw etc) on machines but only pay for them when they are in use. What started as a demo has grown legs into a more unique product than the platform.Botel has prebaked templates for each harness, with a daemon of mine running beside it monitoring the harness’ activity. It communicates out to the host over a link-local self api; instructing when to pause or wake next based on stored schedules. With a proxy in front to wake on http. The harnesses are preconfigured to point to my llm gateway that proxies through to openrouter.One of the biggest struggles while building it was preventing claude from going off the rails with hotel metaphors in the ui. Once it sees a joke it really strangles the hell out of it.A more real ;) awkward part is that the harnesses don’t expose exactly what I needed in order to detect activity. I'm still struggling with how to handle the fact that background job can be short or long lived (http/dev servers etc). I’m hoping to propose changes to hermes, openclaw, and dsh soon for a consistent way to know what kind of a job is running with annotated lifecycle hooks.Some of the nicest things about the bot hotel are:- You get a proper linux vm with sudo, so you can ssh in, scp, or run docker.- You can ask the agent to expose something publicly or privately (behind your login). A port gets a unique hostname/url. Those endpoints also wake the vm. So you could build and host a little app or self host something.- Guided telegram setup. It’s pretty awkward in general/my setup hopefully takes some of the edge off.A friend of mine who built a website for his local orienteering club has used this to make it easy for peoge on the committee to update news and events. All in all it should cost something like 40 cents a month to run so long as the club members don’t get too friendly with the agent.If you’re interested, give the thing a spin. The first 50 signups get $2 credit. Price is pretty low at 3c per GB of ram per hour awake, plus a few cents per GB-month asleep. You use credit for inference or byok.Let me know how you get on and whether you have any ideas or requests for it. Thx!

## 评论（3/3）

> **isaachawley** · 2026-11-06T16:00:15.000Z　
> Ah finally. Been waiting forever for my friend to release this. It’s pretty easy to use, cheap, and if the agent manages to wreck the system or run up a huge bill it’s not my problem. The thing is prepaid.It seems pretty efficient. You could have had subscription pricing! Leaving money on the table. I guess there’s value in being the cheapest possible approach.

---

> **4ver** · 2026-11-06T16:02:24.000Z　
> Race to the bottom from the start

---

> **isaachawley** · 2026-11-06T16:05:51.000Z　
> Congrats on shipping!

## 导航

- 项目页：[[10-项目/botel.dev_055ebde4]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
