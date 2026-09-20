---
type: "project"
title: "Show HN: Sokit – a LangChain like harness for Jev (or other System 1 models)"
project_url: "https://github.com/jodan-alberts/sokit"
first_seen: "2026-09-20T14:02:58+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_phantomCupcake
  - story_49744527
  - show_hn
lang: "en"
---

# Show HN: Sokit – a LangChain like harness for Jev (or other System 1 models)

> [!info] 一句话导读
> A harness to allow users to build agents using System One models.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/jodan-alberts/sokit>
> 首次收录：2026-09-20T14:02:58+08:00
> 来源渠道：HN Show HN
> 标签：author_phantomCupcake, story_49744527, show_hn
> 最新指标：点赞=2 · 评论=1 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/a05eb765e482b181_Show-HN-Sokit-–-a-LangChain-like-harness-for-Jev-(]] |
| 2026-09-20T09:36:47+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/a05eb765e482b181_Show-HN-Sokit-–-a-LangChain-like-harness-for-Jev-(]] |
| 2026-09-20T14:02:58+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/a05eb765e482b181_Show-HN-Sokit-–-a-LangChain-like-harness-for-Jev-(]] |

## 摘要正文

# jodan-alberts/sokit  A harness to allow users to build agents using System One models.  - Stars: 2 - Forks: 0 - Watchers: 2 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-09-17T09:38:49Z  ## Languages  - Python  ## Top Contributors  - jodan-alberts (11 contributions)  ---  ## README  # SOKIT (System One Knowledge Instructions Tools)  A decision-driven agent harness for **System One models** (TypeSafe's Jev-class models). System One models make fast, calibrated, typed decisions but cannot generate text, call tools, or fetch data on their own. This harness is the *body* that adds those abilities: **iterate**, **call tools**, and **access external datasources** — while the model stays a calibrated policy.  Read **DESIGN.md** for the full design rationale.  ## Layout  ``` harness/   client.py      # SystemOneClient (TypeSafe / mock) — the model adapter   decisions.py   # Question, Decision, Evaluation (Choice / Score / Noul)   state.py       # State (working memory) + Event   context.py     # StateBuilder + ContextProvider protocol + Document   providers.py   # Files/HTTP/clock/memory/SQL providers (web-search stub)   policy.py      # Policy, Action (i…
