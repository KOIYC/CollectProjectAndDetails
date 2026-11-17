---
type: "corpus"
item_id: "3accf8154ae57010"
title: "Show HN: Astrum – a terminal multiplexer with integrated AI assistant"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50526510"
project_url: "https://robert-mcdermott.github.io/astrum"
author: "mcdermott"
published_at: "2026-11-17T02:10:21Z"
captured_at: "2026-11-17T11:09:12+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-17"
pub_day: "2026-11-17"
tags:
  - 语料
  - hn_show
  - author_mcdermott
  - story_50526510
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Astrum – a terminal multiplexer with integrated AI assistant

> [!info] 一句话导读
> Documentation Install Changelog GitHub

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50526510>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：mcdermott　|　发布：2026-11-17T02:10:21Z
> 项目链接：<https://robert-mcdermott.github.io/astrum>
> 采集：2026-11-17T11:09:12+08:00　|　id：`3accf8154ae57010`

## 正文

Skip to the content
Documentation Install Changelog GitHub
A persistent terminal with a built-in AI agent
 A terminal that keeps your place , and an agent that shares it
Astrum runs inside the terminal you already use, locally or over SSH. Close the window and everything keeps running; come back and it is all there. Click anything, split panes, and ask an agent that works in the same shell you do, where you can watch it and take over.
Get started
 Read the documentation
$ curl --proto '=https' --tlsv1.2 -fsSL https://raw.githubusercontent.com/robert-mcdermott/astrum/main/install.sh | sh Copy
Version 0.11.0, open source. One file, nothing else to install. macOS on Apple silicon, Linux on x86-64 and ARM64.
Two panes on the left, the agent on the right, and an agent in each of three tabs
What Astrum does
Astrum is a session manager for the terminal: tabs, panes and shells that keep running in the background, with an AI agent built in. It changes nothing about your shell, your prompt or your colors.
$_ Feels like your own shell
 Run astrum and you are in your usual zsh, bash or fish, with your own prompt and colors, plus a tab bar.
↺ Sessions survive
 Close the window and come back later: every tab, running program and scrollback is still there. After a reboot the tabs, splits and directories come back too.
⌖ Made for the mouse too
 Click tabs, + and ✕ , drag dividers, scroll with the wheel, right-click for a menu, and find everything else in ≡ menu . Keys are there for people who want them.
⊞ Room to work
 Split a tab into panes, search the scrollback, open links, see the pictures programs print, and look at one session from several windows.
⇄ Other machines, kept
 Open a tab on a server over your own ssh : its shells stay there, so a dropped connection or a closed laptop loses nothing.
✦ Any model
 Ollama and any OpenAI-compatible endpoint, Anthropic, and Amazon Bedrock. Switch with /model ; keys are kept in the system's keychain.
The agent
 It works in your shell, where you can see it
Press Ctrl+Space or click the SHELL chip and ask. The agent reads what is on screen, proposes commands and runs them in your real session. You see each one before it runs, and you decide how much it may do on its own.
Ask first, run read-only commands by itself, or work on autopilot
Commands you always allow, and commands it may never run
Keys and passwords hidden from the model before anything is sent
How the agent works →
The agent asks before it runs a command, unless you have said it need not
At the prompt
 Ask without leaving the shell
Type # and a question at your prompt and the agent answers beside it. When a command fails, click explain or fix in the status bar; when one is taking long, watch has the agent keep an eye on it.
Asking from the shell →
A question typed at the prompt goes to the agent
Several agents
 Everything that needs you, at a glance
Each tab has an agent of its own, and any pane can say it needs you: a long build that ends, a bell, a program's notification, a coding agent run as a program that waits for your permission. One list shows them all. Answer from the list, or click to go there. Your terminal is told when something you cannot see needs you.
Several agents, and what needs you →
Every agent, and whatever needs you, in one list
Tools
 MCP servers and skills
Give the agent the tools of MCP servers, on your machine or on the network, signing in with OAuth where a server asks. Skills, folders with a SKILL.md , teach it how your projects do things, and are loaded only when they fit.
MCP servers → · Rules and skills →
An answer made with an MCP server's tool, and what /mcp says of the servers
Tabs and panes
 Split, drag, zoom, and keep going
Split a tab side by side or one above the other, drag the dividers, zoom one pane to fill the tab and back. Find text in the scrollback, select to copy, and right-click a link to open it.
Tabs and panes →
A tab split into three panes
Other machines
 A tab on a server, kept there
Open a tab on another machine over your own ssh . Its shells are kept on that machine, so a dropped connection, a closed laptop or a restart here loses nothing: the tab picks up where it was. The agent works there with all its tools.
Tabs on other machines →
A tab on another machine: the tab bar and the status bar say where it is
Themes
 Your colors, or one of 21
Out of the box Astrum uses your terminal's own colors and changes nothing about how it looks. 21 themes are built in, from calm to neon, shown live as you move through them. Or make one of your own.
Themes →
Moving through the list puts each theme on the screen
Install
The installer downloads the file for your machine from the latest release, checks it against the release's checksums, and puts it in ~/.local/bin . It does not use sudo or change anything else.
$ curl --proto '=https' --tlsv1.2 -fsSL https://raw.githubusercontent.com/robert-mcdermott/astrum/main/install.sh | sh Copy
More ways to install
 Releases
 Source code
A persistent terminal with tabs, mouse support and a built-in AI agent. Open source, under the Apache License 2.0.
Using Astrum
 Getting started
 Tabs and panes
 The mouse and the keys
 Settings
The agent
 The agent
 Providers and models
 MCP servers
 Several agents at once
The project
 Source code
 Releases
 Report a problem
 Changelog
Astrum 0.11.0 · Apache License 2.0 · The screenshots on this site were made by Astrum itself.

## 关联链接

- https://raw.githubusercontent.com/robert-mcdermott/astrum/main/install.sh

## 导航

- 项目页：[[10-项目/robert-mcdermott.github.io_bdd5990d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
