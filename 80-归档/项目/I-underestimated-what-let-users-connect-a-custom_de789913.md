---
type: "project"
title: "I underestimated what \"let users connect a custom domain\" actually takes. Sharing what I learned."
project_url: "https://www.reddit.com/r/indiehackers/comments/1tsu4f7/i_underestimated_what_let_users_connect_a_custom/"
first_seen: "2026-09-21T03:01:10+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/indiehackers
  - Sharing story/journey/experience
lang: "en"
stale: true
---

# I underestimated what "let users connect a custom domain" actually takes. Sharing what I learned.

> [!info] 一句话导读
> A friend asked me last week how hard it would be to add custom domains to his SaaS. I told him "two weeks." He's now two months in and not done.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://www.reddit.com/r/indiehackers/comments/1tsu4f7/i_underestimated_what_let_users_connect_a_custom/>
> 首次收录：2026-09-21T03:01:10+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/indiehackers, Sharing story/journey/experience
> 最新指标：得分=15 · 评论=47 · 赞踩比=0.800000011920929

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T03:01:10+08:00 | Reddit 独立开发版块 | 得分=15 · 评论=47 · 赞踩比=0.800000011920929 | [[20-语料/posts/reddit/2026-09-21/de789913faaa6297_I-underestimated-what-let-users-connect-a-custom-d]] |

## 摘要正文

A friend asked me last week how hard it would be to add custom domains to his SaaS. I told him "two weeks." He's now two months in and not done.  This is the post I wish I'd had three years ago when I made the same mistake at my own company.  What you actually have to build, in rough order of how soon it bites:  - **Multi-tenant TLS termination.** A cert per customer hostname. Let's Encrypt has rate limits (50 new certs per registered domain per week, 5 duplicate certs per week, 300 pending authz). Hit them once and customer onboarding goes dark for days. - **An ACME on-demand flow.** Issuing certs ahead of time means knowing every customer hostname in advance. Issuing on first SNI hit means an "ask the control plane if this hostname is legit" loop before LE issues — otherwise an attacker can DoS your rate limit. - **DNS validation.** Customers paste a hostname, you give them a CNAME, you poll until it resolves. Cloudflare caches your NXDOMAIN for 30 minutes. Public resolvers don't. You learn this at 2am. - **Renewal.** ACME certs are 90 days. You need a renewal worker, retries, backoff, and per-customer failure alerts (because renewals will fail). - **DNS drift.** Customer flips o…
