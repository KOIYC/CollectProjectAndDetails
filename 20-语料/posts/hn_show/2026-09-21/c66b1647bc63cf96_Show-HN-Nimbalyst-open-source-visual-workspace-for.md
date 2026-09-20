---
type: "corpus"
item_id: "c66b1647bc63cf96"
title: "Show HN: Nimbalyst open-source visual workspace for ClaudeCode, Codex, OpenCode"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47962230"
project_url: "https://github.com/Nimbalyst/nimbalyst"
author: "ghinkle"
published_at: "2026-04-30T13:36:06Z"
captured_at: "2026-09-21T01:40:59+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_ghinkle
  - story_47962230
  - show_hn
metrics: {"points": 8, "comments": 4, "engagement_velocity": 8}
comments_count: 4
comments_total: 4
discovered_via: "hn:show_hn:174d"
---

# Show HN: Nimbalyst open-source visual workspace for ClaudeCode, Codex, OpenCode

> [!info] 一句话导读
> We're open sourcing Nimbalyst, a multi-agent, visual workspace for building with Claude Code, Codex, and Opencode (alpha). It pairs parallel session management …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47962230>
> 指标：点赞=8 · 评论=4 · engagement_velocity=8
> 作者：ghinkle　|　发布：2026-04-30T13:36:06Z
> 项目链接：<https://github.com/Nimbalyst/nimbalyst>
> 采集：2026-09-21T01:40:59+08:00　|　id：`c66b1647bc63cf96`

## 正文

We're open sourcing Nimbalyst, a multi-agent, visual workspace for building with Claude Code, Codex, and Opencode (alpha). It pairs parallel session management with WYSIWYG editors so you and your agents can work on the same files at the same time.The core idea: agents edit files, you edit files, and Nimbalyst makes that collaboration legible. Built-in WYSIWYG editors cover markdown, mockups, Excalidraw diagrams, data models, spreadsheets, and code (Monaco). Every edit is tracked back to the session that made it, with red/green WYSIWYG markdown diffs for review and approval. A session Kanban lets you search, resume, and manage parallel runs, and link sessions to files (and back). A lightweight tracker (alpha) keeps plans, bugs, tasks, and custom items in the same workspace the agent is working in — agents create, update, and execute them, and you see the same view they do. The extension system makes any file type pluggable; current extensions include Excalidraw, mind maps, CSV spreadsheets, a data model designer, mockups, PDF viewing, and a SQLite browser, and they're exposed to the agents too. Worktrees, workstreams, visual git management, and agent-driven commit proposals round out the developer side, and an iOS app handles remote session management (Android in development). Currently supports Claude Code, Codex, Opencode (alpha), and Copilot (alpha), with more planned.It's local-first: files stay on your filesystem in open formats (markdown, excalidraw, html). The local app is MIT licensed and free; team collaboration features are AGPL and will be paid. Tech stack: Electron, React, Jotai, PGLite (Postgres in WASM), Lexical, Monaco, Playwright; collaboration runs on Cloudflare Workers with Durable Objects.https://github.com/Nimbalyst/nimbalysthttps://nimbalyst.com/We'd love your feedback and contributions.

## 评论（4/4）

> **radial_symmetry** · 2026-04-30T14:03:58.000Z　
> Congrats on going open-source, can't wait to see the community contributions come in

---

> **chrispwirth** · 2026-04-30T14:35:19.000Z　
> looks cool! do you plan on adding support for jupyter notebooks?

---

> **wek** · 2026-04-30T14:28:06.000Z　
> Thanks! A good way to learn the platform is by building an extension.

---

> **wek** · 2026-04-30T14:45:38.000Z　
> This is on our wish list for a custom extension. Many users have asked for it. If someone in the community wants to take a crack at it....

## 关联链接

- https://github.com/Nimbalyst/nimbalysthttps://nimbalyst.com/We

## 导航

- 项目页：[[10-项目/github.com_ae95b3f8]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
