---
type: "project"
title: "Show HN: Pico, a small register-based scripting language I wrote in C"
project_url: "https://github.com/the0cp/pico"
first_seen: "2026-09-21T02:52:47+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_vaergawdd
  - story_48344259
  - show_hn
lang: "en"
---

# Show HN: Pico, a small register-based scripting language I wrote in C

> [!info] 一句话导读
> A small, compact, register-based scripting language and virtual machine implemented in C. Inspired by clox.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/the0cp/pico>
> 首次收录：2026-09-21T02:52:47+08:00
> 来源渠道：HN Show HN
> 标签：author_vaergawdd, story_48344259, show_hn
> 最新指标：点赞=2 · 评论=1 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:27:24+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/3ea90c193883baf3_Show-HN-Pico,-a-small-register-based-scripting-lan]] |
| 2026-09-21T01:43:01+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/3ea90c193883baf3_Show-HN-Pico,-a-small-register-based-scripting-lan]] |
| 2026-09-21T02:52:47+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/3ea90c193883baf3_Show-HN-Pico,-a-small-register-based-scripting-lan]] |

## 摘要正文

# the0cp/pico  A small, compact, register-based scripting language and virtual machine implemented in C. Inspired by clox.  - Stars: 6 - Forks: 0 - Watchers: 6 - Open issues: 0 - License: GNU General Public License v3.0 - Default branch: master - Created: 2025-07-16T12:05:39Z  ## Languages  - C - CMake - Shell  ## Topics  - c - compiler - compiler-design - gcc - interpreter - language - programming-language - scripting-language - virtual-machine  ## Top Contributors  - the0cp (154 contributions)  ---  ## README  # PiCo  A small, compact scripting language and virtual machine implemented in C. pico includes a compiler, virtual machine, REPL, and a set of core modules for working with values, objects, and I/O.  ## Features  - Register-based bytecode VM - REPL - Functions and closures - Classes and methods - Modules - Lists, maps, strings, and slicing - Small standard library - Manual / automatic GC modes  See the included `manual.md` for a detailed language reference and usage examples: https://github.com/the0cp/pico/blob/master/manual.md  ## What it looks like  ```javascript # A tiny PiCo demo:   func slug(s) {     return s.trim().lower().replace(" ", "-"); }  func badge(s) {     re…
