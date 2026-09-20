---
type: "corpus"
item_id: "13f7353cee484d40"
title: "Show HN: FBSimCity – an explorable city that shows how Firebird works"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49109262"
project_url: "https://mariuz.github.io/FBSimCity"
author: "mariuz"
published_at: "2026-07-30T12:46:35Z"
captured_at: "2026-09-21T03:11:20+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-30"
tags:
  - 语料
  - hn_show
  - author_mariuz
  - story_49109262
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:83d"
---

# Show HN: FBSimCity – an explorable city that shows how Firebird works

> [!info] 一句话导读
> an explorable city of Firebird internals

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49109262>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：mariuz　|　发布：2026-07-30T12:46:35Z
> 项目链接：<https://mariuz.github.io/FBSimCity>
> 采集：2026-09-21T03:11:20+08:00　|　id：`13f7353cee484d40`

## 正文

FBSimCity
an explorable city of Firebird internals
Guided tour
 Trace
 Anatomy
 Decisions
 Latency
 Lifecycle
 Machine room
 ⏸ Pause
 1×
 ☀ Day
 ?
 About
 GitHub
Control room
 −
Scenario
— pick a scenario —
 Steady state
 Cache thrash
 Stuck OIT / version bloat
 Lock contention
 Rush hour
 Sweep storm
 Nightly gbak on a busy DB
 nbackup with delta
 Replica falling behind
 Synchronous replica dies
Query rate
Write mix
Page cache
Sort memory
Sweep interval
Automatic sweep
Long-running transaction
 pins the OIT — garbage piles up
Sweep now
 Rush hour ×60
Replication
Mode
off
 asynchronous
 synchronous
Replica
healthy
 slow to apply
 unreachable
Backup yard
gbak
 nbackup L0
 L1
Lock / unlock
 Restore chain
×
queries/s
 cache hit
 evictions (dirty )
 Next
 OAT
 OIT
 stale versions
 lock waits
 rollbacks
 backup
 delta
 repl lag ( seg)
 model clock
 v0.9.0
Operator decisions
×
Where the time goes
×
drag to pan · scroll to zoom · click a building
×
← Back
 Next →
Query trace
×
Auto play
 Next step →
×
 Keyboard & mouse
Tab / Shift+Tab step through every subsystem in pipeline order
Enter reopen the selected subsystem's panel
drag pan the city
scroll / pinch zoom
click building story
←→↑↓ pan
+ / − zoom in / out
space pause / resume the simulation
T guided tour
G trace one query, step by step
P data-page anatomy
D day / night theme
? this help
Esc close overlays
×
 Anatomy of a Firebird data page
Every table lives on data pages inside the single database
 file. Record descriptors grow from the top, record data grows from the
 bottom, and free space sits in between — and every record carries its
 transaction of origin plus a pointer to its previous version.
page header — type=DATA, flags, checksum/SCN, generation
dpg_sequence · dpg_relation (table id) · dpg_count (records)
descriptor[0] — offset, length
descriptor[1] — offset, length
descriptor[2] — offset, length
free space
 (descriptors grow ↓ · records grow ↑)
rpb: txn 1042 · back version → p118/l3 · flags · format#
 record 2 — RLE-compressed data
rpb: txn 1017 · back version → none · flags · format#
 record 1 — RLE-compressed data
rpb: txn 998 · back version → none · flags · format#
 record 0 — RLE-compressed data
The version chain
newest version
 txn 1042 — what new snapshots see
↓ back pointer (delta)
older version
 txn 981 — still visible to older snapshots
↓ back pointer (delta)
oldest version
 below the OIT — garbage, awaiting GC / sweep
A reader walks down the chain until it finds the
 version its transaction snapshot is allowed to see. Versions below
 the Oldest Interesting Transaction are demolished by cooperative GC
 or the sweep. Back versions are stored as deltas, usually on the
 same page — this is Firebird's multi-generational architecture, and
 why it needs no rollback segment and no WAL.

## 评论（1/1）

> **sifarhub_com** · 2026-07-30T13:29:19.000Z　
> its visually appealing and great. but can it be used in real-time like if I connect to any system which has firebird and than it will show all this running with my live data.

## 导航

- 项目页：[[10-项目/mariuz.github.io_61c9afaa]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
