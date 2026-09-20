---
type: "corpus"
item_id: "d4fa1ca95200c8e1"
title: "Show HN: Compress your screenshots for AI coding agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48346481"
project_url: "https://github.com/mgranados/screenshotter"
author: "mgranados"
published_at: "2026-05-31T15:27:38Z"
captured_at: "2026-09-21T02:52:42+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-31"
tags:
  - 语料
  - hn_show
  - author_mgranados
  - story_48346481
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:144d"
---

# Show HN: Compress your screenshots for AI coding agents

> [!info] 一句话导读
> mgranados/screenshotter

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48346481>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：mgranados　|　发布：2026-05-31T15:27:38Z
> 项目链接：<https://github.com/mgranados/screenshotter>
> 采集：2026-09-21T02:52:42+08:00　|　id：`d4fa1ca95200c8e1`

## 正文

# mgranados/screenshotter

Small utility to compress screenshots in macos and copy to clipboard

- Stars: 5
- Forks: 0
- Watchers: 5
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-05-31T13:03:04Z

## Languages

- JavaScript
- Swift

## Top Contributors

- mgranados (1 contributions)

---

## README

# screenshotter

npm version
license
platform

Local macOS screenshots for coding agents.

Take a screenshot. `screenshotter` optimizes it locally and copies it to your clipboard.

## Preview

screenshotter toolbar output

## Install

Requires macOS and Node.js 20+.

npm package:

```sh
npm install -g @marttinn/screenshotter
screenshotter doctor
```

Try without installing:

```sh
npx @marttinn/screenshotter doctor
```

Development checkout:

```sh
git clone https://github.com/mgranados/screenshotter.git
cd screenshotter
npm install
npm run check
node bin/screenshotter.mjs doctor
```

When running from source, replace `screenshotter` with `node bin/screenshotter.mjs`, or symlink it:

```sh
mkdir -p ~/.local/bin
ln -sf "$PWD/bin/screenshotter.mjs" ~/.local/bin/screenshotter
```

## Use

```sh
screenshotter watch --verbose
```

Take a screenshot with `Cmd+Shift+3` or `Cmd+Shift+4`, then paste into Codex, Claude, or another agent with `Cmd+V`.

Optional menu bar:

```sh
screenshotter toolbar
```

screenshotter toolbar menu

This is the same watcher with a small menu-bar control. It needs Apple command line tools for the optional menu bar; without them, use `screenshotter watch`.

For pi:

```sh
pi install npm:@marttinn/screenshotter
```

Then run `/screenshotter on`.

## Savings

| Size | Original | Default | Size saved | Bandwidth saved / 1k |
| --- | ---: | ---: | ---: | ---: |
| Pro Display XDR 6016x3384 | 5.48 MB | 0.89 MB | 93% | 5.0 GB |
| 16in MacBook Pro 3456x2234 | 1.86 MB | 0.83 MB | 89% | 1.6 GB |
| 14in MacBook Pro 3024x1964 | 2.34 MB | 0.75 MB | 91% | 2.1 GB |
| Window 1920x1200 | 1.04 MB | 0.40 MB | 81% | 0.8 GB |
| Window 1440x900 | 0.63 MB | 0.38 MB | 68% | 0.4 GB |

Average from 5 recent screenshots. Default preserves readability. Downscale defaults are checked with Apple Vision text-readability benchmarks.

Default mode helps with:

- Upload bandwidth: often `2-5 MB -> <1 MB`.
- Paste/send latency: less image data for Codex or Claude to ingest.
- Local storage: optimized copies are smaller.
- Reliability: less likely to hit attachment limits.
- Readability per byte: efficient encoding while keeping dimensions high.

## Profiles

```sh
screenshotter watch --profile readability  # default
screenshotter watch --profile balanced
screenshotter watch --profile token
```

The menu bar and pi use the same profiles. In pi: `/screenshotter readability`, `/screenshotter balanced`, or `/screenshotter token`.

## Commands

```sh
screenshotter watch --verbose
screenshotter toolbar
screenshotter clip --target codex-app
screenshotter claude-app --verbose
screenshotter prepare-latest --target manual --json
screenshotter claim --target manual --json
screenshotter bench --latest 20 --tokens --json
screenshotter doctor
```

MCP, experimental:

```sh
codex mcp add screenshotter -- screenshotter mcp-server
claude mcp add screenshotter -- screenshotter mcp-server
```

For agent/tool discovery, see docs/agents.md.

Verbose runs write JSONL logs to:

```text
~/Library/Application Support/screenshotter/logs/events.jsonl
```

## License

MIT.

# Strudai

## 关联链接

- https://github.com/mgranados/screenshotter.git

## 导航

- 项目页：[[10-项目/github.com_12d4a7ef]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
