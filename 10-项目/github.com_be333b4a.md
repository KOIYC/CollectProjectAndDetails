---
type: "project"
title: "Show HN: I built a tool that finds reliability bugs in your code"
project_url: "https://github.com/dubinc/dub.link/issues/4707"
first_seen: "2026-10-29T20:41:52+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_aray07
  - story_50280650
  - show_hn
lang: "en"
---

# Show HN: I built a tool that finds reliability bugs in your code

> [!info] 一句话导读
> Hey HN,I’m Abhishek. I'm building Opslane, a tool that finds reliability issues in your code. On every PR, it spins up your entire app and then tries to find we…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/dubinc/dub.link/issues/4707>
> 首次收录：2026-10-29T20:41:52+08:00
> 来源渠道：HN Show HN
> 标签：author_aray07, story_50280650, show_hn
> 最新指标：点赞=6 · 评论=0 · engagement_velocity=6

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-29T20:41:52+08:00 | HN Show HN | 点赞=6 · 评论=0 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-10-29/d5adaa297ed275f8_Show-HN-I-built-a-tool-that-finds-reliability-bugs]] |

## 摘要正文

Hey HN,I’m Abhishek. I'm building Opslane, a tool that finds reliability issues in your code. On every PR, it spins up your entire app and then tries to find weak spots that would break in production.Demo: https://youtu.be/47phxkdh6f0Example: We tested Opslane on Lago (open-source billing) and found a bug where customers get double charged. Opslane made Stripe take the money and then return a 500. Lago marked the payment failed. A retry from the dashboard charged the customer again. https://github.com/getlago/lago-api/issues/6903Why I built thisI used to work on reliability at Robinhood. We used to run chaos testing in our staging environments: inject faults in various parts of the system and see what breaks. We found issues like Kafka or Redis being unavailable for a few seconds could take the whole app down.But that kind of testing was expensive. It needed a well maintained staging environment. Engineers needed to know what to test. Most teams never actually did it.Over the last year, coding agents have gone writing some of my code to almost all my code now. Teams are shipping way more code than they were 6 months ago.Code review tools read the diff, but a lot of reliability bugs…
