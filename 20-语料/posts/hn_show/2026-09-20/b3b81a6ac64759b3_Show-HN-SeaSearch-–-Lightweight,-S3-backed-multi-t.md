---
type: "corpus"
item_id: "b3b81a6ac64759b3"
title: "Show HN: SeaSearch – Lightweight, S3-backed multi-tenant search engine"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49721546"
project_url: "https://github.com/seacloud-lab/seasearch"
author: "Daniel-Pan"
published_at: "2026-09-16T02:45:52Z"
captured_at: "2026-09-20T14:04:44+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_Daniel-Pan
  - story_49721546
  - show_hn
metrics: {"points": 2, "comments": 2, "engagement_velocity": 2}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:90d"
---

# Show HN: SeaSearch – Lightweight, S3-backed multi-tenant search engine

> [!info] 一句话导读
> seacloud-lab/seasearch

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49721546>
> 指标：点赞=2 · 评论=2 · engagement_velocity=2
> 作者：Daniel-Pan　|　发布：2026-09-16T02:45:52Z
> 项目链接：<https://github.com/seacloud-lab/seasearch>
> 采集：2026-09-20T14:04:44+08:00　|　id：`b3b81a6ac64759b3`

## 正文

# seacloud-lab/seasearch

SeaSearch is a multi-tenant search engine with full-text indexing and vector indexing. Elasticsearch-compatible and S3-backed.

- Stars: 28
- Forks: 2
- Watchers: 28
- Open issues: 4
- License: Apache License 2.0
- Homepage: https://seasearch-manual.seacloud-labs.ai
- Default branch: main
- Created: 2024-04-24T01:54:45Z

## Languages

- C
- C++
- Dockerfile
- Go
- Shell

## Top Contributors

- hengfeiyang (211 contributions)
- prabhatsharma (188 contributions)
- KaniuBillows (69 contributions)
- dependabot[bot] (32 contributions)
- rumtid (32 contributions)
- xiaojun207 (26 contributions)
- killing (8 contributions)
- snyk-bot (5 contributions)
- EpicStep (4 contributions)
- songzhibin97 (4 contributions)

---

## README

# SeaSearch — Lightweight, Go-based multi-tenant search engine

**SeaSearch** is a lightweight, Go-based multi-tenant search engine featuring Elasticsearch API compatibility and S3-backed storage—designed to support unlimited indexes without overhead.

In a multi-tenant environment, such as a SaaS application, this allows each tenant's data to be indexed independently. With traditional search engines such as Elasticsearch, when all tenants' data is stored in a single index, the index may eventually become too large and require manual sharding. With SeaSearch, each tenant can have its own index, making it easier to manage and scale large numbers of tenants.

## SeaSearch vs. Elasticsearch

* **Lightweight**: SeaSearch is implemented in Go and has a smaller runtime footprint than Elasticsearch, which is built on the JVM.
* **No Practical Limit on the Number of Indexes**: SeaSearch is designed to support a large number of indexes. This makes it possible to create a separate index for each tenant, project, or other logical unit in an application. Queries can then be restricted to the relevant index, reducing the amount of data that needs to be searched. With Elasticsearch, applications often store data from many tenants or projects in the same index, which can become less efficient as the data volume grows.
* **Elasticsearch API Compatibility**: SeaSearch provides an API compatible with Elasticsearch, making it easier to integrate with existing applications.
* **S3-Compatible Storage**: SeaSearch can use S3-compatible object storage as its storage backend.
* **Shared-Storage Cluster Architecture**: Elasticsearch clusters replicate data across nodes, which can make cluster management and scaling relatively complex. SeaSearch uses a shared-storage architecture in which cluster nodes share the same storage backend, typically S3-compatible object storage. This simplifies cluster management and makes it easier to provide high availability. Query performance can also be scaled horizontally by adding more query nodes.
* **Vector Search**: SeaSearch provides a lightweight vector search implementation with support for Flat, HNSW, and IVFPQ vector indexes.

## Architecture

SeaSearch uses a shared-storage architecture.

A SeaSearch cluster consists of the following types of nodes:

* **SeaSearch compute node**: Handles index read and write requests. All compute nodes share the same S3-compatible storage backend, where the index data is stored.
* **SeaSearch proxy (or gateway)**: Distributes client requests among SeaSearch compute nodes.
* **Etcd**: Stores cluster metadata, including index metadata and the data distribution map.
* **SeaSearch cluster manager**: Monitors the health of SeaSearch compute nodes and redistributes index ownership among the nodes when necessary.

In a single-node deployment, SeaSearch uses a local KV database (bbolt) to store index metadata and the local file system to store index data.

### Data Distribution and Failover

Because all compute nodes share the same storage backend, SeaSearch only needs to distribute **index ownership** among nodes rather than moving or replicating the actual index data.

* All indexes are grouped into a fixed number of partitions based on a hash of their names.
* The cluster manager maintains a map that determines which node currently owns each index partition. This map is stored in Etcd.
* The SeaSearch proxy routes requests for an index to the compute node that owns the corresponding partition.
* Whenever a compute node fails or a new node is added, the cluster manager recomputes the ownership map and transfers partition ownership between nodes as needed.

Because updating the cluster configuration does not require transferring large amounts of data, SeaSearch can efficiently manage a large number of indexes.

### Local Cache

When handling requests, compute nodes may need to retrieve index data from S3 storage, which can introduce additional latency. To reduce this latency, SeaSearch compute nodes cache index data on their local disks.

This caching strategy is feasible because index data is organized into immutable segments. Once created, an index segment can only be read or deleted; its contents are never modified.

To support queries against indexes that are larger than the available local disk space, compute nodes use a rotating cache. When a new segment needs to be cached and the cache has reached its size limit, older segments are evicted to make room.

With this design, clients typically experience higher latency only for the first request after an index segment has been evicted or when a node starts up. Once the cache is warmed up, subsequent requests can be served at speeds comparable to those of local storage.

In our experience, the warm-up latency can be further reduced by taking advantage of the high network bandwidth available in modern data centers. During the warm-up stage, multiple index segments can be retrieved from S3 in parallel, significantly accelerating index loading.

**Distributed Query Execution**: To further improve the ability to serve queries against very large indexes, SeaSearch can automatically distribute a search query across multiple compute nodes. Each node loads and searches a portion of the index data in parallel, and the results are then aggregated. This approach not only accelerates query execution but also reduces cache pressure on individual nodes, allowing SeaSearch to efficiently serve indexes that are significantly larger than the local disk capacity of a single node.

# Your writing · Writeably - Writeably

## 评论（2/2）

> **gnat** · 2026-09-16T02:52:24.000Z　
> URL?

---

> **Daniel-Pan** · 2026-09-16T02:53:07.000Z　
> https://github.com/seacloud-lab/seasearch

## 关联链接

- https://seasearch-manual.seacloud-labs.ai

## 导航

- 项目页：[[10-项目/github.com_968d5a1e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
