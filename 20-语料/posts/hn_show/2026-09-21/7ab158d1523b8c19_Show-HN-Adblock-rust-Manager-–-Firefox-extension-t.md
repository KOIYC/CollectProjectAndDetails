---
type: "corpus"
item_id: "7ab158d1523b8c19"
title: "Show HN: Adblock-rust Manager – Firefox extension to enable the Brave ad blocker"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47947369"
project_url: "https://github.com/electricant/adblock-rust-manager"
author: "electricant"
published_at: "2026-04-29T12:24:53Z"
captured_at: "2026-09-21T01:42:06+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_electricant
  - story_47947369
  - show_hn
metrics: {"points": 95, "comments": 47, "engagement_velocity": 95}
comments_count: 47
comments_total: 47
discovered_via: "hn:show_hn:174d"
---

# Show HN: Adblock-rust Manager – Firefox extension to enable the Brave ad blocker

> [!info] 一句话导读
> Firefox 149 ships adblock-rust (Brave's Rust engine, MPL-2.0) completely disabled with no UI. It's controlled by two about:config prefs with no WebExtension API…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47947369>
> 指标：点赞=95 · 评论=47 · engagement_velocity=95
> 作者：electricant　|　发布：2026-04-29T12:24:53Z
> 项目链接：<https://github.com/electricant/adblock-rust-manager>
> 采集：2026-09-21T01:42:06+08:00　|　id：`7ab158d1523b8c19`

## 正文

Firefox 149 ships adblock-rust (Brave's Rust engine, MPL-2.0) completely disabled with no UI. It's controlled by two about:config prefs with no WebExtension API, so you can't touch them programmatically from a standard extension.This extension gives it a UI: ETP toggle (via browser.privacy API, instant), filter list manager with clipboard helpers for the manual about:config steps, and 8 preset lists. You can also add your own if you so desire.

## 评论（47/47）

> **kgwxd** · 2026-04-29T13:17:00.000Z　
> Don't want it. Tracker/Ad blocking should forever be an extension, maintained by someone with zero obligation to, or association with, the ad/tracking industry. A USER agent.

---

> **embedding-shape** · 2026-04-29T13:20:44.000Z　
> > Disable Firefox's built-in Enhanced Tracking Protection so adblock-rust handles blocking instead.What concrete and practical differences are there between the two? I'm guessing because this exists, adblock-rust somehow is better than the built-in ETP? In what way?I'm using ETP + uBlock Origin right now, and can't remember the last time I saw an ad, if I used this instead, what practical differences would I notice?

---

> **HelloUsername** · 2026-04-29T13:32:46.000Z　
> Relevant recent discussion: "Firefox Has Integrated Brave's Adblock Engine" https://news.ycombinator.com/item?id=47897891 25-apr-2026 248 comments

---

> **2ndorderthought** · 2026-04-29T13:42:39.000Z　
> Cool project but I have to ask. Why not use brave?

---

> **RandomGerm4n** · 2026-04-29T13:53:12.000Z　
> Can this extension effectively block ads on YouTube? When I manually enabled the Rust ad blocker in about:config and added filter lists there, ads still appeared on YouTube and some porn sites. While uBlock Origin blocks everything.

---

> **mp3geek** · 2026-04-29T13:31:00.000Z　
> The lists are maintained same as extensions.

---

> **RandomGerm4n** · 2026-04-29T14:23:02.000Z　
> One thing doesn't rule out the other. Just because a browser has a built-in adblocker doesn't mean you can't replace it with another one if it's not working well.
> Every browser should have at least a basic adblocker enabled by default. Anything else is a major security risk. In the context of web browsers ads are the main entry point for malware. Either through exploits delivered via ad banners or by tricking users into downloading something. Many search engines such as Google display fake search results that lead to infected versions of otherwise secure software. Additionally some sites offering downloads have ads disguised as download buttons that lead to something else. A browser manufacturer should try to protect its users from such things.

---

> **jasonlotito** · 2026-04-29T15:17:00.000Z　
> "https://easylist.to/easylist/easylist.txt","https://easylist.to/easylist/easyprivacy.txt","https://secure.fanboy.co.nz/fanboy-cookiemonster.txt","https://raw.githubusercontent.com/uBlockOrigin/uAssets/refs/..."These are the lists you say you do not want being used.Please explain how these lists and the people who maintain them are compromised by someone with an obligation or association with the ad/tracking industry. This would be revelatory.

---

> **celsoazevedo** · 2026-04-29T16:27:29.000Z　
> I'll keep using uBlock Origin, but I don't see having a built-in content blocker as a bad thing, especially if the lists are the same (easylist, etc). It's no different from the (very old) option to block popups.

---

> **dartharva** · 2026-04-30T03:12:29.000Z　
> The entirety of the web browser runs in userspace afaik. Whatever goes there and within is de facto a user agent.

---

> **ernesth** · 2026-04-29T13:42:10.000Z　
> I've been using ETP plus adblock-rs in Waterfox for 2 weeks. I don't see much a difference compared to ETP + ublock origin apart from some cosmetic filtering. The fact that it's not an extension supposedly allows to block at more layers so it's theoretically better than an extension (https://github.com/BrowserWorks/waterfox/issues/4182)Note that there are (were?) also some small bugs in the waterfox integration (such as the configuration options sometimes disappearing).

---

> **nathanmills** · 2026-04-30T00:33:25.000Z　
> It's memory safe

---

> **nemomarx** · 2026-04-29T13:49:13.000Z　
> You might want to not use chromium?

---

> **monegator** · 2026-04-29T14:25:52.000Z　
> why use brave, really, when you have firefox?
> I get it if you're on iOS

---

> **kuekacang** · 2026-04-29T14:34:54.000Z　
> Genuine question, does brave have ff's container extension? currently that's one of the thing that keeps holding me on ff. another big one is i test website on firefox so to not get carried away with features only available in chromium

---

> **Larrikin** · 2026-04-29T14:51:58.000Z　
> Why support Chrome at all?

---

> **Dwedit** · 2026-04-29T15:04:46.000Z　
> Some people don't like how Brave is pushing cryptocurrency.

---

> **avazhi** · 2026-04-29T15:04:55.000Z　
> Why would you use Brave when for many years it wouid surreptitiously install a VPN service on your Windows machine. The Brave devs took more than a year to even address it, let alone remove it.More ideologically, Google and Chromium are awful for the internet as monopolistic tech.

---

> **jrm4** · 2026-04-29T15:38:21.000Z　
> Their whole thing looks sketchy, frankly. I'm not saying they're evil or have some deep secret ulterior motive. But their "vision" appears to be bunch of absolutely half-baked ideas for privacy, for which Firefox has a much more boring, and consequently better, track record.

---

> **EbNar** · 2026-04-29T16:40:38.000Z　
> I do.

---

> **recursive** · 2026-04-29T16:43:59.000Z　
> I got turned off to brave with all the token stuff. Just my take.

---

> **gpm** · 2026-04-29T17:14:47.000Z　
> I care a good deal that I trust the people who developed my browser. It's about the most critical piece of software in my life. From banking to professionally to personal life.The people who developed brave used brave to impersonate people and defraud their users out of money by asking for donations using other peoples names [1]. I don't trust them at all. Thus I don't use their browser.And, unsurprisingly, this is part of a pattern of bad behavior, not a one off criminal act by otherwise trustworthy people, for some examples [2].[1] https://web.archive.org/web/20181221180137/https://twitter.c... / https://news.ycombinator.com/item?id=18734999[2] https://github.com/lobsters/lobsters-ansible/issues/45#issue... and https://lobste.rs/s/iopw1d/what_s_up_with_lobste_rs_blocking...

---

> **thesuitonym** · 2026-04-29T21:22:27.000Z　
> Brave is malware. https://www.reddit.com/user/lo________________ol/comments/1i...

---

> **dartharva** · 2026-04-30T03:10:30.000Z　
> Brave runs Sluggish and causes random temperature spikes on both Windows and Linux on my laptop like no other browser does.

---

> **antonok** · 2026-04-29T15:23:49.000Z　
> It should be able to. Waterfox is using roughly the same integration and the maintainer has been seeing reports of YouTube issues, but cannot reproduce it.
> https://github.com/BrowserWorks/waterfox/issues/4182#issueco...

---

> **thesuitonym** · 2026-04-29T21:23:03.000Z　
> If it can't, plain old ublock Origin can.

---

> **gblargg** · 2026-04-29T15:55:11.000Z　
> If browsers came with ad blocking that's enabled, it would just make those lists less effective since advertisers would have a serious incentive to work around them. I'd rather ad blocking only be used by people who care enough to install it.

---

> **RandomGerm4n** · 2026-04-29T14:35:51.000Z　
> I’m a Firefox user myself but there are some very valid arguments against it on Android as well. Firefox on Android is significantly more vulnerable to exploits, lacks internal sandboxing and doesn’t properly isolate tabs from each other.

---

> **Barbing** · 2026-04-29T14:40:39.000Z　
> Best iOS strategy that comes to mind is Safari: -iCloud Private Relay (native VPN-like thing)
>  -uBlock Origin Lite
>  -AdGuard DNS
>
> (Using fresh private tabs for small privacy gain?) Better than third-party skinned browsers right? Always happy to be informed otherwise.(AdGuard does have an option to supplant uBlock in this stack btw, does “advanced” blocking https://adguard.com/kb/adguard-for-ios/web-extension/ which is nice but trust $mm-refusing uBlock dev gorhill forever)

---

> **avazhi** · 2026-04-29T15:06:44.000Z　
> Firefox and Brave are both profoundly bad on iOS. Scrolling is a nightmare.

---

> **EbNar** · 2026-04-29T16:40:01.000Z　
> Faster.

---

> **2ndorderthought** · 2026-04-29T15:46:36.000Z　
> Containers are experimental as of very recently. So they will soon, but expect it to be in development right now.I also test on FF and I don't care much for chromium. I was just curious why the author chose to do this.

---

> **coffeeling** · 2026-05-09T12:40:29.000Z　
> Chromium has better security than Firefox, especially on mobile, where Firefox's site isolation is either nonexistent or rudimentary.

---

> **ndisn** · 2026-04-29T15:14:16.000Z　
> What’s wrong with a VPN service as long as it doesn’t route your traffic or anything.

---

> **2ndorderthought** · 2026-04-29T23:51:25.000Z　
> Wtaf? Never heard about this. I don't use any of the token stuff but that's scary stuff

---

> **2ndorderthought** · 2026-04-29T23:48:30.000Z　
> The top comment response from brave was incredibly rational. Seems like they aren't perfect but are consistent. Am I missing something?Chrome and Firefox have also both had serious issues. I'm not sure who is the best right now but it's kind of hard to vouch for any of the major browsers

---

> **Anthony-G** · 2026-04-29T15:38:27.000Z　
> This sounds like good advice so upvoted. I’m a big fan of Raymond Hill¹’s products so I am curious about how much benefit Adguard provides if uBlock Origin is already blocking online trackers, ads and other annoyances.¹ In this case, the developer – not the musician. I really liked the user interface of uMatrix.

---

> **jdmg94** · 2026-04-29T15:08:26.000Z　
> everything on iOS is just a safari skin

---

> **avazhi** · 2026-04-29T21:51:38.000Z　
> Are you wanting me to explain to you why secretly and without notifying the user that your browser is installing a new program + network service he didn’t ask for is a bad thing, or why having an extra Windows service one doesn’t use running 24/7 on top of the network stack and built into the browser is a bad thing?

---

> **lproven** · 2026-04-30T11:40:04.000Z　
> Then you haven't been listening, because it's been widely discussed and well publicised.My personal two favourite piece on Brave are these...2023:«
> Stop using Brave BrowserSeriously.Corbin Davenport07 Aug 2023
> »https://www.spacebar.news/stop-using-brave-browser/And from a couple of years later, with a very apt URL...2025:«
> Why I recommend against BraveLuca BramèMarch 24, 2025
> »https://thelibre.news/no-really-dont-use-brave/

---

> **coffeeling** · 2026-05-09T12:54:12.000Z　
> You haven't heard about it because it is a lie.Brave has a tipping service that lets users tip creators with Brave's crypto coin, BAT. When they launched the tipping service, they put out a pool of their own BAT and let users tip with that BAT. Their initial UI for the tipping app was sadly bad, and didn't really properly show which creators were signed up for the program, which weren't. If the tips from the pool were given to someone not on the program, Brave would hold them assigned to that person for 30 days, then return them to the pool. No user's resources were affected.Tom Scott gave them some harsh criticism for the UI, and Brave improved it within a couple days, resolving Scott's complaints.

---

> **thesuitonym** · 2026-04-30T13:47:52.000Z　
> Well consider that Brave and Chrome are made by for-profit companies that will stop at nothing to extract every bit of money they can from you, while Firefox is made by a non-profit that just wants to make a browser.

---

> **Barbing** · 2026-04-29T17:10:11.000Z　
> It’s really nice to have ad and tracker domains blocked systemwide though I think you need to be more careful and set your device up as supervised to have more robust blocking (real always-on VPN functionality vs. best effort?).And even then when I read about defects in Apple software that means a firewall like Little Snitch isn’t perfect (macOS) I think an external device (mobile VPN router?) is going to be essential for some threat models.(& uMatrix looks great!)

---

> **rafram** · 2026-04-29T15:39:28.000Z　
> That's not totally true. Orion supports Chrome/FF WebExtensions, for example. The engine does (practically, even in the EU) have to be WebKit, but that's not the same thing as a "Safari skin."

---

> **dadoum** · 2026-04-29T15:54:52.000Z　
> There is Reynard if you're motivated too (Gecko-based, but it's not ready for prime time yet, and to get good performance you'll have to resort to some workaround to get JIT enabled, as it does not rely on Apple's BrowserEngineKit; one of the goals of the project is giving to not up-to-date iOS devices access to a modern browser).

---

> **coffeeling** · 2026-05-09T12:33:35.000Z　
> Mozilla wants to do quite a lot more than just make a browser - for years, under Mitchell Baker, they weren't really primarily browser makers even. After she's left, Firefox has gained a new degree of focus and we've actually gotten good new features.Also Firefox is made by Mozilla Corporation, and they're funded by Google money. Firefox defaults to Google search and search suggestions on, which is an awful privacy posture.

---

> **Anthony-G** · 2026-04-29T23:02:25.000Z　
> I can see how system-wide blocking would be useful. I’m personally very conservative and wary about apps that I install on my iPhone (I don’t use any ad-supported apps) so the browser is the “attack surface” that I’m most concerned about.I already use uBlock Origin and iCloud Private Relay (as advised in your original post). I also use Private Browser tabs and regularly remove all “Website Data” from Safari (minor inconvenience in that I have to re-login to sites that I have an account on).I’ve just installed AdGuard on my iPhone to try it out but see that the DNS protection requires a Premium subscription (it now occurs to me that I could possibly install Wireguard to connect to my VPS where I’m already running my own DNS server). I’ve also `never looked into supervised mode; I always assumed it wasn’t relevant for personal devices.Thanks for the reply.

## 导航

- 项目页：[[10-项目/github.com_8e856f38]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
