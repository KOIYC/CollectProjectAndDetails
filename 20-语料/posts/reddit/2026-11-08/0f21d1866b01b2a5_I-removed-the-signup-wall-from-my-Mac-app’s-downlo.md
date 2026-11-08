---
type: "corpus"
item_id: "0f21d1866b01b2a5"
title: "I removed the signup wall from my Mac app’s download flow"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/buildinpublic/comments/1xiabkh/i_removed_the_signup_wall_from_my_mac_apps/"
project_url: "https://awesomeindie.com/product/afterlid"
author: "rjsajnani"
published_at: "2026-10-29T12:25:21+08:00"
captured_at: "2026-11-08T12:52:11+08:00"
lang: "en"
kind: "post"
topic: 健康/生活
shard: "2026-11-08"
pub_day: "2026-10-29"
tags:
  - 语料
  - reddit
  - r/buildinpublic
metrics: {"score": 3, "comments": 5, "upvote_ratio": 1}
comments_count: 5
comments_total: 5
discovered_via: "reddit:14d+settle10"
---

# I removed the signup wall from my Mac app’s download flow

> [!info] 一句话导读
> One change I made before launching AfterLid: you can now download the Mac app without creating an account.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/buildinpublic/comments/1xiabkh/i_removed_the_signup_wall_from_my_mac_apps/>
> 指标：得分=3 · 评论=5 · 赞踩比=1
> 作者：rjsajnani　|　发布：2026-10-29T12:25:21+08:00
> 项目链接：<https://awesomeindie.com/product/afterlid>
> 采集：2026-11-08T12:52:11+08:00　|　id：`0f21d1866b01b2a5`

## 正文

One change I made before launching AfterLid: you can now download the Mac app without creating an account.

It’s a Mac utility with an iPhone and Android companion. The account is needed to connect those devices, but the Mac app also works on its own. Asking people to sign in before downloading felt too early.

The flow is now: download the Mac app, try it, then create an account if you want to connect your phone. Linking still requires signing in on both devices and approving the Mac.

The Mac modes, safeguards and viewing live status from your phone are free. Changing modes remotely is part of the paid Pro plan.

The next thing I want to measure is how many downloads turn into completed phone connections.

AfterLid is on Awesome Indie today:
https://awesomeindie.com/product/afterlid

If you’ve shipped a desktop app with a phone companion, when did you introduce account creation?

## 评论（5/5）

> **TheShoddyRefinery**（1 分） · 2026-10-29T12:29:01+08:00　
> Smart move forcing signup before people even see what the app does always felt backwards to me, like asking for wedding ring before first date
>
> Interesting how you kept the account optional for Mac-only use, most devs would just lock everything behind login out of habit

---

> **rjsajnani**（1 分） · 2026-10-29T12:40:55+08:00　
> Haha, I was definitely proposing too early. The Mac app works on its own, so it made more sense to let people try it first and ask for an account when they want to connect their phone.

---

> **Hot_Statistician3302**（1 分） · 2026-10-29T13:24:43+08:00　
> Good call. I'd bring the account in at the moment it unlocks something the person already wants, which for you is linking the phone. Before that, a Mac app people can just open and poke at has way less friction. For the metric, I'd also track how many downloads get opened at least once, since that tells you whether the leak is at the download or at the connection step.

---

> **rjsajnani**（1 分） · 2026-10-29T13:36:07+08:00　
> Good point. I was jumping from download straight to phone linked. First open belongs in between, otherwise I won’t know whether people are getting stuck opening the Mac app or connecting their phone.

---

> **vincent_sch**（1 分） · 2026-10-29T17:49:19+08:00　
> Some people might only want the Mac app. You could count how many start connecting a phone and how many finish. Then check how many finish signing in on each device and how many approve the Mac.

## 导航

- 项目页：[[10-项目/awesomeindie.com_37353578]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`健康/生活`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
