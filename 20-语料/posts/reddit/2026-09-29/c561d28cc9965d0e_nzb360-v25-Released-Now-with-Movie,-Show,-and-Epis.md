---
type: "corpus"
item_id: "c561d28cc9965d0e"
title: "nzb360 v25 Released :: Now with Movie, Show, and Episode Watching Support!"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1wjx2qp/nzb360_v25_released_now_with_movie_show_and/"
project_url: "https://imgur.com/a/ZFz98jE"
author: "Kev1000000"
published_at: "2026-09-19T01:45:29+08:00"
captured_at: "2026-09-29T09:43:45+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-09-29"
pub_day: "2026-09-19"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Release (No AI)
metrics: {"score": 43, "comments": 15, "upvote_ratio": 0.91}
comments_count: 18
comments_total: 18
discovered_via: "reddit:14d+settle10"
---

# nzb360 v25 Released :: Now with Movie, Show, and Episode Watching Support!

> [!info] 一句话导读
> Hey r/selfhosted, wanted to let you know, v25 of nzb360 (Android Media Server Manager app) has been released!

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1wjx2qp/nzb360_v25_released_now_with_movie_show_and/>
> 指标：得分=43 · 评论=15 · 赞踩比=0.91
> 作者：Kev1000000　|　发布：2026-09-19T01:45:29+08:00
> 项目链接：<https://imgur.com/a/ZFz98jE>
> 采集：2026-09-29T09:43:45+08:00　|　id：`c561d28cc9965d0e`

## 正文

Hey r/selfhosted, wanted to let you know, v25 of nzb360 (Android Media Server Manager app) has been released!

Screenshots: https://imgur.com/a/ZFz98jE

Play Store Link: https://play.google.com/store/apps/details?id=com.kevinforeman.nzb360

------

This is quite a big release and brings with it a pretty fun new feature, allowing you to track which content you and any of your other users have watched all across nzb360's interfaces (Dashboard, Sonarr, Radarr, etc).

Along with watch tracking, here is the full changelog of v25:

---

# New
- Tracearr watch tracking!  Supported by Feature Bounties, you can now track which content you and your other users have watched directly in Sonarr, Radarr, and Dashboard 2.
- You can now create "Sections" within your nav drawer, allowing you to group services together to make it easier to find them.
- Readarr has been completely replaced with Chaptarr, which is an actively-maintained fork.  Your existing server settings, and any lifetime unlocks, carry over automatically and will continue to work with your old Readarr instance and any new Chaptarr instance.
- You can now choose to view Dashboard 2's Universal Calendar in a list view, and choose how may days forward and backward it shows.
- Tracearr's user page has been completely re-designed with the new v2 APIs.  You can now view full history, see their devices, top genres, and a bunch of other stats.
- Completely re-wrote welcome/onboarding flow to modernize the experience and get folks up and running faster.
- Completely re-designed all settings screens within nzb360, providing a more modern and intuitive look.

# Improvements
- Revamped Logging Center UI in the nav drawer, with many more errors showing the full JSON body response for better debugging.
- Add button in Sonarr and Radarr 2 is now placed back on the bottom, and can be swiped upward to begin library search.
- You can now view the current CPU temp and power (in watts) of your Unraid machine.
- Sonarr and Radarr 2's manual search filters now separate source and resolution and provide the ability to save defaults.
- Revamped Sonarr 2's Missing tab UI, with a reduction in taps and increased text sizes for upcoming / missing content.
- Cast/crew bottom sheet UI has been revamped and re-written in Compose to provide a much more modern look.
- Sonarr 2 list progress bar now shows unaired content as a hashed state and now ignores monitored status to show downloaded vs total items.
- Improved design of the downloaded file card in Radarr and Sonarr 2.
- The tag list in Sonarr 2 and Radarr 2's Add sheet is now collapsed by default and can be expanded to view more.
- Auto bulk search of items now searches by content order (earliest first) and will provide a notification the auto search has started.
- Tons of other UI improvements and tweaks all throughout the app.
- Major performance improvements and optimizations all throughout app.  Reduced APK size by 30%+.
- Now targeting Android 16.
- Updated various libraries.

