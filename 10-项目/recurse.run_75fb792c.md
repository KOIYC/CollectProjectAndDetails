---
type: "project"
title: "Show HN: Recurse – Develop and deploy specialist agents faster"
project_url: "https://recurse.run/"
first_seen: "2026-09-26T09:41:08+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_ozankabak
  - story_49850553
  - show_hn
lang: "en"
---

# Show HN: Recurse – Develop and deploy specialist agents faster

> [!info] 一句话导读
> Hi HN! We are looking to gather some feedback on our serverless agent harness. The admittedly not-so-specific use case is to accelerate agent development and de…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://recurse.run/>
> 首次收录：2026-09-26T09:41:08+08:00
> 来源渠道：HN Show HN
> 标签：author_ozankabak, story_49850553, show_hn
> 最新指标：点赞=5 · 评论=0 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-26T09:41:08+08:00 | HN Show HN | 点赞=5 · 评论=0 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-26/74ddcfa5e7307506_Show-HN-Recurse-–-Develop-and-deploy-specialist-ag]] |

## 摘要正文

Hi HN! We are looking to gather some feedback on our serverless agent harness. The admittedly not-so-specific use case is to accelerate agent development and deployment. After building several custom/special-purpose agents for a few customers, we built this to accelerate our workflow at first, and now we are trying to understand whether it could be useful to others.Our driver use case was development of specialist agents with a request/response lifecycle. Think of agents that have a well established input/output contract where they are expected to produce high-quality output (artifacts, responses etc.). Especially when the problem is in some verifiable domain and the LLM can iteratively refine a result to a final value that satisfies constraints or optimizes some goal.The product is a coding agent skill + a serverless execution runtime with a harness that takes in a system prompt + Python functions as tools. The coding agent takes in the requirements from the user, and tries agent variants by executing prompt/tool variants it creates.It works best for cases where you can think of how you can evaluate a candidate agent - when you describe this information to your coding agent, it of…
