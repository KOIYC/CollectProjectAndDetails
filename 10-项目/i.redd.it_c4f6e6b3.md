---
type: "project"
title: "Just started my first indie project, intro and first quest are working!"
project_url: "https://i.redd.it/cnsxafb3gcyg1"
first_seen: "2026-09-21T01:14:47+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/indiedev
  - GIF
lang: "en"
---

# Just started my first indie project, intro and first quest are working!

> [!info] 一句话导读
> Solo devlog: I got the first tiny intro-to-quest loop working in my indie MMORPG prototype.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://i.redd.it/cnsxafb3gcyg1>
> 首次收录：2026-09-21T01:14:47+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/indiedev, GIF
> 最新指标：得分=6 · 评论=11 · 赞踩比=0.6899999976158142

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:10:11+08:00 | Reddit 独立开发版块 | 得分=6 · 评论=11 · 赞踩比=0.6899999976158142 | [[20-语料/posts/reddit/2026-09-21/47ce5a6df73ebcb3_Just-started-my-first-indie-project,-intro-and-fir]] |
| 2026-09-21T01:14:47+08:00 | Reddit 独立开发版块 | 得分=6 · 评论=11 · 赞踩比=0.6899999976158142 | [[20-语料/posts/reddit/2026-09-21/47ce5a6df73ebcb3_Just-started-my-first-indie-project,-intro-and-fir]] |

## 摘要正文

Solo devlog: I got the first tiny intro-to-quest loop working in my indie MMORPG prototype.  I’m building **Ruins of Crestil**, an early solo-developed fantasy MMORPG prototype about rebuilding civilization around the Dragon Keep after a long decline. It is still very small in scope, and I’m deliberately focusing on one playable vertical slice before expanding outward.  Today’s milestone was getting the opening flow working end-to-end:  * main menu into placeholder character select * server-driven character spawn after selection * save/load for character scene, position, rotation, inventory, equipment, and quest state * intro room interactions: bed, wardrobe, key, door, and Aidan conversation * first tutorial quest from Aidan: “find Tucker in the training yard” * transition from the private-feeling intro space into the first shared scene * quest completion by talking to Tucker * TAB menu with inventory and journal panels  A lot of the work behind this was backend rather than visual: account vs character persistence, quest persistence, stable interactable IDs for shared scene objects, server-authoritative interaction handling, and a basic journal snapshot from server to client.  The…
