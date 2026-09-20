---
type: "corpus"
item_id: "d43a40d83f7a699e"
title: "Show HN: I built a cross-browser extension that controls fingerprinting surfaces"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49124017"
project_url: "https://privacything.com/en"
author: "tomaszjanusz"
published_at: "2026-07-31T14:57:39Z"
captured_at: "2026-09-21T02:55:00+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-07-31"
tags:
  - 语料
  - hn_show
  - author_tomaszjanusz
  - story_49124017
  - show_hn
metrics: {"points": 20, "comments": 10, "engagement_velocity": 20}
comments_count: 10
comments_total: 10
discovered_via: "hn:show_hn:83d"
---

# Show HN: I built a cross-browser extension that controls fingerprinting surfaces

> [!info] 一句话导读
> Hello Hacker News! I’m Tomasz, creator of Privacy Thing, a browser extension for Firefox and Chromium-based browsers. I’ve just released its Preview version.Pri…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49124017>
> 指标：点赞=20 · 评论=10 · engagement_velocity=20
> 作者：tomaszjanusz　|　发布：2026-07-31T14:57:39Z
> 项目链接：<https://privacything.com/en>
> 采集：2026-09-21T02:55:00+08:00　|　id：`d43a40d83f7a699e`

## 正文

Hello Hacker News! I’m Tomasz, creator of Privacy Thing, a browser extension for Firefox and Chromium-based browsers. I’ve just released its Preview version.Privacy Thing aims to reduce browser fingerprinting—the tracking of users without cookies.It began as an internal project: a simple location simulator. Over time, I expanded it to cover more fingerprinting surfaces. It now has 13 protection categories affecting 50+ browser APIs and methods: Geolocation, time and locale settings, Canvas, WebGL, Audio, Navigator, Screen, Client Hints, Battery, WebRTC, Dedicated Workers, Service Workers, and Shared Workers. The list is still growing.The extension is fully configurable. Users can create regional profiles and assign them to domain rules, with separate protection settings for each domain. Or they can skip domain rules and rely on the global configuration—I’m not here to decide what works best for them :-)Privacy Thing uses Manifest V3, with all its pros and cons. Chrome and Firefox appear to offer similar extension APIs, but differ fundamentally at the level where Privacy Thing operates. This matters because its scripts must load as early as possible to be effective.Its X-Ray module communicates with scripts running in the page context to show which APIs a site uses and how often it queries them. An aggregate count appears on the extension’s toolbar badge by default.Each release includes processed, compact datasets covering Chrome build numbers, supported language codes, language-to-country mappings, popular screen resolutions, and hardware configurations. This keeps the extension independent of external services and there is no good reason to build extra infrastructure for it.There are two exceptions. The regional preset wizard uses OpenStreetMap’s Nominatim geocoding service, but only after the user consents to sending the query. Maps are displayed using OpenFreeMap.Presets can also be created manually. Users who know the coordinates can enter them directly without contacting any 3rd-party service.The extension does not transmit telemetry or usage data. This makes development harder, but it is fundamental to its identity: user data belongs to the user. Privacy Thing configuration can be exported, edited and imported.The Preview is currently distributed under a proprietary license. This is not ideal; I ultimately intend to release the source under an open-source license, most likely the AGPL.More about the development process:
https://tomaszjanusz.dev/en/projects/privacy-thing/Download:- Mozilla Addons:
https://addons.mozilla.org/en-US/firefox/addon/privacy-thing...- Chrome Web Store:
https://chromewebstore.google.com/detail/privacy-thing-previ...The extension is STILL under review in the Microsoft Edge Add-ons store -_-Thank you for your suggestions and feedback. Please remember that this is still a preview: some things may not work, may be slower, or may not behave as intended. I sincerely hope such issues will be few and far between.P.S. Yes, Privacy Thing fully supports Firefox Containers. I like the concept and believe extensions should support containers whenever possible. Privacy Thing will support them elsewhere too, including Brave, if Brave Software makes its container API public.

## 评论（10/10）

> **clonedhuman** · 2026-07-31T16:26:30.000Z　
> I find, as time goes on, that more and more sites are breaking over relatively minimal privacy protections in my browser.

---

