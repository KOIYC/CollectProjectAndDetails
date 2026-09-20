---
type: "corpus"
item_id: "a545e4b4d667ed00"
title: "Show HN: Chuchu – an Android SSH Client powered by libghostty"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47948222"
project_url: "https://github.com/jossephus/chuchu"
author: "jossephus01"
published_at: "2026-04-29T13:32:13Z"
captured_at: "2026-09-21T02:52:38+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_jossephus01
  - story_47948222
  - show_hn
metrics: {"points": 4, "comments": 1, "engagement_velocity": 4}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:174d"
---

# Show HN: Chuchu – an Android SSH Client powered by libghostty

> [!info] 一句话导读
> ssh client for android based on libghostty

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47948222>
> 指标：点赞=4 · 评论=1 · engagement_velocity=4
> 作者：jossephus01　|　发布：2026-04-29T13:32:13Z
> 项目链接：<https://github.com/jossephus/chuchu>
> 采集：2026-09-21T02:52:38+08:00　|　id：`a545e4b4d667ed00`

## 正文

# jossephus/chuchu

ssh client for android based on libghostty

- Stars: 127
- Forks: 6
- Watchers: 127
- Open issues: 7
- License: MIT License
- Homepage: https://chuchu.jossephus.et/
- Default branch: main
- Created: 2026-04-11T13:52:10Z

## Languages

- C
- Kotlin
- Makefile
- Nix
- Shell
- Zig

## Top Contributors

- jossephus (168 contributions)
- salemsayed (12 contributions)
- bhoffman20 (6 contributions)
- tom-sigil (1 contributions)

---

## README

 Chuchu

 A Modern, Better, Native Android SSH client powered by libghostty

 Download Latest ·
 ChangeLog ·

---

Chuchu is a native Android SSH client powered by libghostty, a terminal-first Compose UI, and has support for both standard SSH and Tailscale SSH workflows.

### Features
- tailscale, ssh password + key authentication
- image display using libghostty's kitty image protocol support
- more than 400 themes from the official ghostty repository
- configurable accessory keys and custom terminal actions
- per-host post-connect actions that autorun a selected custom action after SSH/Mosh connects or reconnects
- encrypted local import/export backups for SSH keys and server profiles
- beautiful and working terminal renderer with fully working resize, scrollback, focus, modifier keys, mouse actions

## Status

Chuchu is in active development. I am daily driving it and improving any issues i found in the way. Join the journey and report any bugs you find. And I welcome any contributions.

### Getting Started

Checkout our releases and download the apk from there. The latest release will have the latest changes.

I don't have a personal Play Store account right now (and I can't open one because of the payment limitation in my country, feel free to contact me if you want to publish it.)

## Stack

- Kotlin + Jetpack Compose for the Android app
- Zig for native build orchestration and JNI/native bridge code
- Ghostty VT for terminal emulation
- `libssh2` + `openssl` for the current native SSH path
- Room for local data storage

### Development - Prerequisites

If you have nix installed, the following three steps will get you started

1. nix develop - will set you up with everything you will need.
2. running 'make build' will build the native code needed
3. running 'make app' will build the apk and install it in a connected device.

If you don't have nix installed, you will need

1. setup tools
- Android Studio - This will set up the needed Android SDK, Android NDK and Java runtime (JDK 17+).
- Zig 0.15.2
2. build the native library

Set `ANDROID_NDK_HOME` or `ANDROID_NDK_ROOT`, then build the JNI library for Android arm64:

```sh
zig build jni -Dtarget=aarch64-linux-android
```

That copies `libchuchu_jni.so` into `app/src/main/jniLibs/arm64-v8a/`.

3. From android studio run
```sh
./gradlew assembleDebug
```

For a manual debug APK, run the native build first, then assemble the app:

```sh
make build
cd android && ./gradlew assembleDebug
```

The APK should include `lib/arm64-v8a/libchuchu_jni.so`; without it native SSH/key generation will fail on device.

## Inspiration

I have been using vvterm on iOS for the past few weeks and i really liked it. This project came from my desire to have native ssh client but for android.

## Project Name
chuchu is one of my favorite characters from the amharic book Yesinbit Kelemat [translated to colors of adios].

## Demo

## 评论（1/1）

> **KetoManx64** · 2026-04-30T01:38:22.000Z　
> Very cool to see third party projects start using libghostty

## 关联链接

- https://chuchu.jossephus.et/

## 导航

- 项目页：[[10-项目/github.com_bf18391d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
