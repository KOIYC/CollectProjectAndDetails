---
type: "project"
title: "Show HN: Similarity, a spiritual successor to 2000s-era OkCupid"
project_url: "https://similarity.com/"
first_seen: "2026-11-01T09:38:09+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_stickfigure
  - story_50317309
  - show_hn
lang: "en"
---

# Show HN: Similarity, a spiritual successor to 2000s-era OkCupid

> [!info] 一句话导读
> This is a side project I've been working on on-and-off (mostly off) since the 1990s. I guess you would call it an experimental "dating site" though it's designe…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://similarity.com/>
> 首次收录：2026-11-01T09:38:09+08:00
> 来源渠道：HN Show HN
> 标签：author_stickfigure, story_50317309, show_hn
> 最新指标：点赞=4 · 评论=2 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-28T09:39:16+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-10-28/5af9a7c8e15bb942_Show-HN-Similarity,-a-spiritual-successor-to-2000s]] |
| 2026-11-01T09:38:09+08:00 | HN Show HN | 点赞=4 · 评论=2 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-11-01/62de93008688680d_Show-HN-Similarity,-a-spiritual-successor-to-2000s]] |

## 摘要正文

This is a side project I've been working on on-and-off (mostly off) since the 1990s. I guess you would call it an experimental "dating site" though it's designed to be fun/interesting to people who aren't single (like me).You don't need to sign in to see how it works, so try it out. There is no swiping.The original inspiration was a 90s-era website called moviecritic.com that let you rate movies and get movie suggestions via collaborative filtering. I thought "hey, what about just matching me to the _people_ with the same taste instead?" And why just movies?The closest thing to this was 2000s-era OkCupid, before it was Tinderized. I want to capture its appeal, while making something novel.Similarity is not vibe coded, though I lean pretty heavily on codex (mostly the $20/mo plan - not a lot of tokens burnt here). The stack is java, guice/gwizard, elastic beanstalk, postgres (neon), react, jotai, and few cloudflare doodads. The match engine is a custom in-memory structure; getting the LLM to load test and optimize it was really a wow moment. Everything is PaaS and designed to scale by itself, cheaply, hands-off.I'm working on some ideas to help with the chicken/egg problem but for n…
