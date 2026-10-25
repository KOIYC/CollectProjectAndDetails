---
type: "project"
title: "Steam Headless v2 - Amazing!"
project_url: "https://steamheadless.com/"
first_seen: "2026-10-25T23:28:44+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/selfhosted
  - Game Server
lang: "en"
---

# Steam Headless v2 - Amazing!

> [!info] 一句话导读
> I have five kids and the older couple are coming to an age where we occasionally let them play video games. I have been mostly out of the console game, but I ha…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://steamheadless.com/>
> 首次收录：2026-10-25T23:28:44+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/selfhosted, Game Server
> 最新指标：得分=92 · 评论=43 · 赞踩比=0.9791666666666666

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-25T23:28:44+08:00 | Reddit 独立开发版块 | 得分=92 · 评论=43 · 赞踩比=0.9791666666666666 | [[20-语料/posts/reddit/2026-10-25/b1a7799dd082e4ef_Steam-Headless-v2-Amazing!]] |

## 摘要正文

I have five kids and the older couple are coming to an age where we occasionally let them play video games. I have been mostly out of the console game, but I have a decent Steam library and wanted a way to let them play at the same time. For my proof of concept, I picked up a few copies of Wreckfest and my goal was for all of us to be able to play together, utilizing one machine. Here *were* the specs of the machine when I first set out on this journey-  * AMD Ryzen 9 5900 XT (16c/32t) * 64GB DDR4 3200 * 2TB WD NVME SSD * 1x AMD RX 6800 16GB * 2x NVidia P100 16GB (\~GTX 1080 performance) * Linux Mint OS  One thing I liked about a containerized solution was that GPUs could be shared between containers (meaning a GPU could run more than one game concurrently) and I could utilize these retired AI GPUs without a display output.  After playing around for some time with Games on Whales/WOLF, I was having some issues with its design. For one, configuring it can be a bit confusing, and WOLF itself launches child docker containers that are not super configurable from a networking perspective (as far as I could tell). Specifically, I had issues with the different containers being able to com…
