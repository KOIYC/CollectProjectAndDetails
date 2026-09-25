---
type: "corpus"
item_id: "2a247ca136b936fc"
title: "Show HN: I built a seriously detailed free financial planner"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49835193"
project_url: "https://app.finzot.com/plan/6VXFMte2tRMp81sRKhYgXM/results/net-worth"
author: "ryan3789437"
published_at: "2026-09-24T18:50:40Z"
captured_at: "2026-09-25T13:42:25+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-25"
pub_day: "2026-09-24"
tags:
  - 语料
  - hn_show
  - author_ryan3789437
  - story_49835193
  - show_hn
metrics: {"points": 2, "comments": 12, "engagement_velocity": 2}
comments_count: 12
comments_total: 12
discovered_via: "hn:show_hn:3d"
---

# Show HN: I built a seriously detailed free financial planner

> [!info] 一句话导读
> Hi,I spent the last 2.5 years building a super detailed financial planning tool called FinZot (US focused). It helps with questions like deciding when to retire…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49835193>
> 指标：点赞=2 · 评论=12 · engagement_velocity=2
> 作者：ryan3789437　|　发布：2026-09-24T18:50:40Z
> 项目链接：<https://app.finzot.com/plan/6VXFMte2tRMp81sRKhYgXM/results/net-worth>
> 采集：2026-09-25T13:42:25+08:00　|　id：`2a247ca136b936fc`

## 正文

Hi,I spent the last 2.5 years building a super detailed financial planning tool called FinZot (US focused). It helps with questions like deciding when to retire, how much to spend in retirement, how to optimize taxes.I believe it is much more detailed than other free tools or free tiers. It even contains an embedded Excel-inspired domain specific language for customizing the sizing of income/expense, etc.The entire planning engine is free. Runs in your browser (Rust/WASM). No sign-up is necessary. Your data does not leave your browser unless you create an account.There are a couple of paid features in the app which are mostly just quality of life features and AI integration. The AI integration is via a Claude connector that gives Claude access to the full planning engine.Links:
https://app.finzot.com/plan/6VXFMte2tRMp81sRKhYgXM/results/n...finzot.com

## 评论（12/12）

> **dudebro69420** · 2026-09-24T18:59:44.000Z　
> feels vibe coded, and the first modal i tried i couldnt save cause the save button rendered off screen

---

> **kooi** · 2026-09-24T19:07:56.000Z　
> Very cool. Does this integrate with banks like ActualBudget?
> Any plans to support self hosting?

---

> **eecks** · 2026-09-24T21:19:22.000Z　
> The new plan with a 'free' account led me to a payment screen for €91.39.

---

> **nmekala35** · 2026-09-24T22:05:10.000Z　
> honest initial take, feels a lot going in the UI. I think it would be useful if you have some kind of a guided journey asking users a bunch of questions...and then build an initial plan...then enable them to customize

---

> **slater** · 2026-09-24T22:07:09.000Z　
> Content-Security-Policy: The page’s settings blocked an inline script (script-src-elem) from being executed because it violates the following directive: “script-src 'self' 'wasm-unsafe-eval'”. Consider using a hash ('sha256-[redacted]') or a nonce.andUncaught (in promise) Error: telemetry: navigator.sendBeacon is unavailableLatest Firefox, latest macOS

---

> **frlcnic73** · 2026-09-24T22:10:48.000Z　
> Cool! Is the Claude connector best used to build a plan from scratch or to help edit the plan that I start on the Finzot app?

---

> **ryan3789437** · 2026-09-24T19:24:16.000Z　
> Was this on mobile?I started working on FinZot before vibe coding was a thing. It was originally a project to learn rust/wasm. The planning engine is very much not vibe coded. I had too much fun optimizing the engine such that monte carlo trials run trials in ~1ms to have AI write the code. The newer parts of the UI were written by AI. AI has also been amazingly helpful to scale testing.

---

> **ryan3789437** · 2026-09-24T19:18:22.000Z　
> Thanks.I do not have any plans to integrate with banks directly mostly for security reasons. In the paid version you can give Claude a screenshot of your balances/budget and it can update the plan and publish it to the app. Does ActualBudget offer a Claude connector? I have never tried it but I bet with both connectors Claude could read from ActualBudget and update FinZot plans in one conversation.I am also not currently considering true self hosting. The guest mode has no time limit and does not require you to sign in and your data does not leave the browser. I will consider adding a feature to import and export plans.

---

> **ryan3789437** · 2026-09-24T21:23:46.000Z　
> Click Home. Delete the sample plan and then you can start from scratch creating your own plan.

---

> **ryan3789437** · 2026-09-24T22:16:59.000Z　
> There is a semi guided journey. Click Home, delete the sample plan and then click Get Started. It will ask you a series of "simple" questions and then walk you through a series of forms where you can enter your numbers.

---

> **ryan3789437** · 2026-09-24T22:26:15.000Z　
> The connector can do both. It is faster to setup a plan in the app if you are familiar with using these types of tools and know a fair amount about personal finance. If you are less familiar with the space then Claude is really good at answering questions and coming up with reasonable guesses for inputs you might not want to bother figuring out on your own (e.g. the cost of college).I think where the connector really shines is setting up multiple scenarios and comparing the outputs. One pain point of these kinds of multi scenario analysis tools is keeping track of what is different between the setup of each scenario and how those differences in inputs impact the outputs. Claude is really good at this.

---

> **nmekala35** · 2026-09-24T23:35:14.000Z　
> ohk got it. I meant for first time users...set it as default would be quite helpful. I think

## 关联链接

- https://app.finzot.com/plan/6VXFMte2tRMp81sRKhYgXM/results/n...finzot.com

## 导航

- 项目页：[[10-项目/app.finzot.com_f8ee2ce8]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
