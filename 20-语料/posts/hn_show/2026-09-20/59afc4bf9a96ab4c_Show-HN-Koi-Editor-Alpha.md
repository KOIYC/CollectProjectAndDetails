---
type: "corpus"
item_id: "59afc4bf9a96ab4c"
title: "Show HN: Koi Editor Alpha"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49756627"
project_url: "https://koieditor.com/"
author: "hackermanai"
published_at: "2026-09-18T16:21:45Z"
captured_at: "2026-09-25T13:54:35+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - hn_show
  - author_hackermanai
  - story_49756627
  - show_hn
metrics: {"points": 5, "comments": 2, "engagement_velocity": 5}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:90d"
---

# Show HN: Koi Editor Alpha

> [!info] 一句话导读
> A fast, minimal, local-first, scriptable code editor for macOS

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49756627>
> 指标：点赞=5 · 评论=2 · engagement_velocity=5
> 作者：hackermanai　|　发布：2026-09-18T16:21:45Z
> 项目链接：<https://koieditor.com/>
> 采集：2026-09-25T13:54:35+08:00　|　id：`59afc4bf9a96ab4c`

## 正文

GitHub Discord

koi.

# Your text editor

for code

A fast, minimal, local-first, scriptable code editor for macOS

Download for Mac Pricing

v0.1.0-b211 (alpha) · Apple Silicon · macOS 13.2+ · Changelog

koi.py

```
 22960  # EditorContainer : _on_tab_label_clicked
 22961  @func_trace
 22962 def _on_tab_label_clicked(self):
 22963       editor = ensure_not_deleted(self.main_editor.editor)
 22964      if editor is not None:
 22965           safe_focus(editor)
 22966  
 22967  # EditorContainer : _on_tab_label_toggle
 22968  @func_trace
 22969 def _on_tab_label_toggle(self):
 22970       window = ensure_not_deleted(self.window)
 22971      if window is None:
 22972           return
 22973  
 22974       buffer = self.buffer
 22975      if buffer is None:
 22976           return
 22977  
 22978       window.buffer_manager.toggle_active(buffer)
 22979  
 22980  # EditorContainer : _on_tab_label_exclusive
 22981  @func_trace
 22982 def _on_tab_label_exclusive(self):
 22983       window = ensure_not_deleted(self.window)
 22984      if window is None:
 22985           return
 22986  
 22987       buffer = self.buffer
 22988      if buffer is None:
 22989           return
 22990  
 22991       window.buffer_manager.set_as_active_tab(buffer)
 22992  
 22993  # EditorContainer : _file_changed
 22994  @func_trace
 22995 def _file_changed(self, *_): [97 lines folded]
 23093  
 23094  # EditorContainer : _do_after_file_changed
 23095  @func_trace
 23096 def _do_after_file_changed(self): [5 lines folded]

```

```
 10373       directory = os.path.dirname(path) or "."
 10374       tmp_path = None
 10375  
 10376       os.makedirs(directory, exist_ok=True)
 10377  
 10378       fd, tmp_path = tempfile.mkstemp(dir=directory, prefix=".tmp_")
 10379  
 10380      try:
 10381          with os.fdopen(fd, "w", encoding="utf-8") as f:
 10382               f.write(text)
 10383               f.flush()
 10384               os.fsync(f.fileno())
 10385  
 10386           os.replace(tmp_path, path)
 10387           tmp_path = None
 10388  
 10389      finally:
 10390          if tmp_path is not None:
 10391              try:
 10392                   os.remove(tmp_path)
 10393              except OSError:
 10394                   pass
 10395  
 10396  # CodeEditor : _save_file
 10397  # @func_trace
 10398 def _save_file(self): [113 lines folded]
 10512  
 10513  # CodeEditor : _save_shadow_file
 10514  @func_trace
 10515 def _save_shadow_file(self): [18 lines folded]
 10534  
 10535  # CodeEditor : save_file_as
 10536  @plugin_api
 10537  @command("Save file as...")
 10538 def save_file_as(self): [20 lines folded]
 10559  
 10560  # CodeEditor : save_file_copy_as
 10561  @plugin_api
 10562  @command("Save copy of file as...")
 10563 def save_file_copy_as(self): [20 lines folded]

```

Line 22,974, Column 29 qwen2.5-coder:1.5b glm-5.3-flash:cloud ~/Desktop Python

Fast native editing

Built for macOS and optimized for low typing latency, even in very large files.

See the benchmarks →

Private AI

Run code completion and inline chat locally with Ollama. Your code doesn't need to leave your Mac.

A text editor, not an IDE

A focused, scriptable editor for code and text. No accounts, telemetry, or mandatory cloud services.

Large files

Open and edit files with millions of lines while keeping syntax highlighting and editing responsive.

Multi-window workflows

Work across multiple windows and split editors, with the same file open wherever you need it.

Scriptable

Customize Koi with Python scripts, commands, keybindings, and a documented scripting API.

Explore the API →

Flexible workspaces

