---
type: "corpus"
item_id: "870a9cee0fffc076"
title: "Show HN: Bailout – The coding agent meant to be deleted"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49778390"
project_url: "https://github.com/storozhenko98/bailout"
author: "mst98"
published_at: "2026-09-20T18:14:58Z"
captured_at: "2026-09-21T09:44:03+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-09-20"
tags:
  - 语料
  - hn_show
  - author_mst98
  - story_49778390
  - show_hn
metrics: {"points": 2, "comments": 3, "engagement_velocity": 2}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:3d"
---

# Show HN: Bailout – The coding agent meant to be deleted

> [!info] 一句话导读
> hey hn,i made bailout for a pretty specific problem. you boot a fresh vm and want an agent to help get it set up, except you dont have your agent set up yet. no…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49778390>
> 指标：点赞=2 · 评论=3 · engagement_velocity=2
> 作者：mst98　|　发布：2026-09-20T18:14:58Z
> 项目链接：<https://github.com/storozhenko98/bailout>
> 采集：2026-09-21T09:44:03+08:00　|　id：`870a9cee0fffc076`

## 正文

hey hn,i made bailout for a pretty specific problem. you boot a fresh vm and want an agent to help get it set up, except you dont have your agent set up yet. no gh, no config, no api key handy. might not even have codex / claude code / opencode curled and loaded. or you already have a setup but opencode / pi / whatever stopped launching, and the thing you'd normally ask to fix it is the thing that's broken.for me, and this is embarrassing, but at work we switched from per-dev keys to oai / ant to just an internal litellm router, which required configuring opencode. i use opencode2 which can dynamically reload its config. well, while rewriting the config to work with self hosted litellm, it broke, and i was stranded w/ no coding agent. bailout is for that sort of thing, like break glass, agent pls fix.think of bailout like a spare agent for these sorts of things. install it, ask it to set up the machine or fix your usual tools, then remove it. the idea is “the harness meant to be deleted.” i like having a tool whose last useful action can be uninstalling itself. plus a play on hinge, the whole app meant to be deleted.you install it with `curl -fsSL https://bailout.dev/install.sh | bash` and run `bailout`. no account or api key needed for bailout. the tools it helps you set up still need your own accounts, obviously. it can hand you the terminal for those logins without sending what you type to the model.the client is a rust binary, about 639 KB uncompressed on apple silicon. it also runs on linux x64 and arm64. bash is the only tool. it can inspect files, edit configs, install things, curl stuff, etc. commands run automatically with your user's permissions, so it has the same access you do in that shell. i got inspired by vercel's fx.sh in terms of minimalism and size and all that.the hosted router uses free models and switches between available ones when a request fails. there are shared limits, and it will tell you when it has to wait. this is still a small free service, so i dont want to pretend it has unlimited capacity. odds are, if this post gets enough attention and enough of you try it, it will exhaust capacity. to that end if anyone knows anyone willing to toss a free model in for this consistently, would be very cool.there's a recording of it fixing an intentionally broken opencode config on the gh page. bailout gets removed at the end and opencode runs again. waits are shortened in the video; the original terminal capture is there too. mit licensed, and built with a lot of help from codex. curious whether this is useful for the way you set up machines, or if there's some obvious case i'm missing. issues / prs welcome.

## 评论（3/3）

> **GMShuaib** · 2026-09-20T20:11:07.000Z　
> hm but what's the use case exactly? and, is it free or do I have to put API keys in it? and what models are supported?

---

> **mst98** · 2026-09-20T20:41:48.000Z　
> it’s completely free. the use case is if you have a fresh vm and want to skip having to type a bunch of apt install commands / setting up gh and so on. or if you have say opencode or pi but you broke your config. now you have a model that can help bail you out and repair stuff. no api key, it just uses a shared pool of free llms via open router. it’s basically a free minimalist coding harness with free llms to help “bailout” a bad config or a fresh vm into something more useable.

---

> **mst98** · 2026-09-20T20:47:37.000Z　
> tldr free, no api key needed, just curl bash and then have it help you set up your vm or fix a harness etc. think of this as a primitive harness that helps you bootstrap stuff. the long term hope is that most future unix like systems ship with something like an “llm” command. you have vi or nano on most systems, out of the box. curl and so on. so one day “llm” where you boot up and you have a basic, free, minimalist terminal harness that can bootstrap your system for you. it doesn’t need to be an erudite complex llm, but just a basic one that can do the basics. that’s the vision i have.

## 关联链接

- https://bailout.dev/install.sh

## 导航

- 项目页：[[10-项目/github.com_7bea9d76]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
