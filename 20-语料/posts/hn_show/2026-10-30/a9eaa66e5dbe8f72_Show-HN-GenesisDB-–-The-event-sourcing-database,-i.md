---
type: "corpus"
item_id: "a9eaa66e5dbe8f72"
title: "Show HN: GenesisDB – The event sourcing database, is now open source"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50294300"
project_url: "https://genesisdb.io/blog/posts/2026-10-24/genesisdb-2-is-open-source"
author: "patriceckhart"
published_at: "2026-10-29T19:11:26Z"
captured_at: "2026-10-30T09:46:09+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-30"
pub_day: "2026-10-29"
tags:
  - 语料
  - hn_show
  - author_patriceckhart
  - story_50294300
  - show_hn
metrics: {"points": 13, "comments": 0, "engagement_velocity": 13}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: GenesisDB – The event sourcing database, is now open source

> [!info] 一句话导读
> Docs Get started Blog

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50294300>
> 指标：点赞=13 · 评论=0 · engagement_velocity=13
> 作者：patriceckhart　|　发布：2026-10-29T19:11:26Z
> 项目链接：<https://genesisdb.io/blog/posts/2026-10-24/genesisdb-2-is-open-source>
> 采集：2026-10-30T09:46:09+08:00　|　id：`a9eaa66e5dbe8f72`

## 正文

Docs Get started Blog
 Support GitHub
All posts PE Patric Eckhart
 / October 24, 2026
 GenesisDB 2.0 is Open Source
 MIT licensed, drop-in compatible and free for everyone .
 Today GenesisDB 2.0 is released, and with it the complete source code. The server, every SDK and the VS Code extension are now on GitHub under the MIT license.
 What changes for you
 No more Community and Enterprise editions. There is one GenesisDB, and it has every feature.
 No license keys, no event limits, no subscriptions.
 Use it commercially, modify it, embed it, redistribute it.
Why open source
 A database is a long-term decision. You put your history into it, and with event sourcing that history is the system. Nobody should have to wonder whether the vendor behind their event store will still be there in ten years. With the code in the open, that question goes away: GenesisDB belongs to everyone who builds with it.
 What is in 2.0
 One static binary: written in Go, standard library only in the engines, no runtime dependencies.
 CloudEvents native: every event is a CloudEvents 1.0 record in a hierarchical subject tree.
 Preconditions: atomic batch commits guarded by isSubjectNew , isSubjectExisting and isQueryResultTrue .
 GDBQL: filters, ordering, grouping, aggregates, projections and subqueries.
 Live subscriptions: history plus new events over Server-Sent Events.
 Hash chain: every event is SHA-256 chained to its predecessor and the whole store can be audited with one request.
 GDPR erasure: personal data in reference payloads is erased with one request, the hash chain stays valid and an audit trail is written.
 Operations: logical backup and restore, index rebuild, Prometheus and OpenTelemetry metrics, separate read and write tokens, TLS.
 Embeddable: store.Open(dir) runs the database inside your own Go program.
 Upgrading from 1.x
 GenesisDB 2.0 is a drop-in replacement for 1.x. Start it on an existing data directory and it migrates it on the first start. Every 1.x backup restores. Every 1.x route still answers with the same status and body, so existing clients keep working while you move to the new SDKs at your own pace. Your existing 1.x installations also keep running as before.
 A backup is mandatory. As with every migration, a backup before upgrading is not a recommendation but a requirement. The migration is one-way, so stop 1.x and copy the complete data directory before GenesisDB 2 starts on it for the first time. Without that copy there is no way back to 1.x.
 The only required configuration change: GENESISDB_AUTH_TOKEN now needs at least 32 bytes. The upgrade guide has all the details.
 Try it
bash
 docker run --rm --name genesisdb \
 -e GENESISDB_AUTH_TOKEN="$( openssl rand -hex 32 )" \
 -p 127.0.0.1:8080:8080 \
 -v genesisdb-data:/app/data \
 genesisdb/genesisdb:latest
Then follow the quickstart . If something breaks, open an issue. If you want to make GenesisDB better, send a pull request.
 Thank you to everyone who used GenesisDB 1.x, reported problems and shaped what 2.0 became. This one is yours.
GenesisDB is open source
 MIT licensed event sourcing database. One binary, every feature.
 Get started GitHub
Read the documentation
The open source, GDPR-ready event sourcing database for developers who love event sourcing.
Product
 Get started
 Documentation
 Quickstart
 Upgrade from 1.x
 Changelog
 Roadmap
Open source
 GitHub
 SDKs
 Contributing
 Security
 License (MIT)
Community
 Blog
 FAQ
 Issues
 Support
© 2026 GenesisDB
 Privacy Policy Terms of Service

## 导航

- 项目页：[[10-项目/genesisdb.io_105ddeff]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
