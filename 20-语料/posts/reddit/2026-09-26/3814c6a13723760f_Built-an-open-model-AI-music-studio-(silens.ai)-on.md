---
type: "corpus"
item_id: "3814c6a13723760f"
title: "Built an open-model AI music studio (silens.ai) on Cloudflare & Modal. Going back to a full time job soon and looking for advice"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SideProject/comments/1whidzx/built_an_openmodel_ai_music_studio_silensai_on/"
project_url: "https://silens.ai/"
author: "Fit_Firefighter7273"
published_at: "2026-09-16T08:52:09+08:00"
captured_at: "2026-09-26T09:42:50+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-26"
pub_day: "2026-09-16"
tags:
  - 语料
  - reddit
  - r/SideProject
metrics: {"score": 3, "comments": 5, "upvote_ratio": 1}
comments_count: 4
comments_total: 5
discovered_via: "reddit:14d+settle10"
---

# Built an open-model AI music studio (silens.ai) on Cloudflare & Modal. Going back to a full time job soon and looking for advice

> [!info] 一句话导读
> 👋 I built [Silens](https://silens.ai/) as a personal side project.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SideProject/comments/1whidzx/built_an_openmodel_ai_music_studio_silensai_on/>
> 指标：得分=3 · 评论=5 · 赞踩比=1
> 作者：Fit_Firefighter7273　|　发布：2026-09-16T08:52:09+08:00
> 项目链接：<https://silens.ai/>
> 采集：2026-09-26T09:42:50+08:00　|　id：`3814c6a13723760f`

## 正文

👋 I built [Silens](https://silens.ai/) as a personal side project.

I wanted to see how far open-source music models have come compared to closed platforms like Suno or Udio, and whether it was possible to create a full, end-to-end studio experience — lyrics, arrangement, vocal synthesis, and mixing — on a completely serverless, zero-maintenance stack.

It’s live now, and you can try it here: [https://silens.ai](https://silens.ai/)

# The Tech Stack

I designed the architecture to be as lightweight and cost-effective as possible, so it wouldn't incur huge hosting bills while idle:

* **Frontend:** Next.js (static export) hosted on Cloudflare Pages
* **Backend / Edge API:** Cloudflare Workers handles auth, rate limiting, job dispatching, and API routes
* **Database & Storage:** Cloudflare D1 (serverless SQLite) for songs/user metadata, and Cloudflare R2 for streaming audio files
* **Prompt & Lyrics AI:** Cloudflare Workers AI (Llama models) for structured prompt analysis and lyrics generation
* **Audio Inference Engine:** Modal running serverless GPU containers (T4 / A10G)
* **Open-weights models:** ACE-Step 1.5 for vocal synthesis/singing and MusicGen for instrumental arrangements

Because Modal spins up on demand and shuts down to zero when idle, the generous free tiers across Modal and Cloudflare allow it to generate up to \~3,000 songs/month essentially for free.

# My Dilemma

I’m starting a demanding full-time job soon and won't have much bandwidth to actively develop, market, or maintain this solo.

Rather than letting the code gather dust or shutting it down, I’m trying to figure out the right path forward:

**1. Keep it running as a free community sandbox**

Let people generate music within the free limits until the credits run out, and keep it alive primarily as a portfolio/showcase project.

**2. Open source & find co-maintainers**

Open up the repository and find 1–2 collaborators who are excited about open-weight audio models, React/Next.js, and serverless GPU pipelines.

**3. Micro-hosting / "Circle of Trust" tool**

Package it so musicians, producers, or indie collectives can one-click self-host their own instance.

Their audio, stems, prompts, and lyrics would stay in their own private storage rather than being uploaded to a commercial music platform.

# What I’d love from you

**1. Test it out**

Jump onto [https://silens.ai](https://silens.ai/) and try generating a song.

Try different genres, instruments, or lyrics. Let me know what sounds great, what feels clunky, and where the UI/flow could improve.

**2. Advice**

If you’ve ever launched a passion project right before stepping into an intense job, how did you handle it?

Did you find partners, open-source it, pivot, or just let it run?

Thanks for checking it out! I’ll be hanging out in the comments answering questions about the stack, models, latency, or serverless setup.

## 评论（4/5）

> **CaptJan**（1 分） · 2026-09-16T11:58:52+08:00　
> It doesn't have a delete button for creations I don't like.  I really wanted to create an instrumental, and it automatically put song into it - I have another app, for android that listens a bit better with the same prompt.
>
> I would suggest making a PC/Windows and/or Android app that uses a BYOK with the 3 minute \[or more\] option so each person has a virtually unlimited ability for creation.
>
> Thanks for sharing, it's appreciated.

---

> **Fit_Firefighter7273**（1 分） · 2026-09-16T12:07:57+08:00　
> https://preview.redd.it/h0xmkuzt3tph1.png?width=2350&format=png&auto=webp&s=c1f77850efd00d709344a252e0a69613d5245161
>
> Thanks for trying it out and the feedback! I will add the delete button, and look into creating a mobile app. Out of curiosity, what app are you using ?
>
> In the meantime if you are looking to iterate over your creation, you can regenerate the song by refining the prompt and go between the versions you create as seen in the image above

---

> **CaptJan**（1 分） · 2026-09-16T13:35:53+08:00　
> [https://play.google.com/store/apps/details?id=com.fish.audio.suno.music](https://play.google.com/store/apps/details?id=com.fish.audio.suno.music) \- they've updated and it now either pay or watch an ad per generation for 30 seconds of audio
>
> Windows 10 Desktop on a Chrome Browser is where I used your app.
>
> Thanks for the feedback.

---

> **Fit_Firefighter7273**（1 分） · 2026-09-16T23:32:12+08:00　
> Thanks for sharing, ill check it out

## 关联链接

- https://silens.ai

## 导航

- 项目页：[[10-项目/silens.ai_d80d45fd]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
