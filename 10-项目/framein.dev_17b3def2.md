---
type: "project"
title: "Show HN: Framein – a local work-state layer that keeps AI agents in context"
project_url: "https://framein.dev/"
first_seen: "2026-09-21T02:53:08+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_BonPPa
  - story_48731852
  - show_hn
lang: "en"
---

# Show HN: Framein – a local work-state layer that keeps AI agents in context

> [!info] 一句话导读
> Local work frame for AI coding

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://framein.dev/>
> 首次收录：2026-09-21T02:53:08+08:00
> 来源渠道：HN Show HN
> 标签：author_BonPPa, story_48731852, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:29:55+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/126ebcb72a1a0917_Show-HN-Framein-–-a-local-work-state-layer-that-ke]] |
| 2026-09-21T02:53:08+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/126ebcb72a1a0917_Show-HN-Framein-–-a-local-work-state-layer-that-ke]] |

## 摘要正文

GitHub  KO Local work frame for AI coding Keep one work frame across Claude, Codex, and Gemini. Start with one agent, challenge it with another, switch when needed, and close the work with validation. Framein keeps a shared task contract, decision trail, risk state, validation results, and model-switch capsule beneath the agent harness you already use. Read the README  Install guide  Open the Manual pre-release v0.0.6  249 tests  zero runtime dependencies  Node 22.5+ # Start in the agent you already use.  $ framein start "add Google OAuth" contract set : preserve email login lead claude # Ask a different model for a bounded objection.  $ framein challenge "OAuth callback state in session" --run reviewer codex verdict challenge required add nonce/state validation lead accepts required change # Switch when needed; close with validation.  $ framein capsule gemini next lead prepared from facts: contract · diff · tests · decisions $ framein ship build ok · tests passed risk high: auth/ touched => READY WITH HUMAN GATE 30-second demo Challenge, verify, and hand off without losing context. A payment-task walkthrough showing a task contract, independent model challenge, validation evidence…
