---
type: "corpus"
item_id: "d0c73a06b89a5ff5"
title: "Show HN: Open-source private home security camera system (end-to-end encryption)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48330192"
project_url: "https://github.com/secluso/core"
author: "arrdalan"
published_at: "2026-05-29T22:32:29Z"
captured_at: "2026-09-21T01:43:42+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-05-29"
tags:
  - 语料
  - hn_show
  - author_arrdalan
  - story_48330192
  - show_hn
metrics: {"points": 137, "comments": 28, "engagement_velocity": 137}
comments_count: 28
comments_total: 28
discovered_via: "hn:show_hn:144d"
---

# Show HN: Open-source private home security camera system (end-to-end encryption)

> [!info] 一句话导读
> Hey everyone,I previously introduced an open source private home security camera in 2024, which uses OpenMLS for end-to-end encryption: https://news.ycombinator…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48330192>
> 指标：点赞=137 · 评论=28 · engagement_velocity=137
> 作者：arrdalan　|　发布：2026-05-29T22:32:29Z
> 项目链接：<https://github.com/secluso/core>
> 采集：2026-09-21T01:43:42+08:00　|　id：`d0c73a06b89a5ff5`

## 正文

Hey everyone,I previously introduced an open source private home security camera in 2024, which uses OpenMLS for end-to-end encryption: https://news.ycombinator.com/item?id=42284412.It was called Privastead then and it's now renamed to Secluso.John Kaczman found my project from here and has been working on it with me over the last year and half. We've made a lot of improvements to the software, which we would like to share with you:- You can now set this up on your Raspberry Pi in less than 5 minutes with no technical expertise using our easy-to-use GUI deploy tool. We've put together a comprehensive build-your-own guide that walks you through the required steps (you can find a link at the top of the repository README).- We use a customized, minimal OS based on the Yocto project for the camera.- Every part of our stack except for the iOS app has reproducible builds. This includes our Android app, camera/server binaries, deploy tool, and the aforementioned OS.- We've re-designed our mobile app, which is now on the iOS App Store and Google Play store.- We now support UnifiedPush for more privacy-preserving push notifications.Looking forward to seeing what you all think!

## 评论（28/28）

> **wmf** · 2026-05-29T22:55:34.000Z　
> What's the difference between the hub and the server?

---

> **blitzo** · 2026-05-30T00:08:48.000Z　
> I'm curious about the Yocto based OS. Can you tell us about the architecture? How small the LOC is and how much customization has been done if it based from existing stacks?

---

> **eichin** · 2026-05-30T00:25:25.000Z　
> Ah, the name is a near-miss vs https://secuso.aifb.kit.edu/english/105.php (the SECurity USability SOciety research group at Karlsruhe) that makes the "Privacy Friendly Apps" suite for Android. (I don't think there's any actual confusion, it was just a "why did that sound familiar" reflex :-)

---

> **josh3736** · 2026-05-30T01:28:34.000Z　
> What wasn't immediately clear to me is that you're meant to set up Raspberry Pis with a Pi camera attached, and that serves as the camera device. This then provides E2E encryption directly between the Pi and the Secluso mobile app via a cloud relay service that just shovels the encrypted bytes.Contrast with https://frigate.video/, which is a locally installed NVR server that pulls camera feeds over the LAN (from a very wide range of off-the-shelf IP cameras) and does all kinds of really neat local processing to do things like (optionally hardware-accelerated) object and audio detection, face recognition, ALPR, semantic search over recorded video, and more — while still maintaining similar privacy guarantees.It's great that you've done reproducible builds for camera firmware, since that means you don't have to trust a shady IP camera vendor to be competent. Of course, with off-the-shelf stuff, you can largely avoid the security issues there by putting your cameras on a VLAN that can only reach your NVR.What I don't get is why there needs to be a cloud relay involved at all. If you're fully E2E encrypted anyway, just have the app communicate directly with the camera via STUN.I see you're planning on selling the preassembled hardware. There's definitely something to be said for "buy this device, download app, done" ease of setup for the wider market that meaningfully improves their privacy over Ring/Nest/et al. But for the power user and self-hosting crowd, I think Frigate makes a lot more sense.

---

> **ultrarunner** · 2026-05-30T02:25:09.000Z　
> This looks like a great project at first glance. One thing I did not see answered was how storage is handled. Is there a way to view historical video (even an hour ago)?

---

> **fjfaase** · 2026-05-30T06:54:40.000Z　
> Are there also open-source solutions without dependency on server in the cloud and that depend on internet connection? I am looking for a total home solution where I can communicate with doorbel through laptop with headset.

---

> **Keyb0ardWarri0r** · 2026-05-30T07:34:40.000Z　
> This is great, congrats!Do you think it would be possible to use ESP32 (RISC-V CPUs) based cameras?Both for cost reduction and availability of the hardware reasons.Maybe with a ChaCha20-based cipher instead of AES?

