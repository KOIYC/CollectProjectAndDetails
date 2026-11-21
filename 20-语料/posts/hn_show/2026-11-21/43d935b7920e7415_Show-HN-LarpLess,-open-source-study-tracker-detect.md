---
type: "corpus"
item_id: "43d935b7920e7415"
title: "Show HN: LarpLess, open-source study tracker detecting distractions locally"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50577115"
project_url: "https://larpless.app/"
author: "maergune"
published_at: "2026-11-20T16:21:50Z"
captured_at: "2026-11-21T14:45:01+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-21"
pub_day: "2026-11-20"
tags:
  - 语料
  - hn_show
  - author_maergune
  - story_50577115
  - show_hn
metrics: {"points": 3, "comments": 2, "engagement_velocity": 3}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: LarpLess, open-source study tracker detecting distractions locally

> [!info] 一句话导读
> I am ashamed to admit that I am one of those students who go to the library and get very little done (a.k.a. larping). It's very easy to get distracted if you h…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50577115>
> 指标：点赞=3 · 评论=2 · engagement_velocity=3
> 作者：maergune　|　发布：2026-11-20T16:21:50Z
> 项目链接：<https://larpless.app/>
> 采集：2026-11-21T14:45:01+08:00　|　id：`43d935b7920e7415`

## 正文

I am ashamed to admit that I am one of those students who go to the library and get very little done (a.k.a. larping). It's very easy to get distracted if you have any electronic devices with you, but as a CS major, I can't just switch to pen and paper. That's why I started building this app called LarpLess with the help of a few friends.LarpLess is a macOS/Windows app that checks your screen and camera with local AI to determine what you are studying or if you are distracted. Gives you a focus percentage at the end, with a breakdown of what you did during your session (Math, Physics, etc.)Privacy is a big concern for an app like this, so it is open-source (AGPL 3.0) and uses locally run open-source models. It doesn't connect to the internet unless you want to check for updates or enable the friends feature (Disabled by default. You can make an account, add friends and see their shared study sessions/share your study sessions).For the camera, it uses an object detection model, YOLO11n, to detect if there is a person and/or a phone at 1fps. For the screen, there are 2 options: the one we did first is reading window titles + a VLM on Ollama (default is qwen3-vl:2b), simple but power/RAM hungry. The one my friend added later can run on an average laptop easily. It takes less than a second for a verdict. It scores window titles + OCR text on the screen with MiniLM text embeddings and scores the screenshot with image embeddings using SigLIP 2. SigLIP 2 decides if the user is distracted, and MiniLM decides what they are working on. You can run the classifier-based mode on any modern laptop. If you want to use the VLM mode, you need a good GPU with enough VRAM (3GB+) to hold the model in it.You can try it out by downloading the macOS version from GitHub (https://github.com/AlperErg/larpless/releases) or the Windows version from the Microsoft Store (https://apps.microsoft.com/detail/9nrvvphtmr9x).I found it helpful for studying. I hope that you will as well. I'd appreciate it if you can give it a go and kindly share your thoughts.p.s. My friend, who also works on this with me, posted about it before but without a description and not on Show HN, so I decided to post on Show HN with a good description.

## 评论（2/2）

> **carter-qadenza** · 2026-11-20T18:06:41.000Z　
> I do like to see people using local AI! How do you go about describing this to people? The initial reaction to seeing it made me uncomfortable because it feels like Honorlock and I generally don't like having things recording me. I do get that its private given the local model but it still spooks me a bit. Would love to hear your perspective.

---

> **maergune** · 2026-11-20T19:42:10.000Z　
> The emphasis on privacy is a must for pitching the idea. Privacy was a big priority from the start due to its nature. The app is as private as possible in the way it is designed. Right after my first sentence describing it, I always say that it runs offline/local AI. Then I follow up with the fact that no screenshots from the screen or camera are kept after they are used to make a decision. It being open-source is also a big plus since anyone can check the privacy for themselves or ask AI if it is secure. Many people I've pitched it to face-to-face loved the idea and downloaded it to check it out.

## 关联链接

- https://apps.microsoft.com/detail/9nrvvphtmr9x
- https://github.com/AlperErg/larpless/releases

## 导航

- 项目页：[[10-项目/larpless.app_9aeab0c0]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
