---
type: "corpus"
item_id: "d3bcf58cd8375ddd"
title: "Show HN: DeepSearch – Search engine built on DeepSeek API"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50226186"
project_url: "https://deepsearch.ing/"
author: "try-working"
published_at: "2026-10-24T22:44:35Z"
captured_at: "2026-10-25T23:24:35+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-25"
pub_day: "2026-10-24"
tags:
  - 语料
  - hn_show
  - author_try-working
  - story_50226186
  - show_hn
metrics: {"points": 3, "comments": 2, "engagement_velocity": 3}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: DeepSearch – Search engine built on DeepSeek API

> [!info] 一句话导读
> DeepSeek launched their search API so I had to build a search engine on top of it.The search engine is very simple: add your DeepSeek API credentials or OAuth w…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50226186>
> 指标：点赞=3 · 评论=2 · engagement_velocity=3
> 作者：try-working　|　发布：2026-10-24T22:44:35Z
> 项目链接：<https://deepsearch.ing/>
> 采集：2026-10-25T23:24:35+08:00　|　id：`d3bcf58cd8375ddd`

## 正文

DeepSeek launched their search API so I had to build a search engine on top of it.The search engine is very simple: add your DeepSeek API credentials or OAuth with your DeepSeek account and you can search the web using their API and view results in a familiar web interface.Credentials are stored locally only.The search engine exposes the operators from the API:- Time- Language- Exact terms with "..." (like Google used to)- Forbidden terms with "-"- Site search and excluded sitesSearch results expose things like domain authority, rank etc.You can also switch to Ask and get a generated response for your question.Give it a try and see if this works as a Google replacement. So far the results seem passable but I've only done quick test queries.I also shared the source on GitHub so you could self-host or fork it into a local client.The most interesting thing here would be to build a local client with history/memory, so that your knowledge compounds.https://github.com/try-works/deepsearch

## 评论（2/2）

> **A_D_E_P_T** · 2026-10-24T22:49:25.000Z　
> I got an error when I tried to log-in with my Deepseek acct.Also, it would really be best if there were a "general use" API key already assigned, so that 1-2 searches could be run without logging-in and without a key. Most people aren't even going to try this thing, otherwise, despite the fact that it's a cool idea.

---

> **try-working** · 2026-10-24T23:23:18.000Z　
> that's a good point, one search just to get to try it out. I guess I could add that.What error did you see when you tried to log in? I'm not sure if it's displayed clearly enough, but the callback will always fail in the pop up and you'll have to copy the callback URL into the text field in the first modal, and let the worker acquire the credential.

## 关联链接

- https://github.com/try-works/deepsearch

## 导航

- 项目页：[[10-项目/deepsearch.ing_ff0ac760]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
