---
type: "project"
title: "Show HN: DeepSearch – Search engine built on DeepSeek API"
project_url: "https://deepsearch.ing/"
first_seen: "2026-10-25T23:24:35+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_try-working
  - story_50226186
  - show_hn
lang: "en"
---

# Show HN: DeepSearch – Search engine built on DeepSeek API

> [!info] 一句话导读
> DeepSeek launched their search API so I had to build a search engine on top of it.The search engine is very simple: add your DeepSeek API credentials or OAuth w…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://deepsearch.ing/>
> 首次收录：2026-10-25T23:24:35+08:00
> 来源渠道：HN Show HN
> 标签：author_try-working, story_50226186, show_hn
> 最新指标：点赞=3 · 评论=2 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-25T23:24:35+08:00 | HN Show HN | 点赞=3 · 评论=2 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-10-25/d3bcf58cd8375ddd_Show-HN-DeepSearch-–-Search-engine-built-on-DeepSe]] |

## 摘要正文

DeepSeek launched their search API so I had to build a search engine on top of it.The search engine is very simple: add your DeepSeek API credentials or OAuth with your DeepSeek account and you can search the web using their API and view results in a familiar web interface.Credentials are stored locally only.The search engine exposes the operators from the API:- Time- Language- Exact terms with "..." (like Google used to)- Forbidden terms with "-"- Site search and excluded sitesSearch results expose things like domain authority, rank etc.You can also switch to Ask and get a generated response for your question.Give it a try and see if this works as a Google replacement. So far the results seem passable but I've only done quick test queries.I also shared the source on GitHub so you could self-host or fork it into a local client.The most interesting thing here would be to build a local client with history/memory, so that your knowledge compounds.https://github.com/try-works/deepsearch
