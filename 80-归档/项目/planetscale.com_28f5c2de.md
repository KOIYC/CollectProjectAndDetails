---
type: "project"
title: "Tin: full-text search for Postgres"
project_url: "https://planetscale.com/blog/introducing-tin"
first_seen: "2026-09-20T03:41:55+08:00"
sources:
  - hn_front
tags:
  - 项目
  - hn_front
  - author_ksec
  - story_49766611
  - front_page
lang: "en"
stale: true
---

# Tin: full-text search for Postgres

- **项目链接**：https://planetscale.com/blog/introducing-tin
- **首次收录**：2026-09-20T03:41:55+08:00
- **来源渠道**：HN 首页（非 Show HN）
- **标签**：author_ksec, story_49766611, front_page
- **最新指标**：点赞=134 · 评论=59 · engagement_velocity=134

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T03:07:32+08:00 | HN 首页（非 Show HN） | 点赞=122 · 评论=57 · engagement_velocity=122 | [[80-归档/posts/hn_front/2026-09-20/19b6d4e461e491a6_Tin-full-text-search-for-Postgres]] |
| 2026-09-20T03:21:04+08:00 | HN 首页（非 Show HN） | 点赞=127 · 评论=57 · engagement_velocity=127 | [[80-归档/posts/hn_front/2026-09-20/19b6d4e461e491a6_Tin-full-text-search-for-Postgres]] |
| 2026-09-20T03:32:45+08:00 | HN 首页（非 Show HN） | 点赞=129 · 评论=58 · engagement_velocity=129 | [[80-归档/posts/hn_front/2026-09-20/19b6d4e461e491a6_Tin-full-text-search-for-Postgres]] |
| 2026-09-20T03:41:55+08:00 | HN 首页（非 Show HN） | 点赞=134 · 评论=59 · engagement_velocity=134 | [[80-归档/posts/hn_front/2026-09-20/19b6d4e461e491a6_Tin-full-text-search-for-Postgres]] |

## 摘要正文

Neki, sharded Postgres, is now available. Get started  Blog| Engineering| PostgreSQL  Table of contents «Close »  #### Table of contents  - What TIN is for - TIN performance and benchmarking Workloads and corpus Test environment Index build time and size Mixed queries, top-10 ranked Conjunction and phrase queries, top-10 ranked Disjunction queries with concurrent writes When the index fits in memory Full results - Why TIN is fast Document identification 48-bit identifiers are crazy Work elision and vectorization Solving MVCC Segments and merging - Summary  PlanetScale, the fastest cloud Postgres, from $5/month.  Start now  Get the RSS feed  # Introducing TIN: full-text search for Postgres  Eric Ridge, Patrick Reynolds | September 16, 2026  One of the Postgres features our customers ask us for the most is full-text search. Today, we are excited to announce TIN: a fast, full-featured, reliable full-text search extension for Postgres. TIN stands for "Text INdex," and that is what it does.  TIN is available immediately as a GA release for all Postgres and Neki databases. Check it out:  ``` CREATE EXTENSION tin; CREATE INDEX an_index_name ON table_name USING tin(text_column_name); SELEC…
