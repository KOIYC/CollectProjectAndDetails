---
type: "project"
title: "Show HN: CUA-S1 – A System One Model for Computer Use"
project_url: "https://github.com/trycua/cua"
first_seen: "2026-09-20T09:48:16+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_frabonacci
  - story_49767564
  - show_hn
  - front_page
lang: "en"
---

# Show HN: CUA-S1 – A System One Model for Computer Use

> [!info] 一句话导读
> Hello HN! We're Dillon and Francesco from Cua.We were wondering how many computer use tasks actually need a full general purpose LLM (e.g. gpt-6-astra, claude-o…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/trycua/cua>
> 首次收录：2026-09-20T09:48:16+08:00
> 来源渠道：HN Show HN
> 标签：author_frabonacci, story_49767564, show_hn, front_page
> 最新指标：点赞=63 · 评论=7 · engagement_velocity=63

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T02:35:34+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/dbb76c14769be1bd_Show-HN-CUA-S1-–-A-System-One-Model-for-Computer-U]] |
| 2026-09-20T02:46:51+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/dbb76c14769be1bd_Show-HN-CUA-S1-–-A-System-One-Model-for-Computer-U]] |
| 2026-09-20T02:55:58+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/dbb76c14769be1bd_Show-HN-CUA-S1-–-A-System-One-Model-for-Computer-U]] |
| 2026-09-20T03:04:29+08:00 | HN Show HN | 点赞=7 · 评论=0 · engagement_velocity=7 | [[20-语料/posts/hn_show/2026-09-20/dbb76c14769be1bd_Show-HN-CUA-S1-–-A-System-One-Model-for-Computer-U]] |
| 2026-09-20T03:16:53+08:00 | HN Show HN | 点赞=11 · 评论=0 · engagement_velocity=11 | [[20-语料/posts/hn_show/2026-09-20/dbb76c14769be1bd_Show-HN-CUA-S1-–-A-System-One-Model-for-Computer-U]] |
| 2026-09-20T03:29:12+08:00 | HN Show HN | 点赞=12 · 评论=0 · engagement_velocity=12 | [[20-语料/posts/hn_show/2026-09-20/dbb76c14769be1bd_Show-HN-CUA-S1-–-A-System-One-Model-for-Computer-U]] |
| 2026-09-20T03:38:50+08:00 | HN Show HN | 点赞=14 · 评论=1 · engagement_velocity=14 | [[20-语料/posts/hn_show/2026-09-20/dbb76c14769be1bd_Show-HN-CUA-S1-–-A-System-One-Model-for-Computer-U]] |
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=63 · 评论=7 · engagement_velocity=63 | [[20-语料/posts/hn_show/2026-09-20/dbb76c14769be1bd_Show-HN-CUA-S1-–-A-System-One-Model-for-Computer-U]] |
| 2026-09-20T09:48:16+08:00 | HN Show HN | 点赞=63 · 评论=7 · engagement_velocity=63 | [[20-语料/posts/hn_show/2026-09-20/dbb76c14769be1bd_Show-HN-CUA-S1-–-A-System-One-Model-for-Computer-U]] |

## 摘要正文

Hello HN! We're Dillon and Francesco from Cua.We were wondering how many computer use tasks actually need a full general purpose LLM (e.g. gpt-6-astra, claude-opus-5 etc.) to think through all their decisions and steps. Some tasks require thinking about a plan, exploring different paths, recovering from failure. Other tasks are a question of making local decisions, like this value should go in this box, or should I check this box, or this element should be ignored.We wondered how far we could go with a small model trained to only make these kinds of decisions.Our inspiration was Typesafe's Jev and its System One Model framing. This is a nod to the dichotomy between thinking quickly, automatically, and intuitively (system 1) vs. thinking slowly, analytically (system 2), as described by Daniel Kahneman.The interesting question for us was: what happens if you give a model an interface of current context, and a set of possible choices, and you ask it to return a probability for each choice? This kind of model does not generate output token by token like most LLMs do, but rather scores the options you give it, which you can check, trust, and use to drive your app's behavior.CUA-S1 is ou…
