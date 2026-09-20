---
type: "project"
title: "Show HN: Nimic – write pure Python and compile AOT to native binaries via Nim"
project_url: "https://github.com/dima-quant/nimic"
first_seen: "2026-09-21T02:52:50+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_dima-quant
  - story_48339846
  - show_hn
lang: "en"
---

# Show HN: Nimic – write pure Python and compile AOT to native binaries via Nim

> [!info] 一句话导读
> Nimic allows using pure Python as a systems language with AOT compilation. It provides systems-level functionality directly within CPython (backed by the built-…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/dima-quant/nimic>
> 首次收录：2026-09-21T02:52:50+08:00
> 来源渠道：HN Show HN
> 标签：author_dima-quant, story_48339846, show_hn
> 最新指标：点赞=5 · 评论=0 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:27:24+08:00 | HN Show HN | 点赞=5 · 评论=0 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-21/55053e40e4cd7032_Show-HN-Nimic-–-write-pure-Python-and-compile-AOT]] |
| 2026-09-21T02:52:50+08:00 | HN Show HN | 点赞=5 · 评论=0 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-21/55053e40e4cd7032_Show-HN-Nimic-–-write-pure-Python-and-compile-AOT]] |

## 摘要正文

# dima-quant/nimic  Nimic allows using pure Python as a systems language with AOT compilation. It provides systems-level functionality directly within CPython (backed by the built-in ctypes module), while allowing the exact same code to compile Ahead-Of-Time (AOT) to an efficient native binary.  - Stars: 38 - Forks: 1 - Watchers: 38 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2025-12-14T19:24:06Z  ## Languages  - Nim - Python  ## Top Contributors  - dima-quant (2 contributions)  ---  ## README  # Nimic  Nimic allows using pure Python as a systems language with AOT compilation. It provides systems-level functionality directly within CPython (backed by the built-in `ctypes` module), while allowing the exact same code to compile Ahead-Of-Time (AOT) to an efficient native binary.  By closely following the Nim programming language, `nimic` includes emulation of native types, pointers and operations on them, multi-dispatch, operator overloading, templates and more. Nimic code is a statically typed Python subset (domain specific language) which transpiles to Nim, achieving C-level performance without leaving Python.  **Key principle:** `nimic` code is valid P…
