---
type: "corpus"
item_id: "1500b913fdf16b6d"
title: "Show HN: Turn a UniFi Protect relay and sensor into a smarter garage door"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49868392"
project_url: "https://garageopener.app/"
author: "pcrausaz"
published_at: "2026-09-27T16:49:56Z"
captured_at: "2026-09-28T09:47:28+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-28"
pub_day: "2026-09-27"
tags:
  - 语料
  - hn_show
  - author_pcrausaz
  - story_49868392
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Turn a UniFi Protect relay and sensor into a smarter garage door

> [!info] 一句话导读
> Skip to content Garage Opener FAQ Self-hosting Support Français

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49868392>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：pcrausaz　|　发布：2026-09-27T16:49:56Z
> 项目链接：<https://garageopener.app/>
> 采集：2026-09-28T09:47:28+08:00　|　id：`1500b913fdf16b6d`

## 正文

Skip to content Garage Opener FAQ Self-hosting Support Français
 Works with UniFi Protect Your garage door, finally on your phone.
You already have a UniFi Protect console, a relay wired to the opener and a sensor on the door.
 Garage Opener turns those into a proper smart garage door, on your iPhone, your Apple Watch, your Lock
 Screen and in Siri. No hub. No subscription. No Home Assistant.
How it works
The sensor decides, not the app
Most garage integrations fire the opener and then assume. This one doesn't. Every command is verified
 against the door sensor before the app tells you it worked, so open means the door is open,
 not that a relay clicked. When the door doesn't do what it was asked, you get told, clearly.
Two ways to connect
 You pick one during setup, and you can change your mind later.
 Straight to your console
The app talks to UniFi Protect on your home network. Nothing else to install, nothing else to keep
 running. The simplest setup, and the right one for most people.
Alerts come from the optional cloud service, below.
Through your own bridge
A small container on a NAS, a Pi or any box with Docker. It holds one connection to the console and
 runs the alert rules itself, whether or not a phone is awake. It also adds an activity log you can
 export and Shortcuts that work reliably in the background.
Alerts run on the bridge, so no Garage Opener service is involved.
 Self-hosting guide
Being told the door is open
Three rules, the same either way: the door has been open too long, it's still open at your nightly
 check time, or a car is in the garage with the door up. A hold keeps it quiet when you leave it open on
 purpose. Where those rules run is the one real difference between the two setups.
With a bridge , they run on the bridge, on your own hardware, around the clock. The app
 shows them whenever it is running or refreshing in the background. For a notification that reaches a
 phone that is asleep or away from home, point the bridge at ntfy ,
 your own or ntfy.sh.
Without one , the app can only watch the door while it is running, which is no good for
 a door left open at 2am. So there is an optional keyless service you can switch on:
Turn on Cloud alerts in the app. It creates an anonymous install on
 alerts.garageopener.app and hands you a private webhook address. No account, no email, no password.
Paste that address into two Alarm Manager rules on your console, one for the sensor opening and one
 for it closing. The app shows you the address and walks you through it.
Your console posts an event when the door moves. The service starts a timer and pushes you a
 notification if a rule fires, in English or French, with buttons on it.
The service never holds a credential to your console , so it cannot open or close
 anything, and it never receives images or your Protect API key. It keeps the event type, the sensor
 id and the time, for seven days. Tapping Close now on a notification is carried out by the
 app itself, over your own connection.
 Exactly what is stored .
The app has the current, detailed version of this setup built into it, including the Alarm Manager
 screens. Follow it there rather than here if the two ever disagree.
Everyone at home, without handing out secrets
The usual way to give a partner access to something like this is to send them the password. Here you
 don't. From the Family screen you create a one-time invite, they scan the code or tap the link, type
 their name, and they're in. It takes about fifteen seconds and they never see your token.
Invites are single use and expire after fifteen minutes.
 You see everyone who has joined, when they last used it, and you can rename or revoke any of them on the spot.
 The activity log records who opened the door by name, not by device.
 Revoking a phone takes effect immediately, which matters when one gets lost.
 What you actually get
 Everywhere you'd want it. iPhone, Apple Watch, widgets, Control Center, the Action Button, Siri and Shortcuts.
 A Live Activity while the door is open , with a Close button right on the Lock Screen.
 Arriving home gets you a notification with an Open button. Nothing ever opens by itself.
 Stop part-way , and the next press goes the way you expect.
 An activity log you can filter and export, when you run the bridge.
 English and French , throughout, including the notifications.
Try it before you wire anything
Demo mode runs the whole app against a simulated door, with travel time, a sensor and the alert rules.
 No console, no credentials, no hardware. It's the same mode App Review uses.
What you need
 Part Notes
 A UniFi Protect console Tested on Protect 7.2.x. A UDM, Cloud Key or Dream Machine, anything that runs Protect and offers an integration API key.
 A relay with an output set to Pulse Wired across your opener's push-button terminals, exactly like the wall button.
 An all-in-one sensor, mounted as Garage This is the part that makes it honest. It's what reports whether the door is really open.
 An iPhone on a recent iOS Apple Watch optional.
Configuring the relay and sensor in Protect is covered in the
 guide . The relay is wired like a second wall button, and the FAQ answers the
 questions people actually hit, starting with why the relay seems to "toggle".
Last updated: 2026-09-22
Home FAQ Self-hosting Support Privacy Terms Source © 2026 liqpil
 Works with UniFi Protect. Not affiliated with, endorsed by or sponsored by Ubiquiti Inc.
 “UniFi” and “UniFi Protect” are trademarks of Ubiquiti Inc.

## 导航

- 项目页：[[10-项目/garageopener.app_594b6687]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
