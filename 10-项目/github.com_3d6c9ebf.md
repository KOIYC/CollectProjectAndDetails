---
type: "project"
title: "Show HN: Jev as the Bletchley Park Analyst: A Software Bombe on Enigma"
project_url: "https://github.com/agodoy21/enigma-jev"
first_seen: "2026-09-30T18:57:07+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_ag_21
  - story_49903792
  - show_hn
lang: "en"
---

# Show HN: Jev as the Bletchley Park Analyst: A Software Bombe on Enigma

> [!info] 一句话导读
> License: MIT License

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/agodoy21/enigma-jev>
> 首次收录：2026-09-30T18:57:07+08:00
> 来源渠道：HN Show HN
> 标签：author_ag_21, story_49903792, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-30T18:28:30+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-30/694dc1812e9311a0_Show-HN-Jev-as-the-Bletchley-Park-Analyst-A-Softwa]] |
| 2026-09-30T18:57:07+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-30/694dc1812e9311a0_Show-HN-Jev-as-the-Bletchley-Park-Analyst-A-Softwa]] |

## 摘要正文

# agodoy21/enigma-jev  - Stars: 2 - Forks: 0 - Watchers: 2 - Open issues: 0 - License: MIT License - Homepage: https://enigma-jev.vercel.app - Default branch: main - Created: 2026-09-28T17:36:55Z  ## Languages  - CSS - HTML - Python - TypeScript  ## Top Contributors  - agodoy21 (5 contributions)  ---  ## README  # enigma-jev  **A software Turing–Welchman Bombe that breaks real Enigma traffic, with a probabilistic analyst deciding what counts as German.**  CI License: MIT Bun TypeScript Tests  The Enigma I in its oak case, locked until a key is entered  enigma-jev rebuilds Bletchley Park's pipeline in software, then measures it. The pipeline is a verified Enigma I, M3 and M4, crib dragging, a Bombe with Welchman's diagonal board, and a ciphertext-only hill-climber. Two steps in that pipeline were human judgement calls: which probable phrase to try, and whether a trial decryption is German. Here **Jev**, a model that answers only typed probabilistic questions, makes those two calls. The code runs a tiered backtest against historical intercepts with published keys. A second study compares Jev against n-gram judges and XGBoost on the same candidates.  It comes with three pages:  | | | …
