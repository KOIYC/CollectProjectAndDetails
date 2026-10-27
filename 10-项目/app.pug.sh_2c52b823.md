---
type: "project"
title: "pug.sh: self-hosted web and product analytics with a single-binary Go backend"
project_url: "https://app.pug.sh/demo"
first_seen: "2026-10-27T23:48:08+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/selfhosted
  - Release (AI)
lang: "en"
---

# pug.sh: self-hosted web and product analytics with a single-binary Go backend

> [!info] 一句话导读
> Pug is an open-source product analytics that two of us have built over the past year (first commit Oct 2025, public since June). Self-hosting gets every feature…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://app.pug.sh/demo>
> 首次收录：2026-10-27T23:48:08+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/selfhosted, Release (AI)
> 最新指标：得分=28 · 评论=17 · 赞踩比=0.7413793103448276

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-27T23:48:08+08:00 | Reddit 独立开发版块 | 得分=28 · 评论=17 · 赞踩比=0.7413793103448276 | [[20-语料/posts/reddit/2026-10-27/e72d6003bf2035a4_pug.sh-self-hosted-web-and-product-analytics-with]] |

## 摘要正文

Pug is an open-source product analytics that two of us have built over the past year (first commit Oct 2025, public since June). Self-hosting gets every feature.  **The whole backend is a single Go binary.** `pug start` runs the API server and every worker in one process, and migrations and scheduled jobs are subcommands of the same binary. It needs Postgres, ClickHouse, NATS and Redis/Dragonfly next to it.  It does web analytics, trends, funnels, retention, user flows, user profiles and a live visitor map, with SDKs for web, Node, Flutter and Ruby. The web SDK is cookieless by default and visitor IPs are never stored.  * Code: [https://github.com/pug-sh/pug](https://github.com/pug-sh/pug) * Docs: [https://docs.pug.sh/self-hosting](https://docs.pug.sh/self-hosting) * Demo: [https://app.pug.sh/demo](https://app.pug.sh/demo)
