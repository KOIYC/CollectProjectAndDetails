---
type: "project"
title: "I built an open-source AI sales agent with Python, Claude Code, and SQLite"
project_url: "https://github.com/GortexAI/franco"
first_seen: "2026-10-29T20:43:53+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/microsaas
lang: "en"
---

# I built an open-source AI sales agent with Python, Claude Code, and SQLite

> [!info] 一句话导读
> I've been experimenting with automating parts of the B2B sales outreach workflow, especially prospect research, email personalization, follow-ups, and reply man…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/GortexAI/franco>
> 首次收录：2026-10-29T20:43:53+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/microsaas
> 最新指标：得分=4 · 评论=3 · 赞踩比=1

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-29T20:43:53+08:00 | Reddit 独立开发版块 | 得分=4 · 评论=3 · 赞踩比=1 | [[20-语料/posts/reddit/2026-10-29/fff58b85b568890d_I-built-an-open-source-AI-sales-agent-with-Python,]] |

## 摘要正文

I've been experimenting with automating parts of the B2B sales outreach workflow, especially prospect research, email personalization, follow-ups, and reply management.  One thing I noticed is that most sales automation workflows involve multiple tools, integrations, and databases. I wanted to see how much of that could run locally using Python and an AI coding agent.  So I started building **Franco**, an open-source AI sales agent.  The basic workflow:  1. Import prospects from a CSV file or discover potential accounts. 2. Research companies and collect source-backed information. 3. Draft personalized cold emails using Claude Code or Codex. 4. Review and approve outreach sequences before sending. 5. Schedule follow-ups and process email replies. 6. Track everything through a local dashboard.  The application uses SQLite for local data storage and supports different outreach modes, including preapproved email templates that don't require AI-generated copy.  One design decision was keeping human approval in the workflow by default. I didn't want an autonomous agent sending emails without a way to review them first.  It's built with Python, released under the MIT license, and can run…
