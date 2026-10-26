---
type: "corpus"
item_id: "5bbddfc65abcbf92"
title: "Update #2 on xNode360: click a node, see everything it touches"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/microsaas/comments/1x6sgaj/update_2_on_xnode360_click_a_node_see_everything/"
author: "Jealous-Wedding6867"
published_at: "2026-10-16T01:48:13+08:00"
captured_at: "2026-10-26T09:43:47+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-26"
pub_day: "2026-10-16"
tags:
  - 语料
  - reddit
  - r/microsaas
metrics: {"score": 5, "comments": 7, "upvote_ratio": 1}
comments_count: 7
comments_total: 7
discovered_via: "reddit:14d+settle10"
---

# Update #2 on xNode360: click a node, see everything it touches

> [!info] 一句话导读
> Quick recap for anyone new: xNode360 is a live map of your infrastructure. Every VPS, domain, database or SaaS account is a node, you draw the links between the…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/microsaas/comments/1x6sgaj/update_2_on_xnode360_click_a_node_see_everything/>
> 指标：得分=5 · 评论=7 · 赞踩比=1
> 作者：Jealous-Wedding6867　|　发布：2026-10-16T01:48:13+08:00
> 项目链接：—
> 采集：2026-10-26T09:43:47+08:00　|　id：`5bbddfc65abcbf92`

## 正文

Quick recap for anyone new: xNode360 is a live map of your infrastructure. Every VPS, domain, database or SaaS account is a node, you draw the links between them, and each node runs a real check (port, HTTP, TLS cert, DNS, Postgres query). It tracks when certs and secrets expire without storing the values. Private servers are checked by a small outbound-only agent. You can build the map by hand, from a YAML manifest, or let an LLM build it from your repo through the MCP server. There's also a VS Code extension with the live map in a side panel. Previous posts: - Why I built it: [https://www.reddit.com/r/microsaas/comments/1wqdumk/my\_setup\_had\_gotten\_so\_complicated\_that\_i\_could/](https://www.reddit.com/r/microsaas/comments/1wqdumk/my_setup_had_gotten_so_complicated_that_i_could/) \- VS Code extension + MCP server

\*\*What's new: highlighting connections\*\*

Once a map grows past a dozen nodes, the lines start to blur together and it's hard to tell what actually connects to what. So: - \*\*Select an edge\*\* → the two nodes it connects light up. No more following a line across the canvas to see where it ends. - \*\*Select a node\*\* → every node directly connected to it is highlighted and the rest of the map fades out. It sounds small, but it's the feature I use most now. When something goes red, I click it and immediately see what depends on it and what it depends on. It also helps a lot when showing the map to someone else: instead of explaining the whole picture, you click one piece and walk through its neighbours. Demo, no signup (read-only). Still early: no alerting yet, pricing is undecided. Next thing I'm thinking about is following connections more than one hop away (the full chain of what breaks if X goes down). Would that be useful to you, or is the direct neighbourhood enough?

https://reddit.com/link/1x6sgaj/video/qnlegnz65ovh1/player

## 评论（7/7）

> **Tellenze**（1 分） · 2026-10-16T02:16:23+08:00　
> Full chain for an outage, direct neighbours for a quick look. Keeping the path visible would matter to me: app → service → database, so I can follow why a distant node is highlighted.

---

> **loveolya**（2 分） · 2026-10-16T02:33:48+08:00　
> No alerting yet means its a map you have to be staring at when something goes red, and nobody is at 3am. Thats the gap before any new view matters
> Multi hop is the useful version of this feature though, direct neighbors rarely explain an outage
> Ship alerts that say X is down and these four things depend on it, then you have a product

---

> **Thivierge_Arabu**（1 分） · 2026-10-16T03:19:49+08:00　
> multi-hop would be useful but id keep it opt-in, like a toggle. most of the time direct connections are what you need and showing the full chain by default would probably just recreate the clutter problem you're solving

---

> **Fit-Corner2382**（2 分） · 2026-10-16T04:21:34+08:00　
> Seeing the full touch set on click is the feature, depth control is what makes it usable.
>
> I keep hitting graphs where one hop is clean and two hops explode, so a hop limit plus edge-type filter matters more than showing every connected node at once.

---

> **Khavel_dev**（1 分） · 2026-10-16T16:31:56+08:00　
> Multi-hop tracing would be way more useful than direct neighbors, at least for incident response. When a database goes red, I don't just care about what's directly connected. I need the cascade: which services hit that DB, which frontends talk to those services, and whether any of them have fallbacks.
>
> The highlight-on-click feature alone looks super handy for explaining architecture to someone who isn't staring at the map every day. Saves a lot of whiteboard sessions.

---

> **Jealous-Wedding6867**（1 分） · 2026-10-16T16:48:10+08:00　
> 🙏🏻 thanks

---

> **geoffreybyers**（1 分） · 2026-10-18T04:16:34+08:00　
> A map that shows connections without alerting you when one breaks is a picture, not a product. You're building a visual aid for when you're already staring at it. The operational value comes when the tool tells you to stare at it.

## 关联链接

- https://reddit.com/link/1x6sgaj/video/qnlegnz65ovh1/player
- https://www.reddit.com/r/microsaas/comments/1wqdumk/my
- https://www.reddit.com/r/microsaas/comments/1wqdumk/my_setup_had_gotten_so_complicated_that_i_could/

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
