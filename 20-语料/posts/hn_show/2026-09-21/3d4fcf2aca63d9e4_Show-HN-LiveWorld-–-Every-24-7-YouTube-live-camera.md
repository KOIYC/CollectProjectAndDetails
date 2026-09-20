---
type: "corpus"
item_id: "3d4fcf2aca63d9e4"
title: "Show HN: LiveWorld – Every 24/7 YouTube live camera on one globe"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49762099"
project_url: "https://liveworld.info/"
author: "harisingh1612"
published_at: "2026-09-19T00:30:34Z"
captured_at: "2026-09-21T03:17:45+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-09-19"
tags:
  - 语料
  - hn_show
  - author_harisingh1612
  - story_49762099
  - show_hn
metrics: {"points": 39, "comments": 37, "engagement_velocity": 39}
comments_count: 35
comments_total: 37
discovered_via: "hn:show_hn:90d"
---

# Show HN: LiveWorld – Every 24/7 YouTube live camera on one globe

> [!info] 一句话导读
> LiveWorld — Live cameras around the world

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49762099>
> 指标：点赞=39 · 评论=37 · engagement_velocity=39
> 作者：harisingh1612　|　发布：2026-09-19T00:30:34Z
> 项目链接：<https://liveworld.info/>
> 采集：2026-09-21T03:17:45+08:00　|　id：`3d4fcf2aca63d9e4`

## 正文

LiveWorld — Live cameras around the world

### {"requestedAttributes":{"antialias":false,"preserveDrawingBuffer":false,"powerPreference":"high-performance","failIfMajorPerformanceCaveat":false,"desynchronized":false,"alpha":true,"depth":true,"stencil":true,"premultipliedAlpha":true},"statusMessage":"Could not create a WebGL context, VENDOR = 0x1d0f, DEVICE = 0x1111, Sandboxed = no, Optimus = no, AMD switchable = no, Reset notification strategy = 0x0000, ErrorMessage = BindToCurrentSequence failed: .","type":"webglcontextcreationerror","message":"Failed to initialize WebGL"}

```
Error: {"requestedAttributes":{"antialias":false,"preserveDrawingBuffer":false,"powerPreference":"high-performance","failIfMajorPerformanceCaveat":false,"desynchronized":false,"alpha":true,"depth":true,"stencil":true,"premultipliedAlpha":true},"statusMessage":"Could not create a WebGL context, VENDOR = 0x1d0f, DEVICE = 0x1111, Sandboxed = no, Optimus = no, AMD switchable = no, Reset notification strategy = 0x0000, ErrorMessage = BindToCurrentSequence failed: .","type":"webglcontextcreationerror","message":"Failed to initialize WebGL"}
    at Yo._setupPainter (https://liveworld.info/assets/maplibre-Dgf9cLD9.js:803:119422)
    at new Yo (https://liveworld.info/assets/maplibre-Dgf9cLD9.js:803:97323)
    at https://liveworld.info/assets/Globe-D9JYX6ac.js:1:1306
    at rc (https://liveworld.info/assets/index-BRxbV4IG.js:41:24259)
    at As (https://liveworld.info/assets/index-BRxbV4IG.js:41:42369)
    at https://liveworld.info/assets/index-BRxbV4IG.js:41:40687
    at C (https://liveworld.info/assets/index-BRxbV4IG.js:26:1568)
    at MessagePort.Q (https://liveworld.info/assets/index-BRxbV4IG.js:26:1931)
```

💿 Hey developer 👋

You can provide a way better UX than this when your app throws errors by providing your own `ErrorBoundary` or `errorElement` prop on your route.

# wcagent — AI coding with local tools and verifiable results

## 评论（35/37）

> **harisingh1612** · 2026-09-19T00:55:01.000Z　
> hey HN, hari here. built this over the last 2 weeks solo. figured id share now since HN weekend crowd is a good stress test.the idea came from wanting a way to drop into somewhere on earth and see whats happening right now. youtube has thousands of 24/7 live streams (nature, transit, airport aprons, urban corners) but theyre scattered across a million channels so nobody finds them. so i put them on a globe.currently 641 cams across ~60 countries. tap a marker, video plays inline, per-camera chat so you can see who else is watching the same view. free, no login needed to watch, no ads, no tracking.stack: laravel + reverb websockets + postgres, maplibre globe with osm tiles, runs on a $10 tokyo vps. discovery is youtube data api cron on 200+ keywords + admin divisions, plus scraping the internal youtube search bypass for keyword combos api search misses. currently at 6% of the free youtube api quota.thin spots in coverage: africa, small towns anywhere, central asia, pacific islands. if you know good 24/7 cams that arent geo-blocked, either drop the url here or use the submit button on the bottom left of the site. i approve within a day.open to feedback on the map ux, discovery, whatever. happy to answer stack questions too.

---

> **Vakaiser** · 2026-09-19T01:48:36.000Z　
> https://liveworld.info/cam/seattle-sea-otterStarted watching the Sea Otters in the Seattle Aquarium. 10/10 would 'awww' again.

