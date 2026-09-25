---
type: "project"
title: "Show HN: IttyBittyAI – Qwen2.5:0.5B running on a 2017 Asus smartphone"
project_url: "https://ittybitty.local/"
first_seen: "2026-09-25T13:42:25+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_spottedmarley
  - story_49835080
  - show_hn
lang: "en"
---

# Show HN: IttyBittyAI – Qwen2.5:0.5B running on a 2017 Asus smartphone

> [!info] 一句话导读
> Rummaging through some boxes of old stuff, I found one of my old smart phones. It's an Asus Zenfone 4 Max (ZC554KL, Snapdragon 430, 8x Cortex-A53, 3 GB RAM, 32 …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://ittybitty.local/>
> 首次收录：2026-09-25T13:42:25+08:00
> 来源渠道：HN Show HN
> 标签：author_spottedmarley, story_49835080, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-25T13:42:25+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-25/00ff5531d7134875_Show-HN-IttyBittyAI-–-Qwen2.5-0.5B-running-on-a-20]] |

## 摘要正文

Rummaging through some boxes of old stuff, I found one of my old smart phones. It's an Asus Zenfone 4 Max (ZC554KL, Snapdragon 430, 8x Cortex-A53, 3 GB RAM, 32 GB storage) that I bought back in 2017 and so it's been sitting in a box for ~8 or 9 years. Still works! So I thought I'd give it a chance to avoid the garbage bin by turning it into a tiny AI chatbot server that can connect to any wifi network and immediately make itself available to chat via a web UI on the local network.The phone now boots into postmarketOS, with a small touch screen UI for picking a Wi-Fi network. Once connected, the web server is started and a chat URL provided (the app sets the device hostname to ittybitty so the standard chat URL will be http://ittybitty.local or just the IP address) and a QR code that will take you to the chat UI is provided.llama.cpp was compiled on the phone itself (the first full build took over an hour). The model is Qwen2.5-0.5B-Instruct at 4-bit (403 MB).It can't really do a whole lot other than chat and answer questions using it's training data, which is tiny so not super-intelligent on its own, but I added a few helpers to the web app (a calculator, the date/time, Wikipedia l…
