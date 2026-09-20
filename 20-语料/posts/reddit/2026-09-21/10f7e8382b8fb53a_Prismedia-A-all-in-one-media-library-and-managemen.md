---
type: "corpus"
item_id: "10f7e8382b8fb53a"
title: "Prismedia - A all in one media library and management app"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1w3fbfk/prismedia_a_all_in_one_media_library_and/"
project_url: "https://github.com/pauljoda/Prismedia"
author: "Pauljoda"
published_at: "2026-08-31T22:23:58+08:00"
captured_at: "2026-09-21T01:34:41+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Release (AI)
metrics: {"score": 14, "comments": 24, "upvote_ratio": 0.63}
comments_count: 0
comments_total: 0
discovered_via: "reddit:52d+settle3"
---

# Prismedia - A all in one media library and management app

> [!info] 一句话导读
> Over the last year, I've been building Prismedia. Previously, the app was called Obscura, and was actually a Stash alternative, and bits of that are still prese…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1w3fbfk/prismedia_a_all_in_one_media_library_and/>
> 指标：得分=14 · 评论=24 · 赞踩比=0.63
> 作者：Pauljoda　|　发布：2026-08-31T22:23:58+08:00
> 项目链接：<https://github.com/pauljoda/Prismedia>
> 采集：2026-09-21T01:34:41+08:00　|　id：`10f7e8382b8fb53a`

## 正文

Over the last year, I've been building Prismedia. Previously, the app was called Obscura, and was actually a Stash alternative, and bits of that are still present, but the focus has changed drastically.

Essentially, I found I had a whole fleet of apps in my "arrs stack", that all did the same thing, but for different media. So for my own personal use, I created an app that attempts to standardize what these interactions look like.

The core principle is that every media format follows the same "Entity" class, from a data science perspective it actually maps out really well that almost all logic from display to management can be shared, with media specific capabilities augmenting that.

That is what makes this app possible, everything from the core media management, scanning, identifyication via metadata providers, requesting, is all done via the same core platform.

Then, when it makes sense, first class endpoints are added for things like playback, reading, and listening.

The app covers alot of ground, so I'll just list some of the highlights, I enoucrange you to browse the site, source code, and try it out.

* Connect your Prowlarr and downloading clients to automatically track, monitor, and request content. Think the radarr/sonarr/lidarr stack but all integrated, and using the same logic. It even supports soul seek to assist with music sourcing, and when downloading, it will actually probe the files before and after to ensure it is a good match, or upgrade before merging it in.
* View all your content from one interface, from eBooks, comics, audio, movies/tv with rich playback for videos and subtitles, eBooks and audiobook syncing to allow switching between methods of consuming with shared progress, and dedicated audio player
* Identify content already existing using metadata plugins like TMDB, MusicBrainz, OpenLibrary
* Multi user to allow household members access, while delegating which libraries they can see
* NSFW libraries and individual media, to allow filtering of NSFW content, either blocking users from seeing it at all, or using a toggle to quickly hide and view the content. Stash scraper/plugins can be installed and wrapped to identify videos (no StashDB or PornDB, but plugins can be installed in app)
* Progress tracking, stats, and history to see what you've been consuming
* Apple native apps to leverage the native codecs on tvOS, macOS, and iOS for quick and seamless playback of even high quality files

This project was created for a need I have, to have all my media in one rich platform, that treats them all as equals. I liked radarr/sonarr and Jellyfin, but it felt disjointed, and the apps not rich. Jellyfin has a native client, but I felt it was lacking, and audio playback is again in a separate third party app. Prismedia has a native first party app, with all that for free (currently in TestFlight since apple has taken over 2 weeks to even approve the first build).

I post now as I feel the app is in a good release state, it has evolved alot over the last year, but I feel we are now solid, performant, and I challenge you to compare to Kavita, Jellyfin, and the other tools you use. This can be used beside those tools for you to evaluate, simply point at the same directories to scan and it will build out the library in it's own database.

As for AI usage, I did mark this as using AI, but this post (clearly since it probably isn't as coherent as I'd like), and the application were designed, validated, and reviewed by me. These days, I do feel software development is moving to AI assisted, and I've been coding for over 15 years, have a degree in computer science, and worked in large companies. The code isn't just generated and shipped, the design and actualy structure of the app is all exactly as I would write it by hand, but AI has allowed me to develop this while still having a full time job. I use the app every day, I listen to my music on it, have read through books with audiobook interop, watch our tv shows and movies on it, request new content, and for me it fits exactly what I've always wanted.

I hope you feel the same, but if you're happy with your current stack by all means continue to use it, and if you have feedback, please let me know as I'd be happy to look into it.

\- Website: [https://pauljoda.github.io/Prismedia/](https://pauljoda.github.io/Prismedia/)

\- Source: [https://github.com/pauljoda/Prismedia](https://github.com/pauljoda/Prismedia)

\- TestFlight: [https://testflight.apple.com/join/c9bgDxr7](https://testflight.apple.com/join/c9bgDxr7)

## 关联链接

- https://pauljoda.github.io/Prismedia/
- https://testflight.apple.com/join/c9bgDxr7

## 导航

- 项目页：[[10-项目/github.com_c0383749]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
