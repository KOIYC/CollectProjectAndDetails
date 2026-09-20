---
type: "corpus"
item_id: "022cc553a1000580"
title: "Show HN: A Pi extension to monitor your quota for OpenCode GO et CommandCode"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49507224"
project_url: "https://github.com/Anhydrite/pi-quota-monitoring"
author: "anhydrite"
published_at: "2026-08-31T08:50:38Z"
captured_at: "2026-09-21T03:11:24+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - hn_show
  - author_anhydrite
  - story_49507224
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:52d"
---

# Show HN: A Pi extension to monitor your quota for OpenCode GO et CommandCode

> [!info] 一句话导读
> Anhydrite/pi-quota-monitoring

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49507224>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：anhydrite　|　发布：2026-08-31T08:50:38Z
> 项目链接：<https://github.com/Anhydrite/pi-quota-monitoring>
> 采集：2026-09-21T03:11:24+08:00　|　id：`022cc553a1000580`

## 正文

# Anhydrite/pi-quota-monitoring

Pi extension — shows subscription quota usage (%) in the status bar for Command Code and OpenCode Go, next to the TPS readout

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-08-27T10:20:35Z

## Languages

- TypeScript

## Top Contributors

- Anhydrite (15 contributions)

---

## README

# pi-quota-monitoring

npm version

A pi extension that shows your **subscription quota usage (%)** in the status bar.

## Package

Available on npm: ** **

```bash
npm view pi-quota-monitoring   # see the published package
```

Supported providers:

| Provider | Label | Quota source |
| --- | --- | --- |
| Command Code (`commandcode`) | `CC` | `api.commandcode.ai` billing period + 5h window |
| OpenCode Go (`opencode-go`) | `OG` | `opencode.ai/zen/go/v1/usage` rolling window |

The quota only appears when you're using a model from a supported provider. Switch to any other provider (e.g. `minimax`) and the display clears automatically.

## What it looks like

In the pi footer, the extension shows one segment per usage window:

```
CC 5h: 15% resets in 2h · mois: 3% resets in 4d
OG 5h: 10% resets in 2h · mois: 27% resets in 13d
```

If you also have pi-token-speed installed, the quota appears to the **right of your TPS** readout (the `zz-quota` status key sorts right after `tokenSpeed`).

- **Two windows shown**: the **5-hour** window (tighter limit, with reset countdown) and the **monthly** billing period
- **Color-coded**: green (ok), yellow (≥70% used), red (≥90% used)
- **Reset countdown**: each window shows `resets in 2h` / `5m` / `1d` until it resets - the 5h window uses the provider's real reset timestamp; the monthly window uses the provider's reset timestamp when available (OpenCode Go), otherwise the next calendar-month start (Command Code)
- **Auto-refresh**: every 60s and after every agent turn
- **Command Code** shows the 5-hour window + monthly billing-period total
- **OpenCode Go** shows the rolling (≈5h) + monthly windows

## Install

```bash
pi install npm:pi-quota-monitoring
```

Then `/reload` or restart pi.

## Usage

Nothing to configure. Pick a model from a supported provider and the quota shows up in the footer.

## How it works

The extension reads the API key from pi's model registry (falling back to the standard auth stores), then queries each provider's usage endpoint:

- **Command Code**: `GET https://api.commandcode.ai/alpha/whoami` → `GET /alpha/billing/credits` + `GET /alpha/usage/summary` - computes the 5-hour window percentage and the monthly billing-period percentage (`used / total`).
- **OpenCode Go**: `GET https://opencode.ai/zen/go/v1/usage` - the API returns `rolling` (≈5h) and `monthly` percentages directly.

The status is set under the key `zz-quota`, which sorts alphabetically just after `tokenSpeed` in pi's footer (when pi-token-speed is installed), placing the quota to the **right** of the TPS display.

## License

MIT

# lovettsendit/hedgemony

## 关联链接

- https://api.commandcode.ai/alpha/whoami`
- https://opencode.ai/zen/go/v1/usage`

## 导航

- 项目页：[[10-项目/github.com_48c8e2ff]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
