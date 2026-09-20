---
type: "corpus"
item_id: "37c10b883efe4e61"
title: "Show HN: Kaflow Search – A desktop tool for locally indexed Kafka message search"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49726447"
project_url: "https://kaflow-search.whsoul-tools.com/"
author: "whsoul"
published_at: "2026-09-16T13:08:47Z"
captured_at: "2026-09-20T09:37:03+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_whsoul
  - story_49726447
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Kaflow Search – A desktop tool for locally indexed Kafka message search

> [!info] 一句话导读
> Author: Kaflow Search

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49726447>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：whsoul　|　发布：2026-09-16T13:08:47Z
> 项目链接：<https://kaflow-search.whsoul-tools.com/>
> 采集：2026-09-20T09:37:03+08:00　|　id：`37c10b883efe4e61`

## 正文

Author: Kaflow Search

Kafka Message Search & Keyword Watch Tool | Kaflow Search

# Your Kafka messages. Search fast. Explore deeply. Keep watching.

 Index selected topics locally to find the messages you need quickly—even among millions. Search by keyword or detailed conditions, inspect message contents, and watch new messages arrive. No separate search server needed.

macOS 11+ · Windows 10+ — free, no account needed

App interface available in English, Korean, Japanese, and Simplified Chinese.

Your download has started.

 Your browser may say the file is not commonly downloaded and hold it — choose Keep to finish. On first run Windows adds “Windows protected your PC”; select More info → Run anyway. Both appear because this build carries no paid code-signing certificate yet, not because anything harmful was found. If the download will not finish, take the portable zip instead — browsers do not hold it, and there is no installer to run. Install guide

 When you open it, macOS says the developer cannot be verified. Allow it once in System Settings → Privacy & Security → Open Anyway and it runs normally from then on. This appears because this build is not notarized yet, not because anything harmful was found. Install guide

 No Kafka cluster at hand? Point the buttons above at the demo build — seven sample topics, nothing to connect to.

 Real product screen Selected topics indexed locally

Repeated searches over a four-million-message topic — each one answered from the local index.

 Selected-topic indexing Bounded local storage No extra infrastructure Your data stays local

Common starting points

## Helpful use cases.

 These are a few examples, not limits. Start with any identifier, field, keyword, or time range relevant to your system and investigate the Kafka messages that matter to you. Especially useful for independent developers and small teams that already keep operational data in Kafka, but do not need the cost and operational overhead of running a full ELK stack.

 01 Trace a stuck order 02 Trace web & app logs 03 Watch matching traffic 04 Investigate while Kafka is down 05 Your use case

### A customer paid. Why is the order still stuck?

Search the same order ID across order, payment, and processing topics—without writing a temporary consumer for each one.

1. 01 Find the order waiting for inventory
2. 02 Confirm that payment was authorized
3. 03 Locate the warehouse timeout

Real product demo · synthetic data · 28 sec

Search key`ORD-20260812-483921`

Finding Payment succeeded, but inventory reservation failed with WAREHOUSE_TIMEOUT.

### Search Kafka-stored logs without running ELK.

If Nginx and application logs are already collected in Kafka, index them locally, narrow the failure window, and follow a trace ID to the cause.

1. 01 Filter 100K Nginx records to checkout 502s
2. 02 Drill into the incident time window
3. 03 Follow the trace into application logs

Real product demo · synthetic data · 35 sec

Detailed search`P.status = "502*" AND P.path = "/api/checkout*" AND P.method = "POST*"`

Finding The checkout service exhausted its payment connection pool: 50 / 50 active, 184 pending.

### Spot payment failures as they arrive.

A payment operations specialist keeps a lightweight keyword Watch open while Kaflow Search keeps the topic in sync.

1. 01 Watch `payment_failed`
2. 02 Keep the payment topic auto-synced
3. 03 Open the new match and act on the cause

Real product demo · synthetic data · 27 sec

Watched keyword`payment_failed`

New match Order ORD-20260819-WATCH03 failed because the payment gateway timed out after 3000 ms.

### Keep investigating when Kafka is unavailable.

Use the last local index to inspect the messages collected before the outage and identify work that still needs manual intervention.

1. 01 Review the processing flow just before disconnect
2. 02 Continue searching the local index
3. 03 Find the final order needing manual review

Real product demo · synthetic data · 49 sec

Local index search`PENDING`

Finding Payment was authorized, but fulfillment never started. The order remains PENDING for manual review.

### Have a different question hidden in Kafka?

Bring the clues that make sense in your system. Kaflow Search works with the topics and fields you already have.

1. 01 Index the topic locally
2. 02 Search your identifiers, fields, or keywords
3. 03 Use lists, exploration, and timelines to narrow the evidence

Your starting point`an ID · a field · a keyword · a time range`

Your investigation The four scenarios are examples. Apply the same local search workflow to the Kafka data your team operates.

## A closer look at the workflow.

Scroll sideways to explore the actual interface.

01 · Local index Select topics and understand what is stored locally.

02 · Quick search Find matching messages without rescanning Kafka.

03 · Detailed queries Combine fields and boolean conditions to narrow the evidence.

04 · Watch & inspect See matching activity, then open the original message.

Kafka message search & keyword watch

## Search Kafka like a database.

### Keep an eye on the messages that matter.

 Keep selected topics synced and watch for saved keywords as new messages arrive. A lightweight way to spot the signals you care about during day-to-day operations—without adding a separate monitoring stack.

01 Select a topic ↓ 02 Keep it auto-synced ↓ 03 Watch a keyword

01

### Search, don't scan

Index only the topics you need and search millions of messages within a configurable local storage budget.

02

### Query real payloads

Combine AND, OR and NOT across keys, headers, nested JSON fields and time ranges.

03

### Decode anything

Work with JSON, Avro and Protobuf, including Confluent Schema Registry.

04

### Private by design

Messages and indexes stay on your machine. Kaflow Search is read-only.

Stop scrolling through Kafka messages one by one.

## Find the message that matters.

## 导航

- 项目页：[[10-项目/kaflow-search.whsoul-tools.com_01e2d118]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
