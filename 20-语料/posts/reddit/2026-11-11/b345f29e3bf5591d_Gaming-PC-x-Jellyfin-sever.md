---
type: "corpus"
item_id: "b345f29e3bf5591d"
title: "Gaming PC x Jellyfin sever?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1xkrvpy/gaming_pc_x_jellyfin_sever/"
author: "Full-Time-Menace"
published_at: "2026-11-01T10:26:51+08:00"
captured_at: "2026-11-11T13:38:46+08:00"
lang: "en"
kind: "post"
topic: "游戏"
shard: "2026-11-11"
pub_day: "2026-11-01"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Need Help
metrics: {"score": 7, "comments": 21, "upvote_ratio": 0.7333333333333333}
comments_count: 21
comments_total: 21
discovered_via: "reddit:14d+settle10"
---

# Gaming PC x Jellyfin sever?

> [!info] 一句话导读
> Hi, im new to all of this self hosting stuff. Long story short, I replaced my wife's pc so now we have an extra PC which I'll list the specs below.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1xkrvpy/gaming_pc_x_jellyfin_sever/>
> 指标：得分=7 · 评论=21 · 赞踩比=0.7333333333333333
> 作者：Full-Time-Menace　|　发布：2026-11-01T10:26:51+08:00
> 项目链接：—
> 采集：2026-11-11T13:38:46+08:00　|　id：`b345f29e3bf5591d`

## 正文

Hi, im new to all of this self hosting stuff. Long story short, I replaced my wife's pc so now we have an extra PC which I'll list the specs below.

Now, the general plan was to hook up the PC to the TV and run some casual couch games and use it for Jellyfin/media player.

However as I dug more and more into it, I remember I'd be interested in automating/adding on Jellyseer / Prowler/ other plug ins.

My question is, what would be the best way approach this? From my understanding, to run a dual system like this I'd need to use a VM and set up a server on there.

I would appreciate both ways.

The "complicated over engineered fun way"
And
 "I just want it to run and with minimal stuffing around"

I've used Plex before in the past along since Qbit, but in a very basic setup(download -> folder -> sync to Plex -> watch movies)

Generally we aren't planning to use this setup everyday/heavy games as we have our own setups. It would be just for torrenting, watching movies/shows, playing split screen stuff.

Thank you.

Setup:

CPU: Ryzen 5 3600 (this can be upgraded as we have spare parts)
GPU: RTX 3080ti
RAM: DDR4 8GB x 2 units (also can be upgraded as we have spares)
M.2: 500gb
HDD: 8tb x 2 units

## 评论（21/21）

