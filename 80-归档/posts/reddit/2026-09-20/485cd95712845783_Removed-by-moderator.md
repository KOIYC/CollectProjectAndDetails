---
type: "corpus"
item_id: "485cd95712845783"
title: "[ Removed by moderator ]"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1wi4jnj/a_2012_mac_mini_from_an_ewaste_pile_runs_my_whole/"
project_url: "https://reddit.com/gallery/1wi4jnj"
author: "Lopsided-Mirror-6611"
published_at: "2026-09-17T01:54:57+08:00"
captured_at: "2026-09-20T02:44:01+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Personal Dashboard
metrics: {"score": 361, "comments": 50, "upvote_ratio": 0.96}
comments_count: 61
comments_total: 61
discovered_via: "reddit:7d+settle3"
topic: AI 工具/Agent
archived: true
archived_at: "2026-09-20T10:02:36+08:00"
archive_reason: "排除:标题"
---

# [ Removed by moderator ]

- **来源**：Reddit 独立开发版块　|　**kind**：post
- **原帖**：https://www.reddit.com/r/selfhosted/comments/1wi4jnj/a_2012_mac_mini_from_an_ewaste_pile_runs_my_whole/
- **指标**：得分=361 · 评论=50 · 赞踩比=0.96
- **作者**：Lopsided-Mirror-6611　|　**发布**：2026-09-17T01:54:57+08:00
- **项目链接**：https://reddit.com/gallery/1wi4jnj
- **采集**：2026-09-20T02:44:01+08:00　|　**id**：`485cd95712845783`

## 正文

My wife found a late-2012 Mac mini in an e-waste pile. After a RAM upgrade it was a desktop for a while, and when macOS stopped supporting it I installed Ubuntu Server 24.04. It's been the home server since. I drew a map of what runs on it and how data moves between the pieces.

**Hardware**

* Mac mini (late 2012), Intel i5-3210M (2 cores, 4 threads), 16 GB RAM
* 250 GB SSD for the system, 1 TB for files, two 8 TB drives (photos and archive on one, local backups on the other)
* Home Assistant runs on a separate Home Assistant Green, so the home automations don't go down with the server

**What runs, and what it replaces**

* Nextcloud – Google Drive, Dropbox
* Immich – Google Photos
* Paperless-ngx – a filing cabinet. A scanner with a document feeder drops scans into the folder it watches
* Stirling PDF – iLovePDF, Smallpdf
* SplitPro, with a few of my own changes – Splitwise, after it put features behind a paywall
* AdGuard Home – Pi-hole, NextDNS
* PriceBuddy – CamelCamelCamel, Keepa
* Uptime Kuma – UptimeRobot
* Kopia – versioned local backups, plus an encrypted offsite copy
* A meal planner I wrote. It plans the week and a small Chrome extension adds the shopping list to the supermarket cart
* BirdNET with a USB mic at the window. It identifies birds by sound and shows them as an illustrated collage (a fork of Avian Visitors)

Most of it runs in Docker. The bird setup runs in an LXD container (see below).

**Access**

No ports forwarded. The few public things go out through a Cloudflare Tunnel, some of them behind Cloudflare Access. Everything else is Tailscale only.

**Things that bit me**

* The CPU has AVX but not AVX2. Current tflite-runtime wheels die instantly with "Illegal instruction". tflite-runtime 2.14 with numpy 1.26 works.
* The BirdNET installer assumes it owns the machine: it reboots at the end, upgrades packages and adds broad sudo rules. So it lives in an LXD container.
* After a reboot the USB mic came up under a different ALSA card number, and the container got the internal sound card instead. It recorded silence for about 20 hours while the web UI looked completely healthy. A timer now checks the mic every 2 minutes.
* My first mic was a wireless voice receiver with an 8 kHz ceiling, so high-pitched birds never showed up. A cheap wired USB lavalier fixed it.

The map is part of a small static page about the setup, with status dots from Uptime Kuma. I built the page and the meal planner with a lot of help from Claude Code.

Happy to answer questions about any of it.

## 评论（61/61）

**asimovs-auditor**（1 分） · 2026-09-17T01:55:07+08:00：

