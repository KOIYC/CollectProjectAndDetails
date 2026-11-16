---
type: "project"
title: "Show HN: Rystic – Stateful Local Simulators of Slack, GitHub and Linear"
project_url: "https://rystic.ai/"
first_seen: "2026-11-11T13:37:17+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_evan_whitehouse
  - story_50448400
  - show_hn
lang: "en"
---

# Show HN: Rystic – Stateful Local Simulators of Slack, GitHub and Linear

> [!info] 一句话导读
> Hi HN, we're Zach and Evan, founders of Rystic (https://www.rystic.ai). As LLMs have progressed, producing code has become fast and cheap but verification has n…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://rystic.ai/>
> 首次收录：2026-11-11T13:37:17+08:00
> 来源渠道：HN Show HN
> 标签：author_evan_whitehouse, story_50448400, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-11T13:37:17+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-11-11/92df653b7e2a3d1b_Show-HN-Rystic-–-Stateful-Local-Simulators-of-Slac]] |

## 摘要正文

Hi HN, we're Zach and Evan, founders of Rystic (https://www.rystic.ai). As LLMs have progressed, producing code has become fast and cheap but verification has not. At my previous company I noticed that whenever I could test a service locally or in CI this bottleneck went away. If a service needed to use a shared sandbox or staging environment to run integration tests, verification was a huge pain. At Rystic we are taking that idea and applying it to every third-party service. We are trying to give developers a way to verify that their code works without calling real systems.To do this, we build deterministic simulators of APIs like Slack, Stripe and S3. You can control these locally; set their state and inspect it. Our aim is to make these a controllable stand-in for the real service, much more so than any sandbox. For this we offer fault injection, latency injection and multiple actor support. So for example you can cancel a subscription mid-cycle as the customer in the billing portal, then check that your app handles the proration and removes access. In the Stripe sandbox someone has to click through the portal by hand.We recreate these applications as Go binaries to make them pe…
