---
type: "project"
title: "Building PaidCheck in public: what I learned catching \"paid but no access\" bugs in Stripe"
project_url: "https://paidcheck.app/report"
first_seen: "2026-11-08T12:52:11+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/buildinpublic
lang: "en"
---

# Building PaidCheck in public: what I learned catching "paid but no access" bugs in Stripe

> [!info] 一句话导读
> I'm building PaidCheck, a small solo project (link at the bottom is mine). It compares Stripe with who has access in your app.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://paidcheck.app/report>
> 首次收录：2026-11-08T12:52:11+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/buildinpublic
> 最新指标：得分=3 · 评论=11 · 赞踩比=1

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-08T12:52:11+08:00 | Reddit 独立开发版块 | 得分=3 · 评论=11 · 赞踩比=1 | [[20-语料/posts/reddit/2026-11-08/73b49fd67b44af49_Building-PaidCheck-in-public-what-I-learned-catchi]] |

## 摘要正文

I'm building PaidCheck, a small solo project (link at the bottom is mine). It compares Stripe with who has access in your app.  Lessons so far:  \- Stripe is the source of truth for who paid, so I read its subscription and invoice records directly and never trust the app's own state.  \- Duplicate subscriptions are harder to catch than they look. The same customer can be on a different price of the same product, or can appear twice under one email.  \- A read-only restricted key makes it far easier for a founder to try, so I wrote a step-by-step guide for creating one.  \- Traffic is tiny so far, so I'm learning distribution the slow way. I'm focusing on helpful guides for Stripe billing problems.  Question: what billing bug cost you the most that you only found when a customer complained?  [https://paidcheck.app/report](https://paidcheck.app/report)
