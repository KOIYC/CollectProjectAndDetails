---
type: "corpus"
item_id: "2a1f4a93062b29d8"
title: "Show HN: ssh zydra.sh, a GPU Linux desktop in your terminal, with Doom"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50258446"
project_url: "https://zydra.sh/"
author: "teledream"
published_at: "2026-10-27T12:57:20Z"
captured_at: "2026-10-27T23:46:32+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-27"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_teledream
  - story_50258446
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: ssh zydra.sh, a GPU Linux desktop in your terminal, with Doom

> [!info] 一句话导读
> ssh zydra.shThere's no sign-up or anything, and you get a 15-minute demo of a graphical Linux VM drawn entirely in your terminal. It has a browser, an editor, a…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50258446>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：teledream　|　发布：2026-10-27T12:57:20Z
> 项目链接：<https://zydra.sh/>
> 采集：2026-10-27T23:46:32+08:00　|　id：`2a1f4a93062b29d8`

## 正文

ssh zydra.shThere's no sign-up or anything, and you get a 15-minute demo of a graphical Linux VM drawn entirely in your terminal. It has a browser, an editor, and it runs Doom.It works best in Kitty or Ghostty. WezTerm and Konsole also work, as well as Sixel and iTerm2 terminals, though with less detail. Text-only terminals support non-graphical apps: shells, editors, and other TUIs.Why? For a few months I ran coding agents in tmux on a VPS over SSH, and it sucked. I couldn't paste images, scrolling broke and I didn't wanna figure out why, I had no notifications for when an agent finished, I couldn't see browsers agents opened to smoke-test, logins drifted between my laptop and the server, I couldn't check in from my phone, and to know what an agent had done five minutes ago I had to read through opaque chunks of tool calls. These issues added up and had me in a limbo: They made my setup bad enough to annoy me every day, but not quite bad enough to stop my real work and fix it.How it works: Zydra is a custom (Smithay-based) Wayland compositor in a microVM with an AMD GPU, implementing a series of terminal protocols that solve many issues but are often ignored: Kitty graphics for windows, OSC 52 for the clipboard, images included, OSC 9/99/777 for notifications, SGR mouse for scrolling and clicks. VNC is limited to sending pictures of the screen and diffing frames to find what changed. In Zydra, apps directly tell the compositor what changed, and terminal text is sent as text you can select and copy natively. The browser is a WebKit build that delivers frames to the compositor as DMA-BUFs without a readback, and agents drive it through Playwright. Alt+P is sort of like Raycast: browse apps, linked GitHub, websites, and SSH targets from it.You can watch the desktop at any point in time and rewind to periodic snapshots. To achieve this, the desktop records into a timeline file, a kind of structured video, and the VM takes snapshots along it. You can traverse back like a livestream to see what happened while you were away, then restore or fork the whole machine from that point. Agents can mark points on the timeline and checkpoint the whole machine before risky changes.Other things to try: ssh -t zydra.sh dino # the Chromium dino game via SSH
 tar -czf - -C ~ .claude .claude.json | ssh -T zydra.sh upload # bring your configs (includes your Claude login)
 ssh -o ObscureKeystrokeTiming=no -A zydra.sh # lower latency & forward your SSH agent
 ssh -p 443 zydra.sh # connect from a corporate firewall
 sshfs zydra.sh: ~/zydra # paid accounts: mount your home

Everything runs on one dedicated server with one AMD iGPU, so there are 12 demo slots. When they're full you wait in a queue and can play Chromium's offline dino game. The paid plan is $40/month (+ tax): 8 GB RAM, 4 vCPUs, 80 GB disk, GPU access, with no time limit and a 3-day money-back guarantee.I'll be around all day to answer questions.

## 评论（1/1）

> **teledream** · 2026-10-27T12:57:34.000Z　
> Some background: the project started with Zenbu Labs' terminal-browser & terminal-code, a chromium-based browser and VS Code drawn on the terminal (both are available inside Zydra, credits at zydra.sh/credits, although our primary browser is WebKit-based now). These made me wonder if terminal protocols are a hidden gem for solving the pains of running agents remotely.That pain is what I experienced running my previous business. The more sandboxed and remote my agents were, the harder it was to see what they were doing. Zydra is my attempt to bridge that gap: an isolated VM that you can still watch, rewind, and use like your own desktop.I'd love to hear where the rough edges are.

## 导航

- 项目页：[[10-项目/zydra.sh_f9dce444]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
