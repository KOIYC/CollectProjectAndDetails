---
type: "corpus"
item_id: "147ae2ebf0d6b346"
title: "Show HN: Atomic Editor – Obsidian-style live preview for CodeMirror 6"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48345201"
project_url: "https://kenforthewin.github.io/atomic-editor"
author: "kenforthewin"
published_at: "2026-05-31T12:32:54Z"
captured_at: "2026-09-21T01:42:46+08:00"
lang: "en"
kind: "post"
topic: 开发者工具
shard: "2026-09-21"
pub_day: "2026-05-31"
tags:
  - 语料
  - hn_show
  - author_kenforthewin
  - story_48345201
  - show_hn
metrics: {"points": 67, "comments": 19, "engagement_velocity": 67}
comments_count: 19
comments_total: 19
discovered_via: "hn:show_hn:144d"
---

# Show HN: Atomic Editor – Obsidian-style live preview for CodeMirror 6

> [!info] 一句话导读
> Show HN: Atomic Editor – Obsidian-style live preview for CodeMirror 6

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48345201>
> 指标：点赞=67 · 评论=19 · engagement_velocity=67
> 作者：kenforthewin　|　发布：2026-05-31T12:32:54Z
> 项目链接：<https://kenforthewin.github.io/atomic-editor>
> 采集：2026-09-21T01:42:46+08:00　|　id：`147ae2ebf0d6b346`

## 正文

Show HN: Atomic Editor – Obsidian-style live preview for CodeMirror 6

## 评论（19/19）

> **pbjerkeseth** · 2026-05-31T15:05:49.000Z　
> Nice work! It seems like selection highlighting(?) doesn't work but the interaction feels good otherwise.I'm curious when I see things more geared toward prose using CodeMirror instead of ProseMirror. Any comment on that decision?

---

> **benatkin** · 2026-05-31T15:37:30.000Z　
> That looks pretty good, but it isn't quite there yet, for me. If you try to delete the opening fence, the closing fence turns into a closing fence, and the abstraction leaks in tables.

---

> **chaoxu** · 2026-05-31T15:44:00.000Z　
> I'm testing it and seems to be very broken, typing things around and things jumps everywhere.I was trying to create something like this too, because I need something that also work for mathematical writing. Let me push a version on github and update, it fixes a lot of issues.Unfortunately it works on my own version of markdown, which is a subset of pandoc markdown, but I think one can get claude to update the parser to work for other things.

---

> **segphault** · 2026-05-31T19:40:57.000Z　
> I've wanted to see a good, production-quality open source take on this editing paradigm for a long time and your implementation appears to get a lot of things right. I took a crack at this myself a few years ago but never got around to really getting it over the line: https://github.com/segphault/codemirror-rich-markdocYour wysiwyg support for tables is very nice, but I couldn't quite figure out how to delete a row. The checkboxes are also a little fiddly, it would be nice if the checkbox turned into editable text when the cursor moves next to it. Does Atomic Editor work with vim bindings via replit's CM6 vim plugin?Props for building this and sharing it, I hope you stick with it.

---

> **bdcravens** · 2026-05-31T20:29:32.000Z　
> Dreamweaver lives!

---

> **alsetmusic** · 2026-06-01T00:40:52.000Z　
> It's pretty nice. I was impressed with the handling of tables. Good fit-and-finish kinda of project. Congrats on building a respectable, nice tool.

---

> **k43s85** · 2026-06-01T04:59:51.000Z　
> 94439653

---

> **k43s85** · 2026-06-01T05:00:12.000Z　
> Ok 52itf orchid room

---

> **smartrich** · 2026-06-01T08:30:20.000Z　
> How difficult was it to build the live preview synchronization? Was keeping cursor position and scroll position aligned between the editor and preview the hardest part, or were there bigger technical challenges?

---

> **Alex_toani** · 2026-06-01T09:35:16.000Z　
> Perfect like this idea.

---

> **schonfinkel** · 2026-06-02T10:16:09.000Z　
> I regret to inform you that, despite your best intentions, you have built an Emacs + Orgmode.

---

> **peterm4** · 2026-06-03T00:31:07.000Z　
> This is awesome, and exactly what I've been looking for recently.Noticed the demo won't let me add spaces in table cells however.

---

> **bityard** · 2026-05-31T15:24:32.000Z　
> Selection worked for me on mobile, but doesn't show a highlight. Probably a simple CSS fix.

---

> **kenforthewin** · 2026-05-31T15:39:10.000Z　
> Thanks for the heads up - I pushed up a fix to the hightlighting issue.I originally went with Milkdown (Prosemirror-based) for Atomic, the knowledge base project that I built Atomic Editor for. ProseMirror doesn't provide virtualization out of the box. For shorter notes and even moderately long content it's fine - but atomic supports syncing content from a diverse set of sources and I noticed that long documents were causing delays on initial page load and some lag during edits. I didn't find anything like it with native virtualization that felt right to me so I built Atomic Editor.

---

> **kenforthewin** · 2026-05-31T15:51:45.000Z　
> Thanks for trying it out! would you mind giving some steps that allow me to repro the issue? It's early days so i'm sure there are some rough edges, hopefully I can fix them quickly.

---

> **kenforthewin** · 2026-05-31T19:51:44.000Z　
> I was able to repro one issue that could have been contributing to your broken experience - there's a slight delay between, for example, clicking text in a heading and having the "#" markdown decoration appear. This is to prevent the mouse location from shifting mid-click and causing text to be selected unintentionally (obsidian does this too). But there was a bug that was causing a cascading set of failures if edits happened during that delay window, which is likely what folks who are clicking around at random points in the editor and adding text are doing. I fixed it in 0.4.2, which should be live now.

---

> **pbjerkeseth** · 2026-05-31T16:36:27.000Z　
> No problem, I actually went through a similar path of trying milkdown/tiptap/a few others as the core for my own editor needs but kept running into into issues where the abstractions got in the way eventually. I was thinking about using ProseMirror for a custom 'one big text file' concept so I guess Ill close the door on that idea and give this a try.

---

> **chaoxu** · 2026-05-31T18:52:38.000Z　
> My version of a WYSIWYG built on top of CM6.https://github.com/chaoxu/coflatMine also have lot of bugs (especially reader and editor doesn't completely match yet).repro the issue: click random places and add random texts, scroll around, and issues come up sooner or later.

---

> **readthedangcode** · 2026-05-31T18:55:32.000Z　
> I just clicked around a bit and randomly typed, suddenly no matter where I typed, my text was ending up at the end of the document. Found it to be pretty broken as well.

## 导航

- 项目页：[[10-项目/kenforthewin.github.io_e39d658c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
