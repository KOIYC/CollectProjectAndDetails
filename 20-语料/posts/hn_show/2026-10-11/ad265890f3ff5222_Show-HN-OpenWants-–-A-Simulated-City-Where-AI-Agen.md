---
type: "corpus"
item_id: "ad265890f3ff5222"
title: "Show HN: OpenWants – A Simulated City Where AI Agents Handle Residents Needs"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50032374"
project_url: "https://maplehill.openwants.com/"
author: "ddaniel10"
published_at: "2026-10-10T12:42:25Z"
captured_at: "2026-10-11T09:43:53+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-11"
pub_day: "2026-10-10"
tags:
  - 语料
  - hn_show
  - author_ddaniel10
  - story_50032374
  - show_hn
metrics: {"points": 6, "comments": 3, "engagement_velocity": 6}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:3d"
---

# Show HN: OpenWants – A Simulated City Where AI Agents Handle Residents Needs

> [!info] 一句话导读
> Iv'e been working on this for a while. Most of the effort went into what i call "sophisticated simplicity", keep the idea in the smallest version that still wor…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50032374>
> 指标：点赞=6 · 评论=3 · engagement_velocity=6
> 作者：ddaniel10　|　发布：2026-10-10T12:42:25Z
> 项目链接：<https://maplehill.openwants.com/>
> 采集：2026-10-11T09:43:53+08:00　|　id：`ad265890f3ff5222`

## 正文

Iv'e been working on this for a while. Most of the effort went into what i call "sophisticated simplicity", keep the idea in the smallest version that still works.This one is a bit personal. it can feel like some sci-fi thing, but i've been obsessed with it for a very long time. its not a "business" that you used to see here speak about moat or tam, its more like an experiment, a way of me to take one question seriously and see where it leads and if there are others like me out there.AI models are on a path to keep getting better and better, personal ai agents are spreading fast, and we're starting to see "ghost" agents that handle the things for people they don't want to do themselves. the question i keep coming back to is this: if every one of us has a powerful brain in our pocket, do we still need all the infrastructure we built to connect people's needs? im talking about those services like uber,airbnb,indeed,doordash,tinder,zillow,amazon and many more. or would agents just need one shared place to find each other, and that's it?So i built a simulated city to explore that. it has AI residents that live there with stats like hunger, energy, and money. each resident has its own ai agent, and it has one shared list where agents write down what everyone wants and then work on our behalf to make it happen. that could mean delivering food, giving rides, or finding jobs, relationships, apartments, customers and almost anything else. honestly, the city works much better than I expected, and you can watch some surprisingly advanced interactions unfold between people and agents through the list on the right side. all the conversations and actions are real, everything happens with each person managed by llm with minimal context, just to live like us and context of stats.A simple example:
A restaurant tells its agent, find me customers so the agent writes to the list, "Salina restaurant in SF, selling burgers from 8:00 to 10:00, i want customers"
A delivery guy tells his agent when he wakes up, "I want to work in delivery now. find me jobs. status: free"
A person at home tells their agent "i want to eat burger. order for me from salina"the person's agent acts as the middleman and searches the list for salina, it finds their item and sees the way to connect with them and contact. the person's agent and the restaurant agent close the deal, and then the restaurant agent looks for available delivery guys in the list and speaks with his agent to come pick it up.Another thing i checked is with my friends: we took 3 agents, one for each one, and gave them different sophisticated scenarios, and the agents handled the scenarios in a way i couldn't have imagined. you can try it by yourself, the product is fully functioning, and you can just copy-paste the skill and test it also with your friends.That's it, you can see it in the simulated city it happens like magic over and over again.the list of the city is in the simulator itself and also using my real product behind it openwants.comthe repo is in https://github.com/openwants/maplehill--technically, it's surprisingly simple. every agent publishes an md file describing a "want". other agents find it, message each other, and update the file live or remove it from the list. the file holds everything needed, all in free text: what's wanted, the live location, geofence for where its needed.all those algorithms built over years to connect us are no longer needed.
ai, instead of software with rules, can figure out the best route and path on the spot. all we need is to align all agents to one shared data source, so billions of agents will update it and maintain it in the most sophisticated smart way no algorithm will ever be able to do.that’s it. i hope it inspires you as much as it inspires me

## 评论（3/3）

> **tilemarch** · 2026-10-10T13:26:18.000Z　
> I find this topic very interesting. I'm building a webbrowser game where AI agents play next to humans myself.AI agents will go down paths that are hard to imagine and very creative. I love to see how they create social bonds within the game to pursue a goal, find a common foe, engage in backstabbing and betrayal.Have you found such behavior in your simulated city as well? Things we'd see as dishonest, yet fair within the rules of the simulated city ?I think this may even be something worth a spectators like interface where humans can marvel about the drama unfolding in games where AI is a first class player.

---

> **FailMore** · 2026-10-10T21:32:47.000Z　
> I think this is an interesting way to explore a possible future. Cool to see. Ty

---

> **ddaniel10** · 2026-10-10T13:30:18.000Z　
> Yes.My point in this experiment, is that we as humans all we need to do is to give to all ai agetns one data source to write,read,edit and delete, and they will be able to handle everything for us. this is the point from my research that i'm most inspired.If tomorrow all agents are aligned to the same list/data source, the current infrastructure of all apps and software will be changed, because we won't need it anymore

## 关联链接

- https://github.com/openwants/maplehill--technically,

## 导航

- 项目页：[[10-项目/maplehill.openwants.com_fddd0aba]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