Open files side by side, split them into horizontal panes, or detach tabs into separate windows.

Every view stays in sync automatically, even when the same file is open across multiple windows.

Multiple views, single document →

Tab multi-select →

Private AI completions

Run local models with Ollama, keep your code private, and choose the one that fits your machine and workflow.

AI-powered code suggestions are designed to stay fast, unobtrusive, and integrated into your editing workflow.

Local code completion →

Inline shell and chat

Run shell commands or chat with a local AI without leaving your editor. Send the current selection as a prompt and stream the response back into your document.

In-code shell and Python eval →

Inline AI chat →

Custom editor commands

Extend Koi with plain Python instead of learning a plugin framework.

Write editor commands, bind them to shortcuts, and use them like built-in features.

Use cases

Zero-latency typing

Koi maintains a measured P95 typing latency of 17.86 ms while editing a 1 million-line Odin source file with syntax highlighting enabled.

Read more →

Local AI, on your Mac

Koi works directly with local Ollama models, with no account, telemetry, or cloud intermediary. Use local code completion and inline AI while keeping your code and inference on your Mac.

Read more →

Native macOS code editors

A look at code editors built specifically for macOS, from long-running editors like BBEdit and TextMate to newer alternatives like Nova, CodeEdit, and Koi.

Read more →

Koi for note taking

Keep notes as ordinary Markdown, plain text, Org Mode, or other files. Open directly into your notes folder, search with ripgrep, and organize everything without a proprietary database.

Read more →

## Roadmap

What we're currently working on, and recently shipped.

Changelog Submit feature request →

Note taking improvements

Large file search optimizations

Tab multi-select

Multi-cursor editing

Multiple views, single document

Inline AI chat

Local code completion

Project-wide search

Context-aware auto-complete

Custom editor commands

Code scroller (minimap)

Emacs-like org mode for notes

In-code shell and Python eval

Hand-tuned native lexers for fast, precise syntax highlighting.

Asm

Bash

C

CSS

Clojure

C++

D

Diff

Elixir

Fortran

Gleam

Go

Haskell

HTML

Jai

Java

JavaScript

Julia

JSON

LaTeX

Lua

Makefile

Markdown

MATLAB

Mojo

Nim

OCaml

Odin

Org

Pascal

Perl

PHP

Python

R

Ruby

Rust

SQL

Swift

TOML

TypeScript

Typst

WAT

YAML

Zig

## Pricing

Personal Pre-release

$195 ~~$ 325~~

One-time payment

Single user

Unlimited machines

Commercial use

Buy once, own forever

Buy personal

Teams

$795 /year

For up to 10 users

Up to 10 users per license

Unlimited machines per user

Commercial use

One-year expiry

Buy for teams

Business

$19,995 /year

For larger organizations

Unlimited users

Unlimited machines per user

Commercial use

One-year expiry

Buy for business

Licensing FAQ.

End User License Agreement Privacy Policy

Why should I buy a license?

Koi Editor is free for non-commercial use. If you use it for work, a commercial license is required. That is how development is funded.

What is non-commercial use?

Non-commercial use includes learning, personal projects, hobby use, and evaluation. If you use Koi Editor for paid work, company work, client work, or any other commercial activity, a commercial use license is required.

Which license is right for me?

The Personal license is for one individual user. Teams and Business licenses are for organizations and multi-user use.

Working alone and using it professionally: Personal

Buying for a small group: Teams

Covering a larger organization with one license: Business

Can I use my Personal license at work?

Yes. A Personal license can be used for commercial work if you are the only person using the software. For multi-user use, choose Teams or Business.

When should we choose Business instead of Teams?

Teams is designed for smaller groups and covers up to 10 users per license. If you need to cover more users, you can either increase the Teams license quantity at checkout or move to Business at renewal.

I lost my license file, where can I get a new one?

You can recover your license file on License recovery →, using your Session ID displayed to you after purchase.

We can also help you recover your license, send an email to koi@hackerman.ai and include any information relevant to your purchase, such as email, name, business name, approximate date and time.

```json
{
            "@context": "https://schema.org",
            "@type": "SoftwareApplication",
            "name": "Koi Editor",
            "applicationCategory": "DeveloperApplication",
            "operatingSystem": "macOS",
            "description": "Koi is a fast native code editor for Ma. It makes typing feel instant. No distractions. Just fast, keyboard-first coding.",
            "url": "https://koieditor.com/",
            "offers": {
                "@type": "Offer",
                "price": "195",
                "priceCurrency": "USD"
            }
        }

```

# Headlines

## 评论（2/2）

> **nittanymount** · 2026-09-18T18:23:12.000Z　
> could you compare this editor with VSCode/Zed/...? wonder how people would pay for this editor.

---

> **eleventen** · 2026-09-18T22:51:52.000Z　
> I suspect they cannot, or else they would have on the website.

## 关联链接

- https://schema.org

## 导航

- 项目页：[[10-项目/koieditor.com_c4703408]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
