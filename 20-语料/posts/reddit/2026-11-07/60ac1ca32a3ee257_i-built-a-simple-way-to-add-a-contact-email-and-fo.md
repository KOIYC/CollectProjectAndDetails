---
type: "corpus"
item_id: "60ac1ca32a3ee257"
title: "i built a simple way to add a contact email and form to any side project"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1xh4kbq/i_built_a_simple_way_to_add_a_contact_email_and/"
project_url: "https://mailcontact.app/"
author: "MaxBrst"
published_at: "2026-10-28T04:57:00+08:00"
captured_at: "2026-11-07T09:44:34+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-11-07"
pub_day: "2026-10-28"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 4, "comments": 7, "upvote_ratio": 1}
comments_count: 7
comments_total: 7
discovered_via: "reddit:14d+settle10"
---

# i built a simple way to add a contact email and form to any side project

> [!info] 一句话导读
> i’ve been working on a few side projects and kept running into the same annoying problem: setting up a simple contact email.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1xh4kbq/i_built_a_simple_way_to_add_a_contact_email_and/>
> 指标：得分=4 · 评论=7 · 赞踩比=1
> 作者：MaxBrst　|　发布：2026-10-28T04:57:00+08:00
> 项目链接：<https://mailcontact.app/>
> 采集：2026-11-07T09:44:34+08:00　|　id：`60ac1ca32a3ee257`

## 正文

i’ve been working on a few side projects and kept running into the same annoying problem: setting up a simple contact email.

i didn’t want to pay for a mailbox for every project, configure dns records or set up a whole email service just so someone could contact me.

so i built https://mailcontact.app

the idea is pretty simple. you get a contact email address and a free contact form in seconds. messages from both end up in the same inbox, and you can reply directly from there.

you can also get notifications in the tools you already use, so you don’t have to keep checking another inbox.
it’s mainly for indie devs, small saas projects, freelancers or anyone who just needs an easy way for people to reach them.

i’d love to hear what you think, especially if there’s something missing or something you’d do differently.

## 评论（7/7）

> **Dry-Purple-9555**（1 分） · 2026-10-28T05:01:05+08:00　
> this is actually useful, i got like 4 dead side projects and i dont want to pay for email on all of them
>
> the free tier looks generous but what happens when i go over the limit? does it just bounce or you hold the messages somewhere

---

> **MaxBrst**（1 分） · 2026-10-28T05:11:48+08:00　
> good question. nothing gets held, it fails loudly instead:
>
> * **form**: once you hit 50 for the month, new submissions are rejected. the visitor sees “this form has reached its monthly limit, please use another contact method” and their text stays in the form, so they don’t lose what they typed. nothing is stored on our side
> * **email address** (paid plans): the sender gets a normal bounce saying the recipient’s monthly limit is reached
>
> i prefer that to a silent queue: if messages pile up somewhere you never look, the sender thinks it went through. a bounce at least tells them to try another way.
>
> you get a warning in the dashboard at 80% and 100%, you’re never charged automatically, and the count resets monthly on your signup date. caught spam doesn’t count toward the 50.
>
> one thing for your case though: free is 1 project with a contact form, no email address. for 4 projects, Pro is €9/mo total, not per project: up to 10 projects, each with its own form and address, 1000 messages/month shared.

---

> **Holiday_Mhmed**（1 分） · 2026-10-28T07:50:36+08:00　
> how are you handling spam filtering on the forms? that's usually the main pain point with simple contact setups, especially if youre not forcing a harsh captcha on visitors

---

> **MaxBrst**（1 分） · 2026-10-28T08:41:06+08:00　
> No captcha by default. There are several layers of protection, and most real messages go through without the visitor noticing anything. When something looks like a bot, it basically ends up in quarantine: it never hits your inbox, doesn’t notify you and doesn’t count against your quota, and you can still review the borderline ones in case they were legit.
>
> I’m staying vague on purpose: the less spammers know about how the layers work, the better they hold up.

---

> **ImmediateCourage1**（1 分） · 2026-10-28T16:54:58+08:00　
> This is really cool!
>
> And I respect staying vague on purpose, so feel free to ignore my question. But when you say "something looks like a bot", I'm wondering whether that check (I assume some fingerprinting and/or text content analysis) is happening on your backend. Because, if so, there are ways to handle this that would decrease your compute costs while giving the same result.

---

> **MaxBrst**（1 分） · 2026-10-28T21:31:04+08:00　
> Thanks! Yes, it’s on the backend. It has to be, since anyone can POST straight to the endpoint and skip the browser entirely. The cheap checks run first, so the heavier stuff only sees what gets past them, and it’s all self-hosted, so cost isn’t really an issue so far.
>
> Curious what you had in mind though!

---

> **ImmediateCourage1**（1 分） · 2026-10-29T15:45:43+08:00　
> There are a handful of things you can do, but you're right that purely client-side checking is useless. So, a hidden honeypot field that humans can't see but bots will fill out is a cheap filter. Another is a proof of work invisible captcha (full disclosure, I work for Friendly Captcha, and we offer this service); this isn't meant to catch _every_ bot, but it increases abuse cost and makes your form a less appealing target.
>
> Anyway, cool stuff! Keep up the good work!

## 关联链接

- https://mailcontact.app

## 导航

- 项目页：[[10-项目/mailcontact.app_7833cebc]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
