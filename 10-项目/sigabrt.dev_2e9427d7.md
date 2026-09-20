---
type: "project"
title: "Show HN: Sigabrt.dev – cronjob monitor with an SSH TUI"
project_url: "https://sigabrt.dev/"
first_seen: "2026-09-20T09:48:16+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_4815162342
  - story_49765354
  - show_hn
lang: "en"
---

# Show HN: Sigabrt.dev – cronjob monitor with an SSH TUI

> [!info] 一句话导读
> Hello HN. I built this mostly to monitor the things I host myself. I know it's nothing too exciting.Anyway, the TL;DR is: Create an endpoint, and if your script…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://sigabrt.dev/>
> 首次收录：2026-09-20T09:48:16+08:00
> 来源渠道：HN Show HN
> 标签：author_4815162342, story_49765354, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/b4245b92ce5ba205_Show-HN-Sigabrt.dev-–-cronjob-monitor-with-an-SSH]] |
| 2026-09-20T09:36:36+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/b4245b92ce5ba205_Show-HN-Sigabrt.dev-–-cronjob-monitor-with-an-SSH]] |
| 2026-09-20T09:48:16+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/b4245b92ce5ba205_Show-HN-Sigabrt.dev-–-cronjob-monitor-with-an-SSH]] |

## 摘要正文

Hello HN. I built this mostly to monitor the things I host myself. I know it's nothing too exciting.Anyway, the TL;DR is: Create an endpoint, and if your script/cronjob fails to regularly ping it, you get notified (by email or ntfy). E.g.: 0 * * * * ./script.sh && curl -fsS https://sigabrt.dev/pulse//beat  It also has an SSH TUI which is currently experimental and read-only, mostly because I'm not sure whether it is actually useful or just a gimmick :): ssh sigabrt.dev  To use it, simply add your SSH public key in your account settings.Yes, there are services like this already, and this is minimalistic by comparison. Feedback is welcome.