Thanks for posting to r/selfhosted. Your post has been temporarily removed. Please reply to this comment explaining how AI was used in the creation of your post/project. Once you reply, your post will be automatically approved. To learn more about why this is required, please see our [pinned post](https://www.reddit.com/r/selfhosted/comments/1sey9ch/quarter_2_update_revisiting_rules_again/).

**Lopsided-Mirror-6611**（0 分） · 2026-09-17T01:58:25+08:00：

I used Claude Code in a few places:

* **The post itself:** Claude drafted it from my notes and checked the facts against the server (hardware, containers, what's running). I reviewed and edited it before posting.
* **The map page:** a static page I built with Claude Code, adapting the design of Avian Visitors (credited on the page, CC BY-NC-SA). The screenshots come from that page.
* **Setup and troubleshooting:** it helped debug things like the AVX2 crash and the USB mic problem, and with hardening (sandboxing the web server, Cloudflare cache rules).

The services themselves (Nextcloud, Immich, Paperless-ngx, Stirling PDF, SplitPro, AdGuard Home, PriceBuddy, Uptime Kuma, Kopia, BirdNET) are existing open-source projects. I'm not releasing anything, this is just my setup.

**CrrackTheSkye**（4 分） · 2026-09-17T02:09:00+08:00：

Can you give some more info about the birdnet setup? I see it's also an Android app, but I guess that's not what you're running here lol. Is the mic just connected to your Mac then?

**Lopsided-Mirror-6611**（8 分） · 2026-09-17T02:23:14+08:00：

No, it's not the app. BirdNET is the bird-sound model from the Cornell Lab of Ornithology and TU Chemnitz. It's behind the BirdNET app, and Merlin's Sound ID comes from the same lab. Here I'm running BirdNET-Pi, which uses the model on a regular Linux machine despite the name. Specifically, a fork called [Avian Visitors](https://github.com/Twarner491/AvianVisitors), which adds the illustrated collage. My version with a few changes is [here](https://github.com/lkhurana/AvianVisitors).

Yes, the mic is just a cheap wired USB lavalier plugged straight into the Mac mini. The Mac mini is next to the window, and the mic sits just outside it. The chain:

* **Mic:** a USB lavalier with a TI PCM2902 chip. It's on a 2 m cable, so it sits just outside the window with the Mac mini right next to it inside. Two gotchas: its automatic gain control is on by default (bad for this, it pumps the noise floor), and the gain resets on every reboot or replug. A small systemd service sets it back each time.
* **Filtering:** a 300 Hz high-pass filter cuts wind and traffic rumble, low enough that dove coos survive, then a software volume boost because this mic is fairly quiet.
* **Detection:** BirdNET listens in short clips around the clock. Species that don't fit your location and the time of year get filtered out, which cuts down false positives a lot.

Two things I learned the hard way:

* My first mic was wireless and turned out to be a voice device capped at 8 kHz, so it could never pick up high-pitched birds. The €15 wired one hears the full range.
* USB sound card numbers aren't stable across reboots. The mic moved and the container quietly got the internal sound card instead. It recorded silence for about 20 hours while the web UI looked perfectly healthy. A timer now checks the mic every few minutes.

The next step is a Raspberry Pi outside streaming audio over Wi-Fi to the server, since it's a rented flat and I can't drill for cables. The analysis would stay on the Mac mini.

**Anti-Hero25**（0 分） · 2026-09-17T02:28:05+08:00：

Was gonna suggest [CTRoadmap](https://github.com/NoobCity99/CTRoadmap) for your diagramming and documentation… but if you want monitoring too , Homelable might be a better option.

**Lopsided-Mirror-6611**（2 分） · 2026-09-17T02:43:13+08:00：

Oh nice, thanks for the suggestions! I hadn't come across either of them, so I really appreciate it. Homelable looks great, especially the auto-discovery.

My map ended up being a bit different from a network diagram: it shows how data moves between services (scanner → Paperless → Nextcloud → offsite backup, meal planner → shopping list, and so on) rather than which box talks to which IP. Uptime Kuma already feeds the status dots, so monitoring is covered for now.

CTRoadmap does look really handy for the parts that don't fit on the map, like disks, mounts and all the little scripts holding things together. I'll give it a proper look. Thanks again!

**derical_cap_musical**（38 分） · 2026-09-17T02:47:21+08:00：

those 2012 mac minis refuse to die. awesome setup and great use of ewaste.

**ProGamler2**（10 分） · 2026-09-17T02:59:16+08:00：

16gb ram basically a luxury upgrade for a 2012 mac mini lol

**mightyarrow**（2 分） · 2026-09-17T03:06:17+08:00：

Well that's fuckin cool. I played with the Merlin app on my Android while I was in Costa Rica. This takes it to the next level.

**Lopsided-Mirror-6611**（6 分） · 2026-09-17T03:13:59+08:00：

Thanks a lot! They really don't. A RAM upgrade, Ubuntu Server, and it just keeps going. It's nice knowing it's doing useful work instead of sitting in a landfill.

**Lopsided-Mirror-6611**（2 分） · 2026-09-17T03:14:15+08:00：

Right? It came with 4 GB, so it's basically living its best life now. 40€ for 2×8 GB, and it's the only reason all of this runs. Now that it has the memory, what would you run on it next?

**Anti-Hero25**（1 分） · 2026-09-17T03:39:32+08:00：

Yea CTRoadmap has swim lanes for process flows…. (Full Disclosure) it’s mine.  It’s intentionally NOT integrated , doesn’t do any live monitoring so it doesn’t have auto discovery…. It’s meant to be a standalone documentation tool. But will have a manual discover feature soon.

**Darkomen78**（8 分） · 2026-09-17T04:04:45+08:00：

MacMini Intel are the best for Proxmox and homelab stuff.

**Nix-geek**（2 分） · 2026-09-17T04:16:33+08:00：

I have two 2011 mac mini's running a bunch of stuff with Proxmox in my network.  One of them being my OPNSense firewall :)  

Love those little things.

**Nemisis82**（2 分） · 2026-09-17T04:37:32+08:00：

Maybe I am dumb, but what is the connection between Immich and NextCloud?

**1WeekNotice**（1 分） · 2026-09-17T04:48:30+08:00：

Not really Mac related but alot of people throw away machines that are EOL(end of life)/ not supported by their original OS. 

For example, when windows 10 became EOL a ton of computers were just thrown away because windows 11 didn't support them. A lot of people don't know about Linux. They only know about the OS there hardware came with. 

----------

It's good to see you run alot of services. When you start selfhosted you realize that you don't need high performance hardware to run useful services. 8 GB - 16GB goes along way. 

--------

For the Mac ensure you

- use unbuntu LTS instead of the normal Ubuntu distribution. 
  - LTS (long term support) will be supported longer. You can look up the release cycle
- enable the Mac to power on after power outage


Nice find and hope that helps

**debunkedscientist**（1 分） · 2026-09-17T05:04:21+08:00：

Are you able to reboot the 2012 Mac mini without a password?

**Lopsided-Mirror-6611**（3 分） · 2026-09-17T05:19:32+08:00：

Not dumb at all, fair question! The photo library Immich manages is also mounted in Nextcloud as a read-only folder, so I can get to the same files from there too.

My Immich isn't public, so it isn't set up for sharing with other people. If I want to share a folder of photos with someone, I share it from Nextcloud with a link instead. Immich handles the backup, search and faces, and Nextcloud handles the sharing.

**Lopsided-Mirror-6611**（1 分） · 2026-09-17T05:25:49+08:00：

Yep, no password needed. On macOS the password prompt at boot usually comes from FileVault. On Ubuntu I don't use boot-time disk encryption, so it just boots straight up after a reboot. All the containers are set to restart automatically, so everything comes back without me touching it. The trade-off is that someone who physically took the machine could read the disks.

**Lopsided-Mirror-6611**（1 分） · 2026-09-17T05:28:19+08:00：

Thanks, that really helps! Totally agree on the EOL point. Yes, 16 GB goes a surprisingly long way once you stop needing a desktop OS on top.

It's on Ubuntu Server 24.04 LTS, so that part's covered. Power-on after an outage is a good reminder though, it's actually not set up yet! A UPS is a good shout too.

**Only-Stable3973**（1 分） · 2026-09-17T06:32:30+08:00：

Those box's are great, I keep thinking about getting a Minisforum MS-01 mainly because it does not cost 3000 and will most likely keep up with the newer box's.

**River_Tahm**（1 分） · 2026-09-17T06:41:40+08:00：

Same! I managed to mod mine to take a 2.5" SSD in addition to the proprietary m.2 so it's a 4+2TB setup.

**qdatk**（-2 分） · 2026-09-17T06:44:02+08:00：

> Now that it has the memory, what would you run on it next?

Folks really do be outsourcing Reddit comments to LLMs now.

**Lopsided-Mirror-6611**（5 分） · 2026-09-17T06:47:16+08:00：

That was a question for @ProGamler2, to get recommendations for the tools/services that I can run on my setup

**carrigroe**（1 分） · 2026-09-17T07:04:29+08:00：

The Mac mini is the one of the best products apple has ever made, The power usage on apple silicone is insanly low. You can keep them running 24/7 for like $20 a year in electricity costs.

**LookAtThatMonkey**（1 分） · 2026-09-17T07:28:14+08:00：

Similar here, I run a 2011 Mac Mini with 16GB with Linux Mint and its my docker host and runs it all, with an Rpi 4 acting as a secondary for some other bits.  Quiet, not hot, whats not to like?

**psayre23**（5 分） · 2026-09-17T10:13:10+08:00：

Yes, but like an old truck, it’s worth keeping two — for spare parts.

**JhnWyclf**（1 分） · 2026-09-17T11:44:06+08:00：

>250 GB SSD for the system, 1 TB for files, two 8 TB drives (photos and archive on one, local backups on the other)

Are all four drives _in_ the machine?

**cedarwick_263**（1 分） · 2026-09-17T14:36:37+08:00：

How does the mic check distinguish a failed input from a genuinely quiet night? Does it check that audio is arriving, or look for a minimum sound level?

**stofdick**（1 分） · 2026-09-17T14:44:06+08:00：

I just got a mac mini 2012 with the i7 last week for 60 euros. Upgraded the ram and slapped in an extra ssd i had laying around. Works great in my proxmox cluster for the low resource tasks. 👍

**alwaysnewbie**（3 分） · 2026-09-17T14:56:03+08:00：

You might want to have a look at the ESP32 wireless microphone project – [birdnet-esp32-rtsp-mic](https://github.com/Sukecz/esp32-birdnet-mic).

**AlthoughFishtail**（0 分） · 2026-09-17T15:39:52+08:00：

I have the same machine, but with Debian on it. Absolute workhorse.

**Crafty-Industry-1199**（0 分） · 2026-09-17T16:34:20+08:00：

That 2012 Mac mini is an absolute beast for homelabbing; I love seeing these old machines getting a second life instead of hitting the landfill. Managing that AVX/AVX2 compatibility headache with the tflite-runtime is a classic "old hardware" struggle—have you considered moving any of the heavier ML tasks to a Coral TPU to offload that aging CPU, or are you keeping it strictly software-based for now?

**Crafty-Industry-1199**（0 分） · 2026-09-17T16:35:09+08:00：

That 2012 Mac mini is an absolute beast for homelabbers! I’m running a similar setup on an old ThinkPad, and honestly, the AVX instruction set issues with modern AI containers are such a pain—glad you found the workaround for the tflite wheels. Have you looked into using Proxmox for your containers instead of LXD, or do you prefer the native feel of the Mac hardware for that specific bird monitoring setup?

**_squik**（1 分） · 2026-09-17T17:11:07+08:00：

I still have a 2012 Mac mini running as my daily browsing and admin computer, as it has been for the past 13 years. It's not the fastest any more but it works well enough - writing this comment from it. Runs Ubuntu now.

**DuckTheAlucard**（4 分） · 2026-09-17T17:12:24+08:00：

And can be found for extremely cheap prices if you search for a unit without RAM/HDD. The only annoying part is keeping in mind you have to use 1.35V RAM

**Lopsided-Mirror-6611**（2 分） · 2026-09-17T20:07:23+08:00：

It doesn't use a minimum sound level, exactly because a quiet night would trip it. There are two checks:

* **Every 2 minutes:** a script looks for the USB mic by name and reads its settings. If the device is missing, it logs a failure. If a replug or reboot resets the gain or turns auto gain control back on, it sets them back. This catches the "wrong card / reset settings" failures. Every 2 minutes is probably overkill and I can run it less often.
* **Every 15 minutes:** it records 20 seconds and counts exact digital zeros. A real mic always has some self-noise, so even a silent night gives small non-zero values. A failed input tends to give either nothing at all or runs of perfect zeros. Sustained zeros or gaps of a few seconds count as a failure and short ones as a warning.

**Lopsided-Mirror-6611**（2 分） · 2026-09-17T20:11:51+08:00：

Oh nice, thank you! That's really timely. My next step was to use a Raspberry Pi outside to stream RTSP back to the Mac mini, but an ESP32 with an I2S mic seems like a much lighter way to do the same thing! I'll definitely try it.

**Lopsided-Mirror-6611**（1 分） · 2026-09-17T20:15:06+08:00：

Only the system SSD is inside. The rest are USB 3. The 1 TB is a Crucial X9 Pro portable SSD, and the two 8 TB drives are WD Elements Desktop external drives.

**Lopsided-Mirror-6611**（2 分） · 2026-09-17T20:33:06+08:00：

Nice! I'm honestly not very familiar with the firewall and routing side of networking yet. I've been learning self-hosting as I go, so I'm curious how you handled it with only one built-in Ethernet port: a Thunderbolt Ethernet adapter or VLANs on a managed switch?

**Lopsided-Mirror-6611**（3 分） · 2026-09-17T20:52:01+08:00：

For anyone curious: the map in the screenshot is part of a small static page about the setup, [khurana.dev](https://khurana.dev).

**wenestvedt**（1 分） · 2026-09-17T20:57:42+08:00：

I run BirdNETPi at my house and it is, indeed, *really* fuckin cool.

I used a super cheap USB mic, and it's been fine.

Every few weeks I go through the menu and click on the "update" button, but otherwise I just check it and browse the sounds & images.

**Nix-geek**（1 分） · 2026-09-17T20:59:47+08:00：

I'm using this : https://www.amazon.com/dp/B00YUU3KC6?ref_=ppx_hzsearch_conn_dt_b_fed_asin_title_33&th=1

TP Link USB to Ethernet Adapter.  It's been years in use with zero issues.

**crashtheparty**（1 分） · 2026-09-17T22:44:28+08:00：

Is your Immich library importing to Nextcloud? If so, why? I use both and I’m curious.

**Lopsided-Mirror-6611**（1 分） · 2026-09-18T00:04:32+08:00：

Not importing. The folder where Immich keeps the files is also mounted in Nextcloud as a read-only external storage folder, so I can get to the same files from there too.

The reason is sharing. My Immich isn't public, so it isn't set up for sharing with other people. If I want to share a folder of photos with someone, I share it from Nextcloud with a link. Immich handles the backup, search and faces, and Nextcloud handles the sharing.

**crashtheparty**（1 分） · 2026-09-18T03:46:59+08:00：

Ooooh ok thanks for explaining. I set my Immich up to be able to share from directly with my domain. Thanks!

**Lopsided-Mirror-6611**（1 分） · 2026-09-18T04:09:45+08:00：

How are you securing it? I keep mine behind Cloudflare Access, which also means I can't share links from Immich with someone who is not added to my Cloudflare Access list. That is why I share through Nextcloud.

[Immich docs seem to discourage exposing the web interface:](http://docs.immich.app/guides/remote-access/)

>Depending on your configuration, both the Immich web interface and API may be exposed to the internet. Immich is under very active development and the existence of severe security vulnerabilities cannot be ruled out.

**WimmoX**（1 分） · 2026-09-18T05:11:04+08:00：

Awesome setup! Astounding what you can run on old hardware; my brand new Synology (2024, ok not really *brand* new, but still) has lesser specs than your Mac Mini.

**WimmoX**（1 分） · 2026-09-18T05:13:13+08:00：

Looks great!! Since you’re already into connecting external stuff to your setup, take a look at LoRa WAN communication, if you need another rabbithole to dive into

**Lucefin**（1 分） · 2026-09-18T06:26:02+08:00：

I never thought to run Linux on my 2012 Mac mini. Thanks for the idea!

**desucca**（1 分） · 2026-09-18T09:04:51+08:00：

Wait.. if I've got a couple unifi cameras aimed at my pond, could the mic in then be used with this birdnet thing you run?

**JhnWyclf**（1 分） · 2026-09-18T14:09:42+08:00：

I ask because I have a Terramaster DAS and have a huge problem with it dropping off my Mac mini regardless of the power/sleep settings I enable. I was wondering if you ever had problems with your setup.

**Ai_MOON_SHOT**（1 分） · 2026-09-18T15:18:27+08:00：

Why would i host Stirling PDF, is that needed to view PDFs in Paperless or how would that work ?

**codeedog**（1 分） · 2026-09-18T15:59:26+08:00：

I’ve got four late 2012 Mac minis with maxed out 16gb memory and data doublers with SSDs of various sizes all running FreeBSD. My oldest is my current NAS, but I’m migrating off it to a more powerful machine. The current will become a backup onsite. A second one will become a test machine bootable into Linux, FreeBSD and macOS. I have another one offsite paired with another device as my offsite backup. Finally, the fourth mini is a backup machine for my son at his apartment.

They’re fantastic.

**Irratiq**（2 分） · 2026-09-18T20:07:16+08:00：

Yeah, old Intel Mac minis are ridiculously good little homelab boxes once you throw Linux Proxmox on them

**Lopsided-Mirror-6611**（1 分） · 2026-09-18T21:26:55+08:00：

Paperless has its own viewer and does its own OCR. Stirling does two jobs for me:

1. **Double-sided scanning:** My scanner's document feeder only scans one side. I have created three network folders where I can send the scans directly from the printer. One is just the inbox for Paperless, used for single or one-sided documents. The other two folders are "front" and "back". So I scan the stack once for the fronts, flip it, and scan again for the backs. A small script watches both folders, sends the two halves to Stirling's API to merge them and put the pages in order, and drops the finished PDF into the inbox folder for Paperless to consume. (I learnt today from another [post ](https://www.reddit.com/r/Paperlessngx/comments/1wjl2c1/comment/pajdx86/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)that [paperless has a native feature for collating](https://docs.paperless-ngx.com/advanced_usage/?__cf_chl_tk=P5ROQTshfzbvfeVL2J.cHMTuEvNb8S8p416QE4qQrM0-1789737829-1.0.1.1-VgDQ9pLIXZ3ZpbjG0r68hp.yXhaq3TE31FX8LVjXq6I#collate), I need to check that out.)
2. **Any PDF jobs:** merging, splitting, compressing, signing, filling forms, redacting. All the things people usually do on free websites that could potentially keep a copy of your file.

**Lopsided-Mirror-6611**（1 分） · 2026-09-18T21:30:11+08:00：

Thanks! Uh oh, that does sound like a rabbit hole 😄 What do you use it for? Any good starting point you'd recommend?

**Ryan739**（1 分） · 2026-09-18T23:58:33+08:00：

Where can I find one of these "piles?"

**Embarrassed-Yak-1932**（1 分） · 2026-09-19T21:10:50+08:00：

I am not all to familiar with any selfhosting, but could you have run this setup also with a new macmini and just macOS? Or does it have to be Linux? Not hating on Linux, just wondering. Thanks anyway! 🙋🏼‍♂️

**JackDaxter**（1 分） · 2026-09-19T23:52:44+08:00：

For meals, I'm creating [Cuicuit](https://cuicuit.laclau.dev) 🐥 if you'd like to try and open & extensible recipe app + API + MCP :)

**PontyPonty**（1 分） · 2026-09-20T01:27:17+08:00：

2012 is Intel

## 关联链接

- https://www.reddit.com/gallery/1wi4jnj

## 导航

- 项目页：[[80-归档/项目/reddit.com_52615efa]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
