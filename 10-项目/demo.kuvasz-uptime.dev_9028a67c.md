---
type: "project"
title: "Kuvasz Uptime 4.5.0 is out, the biggest release in a while"
project_url: "https://demo.kuvasz-uptime.dev/"
first_seen: "2026-10-25T23:28:44+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/selfhosted
  - Release (AI)
lang: "en"
---

# Kuvasz Uptime 4.5.0 is out, the biggest release in a while

> [!info] 一句话导读
> https://i.redd.it/uqrf0ttmbnvh1.png

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://demo.kuvasz-uptime.dev/>
> 首次收录：2026-10-25T23:28:44+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/selfhosted, Release (AI)
> 最新指标：得分=52 · 评论=33 · 赞踩比=0.8513513513513513

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-25T23:28:44+08:00 | Reddit 独立开发版块 | 得分=52 · 评论=33 · 赞踩比=0.8513513513513513 | [[20-语料/posts/reddit/2026-10-25/d4cab022084077b6_Kuvasz-Uptime-4.5.0-is-out,-the-biggest-release-in]] |

## 摘要正文

https://i.redd.it/uqrf0ttmbnvh1.png  Hey there,  first of all:  *Kuvasz* is an open-source, self-hostable monitoring solution (HTTP, TCP, DNS, push, Docker and ICMP) with status pages, webhooks, an MCP server and IAC support, a great alternative to UptimeRobot or Kuma.  **How AI was used in the project**: I started working on it in 2020 and I didn't use any LLM up until this May (version 3.8.0). Since then I use Claude Code in a quite "old-fashioned" way: I commit everything by hand after carefully reviewing every change on the project. The pre-existing quality gates of the project are also very strict to make slop even harder to introduce.  I was working on the latest release a lot, probably this is the biggest one since the project exists: [https://kuvasz-uptime.dev/changelog/#4.5.0](https://kuvasz-uptime.dev/changelog/#4.5.0)  # A brand new dashboard (see the screenshot above)  The old one was quite ugly and also not so informative, so I rewrote it from scratch.  # Docker monitoring  Instead of checking a port, Docker monitors ask the daemon whether a container is actually running and healthy. They catch crash loops, OOM kills, paused containers and failing healthchecks, and the…
