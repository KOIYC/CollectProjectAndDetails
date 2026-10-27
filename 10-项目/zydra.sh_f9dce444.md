---
type: "project"
title: "Show HN: ssh zydra.sh, a GPU Linux desktop in your terminal, with Doom"
project_url: "https://zydra.sh/"
first_seen: "2026-10-27T23:46:32+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_teledream
  - story_50258446
  - show_hn
lang: "en"
---

# Show HN: ssh zydra.sh, a GPU Linux desktop in your terminal, with Doom

> [!info] 一句话导读
> ssh zydra.shThere's no sign-up or anything, and you get a 15-minute demo of a graphical Linux VM drawn entirely in your terminal. It has a browser, an editor, a…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://zydra.sh/>
> 首次收录：2026-10-27T23:46:32+08:00
> 来源渠道：HN Show HN
> 标签：author_teledream, story_50258446, show_hn
> 最新指标：点赞=2 · 评论=1 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-27T23:46:32+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-27/2a1f4a93062b29d8_Show-HN-ssh-zydra.sh,-a-GPU-Linux-desktop-in-your]] |

## 摘要正文

ssh zydra.shThere's no sign-up or anything, and you get a 15-minute demo of a graphical Linux VM drawn entirely in your terminal. It has a browser, an editor, and it runs Doom.It works best in Kitty or Ghostty. WezTerm and Konsole also work, as well as Sixel and iTerm2 terminals, though with less detail. Text-only terminals support non-graphical apps: shells, editors, and other TUIs.Why? For a few months I ran coding agents in tmux on a VPS over SSH, and it sucked. I couldn't paste images, scrolling broke and I didn't wanna figure out why, I had no notifications for when an agent finished, I couldn't see browsers agents opened to smoke-test, logins drifted between my laptop and the server, I couldn't check in from my phone, and to know what an agent had done five minutes ago I had to read through opaque chunks of tool calls. These issues added up and had me in a limbo: They made my setup bad enough to annoy me every day, but not quite bad enough to stop my real work and fix it.How it works: Zydra is a custom (Smithay-based) Wayland compositor in a microVM with an AMD GPU, implementing a series of terminal protocols that solve many issues but are often ignored: Kitty graphics for wi…