---

> **senordevnyc** · 2026-09-19T01:53:35.000Z　
> Missing this one: https://www.youtube.com/live/ydYDqZQpim8?si=YfuIXAI7N-zy_XTv

---

> **defrost** · 2026-09-19T02:02:33.000Z　
> Every is a bold claim. Aspirational. Good luck going forward filling them all in.There's a fair few missing from Australia (easily more than 8 24/7 live cameras in Oz). eg: The Kings Canyon Waterholes in Watarrka National Park. (mostly dawn and dusk action)

---

> **xnx** · 2026-09-19T02:36:19.000Z　
> A comprehensive site like this would be great. This cam is plotted in Chicago which is incorrect: https://liveworld.info/cam/deshler-ohio-usa-live-train-camer...Some pins also seem stacked exactly on top of one another, making them inaccessible (e.g. Chicago).I've also got a list of 160 live YouTube cam streams with coordinates if you want me to send them somewhere.

---

> **grogenaut** · 2026-09-19T02:44:17.000Z　
> the site is missing a ton of webcams, and is not great ergonomics currently.just off the top of my head:https://www.summitatsnoqualmie.com/webcams all of these are live most of the timeagreed that "every" is a bold claim. I can find more with a google search.(edit) the site doesn't even let me suggest more. oh wait it does, it'a an almost invisible link at the bottom.and man the form is annoying... url, email, catoregy, country, lat, lon... why not just right click place webcam done with it... I know where it is on a map, but this makes me go to google maps, find the lat/lon, copy them out, paste them into this other form....

---

> **tolidano** · 2026-09-19T02:56:07.000Z　
> Have you used Earthcam? It does a pretty good job of this.

---

> **dumbmrblah** · 2026-09-19T03:14:14.000Z　
> You have Toronto, Ontario under Ontario Airport in California. As well as Hamptons Cam in Long Beach, I think.

---

> **s_dev** · 2026-09-19T03:18:51.000Z　
> Dublin, Ireland lists Duluth Canal Cam as a live cam which is wrong.

---

> **ceautery** · 2026-09-19T03:36:23.000Z　
> I like the idea. As others have noted, some of the map placements are wrong. For example, the Glendale Ohio cam is placed in Glendale Arizona. Easy to patch up, and a fun idea. Good job!

---

> **jedbrooke** · 2026-09-19T04:22:33.000Z　
> 23 live streams at null island [0] :)cool idea, I like the round globe too, now with 3D rendering in the browser being trivial on modern devices, there’s no excuse for choosing compromising 2D projections of the globe.[0]: https://en.wikipedia.org/wiki/Null_Island

---

> **MikeNotThePope** · 2026-09-19T04:29:19.000Z　
> Missing Lukla in Nepal. Where is the claim to be every live camera coming from? This looks like dozens, not a lot more than that.WEBCAM NEPAL LIVE: LUKLA AIRPORT - LIVE STREAMING FROM HIMALAYA LODGE LUKLA, SOLUKHUMBU, NEPAL
>  - https://www.youtube.com/live/am9KDRSZQ-0?si=IjVDTSU_IZ418fyT

---

> **Markoff** · 2026-09-19T05:44:37.000Z　
> > Everyyeah right, TIL in Czechia there are only 3 live cameras and in Slovakia and Hungary zerofound immediately one in Bratislavahttps://youtube.com/watch?v=SXt2_-luUr8what a horrible website with such claimsflagged for obvious lies in title

---

> **burello** · 2026-09-19T05:46:31.000Z　
> I like the interface. Keep building the interface. How will you monitor camera uptime? Maybe include a rating system to the camera icons.

---

> **woutr_be** · 2026-09-19T09:03:39.000Z　
> I have something similar at https://livelane.qubic-ventures.com. Started as a simple weekend project, but it’s becoming quite the headache. All sources are mainly from official government sites, which means many are very unreliable.Some have public APIs, others require registration where it takes months to hear back.I currently have about 30 ingestion scripts that more often than not break down.I then also have an iOS app, but that ships with a bundled sqlite database.

---

> **markolb** · 2026-09-19T12:09:18.000Z　
> Nice job! Would be great to watch some nature/jungle stuff realtime ;)

---

> **VCFundedGenYer** · 2026-09-19T14:03:58.000Z　
> I know for a fact we have at least 30-50 live weather cameras in my area (Windy.com shows em) and this site shows absolutely none of them.Gotta work on your discovery more.

---

> **iAMkenough** · 2026-09-19T14:36:01.000Z　
> Definitely not “every” camera by a long shot.

---

> **Todd** · 2026-09-19T01:59:39.000Z　
> Love the idea Hari. On my iPhone, when I tap a dot, it takes me straight to the camera page. I would expect a popover with a title, etc. and a second tap to go to the camera page.

---

