---
type: "corpus"
item_id: "fcd033a7afa1cb50"
title: "Show HN: An open source repo to use your personal context with any agent"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50369251"
project_url: "https://predsymod.github.io/memex"
author: "symuz"
published_at: "2026-11-04T18:04:10Z"
captured_at: "2026-11-05T11:21:45+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-05"
pub_day: "2026-11-04"
tags:
  - 语料
  - hn_show
  - author_symuz
  - story_50369251
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: An open source repo to use your personal context with any agent

> [!info] 一句话导读
> How it works Dreaming Your data GitHub

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50369251>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：symuz　|　发布：2026-11-04T18:04:10Z
> 项目链接：<https://predsymod.github.io/memex>
> 采集：2026-11-05T11:21:45+08:00　|　id：`fcd033a7afa1cb50`

## 正文

Memex
How it works Dreaming Your data GitHub
Open source. Work in progress.
Your repo remembers the code. Memex remembers you.
The durable context about you and your work, like preferences, decisions and background, shouldn't live inside one AI app. Keep it in your own database and let any agent use it.
Hi agent, set up Memex for me. Follow the instructions in SETUP.md at https://github.com/predsymod/memex
 Copy
Paste that into any coding agent. It walks you through the setup and does the typing for you.
In Claude, on Monday
save to memex: my favorite color is red
Saved to Memex.
kept in your own database
In Muse, on Friday
hi, sync memex
One new note from Claude. Pulled.
what's my favorite color?
Red. You saved that from Claude on Monday.
What goes in Memex
The durable, cross-cutting context that every tool should know, and that no single repo can hold.
Keeps
 What follows you
Your preferences and how you like to work, decisions and the reasons behind them, corrections, people and plans, and stable background on your products and projects.
Leaves to the repo
 What lives with the code
Code-specific context, status updates and to-dos stay in your repo, CLAUDE.md or AGENTS.md . Agents are told to leave them out of Memex.
Three things you say
Memex is an MCP server that runs on your own Supabase project. Agents connect to it, and the instructions they follow are plain text in the repo.
Setup
 Point an agent at the repo
It creates the tables, deploys the server and connects itself. You approve the steps that need an account.
"Set up Memex. Follow SETUP.md in the repo."
Sync
 One memory, every agent
An agent pushes what it knows that is worth keeping and pulls what the others learned, without duplicates. You decide, for each agent, what it may save.
"Sync memex."
Invoke
 Use it in your work
Search blends meaning with exact words, favors recent notes when you ask, and shows the current version of anything that was corrected.
"Review memex, then draft the plan."
Hands-off, if you want it
Ask any agent that can run scheduled tasks to keep you in sync. Say it once, and every morning it catches up on what your other agents saved and, if you choose, saves what it learned.
Pull only
 Stay current
"Sync memex every morning at 7."
Fetches what your other agents saved and gives you a short summary. Nothing is saved, so nothing needs approving.
Pull and save
 Stay in sync
"Sync memex every morning and save what's worth keeping."
Your yes at setup is the standing approval. Each run it saves a few durable decisions, lessons and facts, and tells you exactly what it saved.
Built so it stays safe while you're not watching. The server itself caps an unattended run at a small number of short notes (10 by default, and you can change it), skips anything that looks like a secret, skips repeats of what it already saved (or what you retracted), and tags every note it saves. Agents are told to leave out anything taken from web pages or emails. If a save was wrong, "retract what you saved this morning" hides those notes, and only those, and they can be restored. Nothing is ever deleted.
How the pieces fit
No hosted service in the middle. The server and the database both live in your own Supabase project.
Dreaming, if you turn it on
A nightly job reads what you saved since the last run and organizes it. It never deletes or rewrites what you wrote. Everything it changes is logged and can be undone.
Tags, summaries and types for every memory, with relative dates like "next Friday" turned into real dates.
Connections between memories: related, elaborates, supersedes, duplicate.
Corrections win. When a later note corrects an earlier one, the old one is marked superseded, ranks lower in search, and the current version is shown next to it. If an agent later saves the old fact again, it is flagged as disputed and the correction is shown first.
Overviews. When enough notes pile up about one topic, Dreaming writes a single note of the current picture: what it is, what was decided, where it stands. It's linked back to its sources and rewritten when new notes join.
A short digest of what changed.
115 notes, 40 seconds one pass over a real personal memory
Under $1 for that first pass; pennies a day after
Off by default it only runs if you add a model API key
Your data, your keys
Memories live in your own Supabase database. There is no Memex server run by anyone else.
Costs are pennies a month: a small embeddings charge per memory, plus Dreaming if you turn it on.
Anything that looks like a secret (keys, tokens, card or ID numbers) is flagged, never sent to a model, and hidden from search and sync.
Agents are told to treat memories as evidence, never as instructions.
One thing to know: memories are sent to an embeddings provider so they can be searched by meaning, and to a model provider if you enable Dreaming. You choose the providers, and the repo says exactly what is sent.
Works with
Tested with Claude and Muse, reading and writing the same memory. Any agent that supports MCP over HTTP should work: Codex, Cursor, VS Code and others connect with a URL and a key.
Memex is building on the excellent Open Brain project by Nate B. Jones, and on an earlier write-up, Liberating memory . Source and setup instructions are on GitHub .

## 关联链接

- https://github.com/predsymod/memex

## 导航

- 项目页：[[10-项目/predsymod.github.io_b5ca70af]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
