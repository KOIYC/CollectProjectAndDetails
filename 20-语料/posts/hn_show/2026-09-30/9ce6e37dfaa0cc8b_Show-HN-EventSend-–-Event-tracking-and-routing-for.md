---
type: "corpus"
item_id: "9ce6e37dfaa0cc8b"
title: "Show HN: EventSend – Event tracking and routing for solo founders and SaaS teams"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49902837"
project_url: "https://eventsend.io/"
author: "mytinyrocket"
published_at: "2026-09-30T00:33:13Z"
captured_at: "2026-09-30T18:28:30+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-30"
pub_day: "2026-09-30"
tags:
  - 语料
  - hn_show
  - author_mytinyrocket
  - story_49902837
  - show_hn
metrics: {"points": 3, "comments": 2, "engagement_velocity": 3}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: EventSend – Event tracking and routing for solo founders and SaaS teams

> [!info] 一句话导读
> I was tired of learning about failed payments by my customers and not from my system, so I built an event tracker that allowed me to have a searchable feed of t…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49902837>
> 指标：点赞=3 · 评论=2 · engagement_velocity=3
> 作者：mytinyrocket　|　发布：2026-09-30T00:33:13Z
> 项目链接：<https://eventsend.io/>
> 采集：2026-09-30T18:28:30+08:00　|　id：`9ce6e37dfaa0cc8b`

## 正文

I was tired of learning about failed payments by my customers and not from my system, so I built an event tracker that allowed me to have a searchable feed of the important events happening for my apps and route the ones I cared about to my phone so I could take action quickly.EventSend is an event tracker and a router, your system sends the important events you want to track: signups, failed payments, new subscriptions, deployments, a new purchase, etc. so they end up in a searchable and filterable feed that you can use to have quick insight about what's happening with your product.Then there's also the routing side of things, those important events you want to know the moment they happen, and not once you go into your Grafana Loki logs, can be routed to your phone, Slack, Discord, Telegram or any other system or service via a signed webhook. You can configure rules, alerts, quiet hours or smart rollups to have the signal you're looking for.All event's are retried with a reasonable backoff, circuit breakers and limiters maintain the prviders and system reliable.
If we got a 401 or 403, your destination will be inactivated instead of retried and you'll be notified for you to update the configuration.I've been a software engineer for about a decade, and I can tell you this is not a weekend project done on with a single prompt pass, the infrastructure and tooling behind the project is solid, my expertise around distributed systems was put in practice with this one: distributed Elixir, Phoenix and Postgres provide the main stack, with some other technologies that support the event queues aside. So, it's a reliable system.I've launched several other projects, some running for years in production and I'm successfully using EventSend to track what's happening on all my products from my phone.There's also an MCP connector so you can ask stuff like "did anything failed during the night?" or "what did user cus_Qw3Sx did before it churned?" to get a user's timeline or any insights you're interested in.There's a forever free plan, in case you can to try it.Happy to answer any questions.

## 评论（2/2）

> **pggalaviz** · 2026-09-30T02:30:02.000Z　
> This seems helpful, why did you chose the Elixir stack?
> Are you planning on supporting more services for the alerting?I'd like to try it for something I'm building, my main concern is the integration part

---

> **mytinyrocket** · 2026-09-30T02:35:34.000Z　
> I've been working with Elixir for over 7 years, it's out of the box concurrency model and fault tolerance makes it a great candidate for this system.I'm planning on adding Microsoft teams next, but I'd rather know what current users prefer.

## 导航

- 项目页：[[10-项目/eventsend.io_899d3512]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
