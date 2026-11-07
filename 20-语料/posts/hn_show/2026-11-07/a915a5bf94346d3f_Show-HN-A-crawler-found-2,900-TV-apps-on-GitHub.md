---
type: "corpus"
item_id: "a915a5bf94346d3f"
title: "Show HN: A crawler found 2,900 TV apps on GitHub"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50395066"
project_url: "https://github.com/wingedpanther/openshelf"
author: "postgres"
published_at: "2026-11-06T17:05:23Z"
captured_at: "2026-11-07T09:43:25+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-07"
pub_day: "2026-11-06"
tags:
  - 语料
  - hn_show
  - author_postgres
  - story_50395066
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: A crawler found 2,900 TV apps on GitHub

> [!info] 一句话导读
> wingedpanther/openshelf

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50395066>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：postgres　|　发布：2026-11-06T17:05:23Z
> 项目链接：<https://github.com/wingedpanther/openshelf>
> 采集：2026-11-07T09:43:25+08:00　|　id：`a915a5bf94346d3f`

## 正文

# wingedpanther/openshelf

An app store for Android TV that installs open-source TV apps from GitHub releases

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: GNU General Public License v3.0
- Default branch: main
- Created: 2026-11-06T16:43:38Z

## Languages

- Kotlin

## Topics

- android-tv
- app-store
- apps
- fire-tv
- google-tv
- jetpack-compose
- leanback
- open-source
- sideload

## Top Contributors

- wingedpanther (3 contributions)

---

## README

# Open Shelf

An app store for Android TV that lists open-source TV apps from GitHub and installs them from each project's releases, using only the remote.

Google Play on TV only carries apps that publish there. Plenty of good TV apps only live on GitHub, where installing one means a phone, a download link and a guess at which APK fits your box. Open Shelf does that part for you.

Open Shelf on Android TV

Watch the full-quality video

## What it does

- Lists about 2,900 Android TV apps from GitHub, in 18 categories
- Every app in the list declares TV support in its manifest and ships an APK in its latest release
- Search by name or by what an app does, like "video player" or "launcher"
- Picks the APK that matches your TV's CPU
- Checks the signing key before installing an update, and holds the update if the key changed
- My Apps shows what's installed, with updates for apps in the catalog
- Light and dark themes, and a choice of accent colours
- IPTV players and debrid or Stremio streaming clients are hidden by default, with a switch in Settings to show them

## Screenshots

| | |
|---|---|
| Discover | Categories |
| Discover | Categories |
| A category | An app page |
| A category | An app page |
| Search | Settings |
| Search | Settings |

## Install

You need an Android TV, Google TV, Fire TV or other Android box running Android 9 or newer.

1. Download the latest `OpenShelf-x.y.z.apk` from Releases.
2. Sideload it with an app like Downloader, or from a computer with `adb install OpenShelf-x.y.z.apk`.
3. The first time you install an app, Android asks you to allow installs from Open Shelf. Allow it once.

## The catalog

The app list is built from public GitHub data and ships inside the APK. An app is included when:

- the repository isn't a fork
- its latest release has an APK, published in the last 3 years
- that APK's manifest has the Android TV launcher entry

Apps with fewer than 10 stars stay out of browsing, but search still finds them by their exact name.

## Build

Needs JDK 17 or newer and the Android SDK. Point `local.properties` at the SDK (`sdk.dir=...`), then:

```
./gradlew assembleRelease
```

Release builds are signed with the debug key unless a `keystore.properties` file sits in the project root with `storeFile`, `storePassword`, `keyAlias` and `keyPassword`.

## Licence

Open Shelf is licensed under the GNU General Public License v3.0. See LICENSE.

The Geist font is licensed under the SIL Open Font License 1.1. See FONT-LICENSE-OFL.txt.

App names, descriptions and artwork in the catalog belong to their projects.

# smokeeaasd/flawless-ui-ux

## 导航

- 项目页：[[10-项目/github.com_4b5dea50]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
