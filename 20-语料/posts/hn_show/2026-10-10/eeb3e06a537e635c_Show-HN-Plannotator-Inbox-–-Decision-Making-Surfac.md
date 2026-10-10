---
type: "corpus"
item_id: "eeb3e06a537e635c"
title: "Show HN: Plannotator Inbox – Decision Making Surface for Agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50024247"
project_url: "https://plannotator.ai/inbox"
author: "ramoz"
published_at: "2026-10-09T17:52:26Z"
captured_at: "2026-10-10T09:53:50+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-10"
pub_day: "2026-10-09"
tags:
  - 语料
  - hn_show
  - author_ramoz
  - story_50024247
  - show_hn
metrics: {"points": 3, "comments": 1, "engagement_velocity": 3}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Plannotator Inbox – Decision Making Surface for Agents

> [!info] 一句话导读
> An async surface for your long‑running agents

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50024247>
> 指标：点赞=3 · 评论=1 · engagement_velocity=3
> 作者：ramoz　|　发布：2026-10-09T17:52:26Z
> 项目链接：<https://plannotator.ai/inbox>
> 采集：2026-10-10T09:53:50+08:00　|　id：`eeb3e06a537e635c`

## 正文

Plannotator
Docs
 |
Blog
 |
Inbox
 |
Workspaces
 soon |
GitHub
plannotator inbox
An async surface for your long‑running agents
Coding agents now work for hours. Over a run they have questions. They hit blockers. They produce plans and
 prototypes and diffs you need to review. The Inbox is where all of that arrives while they keep working. You
 read it like mail and answer when you get to it. Reviewing and annotating is the native Plannotator
 experience. The agent picks up your answer and goes on.
Local. Claude Code and Pi and OpenCode and any MCP agent. Open source.
 $ curl -fsSL https://plannotator.ai/install.sh | bash
 then plannotator inbox
 GitHub
How it works
Why not the agent's own window
The agent's window is for the run you are watching. Long runs are the ones you are not watching. With several
 agents going you are not sitting in any of their windows. Their questions and blockers and reviews need
 somewhere to land that is not a scrollback.
The Inbox is that place. Every agent writes to it. Each item is a thread with its context attached. You open
 it when you are ready. You answer or annotate once. The agent continues from there.
How it works
 01 An agent writes to the Inbox while it works.
 A question with options. A blocker. A plan or a prototype or a diff to review.
02 You answer in the Inbox.
 Pick an option. Annotate the file with Plannotator. Send.
03 The agent gets the answer.
 It arrives as the session's next turn. The thread shows "Delivered to Claude Code".
What arrives during one run
 01
 The plan
The agent drafts a plan and asks what it cannot decide alone. The plan opens next to the thread. You comment
 on a line and pick the answers. Nothing reaches the agent until you send.
If the agent edits the plan after sending it the Inbox says so and opens the version it sent.
You are somewhere else while this happens. The agents keep working. The Inbox tells you when something needs you.
02
 A question the plan did not cover
Halfway through the agent hits a case the plan left open and stops. The thread goes to the top under
 "Stopped on you". You answer. If the answer is a decision you turn the switch on and the decision is stored
 with the project. Your agents read it on the next run.
03
 A prototype
The agent attaches the prototype. It opens inside the Inbox at full screen. You pin comments on the parts to
 change. The comments go with your next send.
Markdown and HTML and Mermaid and Graphviz. Plannotator's annotation tools.
The prototype open in the Inbox with one comment pinned
 04
 The guided review
At the end of the run the agent sends a guided review. The change is split into sections in reading order.
 Each section has its diff and a short summary. Every file is checked against the real diff. You read the whole
 change in one sitting.
Connections
Plannotator's Claude Code mod and Pi extension and OpenCode plugin write to the Inbox on their own and wake
 the agent when you send. Nothing to install for those three.
Claude Code
 Pi
 OpenCode
Any other agent connects to the Inbox as a local MCP server. The Inbox shows the exact step for Codex and
 Cursor and VS Code and Gemini CLI and Zed and Goose and Amp and Cline.
codex mcp add plannotator-inbox -- plannotator inbox mcp
Local
 Listens on 127.0.0.1 . Opens in your browser.
 Threads and answers and decisions are files under ~/.plannotator .
 Part of Plannotator. MIT or Apache 2.0.
 coming
The same inbox hosted and on your phone.
Blog An Async Surface for Long-Running Agents
 Install
 Install Plannotator and run plannotator inbox .
 $ curl -fsSL https://plannotator.ai/install.sh | bash
Install guide
 GitHub
×
Product
 Plan Review
 Code Review
 Inbox
 Install
Resources
 Quickstart
 Security
 Claude Code
 OpenCode
 Learn
Community
 GitHub
 @backnotprop
 @plannotator
Plannotator
© 2026 backnotprop.
Licensed under MIT or Apache 2.0 , at your option.
Privacy Policy
Built by
With contributions from

## 评论（1/1）

> **ramoz** · 2026-10-09T17:52:26.000Z　
> Plannotator Inbox is an optional runtime using the best of plannotator annotation capabilities.While all your agents work they constantly bombard you with decisions that need to be made. Those decisions get lost over time, Claude might hit you with "I need your 2 answers to X and Y" which was asked 2 days ago. Think about all the remote pi durables to come basically... how can we surface all the important stuff we need to review...The chat ui thread, imo, is becoming outdated very fast. We need a new way to interface with agents and surface the things that matter in an intuitive way. Plannotator Inbox is a stab at that.part of the free/open source capability at: https://github.com/backnotprop/plannotatorAlso feel free to show your love or hate on the x announcement:
> https://x.com/plannotator/status/2108589088139886769?s=20

## 关联链接

- https://plannotator.ai/install.sh

## 导航

- 项目页：[[10-项目/plannotator.ai_3c75822e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
