---
type: "corpus"
item_id: "cfe8bad6c5a2c8e1"
title: "Show HN: Docktor – I put live window previews and widgets on the macOS 26 Dock"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47944044"
project_url: "https://petercsauer.github.io/docktor-releases"
author: "petercsauer"
published_at: "2026-04-29T04:01:55Z"
captured_at: "2026-09-21T01:42:27+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_petercsauer
  - story_47944044
  - show_hn
metrics: {"points": 3, "comments": 2, "engagement_velocity": 3}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:174d"
---

# Show HN: Docktor – I put live window previews and widgets on the macOS 26 Dock

> [!info] 一句话导读
> There's dead space on both sides of the Dock. Nobody uses it. So I stuck widgets there. Music with synced lyrics (Spotify + Apple Music), calendar, weather, a P…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47944044>
> 指标：点赞=3 · 评论=2 · engagement_velocity=3
> 作者：petercsauer　|　发布：2026-04-29T04:01:55Z
> 项目链接：<https://petercsauer.github.io/docktor-releases>
> 采集：2026-09-21T01:42:27+08:00　|　id：`cfe8bad6c5a2c8e1`

## 正文

There's dead space on both sides of the Dock. Nobody uses it. So I stuck widgets there. Music with synced lyrics (Spotify + Apple Music), calendar, weather, a Pomodoro timer, system stats. They sit in little glass panels and stay out of the way until you look down.The other thing: hover a Dock icon and macOS shows you the app name. Thanks, I forgot what Safari was called. Docktor replaces that with live thumbnails of every window for that app. Click one, you're there. Same idea powers a Cmd+Tab replacement. Actual window previews instead of a beauty pageant of app icons.I spent a lot of time matching the system look. Same blur radii, same animation timing. It should feel like part of the Dock, not something bolted on.Native Swift. No Electron, no account, no telemetry.First beta goes out next week. Looking for testers: https://petercsauer.github.io/docktor-releases/Testers get lifetime access free. After that it'll be $10 one-time for 20 seats, 60-day trial. Share it with your whole family or team. No subscription, ever.I'm also building a full Dock replacement for the Liquid Glass haters. Not shipped yet but it's next.43s video: https://youtu.be/iI1zkkPG6hQ

## 评论（2/2）

> **sev_verso** · 2026-04-29T06:14:18.000Z　
> Good work on the polished design, it does seem to blend in with the native interface. Did you need to use any private APIs to position or capture the previews?Personally I hide my dock to reclaim extra space. One app I wish existed is an endless scrollable desktop to plop windows on, in the same manner that Vision Pro does it but without the VR. However, I think that would be hard to impossible to implement with what the native window manager lets you do.

---

> **petercsauer** · 2026-04-29T06:35:26.000Z　
> Thank you! I'd definitely be interested in giving something like that down the line, but I think that might be its own project haha. The one private API is _AXUIElementGetWindow to map AX elements to window IDs.

## 关联链接

- https://petercsauer.github.io/docktor-releases/Testers
- https://youtu.be/iI1zkkPG6hQ

## 导航

- 项目页：[[10-项目/petercsauer.github.io_f0353e3e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
