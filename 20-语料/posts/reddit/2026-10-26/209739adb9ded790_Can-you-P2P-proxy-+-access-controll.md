---
type: "corpus"
item_id: "209739adb9ded790"
title: "Can you P2P proxy + access controll?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1x6tuyr/can_you_p2p_proxy_access_controll/"
author: "feetpic_sniper"
published_at: "2026-10-16T02:41:29+08:00"
captured_at: "2026-10-26T09:43:54+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-10-26"
pub_day: "2026-10-16"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Need Help
metrics: {"score": 3, "comments": 16, "upvote_ratio": 0.8}
comments_count: 14
comments_total: 16
discovered_via: "reddit:14d+settle10"
---

# Can you P2P proxy + access controll?

> [!info] 一句话导读
> Is something like this **possible** in a secure way? Is there reliable enough, **already made software** out there to achieve this? Would you **recommend** this…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1x6tuyr/can_you_p2p_proxy_access_controll/>
> 指标：得分=3 · 评论=16 · 赞踩比=0.8
> 作者：feetpic_sniper　|　发布：2026-10-16T02:41:29+08:00
> 项目链接：—
> 采集：2026-10-26T09:43:54+08:00　|　id：`209739adb9ded790`

## 正文

Sup,

Is something like this **possible** in a secure way? Is there reliable enough, **already made software** out there to achieve this? Would you **recommend** this path, or do you have a **better idea**?

**Background / Resoning:**

I currently use Tailscale to connect to my services, but I can't share my pictures this way with friends or family. A Cloudflare tunnel is also not ideal, since all the media would need to be streamed through them (usage limits and privacy). Finally, I don't want to expose any part of my LAN publicly, since my router didn't get updates in 5y and I don't know enough, except blocking all incoming traffic is pretty safe.

I got a raspberry left over and own a domain. I would place the Raspberry in front of my LAN.

## 评论（14/16）

> **asimovs-auditor**（1 分） · 2026-10-16T02:41:39+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **feetpic_sniper**（1 分） · 2026-10-16T02:44:15+08:00　
> No AI was involved in any way to create this post! The diagram was made in [draw.io](http://draw.io) by myself and the bad ideas and half assed knowledge are nothing but my creation!

---

> **Understanding_SIMP**（1 分） · 2026-10-16T03:57:48+08:00　
> You'd need a fallback relay if direct P2P connections fail.

---

> **GolemancerVekk**（1 分） · 2026-10-16T04:58:40+08:00　
> I'm not sure what exactly you think P2P is or why it would help you.
>
> You can make your reverse proxy require authentication so only known friends and family can get in from the internet. Is that not enough?

---

> **thegeekywanderer**（1 分） · 2026-10-16T05:30:16+08:00　
> Oh I’m building something exactly like this. It’s in early test builds let me know if you’d like to give it a shot.

---

> **feetpic_sniper**（1 分） · 2026-10-16T06:49:57+08:00　
> P2P is peer to peer to me, so two computers talking directly, instead of needing a central connecting node.
>
> Mainly because p2p can do NAT transversal and thus work with a firewall blocking all incoming traffic. Furthermore the proxy server is a bottleneck, all traffic needs to go through. If i want to tranfer more / big files, i might risk a huge hosting bill or need serious hardware just for my proxy server. With a direct connection I\`m hoping to get away with a cheap SoC.

---

> **feetpic_sniper**（1 分） · 2026-10-16T06:50:57+08:00　
> sure, id love to give it a try! Is it on github?

---

> **AirshipCommand**（1 分） · 2026-10-16T07:15:38+08:00　
> You can keep the router closed and still get mostly direct transfers. Your current mesh VPN already does NAT traversal, and most of them let you share a single node with an outside account, so family install the client and only see the photo server, not your LAN. Traffic goes peer to peer when hole punching works and falls back to a relay only when it doesn't. If they won't install anything, put a small VPS in front with the reverse proxy and auth, and have the Pi dial out to it over WireGuard. That way nothing on your LAN listens publicly, but the VPS does carry all the bytes, so pick one with unmetered or generous bandwidth and serve resized previews by default instead of originals.

---

> **Klutzy-Procedure8980**（1 分） · 2026-10-16T15:48:45+08:00　
> I think "Step 3: direct p2p webbrowser <-> NAS)" is going to be hard. You do need a proxy in-between. Is your goal not having to install anything on your family's devices? That and p2p seems to be a near impossible combo :-/
>
> I've built Wispers Access for similar use cases (https://access.wispers.dev, https://github.com/s-te-ch/wispers-access) for similar use cases (concretely: share internal apps with coworkers or family without exposing them to the internet). But you do need a client app install... I haven't been able to work around that

---

> **feetpic_sniper**（2 分） · 2026-10-16T16:22:43+08:00　
> i mean i would really like for my F&F not to need anything special on their side. To my knowledge P2P can punch holes and there are P2P Websites, so a normal Webbroser can do a P2P connection, Thats why I was interestet in it.
>
> But your apps looks really intreseting, ill definetly try it out, so I dont have to disable my adblocker all the time!

---

> **ItsBookx**（1 分） · 2026-10-16T16:50:46+08:00　
> p2p still requires at least one device that can accept inbound connections

---

> **thegeekywanderer**（1 分） · 2026-10-16T17:13:31+08:00　
> Oh I’m going to open source soon but I can give you access to it if you want. You can share your email with me in the dm and I can send you the website and everything there

---

> **Klutzy-Procedure8980**（1 分） · 2026-10-16T18:46:40+08:00　
> There are also a few alternatives listed in the readme file of the repo I linked, have a look at those too (thinking of Cloudflare tunnels primarily)

---

> **GolemancerVekk**（1 分） · 2026-10-16T18:48:29+08:00　
> P2P benefits you when there's something that two peers can do independent, like chat or video. But if you have a central service like streaming or pictures, all the users have to connect to the server anyway.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
