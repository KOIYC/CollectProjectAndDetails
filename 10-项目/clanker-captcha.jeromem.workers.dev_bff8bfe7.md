---
type: "project"
title: "Show HN: A Reverse Captcha for Clankers"
project_url: "https://clanker-captcha.jeromem.workers.dev/"
first_seen: "2026-09-21T02:52:46+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_rydgel
  - story_48344669
  - show_hn
lang: "en"
---

# Show HN: A Reverse Captcha for Clankers

> [!info] 一句话导读
> Author: Made by  Jérôme Mahuet .

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://clanker-captcha.jeromem.workers.dev/>
> 首次收录：2026-09-21T02:52:46+08:00
> 来源渠道：HN Show HN
> 标签：author_rydgel, story_48344669, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:27:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/2e87fa3e4fa167b2_Show-HN-A-Reverse-Captcha-for-Clankers]] |
| 2026-09-21T02:52:46+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/2e87fa3e4fa167b2_Show-HN-A-Reverse-Captcha-for-Clankers]] |

## 摘要正文

Author: Made by  Jérôme Mahuet .  Clanker CAPTCHA Demo  # Clanker CAPTCHA   A playable CAPTCHA built for software instead of people. The answer is hidden in the image frames, and the page publishes everything an agent needs to dig it out. Nobody expects a human to solve this one.   Made by Jérôme Mahuet.  3-4 frames Coherent fusion required  30s TTL Fresh challenge window  No answer leak Server keeps the checksum  ## Live challenge   Playable widget The widget here is the exact library a host page would drop in. This page only hands it a mount point and a couple of endpoint URLs.   Server-kept secret The answer never reaches the browser. All the widget gets are the image frames, some public solve parameters, and a challenge id that expires within seconds.   Library-owned metadata The widget injects `clanker-agent-task`, hidden instructions, current challenge data attributes, and an `application/clanker+json` manifest.  ## Why reverse the usual CAPTCHA shape?   The usual CAPTCHA looks for something people find easy and software finds hard. That gap has been closing for years. Clanker CAPTCHA flips it around: the task is a pain to do by hand against a timer, but simple for an agent t…
