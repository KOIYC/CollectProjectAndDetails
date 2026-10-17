---
type: "corpus"
item_id: "6ebe8559e97d657c"
title: "My open-source project hit 9k GitHub stars, so I'm turning it into a SaaS. Here's how I'm doing it without paywalling the open-source version."
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1wyk1go/my_opensource_project_hit_9k_github_stars_so_im/"
project_url: "https://trustmrr.com/startup/kaneo"
author: "andrejsshell"
published_at: "2026-10-06T04:55:36+08:00"
captured_at: "2026-10-16T09:36:29+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-16"
pub_day: "2026-10-06"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 26, "comments": 10, "upvote_ratio": 0.93}
comments_count: 8
comments_total: 10
discovered_via: "reddit:14d+settle10"
---

# My open-source project hit 9k GitHub stars, so I'm turning it into a SaaS. Here's how I'm doing it without paywalling the open-source version.

> [!info] 一句话导读
> At the end of 2024 I started Kaneo as a small, unserious side project: a project manager that's fast and simple, because every tool I tried was either bloated o…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1wyk1go/my_opensource_project_hit_9k_github_stars_so_im/>
> 指标：得分=26 · 评论=10 · 赞踩比=0.93
> 作者：andrejsshell　|　发布：2026-10-06T04:55:36+08:00
> 项目链接：<https://trustmrr.com/startup/kaneo>
> 采集：2026-10-16T09:36:29+08:00　|　id：`6ebe8559e97d657c`

## 正文

At the end of 2024 I started Kaneo as a small, unserious side project: a project manager that's fast and simple, because every tool I tried was either bloated or locked into someone else's cloud.

It's MIT licensed and you can self-host it for free. Somehow it grew: 9k+ stars on GitHub, 100+ contributors, 150+ releases, and people running it on everything from homelabs to company servers.

A couple of months ago I decided to try making it a business. A few decisions I made, and I'd love your take on them:

1. The paid product is hosting, not features**.** Kaneo Cloud is $4/month for one person and $5/user for teams. The self-hosted version gets every feature, including SSO. I watched other open-source tools move features like SSO into paid tiers and their communities hated it, so I'm betting on convenience instead: backups, updates and EU hosting handled for you.
2. Early users stay free. Every workspace that existed before pricing launched stays free forever. They took a chance on a random side project, so it felt wrong to start charging them.
3. Cheap on purpose. Most of my competitors charge $10 to $25 per user. I'd rather be the obvious choice for small teams than squeeze them.

Where I'm at: the first month of pricing got me to $42 MRR, then $69 (nice). Not life-changing, but people are paying for something they could run for free, which still blows my mind.

Is $4 to $5 per user too cheap to build a real business on? For people who've monetized open source: did hosting alone work, or did you end up with open-core? How do you get self-hosters to try the cloud version without annoying them?

Here's my TrustMRR link: [https://trustmrr.com/startup/kaneo](https://trustmrr.com/startup/kaneo)

## 评论（8/10）

> **UpperWorld11**（0 分） · 2026-10-06T06:31:42+08:00　
> The price isn't the problem, the unit is. Anyone running your MIT build on a homelab will never pay for a container, so per seat is almost free to the people who don't need you and still cheap to the 15 person team that would rather not own the upgrades. Price the instance and put a restore guarantee inside it. You can't charge for MIT code, only for being the one on call.

---

> **andrejsshell**（1 分） · 2026-10-06T06:51:43+08:00　
> This is really useful, thank you. You're right that the homelab folks were never going to pay, and that the value is in not owning upgrades and backups. I'll keep per-seat for small teams who sign up themselves, but I'm going to test a flat-priced managed instance with backups and a tested restore for teams that want someone on call. Out of curiosity, what would you expect that to include, and roughly what would feel fair?

---

> **igrowcabbage**（1 分） · 2026-10-06T07:49:33+08:00　
> First of all congrats to bulding something useful so many people use!
>
> Homelab people might never pay. But self hosting everything can be a pain if you have daily operations and do not want to deal with 10 self hosted apps, managing firewalls and what not. I'd say, hang on and keep going.
>
> Maybe you can offer also better or faster support for the paid model? You could offer extending the platform for customers who need it for their own custom needs. That would be more custom coding work tho for each client.
>
> For 4-5$, I do not know sadly.

---

> **palemotH1**（1 分） · 2026-10-06T08:16:10+08:00　
> the $4-5 pricing is fine to start but your real risk isnt price, its that self-hosters are your best evangelists and they'll never convert. the business probably needs to grow by acquiring new users who never wanted to self-host in the first place, not by converting existing ones.

---

> **soel2103**（0 分） · 2026-10-06T16:34:22+08:00　
> Did you look at what your other competitors do? I'm thinking there are quite a few of them like Upbase, orch and nifty (probably way bigger this one).
>
> Adapt to maybe your pricing based on what they do?

---

> **UpperWorld11**（1 分） · 2026-10-06T19:32:55+08:00　
> Put a number on the restore. A tested restore with a stated target time plus a rollback path is what separates a paid instance from the free build, and a response window of one business day is easier to sell than best-effort. Price it against what it replaces, since teams already anchor on two or three contractor hours a month and anything near the host bill reads as a tip jar. What is a restore taking you end to end right now?

---

> **MartySalade**（1 分） · 2026-10-06T19:54:45+08:00　
> First of all good job on your journey!
>
> Keeping pre-pricing workspaces free forever is a nice touch. The gap between $4 and $10–25 is big. I'm curious whether new Cloud signups would even notice $4 vs $6.

---

> **Konstantin1_61803**（1 分） · 2026-10-07T18:16:31+08:00　
> Hi, I'm just a guy, am trying to start solo-business that involves AI a lot. Was evaluating which project manager to use, that can be used by ai agents also. [Plane.so](http://Plane.so) was a no-go, core is limited, paid plans are expensive (want self-hosted 60 USD/month minimum)
> If there was license to get all features, I would be willing to pay 50-100 USD/year. It may be special license for companies <100k/1M revenue a year (it can also be free <100k).
> Just an idea for you, if you will do paid features, but dont want to screw small guys.
> P.S. I'm also looking at Itsaplan, it's new.

## 导航

- 项目页：[[10-项目/trustmrr.com_a5fdd9a3]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
