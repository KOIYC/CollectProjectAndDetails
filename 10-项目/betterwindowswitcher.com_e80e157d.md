---
type: "project"
title: "Show HN: A 3D Mac window switcher with browser tab support and search"
project_url: "https://betterwindowswitcher.com/"
first_seen: "2026-09-21T09:44:03+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_julien_dev
  - story_49776828
  - show_hn
lang: "en"
---

# Show HN: A 3D Mac window switcher with browser tab support and search

> [!info] 一句话导读
> Hey HN. I made this little app, because I missed Compiz but also because I wanted a way to switch between tabs as well as my windows.Around 2008 a Linux desktop…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://betterwindowswitcher.com/>
> 首次收录：2026-09-21T09:44:03+08:00
> 来源渠道：HN Show HN
> 标签：author_julien_dev, story_49776828, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T09:44:03+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/33f748ff5a4a19c7_Show-HN-A-3D-Mac-window-switcher-with-browser-tab]] |

## 摘要正文

Hey HN. I made this little app, because I missed Compiz but also because I wanted a way to switch between tabs as well as my windows.Around 2008 a Linux desktop could spin your windows around a cube and flip through them like cards, and so far I have not seen anything like that on Mac. I also tried a bunch of different Command-Tab alternatives like AltTab, but so far they always lacked the following things: a live visual preview of windows and some kind of way to switch and search between individual browser tabs.So I built a simple prototype and refined it over the last two months.It goes like this: press a shortcut and every open window shows up as a 3D card, in one of seven arrangements. Browser tabs get their own cards as well and you can flick through each one. Hitting space makes the search come up so you can type a few letters and it finds the window or tab. Fuzzy searching is implemented as well. I also added a quick Option + ` (key above tab) to instantly switch to the last window without any UI coming up, because I do this a lot.For the curious: Swift and Metal, window pictures come from ScreenCaptureKit and it only captures while the switcher is open, nothing runs in the …
