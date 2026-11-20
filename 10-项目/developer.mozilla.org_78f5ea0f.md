---
type: "project"
title: "One Month After the Hackathon: Why My 4-Service App Stopped Working (and What @mansio Caught in the Verifiers)"
project_url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols"
first_seen: "2026-11-20T09:48:47+08:00"
sources:
  - devto
tags:
  - 项目
  - devto
  - ai
  - javascript
  - buildinpublic
  - opensource
lang: "en"
---

# One Month After the Hackathon: Why My 4-Service App Stopped Working (and What @mansio Caught in the Verifiers)

> [!info] 一句话导读
> What breaks a month after a hackathon, and what a fellow DEV writer caught in the verifiers.*

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols>
> 首次收录：2026-11-20T09:48:47+08:00
> 来源渠道：dev.to
> 标签：ai, javascript, buildinpublic, opensource
> 最新指标：reactions=54 · 评论=34 · reading_time=6

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-16T10:03:12+08:00 | dev.to | reactions=33 · 评论=25 · reading_time=6 | [[20-语料/posts/devto/2026-11-16/63c3e7b66478d404_One-Month-After-the-Hackathon-Why-My-4-Service-App]] |
| 2026-11-17T11:11:25+08:00 | dev.to | reactions=37 · 评论=27 · reading_time=6 | [[20-语料/posts/devto/2026-11-16/63c3e7b66478d404_One-Month-After-the-Hackathon-Why-My-4-Service-App]] |
| 2026-11-19T09:46:14+08:00 | dev.to | reactions=54 · 评论=33 · reading_time=6 | [[20-语料/posts/devto/2026-11-16/63c3e7b66478d404_One-Month-After-the-Hackathon-Why-My-4-Service-App]] |
| 2026-11-19T09:56:24+08:00 | dev.to | reactions=54 · 评论=33 · reading_time=6 | [[20-语料/posts/devto/2026-11-16/63c3e7b66478d404_One-Month-After-the-Hackathon-Why-My-4-Service-App]] |
| 2026-11-20T09:48:47+08:00 | dev.to | reactions=54 · 评论=34 · reading_time=6 | [[20-语料/posts/devto/2026-11-16/63c3e7b66478d404_One-Month-After-the-Hackathon-Why-My-4-Service-App]] |

## 摘要正文

*What breaks a month after a hackathon, and what a fellow DEV writer caught in the verifiers.*  > **TL;DR:** A month after shipping [README Clew 2](https://readme-clew-2.vercel.app), I opened it up and every scan failed. Nothing was wrong with the deterministic verifiers or with Jev on Glasser. Instead, three small operational traps lined up at once: an expired 30-day GitHub token on a tool that only reads public repos, a rotated Claude Haiku key scoped only to `Development` in Vercel, and a substring bug that fellow DEV writer [Mikhail (@mansio)](https://dev.to/mansio) found and fixed in [PR #2](https://github.com/earlgreyhot1701D/readme-clew-2/pull/2).  In October I built [README Clew 2](https://github.com/earlgreyhot1701D/readme-clew-2) for the AdaL "What Would Jev Do?" hackathon. It checks whether a public JavaScript or TypeScript repo's README matches its code, sorting every checkable line into four buckets: **Contradicted**, **Missing**, **Unverifiable**, and **Verified**.  The core rule of the build is that **models never decide what is true**:  | Job | Who does it | |---|---| | Split the README into lines and settle obvious headings/badges | Deterministic code rules | | Lab…
