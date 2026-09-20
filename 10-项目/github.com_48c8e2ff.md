---
type: "project"
title: "Show HN: A Pi extension to monitor your quota for OpenCode GO et CommandCode"
project_url: "https://github.com/Anhydrite/pi-quota-monitoring"
first_seen: "2026-09-21T03:11:24+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_anhydrite
  - story_49507224
  - show_hn
lang: "en"
---

# Show HN: A Pi extension to monitor your quota for OpenCode GO et CommandCode

> [!info] 一句话导读
> Anhydrite/pi-quota-monitoring

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/Anhydrite/pi-quota-monitoring>
> 首次收录：2026-09-21T03:11:24+08:00
> 来源渠道：HN Show HN
> 标签：author_anhydrite, story_49507224, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:33:52+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/022cc553a1000580_Show-HN-A-Pi-extension-to-monitor-your-quota-for-O]] |
| 2026-09-21T03:11:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/022cc553a1000580_Show-HN-A-Pi-extension-to-monitor-your-quota-for-O]] |

## 摘要正文

# Anhydrite/pi-quota-monitoring  Pi extension — shows subscription quota usage (%) in the status bar for Command Code and OpenCode Go, next to the TPS readout  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-08-27T10:20:35Z  ## Languages  - TypeScript  ## Top Contributors  - Anhydrite (15 contributions)  ---  ## README  # pi-quota-monitoring  npm version  A pi extension that shows your **subscription quota usage (%)** in the status bar.  ## Package  Available on npm: ** **  ```bash npm view pi-quota-monitoring   # see the published package ```  Supported providers:  | Provider | Label | Quota source | | --- | --- | --- | | Command Code (`commandcode`) | `CC` | `api.commandcode.ai` billing period + 5h window | | OpenCode Go (`opencode-go`) | `OG` | `opencode.ai/zen/go/v1/usage` rolling window |  The quota only appears when you're using a model from a supported provider. Switch to any other provider (e.g. `minimax`) and the display clears automatically.  ## What it looks like  In the pi footer, the extension shows one segment per usage window:  ``` CC 5h: 15% resets in 2h · mois: 3% resets in 4d OG 5h: 10% resets in 2…