> **gruez** · 2026-07-31T16:55:52.000Z　
> Anti-fingerprinting measures with configurable knobs is always going to be a risky proposition because those options themselves end up being a fingerprinting surface. It's better to take firefox/tor browser's approach and have a common profile eg. "resistfingerprinting" to get crowd anonymity.

---

> **m00dy** · 2026-07-31T17:31:46.000Z　
> There's a business value if you implement your patches on C++/source code level.

---

> **mtweak** · 2026-07-31T17:40:51.000Z　
> Have you thought of active fingerprint pollution? Mathematically, find the search term that has the farthest embedding + noise than your current search term. You search for Harley Davidson, a parallel search is done for "3 mo old diapers".Like another person said: passive fingerprint protection will be limited.

---

> **xnx** · 2026-07-31T18:06:46.000Z　
> The only thing that will protect against fingerprinting is enough people connecting through some type of stock configuration virtual machine.

---

> **tomaszjanusz** · 2026-07-31T18:18:04.000Z　
> I believe that the genesis of this type of problems has several reasons:
> 1) Incorrect implementation of spoofing
> 2) a family of browser APIs whose context extensions do not (usually) have access to
> 3) the website owner decided that, for example, to fill out the form, the user must show him the RAM volume, battery charge level or graphics card manufacturer.

---

> **tomaszjanusz** · 2026-07-31T17:54:39.000Z　
> This extension does not allow you to adjust how a given patch works - for the reasons you wrote. You are 100% right. This extension allows you to configure the availability of certain spoofed surfaces for specific sites. Moreover, this extension does not try to override the protections that Firefox uses, e.g. in the case of limits on the presentation of the amount of available RAM.Your opinion is completely correct if we assume that most users will use Tor Browser. However, it is 2026, and it does not seem that Firefox will regain its position on the market. The idea behind this extension is to provide very basic (relative to what the browser manufacturer could do - and often does not do) protection for users of mainstream browsers. I use Helium and Zen myself, depending on the context of the work I do, but I am aware that most people will reach for a browser whose manufacturer sunsetted Privacy Sandbox a year ago.

---

> **tomaszjanusz** · 2026-07-31T17:59:40.000Z　
> Thanks for this opinion. You may be right. However, I believe that this type of protection will reach a wider audience in the form of an extension written in TypeScript. If we wanted to dress this code in the form of native code, we would be talking about making a fork of one of the popular browsers. It's a big challenge and a big responsibility.

---

> **gruez** · 2026-07-31T18:50:01.000Z　
> >Moreover, this extension does not try to override the protections that Firefox uses, e.g. in the case of limits on the presentation of the amount of available RAM.This seems contradicted by the screenshots, which lists options for "time", "canvas", and "screen". Firefox's RFP has protections for all of those. Not to mention it has "protections" for APIs that don't even exist on firefox.https://developer.mozilla.org/en-US/docs/Web/API/Battery_Sta...

---

> **tomaszjanusz** · 2026-07-31T19:52:20.000Z　
> Firefox has some protections in the topics you mentioned, but it does not allow you to change things like time zone (and regional or language settings) per domain. This extension has such functions. That's what these switches are for.As I wrote - the extension does not patch something that does not exist. I didn't mention it in the main post because the 4,000 character limit was simply too limiting for me. The text entry in AMO does not tell the user this either. Thanks for capturing one screenshot, as I simply had to mix up the collection of screenshots when I updated the extension's page - in fact, under Firefox, the configuration window does not present options related to Client Hints (also unavailable on the Mozilla platform) as well as the Battery Status API.In the extension interface, you will find two places presenting protection details for those APIs with a "Not applicable" status. Configuration options for these items in the settings panel are not visible.Thanks for pointing out this screenshot, as that wasn't my intention. If you look at the screenshot of the container options, you will see the actual feature set for Firefox. I've already deleted the screenshot, sorry for the confusion.

## 关联链接

- https://addons.mozilla.org/en-US/firefox/addon/privacy-thing...-
- https://chromewebstore.google.com/detail/privacy-thing-previ...The
- https://tomaszjanusz.dev/en/projects/privacy-thing/Download:-

## 导航

- 项目页：[[10-项目/privacything.com_6278029d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
