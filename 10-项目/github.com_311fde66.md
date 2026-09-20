---
type: "project"
title: "Show HN: TypeScript7 LSP Claude Code Plugin"
project_url: "https://github.com/mjn298/ts7-lsp-plugin/tree/main"
first_seen: "2026-09-21T03:11:04+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_seedlessmike
  - story_48723931
  - show_hn
lang: "en"
---

# Show HN: TypeScript7 LSP Claude Code Plugin

> [!info] 一句话导读
> Published: 2026-06-29

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/mjn298/ts7-lsp-plugin/tree/main>
> 首次收录：2026-09-21T03:11:04+08:00
> 来源渠道：HN Show HN
> 标签：author_seedlessmike, story_48723931, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:29:55+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/5d3af04fb7243678_Show-HN-TypeScript7-LSP-Claude-Code-Plugin]] |
| 2026-09-21T03:11:04+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/5d3af04fb7243678_Show-HN-TypeScript7-LSP-Claude-Code-Plugin]] |

## 摘要正文

Published: 2026-06-29 Author: mjn298  GitHub - mjn298/ts7-lsp-plugin: Claude Code plugin: TypeScript LSP backed by the native TypeScript 7 server (tsc --lsp) · GitHub  ## Folders and files  | Name | Name | Last commit message | Last commit date | | --- | --- | --- | --- | | .claude-plugin | .claude-plugin | | | | plugins/ ts7-lsp | plugins/ ts7-lsp | | | | LICENSE | LICENSE | | | | README.md | README.md | | | | View all files | | | |  # ts7-lsp-plugin  A Claude Code marketplace that provides a TypeScript language server backed by the native TypeScript 7 server (`typescript@rc`), launched as `tsc --lsp --stdio`.  It replaces the official `typescript-lsp` plugin (which uses the Node-based `typescript-language-server` wrapper around the classic `tsserver`) with the faster native Go implementation.  > Unofficial. This is a community project and is not affiliated with, endorsed by, or maintained by Microsoft or the TypeScript team. "TypeScript" and `tsc` are products of Microsoft; this repo just wires the `typescript@rc` LSP into Claude Code. Provided as-is.  ## Layout  ``` .claude-plugin/marketplace.json   # marketplace "ts7-lsp-marketplace" → plugin "ts7-lsp" plugins/ts7-lsp/README.md…
