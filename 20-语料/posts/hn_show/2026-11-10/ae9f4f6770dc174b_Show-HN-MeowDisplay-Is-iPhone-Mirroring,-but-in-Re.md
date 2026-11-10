---
type: "corpus"
item_id: "ae9f4f6770dc174b"
title: "Show HN: MeowDisplay Is iPhone Mirroring, but in Reverse"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50429636"
project_url: "https://meowdisplay.app/"
author: "raiseCatError"
published_at: "2026-11-09T18:39:22Z"
captured_at: "2026-11-10T09:49:42+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-10"
pub_day: "2026-11-09"
tags:
  - 语料
  - hn_show
  - author_raiseCatError
  - story_50429636
  - show_hn
  - front_page
metrics: {"points": 75, "comments": 29, "engagement_velocity": 75}
comments_count: 29
comments_total: 29
discovered_via: "hn:show_hn:3d"
---

# Show HN: MeowDisplay Is iPhone Mirroring, but in Reverse

> [!info] 一句话导读
> Hey HN and Cats, thank you for checking this out!Github:

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50429636>
> 指标：点赞=75 · 评论=29 · engagement_velocity=75
> 作者：raiseCatError　|　发布：2026-11-09T18:39:22Z
> 项目链接：<https://meowdisplay.app/>
> 采集：2026-11-10T09:49:42+08:00　|　id：`ae9f4f6770dc174b`

## 正文

Hey HN and Cats, thank you for checking this out!Github:
https://github.com/raiseCatError/meowdisplayEDIT 2: I should've mentioned that MeowDisplay started as a fork of OpenDisplay: https://github.com/peetzweg/opendisplay
which provided the foundational screen capture, virtual display, encoding and iPhone/iPad receivers. I've since taken it in a more phone-first direction, with work on the interaction, streaming and security layers. I've credited OpenDisplay and its developer Philip in the README under "Built on OpenDisplay".MeowDisplay is my take on the control your Mac from your phone scene. Available on iPhones, iPads and Macs, with Android rn in closed testing.The website has interactive illustrative demos if you'd like to see the app demonstrated.I think MeowDisplay does a few things differently, some of which I prefer and you might too.Such as Window view: allowing multiple tabs in split-screen type panes. Traditional Mirror/Extend views exist as alternatives.
Floating windows: coming in the 2.1 release.Touch input approaches: Direct Touch(Classic or Natural), experimental Smart Touch, and Trackpad mode alongside Apple Pencil support. Doesn't sacrifice display space for a trackpad, use all of the phone's screen with your preferred mode.Stage Peek: shows a scrollable and searchable list of your Mac's windows on your phone along with an app drawer when you hold and pull on the left edge of your screen.It's free and open source so you can try it and see if it's for you without having to commit to it or anything.EDIT: I've used MeowDisplay during development whilst I was travelling between cities, left my acbook at home clamshell, powered, external display attached, and used it for small tasks remotely, it was pretty reliable even on a 5G network on a moving bus.Meow,
Jai

## 评论（29/29）

> **_aavaa_** · 2026-11-09T18:49:54.000Z　
> Cool. Does it support proper color profiles on the iPhone and HDR content?

---

> **Shank** · 2026-11-09T18:50:23.000Z　
> I really want an evaluation of all of these classes of remote desktop systems and latency. Almost all of my remote display experiences have been mediocre due to lag. Maybe my tolerance is too low? How is the latency on this product?Only RDP has felt truly responsive to me, and my understanding is that it cheats by not sending raster graphics and instead drawing primaries directly on the remote system and then updating the state based on the server?

---

> **iLoveOncall** · 2026-11-09T19:06:22.000Z　
> Isn't that natively supported? I thought you could use your iPhone as side display for your Mac.EDIT: Yes, the feature is called Sidecar.

---

> **jdalgetty** · 2026-11-09T19:06:59.000Z　
> Is this much different from Sill?

---

> **TazeTSchnitzel** · 2026-11-09T19:12:10.000Z　
> Refreshing to see a marketing site that isn't slop.

---

> **mpolichette** · 2026-11-09T19:12:45.000Z　
> Since this forks opendisplay, what are you doing differently? Are you a layer on top, or a different direction?I'd have expected that to be declared in an announcement for this community.

