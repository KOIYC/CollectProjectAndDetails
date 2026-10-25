---
type: "corpus"
item_id: "b1a7799dd082e4ef"
title: "Steam Headless v2 - Amazing!"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1x6nedp/steam_headless_v2_amazing/"
project_url: "https://steamheadless.com/"
author: "tjacoby2006"
published_at: "2026-10-15T22:38:52+08:00"
captured_at: "2026-10-25T23:28:44+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-25"
pub_day: "2026-10-15"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Game Server
metrics: {"score": 92, "comments": 43, "upvote_ratio": 0.9791666666666666}
comments_count: 43
comments_total: 43
discovered_via: "reddit:14d+settle10"
---

# Steam Headless v2 - Amazing!

> [!info] 一句话导读
> I have five kids and the older couple are coming to an age where we occasionally let them play video games. I have been mostly out of the console game, but I ha…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1x6nedp/steam_headless_v2_amazing/>
> 指标：得分=92 · 评论=43 · 赞踩比=0.9791666666666666
> 作者：tjacoby2006　|　发布：2026-10-15T22:38:52+08:00
> 项目链接：<https://steamheadless.com/>
> 采集：2026-10-25T23:28:44+08:00　|　id：`b1a7799dd082e4ef`

## 正文

I have five kids and the older couple are coming to an age where we occasionally let them play video games. I have been mostly out of the console game, but I have a decent Steam library and wanted a way to let them play at the same time. For my proof of concept, I picked up a few copies of Wreckfest and my goal was for all of us to be able to play together, utilizing one machine. Here *were* the specs of the machine when I first set out on this journey-

* AMD Ryzen 9 5900 XT (16c/32t)
* 64GB DDR4 3200
* 2TB WD NVME SSD
* 1x AMD RX 6800 16GB
* 2x NVidia P100 16GB (\~GTX 1080 performance)
* Linux Mint OS

One thing I liked about a containerized solution was that GPUs could be shared between containers (meaning a GPU could run more than one game concurrently) and I could utilize these retired AI GPUs without a display output.

After playing around for some time with Games on Whales/WOLF, I was having some issues with its design. For one, configuring it can be a bit confusing, and WOLF itself launches child docker containers that are not super configurable from a networking perspective (as far as I could tell). Specifically, I had issues with the different containers being able to communicate with each other, and I had some other strange issues with the platform as a whole (sometimes child containers got left running, for example) and it just felt a little clunky (scanning the logs for moonlight pairing codes).

I was considering just splitting it all up into different machines, until I discovered that there was a version 2 of Steam Headless. I had tried the original version and had some issues with audio and a few other things, but this new version looked really polished.

After giving it a quick go and seeing how well it worked with just my own instance, I created two more for the older boys. While the P100s worked fine, I wanted something that used less power at idle and offered additional scaling. It was at this time I discovered some AMD V540 GPUs for $99 each on ebay- I ordered two. The secret sauce here is that each of these is actually 2 GPUs (\~RX 5700) with 8GB of HBM per GPU, so these two add-in cards can be used for 4 instances of Steam Headless while idling at just a few watts. This is going to allow me to scale to more instance without too much concern about crowding GPUs (and 1080p without every detail is fine for their games).

For Steam apps, each child has their own account with the family sharing features and I am utilizing a shared directory to keep disk usage down. I am also emulating some XB360 games from a NAS. Games are streamed via Moonlight to whatever laptop we have laying around or to my Steam Link boxes (though Steam Remote Play also works). With this setup, I have even been able to stream games to myself at work over my lunch break on my phone VPN'd home, and it works great! And in case anyone is wondering, dad gets the RX 6800 to himself 😄 I have another 64GB RAM kit I can throw in if it looks like there is a need, otherwise it serves as a backup since I bought them cheap years ago.

