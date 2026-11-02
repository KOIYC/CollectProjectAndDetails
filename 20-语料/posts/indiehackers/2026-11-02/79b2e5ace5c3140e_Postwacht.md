---
type: "corpus"
item_id: "79b2e5ace5c3140e"
title: "Postwacht"
source: "indiehackers"
source_name: "Indie Hackers 产品库"
url: "https://www.indiehackers.com/product/postwacht"
captured_at: "2026-11-02T09:41:05+08:00"
lang: "en"
kind: "project"
topic: "开发者工具"
shard: "2026-11-02"
tags:
  - 语料
  - indiehackers
metrics: {}
comments_count: 0
comments_total: 0
discovered_via: "ih:products"
---

# Postwacht

> [!info] 一句话导读
> Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+

> [!meta]- 语料信息（点开展开）
> 来源：Indie Hackers 产品库（project）
> 原帖：<https://www.indiehackers.com/product/postwacht>
> 指标：—
> 作者：—　|　发布：—
> 项目链接：—
> 采集：2026-11-02T09:41:05+08:00　|　id：`79b2e5ace5c3140e`

## 正文

Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+
Starting Up Case Studies
 Ideas DB Products DB Sign in Join
Postwacht
 Free email deliverability test with a fix plan
Visit Website
Postwacht Free email deliverability test with a fix plan
 Post 1
 Website
November 1, 2026
 I built a free email deliverability tester that tells you how to fix each problem
Most mail testers tell you "SPF: fail" and leave it there. I wanted one that says what is wrong, why it matters, and gives you the exact DNS record to copy.
 So I built Postwacht (postwacht.de/en). Everything below is free.
 The test: you get a one-time address and send your email to it. No account needed. About 20 checks run in parallel (SPF, DKIM, DMARC, blocklists, TLS, reverse DNS, spam score) and you get a score from 0 to 10 plus a prioritized fix plan with ready-to-paste DNS records.
 With a free account you also get:
 Daily monitoring of your domain (SPF, DKIM, DMARC, MX, MTA-STS, TLS, blocklists) with an email when something changes
A DMARC rollout assistant: it reads your DMARC reports and tells you when it is safe to go from p=none to quarantine to reject, and which senders still fail
Alerts in Telegram, Slack, Microsoft Teams or via webhook
A real inbox test: it shows whether your mail lands in the inbox or in spam at major mailbox providers
There is also a public status page, and the data stays in Germany with no third-party trackers.
 Honest numbers: it is 3 weeks old, about 26 tests so far, 2 accounts, and Google still shows most pages around position 60+. The one thing that works is a niche guide at the bottom of page 1. So it is early days, and I would really like to hear:
 Which check is missing?
Where is the fix plan unclear?
Would you use the DMARC assistant, or do you just set p=none and forget it?
Stack: FastAPI, Postfix, rspamd, PostgreSQL.
postwacht
3 Upvotes
3 Comments
About
 Existing mail testers tell you 'SPF: fail' but not how to fix it. I wanted a free test that explains every problem in plain language and gives you the exact DNS record to copy.
People
 postwacht Founder
Stay informed as an indie hacker.
 Market insights that help you start and grow your business.
Subscribe
Follow @IndieHackers on X for stories and insights about founders building profitable online businesses, and to connect with others in the Indie Hackers community.
 © Indie Hackers, Inc. · FAQ · Terms · Privacy · Cookie Policy ·
Community
 Top Today Top This Week Top This Month Join
Products
 All Products Highest Revenue Add Yours
Databases
 Ideas Products Stories

## 导航

- 项目页：[[10-项目/Postwacht_79b2e5ac]]
- 渠道页：[[50-渠道/indiehackers]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