---

> **sleepybrett** · 2026-11-09T19:49:40.000Z　
> write me a client for the steam frame

---

> **dabbz** · 2026-11-09T19:51:19.000Z　
> It's uncanny, I just vibe built something super similar. A server/client system to share individual windows as a resized app on the phone. I can select certain windows to render as if it was an app on either my Windows client, mac client, or iPhone client from a windows or mac server.Glad to know I'm not the only one thinking about this. It also connects over tailnet.

---

> **qingcharles** · 2026-11-09T20:30:57.000Z　
> What can I use to bring the iMessage window from my clamshut MacBook onto my Windows desktop so I can write texts on a big boy screen instead of on the phone?

---

> **montjoy** · 2026-11-09T21:17:06.000Z　
> Does this require that Apple devices use the same account like sidecar?

---

> **SirFatty** · 2026-11-09T21:52:59.000Z　
> VNC?

---

> **OsrsNeedsf2P** · 2026-11-10T01:21:40.000Z　
> Surprised how few screenshots are in the README, given how visual of a program this is

---

> **raiseCatError** · 2026-11-09T19:11:33.000Z　
> Not currently, haven't verified color profile accuracy on the iPhone yet, and HDR isn't supported as of now either.

---

> **raiseCatError** · 2026-11-09T19:08:34.000Z　
> I agree, I have benchmarks planned for the future.As far as the latency on MeowDisplay, In my testing on Wifi, I measured around 14-17ms median from capture to receiver handoff, not e2e. I've also seen occasional spikes around 50-90ms and some stalled frames, you do notice the stalls but overall it's pretty responsive.I've preferred to show the cursor as it is on the mac instead of rendering it locally on the phone which may make it feel smoother but the trade-off is that it may not accurately represent where the cursor actually is on the mac if things lag or hang.Then again, it does depend on the connection.

---

> **BLKNSLVR** · 2026-11-09T22:25:07.000Z　
> That's pretty much been the only compromise I've had to make when migrating to an entirely Linux ecosystem at home. I settled on NoMachine as my pick of 'remote control desktop' software after trying a whole lot of other options (including various flavours of VNC).Every time I use it I'm reminded of how good RDP is/was.

---

> **monster_truck** · 2026-11-10T01:06:49.000Z　
> Assuming you are remoting into machines on your local network, I have made the Very Dumbest Compromise that I actually love, which is just leaving them connected to displays natively and creating a fake display on the controlling machine that runs a fullscreened remote desktop session set to potato. It's the only way I'll even bother to use a mac anymore, I'm not wasting another second fighting their godawful mouse input.

---

> **freeli** · 2026-11-09T19:12:19.000Z　
> Sidecar works to extend your Mac's display to iPads but does not work on iPhones.

---

> **raiseCatError** · 2026-11-09T20:07:24.000Z　
> The question I saw coming, and was hoping for too.
> Thank you for asking!There's quite a bit of overlap in what we're both trying to do. I've come across Sill and tried it as well, and it's nice.I think the biggest difference for most people would be the iPhone experience across both apps. I've specifically prioritized making the whole "use your Mac from your phone" experience better, and the iPad has received the same care too, with additional customizability to make use of the extra screen space.I've looked at quite a few remote desktop apps, how they've approached things and the trade-offs they've made, and weighed those against how I'd want MeowDisplay to do things.Part of MeowDisplay also came from a question: why hasn't Apple done something like this natively? The iPad has Sidecar, so I've often imagined how Apple might've approached it for the iPhone, and how I'd do it based on my experience with remote desktop apps.Coming to how they're different, I think the biggest distinctions are how I've chosen to handle Mac windows, the limited screen space on phones, and the overall UX.Sill's optional virtual display moves the selected window onto a separate display sized for the receiver, which can resize the actual Mac window. MeowDisplay's Window view keeps the Mac window's existing size and position, adapting how it's displayed on the phone instead.My reasoning behind this is that most desktop apps weren't designed for phone-sized windows. Resizing them can make their interfaces cramped or awkward, and I'd rather preserve their original layouts, even if that means occasionally zooming, which I find acceptable.Sill currently focuses on displaying one window or the desktop at a time, while MeowDisplay offers a different multitasking workflow with multiple windows arranged in tabs and panes, and floating windows coming in 2.1.Another difference is the screen space. Sill's portrait layout has the streamed picture at the top with a dedicated trackpad below it, although it also offers a Larger Picture option and direct touch.I've questioned why we even need a separate trackpad when the whole phone is already a touch surface. MeowDisplay lets you use the displayed content itself for Direct Touch or trackpad-style input, without sacrificing a portion of the screen for a dedicated trackpad. Personally, I find that screen space too valuable to give up.There's a difference in how you navigate through the UI as well. Sill has window thumbnails and app selection, while MeowDisplay uses Stage Peek, which you pull from the screen's edge to browse and search windows and apps, along with an expanded window overview.So yupp, we're both trying to solve a similar problem, just with different approaches and trade-offs. I think some people might prefer Sill's approach, and others might prefer MeowDisplay's.

