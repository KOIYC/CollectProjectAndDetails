---
type: "corpus"
item_id: "2a17266c86f2861f"
title: "Self Hosting Dashcams?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1xrapn3/self_hosting_dashcams/"
author: "MrSumOne"
published_at: "2026-11-09T06:14:31+08:00"
captured_at: "2026-11-19T09:44:40+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-11-19"
pub_day: "2026-11-09"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Need Help
metrics: {"score": 31, "comments": 26, "upvote_ratio": 0.8604651162790697}
comments_count: 25
comments_total: 26
discovered_via: "reddit:14d+settle10"
---

# Self Hosting Dashcams?

> [!info] 一句话导读
> I have been using a Viofo dashcam, and putting the micro SD into my computer whenever I need to review the footage, but it needs an upgrade.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1xrapn3/self_hosting_dashcams/>
> 指标：得分=31 · 评论=26 · 赞踩比=0.8604651162790697
> 作者：MrSumOne　|　发布：2026-11-09T06:14:31+08:00
> 项目链接：—
> 采集：2026-11-19T09:44:40+08:00　|　id：`2a17266c86f2861f`

## 正文

I have been using a Viofo dashcam, and putting the micro SD into my computer whenever I need to review the footage, but it needs an upgrade.

Rear camera and cabin cameras. Access from my phone, or automatically reviewable when I get home would be a huge bonus.

Does anyone have camera recommendations and self hosting apps that accomplishes this?

## 评论（25/26）

> **asimovs-auditor**（1 分） · 2026-11-09T06:14:41+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **MrSumOne**（1 分） · 2026-11-09T06:15:37+08:00　
> No AI used

---

> **abeorch**（37 分） · 2026-11-09T06:28:57+08:00　
> Im interested in dashcams that would automatically download/backup when on the local network when you get home.
>
>  It would be amazing to have one like that so I could then also automatically  process images and upload some to panoramax.

---

> **FrogSkyWater**（2 分） · 2026-11-09T06:37:19+08:00　
> I use the Viofo app on phone

---

> **np0x**（2 分） · 2026-11-09T07:07:15+08:00　
> Does the viofo have the option to automatically save the video to your phone camera roll?  Because if it did then you could leverage something like Immich…

---