Here is a link to the website (I have no affiliation)- [Steam Headless](https://steamheadless.com/)

Here is my compose today. You may notice I am setting core affinity, and this is because my CPU has 2 CCDs, so I am making sure each container stays within a single CCD.

```yml
name: steam-headless

x-base-service: &base-service
  image: josh5/steam-headless:2
  restart: unless-stopped
  cap_add:
    - DAC_READ_SEARCH
    - NET_ADMIN
    - SYS_ADMIN
    - SYS_NICE
    - SYS_PTRACE
  security_opt:
    - apparmor:unconfined
    - seccomp=unconfined
    - systempaths=unconfined
    - writable-cgroups=true
  cgroup: private
  stop_signal: SIGRTMIN+3
  stop_grace_period: 30s
  pids_limit: 8192
  shm_size: 2gb
  device_cgroup_rules:
    - 'c 13:* rwm'
  tmpfs:
    - /run
    - /run/lock
    - /tmp
    - /dev/input:rw,dev,mode=075


services:
  dad-steamheadless:
    <<: *base-service
    container_name: dad-steamheadless
    hostname: dad-steamheadless
    environment:
      PUID: '1000'
      PGID: '1000'
      DISPLAY_MODE: wayland
      WAYLAND_DISPLAY: wayland-0
      INITIAL_DISPLAY_WIDTH: '1920'
      INITIAL_DISPLAY_HEIGHT: '1080'
      INITIAL_DISPLAY_REFRESH: '60'
      SUNSHINE_NAME: 'Dad'
      XDG_SEAT: ''
      ENABLE_STEAM_SYSTEMD_SERVICE: 'true'
      SHUI_MEDIA_BACKEND: 'gstreamer-vaapi'
      COMPOSITOR_RENDER_DEVICE: '/dev/dri/renderD130'
      ENCODER_RENDER_DEVICE: '/dev/dri/renderD130'
    devices:
      - /dev/dri/renderD130:/dev/dri/renderD130
      - /dev/fuse:/dev/fuse
      - /dev/uinput:/dev/uinput
      - /dev/uhid:/dev/uhid
    volumes:
      - /etc/localtime:/run/host-localtime:ro
      - /sys/devices/virtual/input:/sys/devices/virtual/input:ro
      - dad-steamheadless-state:/var/lib/steam-headless
      - dad-steamheadless-journal:/var/log/journal
      - ~/sambashare/SteamHeadless/homes/dad:/home/steamheadless:Z
      - /var/lib/steamapps:/mnt/games:z
      - /mnt/nas/Multimedia/Roms:/mnt/roms
    networks:
      steam-headless:
        ipv4_address: 192.168.1.3
    cpuset: "0-7,16-23" # Dedicated to CCD 0

  child0-steamheadless:
    <<: *base-service
    container_name: child0-steamheadless
    hostname: child0-steamheadless
    environment:
      PUID: '1000'
      PGID: '1000'
      DISPLAY_MODE: wayland
      WAYLAND_DISPLAY: wayland-0
      INITIAL_DISPLAY_WIDTH: '1920'
      INITIAL_DISPLAY_HEIGHT: '1080'
      INITIAL_DISPLAY_REFRESH: '60'
      SUNSHINE_NAME: 'child0'
      XDG_SEAT: ''
      ENABLE_STEAM_SYSTEMD_SERVICE: 'true'
      SHUI_MEDIA_BACKEND: 'gstreamer-vaapi'
      COMPOSITOR_RENDER_DEVICE: '/dev/dri/renderD128'
      ENCODER_RENDER_DEVICE: '/dev/dri/renderD128'
    devices:
      - /dev/dri/renderD128:/dev/dri/renderD128
      - /dev/fuse:/dev/fuse
      - /dev/uinput:/dev/uinput
      - /dev/uhid:/dev/uhid
    volumes:
      - /etc/localtime:/run/host-localtime:ro
      - /sys/devices/virtual/input:/sys/devices/virtual/input:ro
      - child0-steamheadless-state:/var/lib/steam-headless
      - child0-steamheadless-journal:/var/log/journal
      - ~/sambashare/SteamHeadless/homes/child0:/home/steamheadless:Z
      - /var/lib/steamapps:/mnt/games:z
    networks:
      steam-headless:
        ipv4_address: 192.168.1.4
    cpuset: "8-15,24-31" # Dedicated to CCD 1

  child1-steamheadless:
    <<: *base-service
    container_name: child1-steamheadless
    hostname: child1-steamheadless
    environment:
      PUID: '1000'
      PGID: '1000'
      DISPLAY_MODE: wayland
      WAYLAND_DISPLAY: wayland-0
      INITIAL_DISPLAY_WIDTH: '1920'
      INITIAL_DISPLAY_HEIGHT: '1080'
      INITIAL_DISPLAY_REFRESH: '60'
      SUNSHINE_NAME: 'child1'
      XDG_SEAT: ''
      ENABLE_STEAM_SYSTEMD_SERVICE: 'true'
      SHUI_MEDIA_BACKEND: 'gstreamer-vaapi'
      COMPOSITOR_RENDER_DEVICE: '/dev/dri/renderD129'
      ENCODER_RENDER_DEVICE: '/dev/dri/renderD129'
    devices:
      - /dev/dri/renderD129:/dev/dri/renderD129
      - /dev/fuse:/dev/fuse
      - /dev/uinput:/dev/uinput
      - /dev/uhid:/dev/uhid
    volumes:
      - /etc/localtime:/run/host-localtime:ro
      - /sys/devices/virtual/input:/sys/devices/virtual/input:ro
      - child1-steamheadless-state:/var/lib/steam-headless
      - child1-steamheadless-journal:/var/log/journal
      - ~/sambashare/SteamHeadless/homes/child1:/home/steamheadless:Z
      - /var/lib/steamapps:/mnt/games:z
    networks:
      steam-headless:
        ipv4_address: 192.168.1.2
    cpuset: "0-7,16-23" # Dedicated to CCD 0

networks:
  steam-headless:
    driver: macvlan
    driver_opts:
      parent: enp11s0
    ipam:
      config:
        - subnet: 192.168.1.0/24
          gateway: 192.168.1.1

volumes:
  dad-steamheadless-state:
  dad-steamheadless-journal:
  child0-steamheadless-state:
  child0-steamheadless-journal:
  child1-steamheadless-state:
  child1-steamheadless-journal:
```

## 评论（43/43）

> **asimovs-auditor**（1 分） · 2026-10-15T22:39:03+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **tjacoby2006**（3 分） · 2026-10-15T22:44:23+08:00　
> No AI was used in the creation of this post.

---

> **Lark1ng**（20 分） · 2026-10-15T22:55:10+08:00　
> Damn, that is mighty fine.
>
> I was wondering if a setup like this is actually possible and would run smoothly. My thoughts currently are to buy 1 beefed up server for all my needs and then have only lightweight devices to access it. I guess currently the RAM prices kinda make this an expensive purchase.
>
> Anyway, kudos to your project and apparently it is working really well!

---

> **tjacoby2006**（6 分） · 2026-10-15T23:03:32+08:00　
> Yeah, on this consumer grade stuff it seems to be fine. I occasionally see some micro-studdering in moonlight (though the performance HUD is not revealing a reason), so it is not perfect, but I have been very happy with it overall.

---

> **TheRedcaps**（7 分） · 2026-10-15T23:03:43+08:00　
> Interesting to do this via docker - most people I've seen attempt the gaming server setup are doing full VMs will need to look into this a bit more.

---

> **peter_hungary**（1 分） · 2026-10-15T23:04:23+08:00　
> Is it uses a Moonlight fork with microphone support? Afaik only steam remote play can do that. Not mentioning web camera support (for age verification...),

---

> **Potential-Block-6583**（-5 分） · 2026-10-15T23:10:36+08:00　
> What kind of hardware are you running this on?

---

> **bobbywaz**（1 分） · 2026-10-15T23:11:15+08:00　
> This is pretty awesome, I've had an PowerEdge R720XD for like 10 years in my living room and I finally installed a GTX 1660 in it and bazzite and have been pretty impressed with performance but never thought to have more than one card headless, I have a 3060 in my computer I could also add...

---

> **Icy-Buffalo-1015**（1 分） · 2026-10-15T23:18:56+08:00　
> This is super cool. Hadn’t heard of steam headless only games on whales. Will check this out.

---

> **Squanchy2112**（1 分） · 2026-10-15T23:21:44+08:00　
> I'll have to try this I have failed several times at getting gaming cams for kids working so if really love this

---

> **radakul**（10 分） · 2026-10-15T23:23:03+08:00　
> I'm going to start referring to my nephews and niece as "child #". Thats hilarious 😂  neat project, too!

---

> **SolFlorus**（2 分） · 2026-10-15T23:24:28+08:00　
> Are you single? I can’t imagine my wife being ok with a 720 in the living room. Mine is in a dedicated room in the basement and I can still here it when the load increases.

---

> **tjacoby2006**（7 分） · 2026-10-15T23:29:07+08:00　
> lol I use their names in the real compose, I only took them out for added anonymity 👍

---

> **elgueromanero**（2 分） · 2026-10-15T23:29:48+08:00　
> Very cool!!!! I did something similar albeit not for steam, I run wolf via docker then use moonlight app on apple tv so my kids can play large collection of roms across multiple tvs.  IT also has steam support which plays fairly well!

---

> **radakul**（3 分） · 2026-10-15T23:30:12+08:00　
> Oh I know, but i think you should keep it going. Begin referring to them by their numerical designation. Get them used to when the robot overlords take over 🤣

---

> **bobbywaz**（0 分） · 2026-10-15T23:38:52+08:00　
> I have the L series processors so they are low power, I just have it set to 15% fan speed at all times after boot unless it really really needs it, and it almost never spins up unless I'm gaming. It's no louder than the $360 air purifier next to it.

---

> **Not_a_Candle**（2 分） · 2026-10-15T23:47:59+08:00　
> Enable frame pacing in the moonlight settings. That should calm it down, at least a bit.

---

> **tjacoby2006**（1 分） · 2026-10-15T23:50:54+08:00　
> Thanks for the tip, I will give that a shot!

---

> **C4ddy**（3 分） · 2026-10-15T23:54:35+08:00　
> I think you left one name in there.

---

> **tjacoby2006**（2 分） · 2026-10-15T23:55:57+08:00　
> Good eye, thanks

---

> **wildcarde815**（1 分） · 2026-10-16T00:32:14+08:00　
> Anybody know if this works on a system otherwise running a desktop? I've got a headless sway + sunshine setup running right now but it has a few 'gotchas' that containers would probably help resolve involving sound. Mostly, can you share your user steam folder as an install target I wonder?

---

> **tjacoby2006**（1 分） · 2026-10-16T01:19:39+08:00　
> I am sharing a single steam folder across all the containers, I don't know why you wouldn't be able to do the same with your desktop.

---

> **cardfire**（2 分） · 2026-10-16T01:21:41+08:00　
> Bummed the post got deleted. Sounded  super useful for me and its meat and potatoes is gone.

---

> **tjacoby2006**（3 分） · 2026-10-16T01:34:40+08:00　
> I appealed to the mods, it looks like a Reddit thing, not this sub

---

> **cardfire**（1 分） · 2026-10-16T02:27:41+08:00　
> Can you offer a link to the GitHub or any other posts about it?

---

> **tjacoby2006**（2 分） · 2026-10-16T03:51:15+08:00　
> You find out all about it here: [Steam Headless](https://steamheadless.com/)

---

> **cardfire**（2 分） · 2026-10-16T04:58:55+08:00　
> Oh, all of this is lovely!  I know what I'm doing with my weekend, now.
>
> May you always find the cool spot on your pillow, and may your project level up to the top of search engine results soon.

---

> **Squanchy2112**（1 分） · 2026-10-19T03:38:56+08:00　
> 720 can be pretty quiet with the dell shutup container [https://hub.docker.com/r/spazcatsam/idracquiet](https://hub.docker.com/r/spazcatsam/idracquiet)

---

> **s0n1cm0nk3y**（1 分） · 2026-10-21T23:35:42+08:00　
> Any idea if its EAC friendly? I'm trying to build the same with Nobara after I had issues with proxmox and Windows VMs. Proton handles it, but curious how this does with it.

---

> **tjacoby2006**（1 分） · 2026-10-21T23:39:50+08:00　
> I am not sure if I have a game to test with, but I don't think it is supported base on what Gemini tells me about it ¯\_(ツ)_/¯

---

> **s0n1cm0nk3y**（2 分） · 2026-10-22T00:22:28+08:00　
> Understood. Seems to work on base proton. The issue I ran into under proxmox with either bazzite or windows was it would see a virtualization layer and I'm wondering if thats the case here.

---

> **goodelyfe**（4 分） · 2026-10-22T03:39:16+08:00　
> This is super badass. Hadn't heard of it

---

> **Bladerail**（1 分） · 2026-10-22T09:22:40+08:00　
> Hi, I only just saw this post today and I’m very excited to learn more, but regarding Moonlight micro stuttering, are you seeing that like every second, and what devices are you using to stream from? If it is an Apple product like iPad, disabling airdrop and location services while gaming solved the stuttering for me completely.
>
> Edit: Oops read the post again and you mentioned older laptops or steam boxes

---

> **tjacoby2006**（1 分） · 2026-10-22T09:25:29+08:00　
> It was various windows laptops and my phone. Network was wireless, though even when my laptop showed the symptoms. I think frame pacing will help based on my limited testing on 5g (which has its own inconsistencies)

---

> **Byte-64**（2 分） · 2026-10-22T21:39:59+08:00　
> The advantage I can see is GPU partitioning. Traditionally, with a VM you are restricted to a single GPU for a single VM. Nvidia nowadays supports GPU-P under specific conditions, but Hyper-V doesn't support single USB-Port assignment, so you would need a USB-Controller for each VM (cheaper than a GPU, but also not viable in my situation, as my case is a DAN A4). With Docker, a GPU can be natively shared between containers.

---

> **UnethicalExperiments**（2 分） · 2026-10-22T21:45:11+08:00　
> Same here , I'd love to try this out as I don't game all that often, but when I am it's games with EAC and you cannot get around it detecting you're in a VM. Otherwise I would add it to my gpu node server I have which is all docker containers sharing gpus for various compute tasks

---

> **s0n1cm0nk3y**（1 分） · 2026-10-22T22:38:53+08:00　
> So i can say that Proton has worked with some EAC. It appears this approach does use the latest proton thus it might work.

---

> **tjacoby2006**（1 分） · 2026-10-22T22:49:11+08:00　
> It's a matter of kernel level items from my understanding that are not available to the container, so it will not likely work.

---

> **s0n1cm0nk3y**（2 分） · 2026-10-22T23:04:35+08:00　
> Their site states otherwise.   Im in the middle of configuring seats got my multiple GPUs so ill let you know if its successful

---

> **s0n1cm0nk3y**（3 分） · 2026-10-22T23:10:46+08:00　
> I have a question for you on the GPU allocation. Do you designate user to gpu dynamically (next available) or do you have set seats for each? I'm doing similar with 2x 3060s and a bit confused on seat assignment given my board has one at x8 and one at x4.

---

> **tjacoby2006**（1 分） · 2026-10-22T23:12:43+08:00　
> It is fixed per-seat. Games on Whales is trying to figure out dynamic assignment from what I recall, but this is fixed. If there was some heuristic I wonder how it might work...

---

> **UnethicalExperiments**（2 分） · 2026-10-22T23:58:26+08:00　
> Wanna check out 7 days to die? My wife adores that still and that's one game i do pick up that's preventing me from just throwing my gaming setup in a container or VM.
>
> Best I can pay is some cat tax , or dog tax.
>
> https://preview.redd.it/9xyyn6t0k1xh1.jpeg?width=1840&format=pjpg&auto=webp&s=7c5f86442e3c3d4fdf18af707d4dc0ab73932a81

---

> **s0n1cm0nk3y**（1 分） · 2026-10-24T03:17:31+08:00　
> lol, I'll be testing out dead by daylight, same situation for my lady. Has EAC as the primary issue with my prior Proxmox setup. Working on it now as I speak, with small hurdles of multiple GPUs

## 导航

- 项目页：[[10-项目/steamheadless.com_8d2b3160]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
