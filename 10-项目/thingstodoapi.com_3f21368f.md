---
type: "project"
title: "Show HN: Things to Do API"
project_url: "https://thingstodoapi.com/"
first_seen: "2026-10-17T13:35:15+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_invalidmonk
  - story_50126384
  - show_hn
lang: "en"
---

# Show HN: Things to Do API

> [!info] 一句话导读
> I built an api/mcp for local events: pop-ups, one-off events, concerts, etc. currently covering the SF bay area.I've been building a bunch of consumer apps late…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://thingstodoapi.com/>
> 首次收录：2026-10-17T13:35:15+08:00
> 来源渠道：HN Show HN
> 标签：author_invalidmonk, story_50126384, show_hn
> 最新指标：点赞=6 · 评论=2 · engagement_velocity=6

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-17T13:35:15+08:00 | HN Show HN | 点赞=6 · 评论=2 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-10-17/19485b413372e54f_Show-HN-Things-to-Do-API]] |

## 摘要正文

I built an api/mcp for local events: pop-ups, one-off events, concerts, etc. currently covering the SF bay area.I've been building a bunch of consumer apps lately around personalization and recommendation and have had a hard time finding this data in one spot. agents can find useful stuff through tool calls / web search, but slow.you can scrape on demand too, but i wanted a faster data set and couldn't find an existing provider for the mix of event types I was searching for.the methodology for it is to find influential accounts/posters/etc. and do a fan out across things that they co-post with.mcp: `claude mcp add --transport http thingstodo https://api.thingstodoapi.com/mcp`I'm considering adding other cities. If you're building something that needs local event data, would something like this be useful and where would you want coverage?
