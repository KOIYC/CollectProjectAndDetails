---
type: "corpus"
item_id: "00ff5531d7134875"
title: "Show HN: IttyBittyAI – Qwen2.5:0.5B running on a 2017 Asus smartphone"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49835080"
project_url: "https://ittybitty.local/"
author: "spottedmarley"
published_at: "2026-09-24T18:42:53Z"
captured_at: "2026-09-25T13:42:25+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-25"
pub_day: "2026-09-24"
tags:
  - 语料
  - hn_show
  - author_spottedmarley
  - story_49835080
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: IttyBittyAI – Qwen2.5:0.5B running on a 2017 Asus smartphone

> [!info] 一句话导读
> Rummaging through some boxes of old stuff, I found one of my old smart phones. It's an Asus Zenfone 4 Max (ZC554KL, Snapdragon 430, 8x Cortex-A53, 3 GB RAM, 32 …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49835080>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：spottedmarley　|　发布：2026-09-24T18:42:53Z
> 项目链接：<https://ittybitty.local/>
> 采集：2026-09-25T13:42:25+08:00　|　id：`00ff5531d7134875`

## 正文

Rummaging through some boxes of old stuff, I found one of my old smart phones. It's an Asus Zenfone 4 Max (ZC554KL, Snapdragon 430, 8x Cortex-A53, 3 GB RAM, 32 GB storage) that I bought back in 2017 and so it's been sitting in a box for ~8 or 9 years. Still works! So I thought I'd give it a chance to avoid the garbage bin by turning it into a tiny AI chatbot server that can connect to any wifi network and immediately make itself available to chat via a web UI on the local network.The phone now boots into postmarketOS, with a small touch screen UI for picking a Wi-Fi network. Once connected, the web server is started and a chat URL provided (the app sets the device hostname to ittybitty so the standard chat URL will be http://ittybitty.local or just the IP address) and a QR code that will take you to the chat UI is provided.llama.cpp was compiled on the phone itself (the first full build took over an hour). The model is Qwen2.5-0.5B-Instruct at 4-bit (403 MB).It can't really do a whole lot other than chat and answer questions using it's training data, which is tiny so not super-intelligent on its own, but I added a few helpers to the web app (a calculator, the date/time, Wikipedia lookups). This project was mostly just to see if it would work at all, so the results were relatively impressive.What I'm seeing:- ~4.5 tokens/sec generating (generally faster than you can read the output being generated), ~13 tokens/sec reading the prompt
- llama-server uses about 570 MB of RAM with the model loaded
- two people can chat at once, users wait their turn
- I tried SmolLM2-360M first, it was faster (6 tok/s) but it looped and refused to answer things. The 0.5B model is noticeably better at holding a conversation.The coolest thing is it's portability. Anywhere you go that has a wifi to connect to you can just turn the phone on, connect it to the wifi, and now that network has a little AI chat bot to talk to. If this old crappy smart phone does this well I can only imagine how newer, better, faster, bigger phones would do.If anybody has this same smart phone and is interested in doing the same thing just let me know and I can give you the custom OS and llamacpp builds to start from.Not a whole lot to 'show' since it runs inside my local network but here are some screenshots of the mobile app/server and the web UI:https://spottedmarley.com/ittybitty-home.pnghttps://spottedmarley.com/ittybitty-ui.jpg

## 关联链接

- http://ittybitty.local
- https://spottedmarley.com/ittybitty-home.pnghttps://spottedmarley.com/ittybitty-ui.jpg

## 导航

- 项目页：[[10-项目/ittybitty.local_c68d5400]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