> **shopsd**（28 分） · 2026-11-09T07:07:54+08:00　
> [https://github.com/RobXYZ/viofosync](https://github.com/RobXYZ/viofosync) is probably what you want

---

> **dedicated_blade**（1 分） · 2026-11-09T07:09:25+08:00　
> The best I could think of is having a Rasp Pi Zero or 3B+ that’s powered via your cars ignition, and after x amount of no ignition power it powers down and the ignition sequence cycles the Pi back on.
>
> Then have the Pi sync the files from the dash cam via FTP to your local server for backup.

---

> **iwasboredsoyeah**（1 分） · 2026-11-09T07:11:35+08:00　
> What's the app name? The one I found isn't available in my country

---

> **lipusal**（3 分） · 2026-11-09T07:25:01+08:00　
> Oh wow this is cool, I was developing something similar, my problem being that my camera needs its WiFi to be manually turned on. The repo says a custom firmware is needed to keep it on, do you happen to know how I can request that, or if anyone has shared? I will also ask in the repo, just figured I'd ask here too

---

> **shopsd**（2 分） · 2026-11-09T07:52:53+08:00　
> you can contact VIOFO support for the firmware

---

> **ceestars**（2 分） · 2026-11-09T07:56:02+08:00　
> It's just called VIOFO. Here's the link for the UK app store
> https://play.google.com/store/apps/details?id=com.viofo.viofo

---

> **iwasboredsoyeah**（2 分） · 2026-11-09T09:09:24+08:00　
> Yep that the one I found and its not available :/ maybe I'll just side load it and see if it works

---

> **winner_68**（1 分） · 2026-11-09T09:26:31+08:00　
> I went through the same SD-card shuffle with a Viofo A129, and the part that finally made it tolerable wasn't a better camera, it was getting the files off the card without thinking about it.
>
> viofosync is the right starting point — I run it on a little box at home, and when the car joins my home Wi-Fi it pulls new clips into dated folders. The trick I learned the hard way is to keep the sync one-way and let the camera keep recording: the first time I tried to be clever and delete after sync, a flaky Wi-Fi drop left me with half a trip missing.
>
> For watching them, I don't use Frigate or anything live-camera-shaped — a dashcam isn't an RTSP camera, and I wasted an afternoon trying to force it into that shape. I just browse the synced folder through Immich on my phone over Tailscale, and I only keep locked/event clips long-term. Everything else gets pruned after about two weeks, otherwise a 256GB card fills your server faster than you'd expect.

---

> **amarsaudon**（0 分） · 2026-11-09T12:33:01+08:00　
> Thanks for plugging this! Incredibly cool / better than the shitty download script I had been leaning on.

---

> **cat2devnull**（1 分） · 2026-11-09T18:54:59+08:00　
> How did I not know about this!

---

> **Hostman_com**（1 分） · 2026-11-10T00:49:25+08:00　
> The Viofo A329S 3CH is one to look at if you want rear and cabin cameras. It's on the viofosync tested list. Before buying, I'd ask Viofo whether it can rejoin your home Wi-Fi on its own after you park and turn the car off. If you still have to press the Wi-Fi button every time, the automatic backup isn't really automatic.
>
> https://i.redd.it/hs8h61759m0i1.jpeg

---

> **Significant_Book8223**（3 分） · 2026-11-10T02:12:10+08:00　
> support.viofo.com/support/home
> Let them know what model dashcam you have and that you need the custom firmware that keeps the wifi station mode enabled during park mode.  Takes about 48 hours for them to respond but they'll send it to you.
>
> you will need the dashcam hardwired to the car

---

> **AlbanMApp**（4 分） · 2026-11-10T03:37:13+08:00　
> The "automatically reviewable when I get home" part is what narrows the choice. You want a camera that can join your home Wi-Fi as a client. Most dashcams only create their own hotspot, which means you connect your phone to the camera every time.
>
> BlackVue is the easy answer for self-hosting. The 3-channel models (front, rear and interior IR, e.g. the DR970X-3CH series) can connect to your home Wi-Fi when you park. There's an open-source tool, blackvuesync, that runs on a NAS or in a Docker container and pulls new recordings over the LAN automatically. No cloud subscription needed. Downsides: it's pricey, and you should check whether the exact model you buy supports Wi-Fi client mode.
>
> Staying with Viofo: the 3-channel A229 Pro / A139 Pro give you front, rear and interior with good image quality. Phone access works well through the Viofo app over the camera's own hotspot. Fully automatic home sync is more DIY, though. People use a small always-on device (Raspberry Pi, etc.) that joins the camera's hotspot when the car is in the driveway and copies the files over. It works, but expect some tinkering. Check the current firmware features before buying, they change often.
>
> Whatever you pick:
>
> \- For the parking footage to be useful, use a hardwire kit or a battery pack, so the camera is still recording when it's parked at home.
>
> \- Use a high-endurance microSD. Three channels write a lot of data and kill regular cards quickly.
>
> \- An interior camera with IR is worth it if you want usable cabin footage at night.

---

> **lipusal**（2 分） · 2026-11-10T05:34:01+08:00　
> Thanks, I did reach out but no luck, at least not for the A129 Pro Duo. this was their response:
>
> > Thank you for contacting VIOFO Support and for sharing your feedback.
> > Unfortunately, we do not have custom firmware available that can automatically enable Wi-Fi and permanently set it to Station Mode. The Wi-Fi settings need to be enabled and configured manually.
> > We will pass your feedback along to our product team for future consideration.
> > Thank you for your continued support of VIOFO!
>
> I'll try to rephrase as parking mode, but they may just not do it for the older models =(

---

> **lipusal**（1 分） · 2026-11-10T05:37:35+08:00　
> Thanks, no luck unfortunately, see [this reply](https://www.reddit.com/r/selfhosted/comments/1xrapn3/comment/19se7k1238j9h/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)

---

> **MrSumOne**（1 分） · 2026-11-10T06:32:41+08:00　
> Thanks for the info, maybe having the secure hotspot for phone access, and then hitting the wifi button in emergencies is the answer I'm looking for

---

> **MrSumOne**（1 分） · 2026-11-10T06:34:16+08:00　
> Maybe it's better that I only back stuff up when it's important, otherwise I'll be storing tons of footage of boring drives.

---

> **shaltaSt**（5 分） · 2026-11-10T19:48:22+08:00　
> the power draw while parked is the real killer here tbh. transferring gigabytes of 4k video over wifi takes a solid chunk of time, so unless you have a dedicated battery pack wired in, the low-voltage cutoff will probably kill the camera before the sync finishes.

---

> **imetators**（1 分） · 2026-11-11T03:26:41+08:00　
> Dope! 8 got viofo. But I live in a parent any my car is always parked around the block. Sad I can use it but this is so cool! I wish 8d have a house!

---

> **madmax8898**（1 分） · 2026-11-11T13:30:06+08:00　
> I have a BlackVue 750xPlus which can connect to the WiFi. I didn’t know I could run BlackVue on my NAS but normally just go inside and connect to it via the phone app then download what I want so it’s already on the phone.
> I would defo say hardwire it and include a battery as well so it doesn’t put a lot of stress on your battery.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
