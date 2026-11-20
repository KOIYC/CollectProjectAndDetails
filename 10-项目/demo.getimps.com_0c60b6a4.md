---
type: "project"
title: "IMPS: Self-hosted photo inventory for storage boxes, with printable QR labels"
project_url: "https://demo.getimps.com/"
first_seen: "2026-11-20T09:47:05+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/selfhosted
  - Product Announcement
lang: "en"
---

# IMPS: Self-hosted photo inventory for storage boxes, with printable QR labels

> [!info] 一句话导读
> My daughter and I wrote IMPS (Inventory Management Photo System) as a fun coding project together. We built it for our own household, and we're sharing it in ca…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://demo.getimps.com/>
> 首次收录：2026-11-20T09:47:05+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/selfhosted, Product Announcement
> 最新指标：得分=21 · 评论=20 · 赞踩比=0.8620689655172413

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-20T09:47:05+08:00 | Reddit 独立开发版块 | 得分=21 · 评论=20 · 赞踩比=0.8620689655172413 | [[20-语料/posts/reddit/2026-11-20/4913089ff687282b_IMPS-Self-hosted-photo-inventory-for-storage-boxes]] |

## 摘要正文

My daughter and I wrote IMPS (Inventory Management Photo System) as a fun coding project together. We built it for our own household, and we're sharing it in case others find it useful.  The idea is simple: find out what's in a box without taking it down and opening it. Add your items with photos, assign them to boxes, and print a label with the box number, name, and a QR code. Scan the label with your phone to see the contents.  Features include:  * Items organized into boxes, categories, and locations. *  Photos, descriptions, and searchable inventory. * Photo-grid and detailed-list views for desktop and mobile. * Printable QR labels for boxes. * Database and photo backup/restore.  IMPS is written in Python/Flask with MariaDB and is open source under the MIT license. Docker Compose runs the application and database, with published images for amd64 and arm64. We run our own installation on a Raspberry Pi.  It's designed for a private home network, with one shared login password, and isn't intended to be exposed directly to the internet.  * Website and screenshots (https://getimps.com/) * Try the demo with sample data (https://demo.getimps.com/) * Source code (https://github.com/ai…
