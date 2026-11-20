---
type: "corpus"
item_id: "24f13a36c3df46b6"
title: "Show HN: Purple Flow – AI-first n8n alternative, 10k+ workflows on 512MB"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50560170"
project_url: "https://github.com/leetheguy/purple_flow"
author: "leetheguy"
published_at: "2026-11-19T13:57:14Z"
captured_at: "2026-11-20T09:45:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-20"
pub_day: "2026-11-19"
tags:
  - 语料
  - hn_show
  - author_leetheguy
  - story_50560170
  - show_hn
metrics: {"points": 5, "comments": 2, "engagement_velocity": 5}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Purple Flow – AI-first n8n alternative, 10k+ workflows on 512MB

> [!info] 一句话导读
> I ran into a wall with n8n - hard and expensive to scale, limited streaming, heavy MCP is confusing for agents.That scaling was becoming more and more critical …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50560170>
> 指标：点赞=5 · 评论=2 · engagement_velocity=5
> 作者：leetheguy　|　发布：2026-11-19T13:57:14Z
> 项目链接：<https://github.com/leetheguy/purple_flow>
> 采集：2026-11-20T09:45:52+08:00　|　id：`24f13a36c3df46b6`

## 正文

Hey all!
I ran into a wall with n8n - hard and expensive to scale, limited streaming, heavy MCP is confusing for agents.That scaling was becoming more and more critical as I was beginning to build agentic swarms.
So I built my own alternative with Elixir and Beam. Been using it in production for almost 2 months.It connects my agent to multiple databases, sandboxes, and APIs.
I've even migrated over my most used n8n workflows without a hiccup.I ran some benchmarks and 10,000 concurrent workflows executed in 3 seconds and cost about 330MB of ram (listed as 512 in the case study). Equivalent workflows in n8n took 2GB of ram to run 100. It's roughly 200x the memory efficiency of the usual Node/Python stacks. And while you don't edit the workflows yourself visually, you can see and manage them through a UI, along with credentials that the agent never sees.The workflows themselves are pure TOML. Not as easy as dragging node connectors. But the idea is that AI creates the flows and you can easily understand them.This isn't a shaky demo. I'm using it as my daily driver to create complex multi-agent personas, run research and info gathering swarms, and whatever else my agent needs to get its job done. (it's built more than 70 so far)I have a live working demo on my website that was built by an agent using Purple Flow to connect to my server. The demo itself lets an agent using Purple Flow access live (Adventure Works) data and generate reports, documents, and slides on demand. My agent and I built it in an afternoon. It runs on a lightweight model (to save money for a public demo) with very few hiccups.- Repo: https://github.com/leetheguy/purple_flow
- Discord, benchmarks, and demo links in the repo.

## 评论（2/2）

> **sambejk** · 2026-11-19T14:03:57.000Z　
> Isn't n8n already AI-first Zapier? So this is AI-first AI-first Zapier? I wonder if these tools still have a purpose if I can just ask Claude to do it. Don't know what your experience is with this? Probably also more efficient to just make everything in a script rather than these GUI workflows. End rant

---

> **leetheguy** · 2026-11-19T16:28:42.000Z　
> Totally fair. In order for an AI to use N8N, it has to use an elaborate MCP connection and sift through a ton of heavy JSON to manage a system that was designed to be built visually by humans. So basically, N8N was designed to be a visual tool for humans to create workflows quickly and easily. AI access to that tool was added much later.Purple Flow was designed to allow AIs to create workflows with simple, lightweight TOML files and a minimal connector that lets them manage those files. AI doesn't have to do any gymnastics and wrap its head around layers of human-first complexity to do its job.And yes, you could use scripts to build just about anything. These tools are designed to be universal connectors to make it easy to transfer data from point A to point B without all the boilerplate. These tools can replace a lot of scripts and keep you from having to set up servers and connectors and web calls and cron jobs and keep everything organized and tidy. With Purple Flow, it's all tucked away. The credentials are kept out of your agent's hands and the scripts are easy enough for even cheap, lightweight models to build and manage.

## 导航

- 项目页：[[10-项目/github.com_5bf0c709]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
