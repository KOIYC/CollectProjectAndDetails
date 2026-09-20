---
type: "project"
title: "Show HN: A Coding Agent from Scratch"
project_url: "https://blog.softwarewrighter.com/2026/09/16/ai-tools-coding-agent-in-mlpl"
first_seen: "2026-09-20T09:37:00+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_softwarewright
  - story_49729456
  - show_hn
lang: "en"
---

# Show HN: A Coding Agent from Scratch

> [!info] 一句话导读
> Published: 2026-09-16

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://blog.softwarewrighter.com/2026/09/16/ai-tools-coding-agent-in-mlpl>
> 首次收录：2026-09-20T09:37:00+08:00
> 来源渠道：HN Show HN
> 标签：author_softwarewright, story_49729456, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/a1683742b4ef29d9_Show-HN-A-Coding-Agent-from-Scratch]] |
| 2026-09-20T09:37:00+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/a1683742b4ef29d9_Show-HN-A-Coding-Agent-from-Scratch]] |

## 摘要正文

Published: 2026-09-16 Author: Software Wrighter  AI Tools #7: A Coding Agent Small Enough to Understand | Software Wrighter Lab Blog  # AI Tools #7: A Coding Agent Small Enough to Understand  September 16, 2026 • Software Wrighter  Coding agents are usually described from the outside: a product with a terminal UI, a permission system, a dozen tools, and a model behind it all. mlplcode is the inside, kept small: the whole control loop in sw-MLPL, an array language, with Rust only for the mechanisms the language cannot express and a local model for inference. One LLM primitive, six verbs, about 850 lines of MLPL that matter and 220 of Rust --- and a verifier standing between the model's claim of success and the real thing, because a 7B model will say it ran the tests when it did not.  Strip a coding agent down to what it actually does and there is not much left: build a prompt from the task and what has happened so far, ask a model, read the one action it asks for, check whether that action is allowed, do it, add the result to what has happened so far, repeat. Everything else in a product-grade agent — the terminal UI, sessions, providers, MCP, language servers, subagents — is engine…
