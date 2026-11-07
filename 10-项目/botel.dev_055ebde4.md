---
type: "project"
title: "Show HN: Botel – always reachable agents you pay for only while they're working"
project_url: "https://botel.dev/"
first_seen: "2026-11-07T09:43:25+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_4ver
  - story_50393793
  - show_hn
lang: "en"
---

# Show HN: Botel – always reachable agents you pay for only while they're working

> [!info] 一句话导读
> I built a pay-as-you-go two star hotel for bots that you’re only charged for while it’s active. Typically wakes in under a second, runs on a vm, and costs very …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://botel.dev/>
> 首次收录：2026-11-07T09:43:25+08:00
> 来源渠道：HN Show HN
> 标签：author_4ver, story_50393793, show_hn
> 最新指标：点赞=4 · 评论=3 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-07T09:43:25+08:00 | HN Show HN | 点赞=4 · 评论=3 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-11-07/ad8d0e4592b30736_Show-HN-Botel-–-always-reachable-agents-you-pay-fo]] |

## 摘要正文

I built a pay-as-you-go two star hotel for bots that you’re only charged for while it’s active. Typically wakes in under a second, runs on a vm, and costs very little while it’s paused.In my free time I’ve been building a firecracker based vm orchestration platform. In order to dogfood the thing I put together a place to run agent harnesses (openclaw etc) on machines but only pay for them when they are in use. What started as a demo has grown legs into a more unique product than the platform.Botel has prebaked templates for each harness, with a daemon of mine running beside it monitoring the harness’ activity. It communicates out to the host over a link-local self api; instructing when to pause or wake next based on stored schedules. With a proxy in front to wake on http. The harnesses are preconfigured to point to my llm gateway that proxies through to openrouter.One of the biggest struggles while building it was preventing claude from going off the rails with hotel metaphors in the ui. Once it sees a joke it really strangles the hell out of it.A more real ;) awkward part is that the harnesses don’t expose exactly what I needed in order to detect activity. I'm still struggling wit…
