---
type: "corpus"
item_id: "67861861e81ac9c2"
title: "Show HN: Panel – A research workspace where the agent can build its own panes"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49712621"
project_url: "https://github.com/greentfrapp/panel"
author: "greentfrapp"
published_at: "2026-09-15T13:58:37Z"
captured_at: "2026-09-21T13:02:32+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_greentfrapp
  - story_49712621
  - show_hn
metrics: {"points": 53, "comments": 22, "engagement_velocity": 53}
comments_count: 21
comments_total: 22
discovered_via: "hn:show_hn:90d"
---

# Show HN: Panel – A research workspace where the agent can build its own panes

> [!info] 一句话导读
> License: MIT License

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49712621>
> 指标：点赞=53 · 评论=22 · engagement_velocity=53
> 作者：greentfrapp　|　发布：2026-09-15T13:58:37Z
> 项目链接：<https://github.com/greentfrapp/panel>
> 采集：2026-09-21T13:02:32+08:00　|　id：`67861861e81ac9c2`

## 正文

# greentfrapp/panel

- Stars: 78
- Forks: 7
- Watchers: 78
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-09-15T06:18:47Z

## Languages

- CSS
- HTML
- JavaScript
- Python
- TypeScript
- Vue

## Top Contributors

- greentfrapp (594 contributions)

---

## README

# Panel

A research workspace where the agent works beside you: chat, files, PDFs and notebooks in one dock, and the agent can also create custom viewers and apps when necessary

This is an early build for testers. Expect rough edges, and feel free to raise issues.

Screenshot of Panel in action.

## Before you start

- Node 22.18 or newer (or 24.12 and newer)
- pnpm
- uv, which fetches the Python it needs (3.12 or newer) by itself
- Claude Code, installed and signed in: run `claude` once and log in. The agent and the literature review run through it.

## Install and start

```sh
pnpm install
uv sync
pnpm start
```

Then open. `pnpm start` builds the app first, so the first start takes a minute. Ctrl-C stops everything it started.

## Where your things are

- `~/Panel/panel.db` holds your conversations and everything the agents did.
- `~/Panel/workspaces` is where new Workspaces are created, unless you pick another folder.

Both are outside this folder, so deleting or re-cloning the repo keeps them.

## What works

- Chatting with an agent that can read and write files, and asks before running a tool.
- Workspaces: a folder the agent works in, with its own chats and saved layout.
- Panes for files, PDFs, markdown and Jupyter notebooks. Notebooks run against a real kernel, and you and the agent can edit the same one.
- Long-running commands in the background, which you can watch and stop.
- Panes the agent writes for you when you ask to see something a built-in Pane cannot show.
- A literature review: ask the chat for one, and open its result from the tool card.

## What doesn't yet

- Currently only has full support for Claude Code.
- Modules start only by asking the chat. There is no button to launch one.
- The hypothesis Modules have no view of their own, so their results can be hard to read.
- Modules don't work with OpenAI API yet.

## The OpenAI key (optional)

Copy `apps/server/.env.example` to `apps/server/.env` and set `OPENAI_API_KEY`. This adds "OpenAI API" to the agent picker, for chat and tools.

It does not run literature reviews or the hypothesis Modules: those need an agent that can search the web, and today only Claude Code can. Without a key, the picker shows OpenAI as not set up, which is expected.

## If something's wrong

- **"Panel couldn't reach its server."** The server half is not running. Check the terminal `pnpm start` is in, then press Retry.
- **An agent shows as not set up.** The reason is written under the message box.
- **A port is already in use**, or the app answers but never loads: run `pnpm dev:doctor`. It says what is holding each port and how to clear it.

## Licence

MIT

---

## The idea

### UI

The UI has multiple configurable windows, called Panes, that can display things ranging from image files, data files, code, as well as chat sessions. This is critical for researchers who often have to context switch between different types of files.

A default set of Panes are provided for common use cases. But custom Panes can also be added by humans and agents, such as a PDB viewer or SQLite visualizer.

### Module Protocol

Modules are similar to Skills but with additional definitions to support inter-module workflows and integration with the workspace.

Specifically, Modules have typed definitions for Inputs, Outputs, and Intermediates.

Inputs and Outputs are straightforward. Intermediates refer to objects that provide observability, such as the Chain-of-Thought or scratchpad for an agentic Module, or may be intermediate outputs in a multi-stage Module. These are especially important for processes that need transparency or long-running jobs that should show progress.

Having typed definitions for these enable validation at runtime and make it easier for humans and agents to develop custom Modules for downstream tasks and Panes for visualizations.

#### Data Abstraction Layer

A data abstraction layer (DAL) bridges in-memory and filesystem objects. A DAL helps to map a URI to either an in-memory store or a local file, so that the Module just has to concern itself with the manipulation of the object.

# Lume — open-source terminal: command blocks, AI, remote control

## 评论（21/22）

> **greentfrapp** · 2026-09-15T13:58:56.000Z　
> Hi HN, I built Panel because research work means switching all the time between a chat with an agent, the papers I'm reading, the notebook I'm running and the data files I'm looking at.Panel is a local web app with dockable panes made with dockview. You get chat, files, PDFs, markdown and Jupyter notebooks.The agent can also create custom panes on request, like a protein structure viewer or an SQLite browser.There's also an early "Module" system. Modules are like Skills, but with typed inputs, outputs and intermediates, so a long job shows its progress and its results can feed the next step. Right now the working one is a literature review, with an early version for hypothesis generation.How it's built: a Vue + dockview frontend and a Python (FastAPI) sidecar that drives the agent backends. Everything runs on your machine.Honest limits for now:
> - Full support is Claude Code only, so you need it installed and signed in. Codex and other harnesses are not supported yet.
> - Still very rough around the edges, I've been adding to it as I use it myself. Feedback welcome!MIT licensed.

