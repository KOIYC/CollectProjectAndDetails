---
type: "project"
title: "I built an event-discovery site for 1,000+ DJs in pure PHP and vanilla JS — zero dependencies, zero frameworks. Here are the parts I'm weirdly proud of."
project_url: "https://thedjcalendar.com/"
first_seen: "2026-10-29T20:43:48+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/SideProject
lang: "en"
---

# I built an event-discovery site for 1,000+ DJs in pure PHP and vanilla JS — zero dependencies, zero frameworks. Here are the parts I'm weirdly proud of.

> [!info] 一句话导读
> Launched this week: [thedjcalendar.com](http://thedjcalendar.com) — tracks tour dates for the world's biggest DJs. Around 1,000 pages (artists, venues, cities, …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://thedjcalendar.com/>
> 首次收录：2026-10-29T20:43:48+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/SideProject
> 最新指标：得分=3 · 评论=2 · 赞踩比=1

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-29T20:43:48+08:00 | Reddit 独立开发版块 | 得分=3 · 评论=2 · 赞踩比=1 | [[20-语料/posts/reddit/2026-10-29/dc645919289773db_I-built-an-event-discovery-site-for-1,000+-DJs-in]] |

## 摘要正文

Launched this week: [thedjcalendar.com](http://thedjcalendar.com) — tracks tour dates for the world's biggest DJs. Around 1,000 pages (artists, venues, cities, genres), and the whole thing is PHP + vanilla JS. No build step, no npm, no framework. I know that's a controversial lifestyle choice, so let me show the parts where it paid off.  **1. The search index is a prebuilt JSON file, not a server round-trip.** Every artist name, alias and genre gets compiled into a static JSON index at deploy time. Client-side matching scores candidates and returns results in a keyboard-navigable combobox. Search feels instant because there's no network involved at all. On a shared host with no Node, this was the difference between "search box" and "search feature."  **2. The equalizer bars aren't animated — they're a readout.** Hovering an artist card previews one of their tracks, and an 8-bar EQ reacts to the actual audio via Web Audio's AnalyserNode. Every animation frame the analyser hands me 32 frequency bins (0-255); bar N IS bin N. No easing, no random jitter to fake liveliness. When the preview stops, the bars flatline. It's an instrument readout, not a decoration — and it took real work to…
