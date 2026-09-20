---
type: "corpus"
item_id: "2d46bc632a4715cc"
title: "Show HN: Overslash – an auth gateway for AI Agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48344584"
project_url: "https://overslash.com/"
author: "arturogoosnargh"
published_at: "2026-05-31T10:34:23Z"
captured_at: "2026-09-21T01:42:53+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-31"
tags:
  - 语料
  - hn_show
  - author_arturogoosnargh
  - story_48344584
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:144d"
---

# Show HN: Overslash – an auth gateway for AI Agents

> [!info] 一句话导读
> Show HN: Overslash – an auth gateway for AI Agents

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48344584>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：arturogoosnargh　|　发布：2026-05-31T10:34:23Z
> 项目链接：<https://overslash.com/>
> 采集：2026-09-21T01:42:53+08:00　|　id：`2d46bc632a4715cc`

## 正文

Show HN: Overslash – an auth gateway for AI Agents

## 评论（1/1）

> **arturogoosnargh** · 2026-05-31T10:34:55.000Z　
> Author here. Overslash is an authorization gateway for AI agents (or any programmatic user, really).Overslash can register as a service any HTTP API or MCP server, defined as an OpenAPI document with some small extensions. Once that's done you can share access to those services with agents or teammates. Agents start with no write permissions (and no read permissions either, if you choose). Every time an agent attempts an action, a set of permission keys based on the action and its fields is generated; if the agent is missing any, an approval request is created. The approver can inspect the request — which has human-readable descriptions for the action and fields, taken from the OpenAPI doc — and deny or approve, either just this time or for similar requests in the future (choosing coarser or finer permission keys to remember).Overslash itself can be used as an MCP server, via REST, via CLI, or via the dashboard (think of it as an authenticated, shareable, auditable Postman).It's a single Rust binary, persistence on Postgres. Self-hosting will always be free; cloud at https://app.overslash.com is free for individuals, cheap for teams.I wrote a longer post (with a video demo) on the origins of Overslash: https://www.angelmartin.name/2026/05/29/why-did-i-build-an-a...Repo: https://github.com/overfolder/overslashNote: had to use an old HN account since i dont have enough karma on my new one

## 导航

- 项目页：[[10-项目/overslash.com_6e4fbdc6]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
