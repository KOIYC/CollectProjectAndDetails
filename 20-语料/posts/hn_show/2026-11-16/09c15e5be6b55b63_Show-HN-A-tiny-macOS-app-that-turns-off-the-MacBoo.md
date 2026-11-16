---
type: "corpus"
item_id: "09c15e5be6b55b63"
title: "Show HN: A tiny macOS app that turns off the MacBook display [free license]"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50507722"
project_url: "https://blackoutapp.io/"
author: "sliqqq"
published_at: "2026-11-15T15:37:52Z"
captured_at: "2026-11-16T10:00:05+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-11-16"
pub_day: "2026-11-15"
tags:
  - 语料
  - hn_show
  - author_sliqqq
  - story_50507722
  - show_hn
metrics: {"points": 9, "comments": 27, "engagement_velocity": 9}
comments_count: 27
comments_total: 27
discovered_via: "hn:show_hn:3d"
---

# Show HN: A tiny macOS app that turns off the MacBook display [free license]

> [!info] 一句话导读
> Hi, I made a tiny app that lets you turn off the MacBook screen when you work on external monitors.It does NOT just dim the brightness to zero, the screen is ac…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50507722>
> 指标：点赞=9 · 评论=27 · engagement_velocity=9
> 作者：sliqqq　|　发布：2026-11-15T15:37:52Z
> 项目链接：<https://blackoutapp.io/>
> 采集：2026-11-16T10:00:05+08:00　|　id：`09c15e5be6b55b63`

## 正文

Hi, I made a tiny app that lets you turn off the MacBook screen when you work on external monitors.It does NOT just dim the brightness to zero, the screen is actually turned off via the Apple hardware API, the according desktop is removed, so you have a clean "one big monitor" setup.- Safe fallback if you turn off the external monitor(s), unplug the monitor cable(s), the app crashes or anything else happens.
- Keyboard, touchpad and TouchID still work fine.
- Automatic restart. 2 Megabyte size.
- Totally niche, I know, but it helps me to concentrate.The app is commercial ($9 once), but everybody who writes me at hi@blackoutapp.io gets a *FREE* lifetime license, and everybody who uses in the feedback form (to report if the apps works on your setup) gets a free lifetime license too.Thanks ;)https://blackoutapp.io

## 评论（27/27）

> **theplumber** · 2026-11-15T16:30:30.000Z　
> But you can just close the lid? What am I missing ?

---

> **QuantumNomad_** · 2026-11-15T16:38:45.000Z　
> What guarantees that the monitor comes back on if your app crashes?

---

> **jdiff** · 2026-11-15T16:44:25.000Z　
> DMs? This site has DMs?

---

> **TekMol** · 2026-11-15T16:45:23.000Z　
> 2 Megabyte size
>
> I would have expected this to be just a few lines of code.Let's say it is 100 lines because it has a bunch of convenience or edge case handling. Lets say with an average length of 20 chars, that would be 2KB.How can it fill 1000 times of that to get to 2MB?

---

> **kxrm** · 2026-11-15T17:12:57.000Z　
> We are in the age of LLMs.https://github.com/kxrm/displayoff/blob/main/displayoff.c

---

> **pacifika** · 2026-11-16T00:24:09.000Z　
> Great idea and excellent small use case. Not sure why this is flagged.

---

> **bubblemoth** · 2026-11-15T16:38:23.000Z　
> LLM bros want to turn off The monitor but keep their LLMs running.

---

> **nsoam** · 2026-11-15T16:38:25.000Z　
> You save the 20 cents in tokens it would cost you to replicate this app.

---

> **gloxkiqcza** · 2026-11-15T16:40:01.000Z　
> > Keyboard, touchpad and TouchID still work fineIn case you close the lid those no longer work I suppose.

---

> **harikb** · 2026-11-15T16:40:03.000Z　
> My guess would be that it allows continued use of other things like finger-print sensor, or possibly camera?Mac also cannot run with lid closed if power is not connected, but I am not sure if it will power display-out when power is not there.

---

> **mfro** · 2026-11-15T16:49:50.000Z　
> Yeah uh, you can just lower the brightness to minimum and the display turns off

---

> **sliqqq** · 2026-11-15T16:59:23.000Z　
> You cannot use the keyboard anymore when you close the lid ;)
> I think you misunderstood what the app does

---

> **sliqqq** · 2026-11-15T17:04:54.000Z　
> the app watches itself. when it crashes, it closed or anything else happens that is not the intended state, the display is reset.beside this, it's also reset to on-status by macOS itself after restart (however you can turn it off again by auto-starting the app)