# Fixed
- Fixed issue where Sonarr 2 Upcoming items were not showing the correct airing days in some timezones.
- Fixed issue where Sonarr 2 wouldn't show all items in the Activity Queue.
- Fixed issue where "Download Anyway" on manual Sonarr 2 releases wouldn't work.
- Stability improvements.

## 评论（18/18）

> **asimovs-auditor**（1 分） · 2026-09-19T01:45:38+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **Kev1000000**（5 分） · 2026-09-19T01:46:56+08:00　
> nzb360 has been human-written for over 15 years.   No vibe-coded slop here :)

---

> **Hot-Replacement-323**（5 分） · 2026-09-19T02:09:57+08:00　
> wow this is huge update, the watch tracking thing is exactly what i was missing. always hard to remember which episode i left off on my phone vs tablet

---

> **Mohitkoul841**（1 分） · 2026-09-19T02:24:08+08:00　
> Small request, my radar and sonnar is behind traefik basic auth (browser popup sign-up) and the app cant access the servers.
>
> Can you do any work around this?

---

> **Kev1000000**（5 分） · 2026-09-19T02:29:55+08:00　
> Add your basic auth params as headers using the custom headers feature.

---

> **userXinos**（1 分） · 2026-09-19T02:35:23+08:00　
> just configure bypass for /api paths

---

> **alexkidddd**（3 分） · 2026-09-19T03:36:43+08:00　
> What a great update!

---

> **derical_cap_musical**（6 分） · 2026-09-19T03:43:39+08:00　
> one of the few apps i bought a lifetime license for and never regretted it. great update

---

> **BP041**（2 分） · 2026-09-19T04:21:03+08:00　
> Tracearr watch tracking is the killer feature here. Been running a janky Claude Code agent that scrapes Sonarr logs to figure out what's been watched — this is way cleaner. Does it sync play states back to Plex/Jellyfin or is it purely an nzb360-side thing?

---

> **Kev1000000**（1 分） · 2026-09-19T04:23:36+08:00　
> Tracearr gets it from Plex/Jellyfin, and nzb360 gets it from Tracearr, so yes, they should be in sync.

---

> **KHthe8th**（5 分） · 2026-09-19T05:58:22+08:00　
> Maybe I'm not following, but how exactly does that help? Plex/Jellyfin/emby already have the "continue watching". And I run a script to sync my plex and jellyfin watch states so I can seamlessly go back and forth (never used emby)
>
> It seems only useful if you are watching on different accounts?

---

> **ANDROID_16**（1 分） · 2026-09-19T06:47:07+08:00　
> This is what I do. Good luck brute forcing my API keys

---

> **Mizzoufan523**（1 分） · 2026-09-19T09:03:01+08:00　
> Is there a specific thing you need to do to properly connect to Tracearr?
>
> I'm able to use their own mobile app and connect just fine but no matter what I do the connection always fails in nzb360

---

> **userXinos**（0 分） · 2026-09-19T14:08:16+08:00　
> this is the next level of protection - fail2ban.
> btw, it’s not turned on for you, I already found the key and set it to download Snow White (2025) *villainous laughter*

---

> **Chess-Gitti**（4 分） · 2026-09-20T06:29:42+08:00　
> i hate that godawful play store nowadays as apparently the app description is on the very bottom of the playstore page.
>
> yet still it does not say how much an app licence would cost. even after going to the website of nbz360, there is no word of it.
>
> so after this small odysseey, would you be so kind as to tell me how much this app is going to cost me?
>
> i mean at this point, i am not even sure if i want to endorse these shenanigans.

---

> **totomo26**（1 分） · 2026-09-21T03:16:20+08:00　
> Adding on to what the other commenters have said, this is how I've done it using the file config instead of the labels:
>
> [Regular router](https://i.imgur.com/XKbsckr.png)
>
> [Router with header](https://i.imgur.com/pAFXlo5.png)

---

> **2nistechworld**（1 分） · 2026-09-21T14:16:38+08:00　
> Bought a lifetime license, but switched to iOS recently it’s the app I miss the most 😞

---

> **kzshantonu**（1 分） · 2026-09-23T04:37:08+08:00　
> It depends on your play store region

## 关联链接

- https://play.google.com/store/apps/details?id=com.kevinforeman.nzb360

## 导航

- 项目页：[[10-项目/imgur.com_d1da8d41]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
