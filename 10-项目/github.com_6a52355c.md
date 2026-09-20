---
type: "project"
title: "Show HN: Graph RAG in Postgres. New facts replace older facts"
project_url: "https://github.com/crajah/post-graph-rag"
first_seen: "2026-09-20T09:36:50+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_chandanrajah
  - story_49743385
  - show_hn
lang: "en"
---

# Show HN: Graph RAG in Postgres. New facts replace older facts

> [!info] 一句话导读
> crajah/post-graph-rag

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/crajah/post-graph-rag>
> 首次收录：2026-09-20T09:36:50+08:00
> 来源渠道：HN Show HN
> 标签：author_chandanrajah, story_49743385, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/7f94ae900670c580_Show-HN-Graph-RAG-in-Postgres.-New-facts-replace-o]] |
| 2026-09-20T09:36:50+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/7f94ae900670c580_Show-HN-Graph-RAG-in-Postgres.-New-facts-replace-o]] |

## 摘要正文

# crajah/post-graph-rag  High-Precision GraphRAG. Native to PostgreSQL.  - Stars: 2 - Forks: 0 - Watchers: 2 - Open issues: 0 - License: Apache License 2.0 - Homepage: https://crajah.github.io/post-graph-rag/ - Default branch: main - Created: 2026-07-25T10:09:49Z  ## Languages  - Makefile - Python - Shell  ## Top Contributors  - crajah (39 contributions)  ---  ## README  # post-graph-rag  PyPI version License: Apache 2.0 Python 3.9+  **Graph RAG with a memory of time — on the PostgreSQL you already run.**  `post-graph-rag` extracts entities and relations with an LLM, stores them as a property graph beside `pgvector` embeddings, and answers questions by fusing vector similarity, graph traversal and full-text search. What makes it different: **a later document can close an earlier fact**, so your model stops reporting that someone is both an ally and a rival.  No separate vector store. No graph engine to operate. One database, one consistency model, one backup — and transactions that span your graph *and* your application tables.  ## 📈 Benchmarks  On the full 500-question LongMemEval set — all six question types, nothing sampled — against the numbers Zep publish for Graphiti (arXiv:2…
