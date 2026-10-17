---
type: "corpus"
item_id: "728c1e2eee480a74"
title: "Kelbra"
source: "indiehackers"
source_name: "Indie Hackers 产品库"
url: "https://www.indiehackers.com/product/kelbra"
project_url: "https://getkelbra.com/guides"
captured_at: "2026-10-17T13:38:36+08:00"
lang: "en"
kind: "project"
topic: "开发者工具"
shard: "2026-10-17"
tags:
  - 语料
  - indiehackers
metrics: {}
comments_count: 0
comments_total: 0
discovered_via: "ih:products"
---

# Kelbra

> [!info] 一句话导读
> Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+

> [!meta]- 语料信息（点开展开）
> 来源：Indie Hackers 产品库（project）
> 原帖：<https://www.indiehackers.com/product/kelbra>
> 指标：—
> 作者：—　|　发布：—
> 项目链接：<https://getkelbra.com/guides>
> 采集：2026-10-17T13:38:36+08:00　|　id：`728c1e2eee480a74`

## 正文

Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+
Starting Up Case Studies
 Ideas DB Products DB Sign in Join
Kelbra
 Two-way calendar sync for Google, Outlook, iCloud & CalDAV
Visit Website
Kelbra Two-way calendar sync for Google, Outlook, iCloud & CalDAV
 Post 1
 Revenue $200 / mo
 Website
October 16, 2026
 What I learned testing a calendar sync tool against real-world setups
I'm building Kelbra, which keeps calendars in sync across Google, Outlook, iCloud and CalDAV. Before writing any marketing, I tested it against the setups people complain about in forums. Some of it went fine, and some of it broke in ways I'm glad I found before users did.
 The setups people actually struggle with:
 People with calendars from different organizations: two part-time jobs, a consultant with a client-issued Outlook account, a work and a personal calendar. Each calendar only knows its own meetings.
 Microsoft Bookings users. Bookings only checks your default Outlook calendar, so a Google event or a second account doesn't block the slot. Microsoft's own moderators call it a known limitation.
 People who built the sync themselves in Zapier, Make or Power Automate, and now have duplicates, two automations triggering each other, and deletions that never reach the other calendar.
 What broke in my own testing:
 A "Busy only" mode (show other calendars only that you're busy, never the details) worked on the first sync, but editing the event later raised a false conflict, and resolving that conflict could have leaked the private details or overwritten the real event with "Busy". Fixed.
 Outlook connections silently died an hour after connecting, because the access token was never refreshed. Fixed.
 A weekly meeting with no end date expanded into every Monday until 2040, and the tool tried to create 730 events in one go. It now only syncs a year ahead.
 I turned what I learned into a few guides, each with the do-it-yourself fix first:
 https://www.getkelbra.com/guides
 Two questions for anyone here: if you use more than one calendar, how do you keep them in step today? And if you've tried a sync tool before, what made you stop using it?
mosse692
1 Upvote
Comment
About
 I kept seeing the same problem: people whose calendars belong to different places (a work and a personal account, two jobs, a client's Outlook account) get double-booked because each calendar only knows its own meetings.
 People
 mosse692 Founder
Stay informed as an indie hacker.
 Market insights that help you start and grow your business.
Subscribe
Follow @IndieHackers on X for stories and insights about founders building profitable online businesses, and to connect with others in the Indie Hackers community.
 © Indie Hackers, Inc. · FAQ · Terms · Privacy · Cookie Settings / Policy ·
Community
 Top Today Top This Week Top This Month Join
Products
 All Products Highest Revenue Add Yours
Databases
 Ideas Products Stories

## 关联链接

- https://www.getkelbra.com/guides

## 导航

- 项目页：[[10-项目/Kelbra_75d0f0fd]]
- 渠道页：[[50-渠道/indiehackers]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
