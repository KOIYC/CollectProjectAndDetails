---
type: "corpus"
item_id: "acd732f65625e7e1"
title: "Show HN: Jexxa: High Speed on Device Dictation"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49712720"
project_url: "https://jexxa.org/"
author: "sankde"
published_at: "2026-09-15T14:05:42Z"
captured_at: "2026-09-20T14:06:24+08:00"
lang: "en"
kind: "post"
topic: 开发者工具
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_sankde
  - story_49712720
  - show_hn
metrics: {"points": 6, "comments": 18, "engagement_velocity": 6}
comments_count: 18
comments_total: 18
discovered_via: "hn:show_hn:90d"
---

# Show HN: Jexxa: High Speed on Device Dictation

> [!info] 一句话导读
> JEXXA — Dictation that never leaves your Mac

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49712720>
> 指标：点赞=6 · 评论=18 · engagement_velocity=6
> 作者：sankde　|　发布：2026-09-15T14:05:42Z
> 项目链接：<https://jexxa.org/>
> 采集：2026-09-20T14:06:24+08:00　|　id：`acd732f65625e7e1`

## 正文

JEXXA — Dictation that never leaves your Mac

# JEXXA

Dictation that never leaves your Mac.

macOS 14 or later · Apple silicon · version 0.1.10

## Everything happens on your Mac

The model is on your disk. Hold a key, speak, and the words appear where your cursor already is — in any app that takes text.

### Nothing is uploaded

No audio, no transcript. What does leave is small and listed in the privacy policy: your subscription check, update checks, and diagnostics you can turn off.

### Fast enough to think in

Most dictations are typed within a fifth of a second of letting go of the key. No queue, no per-minute cost.

### It learns your words

Names and jargon it gets wrong once, it gets right after you fix it. It tells you what it learned, and you can undo it.

### Take back what you said

Say JX minus one to remove the last line, JX minus two for two, JX clear for the lot.

### See it as you speak

A live preview while you talk, so you know it is hearing you.

### Works with the wifi off

On a plane, on a train, on a bad hotel connection. It does not care.

## Which one do I want?

Same app, same features. The difference is how much of your memory the model needs while it is running.

16 GB or more

3.1 GB download · the more accurate weights

2.0 GB download · smaller weights, leaves your Mac usable

# udbhav-s/password-dungeon

## 评论（18/18）

> **copper-float** · 2026-09-15T14:14:50.000Z　
> One price, indefinitely for the rest of your life. The developer isn't maintaining any infrastructure, there's no ongoing cost whatsoever, so there's no reason for monthly payments.It's just a static file on your own computer that's burning your own CPU cycles. Sorry, but it just feels a bit greedy to me.

---

> **dangoodmanUT** · 2026-09-15T14:29:47.000Z　
> > "Your voice and text never leave the machine"> "Runs on your Mac — no upload, no queue"> $8/month

---

> **hmokiguess** · 2026-09-15T14:47:29.000Z　
> You should include your demo video on your landing page

---

> **woadwarrior01** · 2026-09-15T14:53:42.000Z　
> I spent ~10 minutes looking at it.Vibe-coded website.Both bundles contain quantized versions of the CohereLabs/cohere-transcribe-03-2026 model. The model in JEXXA.dmg is MLX int8 g64 affine quantized. JEXXA-Small.dmg has the same model but MLX int4 g32 affine quantized. There's also an int8 quantized WeSpeaker ECAPA-TDNN speaker-verification ONNX encoder. No acknowledgments for both models (doesn't the Apache 2.0 license require it? WeSpeaker's cc-by-4.0 license certainly does). Both bundles also contain full-blown Python 3.12.8 runtimes with about a dozen packages installed.Apps are unsandboxed menubar apps and also contain PostHog analytics and Supabase auth. So, I wouldn't run it on any of my machines.A few engineering hygiene issues like a .pytest_cache directory, Python code, .DS_Store files, etc.Given the above, I suspect the "I am training better models." is just marketing speak.nb: The demo link without LinkedIn tracking slop: https://www.linkedin.com/posts/sankyde_jexxa-demo-httpsjexxa...

---

> **sankde** · 2026-09-15T14:17:43.000Z　
> I was thinking of such a payment system.
> I would love to offer you that as I am still testing the pricing.Edit: You also would get updates for life.

---

> **sankde** · 2026-09-15T14:21:32.000Z　
> We also have better models in training.
> Also the underlying system would get faster, the models smaller over time along with grammar correction, in voice commands and better live preview models

---

> **vlovich123** · 2026-09-15T14:42:47.000Z　
> They have development costs to pay for which is substantial. Not sure why you are framing it as greedy and complaining it should be free vs celebrating someone putting this out there.

---

> **sankde** · 2026-09-15T14:32:39.000Z　
> Yes, I am training better models.
> On Device Dictation requires more resources than API based systems.My competitor charges more and at the same time the data is being sent to someone else's servers.

---

> **azornathogron** · 2026-09-15T14:30:27.000Z　
> The way this used to be handled is to sell new versions.

---

> **sankde** · 2026-09-15T15:02:35.000Z　
> Thanks.
> I don't want my data, especially voice and text to be sent to servers.
> That's why I built this.I love my competitor's product, but the amount of private data I sent over was really uncomfortable to me.
> Especially when sometimes it included Phone Numbers and some private info.At the same time, tools like mine will fall behind if I don't keep updating the models.

---

> **cipehr** · 2026-09-15T14:55:35.000Z　
> Better models than… whisper, cohere, parakeet v2/v3? Did I miss the comparison on the webpage?Is it just the models I’m paying for, or an app too?I’ve been using anomalyco/HEX and MacParakeet… which are free and work great for my uses…

---

> **sankde** · 2026-09-15T14:59:22.000Z　
> Yes. Newer models is the direction I am going in.
> New Models are expensive.

---

> **woadwarrior01** · 2026-09-15T16:34:19.000Z　
> If you care so much about user privacy, why do you exfiltrate events named "dictation_started", "dictation_completed", "dictation_rejected", "dictation_blocked", "insertion_failed", etc to PostHog, with properties named: "audio_seconds", "latency_ms", "duration_ms", "install_id", etc?

---

> **sankde** · 2026-09-15T15:05:00.000Z　
> Yes, I have used Handy, a lot.
> Open Models need the system around them to keep getting better.
> Also faster.The models you have quoted take a lot of RAM, especially on Mac.
> That's why I am optimizing my models too.

---

> **vlovich123** · 2026-09-15T20:28:32.000Z　
> Because anyone building a system needs performance metrics to understand how it’s behaving in aggregate / if they update the model? With the exception of install_id these all seem innocuous. Install_id is maybe needed anyway for purchase management. Probably could use a session uuid to track the other metrics at the cost of blinding you to being able to find individual customers with a bad experience which is probably much more important for a small player like this.

---

> **woadwarrior01** · 2026-09-16T09:51:06.000Z　
> Apple provides APIs for doing this in a privacy-sensitive way, instead of exfiltrating data like this, carte blanche using PostHog.https://developer.apple.com/documentation/metrickit

---

> **sankde** · 2026-09-16T15:03:14.000Z　
> Yes These metrics are there to check system issues.
> Like Crashes and etc.
> Also I need to check Model performance too.
> However your data is yours, and this data will be anonymized too.
> I really want Jexxa to be private and secure, as I am a heavy user of it too.

---

> **sankde** · 2026-09-16T15:00:09.000Z　
> Thanks for your Feedback.
> More Privacy Improvements, Package Corrections and Attribution Incoming.

## 导航

- 项目页：[[10-项目/jexxa.org_96b74dc4]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
