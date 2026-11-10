---
type: "project"
title: "Show HN: A doc server where Claude or local agent edits based on added comments"
project_url: "https://smarchone.github.io/docs"
first_seen: "2026-11-10T09:49:42+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_smarch27
  - story_50428595
  - show_hn
lang: "en"
---

# Show HN: A doc server where Claude or local agent edits based on added comments

> [!info] 一句话导读
> Comment on your docs.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://smarchone.github.io/docs>
> 首次收录：2026-11-10T09:49:42+08:00
> 来源渠道：HN Show HN
> 标签：author_smarch27, story_50428595, show_hn
> 最新指标：点赞=2 · 评论=1 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-10T09:49:42+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-10/a3e946ede33c4d92_Show-HN-A-doc-server-where-Claude-or-local-agent-e]] |

## 摘要正文

~/ smarchone/docs Star on GitHub Comment on your docs.  Claude makes the edits. tl;dr Comment on your repo's Markdown docs in the browser. Claude Code, or any local agent, edits the file and replies. The problem Editing a doc from the terminal means describing where the problem is: "second section, the bullet about retries…" Then you scroll a diff to check it got the right spot. That's a lot of attention for a one-line fix, and you lose your place in the doc. How it works One small daemon on your machine. Each repo's agent connects to it with a skill and a polling script. Browser  The editor One tab for every repo. You read, highlight and comment. Changes stream in live. ⇄ comments edits Daemon  docs serve · localhost:3459 Owns the workspaces. Stores each doc's comment threads and version history, and queues threads as jobs for that repo's agent. repo-a/.docs threads · history · job queue repo-b/.docs threads · history · job queue ⇄ jobs replies Agent, per repo  Skill + poll.sh Claude Code with the /collab-docs skill, or any local agent. It edits the Markdown file directly and posts replies. The skill registers the current repo as a workspace. docs serve "$PWD" starts the daemon if…
