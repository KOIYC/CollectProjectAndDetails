---
type: "corpus"
item_id: "63eda46e893026d4"
title: "WD MyCloud support caught me off guard."
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1xpo77q/wd_mycloud_support_caught_me_off_guard/"
author: "UberWagen"
published_at: "2026-11-07T05:07:07+08:00"
captured_at: "2026-11-17T11:10:00+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-17"
pub_day: "2026-11-07"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Cloud Storage
metrics: {"score": 11, "comments": 7, "upvote_ratio": 0.7619047619047619}
comments_count: 8
comments_total: 8
discovered_via: "reddit:14d+settle10"
---

# WD MyCloud support caught me off guard.

> [!info] 一句话导读
> Call me un-aware, living under a rock, whatever...But my PR2100, that still works, which I've had since 2019 is now going to lose remote access come December. I…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1xpo77q/wd_mycloud_support_caught_me_off_guard/>
> 指标：得分=11 · 评论=7 · 赞踩比=0.7619047619047619
> 作者：UberWagen　|　发布：2026-11-07T05:07:07+08:00
> 项目链接：—
> 采集：2026-11-17T11:10:00+08:00　|　id：`63eda46e893026d4`

## 正文

Call me un-aware, living under a rock, whatever...But my PR2100, that still works, which I've had since 2019 is now going to lose remote access come December. I mainly use it for file storage and a handful of plex streams, but I have enjoyed being able to access my files remotely through browser. I'm stuck between "load unraid and hax0r-fy the fan" or "maybe I should just build my own to future proof corporate shenanigans".

I like the footprint and the ease of use that the PR2100 brought me in the past. I really don't want to buy another NAS, this put me off.

What would you recommend if you were to build a pr2100 clone?

## 评论（8/8）

> **asimovs-auditor**（1 分） · 2026-11-07T05:07:33+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **UberWagen**（1 分） · 2026-11-07T05:08:44+08:00　
> AI was not used at all in the creation of this post.

---

> **jlcs-es**（1 分） · 2026-11-07T05:42:53+08:00　
> Prebuilt: in ugreen NAS (Intel versions) you can install your own OS, you just need to disable a watchdog in the BIOS and you can override the ugreen OS with unRAID/truenas/whatever. They have 2 bay versions quite small
>
> Build your own: plenty of guides written and in YouTube with part lists to build your own NAS. Depending on your location, there are PC cases for mini itx boards with HDD slots

---

> **imbannedanyway69**（5 分） · 2026-11-07T05:43:31+08:00　
> Or just run tailscale and access it from anywhere over a self hosted VPN

---

> **Timely-Shine**（0 分） · 2026-11-07T05:43:50+08:00　
> Beelink Me PRO or Ugreen (both would allow you to load whatever OS you want)

---

> **epsiblivion**（1 分） · 2026-11-07T06:06:42+08:00　
> you can install truenas or openmediavault on a diy server/pc with some hard drives.

---

> **MongooseWonderful198**（2 分） · 2026-11-07T12:25:01+08:00　
> For the browser access you mentioned, Tailscale gives you a network path to the NAS; you'd still need a web file interface to replace MyCloud's portal.
>
> If the PR2100 keeps serving its files over SMB and you have another always-on machine, one option is Nextcloud with its [SMB external-storage backend](https://docs.nextcloud.com/server/latest/admin_manual/configuration_files/external_storage/smb.html). That lets you keep the files on the NAS while running the browser interface elsewhere. You'd be taking on a Nextcloud service to maintain, but it gives you an option before replacing the storage hardware or installing another OS on it.

---

> **lplanum**（1 分） · 2026-11-07T14:29:19+08:00　
> Just setup a vpn or proxy.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
