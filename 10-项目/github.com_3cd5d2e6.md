---
type: "project"
title: "Show HN: Jevlang: Python with a Smart \"If\""
project_url: "https://github.com/sumanmichael/jevlang"
first_seen: "2026-09-21T09:44:03+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_sumanmichael
  - story_49780133
  - show_hn
lang: "en"
---

# Show HN: Jevlang: Python with a Smart "If"

> [!info] 一句话导读
> sumanmichael/jevlang

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/sumanmichael/jevlang>
> 首次收录：2026-09-21T09:44:03+08:00
> 来源渠道：HN Show HN
> 标签：author_sumanmichael, story_49780133, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T09:44:03+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/a1a22ebd0d097a12_Show-HN-Jevlang-Python-with-a-Smart-If]] |

## 摘要正文

# sumanmichael/jevlang  The simplest way to write decision workflows in Python. Python with a smart if.  - Stars: 3 - Forks: 0 - Watchers: 3 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-09-20T17:27:50Z  ## Languages  - Python  ## Top Contributors  - sumanmichael (1 contributions)  ---  ## README   jevlang   The simplest way to write decision workflows in Python.   Python with a smart if.  ```python if ticket ~ "the customer wants a refund":     route("billing") ```  `~` asks a question about a value and gets back a number or a label, never text. Here it is a probability, and the `if` fires at `>= 0.5`. The model answering is TypeSafe's Jev, a hosted classifier that judges instead of writes.  Four things to know first:  - `.jev` is Python plus two forms: `x ~ question` and a `jev`/`case` block.  Files are rewritten to plain Python at import time. No new interpreter. - Every `~` is one call to TypeSafe's API. It needs a key and is paid per call. - The value left of `~` is what gets sent. Keep secrets out of it. - Answers are probabilities, not facts. Guard the branches that matter.  It is a prototype: tested, working, with its limits listed below.  #…
