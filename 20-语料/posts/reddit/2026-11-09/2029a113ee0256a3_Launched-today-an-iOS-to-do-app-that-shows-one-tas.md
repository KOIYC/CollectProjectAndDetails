---
type: "corpus"
item_id: "2029a113ee0256a3"
title: "Launched today: an iOS to-do app that shows one task at a time. I can't code; Claude Code wrote it on a Windows PC with no Mac"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/microsaas/comments/1xir2rr/launched_today_an_ios_todo_app_that_shows_one/"
project_url: "https://apps.apple.com/app/id6819368552"
author: "roflwaffle666"
published_at: "2026-10-30T01:52:58+08:00"
captured_at: "2026-11-09T09:41:03+08:00"
lang: "en"
kind: "post"
topic: "SaaS/B2B"
shard: "2026-11-09"
pub_day: "2026-10-30"
tags:
  - 语料
  - reddit
  - r/microsaas
metrics: {"score": 7, "comments": 8, "upvote_ratio": 1}
comments_count: 8
comments_total: 8
discovered_via: "reddit:14d+settle10"
---

# Launched today: an iOS to-do app that shows one task at a time. I can't code; Claude Code wrote it on a Windows PC with no Mac

> [!info] 一句话导读
> Disclosure: I made this.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/microsaas/comments/1xir2rr/launched_today_an_ios_todo_app_that_shows_one/>
> 指标：得分=7 · 评论=8 · 赞踩比=1
> 作者：roflwaffle666　|　发布：2026-10-30T01:52:58+08:00
> 项目链接：<https://apps.apple.com/app/id6819368552>
> 采集：2026-11-09T09:41:03+08:00　|　id：`2029a113ee0256a3`

## 正文

Disclosure: I made this.

**Backstory:** I have ADHD and I forget my to-do list exists. So I built Resurface: a to-do app that shows one task at a time, mostly on a Lock Screen widget, and brings it back later if you ignore it. It went live on the App Store today.

**Tech stack:** Swift and SwiftUI, every line written by Claude Code. I can't read code; I wrote the spec and made every product call. Built on Windows: xtool through WSL builds and installs straight onto a real iPhone. I rented a Mac for one day for the App Store upload. No server, no accounts, no analytics: tasks stay on the phone, so there's no backend to pay for.

**Pricing and revenue:** first month free, then $0.99 a month or $9.99 a year. Kept cheap on purpose. Revenue so far: $0, it launched today.

**Lesson:** most of the work was deciding what to leave out. No list to pick from, no streaks, no "overdue", no due dates. A lot of features that look helpful quietly work against the people they're for.

App Store: https://apps.apple.com/app/id6819368552

Site: https://resurfacehq.app

Roasts of the landing page welcome.

## 评论（8/8）

> **AndrewHahaCO2**（0 分） · 2026-10-30T03:01:47+08:00　
> one task at a time is a sharp constraint. after the free month, i'd watch how many people still use the lock screen widget, not just how many started the trial

---

> **CarefulFoundation801**（0 分） · 2026-10-30T03:31:07+08:00　
> no backend to pay for" and yet $0.99 a month, forever, for a widget. curious what the money is for exactly

---

> **mvrk57**（1 分） · 2026-10-30T03:43:10+08:00　
> since there's no analytics you won't see widget usage like the other comment suggests, so your real number on day 30 is trial to paid in the app store connect subscription stats. also worth checking how the task comes back: ios gives each widget a limited daily reload budget and won't refresh it on demand, so the resurfacing has to be scheduled ahead as timeline entries or it shows up late

---

> **Kyunghun_Venturini**（1 分） · 2026-10-30T04:50:58+08:00　
> for a sub-dollar monthly price, a one-time lifetime unlock might actually convert better. people with adhd often have strong subscription fatigue because they worry they'll forget to cancel it later.

---

> **rnato35**（1 分） · 2026-10-30T09:07:40+08:00　
> Apple developer subscription maybe ?

---

> **roflwaffle666**（1 分） · 2026-10-30T09:27:00+08:00　
> No “backend” but there’s still my time, dev license, domain costs etc.
>
> If an app is free, you and your information are the cost guaranteed

---

> **roflwaffle666**（1 分） · 2026-10-30T09:27:39+08:00　
> That’s right!

---

> **roflwaffle666**（1 分） · 2026-10-30T09:28:06+08:00　
> I’ve thought about it, there’s a fine line. I may introduce a lifetime tier later

## 关联链接

- https://resurfacehq.app

## 导航

- 项目页：[[10-项目/apps.apple.com_e637db01]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`SaaS/B2B`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
