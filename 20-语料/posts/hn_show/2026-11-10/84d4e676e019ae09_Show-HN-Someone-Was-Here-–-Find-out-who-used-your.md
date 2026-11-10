---
type: "corpus"
item_id: "84d4e676e019ae09"
title: "Show HN: Someone Was Here – Find out who used your Mac while you were away"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50429812"
project_url: "https://someonewashere.app/"
author: "4onthefloor124"
published_at: "2026-11-09T18:50:56Z"
captured_at: "2026-11-10T10:03:37+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-11-10"
pub_day: "2026-11-09"
tags:
  - 语料
  - hn_show
  - author_4onthefloor124
  - story_50429812
  - show_hn
  - front_page
metrics: {"points": 61, "comments": 24, "engagement_velocity": 61}
comments_count: 24
comments_total: 24
discovered_via: "hn:show_hn:3d"
---

# Show HN: Someone Was Here – Find out who used your Mac while you were away

> [!info] 一句话导读
> Many thanks to my ex for inspiring my new MacOS app, Someone Was Here.It takes a photo of whoever uses your Mac while you're away, whether you left it unlocked …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50429812>
> 指标：点赞=61 · 评论=24 · engagement_velocity=61
> 作者：4onthefloor124　|　发布：2026-11-09T18:50:56Z
> 项目链接：<https://someonewashere.app/>
> 采集：2026-11-10T10:03:37+08:00　|　id：`84d4e676e019ae09`

## 正文

Many thanks to my ex for inspiring my new MacOS app, Someone Was Here.It takes a photo of whoever uses your Mac while you're away, whether you left it unlocked or they know your password, and sends their photo to your iPhone if the face isn't yours.I built Someone Was Here as a menu bar app making use of Apple Vision and a local face recognition run via Core ML. It all runs locally on your Mac with no tracking or ads.Real-time remote alerts are available via one-time $4.99 lifetime purchase via the free companion iPhone/iPad app, Pushover, ntfy, Telegram or a webhook.

## 评论（24/24）

> **ludsan** · 2026-11-09T19:41:32.000Z　
> > Many thanks to my ex for inspiring my new MacOS appstory implied?

---

> **thisislife2** · 2026-11-09T19:59:36.000Z　
> Nice idea.> Real-time remote alerts are available via one-time $4.99 lifetime purchase via the free companion iPhone/iPad app, Pushover, ntfy, Telegram or a webhook.Instead of making users download 2 apps (one on the Mac and one on the iPhone), you should instead consider sending the alert by email (through Mail extensions) and / or iMessage (iMessage Extensions) - you can still charge for it.

---

> **hyperjeff** · 2026-11-09T20:02:31.000Z　
> Ads for spyware on HN. Is the goal entrapment instead of proper account boundaries?

---

> **nikolay** · 2026-11-09T21:50:35.000Z　
> How about the free DND (DoNotDisturb) [0] by Objective See foundation?[0]: https://objective-see.org/products/donotdisturb.html

---

> **alentred** · 2026-11-09T22:00:59.000Z　
> I understand that the objective is to, pardon the language, detect the "creeps", but somehow the app itself feels creepy, too :/ Somehow I wouldn't feel comfortable even installing it. Not to mention my own privacy concerns.

---

> **cadamsdotcom** · 2026-11-09T22:15:01.000Z　
> This is so weird.Like, ...Lock your laptop when you stand up??Why would anyone know your password? If they do, change it.This advice is available for the low low price of $4.99/month.

---

> **_ks3e** · 2026-11-09T22:56:08.000Z　
> I look forward to a barrage of alerts with cat pictures.

---

> **4onthefloor124** · 2026-11-09T19:50:06.000Z　
> Oh yes...some relationships end in closure, others end in software.

---

> **4onthefloor124** · 2026-11-09T20:26:52.000Z　
> Fair suggestion! The real-time remote alerts are optional.The companion app gives you encrypted delivery through your own iCloud account without involving my servers, but I can see the appeal of email. For anyone comfortable wiring things together, there’s also a built-in MCP server alongside webhooks, so there’s plenty of room for custom integrations.

