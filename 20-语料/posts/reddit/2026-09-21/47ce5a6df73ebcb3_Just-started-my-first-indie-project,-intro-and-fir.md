---
type: "corpus"
item_id: "47ce5a6df73ebcb3"
title: "Just started my first indie project, intro and first quest are working!"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/IndieDev/comments/1szyvze/just_started_my_first_indie_project_intro_and/"
project_url: "https://i.redd.it/cnsxafb3gcyg1"
author: "RohynOak"
published_at: "2026-04-30T23:11:48+08:00"
captured_at: "2026-09-21T01:14:47+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - reddit
  - r/indiedev
  - GIF
metrics: {"score": 6, "comments": 11, "upvote_ratio": 0.6899999976158142}
comments_count: 0
comments_total: 0
discovered_via: "reddit:174d+settle3"
---

# Just started my first indie project, intro and first quest are working!

> [!info] 一句话导读
> Solo devlog: I got the first tiny intro-to-quest loop working in my indie MMORPG prototype.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/IndieDev/comments/1szyvze/just_started_my_first_indie_project_intro_and/>
> 指标：得分=6 · 评论=11 · 赞踩比=0.6899999976158142
> 作者：RohynOak　|　发布：2026-04-30T23:11:48+08:00
> 项目链接：<https://i.redd.it/cnsxafb3gcyg1>
> 采集：2026-09-21T01:14:47+08:00　|　id：`47ce5a6df73ebcb3`

## 正文

Solo devlog: I got the first tiny intro-to-quest loop working in my indie MMORPG prototype.

I’m building **Ruins of Crestil**, an early solo-developed fantasy MMORPG prototype about rebuilding civilization around the Dragon Keep after a long decline. It is still very small in scope, and I’m deliberately focusing on one playable vertical slice before expanding outward.

Today’s milestone was getting the opening flow working end-to-end:

* main menu into placeholder character select
* server-driven character spawn after selection
* save/load for character scene, position, rotation, inventory, equipment, and quest state
* intro room interactions: bed, wardrobe, key, door, and Aidan conversation
* first tutorial quest from Aidan: “find Tucker in the training yard”
* transition from the private-feeling intro space into the first shared scene
* quest completion by talking to Tucker
* TAB menu with inventory and journal panels

A lot of the work behind this was backend rather than visual: account vs character persistence, quest persistence, stable interactable IDs for shared scene objects, server-authoritative interaction handling, and a basic journal snapshot from server to client.

The current visuals are still very placeholder, but this is the first time the project has felt like an actual playable slice instead of disconnected systems. Next I’m polishing the intro room visually and then I’ll be working toward private intro instances, tutorial prompts, and eventually the first skill/progression systems.

For people who like following early indie development: what kinds of posts are most interesting at this stage? Short gameplay clips, technical breakdowns, design notes, before/after art passes, or something else?

## 导航

- 项目页：[[10-项目/i.redd.it_c4f6e6b3]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
