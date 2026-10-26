---
type: "corpus"
item_id: "564981b43eadffcb"
title: "Custom NVR / Camera system build plan , i'd appreciate some feedback"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1x6wiiq/custom_nvr_camera_system_build_plan_id_appreciate/"
author: "LocksmithCultural968"
published_at: "2026-10-16T04:22:16+08:00"
captured_at: "2026-10-26T09:43:54+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-26"
pub_day: "2026-10-16"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Need Help
metrics: {"score": 3, "comments": 11, "upvote_ratio": 0.8}
comments_count: 11
comments_total: 11
discovered_via: "reddit:14d+settle10"
---

# Custom NVR / Camera system build plan , i'd appreciate some feedback

> [!info] 一句话导读
> I’m in the process of planning a home security camera setup and wanted to get some feedback on my hardware choices, OS choices, and my operational blueprint—spe…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1x6wiiq/custom_nvr_camera_system_build_plan_id_appreciate/>
> 指标：得分=3 · 评论=11 · 赞踩比=0.8
> 作者：LocksmithCultural968　|　发布：2026-10-16T04:22:16+08:00
> 项目链接：—
> 采集：2026-10-26T09:43:54+08:00　|　id：`564981b43eadffcb`

## 正文

I’m in the process of planning a home security camera setup and wanted to get some feedback on my hardware choices, OS choices, and my operational blueprint—specifically how I plan to configure, host, and run everything before pulling the trigger on this. 

I’m planning on using a Dell Optiplex 700 Micro to be my NVR. I'm pairing it with a PoE Switch (Netgear GS308PP PoE+ 8-port gigabit switch) and installing an SSD drive, probably 1 TB (could I go lower than 1 TB?), for operating systems, 3rd-party VMS video processing, AI model processing, etc and having a dedicated HDD 3.5 or 2.5 for 24/7 continuous long-term stream storage. For my OS and VMS software, I'm thinking of using a Frigate running via Docker container. I've been reading a lot, and I've been seeing Linux-based OS. The Debian/Ubuntu distro is efficient, lightweight, and stable. Better than Windows So I'm thinking of going that route to run my system. I'm wondering if the Dell OptiPlex 7000 can handle and do everything I'm planning to do. Could it handle continuous 16MP 180° panoramic streams? which the cameras I want to use have the capability of.

My plan regarding my usage and intent is to start with 4 cameras and expand to 5 or 6 in the future and to have 24/7 continuous recording, sub-stream AI object detection (person/vehicle/pet), and high-resolution event recording.

My Planned Hardware 

**NVR Host:** Dell OptiPlex 7000 Micro (12th Gen Intel Core i5/i7)

**OS / Software:** Ubuntu Server / Debian running **Frigate NVR inside Docker**

**Network / PoE Switch:** Netgear GS308PP (8-port Gigabit Unmanaged PoE+, 83W budget)

**Primary Drive (SSD):** 1TB NVMe M.2 SSD (for OS, Docker containers, VMS database, sub-streams, AI model processing, and alert clips)

**Secondary Storage (HDD):** External powered 3.5" Surveillance HDD (WD Purple / Seagate SkyHawk) dedicated strictly to 24/7 continuous main-stream video retention

**Cameras & Stream Workload:**

* **Cameras:** 4 cameras to start, expanding to 5 or 6 in the future.
* **Resolution / View:** 4 of the planned cameras will be high-bitrate 16MP 180° panoramic streams (H.265).
* **Tasks:** 24/7 continuous recording, sub-stream AI object detection (person/vehicle/pet), and high-resolution event recording.

Questions I have 

1. Is everything I planned feasible?
2. Can I go lower on the SSD, maybe 500 GB? Do I actually need 1 TB? 

Is my plan alright? Does anyone run a similar micro server setup?   I would appreciate feedback; thank you!

## 评论（11/11）

> **asimovs-auditor**（1 分） · 2026-10-16T04:22:26+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **LocksmithCultural968**（1 分） · 2026-10-16T04:24:24+08:00　
> I used AI to research the subject im trying to talk about

---

> **Other_Criticism_4285**（0 分） · 2026-10-16T04:38:30+08:00　
> that optiplex micro gonna struggle with four 16MP streams, even if you use sub streams for detection the decoding alone will murder that little cpu

