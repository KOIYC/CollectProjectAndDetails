---
type: "corpus"
item_id: "702aaafdb9b3c32a"
title: "Show HN: Golang binaries built for your users depending on their arch and system"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47962828"
project_url: "https://goblin.run/"
author: "aliezsid"
published_at: "2026-04-30T14:13:33Z"
captured_at: "2026-09-21T01:40:57+08:00"
lang: "en"
kind: "post"
topic: "未分类"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_aliezsid
  - story_47962828
  - show_hn
metrics: {"points": 8, "comments": 7, "engagement_velocity": 8}
comments_count: 7
comments_total: 7
discovered_via: "hn:show_hn:174d"
---

# Show HN: Golang binaries built for your users depending on their arch and system

> [!info] 一句话导读
> Show HN: Golang binaries built for your users depending on their arch and system

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47962828>
> 指标：点赞=8 · 评论=7 · engagement_velocity=8
> 作者：aliezsid　|　发布：2026-04-30T14:13:33Z
> 项目链接：<https://goblin.run/>
> 采集：2026-09-21T01:40:57+08:00　|　id：`702aaafdb9b3c32a`

## 正文

Show HN: Golang binaries built for your users depending on their arch and system

## 评论（7/7）

> **fractorial** · 2026-05-03T02:37:38.000Z　
> I cannot fathom why anyone would want this.

---

> **ivere27** · 2026-05-03T02:56:41.000Z　
> so, it's kinda build server, building golang sources in remote server?
> then, download the built binary?
> it seems to be useful for normal enduser I guess

---

> **guessmyname** · 2026-05-03T03:43:06.000Z　
> Oh, this web service is going to be such a nice target for hackers waiting to infect everyone who dares download random binaries. Centralizing “builds on demand” like this creates a pretty juicy supply-chain target. If the service gets popped, you’ve got a one-stop shop for shipping compromised binaries to every arch/OS combo. Convenient idea, but I’d only trust it with strong guarantees: reproducible builds, signed artifacts tied to commits, and a way to verify locally. Otherwise it’s basically “go install URL” with extra steps.

---

> **oefrha** · 2026-05-03T04:15:18.000Z　
> If you're in the market for this kind of thin convenience wrapper you might as well just vibe code a .goreleaser.yaml, .github/workflows/releases.yml and an install.sh. Takes a couple minutes, and you don't need to face angry users when this service is hacked/turns evil/shuts down. (Before anyone protests vibe coding, you're doing less due diligence by using this.)

---

> **duskwuff** · 2026-05-03T04:20:08.000Z　
> > The response of this request is a Golang binary compiled for the requested
> operating system, architecture, package version, and the binary's name—using Go
> 1.17.xUh... Go 1.17 is almost five years old. (The current version is 1.26.) Why is this service using an ancient version of Go?

---

> **gbraad** · 2026-05-03T03:10:35.000Z　
> It is mostly indicative of another underlying issue, like glibc versions or so. But this also leads to weird situations with reproducibility for QE/error reporting. One of the reasons I also hated some distro wanting to devendor and use distro dependencies. This all makes it harder to have a consistent support matrix.

---

> **fractorial** · 2026-05-03T04:29:29.000Z　
> Precisely; Go is by no means perfect, but if you want to throw away its security efforts, by all means use goblin.runI’ll take vibe shooting myself in the foot over lying to myself any day.

## 导航

- 项目页：[[10-项目/goblin.run_23945c84]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`未分类`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
