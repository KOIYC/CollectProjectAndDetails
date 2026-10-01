---
type: "project"
title: "Show HN: DragomanD – local language translator for Linux"
project_url: "https://dragomand.l10n-bg.dev/"
first_seen: "2026-10-01T09:41:49+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_eniac111
  - story_49914804
  - show_hn
lang: "en"
---

# Show HN: DragomanD – local language translator for Linux

> [!info] 一句话导读
> Dragomand is a per-user Linux daemon that gives desktop applications

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://dragomand.l10n-bg.dev/>
> 首次收录：2026-10-01T09:41:49+08:00
> 来源渠道：HN Show HN
> 标签：author_eniac111, story_49914804, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-01T09:41:49+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-10-01/54e35a94f567283c_Show-HN-DragomanD-–-local-language-translator-for]] |

## 摘要正文

Skip to content English  Български Install  Integrations  About  Documentation Dragomand is a per-user Linux daemon that gives desktop applications fully offline machine translation over D-Bus. It runs Mozilla's Bergamot/Marian translation models locally, the ones behind Firefox Translations, and manages which models are installed and which stay loaded in memory. $ dragomanctl translate -f bg -t en "Добро утро. Как си днес?" Good morning. How are you today?  The first call downloads the model from Mozilla (verified by SHA-256) and starts the daemon through D-Bus activation. Everything afterwards is fully offline, and the daemon exits again when idle. The Daemon ¶ The existing Linux options are either standalone applications or translation tied to a single host such as Firefox. Dragomand is one shared service instead: One API for every app. Editors, browsers, clipboard tools,  KRunner, GNOME Shell, LibreOffice and accessibility software all call  the same D-Bus interface: dev.l10n_bg.dragomand.Translator1 . One copy of every model. The Bergamot engine keeps models in  private memory, so every application embedding it would pay for its  own copy. A shared daemon loads each model once…
