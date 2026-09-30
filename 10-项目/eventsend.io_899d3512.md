---
type: "project"
title: "Show HN: EventSend – Event tracking and routing for solo founders and SaaS teams"
project_url: "https://eventsend.io/"
first_seen: "2026-09-30T18:28:30+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_mytinyrocket
  - story_49902837
  - show_hn
lang: "en"
---

# Show HN: EventSend – Event tracking and routing for solo founders and SaaS teams

> [!info] 一句话导读
> I was tired of learning about failed payments by my customers and not from my system, so I built an event tracker that allowed me to have a searchable feed of t…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://eventsend.io/>
> 首次收录：2026-09-30T18:28:30+08:00
> 来源渠道：HN Show HN
> 标签：author_mytinyrocket, story_49902837, show_hn
> 最新指标：点赞=3 · 评论=2 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-30T18:28:30+08:00 | HN Show HN | 点赞=3 · 评论=2 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-30/9ce6e37dfaa0cc8b_Show-HN-EventSend-–-Event-tracking-and-routing-for]] |

## 摘要正文

I was tired of learning about failed payments by my customers and not from my system, so I built an event tracker that allowed me to have a searchable feed of the important events happening for my apps and route the ones I cared about to my phone so I could take action quickly.EventSend is an event tracker and a router, your system sends the important events you want to track: signups, failed payments, new subscriptions, deployments, a new purchase, etc. so they end up in a searchable and filterable feed that you can use to have quick insight about what's happening with your product.Then there's also the routing side of things, those important events you want to know the moment they happen, and not once you go into your Grafana Loki logs, can be routed to your phone, Slack, Discord, Telegram or any other system or service via a signed webhook. You can configure rules, alerts, quiet hours or smart rollups to have the signal you're looking for.All event's are retried with a reasonable backoff, circuit breakers and limiters maintain the prviders and system reliable. If we got a 401 or 403, your destination will be inactivated instead of retried and you'll be notified for you to update…
