---
type: "corpus"
item_id: "92df653b7e2a3d1b"
title: "Show HN: Rystic – Stateful Local Simulators of Slack, GitHub and Linear"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50448400"
project_url: "https://rystic.ai/"
author: "evan_whitehouse"
published_at: "2026-11-11T00:44:10Z"
captured_at: "2026-11-11T13:37:17+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-11"
pub_day: "2026-11-11"
tags:
  - 语料
  - hn_show
  - author_evan_whitehouse
  - story_50448400
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Rystic – Stateful Local Simulators of Slack, GitHub and Linear

> [!info] 一句话导读
> Hi HN, we're Zach and Evan, founders of Rystic (https://www.rystic.ai). As LLMs have progressed, producing code has become fast and cheap but verification has n…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50448400>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：evan_whitehouse　|　发布：2026-11-11T00:44:10Z
> 项目链接：<https://rystic.ai/>
> 采集：2026-11-11T13:37:17+08:00　|　id：`92df653b7e2a3d1b`

## 正文

Hi HN, we're Zach and Evan, founders of Rystic (https://www.rystic.ai). As LLMs have progressed, producing code has become fast and cheap but verification has not. At my previous company I noticed that whenever I could test a service locally or in CI this bottleneck went away. If a service needed to use a shared sandbox or staging environment to run integration tests, verification was a huge pain. At Rystic we are taking that idea and applying it to every third-party service. We are trying to give developers a way to verify that their code works without calling real systems.To do this, we build deterministic simulators of APIs like Slack, Stripe and S3. You can control these locally; set their state and inspect it. Our aim is to make these a controllable stand-in for the real service, much more so than any sandbox. For this we offer fault injection, latency injection and multiple actor support. So for example you can cancel a subscription mid-cycle as the customer in the billing portal, then check that your app handles the proration and removes access. In the Stripe sandbox someone has to click through the portal by hand.We recreate these applications as Go binaries to make them performant. A single simulator can handle thousands of requests per second. You can even control whether they get rate limited or not depending on how realistic you want your test to be.To make the simulators we construct a set of tests based on their docs, probe their API, gather traces then use that to reverse engineer the state transitions of the application. Then we iterate on this by running deterministic tests and actively trying to break it. Proving this state machine is the same as the original would be NP hard but we can still show that they are equivalent over several hundred multi-step workflows. To make sure that our version stays accurate we test every night to catch drift and repair it. Each simulator's fidelity card lists its score, which is how closely it matches the real API across those workflows, and we share the failing tests with customers: https://www.rystic.ai/simulatorsIt is frustrating to have these incredibly powerful tools for producing code but then be left with the annoying work of verifying that what is produced actually works. No one wants to spend their day finding API keys, setting up sandbox accounts and manually clicking through applications. We are trying to make a future where that does not happen, where you can move fast and not break things.We would love for you to give it a try. Any feedback is very welcome.Here's a quick video on using the Slack twin to run evals: https://youtu.be/qwin0LAeaeUInstall:curl -fsSL https://www.rystic.ai/install.sh | shbrew install rystic-inc/tap/rysticor download a binary with checksums from https://github.com/Rystic-Inc/rystic/releases.Free: the Slack, GitHub and Linear simulators. No card needed. Everything else is $90 a month, and code HACKERNEWS will get you a month free.Current simulators: Stripe, Slack, GitHub, Kalshi, PayPal, Lob, Okta, Linear, Resend, Anthropic, Clerk, Dropbox, Gmail, Google Drive, Notion, S3, Shopify Storefront, Word.Coming: OpenAI, ElevenLabs, NetSuite, QuickBooks, Square, Sentry, PostHog.We are rapidly adding more to our catalog and if there are any that you would like to see added, please let us know in the comments.

## 关联链接

- https://github.com/Rystic-Inc/rystic/releases.Free:
- https://www.rystic.ai
- https://www.rystic.ai/install.sh
- https://www.rystic.ai/simulatorsIt
- https://youtu.be/qwin0LAeaeUInstall:curl

## 导航

- 项目页：[[10-项目/rystic.ai_56ded948]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
