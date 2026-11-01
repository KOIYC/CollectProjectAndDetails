---
type: "project"
title: "Show HN: A Kotlin compiler written in Go, 10x faster than kotlinc"
project_url: "https://github.com/barteo/kotlin-compiler-go"
first_seen: "2026-11-01T09:38:09+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_barteo
  - story_50315577
  - show_hn
lang: "en"
---

# Show HN: A Kotlin compiler written in Go, 10x faster than kotlinc

> [!info] 一句话导读
> barteo/kotlin-compiler-go

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/barteo/kotlin-compiler-go>
> 首次收录：2026-11-01T09:38:09+08:00
> 来源渠道：HN Show HN
> 标签：author_barteo, story_50315577, show_hn
> 最新指标：点赞=3 · 评论=2 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-01T09:38:09+08:00 | HN Show HN | 点赞=3 · 评论=2 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-11-01/607516b36e162aea_Show-HN-A-Kotlin-compiler-written-in-Go,-10x-faste]] |

## 摘要正文

# barteo/kotlin-compiler-go  A Kotlin compiler for the JVM in Go, 10x faster than kotlinc  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: Apache License 2.0 - Default branch: main - Created: 2026-10-31T11:02:08Z  ## Languages  - Go - Java - Python - Shell  ## Topics  - compiler - go - jvm - kotlin  ## Top Contributors  - barteo (1 contributions)  ---  ## README  # kotlin-compiler-go: a Kotlin compiler in Go  `kc` is a Kotlin compiler for the JVM, written in Go. On real libraries it compiles 10x faster or more than `kotlinc` running in a warm JVM, and uses about a tenth of the memory. The libraries it builds pass their own test suites (Survey of real code), and it passes 95% of `kotlinc`'s box tests (Conformance).  It is a prototype: it compiles most of Kotlin but not all of it, and it checks less than `kotlinc` does (What it doesn't do).  ## Results  `kc` against `kotlinc` 2.4.21 on an Apple M2 MacBook Air (8 cores, 16 GB), JDK 21. `kotlinc` runs in a warm JVM, as it does in the Gradle daemon: the median of repeated compilations in one JVM, after the JIT has warmed up. `kc` uses all cores, as it does by default.  | Project | Files | Lines | `kotlinc` | `kc` | Speed…
