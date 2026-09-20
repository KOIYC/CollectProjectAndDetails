---
type: "corpus"
item_id: "8ba116380fd955b4"
title: "Show HN: 49Agents – 2D Canvas IDE for Orchestrating Agents, Repos, Issues"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47942287"
project_url: "https://github.com/49Agents/49Agents"
author: "alpadurza"
published_at: "2026-04-28T23:34:10Z"
captured_at: "2026-09-21T01:42:32+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-28"
tags:
  - 语料
  - hn_show
  - author_alpadurza
  - story_47942287
  - show_hn
metrics: {"points": 21, "comments": 2, "engagement_velocity": 21}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:174d"
---

# Show HN: 49Agents – 2D Canvas IDE for Orchestrating Agents, Repos, Issues

> [!info] 一句话导读
> Beads tables (Steve Yegge's) for issue tracking. Can view git trees, terminals, issue tables, notes, and files all on one screen. Can connect multiple machines …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47942287>
> 指标：点赞=21 · 评论=2 · engagement_velocity=21
> 作者：alpadurza　|　发布：2026-04-28T23:34:10Z
> 项目链接：<https://github.com/49Agents/49Agents>
> 采集：2026-09-21T01:42:32+08:00　|　id：`8ba116380fd955b4`

## 正文

Beads tables (Steve Yegge's) for issue tracking. Can view git trees, terminals, issue tables, notes, and files all on one screen. Can connect multiple machines via private network (like tailscale)

## 评论（2/2）

> **2001zhaozhao** · 2026-04-29T07:00:11.000Z　
> I'm building an agent wrapper with an in-browser windowing user interface, and this is surprisingly close to what I have in mind from a UX perspective.Similarities:- Lots of UX focus with the details like keyboard shortcuts. Other gui projects straight-up forget this, and the CLI agents include it only out of necessity. I think this is the way to go because no matter how much can be automated in today's world, having the lowest-friction UX is still king in making the parts that need to be manual go as fast as possible.- The idea of a windowing system in the browser. I think we both think that agentic development is complex enough to warrant a multi-window environment being optimal.- Focus on being accessible from any device, although i don't have the persistent layout thing quite as developed as your approach.- Our monetization approach is similar (monetize hosted version). you're monetizing through hosting the remote while i want to monetize through hosting 24/7 dev machinesDifferences:- My windowing approach is a bit more safe (just focused on making a really good remote desktop) while you seem to have a more adventurous idea with the 2D zoomable canvas- I think your choice of Beads issue tracking is really interesting for context management. I don't have an equivalent in my project.- You're running agents on a dev's laptop and enabling remote access through a relay layer, whereas i'm designing my tool's backend to run directly on 24/7 dev servers.- You're using cli agents directly (like cmux) while i'm wrapping them in a GUI with ACP (like Zed)- You have monaco editor built in while I'm planning to integrate code-server- From your canvas approach i'm assuming you're rendering client side. I'm focused on server-rendered web HTML (liveview-like), mostly chosen for reasons for supporting a plugin system where plugins are server-side-only but can alter the UI. my approach probably sends more data through the wire but drains less battery than yoursOverall a bit of nice validation and food for thought. I think we have really different backend approaches but the UX portion converges nonetheless. Thanks for sharing!By the way, in the GitHub repo description, your 49agents website still says coming soon, you should probably update that.Also, the Discord invite on your website doesn't work

---

> **alpadurza** · 2026-04-29T11:53:02.000Z　
> hey zhaozhao, thanks for sharing! i will check the website... dont have much time to work on landing page lately haha

## 导航

- 项目页：[[10-项目/github.com_e21b72e6]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
