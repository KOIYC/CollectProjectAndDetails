---
type: "corpus"
item_id: "5d3af04fb7243678"
title: "Show HN: TypeScript7 LSP Claude Code Plugin"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48723931"
project_url: "https://github.com/mjn298/ts7-lsp-plugin/tree/main"
author: "seedlessmike"
published_at: "2026-06-29T19:27:48Z"
captured_at: "2026-09-21T03:11:04+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-06-29"
tags:
  - 语料
  - hn_show
  - author_seedlessmike
  - story_48723931
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: TypeScript7 LSP Claude Code Plugin

> [!info] 一句话导读
> Published: 2026-06-29

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48723931>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：seedlessmike　|　发布：2026-06-29T19:27:48Z
> 项目链接：<https://github.com/mjn298/ts7-lsp-plugin/tree/main>
> 采集：2026-09-21T03:11:04+08:00　|　id：`5d3af04fb7243678`

## 正文

Published: 2026-06-29
Author: mjn298

GitHub - mjn298/ts7-lsp-plugin: Claude Code plugin: TypeScript LSP backed by the native TypeScript 7 server (tsc --lsp) · GitHub

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| .claude-plugin | .claude-plugin | | |
| plugins/ ts7-lsp | plugins/ ts7-lsp | | |
| LICENSE | LICENSE | | |
| README.md | README.md | | |
| View all files | | | |

# ts7-lsp-plugin

A Claude Code marketplace that provides a TypeScript language server backed by the native TypeScript 7 server (`typescript@rc`), launched as `tsc --lsp --stdio`.

It replaces the official `typescript-lsp` plugin (which uses the Node-based `typescript-language-server` wrapper around the classic `tsserver`) with the faster native Go implementation.

> Unofficial. This is a community project and is not affiliated with, endorsed by, or maintained by Microsoft or the TypeScript team. "TypeScript" and `tsc` are products of Microsoft; this repo just wires the `typescript@rc` LSP into Claude Code. Provided as-is.

## Layout

```
.claude-plugin/marketplace.json   # marketplace "ts7-lsp-marketplace" → plugin "ts7-lsp"
plugins/ts7-lsp/README.md         # install + enable instructions

```

## Quick start

```
npm install -g typescript@rc                       # a TS7 `tsc` on PATH — any package manager works
/plugin marketplace add mjn298/ts7-lsp-plugin      # add this marketplace straight from GitHub
/plugin install ts7-lsp@ts7-lsp-marketplace
/plugin disable typescript-lsp@claude-plugins-official   # ONLY if you'd already installed the official TS LSP
/reload-plugins
```

> `mjn298/ts7-lsp-plugin` is shorthand for this GitHub repo. You can also pass the full URL (`https://github.com/mjn298/ts7-lsp-plugin`), or a local checkout path if you're hacking on it.

See `plugins/ts7-lsp/README.md` for full details and the switch-back instructions.

## License

0BSD — public-domain-equivalent, no attribution required. Do whatever you want.

Claude Code plugin: TypeScript LSP backed by the native TypeScript 7 server (tsc --lsp)

## 关联链接

- https://github.com/mjn298/ts7-lsp-plugin`

## 导航

- 项目页：[[10-项目/github.com_311fde66]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
