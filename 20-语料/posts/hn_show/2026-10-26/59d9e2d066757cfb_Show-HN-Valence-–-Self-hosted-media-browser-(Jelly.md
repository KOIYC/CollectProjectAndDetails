---
type: "corpus"
item_id: "59d9e2d066757cfb"
title: "Show HN: Valence – Self-hosted media browser (Jellyfin/Plex alternative)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50236422"
project_url: "https://getvalence.app/"
author: "MarquesCoding"
published_at: "2026-10-25T21:57:41Z"
captured_at: "2026-10-26T09:42:36+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-26"
pub_day: "2026-10-25"
tags:
  - 语料
  - hn_show
  - author_MarquesCoding
  - story_50236422
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Valence – Self-hosted media browser (Jellyfin/Plex alternative)

> [!info] 一句话导读
> Valence: a self-hosted streaming platform

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50236422>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：MarquesCoding　|　发布：2026-10-25T21:57:41Z
> 项目链接：<https://getvalence.app/>
> 采集：2026-10-26T09:42:36+08:00　|　id：`59d9e2d066757cfb`

## 正文

Valence: a self-hosted streaming platform

# Your films and programmes, on every screen in the house. Your films and programmes, on every screen in the house

A streaming platform you run on your own server, for films, programmes, music and books. Nothing you run depends on a server of ours.

See every feature open sourced, and always will be

Your library stays yours. So does what you watch, when you watch it, and who with. It all lives on your server, and with Valence, it never leaves.

- ### Direct play, or a transcode that earns its keep

Every device gets what it can actually take, negotiated per device rather than per server. Hardware transcoding runs on VideoToolbox, NVENC, VAAPI, QSV and AMF, several with AV1, and falls back to the processor cleanly when there's no GPU.
- ### HDR stays HDR

Real PQ and HLG tone-mapping, in software or on the device, because a screen needs it, not because the transcoder gave up and flattened it.
- ### Skips the parts you already know

Intros are found by fingerprinting the audio across episodes and credits by reading the picture, not by a hand-typed timestamp, so it works on a library you already own. Recaps come from an import from Jellyfin or Emby.
- ### Reads books too

A real EPUB reader with its own place in your library, remembering exactly where you left off. Not a bolt-on plugin.

- ### Watch together, properly in sync

A party keeps everybody at the same moment in the same film, drift-corrected rather than drifting, and can be password-protected.
- ### Share a link, not an account

One title or one series, to somebody with no account at all, for as long as you decide. No dock, no search, nothing else to see.
- ### Take it with you

Choose a quality against a size before you commit, then watch offline, including a full offline mode with no server calls at all.
- ### Actually tells you things

In-app notifications and real web push, not just a bell nobody checks.

- ### An admin area built for a real library

Accounts, roles and permissions, live session control, background jobs and scheduling, a metadata match-picker, cache breakdown by artifact kind, a live log viewer.
- ### Webhooks with a real event catalogue

Job lifecycle, library scans, playback, account changes and more, with delivery history and a redeliver button: an automation surface, not a checkbox.
- ### A setup wizard, not a config file

First run walks through the admin account, the server's name and its trusted origins, and gates the app until it's done.

- ### Every endpoint has a contract

Contract-first with Zod, an OpenAPI 3.1 document, and a reference generated from it and served by the server itself: over a hundred routes, actually documented.
- ### API keys as a feature, not an afterthought

Create, list and revoke keys from the account area. Build on the API for real.
- ### Plugins that ask first

Plugins run in a sandbox on your server and can only do what you allowed when you installed them: the sites they may reach, what they may read, how much they may keep. Official ones are signed, and they work on every Valence app.

- ### One image, self-hosted, no phoning home

The server, the web client and the media service ship in one Docker image. Valence reads your library read only by default. Nothing calls out to us; the server asks GitHub whether there is a newer release, which CHECK_FOR_UPDATES=false stops.
- ### A household, not a single account

Everybody gets a face, their own continue watching, their own ratings and history. Admin-issued invites, not open signup.
- ### Real auth

TOTP two-factor with backup codes, WebAuthn passkeys, a device-authorization code flow for TVs: the kind of auth a self-hosted app usually skips.

By the way... Every word is in one strings file, ready to be translated.

## In your pocket, on your server.

The phone app plays your music, films and books from your own server, at home or away, and keeps them for the train.

Fun fact... Your library plays on Apple TV, Android TV and Fire TV* too, with an app for each.*TV models from before 2025 (Android)

## One app for everything you own.

Films, series, music and books in one place, from the same server, with the admin pages that run it a click away.

Home Library Music Books Server

What to carry on with, what is new, and something picked out for tonight.

Psst... Every plugin runs in a process of its own, kept apart from the server.

## Changelog

1. A new look, profiles for everyone in the house, and credits found in everything Valence 1.7 redesigns the interface and the admin area, gives one account several profiles with children’s accounts a parent looks after, finds the end credits in every film and episode, makes HDR in the browser match the server, and adds Whisper subtitles, MPEG-DASH, libraries in S3 buckets and white-labelling. v1.7.0 · 24 October 2026
2. Valence on the App Store Valence 1.6 is the app for iPhone, iPad and Apple TV, now on the App Store. It rebuilds the phone player around stats for nerds and a layout like the big streaming apps, and brings Live TV, Discover, requests and the calendar to the phone. v1.6.0 · 14 October 2026
3. Live TV, and more direct play support in the browser Valence 1.5 adds live television with a guide, plays DTS, TrueHD, 7.1 and HDR films in the browser without the server converting them, and rebuilds requests around a catalogue of every title that works alongside Sonarr, Radarr and Lidarr. v1.5.0 · 11 October 2026
4. Every television, a proper music player on the phone, and the next episode as the credits roll Valence 1.4 comes to Android TV and Fire TV, gives the phone a full music player that keeps time with your other devices, offers the next episode before the credits finish, and lets a public demo hand out a shared account safely. It also closes a round of security holes found in a sweep of the whole app. v1.4.0 · 7 October 2026

Every release

Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence Valence

## Ready to get started?

Valence is free and open source. Put it on your own server in a few minutes, or look round the demo first.

# unxsist/jet-pilot

## 导航

- 项目页：[[10-项目/getvalence.app_1cdc4946]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
