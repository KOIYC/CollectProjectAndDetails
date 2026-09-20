---
type: "project"
title: "Show HN: Hillock: Local neuro-symbolic memory engine in <1.2GB VRAM"
project_url: "https://github.com/roandejager/Hillock"
first_seen: "2026-09-21T03:11:29+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_roandejager5
  - story_49501209
  - show_hn
lang: "en"
---

# Show HN: Hillock: Local neuro-symbolic memory engine in <1.2GB VRAM

> [!info] 一句话导读
> License: GNU Affero General Public License v3.0

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/roandejager/Hillock>
> 首次收录：2026-09-21T03:11:29+08:00
> 来源渠道：HN Show HN
> 标签：author_roandejager5, story_49501209, show_hn
> 最新指标：点赞=12 · 评论=3 · engagement_velocity=12

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:33:52+08:00 | HN Show HN | 点赞=12 · 评论=3 · engagement_velocity=12 | [[20-语料/posts/hn_show/2026-09-21/5849687f97ebbe37_Show-HN-Hillock-Local-neuro-symbolic-memory-engine]] |
| 2026-09-21T02:57:10+08:00 | HN Show HN | 点赞=12 · 评论=3 · engagement_velocity=12 | [[20-语料/posts/hn_show/2026-09-21/5849687f97ebbe37_Show-HN-Hillock-Local-neuro-symbolic-memory-engine]] |
| 2026-09-21T03:11:29+08:00 | HN Show HN | 点赞=12 · 评论=3 · engagement_velocity=12 | [[20-语料/posts/hn_show/2026-09-21/5849687f97ebbe37_Show-HN-Hillock-Local-neuro-symbolic-memory-engine]] |

## 摘要正文

# roandejager/Hillock  - Stars: 5 - Forks: 0 - Watchers: 5 - Open issues: 0 - License: GNU Affero General Public License v3.0 - Default branch: master - Created: 2026-06-11T20:18:44Z  ## Languages  - Python  ## Top Contributors  - roandejager (46 contributions)  ---  ## README  # Hillock 🧠  Hi! This is **Hillock**, a local, personal memory system that integrates symbolic data structures with high-dimensional vector computing. I started hacking on this because standard vector databases always felt way too heavy, expensive, and over-engineered just to run a quick, offline chatbot on my own computer.  ⚠️ **Heads up:** This project is very much a work in progress and honestly, it isn't all that yet. Right now it's a personal, highly experimental research prototype. However, the ultimate ambition is to build a mathematically sound, completely gradient-free cognitive layer for secure, privacy-first local applications.  ---  ## ⚙️ How It Works (The General Flow)  Here is a quick look at how data moves through the system:  ```text        [Raw Text / PDFs]                │                ▼  (Parallel Ingestor)        [ Ollama (Qwen3) ]          │            │          ▼            ▼     [SQ…
