---
type: "corpus"
item_id: "98ae7d592c7c9ce3"
title: "Show HN: Widen – Open-source Mac Postgres GUI with local or cloud text-to-SQL"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49117989"
project_url: "https://widen.dev/"
author: "thedreammachine"
published_at: "2026-07-31T01:21:42Z"
captured_at: "2026-09-21T03:11:11+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-31"
tags:
  - 语料
  - hn_show
  - author_thedreammachine
  - story_49117989
  - show_hn
metrics: {"points": 7, "comments": 0, "engagement_velocity": 7}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: Widen – Open-source Mac Postgres GUI with local or cloud text-to-SQL

> [!info] 一句话导读
> Skip to content GitHub

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49117989>
> 指标：点赞=7 · 评论=0 · engagement_velocity=7
> 作者：thedreammachine　|　发布：2026-07-31T01:21:42Z
> 项目链接：<https://widen.dev/>
> 采集：2026-09-21T03:11:11+08:00　|　id：`98ae7d592c7c9ce3`

## 正文

Skip to content GitHub
Postgres GUI for your Mac with local or cloud text-to-SQL
Widen is a free, open-source, native macOS Postgres GUI. Its agents search
 your schema, draft SQL, and verify it against PostgreSQL before it reaches
 your editor.
Swift · Text-to-SQL agents · On-device or cloud · No account
Download for macOS 15MB GitHub
On-device AI on macOS 26+ only
Text-to-SQL that verifies itself
 Search. Draft. Verify. Run.
Instead of dumping your whole schema into one prompt, Widen's agents
 search your schema, call only the tables they need, draft SQL, and
 verify it against PostgreSQL before it reaches your editor. If it
 doesn't parse, they get one repair — then stop.
Verified before run
 Review-before-run
 On-device or cloud
 No account
 MIT
You Which users have spent the most?
generated SQL · editable
 verified · Postgres
 SELECT u.name, SUM (o.total_cents) / 100.0 AS spent
 FROM users u
 JOIN orders o ON o.user_id = u.id
 GROUP BY u.name
 ORDER BY spent DESC
 LIMIT 5
query complete · 4 rows · 11 ms
name spent
 Ada Lovelace $482.50
 Grace Hopper $391.00
 Alan Turing $274.20
 Katherine Johnson $168.75
⌘↵ Run
 ⌘N New session
 ⌘R Refresh schema
Ask in plain English
 Type a question. Widen's agents search your schema for the right tables and columns, draft SQL with an explanation and confidence, and verify it against Postgres before showing you.
 Agents discover the schema themselves — no giant context dump
 SQL is verified against PostgreSQL before it reaches your editor
 One repair if it doesn't parse, then it stops
 Or write raw SQL yourself when you don't need the agents
 Persistent sessions that survive restarts
Privacy
 your call
 On-device model · macOS 26 on
 Cloud · your OpenRouter key
 Results stay on your Mac
 No backend · No account · No analytics
On your Mac, or in the cloud
 Run the model that ships on your Mac for fully offline SQL, or bring your own OpenRouter key to use any frontier model — open or closed. Your query results never leave your Mac either way.
 On-device mode on macOS 26 — no network except your Postgres
 Cloud mode with your own OpenRouter API key, any model
 Cloud-only on older macOS
 Passwords and API keys live in the macOS Keychain
 No backend, no accounts, no analytics
data change query review then run
 UPDATE public.orders
 SET status = 'archived'
 WHERE id = 42 ;
Data changes run today. Table-structure editing comes later.
A focused Postgres workbench
 Connect your Postgres databases, browse schemas, keep sessions, and run SELECT, INSERT, UPDATE and DELETE from one native Mac app.
 One native app for local and remote Postgres databases
 Ask for SQL or write it yourself, review the statement, then choose whether to run it
 Single-statement validation before execution
 Timeouts, row caps and confirmations for dangerous writes
 Schema-design tools like creating or altering tables come next
FAQ
 Common questions
Is it really free? Yes. Widen is free and MIT-licensed. The only thing that can cost money is the cloud model you bring yourself via your own OpenRouter API key.
Does my data leave my Mac? On-device mode keeps everything on your Mac — the only network connection is the Postgres you configure. Cloud mode sends your question and the relevant schema (never your query results) to the model provider you pick via your own OpenRouter key. Your results always stay on your Mac.
How do the SQL agents work? Instead of dumping your whole schema into one prompt, Widen's agents search your schema for the relevant tables, inspect the columns and join paths they need, then draft SQL. The draft is verified against PostgreSQL — parsed and bound in a read-only transaction — before it reaches your editor. If it fails, the agent gets one repair attempt, then stops.
Can the AI modify my database? Yes. It runs SELECT, INSERT, UPDATE and DELETE, whether the model wrote the SQL or you did. It’s meant for developers managing their own Postgres databases, so review generated SQL before running it. Creating or altering tables isn’t implemented yet.
Do I need Apple Intelligence turned on? Only for on-device AI. Enable it in System Settings, Apple Intelligence & Siri, and the local model drafts SQL fully offline. Without it, Widen still works as a Postgres GUI for writing SQL by hand, and cloud mode works regardless.
What do I need to run it? For the full experience: a Mac on macOS 26 or later with Apple Silicon and Apple Intelligence enabled. For cloud-only mode: an older Mac works fine — you bring your own OpenRouter API key. Either way, you need a PostgreSQL server you can reach. Postgres.app on localhost works great.
Does it work on older macOS? Yes — in cloud mode. Bring your own OpenRouter API key and Widen routes your questions to any frontier model, open or closed. The on-device model (the one that ships with macOS 26) needs Apple Silicon and Apple Intelligence.
What are the current limitations? It's an early release. PostgreSQL only, no table-structure editor yet, results render as a plain table, no SQL syntax highlighting yet, and query results aren't kept across restarts. On-device mode is experimental and limited to SELECT queries over a few tables; complex requests fall back to cloud. Transcripts and SQL are saved, so rerun a query to repopulate its grid.
What about MySQL or SQLite? PostgreSQL only for now. It’s the focus of the MVP; other engines may come later.
How do I install it? Download the macOS app from the releases page, or build it from source with Xcode 26 (git clone, then make run). It’s open source, so you can read the source first.
Is the on-device model good enough? For simple, single-table queries, yes. Apple's on-device model has a small context window and still struggles with complex joins or large schemas, so Widen keeps on-device mode experimental and constrained to SELECT queries. For hard queries, use cloud mode with a frontier model — or just write the SQL yourself.
What's the cloud option? Cloud mode is the recommended default for anything beyond simple queries. Bring your own OpenRouter API key and use any frontier model — open or closed. On-device mode on macOS 26 is there when you want fully offline, private SQL generation. Everything keeps working as a plain Postgres GUI if you never turn either on.
Talk to your Postgres in plain English
A native Swift Mac app that's free, open source, and verifies every query against Postgres before it runs.
>_ git clone https://github.com/betocmn/widen && cd widen && make run
Download for macOS 15MB Star on GitHub
Free · MIT · On-device on macOS 26 · Cloud on any supported Mac
Talk to your Postgres databases with a team of SQL agents. Widen
 searches your schema, drafts SQL, and verifies it against PostgreSQL
 before it runs — on-device on macOS 26, or with your own cloud key.
Source Releases Build from source Privacy Security MIT license
Verified before run
 Review-before-run
 On-device or cloud
 No account
 MIT
 @betocmn

## 关联链接

- https://github.com/betocmn/widen

## 导航

- 项目页：[[10-项目/widen.dev_83536b29]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