---

> **HelloUsername** · 2026-05-30T07:58:34.000Z　
> Why not release the iOS app in all regions?

---

> **Jemm** · 2026-05-30T13:14:41.000Z　
> Paint point on most systems is the camera itself. Seems like every Chinese ip camera has some 'ecosystem'. Does you system use any cameras other than Raspberry Pi?

---

> **bitbasher** · 2026-05-30T22:28:20.000Z　
> Do any of these NVR solutions offer police/authority notifications when alerts trigger and you are not home? It's the one thing that keeps me tied to a cloud provider.

---

> **armx40** · 2026-05-30T23:06:29.000Z　
> Guys if you need ESP32-P4 based IP cam solution with PoE support and optional edge TPU. Just 50*60mm footprint. Full firmware installed (or if you need without firmware). Let me know at info@c3rl.com. A proper IP camera with free python scripts to discover and configure the camera.

---

> **tamimio** · 2026-05-31T06:39:01.000Z　
> Having a rpi for each camera is an overkill. What I found the best approach for private CCTV is getting a cheapo camera (like Cinnado D1, I think I got it for $2 each, or go high end) and install thingino, then connect all to frigade on a separate vlan, accessible through VPN. You can use wired cams for even better security.I still think thingino needs a lot, but it does the job so far.

---

> **arnabdey0503** · 2026-05-31T08:59:35.000Z　
> Do you have plans to add smart features like pet detection, etc.?

---

> **arrdalan** · 2026-05-29T22:59:54.000Z　
> The camera_hub runs in the camera. It records videos, encrypts them, and sends them to the mobile app. The server is a relay in the cloud. It transfers encrypted videos from the camera to the mobile app.

---

> **jkaczman** · 2026-05-30T00:40:57.000Z　
> Hi u/blitzo, thanks for the reply! I'm the other contributor mentioned in the post (John Kaczman).In case you're not familiar with the Yocto Project, it's designed to be a tool/template for developers (like Ardalan and I!) to use to create custom Linux images for embedded devices (in this case, a Raspberry Pi).It works off of distributing layers/recipes (these "templates") in open-source repositories for re-use among such developers that can be very easily baked in and customized if necessary.Our current usage of it is relatively small. Our OS codebase is roughly ~1,000 LOC of a few recipe modifications (e.g. for fixing reproducible build issues, some minimizations, necessary dependencies we need), and, of course, integrating our camera_hub binary and updater binary (as well as their respective system services). We also bake in a custom rpicam-apps (the library responsible for driving camera feeds into the app), which was modified to be more performant in our use case (specifically, we modified it to add a secondary UNIX domain socket channel to send raw images simultaneously with the H.264 stream, so that we wouldn't need to decode them separately). Additionally, there's ONNX Runtime, which I mention below.In the image itself, we've added two partitions: a data and provisioning partition. The data partition is designed to separate the mutable data (the state files for our camera binary) against the rest of the root filesystem. The provision partition is used by the deploy tool to inject a random camera_secret in as the pre-shared key (PSK) used to initiate pairing in OpenMLS (for our E2EE).We have a lot of future work in store for this Secluso OS! A few things I'm working on right now are a read-only root filesystem (through squashfs), hardening the kernel, and getting rid of a massive dependency we currently rely on (ONNX Runtime) for machine learning. We've been working with burn, a popular Rust machine learning library, to optimize their "burn-flex" crate to match the performance of ONNX Runtime for the model we use for object detection. After that's done, half of the dependencies used by the OS will be able to be removed! (as ONNX Runtime drags in things such as python).Please let me know if you have any questions!

---

