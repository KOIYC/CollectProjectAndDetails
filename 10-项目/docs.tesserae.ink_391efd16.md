---
type: "project"
title: "What a self-hosted dashboard looks like on 31.5 inches of colour e-ink"
project_url: "https://docs.tesserae.ink/"
first_seen: "2026-11-21T14:46:47+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/selfhosted
  - Wednesday Exceptions
lang: "en"
---

# What a self-hosted dashboard looks like on 31.5 inches of colour e-ink

> [!info] 一句话导读
> I maintain Tesserae, a self-hosted server for e-ink dashboards. You compose a dashboard in the browser, the server renders it headless, and it pushes the frame …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://docs.tesserae.ink/>
> 首次收录：2026-11-21T14:46:47+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/selfhosted, Wednesday Exceptions
> 最新指标：得分=2669 · 评论=150 · 赞踩比=0.9826086956521739

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-21T14:46:47+08:00 | Reddit 独立开发版块 | 得分=2669 · 评论=150 · 赞踩比=0.9826086956521739 | [[20-语料/posts/reddit/2026-11-21/b753fa1c4e0e3c8b_What-a-self-hosted-dashboard-looks-like-on-31.5-in]] |

## 摘要正文

I maintain Tesserae, a self-hosted server for e-ink dashboards. You compose a dashboard in the browser, the server renders it headless, and it pushes the frame to your panels. It's AGPL-3.0, runs as a Docker container or Home Assistant add-on, and needs no account.  The frame is a Fraimic Large Canvas, a 31.5" colour e-ink display. Two dashboards are in rotation on it:  1. The project's own numbers for the last 30 days: 606 active installs (up from 342), 1,020 stars, and 92 merged pull requests, 68 of them from 8 outside contributors. 2. My GitHub profile: contribution graph, streak, top repos and recent activity.  On the install numbers: they come from telemetry that is off by default. You're asked once at setup, and it only sends an anonymous count. If you leave it off, the server never contacts me.  I didn't lay these out by hand. Tesserae has an MCP server, so I described what I wanted and an AI agent built both through it. Each one is still just a page of HTML/CSS/JS fed by a few data sources, so you can write or edit them yourself too, for your own repos or homelab. It also runs on much cheaper panels: TRMNL, Seeed reTerminal, Inky Frame, and old Kindles.  **Repo:** [https://…
