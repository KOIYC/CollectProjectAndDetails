---
type: "corpus"
item_id: "de789913faaa6297"
title: "I underestimated what \"let users connect a custom domain\" actually takes. Sharing what I learned."
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/indiehackers/comments/1tsu4f7/i_underestimated_what_let_users_connect_a_custom/"
author: "Jonathan_Geiger"
published_at: "2026-05-31T20:33:26+08:00"
captured_at: "2026-09-21T01:27:53+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-05-31"
tags:
  - 语料
  - reddit
  - r/indiehackers
  - Sharing story/journey/experience
metrics: {"score": 15, "comments": 47, "upvote_ratio": 0.800000011920929}
comments_count: 0
comments_total: 0
discovered_via: "reddit:144d+settle3"
---

# I underestimated what "let users connect a custom domain" actually takes. Sharing what I learned.

> [!info] 一句话导读
> A friend asked me last week how hard it would be to add custom domains to his SaaS. I told him "two weeks." He's now two months in and not done.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/indiehackers/comments/1tsu4f7/i_underestimated_what_let_users_connect_a_custom/>
> 指标：得分=15 · 评论=47 · 赞踩比=0.800000011920929
> 作者：Jonathan_Geiger　|　发布：2026-05-31T20:33:26+08:00
> 项目链接：—
> 采集：2026-09-21T01:27:53+08:00　|　id：`de789913faaa6297`

## 正文

A friend asked me last week how hard it would be to add custom domains to his SaaS. I told him "two weeks." He's now two months in and not done.

This is the post I wish I'd had three years ago when I made the same mistake at my own company.

What you actually have to build, in rough order of how soon it bites:

- **Multi-tenant TLS termination.** A cert per customer hostname. Let's Encrypt has rate limits (50 new certs per registered domain per week, 5 duplicate certs per week, 300 pending authz). Hit them once and customer onboarding goes dark for days.
- **An ACME on-demand flow.** Issuing certs ahead of time means knowing every customer hostname in advance. Issuing on first SNI hit means an "ask the control plane if this hostname is legit" loop before LE issues — otherwise an attacker can DoS your rate limit.
- **DNS validation.** Customers paste a hostname, you give them a CNAME, you poll until it resolves. Cloudflare caches your NXDOMAIN for 30 minutes. Public resolvers don't. You learn this at 2am.
- **Renewal.** ACME certs are 90 days. You need a renewal worker, retries, backoff, and per-customer failure alerts (because renewals will fail).
- **DNS drift.** Customer flips on Cloudflare proxy 60 days after going live. Your renewal silently breaks. Cert expires. You don't notice until support pings about a 404.
- **Edge routing.** The customer's hostname hits your edge, you look up which tenant owns it, you reverse-proxy. Latency budget is now critical because every customer request pays this hop.
- **A monitoring fleet.** At 50 customers you can cron-check each one. At 5,000 you can't. You build sampling. You build alert ladders (30/7/1 day expiry). You build DNS drift detection. You add a Slack channel called #domains-on-fire.

Each of those is a small project. Together they're a quarter of engineering, then ongoing care forever.

I built this all myself the first time. Sold the SaaS, joined another company, watched the team there go through the same arc. Eventually built **Domainee .dev** so I'd stop watching engineers do this from scratch every other year.

If you're at the start of this and your gut says "two weeks," at least double the list above before you commit. The platform engineering eats more time than the user-facing feature.

What did the rest of you learn the hard way?

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
