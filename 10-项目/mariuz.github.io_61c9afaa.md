---
type: "project"
title: "Show HN: FBSimCity – an explorable city that shows how Firebird works"
project_url: "https://mariuz.github.io/FBSimCity"
first_seen: "2026-09-21T03:11:20+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_mariuz
  - story_49109262
  - show_hn
lang: "en"
---

# Show HN: FBSimCity – an explorable city that shows how Firebird works

> [!info] 一句话导读
> an explorable city of Firebird internals

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://mariuz.github.io/FBSimCity>
> 首次收录：2026-09-21T03:11:20+08:00
> 来源渠道：HN Show HN
> 标签：author_mariuz, story_49109262, show_hn
> 最新指标：点赞=2 · 评论=1 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:31:46+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/13f7353cee484d40_Show-HN-FBSimCity-–-an-explorable-city-that-shows]] |
| 2026-09-21T02:56:14+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/13f7353cee484d40_Show-HN-FBSimCity-–-an-explorable-city-that-shows]] |
| 2026-09-21T03:11:20+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/13f7353cee484d40_Show-HN-FBSimCity-–-an-explorable-city-that-shows]] |

## 摘要正文

FBSimCity an explorable city of Firebird internals Guided tour  Trace  Anatomy  Decisions  Latency  Lifecycle  Machine room  ⏸ Pause  1×  ☀ Day  ?  About  GitHub Control room  − Scenario — pick a scenario —  Steady state  Cache thrash  Stuck OIT / version bloat  Lock contention  Rush hour  Sweep storm  Nightly gbak on a busy DB  nbackup with delta  Replica falling behind  Synchronous replica dies Query rate Write mix Page cache Sort memory Sweep interval Automatic sweep Long-running transaction  pins the OIT — garbage piles up Sweep now  Rush hour ×60 Replication Mode off  asynchronous  synchronous Replica healthy  slow to apply  unreachable Backup yard gbak  nbackup L0  L1 Lock / unlock  Restore chain × queries/s  cache hit  evictions (dirty )  Next  OAT  OIT  stale versions  lock waits  rollbacks  backup  delta  repl lag ( seg)  model clock  v0.9.0 Operator decisions × Where the time goes × drag to pan · scroll to zoom · click a building × ← Back  Next → Query trace × Auto play  Next step → ×  Keyboard & mouse Tab / Shift+Tab step through every subsystem in pipeline order Enter reopen the selected subsystem's panel drag pan the city scroll / pinch zoom click building story ←→↑↓ p…
