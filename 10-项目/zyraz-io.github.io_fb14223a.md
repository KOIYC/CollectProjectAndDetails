---
type: "project"
title: "Show HN: Ekbatan – Java persistence framework for event-driven systems"
project_url: "https://zyraz-io.github.io/ekbatan"
first_seen: "2026-09-21T02:53:10+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_unikzforce
  - story_48731373
  - show_hn
lang: "en"
---

# Show HN: Ekbatan – Java persistence framework for event-driven systems

> [!info] 一句话导读
> Ekbatan — Event-driven Java Persistence Framework

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://zyraz-io.github.io/ekbatan>
> 首次收录：2026-09-21T02:53:10+08:00
> 来源渠道：HN Show HN
> 标签：author_unikzforce, story_48731373, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:29:55+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/db097ada252d1a33_Show-HN-Ekbatan-–-Java-persistence-framework-for-e]] |
| 2026-09-21T02:53:10+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/db097ada252d1a33_Show-HN-Ekbatan-–-Java-persistence-framework-for-e]] |

## 摘要正文

Ekbatan — Event-driven Java Persistence Framework  # Ekbatan event-driven java persistence framework.  v1.0.0-RC1 · Apache 2.0 · Java 25+  Ekbatan is a Java persistence framework for event-driven systems. One database transaction commits your data and the domain events; the persisted events can then be drained from the events outbox table to Kafka or any event broker.  A replacement for Hibernate, Spring Data, or hand-rolled JDBC. Drops into Spring Boot, Quarkus, or Micronaut — or plain java.  ## Two writes. Two systems. One silent drift.  Your service inserts a row into the database, then publishes an event to Kafka. Two independent operations across two systems. If the second fails — Kafka outage, network blip, service crash — the row is committed but the event is lost. Your database and your event stream silently disagree.  ### Two writes  ✗ broken  app db State saved kafka Publish failed consumer No events  Crash between writes ⇒ DB and Kafka disagree.  The solution is a known pattern: the Transactional Outbox. Write the row AND the event into the same database transaction — both commit or both roll back. A separate process (a CDC tool like Debezium, a background job, or simila…
