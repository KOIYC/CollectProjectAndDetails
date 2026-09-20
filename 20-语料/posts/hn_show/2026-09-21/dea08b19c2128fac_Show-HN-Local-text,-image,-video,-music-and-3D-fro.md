---
type: "corpus"
item_id: "dea08b19c2128fac"
title: "Show HN: Local text, image, video, music and 3D from one CLI, no Python"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49109663"
project_url: "https://github.com/sawfwair/mere-run"
author: "sawfwair"
published_at: "2026-07-30T13:25:04Z"
captured_at: "2026-09-21T02:56:08+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-30"
tags:
  - 语料
  - hn_show
  - author_sawfwair
  - story_49109663
  - show_hn
metrics: {"points": 16, "comments": 7, "engagement_velocity": 16}
comments_count: 7
comments_total: 7
discovered_via: "hn:show_hn:83d"
---

# Show HN: Local text, image, video, music and 3D from one CLI, no Python

> [!info] 一句话导读
> Hi HN! I'm the author of mere.run a local first inference runtime built around an installable CLI. I believe that whenever possible we should use the stuff we a…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49109663>
> 指标：点赞=16 · 评论=7 · engagement_velocity=16
> 作者：sawfwair　|　发布：2026-07-30T13:25:04Z
> 项目链接：<https://github.com/sawfwair/mere-run>
> 采集：2026-09-21T02:56:08+08:00　|　id：`dea08b19c2128fac`

## 正文

Hi HN! I'm the author of mere.run a local first inference runtime built around an installable CLI. I believe that whenever possible we should use the stuff we already own (like our Mac laptops, decent machines gathering dust, our gaming PC) and the limited electrical power we have easy access to, like the socket in the wall next to most of us. We shouldn't have to send our data to the cloud hoping some T&C will prevent it from being used in a way that we'd regret. Most of the local AI solutions are technical, involved, and land a curious body in some package hell. People are optimizing for one system and not another, the fun stuff is on PC if you own a Mac, and on Mac if you own a PC.So mere.run was my choice to begin to patch many of those things that I saw as problematic. Text, chat, code, image gen, speech tts+asr, vision (caption/ground/segment/track/pose/depth/face/OCR/etc), music, sfx, video, 2d->3d, persistent worlds, lora training plus a few more things I am probably forgetting all in one place to work the way you work, with a scriptable CLI, an openAI compatible serve, and optionally a native app on Mac.It's native swift on MLX, no python, PyTorch, diffusers for inference. For text lanes with GGUF it uses llama.cpp and for a/v muxing its FFmpeg. Most upstream releases that don't have an MLX variant are converted offline and hosted on huggingface. All release packages are built for arm64 (Mac & Cuda) plus x86. They're signed and ship SHA256SUMS. No windows at the moment.> mere.run model capabilities --recommended # That inspects your machine before recommending to prevent pulling models that don't fit your specThere's a workflow layer with typed, validated graphs so you can create immutable job bundles and run them locally, over an ssh executor or using a fleet of machines and the relay service. (It's hosted at relay.mere.run and is currently invite only while I test, but its also totally open MIT so you can set it up yourself)The whole runtime is MIT along with the companion packages, models carry their own licenses and the CLI makes it clear when something has specific terms. Once you've pulled the models, everything works fully offline.I've been working on a (hopefully) comprehensive docs -> https://docs.mere.runNo account, no API key, no analytics or phone home. Any network calls in the source are all at your request only like huggingface.co (models), GitHub.com (Pi install).I'm just getting started, but it's finally at the point I'd love feedback, contributions, and just folks to generally find it useful. I hope it helps you make things and explore what's possible with the stuff you've already got in your home.Would love any thoughts, questions, ideas and maybe a star if you do that kinda thing.-Kyle

## 评论（7/7）

> **sawfwair** · 2026-07-30T16:11:18.000Z　
> some real numbers on my m4 max -image gen (zimage-nano), 1024x1024: 58simage -> textured mesh (trellis.2): 2m 49ssfx generate (5s clip): 3.6smusic generate (8s, ace-step): 15sspeech synth: 13s | transcribed back: 2.2svideo gen w/ audio(ltx unified-av) 4s,768x512: 2m 48stext chat (laguna xs2.1): 102 tok/s - https://mlx.fast leaderboard

---

> **ks2048** · 2026-07-30T23:27:05.000Z　
> FYI, the title makes no sense in isolation.

---

> **janrakete** · 2026-07-31T15:25:49.000Z　
> I think it’s generally a good idea to use a standalone, local solution. I also like the approach of combining multiple models with different focuses under a single interface. On the other hand, I usually use very specialized models (for programming, for example) and rarely end up generating music or a video on the side. So I can’t think of a reason to use the system right now.What target audience do you have in mind?

---

> **sawfwair** · 2026-07-30T23:35:11.000Z　
> totally fair! i spent a while trying to get clever and compress what i wanted to say and finally just hit submit but prob lost too much - local inference runtime, one cli that runs image/video/music/speech/3d/etc on your own machine without package hell. would def edit if I still could after your feedback, but window is closed. Thank you!

---

> **sawfwair** · 2026-07-31T15:38:46.000Z　
> That's a great q and point. I built it to get at a broad approach to tying multimodal capability together in one place as I'm personally building products on top of it that stitch chat, image, video together and wanted to enable others to do the same. For just coding/chat/specialized models I'd say ollama or lm studio is still the better bet generally, but for some of the models I care about I'm trying to optimize pretty deeply and make fine-tuning really simple. Plus I'm often supporting and bouncing between Mac and Cuda boxes so wanted something where the same codebase ran on both.

---

> **ks2048** · 2026-07-31T00:17:22.000Z　
> At least add “models”. Doing “music” on your local machine can mean many things.

---

> **sawfwair** · 2026-07-31T02:06:15.000Z　
> Yes, missed that completely... Great point!

## 关联链接

- https://docs.mere.runNo

## 导航

- 项目页：[[10-项目/github.com_5e5be9ef]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