> **arrdalan** · 2026-05-30T03:34:19.000Z　
> There are two comments/questions here and I'll try to address them one by one.Secluso vs. Frigate: I think you correctly mentioned some of the differences. We intend Secluso to be replacement for Ring-like WiFi cameras. Therefore, it needs to be easy to set up and use and provide similar functions to a Ring camera: the user plugs in the camera, opens the app, scan a QR code and perform a pairing process, and the camera is ready to use with its strong end-to-end encryption. The self-hosted version of Secluso requires a few more steps, but we've tried to automate it as much as possible. Home Assistant and Frigate are great platforms that are capable of providing good privacy (although they don't support advanced end-to-end encryption that Secluso does with forward secrecy and post-compromise security through MLS), but they require several steps, e.g., prepare/configure the IP camera, install and configure Frigate, integrate Frigate with Home Assistant, and configure remote viewing via cloud relay or VPN. Also, they are typically used with wired (Ethernet) IP cameras. WiFi IP cameras are possible but the RTSP stream between the camera and hub will be unencrypted, which might be vulnerable to eavesdropping.Need for cloud relay: We have considered STUN and we are planning to deploy MLS over WebRTC for livestreaming (using the DAVE protocol) to improve the livestream performance. But this doesn't completely eliminate the need for a relay. If a STUN connection cannot be made due to some restrictions in one of the networks (that the camera and app are connected to), we will need to fall back to the relay. Also, if the phone is off/disconnected when an event video is recorded, we would like to transfer it (encrypted) to the relay ASAP in case something happens to the camera (e.g., it's taken by the intruder).

---

> **arrdalan** · 2026-05-30T03:07:57.000Z　
> The videos are stored in the mobile app and you can view them when you need. The camera captures videos when it detects an event, e.g., a person, encrypts them, and sends them to the mobile app. The app decrypts them and stores them locally, allowing the user to view them when needed. The app also allows for livestreaming and it keeps the livestreamed video locally as well.

---

> **flowerthoughts** · 2026-05-30T07:40:02.000Z　
> When embedded SoCs are _much_ more likely to have AES accelerators, why are you looking to ChaCha20 for encrypting video?

---

> **arrdalan** · 2026-05-30T08:00:58.000Z　
> ESP32: We haven't tested them. I would guess that they won't be able to handle the workload (on-device AI, encryption, and video encoding if there's no hardware encoder).Ciphersuite: We use OpenMLS and we can choose any of the ciphersuites supported by it. We are using its post-quantum secure ciphersuite (MLS_256_XWING_CHACHA20POLY1305_SHA256_Ed25519).

---

> **jkaczman** · 2026-05-30T09:29:46.000Z　
> Hi u/HelloUsername, thanks for the question.Apple has not approved our documentation for 23 countries in Europe yet. They require it for the European Union Digital Services Act [see https://developer.apple.com/help/app-store-connect/manage-co...]. Note that the Android app is available in these (both in the Google Play Store as well as Obtainium).France, specifically, is excluded due to needing a specific French encryption declaration form. [https://developer.apple.com/help/app-store-connect/manage-ap...] - as we do not have a lawyer to consult, we decided it would be best to hold off on this to be certain we do it right.For some other specific countries outside of Europe, such as North Korea, we are required to abide by export laws in the US. We tend to try to go on the safe side when excluding, as we do not have a lawyer to consult.Please let me know if you have any other questions!

---

> **jkaczman** · 2026-05-30T13:38:08.000Z　
> I know that there exists projects such as https://github.com/OpenIPC and https://github.com/themactep/thingino-firmware. These allow you to replace the firmware running on some of the Chinese IP cameras with an open-source alternative.Our project specifically is only meant for Raspberry Pi Zero 2W. We decided on this early on due to Raspberry Pi being a safer source for hardware, and it allows much more customization (e.g. custom 3D printed cases, our HAT, etc). We also wanted it to be a WiFi camera that's super easy to setup and doesn't require technical knowledge to use.

---

> **arrdalan** · 2026-05-31T22:41:53.000Z　
> Our on-device AI is able to detect people, pets, and vehicles. We have tested people detection and it works well. We haven't really tested the other two.

---

> **tmikaeld** · 2026-05-30T08:56:30.000Z　
> So only when viewing the steam or also receiving in background? If in the background that means wiping the battery in no-time.

---

> **Keyb0ardWarri0r** · 2026-05-30T09:45:08.000Z　
> RSIC-V based are probably the most widely available microcontrollers / dev boards, but they unfortunately don't have AES accelerators.
> On the other hand, ChaCha20 (or ChaCha12) run great on them.

---

> **Keyb0ardWarri0r** · 2026-05-30T09:47:52.000Z　
> From what I understand, some camera modules for ESP32 have built-in video encoding, so basically the ESP32 will only have to manage the encryption + network.If you are interested, take a look at what SeeedStudio are doing. I think It's worth exploring for very cheap cameras, but yeah, no AI (without an additional accelerator).

---

> **jkaczman** · 2026-05-30T09:49:48.000Z　
> Hi u/tmikaeld, livestreams are available when clicking a button. It is not possible to livestream in the background. That's what motion/object-detection-based events are meant to help augment. When something happens, you'll get a push notification + a video, so that you don't need to look through a very long video to try to figure out when something happens.

---

> **flowerthoughts** · 2026-05-31T10:54:00.000Z　
> I don't follow. I haven't done an exhaustive search, but it seems all esp32, whether xtensa or riscv have AES accelerators. Not sure I've seen a modern 32 bit Arm MCU without it either.

---

> **arrdalan** · 2026-05-30T16:33:28.000Z　
> Will do. Thanks for the suggestion.

## 关联链接

- https://news.ycombinator.com/item?id=42284412.It

## 导航

- 项目页：[[10-项目/github.com_bbef0fe6]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
