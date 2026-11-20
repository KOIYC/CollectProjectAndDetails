---
type: "corpus"
item_id: "4913089ff687282b"
title: "IMPS: Self-hosted photo inventory for storage boxes, with printable QR labels"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1xs1w9j/imps_selfhosted_photo_inventory_for_storage_boxes/"
project_url: "https://demo.getimps.com/"
author: "Superb-Bluebird4648"
published_at: "2026-11-10T03:55:37+08:00"
captured_at: "2026-11-20T09:47:05+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-20"
pub_day: "2026-11-10"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Product Announcement
metrics: {"score": 21, "comments": 20, "upvote_ratio": 0.8620689655172413}
comments_count: 19
comments_total: 20
discovered_via: "reddit:14d+settle10"
---

# IMPS: Self-hosted photo inventory for storage boxes, with printable QR labels

> [!info] 一句话导读
> My daughter and I wrote IMPS (Inventory Management Photo System) as a fun coding project together. We built it for our own household, and we're sharing it in ca…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1xs1w9j/imps_selfhosted_photo_inventory_for_storage_boxes/>
> 指标：得分=21 · 评论=20 · 赞踩比=0.8620689655172413
> 作者：Superb-Bluebird4648　|　发布：2026-11-10T03:55:37+08:00
> 项目链接：<https://demo.getimps.com/>
> 采集：2026-11-20T09:47:05+08:00　|　id：`4913089ff687282b`

## 正文

My daughter and I wrote IMPS (Inventory Management Photo System) as a fun coding project together. We built it for our own household, and we're sharing it in case others find it useful.

The idea is simple: find out what's in a box without taking it down and opening it. Add your items with photos, assign them to boxes, and print a label with the box number, name, and a QR code. Scan the label with your phone to see the contents.

Features include:

* Items organized into boxes, categories, and locations.
*  Photos, descriptions, and searchable inventory.
* Photo-grid and detailed-list views for desktop and mobile.
* Printable QR labels for boxes.
* Database and photo backup/restore.

IMPS is written in Python/Flask with MariaDB and is open source under the MIT license. Docker Compose runs the application and database, with published images for amd64 and arm64. We run our own installation on a Raspberry Pi.

It's designed for a private home network, with one shared login password, and isn't intended to be exposed directly to the internet.

* Website and screenshots (https://getimps.com/)
* Try the demo with sample data (https://demo.getimps.com/)
* Source code (https://github.com/airbornedan/IMPS)
* Docker installation instructions (https://github.com/airbornedan/IMPS/blob/main/deploy/docker/DOCKER.md)

I'd appreciate feedback, especially on the installation instructions and how the box-and-photo workflow fits the way you organize your storage.

## 评论（19/20）

> **asimovs-auditor**（1 分） · 2026-11-10T03:55:48+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **Superb-Bluebird4648**（2 分） · 2026-11-10T03:58:07+08:00　
> The project was hand-written by myself and my daughter, but Claude helped solve some DB issues, and audited it, and we used its recommendations for hardening.

---

> **RowdyNL**（1 分） · 2026-11-10T04:27:11+08:00　
> Looks great! Going to install and try it. I hope when my little girl is older I also can do some coding together !

---

> **Superb-Bluebird4648**（2 分） · 2026-11-10T04:30:57+08:00　
> Honestly, that was the coolest part. She's in college now (a CS major) but we've done all sorts of little "coding" projects along the way--from Scratch all the way to this Python/DB thing.

---

> **RowdyNL**（1 分） · 2026-11-10T04:32:16+08:00　
> Love that! Mine is just three now, so I have to wait a little.. 😇

---

> **ErebusBat**（1 分） · 2026-11-10T04:57:15+08:00　
> This actually looks really interesting.
>
> Q: Can you pre-print the box labels and scan the contents in two different steps?
>
> My use case: I want to print out 20-30 labels and then goto the storage unit and scan / enter them where I won't have a printer or anything like that.

---

> **Superb-Bluebird4648**（1 分） · 2026-11-10T05:14:49+08:00　
> Yes, if I understand your question. Creating the inventory and printing the labels are two separate steps. For your use case, you'd create the boxes first, then print all their labels (the labels have a human-readable number/name as well as the QR code) while at home. Then you'd apply the label to a box and start adding the items as you inventoried the box. But the current version isn't really set up to be on the public internet--you'd have to use a VPN or something to connect to it if the server is at your house and your items are somewhere else.

---

> **ErebusBat**（1 分） · 2026-11-10T05:18:57+08:00　
> I have tailscale so that isn't a problem.
>
> What I am asking is if I can just create "empty" boxes (so I can print the labels).
>
> I then take that stack of labels with me to storage.  Pick a box and then "edit" it's contents, slap the label on, and bob's your uncle.
>
> If I have to create then go back and print, then go back and re-label... that is not a good workflow (for my use)

---

> **Xath0n**（1 分） · 2026-11-10T05:34:56+08:00　
> Your website is down.
>
> Edit: nevermind, it's just because of the ) in the end.

---

> **Superb-Bluebird4648**（1 分） · 2026-11-10T07:34:30+08:00　
> Yes, that would work. You have to “add” the boxes to print the labels but you can do that at home and take them with you. As many as you want

---

> **Superb-Bluebird4648**（1 分） · 2026-11-10T07:35:44+08:00　
> Sorry about that. Reddit caught the end paren in the links

---

> **yellow_neck123**（0 分） · 2026-11-10T07:45:17+08:00　
> Thank you! I have the thought of this to manage my cluttered storage for years but haven't got time to do it.
> Ideally, we can just take a photo of scattered items in a box/container, and let AI to sort out all individual items in a list.

---

> **BrilliantSebastian**（6 分） · 2026-11-10T10:51:50+08:00　
> Homebox.

---

> **MstrVc**（2 分） · 2026-11-10T12:32:37+08:00　
> is awesome

---

> **ikukuru**（1 分） · 2026-11-10T13:58:25+08:00　
> I recently needed a solution for my home, and moving boxes, and found homebox to be too limited and inflexible. Anyway, this project popped up recently and has been working great for me. https://keptinventory.info

---

> **diazeriksen07**（1 分） · 2026-11-10T15:00:14+08:00　
> Somehow doesn't have calendar scheduling for like, recurring filter replacement or other maintainence tasks.

---

> **BrilliantSebastian**（1 分） · 2026-11-10T20:46:42+08:00　
> Homebox? That's not what its for. It's a home inventory system. And a beautiful one at that. We just use home assistant for reminders etc.

---

> **BrilliantSebastian**（0 分） · 2026-11-10T20:48:30+08:00　
> Too limited and inflexible? It's an inventory system. What else do you want it to do? LOL I find that it does everything my family has ever needed. That Kept inventory looks cool though!

---

> **Important_Pomelo_407**（1 分） · 2026-11-11T11:45:29+08:00　
> Saw there was no demo video yet, so I made you one. Here’s the PR:
> https://github.com/airbornedan/IMPS/pull/1
>
> and I used my repo to do it :)
> https://github.com/yasirwhite/OpenDemo

## 关联链接

- https://getimps.com/
- https://github.com/airbornedan/IMPS
- https://github.com/airbornedan/IMPS/blob/main/deploy/docker/DOCKER.md

## 导航

- 项目页：[[10-项目/demo.getimps.com_0c60b6a4]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
