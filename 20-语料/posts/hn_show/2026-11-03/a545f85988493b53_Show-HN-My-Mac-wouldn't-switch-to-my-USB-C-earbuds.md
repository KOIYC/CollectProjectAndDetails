---
type: "corpus"
item_id: "a545f85988493b53"
title: "Show HN: My Mac wouldn't switch to my USB-C earbuds, so I made an app that does"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50339983"
project_url: "https://github.com/ishanray/AudioAutoSwitch"
author: "ishanr"
published_at: "2026-11-02T17:09:29Z"
captured_at: "2026-11-04T10:05:48+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-03"
pub_day: "2026-11-02"
tags:
  - 语料
  - hn_show
  - author_ishanr
  - story_50339983
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: My Mac wouldn't switch to my USB-C earbuds, so I made an app that does

> [!info] 一句话导读
> ishanray/AudioAutoSwitch

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50339983>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：ishanr　|　发布：2026-11-02T17:09:29Z
> 项目链接：<https://github.com/ishanray/AudioAutoSwitch>
> 采集：2026-11-04T10:05:48+08:00　|　id：`a545f85988493b53`

## 正文

# ishanray/AudioAutoSwitch

Mac menu bar app that switches sound to your USB-C headphones when you plug them in. Made for the Bose Noise Cancelling Wired Earbuds.

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-10-17T00:41:28Z

## Languages

- Shell
- Swift

## Topics

- audio
- bose
- macos
- menu-bar
- menubar-app
- swiftui
- usb-c
- usb-headphones

## Top Contributors

- ishanray (3 contributions)

---

## README

# Audio Auto Switch: make your Mac play through USB-C headphones when you plug them in

A small, free menu bar app for macOS. When you plug in your USB or USB-C headphones, it switches your Mac's sound output to them.

I made it for my **Bose Noise Cancelling Wired Earbuds (USB-C)**. When I plugged them into my MacBook Pro, the microphone switched over but the sound kept coming out of the speakers, so I had to open Sound settings every time. With this app, the sound moves to the earbuds when I plug them in.

It works with any audio device you can plug in, such as USB-C earbuds, USB headsets, USB DACs, and docks with a headphone jack.

## Does this fix your problem?

It's for you if one of these happens on your Mac:

- You plug in your Bose wired earbuds (or other USB-C earbuds) and there's no sound in them. It keeps playing from the MacBook speakers.
- The USB-C headphones' microphone works on your Mac, but the sound doesn't.
- Your Mac doesn't switch to USB headphones on its own, so you have to change the output in System Settings → Sound every time.
- Your USB headset, USB DAC, or dock's headphone jack isn't picked as the sound output when you connect it.

## How to use it

1. Open the app. A headphones icon appears in the menu bar.
2. Plug in your headphones.
3. Click the icon and tick your headphones.

From then on, your Mac plays through them whenever you plug them in. When you unplug them, macOS goes back to your speakers like it normally does.

Turn on **Open at Login** in the same menu so you don't have to start the app yourself.

## Install

**Download Audio Auto Switch**

Unzip it, drag **Audio Auto Switch** into Applications, and open it. The app is signed and notarized by Apple.

Requires macOS 13 Ventura or later. Runs on Apple silicon and Intel Macs.

### Build from source

You need Xcode or the Xcode Command Line Tools.

```sh
git clone https://github.com/ishanray/AudioAutoSwitch.git
cd AudioAutoSwitch
./scripts/build-app.sh
open build
```

To make a signed and notarized release, sign in to your Apple developer account in Xcode → Settings → Accounts, then run:

```sh
TEAM_ID=<your team ID> ./scripts/release.sh
```

## Why doesn't my Mac switch to USB headphones on its own?

macOS switches to the headphone jack and to AirPods, but it often keeps playing through the current output when you plug in a USB device. Apple doesn't document the rules. Other people report the same thing with USB-C earbuds, USB headsets, and docks. Picking the device once in System Settings → Sound fixes it for some people. This app is for when it doesn't.

## How it works

The app listens for Core Audio device changes. When one of your ticked devices connects, it becomes the output for sound and for alerts. Devices are remembered by their unique ID, so two pairs of the same headphones are tracked separately.

It has no network access and collects nothing. All the code is in `Sources/AudioAutoSwitch`.

## License

MIT

## 关联链接

- https://github.com/ishanray/AudioAutoSwitch.git

## 导航

- 项目页：[[10-项目/github.com_7ff65b1f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
