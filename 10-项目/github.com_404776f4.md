---
type: "project"
title: "Show HN: Distributed SQLite on Modal"
project_url: "https://github.com/modal-projects/sqlite-modal"
first_seen: "2026-09-25T00:12:57+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_botirk
  - story_49789058
  - show_hn
lang: "en"
---

# Show HN: Distributed SQLite on Modal

> [!info] 一句话导读
> modal-projects/sqlite-modal

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/modal-projects/sqlite-modal>
> 首次收录：2026-09-25T00:12:57+08:00
> 来源渠道：HN Show HN
> 标签：author_botirk, story_49789058, show_hn
> 最新指标：点赞=4 · 评论=1 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-22T12:53:31+08:00 | HN Show HN | 点赞=3 · 评论=1 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-22/0a2f4fd54d5f55de_Show-HN-Distributed-SQLite-on-Modal]] |
| 2026-09-22T14:15:47+08:00 | HN Show HN | 点赞=4 · 评论=1 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-22/0a2f4fd54d5f55de_Show-HN-Distributed-SQLite-on-Modal]] |
| 2026-09-25T00:12:57+08:00 | HN Show HN | 点赞=4 · 评论=1 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-22/0a2f4fd54d5f55de_Show-HN-Distributed-SQLite-on-Modal]] |

## 摘要正文

# modal-projects/sqlite-modal  Distributed SQLite on Modal  - Stars: 8 - Forks: 0 - Watchers: 8 - Open issues: 0 - License: Apache License 2.0 - Default branch: main - Created: 2026-07-14T22:45:34Z  ## Languages  - Python  ## Top Contributors  - botirkhaltaev (4 contributions)  ---  ## README  # sqlite-modal  Distributed SQLite on Modal. Local SQL against a file; `push` / `pull` to a Server in your workspace. A Volume holds the remote file on exit. Sync uses the Turso SDK.  You create named DBs in your Modal workspace. This is not a managed multi-tenant service.  ```text local file  --push/pull-->  SyncServer                                 |                          exit → Volume /data ```  Local SQL stays on your machine. Sync is an explicit hop to a warm Server in eu-west.  Reads are about 0.01 ms and 121k/s. A local commit is about 0.09 ms.  Warm push / pull is about 158 ms / 79 ms. Conflicts are last-push-wins.  ## Install  Python >= 3.12 and a Modal account (`modal setup`).  ```bash uv add git+https://github.com/modal-projects/sqlite-modal.git ```  Deploy from a checkout (or editable install) so Image builds can `add_local_python_source("sqlite_modal")`. PyPI is not set up ye…