---

> **keyringlight** · 2026-11-09T22:38:00.000Z　
> Wouldn't messages syncing to all devices, which might be a concern if you wanted the detection to be covert and only get alerts on a devices you can trust to be on your person? i.e. the 'unrecognized person' won't see a new email coming in to tell them they've been spotted and prompt then to cover their tracks.

---

> **4onthefloor124** · 2026-11-09T20:19:17.000Z　
> The goal is an audit trail of someone trying to use your Mac, including at the lock screen. Much like a doorbell camera or home security system. It complements proper account boundaries.There's nothing hidden about the app. It sits visibly in the menu bar, and the camera light comes on whenever it takes a photo. Face recognition happens locally. Photos stay on your Mac unless you enable an alert destination. They never touch my server. No ads or tracking. I built it how I would want an app to function from a privacy standpoint.

---

> **kube-system** · 2026-11-09T22:25:39.000Z　
> spyware is by definition capturing information from someone else's computer

---

> **4onthefloor124** · 2026-11-09T22:29:11.000Z　
> DND is a valid alternative! There's definitely overlap, including photo alerts. DND's detection is based on opening a MacBook's lid.Someone Was Here also detects activity after idle, lock-screen interaction, and unlocks, so it covers an already-open laptop or a desktop Mac that has no "lid" as well.It also recognizes your face locally to suppress alerts about yourself, and offers a multiple remote alert options, Shortcuts actions with Siri phrases, a webhook for integration, and an MCP server for agents.

---

> **4onthefloor124** · 2026-11-09T22:24:58.000Z　
> I felt pretty violated when someone went through my Mac and personal data without my knowledge which is why I created this app. I see this much like a home security system with cameras: a way to know when someone accesses your space.The app runs sandboxed, doesn't have access to your personal files, and meets Apple's privacy requirements as well as my own. That said, not everyone will be comfortable with it, and that's fine.

---

> **4onthefloor124** · 2026-11-09T22:30:44.000Z　
> Locking your Mac is good advice. This also records someone trying to use it while it's locked.A lock prevents access; an audit trail tells you someone tried. Same reason people have both door locks and security cameras.And to clarify the pricing: the Mac app and local history are free. Remote alerts are $4.99 once, not per month.

---

> **judge2020** · 2026-11-10T00:53:18.000Z　
> Ctrl-command Q (and Win+L for Linux/Windows) is instinct at this point for me.

---

> **ostacke** · 2026-11-09T20:03:24.000Z　
> Maybe in Clojure, even

---

> **4onthefloor124** · 2026-11-09T22:45:41.000Z　
> To this point, the app holds its own desktop notification until it recognizes your face again, and only then tells you who came by. Remote alerts are instant.

---

> **mahboi** · 2026-11-09T22:50:03.000Z　
> Where is your Mac sitting that random people go through it? And it stays unlocked? My family had a shared iMac when I was a kid, but people still had their own accounts. Some of us may have known one or more other users' passwords, plus I had sudo, but that still prevented random people from going on.

---

> **lakeviewterrace** · 2026-11-10T00:53:27.000Z　
> Or you could just buy a Yubikey

---

> **pizzly** · 2026-11-10T00:50:18.000Z　
> I guess it could help determine physical tampering. While you lock your computer, someone could stick something on the laptop or inside it such as a microphone, location tracker etc. That app will help for that type of situation. Perhaps unlikely situation but still within the realm of possibility.Also could be cool to see if your "friends" + "family" try to access your locked computer.

---

> **DANmode** · 2026-11-10T00:51:32.000Z　
> Slick!

---

> **Scarbutt** · 2026-11-10T00:20:36.000Z　
> He's is Mr. Nice Guy, gives his passwords to everyone but someone violated him.

---

> **saagarjha** · 2026-11-10T01:49:04.000Z　
> This is an extremely disrespectful and ignorant position to take in the context of domestic abuse.

## 导航

- 项目页：[[10-项目/someonewashere.app_3b1b1624]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
