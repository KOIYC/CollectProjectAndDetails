---
type: "corpus"
item_id: "fa03e1fb12c3115f"
title: "Show HN: TermRover – a native tmux-first terminal for iOS and Android"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48723755"
project_url: "https://termrover.sh/"
author: "ptgamr"
published_at: "2026-06-29T19:12:18Z"
captured_at: "2026-09-21T03:11:04+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-29"
tags:
  - 语料
  - hn_show
  - author_ptgamr
  - story_48723755
  - show_hn
metrics: {"points": 5, "comments": 0, "engagement_velocity": 5}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: TermRover – a native tmux-first terminal for iOS and Android

> [!info] 一句话导读
> The tmux-first mobile terminal

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48723755>
> 指标：点赞=5 · 评论=0 · engagement_velocity=5
> 作者：ptgamr　|　发布：2026-06-29T19:12:18Z
> 项目链接：<https://termrover.sh/>
> 采集：2026-09-21T03:11:04+08:00　|　id：`fa03e1fb12c3115f`

## 正文

TermRover
Guide
 |
 Tour
 |
 Blog
 |
The tmux-first mobile terminal
SSH & tmux that feel good on a phone.
TermRover is a native SSH + Mosh terminal optimized for working with tmux on iPhone and Android. Browser-style tabs, one-tap prefix actions, and scrolling all just work.
App Store
Google Play
Watch the 10-minute TermRover tour
New
 The Herdr agents fleet is here
Select a feature to find it on the screen →
1
 Tmux quick row One-tap prefix actions
2
 Session picker One-tap → switch
3
 Swipe to scroll Mouse mode on → scroll
4
 Attach an image Screenshot → your agent
5
 Voice mode Dictate, don't type
▶
 Feel it Run the live demo
Found a bug or have an idea? Send feedback or join Discord .
From the maker
Anh Trinh - @ptgamr
I built TermRover because using tmux on a phone kept annoying me in small but constant ways.
The tmux prefix, usually Ctrl-b, is awkward on a touchscreen. Scrolling is worse: it usually requires mouse mode and changes to .tmux.conf , with no clear indication whether it is enabled.
I wanted those things to simply work. Common tmux actions should be one tap away , scrolling should feel natural , tapping the terminal should open the keyboard, and sending a screenshot to a coding agent should be as easy as sending one in a chat.
I learned about Mosh only after building the first version. It immediately made sense for a phone: SSH can drop as you move between networks, while Mosh keeps the terminal working. I added it, and later added support for Herdr and Zellij as alternatives to tmux. You can make either one the default multiplexer for a host.
TermRover is the mobile terminal I wanted to use. If something about it annoys you, tell me. That is how much of the app came to exist.
My remote setup For private remote access, I use TermRover with Tailscale .
Made for touch
The awkward parts of a mobile terminal, fixed
One-tap tmux controls
Frequently used tmux actions are one tap away: zoom a pane, create a new window, or move between windows. The session picker lets you jump between sessions and keep favourites at the top.
Watch the quick row
tmux scrolling that just works
Swipe to scroll. If tmux mouse mode is off, turn it on without editing .tmux.conf ; an amber indicator shows clearly when the mode is active.
Watch scrolling
Better input for coding agents
Tap the terminal to bring up the keyboard, compose longer prompts in a multiline field, dictate on-device, or attach and annotate screenshots for an agent.
Send image to agent
 Smart composer
Familiar browser-style tabs
Work across sessions and hosts with familiar browser-style tabs. Open a new tab, then reorder, rename or pin it just as you would in a browser.
Watch the TermRover overview
That’s not all. Check out the guide for more .
Recently added features
Better Terminal. One step at a time.
Here’s what we’ve been cooking lately.
v1.2.1 Connectivity
Take the jump.
Reach private servers through SSH jump hosts. Chain up to three hops, with a separate login for each.
Your phone
Jump host
Private host
v1.2.0 Access & security
Your tailnet. At your fingertips.
Discover your Tailscale hosts and connect with keyless Tailscale SSH. Keep app access protected with biometric locking.
Tailnet connected
 App locked
Explore Tailscale SSH
v1.1.0 Herdr agents fleet
All your agents. One view.
See Herdr agents across all your hosts. Find the one that needs you and jump straight into its terminal.
macbook Working
dev-server Waiting
homelab Ready
Meet the Herdr Agents Fleet
v1.0.10 tmux on touch
Select the text. Stay in the pane.
More precise, pane-aware text selection in tmux. Copy what you need without picking up text from the pane next door.
tmux / two panes
$ npm test 12 tests passed
 $ tail -f listening…
v1.0.9 Deeper Herdr integration
A little closer to your workspace.
A better Herdr picker, workspace names that stay in sync, and pane-aware selection for cleaner copy and paste.
herdr / api-service
Ready for review. 3 files changed
 $ git status main ↑ 1
See pane-aware selection
Product philosophy
A good terminal, first and foremost
Stay true to the core
TermRover focuses on the core terminal experience: reliable connections, practical tmux controls, natural scrolling and input that works on a phone. AI makes it easy to keep adding features simply because they are possible. TermRover tries to stay minimal.
The attention is yours
TermRover deliberately stays away from agent notifications. You already have enough distractions in your life; you don’t need more. The True Cost of AI Coding is a thoughtful look at the fatigue and burnout that can follow. The agent can wait.
More on “Why TermRover doesn’t notify you”
Pricing
The core terminal is not subscription-gated
Free for the terminal
SSH, tmux, Mosh, unlimited saved hosts and the phone-friendly terminal controls are free. The free tier also includes a daily allowance for voice and image attachments, plus one active port forward.
TermRover Pro
Pro makes voice and image attachments unlimited, allows as many port forwards as you need, and unlocks every theme. Pro is available yearly or as a lifetime purchase. No monthly subscription. See how that compares with Termius and other mobile SSH clients .
Same app, both platforms
A mobile SSH terminal for both iOS and Android
Many mobile terminals are available on only one platform. TermRover runs on iPhone, iPad and Android, giving you the same intuitive, seamless experience across devices.
App Store
Google Play
Found a bug or have an idea? Send feedback or join Discord .
TermRover © 2026 made by @ptgamr
Blog
 Guide
 Video tour
 Privacy Policy
 Terms of Service

## 导航

- 项目页：[[10-项目/termrover.sh_a3aa0683]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
