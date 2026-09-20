---
type: "project"
title: "Show HN: Otzar – Local hybrid search over your own files"
project_url: "https://github.com/danielfleischer/otzar"
first_seen: "2026-09-21T03:11:14+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_yruthewaythatur
  - story_49113718
  - show_hn
lang: "en"
---

# Show HN: Otzar – Local hybrid search over your own files

> [!info] 一句话导读
> danielfleischer/otzar

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/danielfleischer/otzar>
> 首次收录：2026-09-21T03:11:14+08:00
> 来源渠道：HN Show HN
> 标签：author_yruthewaythatur, story_49113718, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:31:46+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/dc525ed2dc77d397_Show-HN-Otzar-–-Local-hybrid-search-over-your-own]] |
| 2026-09-21T03:11:14+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/dc525ed2dc77d397_Show-HN-Otzar-–-Local-hybrid-search-over-your-own]] |

## 摘要正文

# danielfleischer/otzar  Local hybrid search over your own files — dense vectors, BM25, and metadata filters in one query. The same binary is an MCP server, so agents can search your notes.  - Stars: 1 - Forks: 0 - Watchers: 1 - Open issues: 0 - License: GNU General Public License v3.0 - Default branch: main - Created: 2026-07-29T18:41:59Z  ## Languages  - Clojure - Go - Makefile  ## Topics  - clojure - embeddings - full-text-search - golang - lucene - model-context-protocol - ollama - personal-knowledge-management - semantic-search - vector-search  ## Top Contributors  - danielfleischer (81 contributions)  ---  ## README  # otzar  **Hybrid search over your own files** — dense vector similarity, BM25 keyword matching, and metadata filters in a single query, running entirely on your machine. A Clojure/Lucene server holds the index; a Go CLI is the UX; the same binary speaks **MCP**, so Claude Code and friends can search your notes as a tool.  *otzar* (אוֹצָר) is Hebrew for **treasure** — and, fittingly, *thesaurus*.  ```sh otzar index -r ~/notes otzar query "what did I decide about chunk overlap?" ```  ``` #  score  path                     snippet 1  0.055  ~/notes/rag.md:42-47    …
