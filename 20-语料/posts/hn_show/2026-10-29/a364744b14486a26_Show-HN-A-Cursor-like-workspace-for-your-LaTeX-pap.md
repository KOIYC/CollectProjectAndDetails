---
type: "corpus"
item_id: "a364744b14486a26"
title: "Show HN: A Cursor-like workspace for your LaTeX papers"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50284944"
project_url: "https://github.com/cu1ch3n/papilot"
author: "cuichen"
published_at: "2026-10-29T05:39:46Z"
captured_at: "2026-10-29T20:41:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-29"
pub_day: "2026-10-29"
tags:
  - 语料
  - hn_show
  - author_cuichen
  - story_50284944
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: A Cursor-like workspace for your LaTeX papers

> [!info] 一句话导读
> A Cursor-like workspace for your papers: annotate and review PDFs directly without ever touching LaTeX.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50284944>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：cuichen　|　发布：2026-10-29T05:39:46Z
> 项目链接：<https://github.com/cu1ch3n/papilot>
> 采集：2026-10-29T20:41:52+08:00　|　id：`a364744b14486a26`

## 正文

# cu1ch3n/papilot

A Cursor-like workspace for your papers: annotate and review PDFs directly without ever touching LaTeX.

- Stars: 5
- Forks: 0
- Watchers: 5
- Open issues: 4
- License: MIT License
- Homepage: https://cu1ch3n.github.io/papilot/
- Default branch: main
- Created: 2026-10-26T07:50:28Z

## Languages

- CSS
- HTML
- JavaScript
- TypeScript

## Topics

- academic-writing
- ai-agents
- ai-writing
- latex
- pdf-diff
- research-tool
- tex

## Top Contributors

- cu1ch3n (64 contributions)

---

## README

 Papilot

 A Cursor-like workspace for your papers: annotate and review PDFs directly without ever touching LaTeX.

 English · 简体中文

CI
npm
License: MIT
Node.js
TypeScript
React
LaTeX
PRs welcome

Codex
Claude
Antigravity

You read and mark up the PDF the way a supervisor marks up a draft. An AI agent makes the edits in LaTeX, and every change comes back to you as a before-and-after of the typeset page. Nothing touches your paper until you accept it.

## ✨ Features

 📝 Mark up the PDF
Select a sentence or circle an equation and say what should change. SyncTeX hands the agent the exact LaTeX lines.

 ✅ Approve change by change
Each edit comes back as a typeset diff. Accept, reject or comment on it, and undo any decision.

 📖 Read it like a real PDF
Jump to any section from the contents, search every page and zoom in sharply. Selecting text picks exactly the printed words.

 🌿 Commit when you're happy
Diff files and commit the ones you choose, with a commit message an agent writes. Pull and push, or merge a coauthor's changes and let an agent resolve the conflicts.

Also: ✨ **skills** such as Polish, Proofread and Check math, one `/` away, plus your own · 🤖 **Codex, Claude or Antigravity**, each with your own login · 🌳 **every task in its own Git worktree**, up to two at once · 🌗 **light and dark** · 📱 **runs on your computer**, and you can open it from your phone.

## 🚀 Quick start

> [!NOTE]
> You need **Node.js 22.22+**, **Git** and a full **TeX** distribution (MacTeX or TeX Live). Revising also needs one signed-in agent.

```sh
npm install -g papilot
papilot demo
```

Open **http://127.0.0.1:7274** and choose **PDF** in the sidebar. The demo adds an example paper to revise: a 26-page LaTeX paper about Papilot itself, full of equations. When you are ready, run `papilot` and choose **Add paper** to add any LaTeX project in a Git repository.

## 🤖 Agents

| Agent | Sign in once | How Papilot runs it |
| --- | --- | --- |
| **Codex** | `papilot codex login` | Through the Codex app server, in its workspace sandbox. Papilot uses your `codex` if you have one, or installs it on first start. |
| **Claude** | Start `papilot` with `ANTHROPIC_API_KEY` set | Through the Claude Agent SDK, downloaded the first time. The SDK does not accept a Pro or Max subscription login. |
| **Antigravity** | Install Antigravity and sign in to `agy` | `agy -p`, one process per turn, editing files only. If your region needs it, set `PAPILOT_AGY_PROXY`. |

Papilot never reads, stores or forwards your credentials. An agent that isn't installed or signed in shows as unavailable.

Having trouble getting started? Run `papilot doctor` for environment checks and fixes, or `papilot doctor --repo /path/to/paper` to check a paper too. Add `--json` for a machine-readable report. Diagnostics do not install software, start the server or change your paper. See the diagnostics guide for what is checked.

 ⚙️ Options and remote access

```sh
papilot --port 4400            # another local port
papilot --data ~/papilot-data  # keep state somewhere else (default ~/.papilot)
papilot service install        # macOS: start after login, restart if it exits
npm uninstall -g papilot       # remove it; your state stays in ~/.papilot until you delete it
```

Papilot listens only on `127.0.0.1`. To use it from another device, publish it on your tailnet with Tailscale Serve and set `PAPILOT_PUBLIC_ORIGIN` and `PAPILOT_TAILSCALE_LOGIN`. Papilot then checks the host, the browser origin and the Tailscale identity of every request. The guide has the steps.

 🛠️ Develop

```sh
git clone https://github.com/cu1ch3n/papilot && cd papilot
npm ci && npm run setup:review
npm run build && npm start
```

Run `npm run typecheck`, `npm test` and `npm run test:ui` before sending a pull request.

## 📚 Documentation

The **guide** covers every part of the workspace, the configuration variables, recovery after restarts, and development. The example paper in `examples/papilot-paper` explains the design in depth, with proofs. What changed in each release is in the changelog.

## 💬 Community

- 💡 **Questions and ideas**: Discussions
- 🐛 **Something broke**: open an issue
- 🤝 **Want to help**: pick a good first issue and read CONTRIBUTING.md

If Papilot saves you time on a paper, a ⭐ helps other researchers find it.

## 📄 License

MIT © 2026 Cui Chen. The bundled review engine in `vendor/latex-review` is also MIT-licensed.

# FENGARDE · Logs in. Evidence out.

## 评论（1/1）

> **bprathamesh2003** · 2026-10-29T07:08:30.000Z　
> Great work ! I wish this existed when I was writing my college thesis.Just curious about one thingHow is the typeset diff generated? Is it latexdiff under the hood, or do you compare rendered pages? I'm curious how it copes when one edit changes the pagination of everything after it.

## 关联链接

- http://127.0.0.1:7274**
- https://cu1ch3n.github.io/papilot/

## 导航

- 项目页：[[10-项目/github.com_a70ce4ce]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
