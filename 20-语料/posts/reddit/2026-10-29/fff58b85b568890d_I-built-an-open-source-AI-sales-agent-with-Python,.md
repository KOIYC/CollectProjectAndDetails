---
type: "corpus"
item_id: "fff58b85b568890d"
title: "I built an open-source AI sales agent with Python, Claude Code, and SQLite"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/microsaas/comments/1x9rp6n/i_built_an_opensource_ai_sales_agent_with_python/"
project_url: "https://github.com/GortexAI/franco"
author: "KeyConsideration9777"
published_at: "2026-10-19T16:53:23+08:00"
captured_at: "2026-10-29T20:43:53+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-29"
pub_day: "2026-10-19"
tags:
  - 语料
  - reddit
  - r/microsaas
metrics: {"score": 4, "comments": 3, "upvote_ratio": 1}
comments_count: 3
comments_total: 3
discovered_via: "reddit:14d+settle10"
---

# I built an open-source AI sales agent with Python, Claude Code, and SQLite

> [!info] 一句话导读
> I've been experimenting with automating parts of the B2B sales outreach workflow, especially prospect research, email personalization, follow-ups, and reply man…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/microsaas/comments/1x9rp6n/i_built_an_opensource_ai_sales_agent_with_python/>
> 指标：得分=4 · 评论=3 · 赞踩比=1
> 作者：KeyConsideration9777　|　发布：2026-10-19T16:53:23+08:00
> 项目链接：<https://github.com/GortexAI/franco>
> 采集：2026-10-29T20:43:53+08:00　|　id：`fff58b85b568890d`

## 正文

I've been experimenting with automating parts of the B2B sales outreach workflow, especially prospect research, email personalization, follow-ups, and reply management.

One thing I noticed is that most sales automation workflows involve multiple tools, integrations, and databases. I wanted to see how much of that could run locally using Python and an AI coding agent.

So I started building **Franco**, an open-source AI sales agent.

The basic workflow:

1. Import prospects from a CSV file or discover potential accounts.
2. Research companies and collect source-backed information.
3. Draft personalized cold emails using Claude Code or Codex.
4. Review and approve outreach sequences before sending.
5. Schedule follow-ups and process email replies.
6. Track everything through a local dashboard.

The application uses SQLite for local data storage and supports different outreach modes, including preapproved email templates that don't require AI-generated copy.

One design decision was keeping human approval in the workflow by default. I didn't want an autonomous agent sending emails without a way to review them first.

It's built with Python, released under the MIT license, and can run on your own machine.

I'm still exploring some of the trade-offs around reliable prospect research, email deliverability, and automation safeguards.

**I'm curious how other developers approach this:**

* Would you trust an AI agent to handle cold email replies automatically?
* Is local-first storage important for this kind of tool?
* What parts of B2B outreach should never be fully automated?

Would be interested in hearing from anyone building open-source sales tools or experimenting with AI agents for business workflows.

GitHub: [https://github.com/GortexAI/franco](https://github.com/GortexAI/franco)

## 评论（3/3）

> **Tellenze**（2 分） · 2026-10-19T17:35:49+08:00　
> Automatic opt-outs make sense to me. Price negotiations or promises about when a feature will ship would stay with a person, even if the reply looks routine. That's the boundary I'd keep when turning on autopilot.

---

> **ReinatouGushani67**（1 分） · 2026-10-20T02:12:12+08:00　
> do you handle the case where someone replies asking about pricing but frames it as a casual question? feels like that blurs the boundary pretty fast

---

> **Tellenze**（1 分） · 2026-10-20T02:24:14+08:00　
> I meant changing the price, rather than explaining it. A casual question could get the current approved price and what's included. A discount or custom deal would still go to a person, however casually it's asked.

## 导航

- 项目页：[[10-项目/github.com_3633a3de]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
