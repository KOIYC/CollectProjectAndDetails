---
type: "corpus"
item_id: "3dc36f078d95c02a"
title: "Show HN: Roam, a GPS speedometer that tries not to burn in your OLED"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49502017"
project_url: "https://github.com/Nicsilver/roam"
author: "Nicsilver"
published_at: "2026-08-30T19:38:42Z"
captured_at: "2026-09-21T03:11:28+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-08-30"
tags:
  - 语料
  - hn_show
  - author_Nicsilver
  - story_49502017
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:52d"
---

# Show HN: Roam, a GPS speedometer that tries not to burn in your OLED

> [!info] 一句话导读
> GPS speedometer for Android built around OLED burn-in avoidance

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49502017>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：Nicsilver　|　发布：2026-08-30T19:38:42Z
> 项目链接：<https://github.com/Nicsilver/roam>
> 采集：2026-09-21T03:11:28+08:00　|　id：`3dc36f078d95c02a`

## 正文

# Nicsilver/roam

GPS speedometer for Android built around OLED burn-in avoidance

- Stars: 4
- Forks: 0
- Watchers: 4
- Open issues: 0
- License: GNU Affero General Public License v3.0
- Default branch: main
- Created: 2026-07-31T18:28:29Z

## Languages

- Kotlin

## Top Contributors

- Nicsilver (8 contributions)

---

## README

# Roam

A GPS speedometer for Android that treats your OLED with respect.

Feature graphic

Most people who want a speed readout in the car just open Google Maps and leave it on. That works, but hours of a bright, static UI is exactly how OLED panels burn in. Roam shows one thing, your current GPS speed, on a pure black screen, and is built from the ground up to leave no trace on your panel.

## How it protects your screen

- **The readout moves.** Every few minutes (1 to 10, your choice) the speed display glides to a new position. Positions are chosen so consecutive spots land far apart and the whole screen gets used evenly over a drive.
- **Pure black background.** On OLED, black pixels are off. Only the digits are lit.
- **Colour drift.** The digit colour slowly shifts hue so no single subpixel carries the whole load.
- **Outline digits.** Optional hollow digit style that lights a fraction of the pixels.
- **Brightness control.** Dim the display from inside the app without touching system settings.

## The rest

- Current speed in km/h or mph, plus a session max
- Screen stays awake while the app is open
- No ads, no tracking, no network access at all. The only permission is location, used for GPS speed.
- Tiny: the APK is well under 100 KB

| | | |
|---|---|---|
| Speed | Settings | Outline mode |

## Install

Grab the latest APK from Releases, or build it yourself:

```
./gradlew assembleDebug
```

Requires JDK 17+ and the Android SDK.

## Releasing

Tag a version and push it. GitHub Actions builds the signed APK and AAB and attaches them to a GitHub release:

```
git tag v1.1.0
git push origin v1.1.0
```

## License

AGPL-3.0

# Cogram Studio

## 导航

- 项目页：[[10-项目/github.com_a1bc2a2f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
