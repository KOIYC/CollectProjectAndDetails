---
type: "corpus"
item_id: "18cd8a4b1dedbd6c"
title: "Show HN: I built an Android OS in the browser"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48332983"
project_url: "https://mobilegym.dev/"
author: "haozaz"
published_at: "2026-05-30T05:40:24Z"
captured_at: "2026-09-21T01:43:35+08:00"
lang: "en"
kind: "post"
topic: "移动 App"
shard: "2026-09-21"
pub_day: "2026-05-30"
tags:
  - 语料
  - hn_show
  - author_haozaz
  - story_48332983
  - show_hn
metrics: {"points": 28, "comments": 7, "engagement_velocity": 28}
comments_count: 7
comments_total: 7
discovered_via: "hn:show_hn:144d"
---

# Show HN: I built an Android OS in the browser

> [!info] 一句话导读
> Show HN: I built an Android OS in the browser

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48332983>
> 指标：点赞=28 · 评论=7 · engagement_velocity=28
> 作者：haozaz　|　发布：2026-05-30T05:40:24Z
> 项目链接：<https://mobilegym.dev/>
> 采集：2026-09-21T01:43:35+08:00　|　id：`18cd8a4b1dedbd6c`

## 正文

Show HN: I built an Android OS in the browser

## 评论（7/7）

> **haozaz** · 2026-05-31T08:22:31.000Z　
> opensource ： https://github.com/Purewhiter/mobilegym

---

> **haozaz** · 2026-05-31T08:30:03.000Z　
> After burning through tens of billions of tokens, I built an Android-like OS that runs entirely in the browserThe title is a bit clickbaity, but it is not that far from what actually happened.Over the past few months, we built MobileGym: a fully browser-based, Android-like simulation environment implemented in TypeScript + React.It currently includes 28 simulated apps, including WeChat, Alipay, Xiaohongshu/RED, bilibili, X, Reddit, WeChat Read, China Railway 12306, Tencent Meeting, Spotify, and eBay, plus system apps such as Home, Settings, Contacts, Messages, Photos, Calendar, Files, and Browser.The system supports Xiaomi theme packs and custom widgets. We also reimplemented a number of Android-like system mechanisms directly in the browser, including the Activity stack, Intents, gesture navigation, back handling, and soft keyboard behavior.MobileGym was originally built for GUI agent research, but it is also open for anyone who wants to play with it, study Android-like UI/system mechanisms, or fork the code and build something else on top of it.Online demo: https://mobilegym.dev
> GitHub: https://github.com/Purewhiter/mobilegymFeaturesLightweight and highly concurrent
> A single MobileGym instance uses only around 400 MB of memory, compared with roughly 4–10 GB for a typical Android emulator. A single server can run hundreds or even thousands of environment instances in parallel.416 task templates
> The task templates are parameterized, so they can generate an effectively unlimited number of task instances. Evaluation is deterministic and finishes in milliseconds, without relying on LLM-as-a-judge.Sim-to-real transfer that actually works
> In our tests, models trained with GRPO-style reinforcement learning in the simulated environment transferred more than 95% of their gains to real devices.Easy to extend
> MobileGym is designed to be extensible. Adding a new app only requires creating a folder and a manifest file. Adding a new task only requires writing a Python class, and the shortest tasks can be implemented in as little as three lines of code.Fully sandboxed, with no real-world consequences
> MobileGym does not connect to real services, transfer real money, or send real messages. You can safely click around without worrying about side effects.Although the project started as infrastructure for GUI agent training and evaluation, it ended up becoming a fairly complete browser-based Android-like playground.

---

> **dogukan1636** · 2026-05-31T11:04:10.000Z　
> greate job

---

> **matty1911** · 2026-05-31T12:26:36.000Z　
> look nice but why

---

> **haorui123** · 2026-05-31T08:39:46.000Z　
> cool

---

> **haozaz** · 2026-05-31T13:46:07.000Z　
> Thank you!

---

> **haozaz** · 2026-05-31T13:46:13.000Z　
> Thank you!

## 导航

- 项目页：[[10-项目/mobilegym.dev_aa985d6a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`移动 App`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
