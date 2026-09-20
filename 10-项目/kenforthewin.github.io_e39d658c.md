---
type: "project"
title: "Show HN: Atomic Editor – Obsidian-style live preview for CodeMirror 6"
project_url: "https://kenforthewin.github.io/atomic-editor"
first_seen: "2026-09-21T02:52:45+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_kenforthewin
  - story_48345201
  - show_hn
lang: "en"
---

# Show HN: Atomic Editor – Obsidian-style live preview for CodeMirror 6

> [!info] 一句话导读
> Atomic Editor — demo

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://kenforthewin.github.io/atomic-editor>
> 首次收录：2026-09-21T02:52:45+08:00
> 来源渠道：HN Show HN
> 标签：author_kenforthewin, story_48345201, show_hn
> 最新指标：点赞=67 · 评论=19 · engagement_velocity=67

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:27:24+08:00 | HN Show HN | 点赞=67 · 评论=19 · engagement_velocity=67 | [[20-语料/posts/hn_show/2026-09-21/147ae2ebf0d6b346_Show-HN-Atomic-Editor-–-Obsidian-style-live-previe]] |
| 2026-09-21T01:42:46+08:00 | HN Show HN | 点赞=67 · 评论=19 · engagement_velocity=67 | [[20-语料/posts/hn_show/2026-09-21/147ae2ebf0d6b346_Show-HN-Atomic-Editor-–-Obsidian-style-live-previe]] |
| 2026-09-21T02:52:45+08:00 | HN Show HN | 点赞=67 · 评论=19 · engagement_velocity=67 | [[20-语料/posts/hn_show/2026-09-21/147ae2ebf0d6b346_Show-HN-Atomic-Editor-–-Obsidian-style-live-previe]] |

## 摘要正文

Atomic Editor — demo  Atomic Editor  CodeMirror 6 markdown editor with Obsidian-style inline live preview — WYSIWYG tables, syntax-highlighted code, interactive checkboxes, and cursor-scoped link unfold. Showing a 1 page sample.  Try it  Fenced code blocks pick up per-language syntax highlighting. The grammar loads lazily — only fences you actually open hit the wire:  // A tiny markdown chunker. Every token in this block is  // highlighted by a lazy-loaded CodeMirror grammar — open the  // "Sample" picker above and the TypeScript grammar only loads  // when a ```ts fence first appears on screen.  export function chunkMarkdown(input: string): string [] {   const blocks: string [] = [];   let cursor = 0;   while (cursor < input. length) {   const nextBreak = input. indexOf('\n\n', cursor);   if (nextBreak === - 1) {   blocks. push(input. slice(cursor));   break;   blocks. push(input. slice(cursor, nextBreak));   cursor = nextBreak + 2;   return blocks;  Tables render WYSIWYG. Click a cell to edit in place — inline markdown inside cells reveals its delimiters only when your cursor enters:  | Plain | Bold | Italic | Strike | Highlight | Link | | --- | --- | --- | --- | --- | --- | | pl…
