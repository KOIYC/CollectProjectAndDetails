---
type: "project"
title: "Show HN: DBDelve – Open-Source DB Client Made with Rust and GPUI"
project_url: "https://github.com/ShayanAbbas1/dbdelve"
first_seen: "2026-11-10T09:49:42+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_shayan_abbas
  - story_50427934
  - show_hn
  - front_page
lang: "en"
---

# Show HN: DBDelve – Open-Source DB Client Made with Rust and GPUI

> [!info] 一句话导读
> Hi HN, I’m Shayan and a few months ago I started building a DB Client DBDelve with a focus on performance and just making something that feels good to use (in t…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/ShayanAbbas1/dbdelve>
> 首次收录：2026-11-10T09:49:42+08:00
> 来源渠道：HN Show HN
> 标签：author_shayan_abbas, story_50427934, show_hn, front_page
> 最新指标：点赞=94 · 评论=33 · engagement_velocity=94

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-10T09:49:42+08:00 | HN Show HN | 点赞=94 · 评论=33 · engagement_velocity=94 | [[20-语料/posts/hn_show/2026-11-10/e32955d193042fab_Show-HN-DBDelve-–-Open-Source-DB-Client-Made-with]] |

## 摘要正文

Hi HN, I’m Shayan and a few months ago I started building a DB Client DBDelve with a focus on performance and just making something that feels good to use (in the spirit of Zed, Ghostty, and other tools that just feel pleasant to use).For my workflow I’ve always looked for performance, especially since some time ago I had a really outdated machine and any kind of bloat was really noticeable, I remember using DBeaver and it just crashing on me multiple times, I also had to use postGIS which just made it worse. I migrated all my essential dev tools to use the ones with performance in mind (Zed, Ghostty etc) but the only thing that was missing was DB Client. The main choices everyone has are DBeaver which is a memory hog and an overkill for most of the tasks imo. The other options like Datagrid, Beekeeper, TablePlus are either electron based so bloated and memory hogs or paid and closed-source.DBDelve 0.3.6 against DBeaver 25.3.1 on the same Postgres table, median of 5 runs each (2026-10-11, M1 Pro, 32 GB). Times are from the action to the rows rendered. DBDelve DBeaver  Launch 1.1 s 5.2 s  Idle memory 133 MB 606 MB  1,000-row query 0.21 s 1.96 s  1M rows, time 56 s 208 s  1M rows, me…
