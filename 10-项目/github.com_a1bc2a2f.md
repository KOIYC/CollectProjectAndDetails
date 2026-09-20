---
type: "project"
title: "Show HN: Roam, a GPS speedometer that tries not to burn in your OLED"
project_url: "https://github.com/Nicsilver/roam"
first_seen: "2026-09-21T03:11:28+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_Nicsilver
  - story_49502017
  - show_hn
lang: "en"
---

# Show HN: Roam, a GPS speedometer that tries not to burn in your OLED

> [!info] 一句话导读
> GPS speedometer for Android built around OLED burn-in avoidance

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/Nicsilver/roam>
> 首次收录：2026-09-21T03:11:28+08:00
> 来源渠道：HN Show HN
> 标签：author_Nicsilver, story_49502017, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:33:52+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/3dc36f078d95c02a_Show-HN-Roam,-a-GPS-speedometer-that-tries-not-to]] |
| 2026-09-21T03:11:28+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/3dc36f078d95c02a_Show-HN-Roam,-a-GPS-speedometer-that-tries-not-to]] |

## 摘要正文

# Nicsilver/roam  GPS speedometer for Android built around OLED burn-in avoidance  - Stars: 4 - Forks: 0 - Watchers: 4 - Open issues: 0 - License: GNU Affero General Public License v3.0 - Default branch: main - Created: 2026-07-31T18:28:29Z  ## Languages  - Kotlin  ## Top Contributors  - Nicsilver (8 contributions)  ---  ## README  # Roam  A GPS speedometer for Android that treats your OLED with respect.  Feature graphic  Most people who want a speed readout in the car just open Google Maps and leave it on. That works, but hours of a bright, static UI is exactly how OLED panels burn in. Roam shows one thing, your current GPS speed, on a pure black screen, and is built from the ground up to leave no trace on your panel.  ## How it protects your screen  - **The readout moves.** Every few minutes (1 to 10, your choice) the speed display glides to a new position. Positions are chosen so consecutive spots land far apart and the whole screen gets used evenly over a drive. - **Pure black background.** On OLED, black pixels are off. Only the digits are lit. - **Colour drift.** The digit colour slowly shifts hue so no single subpixel carries the whole load. - **Outline digits.** Optional ho…
