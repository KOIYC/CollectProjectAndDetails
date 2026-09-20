---
type: "corpus"
item_id: "df35d80f50625fb9"
title: "Show HN: I made Niri-like terminal colm (cmux alternative)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49763381"
project_url: "https://colm.sh/"
author: "al3rez"
published_at: "2026-09-19T04:44:43Z"
captured_at: "2026-09-20T09:48:16+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-19"
tags:
  - 语料
  - hn_show
  - author_al3rez
  - story_49763381
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: I made Niri-like terminal colm (cmux alternative)

> [!info] 一句话导读
> colm — the column terminal for agents

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49763381>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：al3rez　|　发布：2026-09-19T04:44:43Z
> 项目链接：<https://colm.sh/>
> 采集：2026-09-20T09:48:16+08:00　|　id：`df35d80f50625fb9`

## 正文

colm — the column terminal for agents

# colm

The terminal for

 A Linux workspace manager for coding agents, built on Ghostty. Workspaces live in a sidebar, terminals live in a horizontal column strip, and everything is scriptable over a JSON control socket.

## FEATURES

- Workspace sidebar. Pin, mute, group, and drag-reorder workspaces. Each row shows task status, git branch, agent activity, and a live notification preview.
- Column strip. Terminals tile horizontally like niri. Split, zoom, and jump between columns without leaving the keyboard.
- Column overview. A native-style grid of live column thumbnails — search, click, or arrow-key to any tile in the active workspace.
- Agent aware. Permission prompts, exit plans, and questions from Claude Code and friends surface as cards you can answer from the feed sidebar.
- Remote workspaces. Attach whole workspaces to remote machines over SSH with tmux-backed persistence.
- Scriptable. Every window, workspace, and pane is addressable over a JSON-RPC unix socket — create, focus, split, close, snapshot.
- Ghostty core. GPU-accelerated rendering, fast startup, and the full Ghostty terminal engine underneath.
- Open source. MIT licensed, like the Ghostty it stands on.

## INSTALL

```
git clone https://github.com/al3rez/colm
cd colm
zig build -Doptimize=ReleaseFast -p ~/.local/opt/colm
```

Requires Zig 0.15, GTK 4.16+, and libadwaita 1.5+.

## FAQ

How is this different from Ghostty?

colm is a fork focused on managing many agent sessions at once: a workspace sidebar, a niri-style column strip, live overviews, and an automation socket. The terminal underneath is unmodified Ghostty.

Which platforms?

Linux with GTK 4 and libadwaita. Wayland and X11 both work.

Which agents?

Anything that runs in a terminal. Claude Code, Codex, OpenCode, aider — permission and plan prompts integrate with the feed when the agent supports it.

Is it free?

Yes. MIT licensed, no accounts, no telemetry.

## 关联链接

- https://github.com/al3rez/colm

## 导航

- 项目页：[[10-项目/colm.sh_8c35cd51]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
