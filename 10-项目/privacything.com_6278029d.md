---
type: "project"
title: "Show HN: I built a cross-browser extension that controls fingerprinting surfaces"
project_url: "https://privacything.com/en"
first_seen: "2026-09-21T02:55:00+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_tomaszjanusz
  - story_49124017
  - show_hn
lang: "en"
---

# Show HN: I built a cross-browser extension that controls fingerprinting surfaces

> [!info] 一句话导读
> Hello Hacker News! I’m Tomasz, creator of Privacy Thing, a browser extension for Firefox and Chromium-based browsers. I’ve just released its Preview version.Pri…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://privacything.com/en>
> 首次收录：2026-09-21T02:55:00+08:00
> 来源渠道：HN Show HN
> 标签：author_tomaszjanusz, story_49124017, show_hn
> 最新指标：点赞=20 · 评论=10 · engagement_velocity=20

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:31:46+08:00 | HN Show HN | 点赞=20 · 评论=10 · engagement_velocity=20 | [[20-语料/posts/hn_show/2026-09-21/d43a40d83f7a699e_Show-HN-I-built-a-cross-browser-extension-that-con]] |
| 2026-09-21T02:55:00+08:00 | HN Show HN | 点赞=20 · 评论=10 · engagement_velocity=20 | [[20-语料/posts/hn_show/2026-09-21/d43a40d83f7a699e_Show-HN-I-built-a-cross-browser-extension-that-con]] |

## 摘要正文

Hello Hacker News! I’m Tomasz, creator of Privacy Thing, a browser extension for Firefox and Chromium-based browsers. I’ve just released its Preview version.Privacy Thing aims to reduce browser fingerprinting—the tracking of users without cookies.It began as an internal project: a simple location simulator. Over time, I expanded it to cover more fingerprinting surfaces. It now has 13 protection categories affecting 50+ browser APIs and methods: Geolocation, time and locale settings, Canvas, WebGL, Audio, Navigator, Screen, Client Hints, Battery, WebRTC, Dedicated Workers, Service Workers, and Shared Workers. The list is still growing.The extension is fully configurable. Users can create regional profiles and assign them to domain rules, with separate protection settings for each domain. Or they can skip domain rules and rely on the global configuration—I’m not here to decide what works best for them :-)Privacy Thing uses Manifest V3, with all its pros and cons. Chrome and Firefox appear to offer similar extension APIs, but differ fundamentally at the level where Privacy Thing operates. This matters because its scripts must load as early as possible to be effective.Its X-Ray module …
