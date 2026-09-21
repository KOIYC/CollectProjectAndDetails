---
type: "project"
title: "Show HN: Uniflow – a code skeleton so feature #50 looks like feature #1"
project_url: "https://github.com/splendidz/uniflow"
first_seen: "2026-09-21T09:54:59+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_splendidz
  - story_48731598
  - show_hn
lang: "en"
---

# Show HN: Uniflow – a code skeleton so feature #50 looks like feature #1

> [!info] 一句话导读
> Run dozens of concurrent flows on a single thread - a header-only C++17 cooperative-scheduling framework (reactor + worker-pool), zero deps

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/splendidz/uniflow>
> 首次收录：2026-09-21T09:54:59+08:00
> 来源渠道：HN Show HN
> 标签：author_splendidz, story_48731598, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:29:55+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/c7ff48776160c3bf_Show-HN-Uniflow-–-a-code-skeleton-so-feature-50-lo]] |
| 2026-09-21T02:53:09+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/c7ff48776160c3bf_Show-HN-Uniflow-–-a-code-skeleton-so-feature-50-lo]] |
| 2026-09-21T03:11:00+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/c7ff48776160c3bf_Show-HN-Uniflow-–-a-code-skeleton-so-feature-50-lo]] |
| 2026-09-21T09:54:59+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/c7ff48776160c3bf_Show-HN-Uniflow-–-a-code-skeleton-so-feature-50-lo]] |

## 摘要正文

# splendidz/uniflow  Run dozens of concurrent flows on a single thread - a header-only C++17 cooperative-scheduling framework (reactor + worker-pool), zero deps  - Stars: 4 - Forks: 0 - Watchers: 4 - Open issues: 0 - License: MIT License - Homepage: https://splendidz.github.io/uniflow/ - Default branch: develop - Created: 2026-05-21T13:42:26Z  ## Languages  - C# - C++ - CMake - Python  ## Topics  - async - automation - concurrency - cooperative-scheduling - cpp - cpp17 - event-loop - header-only - reactor - state-machine  ## Top Contributors  - splendidz (8 contributions)  ---  ## README  # uniflow  > Language: 한국어 | **English**  ci C++17 header-only dependencies platform license  ``` 1 header  |  0 external deps  |  C++17  |  no build system required ```   Left: dozens of cars driving by the signals in city_traffic  |  Right: two pickers running a line with no zone collision in pick_and_place  Both demos use zero application-level threads. Every flow runs cooperatively on a single pump thread.  ---  ## What uniflow is.  uniflow is a **tick-based FSM (finite state machine) asynchronous execution framework**. But not the traditional `switch`-with-`sleep` kind - it strips away the ch…
