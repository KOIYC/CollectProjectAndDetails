---
type: "project"
title: "Show HN: LarpLess, open-source study tracker detecting distractions locally"
project_url: "https://larpless.app/"
first_seen: "2026-11-21T14:45:01+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_maergune
  - story_50577115
  - show_hn
lang: "en"
---

# Show HN: LarpLess, open-source study tracker detecting distractions locally

> [!info] 一句话导读
> I am ashamed to admit that I am one of those students who go to the library and get very little done (a.k.a. larping). It's very easy to get distracted if you h…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://larpless.app/>
> 首次收录：2026-11-21T14:45:01+08:00
> 来源渠道：HN Show HN
> 标签：author_maergune, story_50577115, show_hn
> 最新指标：点赞=3 · 评论=2 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-21T14:45:01+08:00 | HN Show HN | 点赞=3 · 评论=2 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-11-21/43d935b7920e7415_Show-HN-LarpLess,-open-source-study-tracker-detect]] |

## 摘要正文

I am ashamed to admit that I am one of those students who go to the library and get very little done (a.k.a. larping). It's very easy to get distracted if you have any electronic devices with you, but as a CS major, I can't just switch to pen and paper. That's why I started building this app called LarpLess with the help of a few friends.LarpLess is a macOS/Windows app that checks your screen and camera with local AI to determine what you are studying or if you are distracted. Gives you a focus percentage at the end, with a breakdown of what you did during your session (Math, Physics, etc.)Privacy is a big concern for an app like this, so it is open-source (AGPL 3.0) and uses locally run open-source models. It doesn't connect to the internet unless you want to check for updates or enable the friends feature (Disabled by default. You can make an account, add friends and see their shared study sessions/share your study sessions).For the camera, it uses an object detection model, YOLO11n, to detect if there is a person and/or a phone at 1fps. For the screen, there are 2 options: the one we did first is reading window titles + a VLM on Ollama (default is qwen3-vl:2b), simple but power/…
