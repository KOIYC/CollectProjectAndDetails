---
type: "corpus"
item_id: "700161923f7c4d2e"
title: "Show HN: Carrier-Explode: iPhone, Pixel and Galaxy carrier settings decoded"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50024499"
project_url: "https://carrierexplode.com/"
author: "simplyalec"
published_at: "2026-10-09T18:10:55Z"
captured_at: "2026-10-10T09:53:50+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-10"
pub_day: "2026-10-09"
tags:
  - 语料
  - hn_show
  - author_simplyalec
  - story_50024499
  - show_hn
  - front_page
metrics: {"points": 215, "comments": 26, "engagement_velocity": 215}
comments_count: 26
comments_total: 26
discovered_via: "hn:show_hn:3d"
---

# Show HN: Carrier-Explode: iPhone, Pixel and Galaxy carrier settings decoded

> [!info] 一句话导读
> Showing off carrier-explode, one of my side projects that continuously archives carrier settings for all major phone brands.carrier-explode also contains decode…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50024499>
> 指标：点赞=215 · 评论=26 · engagement_velocity=215
> 作者：simplyalec　|　发布：2026-10-09T18:10:55Z
> 项目链接：<https://carrierexplode.com/>
> 采集：2026-10-10T09:53:50+08:00　|　id：`700161923f7c4d2e`

## 正文

Showing off carrier-explode, one of my side projects that continuously archives carrier settings for all major phone brands.carrier-explode also contains decoders and explanations for all the common baseband configurations, etc.There’s still quite a bit of work to be done in checking my assumptions, but the tool has already been proven useful for a few enthusiast groups.

## 评论（26/26）

> **mrweasel** · 2026-10-09T18:49:39.000Z　
> Not really sure what to do with the information, but I love the UI.

---

> **dorianmariecom** · 2026-10-09T18:50:51.000Z　
> very interesting here is my carrier for instance https://carrierexplode.com/ios/carriers/Free_fr/72.0/setting...

---

> **tylergetsay** · 2026-10-09T18:58:56.000Z　
> Reminds me of the CDMA days when the qualcom software got leaked

---

> **seba_dos1** · 2026-10-09T19:14:34.000Z　
> It would be great to contribute whatever's applicable to https://gitlab.gnome.org/GNOME/mobile-broadband-provider-inf...

---

> **ahmedfromtunis** · 2026-10-09T19:26:34.000Z　
> Are these configs read-only on the phone or is it possible to manipulate them using the data here to de/activate any service?

---

> **mycofunguy** · 2026-10-09T19:27:53.000Z　
> What do you use the info you have gathered for? It seems comprehensive but curious as to how you use it?

---

> **isomorphic** · 2026-10-09T19:42:14.000Z　
> I saw this linked from MacRumors during the AT&T iPhone 18 Pro Max lockup news discussions. It was interesting to see what AT&T/Apple did to try to get ahead of the issue. So far it looks like they disabled 5G Standalone mode, possibly just to prevent a bug from literally destroying the hardware (possibly only on one batch of phones).Apple/AT&T still haven't released any kind of statement addressing the issue other than to replace affected hardware.

---

> **etatester** · 2026-10-09T19:48:36.000Z　
> This is super cool. Particularly for the fact that it just showed my country's operators rather than the usual America First.

---

> **denysvitali** · 2026-10-09T20:11:46.000Z　
> What's more useful, or at least was a while ago, is the CA combos list - basically showing which bands can be aggregated and how.A while ago I built a decoder for that (Qualcomm only!), it was fun and helped me improve the support of my device for my carrier.https://github.com/denysvitali/ca-combos-editor

---

> **tantalor** · 2026-10-09T21:34:08.000Z　
> How did you build the UI? Is it custom?

---

> **roundup** · 2026-10-09T22:19:21.000Z　
> Can I use these settings to disable incoming calls? Does GrapheneOS have this option at the android level?

---

> **arslan9063** · 2026-10-10T01:01:53.000Z　
> bro this is neat

---

> **jakobdabo** · 2026-10-10T01:29:17.000Z　
> I wonder which field is responsible for disabling the Personal Hotspot feature? About a year ago mine suddenly got disabled in the phone's UI. Since then, the only time it got enabled was when I was traveling and using a travel eSIM.It's sad that phone companies allow carriers such anti-user things.

---

> **rustcleaner** · 2026-10-10T01:37:26.000Z　
> Nice! Thank you for this public service. Phone makers & carriers should be ashamed of themselves for hiding such important configuration behind proprietary formats. If you [lurker] are a decision maker who decided to make our world this way: for shame, for shaaame!

---

> **mjhagen** · 2026-10-09T19:58:30.000Z　
> Very early-2000s

---

> **willio58** · 2026-10-09T23:56:08.000Z　
> Also interested in this - what does this information unlock?

---

> **simplyalec** · 2026-10-09T19:57:16.000Z　
> will look into this :)

---

> **KetoManx64** · 2026-10-10T01:03:08.000Z　
> Probably not a good idea if you used AI in any way to help with obtaining this info, they will ban you at the tiniest whif of you using AI

---

> **flotzam** · 2026-10-09T19:35:32.000Z　
> Depends on the OS. GrapheneOS can override a bunch of them: https://grapheneos.org/usage#carrier-settings-overrides

---

> **simplyalec** · 2026-10-09T19:56:47.000Z　
> You can trick iOS into running different bundles for your carrier up until the most recent beta (just fixed)A very common thing to do in Russia for instance where WiFi calling isn’t available: https://github.com/ios-bundles/CarrierSIM

---

> **simplyalec** · 2026-10-09T22:50:58.000Z　
> plain old CSS w/ svelte (and their new-ish remote functions)!

---

> **KetoManx64** · 2026-10-10T01:25:27.000Z　
> No, but you can automate rejecting an incoming call with Tasker

---

> **mitxela** · 2026-10-10T01:31:42.000Z　
> Did you buy your phone through the carrier?There are apps that can act as a SOCKS proxy for limited hotspottivity. Probably mostly on Android.

---

> **chiefwilsion** · 2026-10-10T00:17:45.000Z　
> nerd tier 8. and after that you get nerd tier 9

---

> **mitxela** · 2026-10-10T01:33:32.000Z　
> Best is to contribute the info, make sure it's accurate, and if they ban someone for contributing accurate info, let them.GNOME is a circus.

---

> **jakobdabo** · 2026-10-10T01:32:03.000Z　
> > Did you buy your phone through the carrier?No.

## 导航

- 项目页：[[10-项目/carrierexplode.com_623cc6d8]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
