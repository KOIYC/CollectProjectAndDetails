---
type: "corpus"
item_id: "38d2635e72f0ec13"
title: "Show HN: Computer use on the phone itself: a 2B model that operates Android apps"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50180190"
project_url: "https://getopposable.com/blog/computer-use-on-the-phone"
author: "erikkannike"
published_at: "2026-10-21T12:59:58Z"
captured_at: "2026-10-22T09:46:18+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-22"
pub_day: "2026-10-21"
tags:
  - 语料
  - hn_show
  - author_erikkannike
  - story_50180190
  - show_hn
metrics: {"points": 12, "comments": 2, "engagement_velocity": 12}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Computer use on the phone itself: a 2B model that operates Android apps

> [!info] 一句话导读
> Skip to content Reval Labs Get started Pricing How it works Recorded runs FAQ Blog Investors Menu Get started Pricing How it works Recorded runs FAQ Blog Invest…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50180190>
> 指标：点赞=12 · 评论=2 · engagement_velocity=12
> 作者：erikkannike　|　发布：2026-10-21T12:59:58Z
> 项目链接：<https://getopposable.com/blog/computer-use-on-the-phone>
> 采集：2026-10-22T09:46:18+08:00　|　id：`38d2635e72f0ec13`

## 正文

Skip to content Reval Labs Get started Pricing How it works Recorded runs FAQ Blog Investors Menu Get started Pricing How it works Recorded runs FAQ Blog Investors Mac app Account Account Get the app
Contents
 TL;DR
 Model and runtime
 Step time on CPU
 Vision encoder on the NPU
 Accuracy on held-out tasks
 Limitations
 Trying it
 Blog · 21 October 2026 · 4 min read
 Computer use on the phone itself: a 2B model that operates Android apps
 Erik
 Opposable is an Android app that reads the screen through the accessibility service and taps and types in any other app. Claude, ChatGPT or Codex can drive it from a computer, and when none of them is connected, a 2-billion-parameter screen model runs the same loop on the phone with no server involved.
 The on-device agent opening Clock and switching to the stopwatch, with no model outside the phone. Android emulator, real time, each step's timing on the right. # TL;DR
 The model is GUI-Owl 1.5 2B in 4 bits on llama.cpp. On a Mac M2 CPU with 4 threads one step takes 7.3 s, down from 10.6 s, at the same accuracy on our 36-screen test set. Half of that step is the vision encoder, and on a Galaxy S25's NPU the encoder runs in 236 ms against 3.9 s on the M2.
 One step of the loop, animated at its real speed on the Mac M2 CPU: 3.6 s to encode, 2.5 s to prefill, 1.1 s to decode, then the tap. # Model and runtime
 GUI-Owl 1.5 comes from Alibaba's Mobile-Agent team. It is a Qwen3-VL fine-tune that looks at a screenshot and answers with one action. We run it in the app through llama.cpp and its multimodal library, quantised to 4 bits: 1.05 GB for the language model and 445 MB for the vision encoder. Both load once and stay in memory between steps.
 The model only sees tasks the app can't do another way. About forty common ones, like setting an alarm, texting a contact or switching on Wi-Fi, run as fixed code with no model, and routines that a large agent worked out earlier replay from the text on the screen.
 # Step time on CPU
 A step is three stages. The vision encoder turns the screenshot into image tokens, the language model reads them along with the task (prefill), and it writes about 45 tokens: a sentence saying what it intends to do, then a JSON tool call. With nothing optimised, on the M2 the encoder took 4.6 s, prefill 4.3 s and decode 1.7 s, 10.6 s per step, and the model got 27 of the 36 graded screens right.
 Step time on the M2 CPU by stage, before and after the CPU work. Our measurements on the 36-screen graded set. Cropping the status bar, navigation bar and keyboard out of the screenshot cut the image before encoding. After the encoder, tokens for patches of flat background that don't border anything are dropped, and the rest keep their original grid positions, so the model sees the same layout with 25 to 40% fewer tokens. That raised accuracy to 28 of 36. The 900-token system prompt is prefilled once and its KV cache kept. At the 400 image tokens the app uses, a step takes 7.3 s and scores 27 of 36.
 A simplified screen. Status and navigation bars are cropped before encoding, and flat-background tokens with no neighbouring content are dropped before prefill. The model states its intent before coordinates, for example "Action: Click the Files app icon." When that sentence matches exactly one element in the accessibility tree, the app taps the element and stops generating. On the emulator those steps decoded in 0.8 to 1.3 s instead of 2 to 4 s. With all of this in place the encoder took 3.6 of the 7.3 seconds.
 When the model's sentence matches exactly one element on screen, the app taps it and the coordinates are never generated. # Vision encoder on the NPU
 We exported only GUI-Owl's vision tower to ONNX: a 24-layer ViT with its mergers, about 0.4 billion parameters, at a fixed input of 416 by 960 pixels. One screen at that size is 542 billion multiply-accumulates. Qualcomm AI Hub compiled it for the Galaxy S25 (Snapdragon 8 Elite) and ran it on a real S25 in Qualcomm's device lab.
 One step on the M2 CPU by stage, and the vision encoder alone on the M2 and on the S25's NPU. In fp16 the encoder ran in 236 ms with all 873 operations on the NPU, about 16 times faster than the M2's 3.9 s. 8-bit weights with 16-bit activations were faster at 213 ms but drifted from the reference output, cosine 0.978 to 0.985 against 0.992 to 0.996 for fp16, and the model's taps depend on small screen details, so the app uses fp16. Fully 8-bit and 4-bit versions scored 0.67 to 0.90. The first load takes 72 s while the NPU prepares the graph, once per install, and 0.39 s after that.
 Encoder precision on the Galaxy S25 NPU (Qualcomm AI Hub): inference time, and how close the output stays to the reference. fp16 is the only version above the 0.99 the app requires. The NPU returns the same float array as llama.cpp's own encoder, so pruning, positions, the cache and the early exit work unchanged. At startup the app tries the NPU, then the GPU through LiteRT, then the CPU, and an encoder is used only if it passes a self-test on a bundled screenshot (cosine 0.97 or better against the CPU encoder) and is faster than the CPU. The 640-token input size failed to compile for the NPU, so steps that need it still encode on the CPU.
 How a phone ends up with an encoder. Each candidate has to pass a self-test at first load, and the CPU path always works. # Accuracy on held-out tasks
 On eight tasks the model had never been tuned on, run on the emulator twice each, giving it the whole task succeeded 4 and 3 times. Giving it one subgoal at a time and checking each claimed success against the accessibility tree before the next subgoal succeeded 6 times in both rounds.
 Eight held-out tasks on the Android emulator, two rounds each, before and after subgoals with on-screen verification. # Limitations
 Only Snapdragon has an NPU build so far. Pixel phones need a separate compile for Tensor, and MediaTek and Exynos need their own, so those phones fall back to the GPU or CPU. The model is also much weaker than a cloud model on apps it hasn't seen, and the app hands those tasks to Claude, ChatGPT or Codex when one is connected.
 # Trying it
 The Android app is free at getopposable.com. The screen model is a 1.5 GB download from its settings, and the same screen shows which encoder your phone picked and how long a screen takes to encode. I'd like to hear both from your phone, at hello@getopposable.com.
Get the app
Reval Labs Opposable is a Reval Labs project: computer use for phones.
Product
 Get started Pricing How it works Recorded runs Company
 Blog Investors Press Contact
 hello@getopposable.com Privacy Terms
 © 2026 Reval Labs

## 评论（2/2）

> **bestony** · 2026-10-21T13:23:28.000Z　
> 这个模型针对不同的应用会自己兼容么？还是需要参与到训练当中？

---

> **voidnullvalue** · 2026-10-21T16:43:26.000Z　
> Why would I use this over ADB?

## 导航

- 项目页：[[10-项目/getopposable.com_d9e9a40e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