> **asimovs-auditor**（1 分） · 2026-11-01T10:27:03+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **Full-Time-Menace**（3 分） · 2026-11-01T10:27:53+08:00　
> Hi? I'm kinda of confused? I hand typed that.
>
> (Apparently my post was flagged for AI 😂 I don't know if I should take that as a compliment or not.)
>
> I swear I didn't use AI, I just want to ask more experienced users what is the best way to accomplish my goal of a mildly ambitious project.

---

> **Chazay**（3 分） · 2026-11-01T10:35:58+08:00　
> Same idea as what you did for plex. The Arrs download stuff to the PC, the PC hosts. You use Jellyfin to watch the files the same way you accessed plex.
>
> No need for a VM. Thats doing some weird complication that’s super unnecessary.

---

> **Zotlann**（6 分） · 2026-11-01T10:36:03+08:00　
> I've got a similar setup, here's what I have (probably closer to your over engineered fun way).
>
> I'm using proxmox, and on that I have a bazzite:steamdeck virtual machine for gaming.  This VM has the bulk of the system RAM allocated to it, as well as the GPU passed through to it.  HDMI connected from the GPU to the TV is near 0 overhead.  Then on that same proxmox node I have an LXC for jellyfin, and on another node in my homelab I have all of the \*arr automation stuff set up in docker containers on an ubuntu server VM.  For your setup, I'd recommend 1 bazzite VM for gaming, and then 1 ubuntu vm or lxc with docker on it for jellyfin+automation.
>
> Simpler setup would just be to install bazzite on the bare metal, and then install docker on that and set up jellyfin+automation on docker there.

---

> **dcherryholmes**（4 分） · 2026-11-01T10:36:58+08:00　
> Install all the \*arrs and the jelly stuff as containers, using docker compose.  Some others might reply and talk about proxmox but I think for your situation that is overkill.  If you want a nice, simple GUI to help manage your containers (mainly upgrading them with a click if you set up your compose files to point to "latest"), I think dockge is a very good tool.
>
> Also, you may know this but since you didn't say it explicitly, make sure you use a VPN and block all ipv6 traffic.  Yarr!

---

> **AdUnfair9248**（2 分） · 2026-11-01T10:40:01+08:00　
> **Hear me out:**
>
> Batocera (retro arcade version of Linux) - extensible enough that you could run Docker in the background and run Jellyfin/\*Arr stack. Has Kodi built-in for media watching purposes. It's ALMOST everything I want. My setup doesn't have Docker in it but not sure how that could backfire for you.
>
> **What I wish existed:**
>
> Would be nice to have a version of Linux with full HDMI-CEC report so that I could use my TV's remote. It's very hit-or-miss for now.
>
> **The complications:**
>
> I'm using Proxmox as the main OS and running Batocera as a VM inside of it so I would actually NOT run Docker inside of Batocera. I would run Docker alongside Batocera because the Batocera VM is deliberately hogging the graphics card. The VM is consuming all of the ports on the host (USB/speaker/HDMI) so it's outputting HDMI to a TV. GPU passthrough is super common these days but it's still not standard enough to be in the Proxmox UI. Requires some extensive changes.
>
> Edit: Running Batocera with Incus inside of it is also an option, but I haven't tried Incus yet.

---

> **Full-Time-Menace**（1 分） · 2026-11-01T10:41:13+08:00　
> As much as I'd love to use Proxmox and I'll probably do that one of these days when I have time to build a proper server. I just don't have the time and energy to maintain a full on server for 1 application.
>
> Your suggestion sounds great, happen to have any videos/resources you'd recommend?

---

> **freshairproject**（4 分） · 2026-11-01T10:42:14+08:00　
> Run it all locally on Windows without containers or VMs.

---

> **Full-Time-Menace**（1 分） · 2026-11-01T10:46:19+08:00　
> Thank you for your detailed response. I will look into Proxmox once I have more free time to actually understand and be able to maintain it without oopies with 1 wrong click. I highly doubt my wife would be impressed if her watch history goes bye bye. Looking at it all layed out, ya.... I think it is really a tad overcomplicated for now. But still sounds so fun!!
>
> I'll stick with the simpler option for now so the misses can watch her TV dramas in pieces. Any recommendations for resources/videos as guidance?

---

> **BashfulLongevity**（1 分） · 2026-11-01T10:59:18+08:00　
> if you go the bare metal route with bazzite, just be careful with how docker and the steam compositor interact, sometimes they fight over network ports and it gets weird. happened to me once with a different setup and i spent a whole afternoon thinking my router was dying
>
> the proxmox way is cleaner if you dont mind the extra work upfront, having the gpu passed through directly makes games feel native and the jellyfin lxc stays out of the way. your 3080ti will handle transcoding like nothing too

---

> **dcherryholmes**（1 分） · 2026-11-01T12:09:35+08:00　
> Will you be keeping Windows on the PC or are you going to run linux?  All of my stuff is linux.

---

> **dcherryholmes**（3 分） · 2026-11-01T12:19:07+08:00　
> But, assuming you will go the linux route, these are some good places to get started.  If you are staying with windows, I am probably not of much help.
>
> [https://yams.media](https://yams.media)
>
> YAMS includes essentially the entire stack you want:
>
> \- Jellyfin for streaming movies and TV.
>
> \- Seerr for media requests.
>
> \- Sonarr, Radarr, Prowlarr, Lidarr and Bazarr for media automation.
>
> \- qBittorrent for torrent downloads.
>
> \- Gluetun for VPN connectivity and an integrated kill switch.
>
> \- Docker Compose for managing the containers.
>
> \- Portainer for a graphical container-management interface (I'd do dockge but portainer is even better-known and solid)
>
> [https://trash-guides.info/File-and-Folder-Structure/How-to-set-up/Docker/](https://trash-guides.info/File-and-Folder-Structure/How-to-set-up/Docker/)
>
> This is probably the gold standard for setting up the \*arrs.  Crucially, it explains what hard-linking is, which is what you'll want your qbittorrent client to use.  Oh, as an aside, when you get around to installing qbittorrent, look into installing the alternative gui called "vuetorrent"  It really kicks it up a notch, and also makes the gui more phone-friendly if you think you might interface with it that way.
>
> [https://gluetun.org/guides/docker-compose](https://gluetun.org/guides/docker-compose)
>
> This explains how to route qBittorrent through a VPN container using network\_mode: "service:gluetun". It's particularly useful for understanding how the kill switch works rather than simply relying on an installer.

---

> **dcherryholmes**（4 分） · 2026-11-01T12:23:48+08:00　
> "as well as the GPU passed through to it"
>
> Be wary, OP.  This person is obviously a wizard, and there was probably some pact with a demon involved in setting that up. :)

---

> **Full-Time-Menace**（1 分） · 2026-11-01T13:57:04+08:00　
> I'd prefer Windows, I'll have a look into it. You rekon there are other alternatives if I pick the windows route?

---

> **TinyAd185**（2 分） · 2026-11-01T19:58:03+08:00　
> The lack of passthrough ability or the constsnt fucking round was what finally made me make the move to Linux. Not looking back

---

> **TheLabLedger**（1 分） · 2026-11-01T21:45:50+08:00　
> If you stay on Windows, it's less work than it sounds. Jellyfin has a normal Windows installer and can run as a background service, so it starts at boot without anyone logging in. Your 3080 Ti can handle hardware transcoding through NVENC, you just turn it on in the playback settings. Point the libraries at the 8TB drives and keep the Jellyfin config folder somewhere you copy off now and then, since that's where the watch history lives. Two things I'd do on Windows: set active hours so updates don't reboot it mid movie, and run the torrent client behind a VPN with a kill switch. Games and Jellyfin coexist fine on one machine at your usage.

---

> **dcherryholmes**（1 分） · 2026-11-01T22:11:33+08:00　
> Definitely.  I just haven't done it.

---

> **PlanktonSuccessful65**（1 分） · 2026-11-01T22:26:23+08:00　
> Have you heard of "games on whales/wolf" its a docker app that can make a virtual gaming vm that can be accessed through Moonlight, although i think your setup lacks Ram if you plan on using that machine for jellyfin and also gaming

---

> **Dhanni-Asmus**（1 分） · 2026-11-02T22:26:47+08:00　
> you really dont need a full VM for the simple route. Just run the services as background applications or in containers directly on your main OS, that hardware has more than enough headroom to handle background media tasks while couch gaming.

---

> **Yaule371**（1 分） · 2026-11-04T19:37:58+08:00　
> Je en

---

> **adarsh1021**（0 分） · 2026-11-07T02:12:44+08:00　
> The minimal setup would be to just run your media apps on your windows PC beside your games - you can use docker desktop, and write docker compose files easily (AI agents can help).
>
> The over engineered fun way would be to install proxmox on the bare metal with Windows in one VM and a linux VM for the server, with the GPU passed through to Windows. You would still need docker on the linux VM to run your media apps.
>
> There is a third way - use mesopod to run your media apps. You run one command for the setup on your windows PC, pick the apps you need and deploy it to your PC from the web console. Mesopod takes care of running them, routing and gives you a domain name for each app that you can use locally

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`游戏`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
