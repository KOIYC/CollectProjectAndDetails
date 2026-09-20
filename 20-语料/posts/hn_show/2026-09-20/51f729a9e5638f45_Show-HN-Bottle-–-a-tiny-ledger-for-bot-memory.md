---
type: "corpus"
item_id: "51f729a9e5638f45"
title: "Show HN: Bottle – a tiny ledger for bot memory"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49739531"
project_url: "https://github.com/imron/bottle"
author: "imron"
published_at: "2026-09-17T12:01:33Z"
captured_at: "2026-09-20T09:36:53+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - hn_show
  - author_imron
  - story_49739531
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Bottle – a tiny ledger for bot memory

> [!info] 一句话导读
> A tiny ledger for autonomous bots

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49739531>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：imron　|　发布：2026-09-17T12:01:33Z
> 项目链接：<https://github.com/imron/bottle>
> 采集：2026-09-20T09:36:53+08:00　|　id：`51f729a9e5638f45`

## 正文

# imron/bottle

A tiny ledger for autonomous bots

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- Default branch: master
- Created: 2026-08-31T15:58:20Z

## Languages

- Rust
- Shell

---

## README

# Bottle

Bottle is a tiny ledger that gives autonomous bots the ability to log facts
against custom schemas and query those facts using a fixed set of commands.

It provides lightweight access to structured data.

## Why it exists

Bots are good at noticing facts but bad at keeping them. The usual method is
keeping notes in markdown files, but such notes lack consistent type information
and structure. You cannot sum these facts efficiently, you have no consistent
way to reason about them chronologically and two bots writing about the same
facts cannot safely share information without stepping on each other's toes.

Bottle corrects for these things.

Users specify a schema containing fields with simple types (text, number, enum).
Bots then log facts against those schemas and query those facts back in
meaningful ways.

## Why not markdown

Markdown is prose, bottle entries are structured data. Entries have types, ids,
dates, and declared numbers you can group and sum far more efficiently than
parsing and interpreting text.

## Why not SQL

SQL is amazing and powerful but the full expressive power of SQL causes bots to
overthink and overcomplicate solutions.

Rogue bots with full SQL access can accidentally corrupt your data store more
easily and "Sorry, that's on me" is poor consolation when a bot messes up.

Bottle is there to provide constraint. A small verb set over structured data.

## Why not Karpathy Wikis

Karpathy Wikis give your bots memory via a knowledge graph. They're great for
synthesising large amounts of data over time without requiring an LLM to
rediscover knowledge from scratch.

Bottle gives your bots memory of specific facts. It's great for recalling and
processing facts in a structured way.

Both are useful.

## Why not JSONL or CSV

An append-only file looks like a ledger until you need to link data, or ignore
data or you have a field with bad data, or you need to do something with the
data that the format makes difficult.

Bottle provides structure and validation for your data. It lets you link data,
group data and ignore data, and its output is tab separated fields making it
convenient to use in pipes with all the unix commands you know and love.

## Why not a specialized app

Your training app, bank app, calendar app and other apps all have unique
interfaces with different ways of accessing and storing data. This can make it
tricky and slow for bots to navigate - especially for repeated queries.

These apps can be the source of truth for a fact, and bottle then becomes the
convenient interface that bots use to query data from these sources in a
consistent and reliable manner.

One bot can speak to the specialized apps and ingest data into bottle. Other
bots just need to speak bottle.

# Install

Rust is required (rustup).

```
cargo build --release
```

The binary is `target/release/bottle`.

Compile with musl if you want a static binary that can be copied without needing
glibc:

```
rustup target add x86_64-unknown-linux-musl
cargo build --release --target x86_64-unknown-linux-musl
```

# Commands

```
$ bottle --help

Usage: bottle [OPTIONS] <COMMAND>

Commands:
  help      Print the long explanation of a command
  mcp       Run bottle as an MCP server on stdio
  schema    Declare and change types of entry
  log       Write one entry of a registered schema
  ls        List entries of a schema [alias: list]
  get       Print one entry by schema and id
  sum       Total a number field
  last      Print the most recent entry of a schema
  today     List entries for the current civil day
  amend     Change an existing entry in place
  ignore    Hide an entry from lists and totals
  unignore  Show an ignored entry in lists and totals again
  backup    Copy the ledger to a sqlite file

Options:
      --db <DB>    Path to the database file
      --no-header  Hide the TSV header
  -h, --help       Print help
```

Run `bottle help ` to see detailed help for each command.

# RhoPool

## 导航

- 项目页：[[10-项目/github.com_da07ad52]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
