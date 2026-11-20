---
type: "project"
title: "Show HN: Purple Flow – AI-first n8n alternative, 10k+ workflows on 512MB"
project_url: "https://github.com/leetheguy/purple_flow"
first_seen: "2026-11-20T09:45:52+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_leetheguy
  - story_50560170
  - show_hn
lang: "en"
---

# Show HN: Purple Flow – AI-first n8n alternative, 10k+ workflows on 512MB

> [!info] 一句话导读
> I ran into a wall with n8n - hard and expensive to scale, limited streaming, heavy MCP is confusing for agents.That scaling was becoming more and more critical …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/leetheguy/purple_flow>
> 首次收录：2026-11-20T09:45:52+08:00
> 来源渠道：HN Show HN
> 标签：author_leetheguy, story_50560170, show_hn
> 最新指标：点赞=5 · 评论=2 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-20T09:45:52+08:00 | HN Show HN | 点赞=5 · 评论=2 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-11-20/24f13a36c3df46b6_Show-HN-Purple-Flow-–-AI-first-n8n-alternative,-10]] |

## 摘要正文

Hey all! I ran into a wall with n8n - hard and expensive to scale, limited streaming, heavy MCP is confusing for agents.That scaling was becoming more and more critical as I was beginning to build agentic swarms. So I built my own alternative with Elixir and Beam. Been using it in production for almost 2 months.It connects my agent to multiple databases, sandboxes, and APIs. I've even migrated over my most used n8n workflows without a hiccup.I ran some benchmarks and 10,000 concurrent workflows executed in 3 seconds and cost about 330MB of ram (listed as 512 in the case study). Equivalent workflows in n8n took 2GB of ram to run 100. It's roughly 200x the memory efficiency of the usual Node/Python stacks. And while you don't edit the workflows yourself visually, you can see and manage them through a UI, along with credentials that the agent never sees.The workflows themselves are pure TOML. Not as easy as dragging node connectors. But the idea is that AI creates the flows and you can easily understand them.This isn't a shaky demo. I'm using it as my daily driver to create complex multi-agent personas, run research and info gathering swarms, and whatever else my agent needs to get it…
