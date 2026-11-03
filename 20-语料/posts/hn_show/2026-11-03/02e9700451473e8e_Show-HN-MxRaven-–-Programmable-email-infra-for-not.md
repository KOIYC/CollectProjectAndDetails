---
type: "corpus"
item_id: "02e9700451473e8e"
title: "Show HN: MxRaven – Programmable email infra for nothing in particular"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50338055"
project_url: "https://sandbox.mxraven.com/"
author: "ku5h"
published_at: "2026-11-02T15:22:49Z"
captured_at: "2026-11-03T09:40:36+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-03"
pub_day: "2026-11-02"
tags:
  - 语料
  - hn_show
  - author_ku5h
  - story_50338055
  - show_hn
metrics: {"points": 3, "comments": 2, "engagement_velocity": 3}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: MxRaven – Programmable email infra for nothing in particular

> [!info] 一句话导读
> Hi HN, I am Kush, a student founder from India building mxRaven (https://mxraven.com). We recently made it available for public use, you can read my post about …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50338055>
> 指标：点赞=3 · 评论=2 · engagement_velocity=3
> 作者：ku5h　|　发布：2026-11-02T15:22:49Z
> 项目链接：<https://sandbox.mxraven.com/>
> 采集：2026-11-03T09:40:36+08:00　|　id：`02e9700451473e8e`

## 正文

Hi HN, I am Kush, a student founder from India building mxRaven (https://mxraven.com). We recently made it available for public use, you can read my post about our launch here: https://mxraven.com/blog/launching-mxravenmxRaven is a programmable email delivery platform for not any one particular thing, but rather a flexible glue which can be used to build anything that requires receiving or sending emails in some form, be it agent mailboxes, personal mailboxes, transactional email, marketing campaigns etc. Think of it as a sort of WAF + Application Layer Router but for the SMTP world with ergonomic SDKs for keeping the developers in the driver's seat.For this public demo (https://sandbox.mxraven.com/), I vibecoded a sandbox that (tries) to preview as many mxRaven features as possible publicly without possibility of abuse. You can try to send or receive emails from and to your designated sandbox addresses and play with some basic subset of programmable rules (https://mxraven.com/docs/concepts/routing-and-actions/introd...)You can read the details about mxRaven from the docs https://mxraven.com/docs/concepts/start-here/why-mxraven/ and check out our first-party SDKs we have so far:https://github.com/synqronlabs/mxraven-js
https://github.com/synqronlabs/mxraven-go
https://github.com/synqronlabs/mxraven-py
https://github.com/synqronlabs/mxraven-javaP.S. Unlike some of our competition we do not use relays like AWS SES. In fact mxRaven was born from the open source raven library (https://github.com/synqronlabs/raven) a high performance comprehensive ESMTP toolkit I wrote in Go. We ARE the email relay, and even the core transport and email auth library is first party and open source, something I am very proud of.

## 评论（2/2）

> **ku5h** · 2026-11-02T15:26:03.000Z　
> The code for this public sandbox is available at https://github.com/synqronlabs/mxraven-demo.One interesting thing which sets us apart is used for the CLI: a durable NATS JetStream consumer over websockets for clients to fetch all events (delivery attempts, side effects from rules and their actions etc). I built perch https://github.com/synqronlabs/perch, a tiny, single-binary mailbox server backed by mxRaven which can run behind CGNATs and firewalls on consumer devices effortlessly using this.If you wanna check out what the mxRaven resources the sandbox uses (the listeners for instance) on the dashboard, use the credentials:
> Username: guest
> Password: c53A!@3qaMzMin the workspace 'kush' on https://app.mxraven.com/login in the 'Open Workspace' option.

---

> **shivzee** · 2026-11-02T15:39:25.000Z　
> Hi, Shivam here. I am Kush's friend and cofounder. I primarily worked on the java and JS SDKs and the mxRaven public docs, I'll be here to clarify doubts or feedback.

## 关联链接

- https://github.com/synqronlabs/mxraven-go
- https://github.com/synqronlabs/mxraven-javaP.S.
- https://github.com/synqronlabs/mxraven-js
- https://github.com/synqronlabs/mxraven-py
- https://github.com/synqronlabs/raven
- https://mxraven.com
- https://mxraven.com/blog/launching-mxravenmxRaven
- https://mxraven.com/docs/concepts/routing-and-actions/introd...
- https://mxraven.com/docs/concepts/start-here/why-mxraven/

## 导航

- 项目页：[[10-项目/sandbox.mxraven.com_74fefcc8]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
