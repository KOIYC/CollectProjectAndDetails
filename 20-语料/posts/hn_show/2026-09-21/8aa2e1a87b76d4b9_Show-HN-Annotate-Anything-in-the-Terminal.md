---
type: "corpus"
item_id: "8aa2e1a87b76d4b9"
title: "Show HN: Annotate Anything in the Terminal"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49510102"
project_url: "https://plannotator.ai/tui-annotate"
author: "ramoz"
published_at: "2026-08-31T14:17:16Z"
captured_at: "2026-09-21T03:11:21+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - hn_show
  - author_ramoz
  - story_49510102
  - show_hn
metrics: {"points": 3, "comments": 1, "engagement_velocity": 3}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:52d"
---

# Show HN: Annotate Anything in the Terminal

> [!info] 一句话导读
> github.com/plannotator/herdr-annotate ↗ GitHub ↗

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49510102>
> 指标：点赞=3 · 评论=1 · engagement_velocity=3
> 作者：ramoz　|　发布：2026-08-31T14:17:16Z
> 项目链接：<https://plannotator.ai/tui-annotate>
> 采集：2026-09-21T03:11:21+08:00　|　id：`8aa2e1a87b76d4b9`

## 正文

Plannotator
plannotator-tui ↗
 github.com/plannotator/herdr-annotate ↗ GitHub ↗
Annotate anything in your terminal. Send it back to your agents.
Comment on any text in your terminal, review plans, specs, wikis and your agent's replies, and send the comments with a native human-in-the-loop UX.
GitHub ↗ Don't use Herdr? The core is plannotator-tui , a standalone terminal app.
Full
 macOS · Linux
What you get
 Comment on terminal text. Review plans, specs, wikis and agent replies with Plannotator TUI .
Comment on any terminal text: select, prefix + a
Review plans, specs, wikis: any Markdown file or folder, with a file tree: prefix + o
Review the agent's last reply: prefix + Shift + o
Per selection: comment, looks good, or delete
Send: the comments become the agent's next message
Ctrl-click a file://…md link to open it
Overlay, split, or popup placement
Claude Code, Codex, pi, Copilot CLI, Droid, omp, Hermes, OpenCode
Bundles plannotator-tui (macOS and Linux)
herdr plugin install plannotator/herdr-annotate Copy
Watch the Full install demo Keys
Lite
 macOS · Linux · Windows
What you get
 Comment on terminal text only. Select, press prefix + a , type. Nothing to download.
Comment on any terminal text: select, prefix + a
Manage comments: list, copy one, copy all, archive: prefix + m
Copy every comment as Markdown: prefix + Shift + a
Works over SSH and herdr --remote with two server settings
TypeScript only, runs on Bun; macOS, Linux, Windows
herdr plugin install plannotator/herdr-annotate/lite Copy
Watch the Lite install demo Keys
Demo
See it in Herdr
One video per install. The Full demo covers documents first, then the agent's last reply.
▶ Full install demo 1:17
 ▶ Lite install demo 0:39
▶ Watch on X
Full. First a folder: select lines, add comments, press Send. Then the agent's last reply, annotated the same way. The agent receives the comments as its next message." data-lite=" Lite. Select terminal text, press prefix + a , type a comment. Copy the comments and paste them into the agent."> Full. First a folder: select lines, add comments, press Send. Then the agent's last reply, annotated the same way. The agent receives the comments as its next message.
Watch the Lite install demo →
Full Review in place Select a line, then comment, mark it good, or mark it for deletion.
Full Send Each comment arrives in the agent with its line numbers and the quoted text.
Lite Manage prefix + m lists your comments. Copy one, copy all, or archive them.
How it works
What you can annotate
terminal text
 lite + full
 Any text on screen: logs, diffs, agent output.
Select the text with the mouse
Press prefix + a , type the comment, press Ctrl + S
prefix + Shift + a copies all comments as Markdown
documents
 full
 Markdown files: plans, specs, wikis, READMEs, or a whole folder.
prefix + o opens the current folder with a file tree
Select with the mouse or v . c comment, a looks good, d delete
Press Send (or E ). Comments from every file go to the agent
agent replies
 full
 The agent's last reply, read from its session.
prefix + Shift + o opens the agent's last reply
Comment on it the same way as a document
Press Send . The comments go back to the same session
Agent replies work with Claude Code , Codex , pi , Copilot CLI , Droid , omp , Hermes and OpenCode . Ctrl-click a file://…md link to open that file. The review opens as an overlay, a split, or a popup; set it in ~/.config/plannotator-tui/config.toml .
Setup
Bind the keys.
Required. The plugin does not add key bindings. Copy one block into ~/.config/herdr/config.toml .
full install keys terminal + documents + agent replies
[ copy ]
 # Terminal annotations
[[keys.command]]
key = "prefix+a"
type = "plugin_action"
command = "annotate.capture"
description = "annotate text"
[[keys.command]]
key = "prefix+shift+a"
type = "plugin_action"
command = "annotate.copy-context"
description = "copy annotations as context"
[[keys.command]]
key = "prefix+m"
type = "plugin_action"
command = "annotate.manage"
description = "manage annotations"
# Document review (plannotator-tui)
[[keys.command]]
key = "prefix+o"
type = "plugin_action"
command = "annotate.open"
description = "review documents in this folder"
[[keys.command]]
key = "prefix+shift+o"
type = "plugin_action"
command = "annotate.last"
description = "review the agent's last reply"
lite install keys terminal annotations only
[ copy ]
 [[keys.command]]
key = "prefix+a"
type = "plugin_action"
command = "annotate.capture"
description = "annotate text"
[[keys.command]]
key = "prefix+shift+a"
type = "plugin_action"
command = "annotate.copy-context"
description = "copy annotations as context"
[[keys.command]]
key = "prefix+m"
type = "plugin_action"
command = "annotate.manage"
description = "manage annotations"
Then run herdr config check and herdr server reload-config . Remote sessions need two settings on the server; see the README .
Built on
Plannotator TUI works without Herdr.
The document review is Plannotator TUI, a standalone program written in Rust. Open a plan, a spec, a wiki page or a whole folder, add comments, and export them as Markdown for any agent. It runs in any terminal.
$ brew trust plannotator/tap && brew install plannotator/tap/plannotator-tui [ copy ]
$ cargo install plannotator-tui [ copy ]
$ plannotator-tui plan.md [ copy ]
GitHub
 Releases
 crates.io
 Keys and command-line tools
 Part of Plannotator
Close
Herdr Annotate is free and open source (MIT).
herdr-annotate
 plannotator-tui
 Plannotator
 Herdr
 @plannotator

## 评论（1/1）

> **murzynalbinos** · 2026-08-31T15:40:27.000Z　
> This seems useful for debugging agent flows, but does it support streaming output or is it restricted to static text blocks?

## 导航

- 项目页：[[10-项目/plannotator.ai_ebbc33bc]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