---

> **jkahrs595** · 2026-11-10T00:33:22.000Z　
> Or RustDesk?

---

> **raiseCatError** · 2026-11-09T19:17:57.000Z　
> Thank you!

---

> **mschuster91** · 2026-11-09T22:08:26.000Z　
> OT but nice to see you're still around!

---

> **raiseCatError** · 2026-11-09T19:25:57.000Z　
> Yup, I'll add a snippet in the post, thanks,For answering your question, MeowDisplay started as a fork of OpenDisplay which had the foundations for screen capture, virtual displays, encoding and the iPhone/iPad receivers built, I've credited OpenDisplay and its developer Philip in the README under "Built on OpenDisplay"After that, I've taken a more phone-first approach, with quite a bit of work on the interaction, streaming and security layers.So it's built on OpenDisplay and not just a UI layer over it, MeowDisplay is going in a different direction, If you only need the core second-display experience, or compatibility that the OpenDisplay project serves better, OpenDisplay is well worth a look.

---

> **raiseCatError** · 2026-11-09T21:25:57.000Z　
> Likewise, Glad to have another person thinking on similar tracks!

---

> **anonzzzies** · 2026-11-09T22:29:49.000Z　
> Same here but I also replaced tailnet for our company with it as the non tech people found it too hard to use.

---

> **hbn** · 2026-11-09T20:54:05.000Z　
> Is there even a way to wake up a shut and sleeping MacBook? Or keep it awake at all? I'd be interested if there was that didn't have some caveat that will kill the battery.This seems more relevant than ever in days that we're sending off an LLM prompt and then letting it chug away for who knows how long. I tend to just leave my screen on with the mouse in a hotcorner that disables the screensaver.

---

> **raiseCatError** · 2026-11-09T21:24:53.000Z　
> Nope! You do not need same Apple ID accounts or be on the same Wifi, it has AWDL for Apple devices and a similar equivalent for Android is being looked into.

---

> **raiseCatError** · 2026-11-09T22:18:26.000Z　
> Similar idea, but not VNC. MeowDisplay uses its own streaming and control protocols, so you need the companion Mac app.I've considered supporting macOS's built-in Screen Sharing too, though with fewer features.

---

> **raiseCatError** · 2026-11-09T21:30:09.000Z　
> There are ways to wake a sleeping Macbook, MeowDisplay has Wake & Connect, which uses Wake-on-LAN to wake a supported Mac on the local network, provided Wake for Network Access is enabled.It doesn't work for a fully shut-down Mac though, and remote waking over something like Tailscale isn't supported yet. That would need something already awake on the Mac's local network, like a compatible router or another device, to relay the wake request. I've been looking into that.As for keeping it awake, macOS already lets you prevent automatic sleep whilst you're plugged into power, even with the display turned off, so you wouldn't need to leave the screen running all the time.

---

> **solyin** · 2026-11-09T23:04:04.000Z　
> Re: batteryAl Dente.app has you covered.

## 关联链接

- https://github.com/peetzweg/opendisplay
- https://github.com/raiseCatError/meowdisplayEDIT

## 导航

- 项目页：[[10-项目/meowdisplay.app_f0a7364e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