> **CommieBobDole** · 2026-09-19T02:11:38.000Z　
> This is nice, but how are you determining the location of a camera for map purposes? Some of them are correct, but there are others that have very specific map locations that are off by as much as a hemisphere - an Ohio one in Chicago, a Venice, Italy one in San Bernardino, Pennsylvania and Ohio in Phoenix, etc.

---

> **softboyled** · 2026-09-19T02:21:37.000Z　
> Firefox' Enhanced Tracking Protection breaks the map in a weird way.
> The Map bounces up and down erratically.This message piles up in the console:Blocked https://liveworld.info from extracting canvas data because no user input was detected

---

> **harisingh1612** · 2026-09-19T02:26:09.000Z　
> ha thanks. the sea otters cam has been the personal favorite too, its up on my second monitor half the workday

---

> **harisingh1612** · 2026-09-19T02:27:13.000Z　
> in. thanks. if you spot others just drop urls, submit button is bottom-left on the site or ping me here

---

> **harisingh1612** · 2026-09-19T02:52:11.000Z　
> deshler-ohio-usa fix pushing tonight (its going into the regression fixtures alongside the ones CommieBobDole flagged). stacked-pin dedupe is a real known gap, adding a spiral offset when markers overlap at the same coords. YES please send the 160 cams. email works, hari at sapporosoft dot com, or paste a github gist here and ill ingest tonight. that gets us over 800 in one shot, huge thanks

---

> **harisingh1612** · 2026-09-19T02:52:28.000Z　
> both fair. summitatsnoqualmie ingesting tonight. submit form: youre right, its overkill. next ship is a right-click-place-marker flow, drop pin on the globe and it autofills coords + reverse-geocodes city and country. only field left is the youtube url. the invisible link is embarrassing, promoting it too. thanks for the honest read

---

> **harisingh1612** · 2026-09-19T03:01:52.000Z　
> yeah earthcam is the big one. mostly a directory of their own camera network with mixed embeds and a paid api, different product. liveworld is youtube-only which means anyone can embed anywhere and videos stay hosted on youtubes side. also free, no paywall, no login. earthcam is more comprehensive on their curated set, less good if you want to freely browse from a globe view

---

> **slacktivism123** · 2026-09-19T04:48:35.000Z　
> You're asking Claude so expect a Claudish answer.Lowercasing the text and removing a few periods does not obfuscate the fact that it is Claudespeak.And that is why most of OP's comments are being auto-flagged by HN's slop detector, which you can see if you turn on showdead.https://news.ycombinator.com/newsguidelines.html#generated

---

> **harisingh1612** · 2026-09-19T11:15:15.000Z　
> update, petrzalka cam is in and live at https://liveworld.info/cam/petrzalka-train-station-live-stre... got a proper bratislava pin now. still workin on the czechia/hungary side, next batch shd land those. thanks for the push

---

> **xnx** · 2026-09-19T15:12:27.000Z　
> Are they YouTube streams? The LiveWorld site is only YouTube streams.

---

> **harisingh1612** · 2026-09-19T02:31:46.000Z　
> good catch, thats a mobile bug. desktop hover shows the popover, tap on mobile skips it and jumps. adding a mobile-only tap-once-for-preview flow tonight. thanks

---

> **harisingh1612** · 2026-09-19T02:31:29.000Z　
> yeah those hurt. geocoder is a priority stack: pinned coords in description first, then country in title, then city in title constrained to that country, description last resort. when the description says streaming from ohio but the cam is chicago, we lose. drop the specific liveworld cam urls and ill fix them tonight and use them as regression fixtures. planning a wrong-location report button next

---

> **harisingh1612** · 2026-09-19T02:30:53.000Z　
> ah interesting, the maplibre canvas needs the tracking permission for tile prefetch and looks like ETP is rate-limiting the calls. will file this. workaround for now is toggling ETP to standard for the site or using a different browser. thanks for the console dump

---

> **harisingh1612** · 2026-09-19T17:08:28.000Z　
> yeah exactly this. and the 160-cam offer still stands whenever youre ready, hari at sapporosoft dot com works.

---

> **DANmode** · 2026-09-19T03:48:04.000Z　
> Keep making stuff.Thank you!

---

> **xnx** · 2026-09-19T23:14:09.000Z　
> Will send. I did a compare and I think about 120 you didn't have.

## 关联链接

- https://liveworld.info/assets/Globe-D9JYX6ac.js:1:1306
- https://liveworld.info/assets/index-BRxbV4IG.js:26:1568
- https://liveworld.info/assets/index-BRxbV4IG.js:26:1931
- https://liveworld.info/assets/index-BRxbV4IG.js:41:24259
- https://liveworld.info/assets/index-BRxbV4IG.js:41:40687
- https://liveworld.info/assets/index-BRxbV4IG.js:41:42369
- https://liveworld.info/assets/maplibre-Dgf9cLD9.js:803:119422
- https://liveworld.info/assets/maplibre-Dgf9cLD9.js:803:97323

## 导航

- 项目页：[[10-项目/liveworld.info_6bbfb06c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
