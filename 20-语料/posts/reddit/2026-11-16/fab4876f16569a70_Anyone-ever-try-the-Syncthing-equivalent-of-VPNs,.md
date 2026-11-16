---
type: "corpus"
item_id: "fab4876f16569a70"
title: "Anyone ever try the Syncthing equivalent of VPNs, Anywherelan?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1xozg3r/anyone_ever_try_the_syncthing_equivalent_of_vpns/"
project_url: "https://github.com/anywherelan/awl"
author: "megamattx0"
published_at: "2026-11-06T08:49:57+08:00"
captured_at: "2026-11-16T10:02:00+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-11-16"
pub_day: "2026-11-06"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - VPN
metrics: {"score": 21, "comments": 12, "upvote_ratio": 0.8}
comments_count: 12
comments_total: 12
discovered_via: "reddit:14d+settle10"
---

# Anyone ever try the Syncthing equivalent of VPNs, Anywherelan?

> [!info] 一句话导读
> I recently found this project called Anywherelan on Fdroid and have not been able to find additional information outside of github.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1xozg3r/anyone_ever_try_the_syncthing_equivalent_of_vpns/>
> 指标：得分=21 · 评论=12 · 赞踩比=0.8
> 作者：megamattx0　|　发布：2026-11-06T08:49:57+08:00
> 项目链接：<https://github.com/anywherelan/awl>
> 采集：2026-11-16T10:02:00+08:00　|　id：`fab4876f16569a70`

## 正文

I recently found this project called Anywherelan on Fdroid and have not been able to find additional information outside of github.

It's a mesh VPN with no coordination server. Peers find each other through a DHT and connect either directly or through relays just like in Syncthing.

I might give it a shot. Anyone here actually used it?

[https://github.com/anywherelan/awl](https://github.com/anywherelan/awl)

## 评论（12/12）

> **asimovs-auditor**（1 分） · 2026-11-06T08:50:16+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **megamattx0**（0 分） · 2026-11-06T08:55:36+08:00　
> Just to organize my thoughts and get straight to the point.

---

> **Weak-Maintenance7659**（2 分） · 2026-11-06T09:46:51+08:00　
> Looks interesting.

---

> **MVanderloo**（7 分） · 2026-11-06T10:59:19+08:00　
> looks like a cool project, although I use rayfish for this purpose

---

> **AliyasDandani_64**（3 分） · 2026-11-06T22:52:14+08:00　
> how does it handle IP allocation and DNS without a central coordinator? seems like avoiding subnet collisions across peers would get messy pretty quick once you have more than a couple devices

---

> **MongooseWonderful198**（2 分） · 2026-11-07T12:23:31+08:00　
> For IPv4, each node keeps its own peer-to-IP map. The receive path rewrites packet addresses into that node's local mapping, so two machines can assign the same peer different local addresses.
>
> The built-in DNS server resolves `.awl` names from the local list of known peers. The code checks for duplicate peer IPs, but overlap with an existing LAN is a separate issue: the default subnet is `10.66.0.0/16`, and automatic subnet selection is still marked TODO. This is from reading the [current source](https://github.com/anywherelan/awl/blob/5fe13bc8dac2240c45f1f874b751d17738888f0f/config/network_addr.go); I haven't run it.

---

> **willjasen**（2 分） · 2026-11-08T06:10:02+08:00　
> i may now have a great new use-case for something i’m working on that fits this perfectly :) \[save the proper security audit\]

---

> **iLaux**（1 分） · 2026-11-09T19:38:14+08:00　
> Tailscale? Headscale?

---

> **ugisman**（2 分） · 2026-11-09T22:29:27+08:00　
> Yep, I'm using it. Works great. It's basically Tailscale but without depending from anyone

---

> **megamattx0**（2 分） · 2026-11-10T01:33:08+08:00　
> Dang, Rayfish looks pretty good too

---

> **MVanderloo**（2 分） · 2026-11-10T01:35:02+08:00　
> yeah and the fact that it’s built on Iroh gives me a lot more confidence. You should listen to the Iroh 1.0 release announcement

---

> **megamattx0**（1 分） · 2026-11-10T01:38:36+08:00　
> I already use Tailsacle, but a VPN without a coordination server (Headscale) would be nice

## 导航

- 项目页：[[10-项目/github.com_013bbd32]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
