---
type: "corpus"
item_id: "54e35a94f567283c"
title: "Show HN: DragomanD – local language translator for Linux"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49914804"
project_url: "https://dragomand.l10n-bg.dev/"
author: "eniac111"
published_at: "2026-09-30T21:35:44Z"
captured_at: "2026-10-01T09:41:49+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-01"
pub_day: "2026-09-30"
tags:
  - 语料
  - hn_show
  - author_eniac111
  - story_49914804
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: DragomanD – local language translator for Linux

> [!info] 一句话导读
> Dragomand is a per-user Linux daemon that gives desktop applications

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49914804>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：eniac111　|　发布：2026-09-30T21:35:44Z
> 项目链接：<https://dragomand.l10n-bg.dev/>
> 采集：2026-10-01T09:41:49+08:00　|　id：`54e35a94f567283c`

## 正文

Skip to content
English
 Български
Install
 Integrations
 About
 Documentation
Dragomand is a per-user Linux daemon that gives desktop applications
fully offline machine translation over D-Bus. It runs Mozilla's
Bergamot/Marian translation models locally, the ones behind Firefox
Translations, and manages which models are installed and which stay
loaded in memory.
$ dragomanctl translate -f bg -t en "Добро утро. Как си днес?"
Good morning. How are you today?
 The first call downloads the model from Mozilla (verified by SHA-256)
and starts the daemon through D-Bus activation. Everything afterwards is
fully offline, and the daemon exits again when idle.
The Daemon ¶
The existing Linux options are either standalone applications or
translation tied to a single host such as Firefox. Dragomand is one
shared service instead:
One API for every app. Editors, browsers, clipboard tools,
 KRunner, GNOME Shell, LibreOffice and accessibility software all call
 the same D-Bus interface: dev.l10n_bg.dragomand.Translator1 .
One copy of every model. The Bergamot engine keeps models in
 private memory, so every application embedding it would pay for its
 own copy. A shared daemon loads each model once.
Current models. Models come from Firefox Remote Settings, exactly
 what Firefox Translations installs, in every language pair Mozilla
 publishes.
Private by design. Text never leaves the machine. The network is
 used only to download models, and updates are checked only when you
 ask.
No idle cost. The daemon is D-Bus activated and exits after an
 idle period; nothing runs permanently.
Currently implemented ¶
Version 0.1.0: the daemon with D-Bus API v1, the dragomanctl
command-line client, install-on-demand model downloads, LRU keep-warm
with memory-pressure eviction, KRunner and GNOME Shell search
integration, a LibreOffice extension and a KTextEditor (Kate) plugin.
Bulgarian and English form the first pair working end to end; every
pair Mozilla publishes is in scope.
Get started: Install ·
 Integrations ·
 Documentation
Pages
Home
Install
Integrations
About
Documentation
Resources
Source code
Bulgarian software localization
Mozilla translation models
Firefox Translations
About this site
Made with MkDocs
Sponsored by
© 2026 Blagovest Petrov · Dragomand is free software, licensed under the GNU GPL 3.0 or later.
 Site content is licensed under a
 Creative Commons Attribution-ShareAlike 4.0 International License .

## 导航

- 项目页：[[10-项目/dragomand.l10n-bg.dev_1af93e70]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