---

> **sliqqq** · 2026-11-15T17:05:17.000Z　
> Sorry, you are correct, i've corrected my mistake and put an email adress into the text

---

> **sliqqq** · 2026-11-15T16:58:36.000Z　
> Hi, that's the images (retina-ready), and other things that are necessary to create a Swift application in macOS that complies with Apple's developer requirements (the app is signed by Apple btw). The Apple Silicon build itself is around 800kb, the Intel build adds stuff up to 2 MB.I thought at this size it's okay to put everything into one file, rather than release different builds for Intel and Silicon.

---

> **ranger_danger** · 2026-11-15T17:14:16.000Z　
> 404

---

> **sliqqq** · 2026-11-15T17:30:58.000Z　
> This is literally like saying "Dropbox is just a remote server, you could easily rent your own, install rsync, and that's it."
> You would be technically totally correct. But there is a reason people use Dropbox and pay money for it. Convenience is value.Also, I think you dont fully understand what this app does. Your script is dramatically underestimating the complexity of keyboard, TouchID, cables, Intel vs. Silicon, the Intel bugs, the M3 model hardware API bugs, the logic behind closing/opening, plugging and unplugging, complex scenarios, restarts, UI, translations etc.The app has even price parity, meaning people in less developed countries pay much much less for it. There's no reason to make the life of people harder who just sell something tiny for a price of a coffee, and on top even give it away for free during testing phase.Use your skill to build alternatives of big shady corporate software, not harming indie devs.

---

> **jdiff** · 2026-11-15T16:44:04.000Z　
> This only works with an external monitor.

---

> **sliqqq** · 2026-11-15T17:23:46.000Z　
> Building this app took me 2 weeks, and testing and bugfixing many different scenarios on many different devices, monitor types, cables types and port types took me 1 week and many many grey hairs.Software is still not just writing a promt and boom there is is. It's a a long process of trial and error, QA, bugfixing, reacting on user feedback etc.Not everybody who uses software is a software engineer and has time and nerve and skill to build everything by themselves.Also, I give away the app for free currently (in exchange for a simple device test feedback), so I would argue that this is way cheaper and quicker than building it by yourself.We should encourage each other to build software, not talking every new software down with the "you could easily vibecode this by yourself"

---

> **sliqqq** · 2026-11-15T17:08:20.000Z　
> i tried to explain that in the post's text: it turns off the internal diplay, but doesnt touch anything else. so, of course you can close the lid, but then your mac is closed and you cannot use the keyboard, cam or touchid anymore.The core concept is to turn off the screen and actually remove the (software) desktop of this screen temporarely. This might sound odd, but there are valid use cases.I built the app because in my bubble this functionality was requested often ;)

---

> **sliqqq** · 2026-11-15T17:09:35.000Z　
> no, this lowers the brighness, it does not turn off the screen or the software desktop of this screen

---

> **kxrm** · 2026-11-15T17:16:08.000Z　
> fixed

---

> **kxrm** · 2026-11-15T17:48:46.000Z　
> Can you honestly say you didn't use an LLM to write your app?> Also, I think you dont fully understand what this app does.I honestly do not care what your app does. There were people in the comments trying to understand how it worked, so I vibe coded this. I have no interest in competing with your app.> Use your skill to build alternatives of big shady corporate softwareI do, but I also don't keep simple concepts draped behind paywalls.

---

> **ranger_danger** · 2026-11-15T16:48:26.000Z　
> sudo pmset -a disablesleep 1does not require an external monitor

---

> **sliqqq** · 2026-11-15T18:00:49.000Z　
> What? the app was of course built with usage of AI, this is industry standard. Nobody writes code character by character by hand anymore. Software engineering is not "coding" alone.I also get strong reddit moderator personality vibes from you.

---

> **sliqqq** · 2026-11-15T17:02:42.000Z　
> you are correct, but misunderstand what the app does.- it does: lid open, screen off, keyboard works, touchid works, touchbar works.
> - difference to just dimming the screen: it actually removes the display/desktop, so you really jsut have one big monitor (or multiple). this is useful for some people.
> - it watches the displays, and if the monitor is turned off, unplugged etc. the internal display turns on again

---

> **jdiff** · 2026-11-15T17:10:55.000Z　
> This app only works with an external monitor*It has nothing to do with LLMs. Or disabling sleep.

## 关联链接

- https://blackoutapp.io

## 导航

- 项目页：[[10-项目/blackoutapp.io_3ac2f0cb]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