---

> **janket** · 2026-09-15T15:24:50.000Z　
> Sounds cool, can you explain a bit more how it works?

---

> **Gabry848** · 2026-09-15T15:29:38.000Z　
> In my opinion it can be more usefol if I can add it with an mcp server, so I can use with my agent and test it in real workflows to see if it can add power and some prons to my agent

---

> **AdityaK_9999** · 2026-09-15T16:59:29.000Z　
> The project seems to be a great initiative however does it have checkpoints? I find that feature a must with agentic workflow for very obvious reasons.

---

> **hellojebus** · 2026-09-15T17:05:28.000Z　
> I built a similar idea as a hobby project to see what was possible with harnesses. My idea was give a model a chat input, but outputs can be data models (sqlite), and panels that are custom react components that can be generated and mounted on the fly by the model.The basic idea in todo list form was:"Let's build a todo model to manage my daily tasks, then build a task list panel where i see today's todos."It got more interesting from there as I kept building ontop of it. For example, I added data hooks (trigger something when data changes, e.g. custom code or even webhooks) and it felt like an AI native Airtable.Everything persists and becomes the UI of the app itself.

---

> **ellg** · 2026-09-15T19:03:23.000Z　
> this is very easy (and fun) to do in emacs with gptel as wellyou can do a lot of very neat stuff when your llm has full access to a lisp repl that can self modify itself / the ui its running in

---

> **purple-leafy** · 2026-09-15T19:44:48.000Z　
> Hey OP I made something very similar called slices-ide [0]It’s a self modifying editor with embedded agents. Honestly that description doesn’t do it justice, it was an experiment in making an architecture to use the strengths of my adhd when coding.You can chat with agents inside the editor itself and ask them to modify ANYTHING in the IDE itself, including adding custom panels, changing the theme, rewriting logicHell, if they wanted to they can brick the entire editor too or remove agents entirely lol. There is a global undo / redo and timeline so as long as the timeline isn’t bricked you can step back to an earlier point in timeThe editor has a visualisation panel that shows all data flowing around the ide itselfYou might enjoy it, i think it’s cool and it’s very very experimental[0] - https://github.com/con-dog/slices-demo#slice-ide---an-experi...

---

> **purple-leafy** · 2026-09-15T19:50:45.000Z　
> Look into openrouter so you aren’t tied to just Claude or codex

---

> **xtiansimon** · 2026-09-16T12:31:19.000Z　
> I’m not familiar with this concept. So the purpose is to have a chat llm spawn new independent activity windows all in the same chat context?

---

> **wek** · 2026-09-17T13:18:20.000Z　
> This is cool! We have a similar approach in Nimbalyst... agent makes extensions that are human editable and agent editable ... includes Jupyter, markdown, csv, excalidraw, code, pdfs, browser. Its so nice not to have to app switch all the time. MIT as well. Maybe we should join forces?

---

> **greentfrapp** · 2026-09-16T00:50:33.000Z　
> It has a chat interface, but also lets you split the window into different sub-windows that can open different interfaces, like a Jupyter notebook (with a working kernel), a code editor, or a file browser. You can also ask the agent to create custom interfaces, like a protein structure visualizer, or an SQLite viewer, or just a simple place to manage your citations.Under the hood it's running on your local Claude Code instance, I'll probably be adding support for other APIs through Open Router soon.

---

> **greentfrapp** · 2026-09-16T00:46:52.000Z　
> I believe currently it would work if you've already set up the MCPs via Claude Code, because it's running off your local Claude Code under the hood. But I'll look into surfacing the MCPs like in the Claude app.

---

> **greentfrapp** · 2026-09-16T00:43:32.000Z　
> By checkpoints do you mean versioning and rollback?

---

> **rush86999** · 2026-09-15T17:56:57.000Z　
> I took it a step further with AI accessibility and recordings for teaching AI agents. Canvas context forms the who, what, when, where, and why, along with the agent conversation for training & agent maturity --- https://github.com/rush86999/atom/tree/main/docs/canvas

---

> **greentfrapp** · 2026-09-16T00:42:30.000Z　
> Yeah I know people who think that chat is the last UI we'll ever need, but I really think there's so much that can be done with malleable interfaces.

---

> **greentfrapp** · 2026-09-16T00:45:40.000Z　
> Thanks for sharing emacs + gptel! I'll find some time to try it out

---

> **greentfrapp** · 2026-09-16T00:41:05.000Z　
> The demo and videos are really cool! Just a few guardrails might make this a lot more usable as an actual IDE.

---

> **greentfrapp** · 2026-09-16T00:38:04.000Z　
> I will! Thanks for the rec

---

> **greentfrapp** · 2026-09-17T02:17:59.000Z　
> Actually it's something like a researcher-focused app that allows you to open Jupyter notebooks, code snippets, PDFs, right next to the chat window pane.Let's say you're working on protein design and you want to view the 3D structure of the protein, you can have the agent build a pane for that in the app, and you can ask the agent to help customize it as well.

---

> **AdityaK_9999** · 2026-09-16T16:46:25.000Z　
> Yes versioning and rollback to return to a previous state

---

> **hellojebus** · 2026-09-15T21:00:16.000Z　
> This is really cool! I'm glad there are others that had the same idea!I prototyped mine early last year and models weren't quite where they are today. I'll try to find some time to update the code and release it.

## 导航

- 项目页：[[10-项目/github.com_9ebc15d6]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
