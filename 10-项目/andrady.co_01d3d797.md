---
type: "project"
title: "My Stripe webhook trusted an older event over the customer's actual subscription state"
project_url: "https://andrady.co/"
first_seen: "2026-11-10T09:52:11+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/microsaas
lang: "en"
---

# My Stripe webhook trusted an older event over the customer's actual subscription state

> [!info] 一句话导读
> I've been building a multi-tenant SaaS starter using Next.js, Supabase and Stripe. Initially, most of my attention went into getting the features working: authe…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://andrady.co/>
> 首次收录：2026-11-10T09:52:11+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/microsaas
> 最新指标：得分=3 · 评论=20 · 赞踩比=1

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-10T09:52:11+08:00 | Reddit 独立开发版块 | 得分=3 · 评论=20 · 赞踩比=1 | [[20-语料/posts/reddit/2026-11-10/2889c4fd8057a258_My-Stripe-webhook-trusted-an-older-event-over-the]] |

## 摘要正文

I've been building a multi-tenant SaaS starter using Next.js, Supabase and Stripe. Initially, most of my attention went into getting the features working: authentication, organisations, roles, billing, API keys and usage limits. Everything appeared to work during normal usage. But when I started testing what would happen if someone deliberately tried to break things, I found four issues I hadn't caught during development. Here's what I found. 1. A privileged database function bypassed the protection I expected from RLS I had a SECURITY DEFINER function involved in a write operation. Because it executed with elevated privileges, I couldn't rely on the table's RLS policies alone. The function needed to independently validate the authenticated user's organisation membership. What I learned: Enabling RLS doesn't automatically protect every database operation. Privileged functions need their own authorization checks. 2. Stripe events arrived out of order My webhook handling wasn't adequately accounting for events arriving in an unexpected sequence. An older event could overwrite a newer subscription state. What I learned: Successfully processing a webhook doesn't guarantee that your bil…
