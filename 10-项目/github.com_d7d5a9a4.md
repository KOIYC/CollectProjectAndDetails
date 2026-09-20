---
type: "project"
title: "Show HN: A self-hostable, distributed, S3-compatible object store on the BEAM"
project_url: "https://github.com/wizenink/aethers3"
first_seen: "2026-09-21T03:11:18+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_wizenink
  - story_49109579
  - show_hn
lang: "en"
---

# Show HN: A self-hostable, distributed, S3-compatible object store on the BEAM

> [!info] 一句话导读
> A self-hostable, distributed, S3-compatible object store that runs on the BEAM.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/wizenink/aethers3>
> 首次收录：2026-09-21T03:11:18+08:00
> 来源渠道：HN Show HN
> 标签：author_wizenink, story_49109579, show_hn
> 最新指标：点赞=2 · 评论=1 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:31:46+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/dd7b85009130abdf_Show-HN-A-self-hostable,-distributed,-S3-compatibl]] |
| 2026-09-21T02:56:10+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/dd7b85009130abdf_Show-HN-A-self-hostable,-distributed,-S3-compatibl]] |
| 2026-09-21T03:11:18+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/dd7b85009130abdf_Show-HN-A-self-hostable,-distributed,-S3-compatibl]] |

## 摘要正文

# wizenink/aethers3  A self-hostable, distributed, S3-compatible object store that runs on the BEAM.  - Stars: 47 - Forks: 1 - Watchers: 47 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-06-25T16:56:31Z  ## Languages  - CSS - Dockerfile - Elixir - JavaScript - Shell  ## Topics  - beam - cluster - distributed - elixir - s3 - s3-compatible  ## Top Contributors  - wizenink (58 contributions) - dependabot[bot] (1 contributions)  ---  ## README  # AetherS3  aether_s3 image aether_console image  A self-hostable, distributed, S3-compatible object store that runs on the BEAM.  AetherS3 stores objects across a cluster of nodes and speaks enough of the S3 HTTP API to be driven by standard S3 clients (bucket and object operations, range reads, multipart uploads, SigV4 auth). It is built as an Erlang/OTP application: nodes discover each other, replicate object data, and self-heal without an external coordinator.  This is a learning project. See Status and limitations before relying on it.  ## Requirements  - Elixir `~> 1.20` on Erlang/OTP 29 (for building from source / dev). A  `mise.toml` pins the toolchain. - Docker, to run a cluster the easy way.  ## Quick st…
