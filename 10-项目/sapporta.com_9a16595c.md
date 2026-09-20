---
type: "project"
title: "Show HN: Sapporta – build database applications for power users"
project_url: "https://sapporta.com/"
first_seen: "2026-09-21T03:11:31+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_jasim
  - story_49499123
  - show_hn
lang: "en"
---

# Show HN: Sapporta – build database applications for power users

> [!info] 一句话导读
> Skip to content Documentation Technical Overview GitHub Sapporta

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://sapporta.com/>
> 首次收录：2026-09-21T03:11:31+08:00
> 来源渠道：HN Show HN
> 标签：author_jasim, story_49499123, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:33:52+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/af1d06189dc3a0b8_Show-HN-Sapporta-–-build-database-applications-for]] |
| 2026-09-21T03:11:31+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/af1d06189dc3a0b8_Show-HN-Sapporta-–-build-database-applications-for]] |

## 摘要正文

Skip to content Documentation Technical Overview GitHub Sapporta  Build custom database software for power users Sapporta is a TypeScript + SQLite web framework for building database applications. Every table gets a spreadsheet-grade grid right away. Filtering, sorting, search, export, and full keyboard navigation. Default agentic. Use your coding agents to drive your application. For a Calorie Tracker, you could tell the agent: “breakfast: 2 eggs and a toast”, and it’ll find the right food entries, create them if needed, and log them accurately. Reports that drill down into the underlying records, shareable by URL. Secure software despite AI code generation with patterns and skills that enforce where user_id = {currentUser.id} and similar on all data access code. Get Started Try demo apps GitHub Demo Arrow keys for navigation. Space to expand quotes. Sample data grid Code: schema definition packages/api/schema/books.ts  export const booksTable = sqliteTable ( "books" , {  id: integer ( "id" ). primaryKey ({ autoIncrement: true }),  title: text ( "title" ). notNull (),  author: text ( "author" ). notNull (),  }); export const books = sapportaTable ({  drizzle: booksTable,  meta: { …