---

> **ethansky**（0 分） · 2026-10-16T04:39:58+08:00　
> Bot ^

---

> **LocksmithCultural968**（1 分） · 2026-10-16T04:42:15+08:00　
> How do u know it’s a bot ?

---

> **GolemancerVekk**（3 分） · 2026-10-16T04:55:28+08:00　
> For the OS drive no you don't need 2 TB, I run a lot of apps on only 128 GB.
>
> I'm not seeing a GPU in the hardware. Without it detection and encoding are going to be very taxing and frankly I don't think the CPU can cope. Perhaps if the cameras can handle the detection themselves but even so encoding multiple high quality streams 24/7 is a bit much.
>
> I'm also not seeing anything about the camera makes and models, what features they have (RTSP?) and how much you trust them on your network. Are they going to be plugged *only* into the NVR (via the switch)? How will you access the NVR from the rest of the LAN? Give some thought to VLANs and network permissions / isolation.

---

> **fernandops**（1 分） · 2026-10-16T07:27:06+08:00　
> Pick the retention period before sizing the recording drive. For continuous recording, 1 Mbps is about 10.8 GB per day per camera. Multiply that by the actual configured bitrate, camera count and days you want to keep, then leave some headroom. “16MP” alone won’t tell you how much storage you need.

---

> **LocksmithCultural968**（2 分） · 2026-10-16T09:22:24+08:00　
> Thanks for commenting ! The OptiPlex 7000 has an integrated GPU ( UHD 770) the processor for that pc has is 12th gen Intel i5-12500T 6 core / 12 thread. From what I've read Frigate ( 3rd party VMS ) will use a downscaled , lightweight stream for AI scanning and the main high resolution stream will be directed / passed through to the external HDD (Which I plan to do) . So I think the CPU will be okay but I plan to start with 4 cameras (Reolink DUO V3 16MP 180° Panoramic capability  )  and later expand to  5 or 6 ( Other brand type cameras)  which is a lot. Maybe the GPU wouldn’t be able to handle ( isn’t built for that much work)  ? Maybe 4 continuous/ simultaneous monitored downscaled streams is already a lot  ?The Reolink Duo v3 supports RTSP and regarding if I trust them on my network , Is there something I should be wary about. I do know Reolink is a chinese brand , have there been privacy problems?  I do plan to have the cameras plugged to the PC (NVR) via the switch only ! Is there something I’m doing wrong / missing ? I hadn't considered anything about VLAN, I didn’t even know what that was. But now from reading it's a great idea and something I'm going to work to implement in my system.I don’t even know how I'm going to access the nvr from the rest of the LAN , I've got a lot of homework to do.

---

> **Joncallim**（1 分） · 2026-10-16T15:32:17+08:00　
> Worth checking the 83W PoE budget against the cameras’ maximum draw with IR on, including the two you might add later.

---

> **GolemancerVekk**（1 分） · 2026-10-16T18:33:10+08:00　
> If the cameras are only plugged into the NVR and it acts as a router for them it would be ok-ish. See if you can set the NVR to also not let them connect outside or to each other, only allow connections to be initiated from the NVR to the cameras.
>
> You will still need to pass through connections from the LAN to the cameras if you want to use the phone app to manage them, and it might be required for some camera makes.
>
> Also, of you plan to connect the NVR to both the camera switch and to the LAN you either need two Ethernet connectors and two wires, or you'll need to figure out tagged VLANs, in which case the NVR and the switch would go into the LAN router which would sort them out. In that case you'd need capable firmware on the router, such as openwrt.
>
> As a rule of thumb I don't trust any device with its own firmware on my LAN. Cameras in particular are notorious for phoning home and all kinds of shenanigans. I want then to sit there without connecting to anything, and only allow the NVR and maybe a phone app to connect to *them*.

---

> **Ill_Leader_7104**（1 分） · 2026-10-16T19:15:15+08:00　
> Biggest thing people underestimate with panoramic cams is the bitrate. Do the math on storage, 4 streams at 16MP can easily eat 15-20TB a month of continuous recording. Make sure your retention expectations match your HDD size.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
