---
type: "corpus"
item_id: "df45ea930cfe7ba8"
title: "Show HN: Dinemic – self-hosted ingress across multiple providers (DNS, LB, TLS)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50260093"
project_url: "https://dinemic.com/"
author: "didijo"
published_at: "2026-10-27T14:38:33Z"
captured_at: "2026-10-27T23:46:32+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-27"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_didijo
  - story_50260093
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Dinemic – self-hosted ingress across multiple providers (DNS, LB, TLS)

> [!info] 一句话导读
> I recently published a project for running self hosted, highly available ingress for your infrastructure: authoritative DNS for your own domain, load balancers …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50260093>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：didijo　|　发布：2026-10-27T14:38:33Z
> 项目链接：<https://dinemic.com/>
> 采集：2026-10-27T23:46:32+08:00　|　id：`df45ea930cfe7ba8`

## 正文

Hey HN,
I recently published a project for running self hosted, highly available ingress for your infrastructure: authoritative DNS for your own domain, load balancers and network mesh, to expose your web apps. It started over a year ago as side project to handle several websites for clients and other side projects, and finished as the replacement cert-manager, external-dns and ingress that works without k8s, and is independent from single cloud/vps provider.It ended up as the HA platform, able to manage dozens of load balancers with TLS termination (and Let's Encrypt integration), DNS servers and full redundant mesh. The design goal from the beginning was to prepare a tool with minimized risk of single point of failure and independent from single hosting.It is running all my home lab, nextcloud, gitlab and production websites for clients for the few last months.Quick links for those who want to test:
https://dinemic.com - project page
https://console.dinemic.com - hosted control plane, if you want to test it with your own vps and domain, without setting up whole stack
https://gitlab.cloudover.io/dinemic/docs - project documentationIn high availability section of documentation you will also find concepts and design of its components and sample analysis of downtime when things go wrong with your infra.It is AGPL, so you can host also at your own. Self hosted version covers all functionality, with API and command line tools.

## 关联链接

- https://console.dinemic.com
- https://dinemic.com
- https://gitlab.cloudover.io/dinemic/docs

## 导航

- 项目页：[[10-项目/dinemic.com_583f146f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
