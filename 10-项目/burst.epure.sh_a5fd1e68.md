---
type: "project"
title: "Take the challenge and try to break my tool."
project_url: "https://burst.epure.sh/"
first_seen: "2026-10-16T09:36:29+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/SaaS
lang: "en"
---

# Take the challenge and try to break my tool.

> [!info] 一句话导读
> I work on Epure , a lightweight self-hosted error tracking for production apps, same Sentry SDK, change the DSN, two containers (Rust + Postgres).

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://burst.epure.sh/>
> 首次收录：2026-10-16T09:36:29+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/SaaS
> 最新指标：得分=5 · 评论=3 · 赞踩比=0.86

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-16T09:36:29+08:00 | Reddit 独立开发版块 | 得分=5 · 评论=3 · 赞踩比=0.86 | [[20-语料/posts/reddit/2026-10-16/3d6b340c482239eb_Take-the-challenge-and-try-to-break-my-tool]] |

## 摘要正文

Hi everyone.  I work on Epure , a lightweight self-hosted error tracking for production apps, same Sentry SDK, change the DSN, two containers (Rust + Postgres).  I want real floods, not synthetic load scripts, so I opened a public box:  [https://burst.epure.sh](https://burst.epure.sh)  One button sends errors from your browser for about 7 seconds. Or copy the DSN / curl and hit it from your own client. Goal is to kill the ingester container. The VM and the dashboard stay up.  Box is sized like a small VPS (2 GB RAM, 2 vCPU). There is a spike valve so duplicate spam does not instantly win , still curious how far it goes when a lot of people click at once.  Send what you can. Let's see what breaks first.
