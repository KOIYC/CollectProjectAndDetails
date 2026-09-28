---
type: "corpus"
item_id: "9d4ad25f3b265777"
title: "Show HN: swe-mux – A terminal multiplexer for coding agents optimized for mobile"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49867905"
project_url: "https://github.com/jatoran/swe-mux"
author: "jatora"
published_at: "2026-09-27T16:02:04Z"
captured_at: "2026-09-28T09:47:28+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-28"
pub_day: "2026-09-27"
tags:
  - 语料
  - hn_show
  - author_jatora
  - story_49867905
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: swe-mux – A terminal multiplexer for coding agents optimized for mobile

> [!info] 一句话导读
> I run a lot of coding agents at once, mostly Claude Code, Codex and pi, across several projects. I got tired of having so many windows open, of agents leaving h…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49867905>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：jatora　|　发布：2026-09-27T16:02:04Z
> 项目链接：<https://github.com/jatoran/swe-mux>
> 采集：2026-09-28T09:47:28+08:00　|　id：`9d4ad25f3b265777`

## 正文

I run a lot of coding agents at once, mostly Claude Code, Codex and pi, across several projects. I got tired of having so many windows open, of agents leaving hung processes behind, of tracking which one needed input, and of having to remote into my desktop or SSH into a single shell to manage them from my phone. Even then, a terminal on a phone couldn't show me the frontend or output I needed to verify the work. I tried Orca and herdr. Both were better than my setup, but neither had a real WYSIWYG markdown notes surface, and neither had a phone interface I could actually work in.swe-mux is the terminal multiplexer I built for that. It runs any shell or CLI in real terminals on your own machine and serves the same live sessions to your desktop and your phone. It's built around agents: Claude Code, Codex, opencode, pi and oh-my-pi get a live status (working, done, or waiting on you), searchable history and resume. Anything else runs as an ordinary terminal with everything except the status.This is the actual terminal and not a UI wrapped around the agent, and you can just use it that way, or start claude in a plain shell and that pane becomes an agent session.On the desktop it's panes and tabs of sessions, notes, files and dev-server previews. Input behaves the same across agents: Shift+Enter, Ctrl+Backspace, paste and click-to-position work in all of them, shortcuts come from presets (tmux, VS Code, Vim, Emacs), and you can paste images straight from the clipboard.Notes and any markdown file in the project open in the same WYSIWYG editor, on desktop and phone, and autosave. No more scattered locations for notes.On the phone it's the same sessions over your own Tailscale network, installed as a PWA: the terminal with a usable keyboard, git diff review, files, notes, and push notifications when an agent needs a decision. A dev server on the host's 127.0.0.1 is proxied through swe-mux, so the phone can open it without exposing another port. Being able to play-test and check a frontend there is what finally closed the development loop on the phone for a lot of my projects. Now I can and do swe anywhere. It's a problemTwo things I use constantly: a prompt queue, so something I think of mid-turn waits until the agent is done instead of interrupting it, and messaging between sessions, so a Codex session can ask a Claude session something. I don't want my workflow tied to one provider.General architecture:Sessions survive restarts. A separate supervisor process owns the terminals, so the daemon can restart and the app can update without killing anything. I update it several times a day, so this wasn't optional.Status comes from the CLI's hooks, its transcript and the terminal itself, because no single one reliably tells "waiting on you" apart from "busy in the background".There's no swe-mux account, no server of mine in the path, and no telemetry. Just your tailnetIt was built on Windows, which is where I use it every day and the only platform with a packaged desktop app. The installer is unsigned, so the PyPI install is the way to avoid the SmartScreen prompt. macOS and Linux run the daemon and use a browser. CI runs it on all three, but I haven't lived on those myself, however Linux I have tested.Demo, the real UI with simulated agents, nothing to install: https://swemux.dev/demo/Install: `uv tool install swe-mux` (or `pipx install swe-mux`), then run `swe-mux` on Windows or `swemux start` elsewhere.Apache-2.0: https://github.com/jatoran/swe-muxI've put a lot of work into the initial user experience to help streamline a quick setup depending on someone's needs, feedback greatly appreciated, thanks

## 关联链接

- https://github.com/jatoran/swe-muxI
- https://swemux.dev/demo/Install:

## 导航

- 项目页：[[10-项目/github.com_163c0240]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
