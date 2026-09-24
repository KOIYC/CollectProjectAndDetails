---
type: "corpus"
item_id: "c826a6db1fa70efa"
title: "How do you decide what goes in your product update email?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/microsaas/comments/1wk4bkt/how_do_you_decide_what_goes_in_your_product/"
author: "Milougri"
published_at: "2026-09-19T06:21:11+08:00"
captured_at: "2026-09-22T12:54:29+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-22"
pub_day: "2026-09-19"
tags:
  - 语料
  - reddit
  - r/microsaas
metrics: {"score": 7, "comments": 10, "upvote_ratio": 1}
comments_count: 10
comments_total: 10
discovered_via: "reddit:7d+settle3"
---

# How do you decide what goes in your product update email?

> [!info] 一句话导读
> Shipping constantly and customers having no idea seems to be the default state. The writing was never the blocker for me. Deciding which of the forty merged PRs…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/microsaas/comments/1wk4bkt/how_do_you_decide_what_goes_in_your_product/>
> 指标：得分=7 · 评论=10 · 赞踩比=1
> 作者：Milougri　|　发布：2026-09-19T06:21:11+08:00
> 项目链接：—
> 采集：2026-09-22T12:54:29+08:00　|　id：`c826a6db1fa70efa`

## 正文

Shipping constantly and customers having no idea seems to be the default state. The writing was never the blocker for me. Deciding which of the forty merged PRs a customer would actually notice was, and that means reading diffs which is usually not the job of the person writing the email.

Visuals are the other half. A screenshot of an interaction says nothing, and re-recording a screen capture every time is the chore that kills the ritual after two months. I've been recording short GIFs off staging instead, which helps, but keeping the demo data presentable is a constant fight.

Curious how other teams handle the selection part. Who owns it where you work, and how often do you actually send?

## 评论（10/10）

> **QuanTradin**（2 分） · 2026-09-19T06:29:03+08:00　
> Engineering owns selection everywhere I have seen it work, for exactly the reason you name: the person who can read forty diffs is the only one who can tell a rename from the thing a customer waited a year for. The writing starts after that list exists.
>
> What made it survive was moving the decision to merge time instead of email time. One line in the PR description saying whether this is worth telling anyone, filled in by whoever merged it. Then the email is a filter over an existing list rather than an archaeology dig once a month.

---

> **lindqvist_e**（2 分） · 2026-09-19T06:35:05+08:00　
> The selection problem goes away if you make it structural: tag PRs with a customer-facing label at merge time, and only those get considered. Whoever merges decides, not the email writer. I do this for my own stuff and the label filter cuts forty PRs to maybe four.
>
> On cadence, monthly is the sweet spot for most microsaas. Weekly trains people to ignore you, quarterly and nobody remembers what changed.

---

> **Wooden_Astronomer718**（3 分） · 2026-09-19T06:39:07+08:00　
> The merge time tagging idea below covers the selection half well. For the visuals, the fix that stuck for us was building one small internal demo environment with fake but realistic data, rather than pulling from staging or production, and keeping it in a state that always looks good to record from. Re-recording real screens fails because live accounts get messy, empty states show up, or numbers look wrong that week. A seeded demo account you refresh once a quarter means you can grab a GIF in five minutes instead of hunting for a clean session. We also stopped trying to visually represent everything: small copy or config changes just get one line of text, and GIFs are saved only for interactions that actually changed on screen. That cut recording time roughly in half and made the email faster to put together every month.

---

> **Milougri**（1 分） · 2026-09-19T07:30:00+08:00　
> Merge time instead of email time is the right call. The part I still find blurry is what happens after. The line in the PR is written from the implementation side, so you have the right four items but not the sentences you'd send to a customer. Who picks it up from there in your setup?

---

> **Milougri**（1 分） · 2026-09-19T07:32:43+08:00　
> The one thing I keep wondering about is whether this holds up long term. Tagging, keeping the seed current, keeping the demo env recordable, none of it is hard, but it's all on engineers and none of it is their job. Did it stick for you, or did it need someone pushing it every cycle?

---

> **Dazzling_Bug_2876**（1 分） · 2026-09-19T07:58:53+08:00　
> does the one-line PR annotation actually stick though? feels like the kind of thing people stop filling in after a few weeks

---

> **QuanTradin**（1 分） · 2026-09-19T08:08:21+08:00　
> Whoever sends the email rewrites all of it. The PR line isn't copy, it's a flag, so it only has to be good enough for someone to decide this one deserves a sentence.
>
> That person never opens the diff. They ask the engineer one question per item when the line is unclear, and it's usually about who it affects rather than what changed.

---

> **Khavel_dev**（1 分） · 2026-09-19T16:35:17+08:00　
> We just tag PRs with a 'changelog-worthy' label at merge time. When it's time to write the email, query for that label and you have the list. Removes the 'read 40 diffs and decide' part entirely.
>
> For the visuals, I stopped doing screenshots, short screen recordings off staging show the interaction instead of a frozen frame. The demo data fight is real though, I don't have a good answer for that one.

---

> **devhisaria**（1 分） · 2026-09-21T23:56:56+08:00　
> We tried the PR label thing and it broke down because nobody wanted to be the one tagging, so we flipped it: PM does a 10 minute loom every Friday walking through what merged, then picks 3.

---

> **Milougri**（1 分） · 2026-09-22T05:23:11+08:00　
> Does the PM keep doing it, or has it started slipping? That's the part I'd expect to decay after a few months.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
