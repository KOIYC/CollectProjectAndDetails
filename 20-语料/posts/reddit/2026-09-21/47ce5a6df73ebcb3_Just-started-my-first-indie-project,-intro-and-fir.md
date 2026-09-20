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
captured_at: "2026-09-21T03:00:12+08:00"
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
comments_count: 11
comments_total: 11
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
> 采集：2026-09-21T03:00:12+08:00　|　id：`47ce5a6df73ebcb3`

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

## 评论（11/11）

> **balmabalmadev**（1 分） · 2026-04-30T23:14:39+08:00　
> The gif isnt playing for me

---

> **RohynOak**（1 分） · 2026-04-30T23:17:14+08:00　
> I noticed it wasn't at first, too. It seems to be working now - may have needed approval or been rendering or something. Try it now!

---

> **hypatiaC**（5 分） · 2026-05-01T00:05:09+08:00　
> > Solo Dev
>
> > MMORPG
>
> Uh oh

---

> **RohynOak**（3 分） · 2026-05-01T00:07:54+08:00　
> I know, I know. I'm honestly not planning/hoping to get to completion. It's a hobby passion project.

---

> **Effective_Hope_3071**（2 分） · 2026-05-01T03:35:25+08:00　
> I commens you for doing pure block out. I was so much time adding placeholder assets just because I want it to look pretty while developing.

---

> **RohynOak**（1 分） · 2026-05-01T03:37:44+08:00　
> That'll be my next step - I'm much much more a coder than an art person, so the real fun for me is in getting systems hooked up and working. The art is work.

---

> **OnlyLuck77**（1 分） · 2026-05-01T06:09:27+08:00　
> Just a tip, if you haven’t already, start soon as possible building around client/server architecture, with the server as authoritative. Decoupling the code and moving it to the server later is a nightmare!
>
> I know people say MMO is a bad idea, but as a hobby passion project if nothing not you will learn tons.

---

> **RohynOak**（2 分） · 2026-05-01T06:30:58+08:00　
> Thanks for the tip! I've already had that notion in mind and everything I've built so far is server authoritative except camera rotation.

---

> **qwnick**（1 分） · 2026-05-01T18:41:06+08:00　
> bait post

---

> **RohynOak**（2 分） · 2026-05-01T20:19:15+08:00　
> You say that like it's a dismissive bad thing, but building an engaged community is a necessary part of game development, and where else would it happen but in existing communities of people interested in the topic...?

---

> **qwnick**（1 分） · 2026-05-01T21:02:03+08:00　
> You framed my response wrong. It's a bad thing not because you want engagement, everybody do. It's bait, cause it's so bad and primitive, that you expect to bait people into reaction, kinda like rage baits works.

## 导航

- 项目页：[[10-项目/i.redd.it_c4f6e6b3]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
