---
type: "corpus"
item_id: "da1fc2dfdcefd6af"
title: "Show HN: Jauvex 1.2, two-way voice chat harness for Claude+Codex+Grok+Jev"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49886390"
project_url: "https://github.com/reindent/jauvex"
author: "daraosn"
published_at: "2026-09-29T00:31:44Z"
captured_at: "2026-09-30T18:57:07+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-29"
pub_day: "2026-09-29"
tags:
  - 语料
  - hn_show
  - author_daraosn
  - story_49886390
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Jauvex 1.2, two-way voice chat harness for Claude+Codex+Grok+Jev

> [!info] 一句话导读
> Your coding agents, side by side, by voice. Claude, Codex & Grok in one desktop app, with Jev for the fast decisions.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49886390>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：daraosn　|　发布：2026-09-29T00:31:44Z
> 项目链接：<https://github.com/reindent/jauvex>
> 采集：2026-09-30T18:57:07+08:00　|　id：`da1fc2dfdcefd6af`

## 正文

# reindent/jauvex

Your coding agents, side by side, by voice. Claude, Codex & Grok in one desktop app, with Jev for the fast decisions.

- Stars: 4
- Forks: 2
- Watchers: 4
- Open issues: 0
- License: Apache License 2.0
- Homepage: https://jauvex.reindent.com
- Default branch: master
- Created: 2026-09-24T17:21:43Z

## Languages

- HTML
- Shell
- TypeScript

## Top Contributors

- diegoaraos (9 contributions)

---

## README

# Jauvex

Your coding agents, side by side, by voice. Claude, Codex and Grok in one desktop app, with Jev (TypeSafe) for the fast
decisions. Jauvex Personal, version 1.3.0, for macOS; Apache License 2.0. Source: github.com/reindent/jauvex; site:
jauvex.reindent.com. Made by Reindent (one human and agents).

Jauvex is an Electron client for the Claude Code, Codex and Grok Build sessions on your Mac. Add a folder, pick up any of its
sessions or start new ones with either provider, and talk to them: a voice channel that answers in three beats (a quick
word, what it understood, a summary of the agent's answer), steers a working agent without interrupting it, names and
starts agents by voice, and lets agents talk to each other inside the app. No server: the window talks to the main
process over IPC, and your sessions stay where Claude Code and Codex keep them.

What changed in each release: CHANGELOG.md.

## Installing

One command in Terminal:

```
curl -fsSL https://jauvex.reindent.com/install | sh
```

It needs Node 22.18 or newer. It downloads this source, checks its SHA-256 and builds Jauvex on your Mac: nothing
prebuilt is downloaded, so there is nothing for Apple to notarize. Jauvex lands in Applications (`~/Applications` when
`/Applications` is not writable), a real app with its own name, icon and microphone permission; the source and the build
stay in `~/.jauvex/personal/app`. Run the command again to update, with Jauvex closed, or let Jauvex do it: it asks
jauvex.reindent.com which version is the latest (`/api/personal/version`), at launch and every six hours, and when a newer one is out
the sidebar's footer says so ("1.2.0 is out") and the Jauvex agent asks you, once per version, whether to update now. On a yes
(or "update the app" at any time) it runs `node scripts/jauvex.ts update`: refused while other agents work (`--now` on your word);
otherwise the app fetches the same install command, checks that it installs the version offered, leaves it and a small runner in
`~/.jauvex/personal/update/`, hands the runner to launchd and quits. The runner waits for the app to exit, runs the install command
(it rebuilds the app on your Mac and opens it), opens the old app again if it does not finish, and removes it; its log is
`update/update.log`. Only the app the install command made updates itself; a clone updates with git (T-165). To remove it, quit it and delete
`Jauvex.app` and `~/.jauvex/personal/app`; its settings stay in `~/.jauvex/personal`. To work on the code, clone this
repository instead: `npm start` runs it from the clone, and `npm run app` makes the same app in `tmp/mac-app/Jauvex.app`
(`scripts/mac-app.ts`: Electron's app renamed Jauvex, with the built app, the Whisper models, Claude and Codex inside, signed
ad hoc on your Mac).

## Setting up on a fresh Mac

Jauvex needs a few things that are not in this repository; the install command and `npm start` take care of most of them. The welcome screen (on the first start, and from Jauvex
settings after) checks each of them and tells you what is missing.

1. **Node 22.18 or newer** (it runs the TypeScript scripts and checks as they are), then `npm install` in this folder (it also fetches the Electron binary; if the app ever says
 `Electron.app does not exist`, run `npx install-electron`).
2. **Claude or Codex, signed in: at least one is a must.** Both binaries come with `npm install` (the Claude Agent SDK
 brings Claude Code, `@openai/codex` brings Codex), and Jauvex uses the account each one is signed in to on this Mac.
 You sign in with their own command lines, in Terminal: `claude auth login` (Claude Code; to install it,
 `curl -fsSL https://claude.ai/install.sh | bash`) or `codex login` (Codex; `brew install codex`). Jauvex signs no one in
 itself: Anthropic does not let apps built on its Agent SDK offer the Claude.ai login. The welcome screen and the accounts
 panel (the Jauvex button below the sidebar) say who is signed in and give the command; with one signed in, the Jauvex
 agent can walk you through the other.
3. **Grok, optional**: Grok Build, xAI's coding agent, when it is on this Mac (`curl -fsSL https://x.ai/cli/install.sh | bash`,
 then `grok login`). Jauvex runs it as `grok agent stdio` with your Grok account and settings; without it, Grok is simply not
 offered.
4. **whisper.cpp for the ears**: `npm start` installs it with Homebrew if it is missing and downloads the two models into
 `models/` (git-ignored): `ggml-small-q5_1.bin` for the transcript and `ggml-base-q5_1.bin` for the live words while you
 speak. Each is checked against the size and SHA-256 Hugging Face lists for it (`scripts/models.sh`): a download goes to a
 `.part` file and becomes the model once it is whole, so one cut short is downloaded again the next time, never taken for done. Other models from huggingface.co/ggerganov/whisper.cpp can be dropped in the same folder and picked in the
 voice settings (`ggml-large-v3-turbo-q5_0.bin`, 574 MB, hears better and is still quick on Apple silicon). Without
 Whisper you can still type.
5. **A TypeSafe key for Jev**, optional: in `TYPESAFE_API_KEY` or the file `~/.typesafe/token`, the key alone (the way Hugging Face keeps its token; the older `~/.typesafe/jev` still works). Without it the small voice model
 makes the decisions Jev would make, a little more slowly.
6. **The microphone**: macOS asks the first time voice mode is switched on.
7. **The voice** is macOS's System voice, through `say`. On a fresh Mac that is the basic Samantha, which sounds robotic:
 pick a Siri voice in System Settings > Accessibility > Spoken Content > System voice. An app cannot choose a Siri
 voice by itself (`say -v` falls back to Samantha); only that setting reaches them. The welcome screen checks this and
 has a button that opens the pane.

```
npm start        # builds, then launches through macOS LaunchServices (start.sh)
npm run dev      # Vite + Electron with reload, for working on the UI
```

Put the folder somewhere plain, such as `~/Coding/jauvex`: macOS protects Documents, Desktop, Downloads and iCloud Drive,
and an app started there cannot read its own files until it has been granted access (`npm start` then starts it from the
terminal instead, which works but attributes the permission prompts to the terminal). Only one copy may run at a time
(the app holds a lock; a second launch focuses the first). It keeps its own state in its data folder, `~/.jauvex/personal`
(every copy, run from source or compiled; `data/` below means that folder; `CVC_DATA_DIR` moves it), and uses ports 4340 (Vite, dev only) and 4341 (whisper-server), plus 4342 for the live words (Pro uses 4320 to 4322, so both can run side by side). Jauvex is built on
your Mac from this source: `npm start` runs it from the Electron binary in `node_modules`, the install command as Jauvex.app.

## What it does today
- **Add folder**: native folder dialog. Each folder is a project, like in Claude Code.
- **+ on a project**: lists every Claude, Codex and Grok session recorded for that folder (title, first prompt,
 provider, branch, size, last activity), with a switch to see all, only Claude's or only Codex's (with counts) and each
 provider's mark on its rows. Tick the ones you want; they appear under the project in the sidebar.
- **Folders fold, the sidebar resizes**: a click on a folder's name (its folder icon open or closed) folds its sessions
 away, and it stays folded after a reload. The sidebar's right edge drags to any width from 220 to 560 px, kept too.
- **Only a signed-in provider can be chosen**: a provider that is not signed in on this Mac is greyed out, with the reason,
 in the provider selector, in the Jauvex agent's move selector and in the default-agent setting; a new session never
 starts on one.
- **What agents are told about the thread**: it is plain markdown, so no LaTeX (formulas and matrices as plain text or a
 code block), no Mermaid or other diagram languages (plain-text drawings in a code block), no raw HTML, local files as
 paths in backticks rather than links, images as markdown images. Terminal colour codes in tool output are stripped.
- **A provider's failure is an error, not an answer**: a turn that fails, or an answer that is the provider's own failure
 text (an organisation that disabled subscription access, an allowance run out, a network error), shows as a red card
 in the thread, and the voice says one line about it instead of summing it up.
- **One provider per session, for life**: a session imported from Claude continues with Claude, one imported from
 Codex continues with Codex, one from Grok with Grok (each session row carries its provider's own tiny mark, Claude's, OpenAI's or Grok's, and a Jev agent row TypeSafe's; the title bar has a chip. The marks are their owners' trademarks, used only to say whose session it is: the first three from `@lobehub/icons-static-svg`, MIT; TypeSafe's is its site icon, `assets/typesafe.png`). A new session
 lets you pick the provider in the composer until the first message is sent; the model and effort pickers follow the
 provider (effort: Claude's fixed levels, or the levels Codex or Grok reports for the chosen model; applies from the next message)
 (Codex models come from your account through `model/list`, Grok's from its agent's model list).
- **Open a session**: the conversation loads. User messages as bubbles, Claude's replies as text,
 tool calls and thinking folded into one-line rows you can expand (a Codex call shows the moment it starts and gets
 its result when it completes), harness plumbing (reminders,
 tool results, cross-session messages) hidden unless you toggle the eye icon. Long sessions page
 from the end ("Load earlier messages").
- **The Jauvex agent**: one session that always exists, pinned at the top of the sidebar, with the app's own folder as
 its project and a briefing about the app itself. It is the entry point for everything about the app: restart it,
 update it (`git pull`, build, relaunch, on request), install what is missing, explain how it works, create agents and
 add folders (through the app's command line, below), and develop it for contributors. Every other agent is told it
 exists and to send it what concerns running the app, and that the app's code is theirs to work on too when the user
 asks and the source is in their folder (a Codex agent made a development agent once refused to read it, told that
 anything about the app was the Jauvex agent's). It runs on the default agent, keeps one session for life
 (`ui.jauvexSession`), and can be hidden in Jauvex settings (it still exists and still answers other agents).
 **It moves between providers with its whole context** (the only session that does, for now): the app keeps its own
 transcript of it (`data/jauvex-transcript.json`, user and assistant text only), the provider selector in its composer
 stays live, and the first message after a move carries the conversation so far as a prelude to a fresh session on the
 other provider, so Claude and Codex pick up where the other left off. Moving back works the same way. The thread shows
 the app's transcript, tool calls and results included (results trimmed), with a note at every move. A move ends voice
 mode (the voice engine and its acknowledgment model belong to the provider it started with): start it again when you
 like. Two ways to move, asked on the welcome when both providers are signed in and changeable in Jauvex settings:
 **unified** (the default, experimental: the app replays the whole conversation, and more can break) or **handover**
 (the leaving assistant writes a handover note in a visible turn, saved as `data/jauvex-handover.md` too, and the
 next provider starts from that note: cheaper on long histories, and the note says what mattered).
- **The app's command line** (`node scripts/jauvex.ts `, in the install folder): every action in the app, for
 agents, the Jauvex agent above all. `list` (folders, sessions, agents, ids), `add-folder`, `pick-folder` (the folder
 dialog for the user; what they choose is added), `new-agent` (provider, folder, name, purpose, first message; unnamed,
 the provider is the Jauvex agent's own; with no first message it starts with its own introduction, since an agent exists
 once it has had one: on 2026-09-24 one ordered without it was an empty chat that vanished), `open` (a session, or the Jauvex agent, on screen; a session not in its folder's sidebar goes in it too: shown only as an open chat,
 seven sessions an agent opened dropped out one by one as other chats took the eight open places, T-152, the user, 2026-09-26), `import` (a folder's existing sessions into its sidebar without opening them,
 as its search button does; with no session named, the ones not listed yet: T-150, the user, 2026-09-26, after an agent asked to
 import sessions opened them over the chat he was in), `send` (a message into a session),
 `rename`, `settings` (default agent, Jauvex row, welcome next time), `welcome`, `reload`, `restart`. It writes a
 request file in `data/commands/`, the running app does the thing and answers in a result file, the script prints the
 JSON. Nothing but files: no port, no server.
- **Default agent**: the provider new sessions and the Jauvex agent start with. Asked on the welcome screen when both
 Claude and Codex are signed in (Start waits for the answer); set automatically when only one is; changeable in
 Jauvex settings.
- **The right pane.** A file or a link an agent shows (a markdown link, a path, a URL) opens in a pane on the right of the
 chat, never in the window itself: markdown rendered, text and code as they are, images shown, PDFs and web pages framed
 in a ` ` of their own that starts muted and stays muted and opens no windows. The pane has an "open outside"
 button (the Mac for files, the browser for pages), a close button, and a draggable width that is remembered. A navigation
 the app did not catch (a link in a place it does not watch) is stopped in the main process and sent to the pane too.
 Later the same pane takes terminals and browsers. Relative paths resolve against the session's folder; a link inside a file the
 pane shows resolves against that file's folder, and opens in the pane too (T-183).
- **Boards** (T-171): a folder's to-do lists, plain markdown in the folder (`PROJECT.md`, `MARKETING.md`, `BOARD.md`, `ROADMAP.md`,
 `boards/*.md`): `## Section` headings (P0, P1, P2), items as `- [ ] **T-01 · Title** — body` with `[ ]` to do, `[~]` doing. A done
 task leaves the board, in the same edit, for the top of its done file beside it (`PROJECT-DONE.md`, `boards/x-DONE.md`), ending
 "— shipped YYYY-MM-DD (commit)"; a reopened one goes back to the top of the board's first section as to do; ids are unique across both
 files (T-174). A board written before brings its `[x]` tasks and its Done section there on its first write. The format has a version (T-173): a board's first line is ` ` (hidden when the markdown is shown); a board
 without it is v1 and gets it when the app writes it, and a board whose line names a newer version is shown as it is, never
 rewritten, with a note to update Jauvex. The file is the only truth and git its history; the agents keep them (every agent is told its folder's boards and how to
 keep them). They are listed under the folder's sessions, with how many items are done, and open as columns of cards, one per section,
 coloured by priority; a click on a card's circle moves it on (to do, doing, done: off to the done file); a click on the card shows its
 text; "Show done" adds the done file's tasks as a last column, where a circle reopens a task. Two views, switched in the board's header and remembered (T-180):
 Sections, a column per section, and Kanban, a lane per status (to do, doing, and done with Show done), each card tagged with its
 section; a circle moves a card to the next lane, in the file. A board's row, secondary click: Delete board, after
 a yes (the question names the file and its done file); both files go, and its view closes (T-179). A new board: the folder's options (New board), or
 `new-board --name "..." [--folder ...]` on the command line, which writes `boards/.md` from a template and opens it. A board an
 agent writes shows up within seconds (on a refresh, when the window comes back to the front, and every 15 s); markdown with no items
 is not a board. **Its own chat** (T-199; the user, 2026-09-28: talking to boards, "it's very important"): under the board, "Talk to
 this board", by text or by voice, as under a Jev agent. A session of its own in the folder (the Jauvex agent's provider), told on
 every message what the board is now (the board itself, or, past 30 KB, to read the file) and the boards format; it adds, takes,
 moves and finishes items by editing the board's files, and the board redraws after every answer. Its session is kept in the app's
 state for that board's file (a board's folder is often a repository: nothing of ours is written there), and it is left out of the
 folder's list of agents. A folder reached through a symlink keeps its history too: Claude Code files a session by the real path,
 and the app looks there as well (`tests/window/board-chat.test.ts`).
- **Workflows** (T-210): a workflow is a markdown file in the folder, `workflows/.md`, and a folder beside it, `workflows/ /`,
 with one file per step: its instructions. The workflow file has a title and a line, `when:`, then the steps in order, one heading each:
 `## 1. Script → Video Agent`, the step's name linked to the file of its instructions, and who does it; `→ you`
 makes a step a human-in-the-loop gate (never a person's name). A step's file holds only what its agent is told, in plain words. They are
 listed under the folder, between its sessions and its boards; a new one comes from the folder's options (New workflow) or
 `new-workflow --name "..."`, and starts as a Hello World that runs as it is: the Jauvex agent says hello, you approve, it writes the
 greeting down in the run's folder. The app's own agent is the one a step goes to when no agent is named, since every install has it.
 - **The view**: one line, one row per step with its agent and the state of the current run; click a row for its details in the right pane,
 the file name to edit the markdown in place (the flow follows, the file is saved), and "All runs" for the history. Everything is editable
 without the markdown: the title and the line under it in place; a step's pane opens to be read (who does it, its instructions and the
 file they are kept in, how it went in its last runs), and **Edit** opens its editor: who does it, picked from **In this folder** first,
 then **Elsewhere** (the Jauvex agent first, then the other folders' agents), or you; its instructions; an optional title (without one,
 the step is called by its instructions, cut short). A + on the line between two steps adds one there; a step can be removed. Each edit
 rewrites only its part of the file (`shared/workflow-edit.ts`), and a step's file is made, renamed and removed with it; the app reads
 and writes a step's file only in the workflow's own folder. **The sidebar's order** (T-224; the user, 2026-09-29: "when it needs a human
 supervision, it should be on top, 100% ... then by those that were last modified, not created or last run"): the workflows waiting for
 you first, then the running ones, then the rest by the last change of their file or their steps' instructions, the newest first
 (`sortWorkflows` in `shared/workflow.ts`, `tests/workflow-parse.test.ts`).
 - **Running one**: the Run button, or an agent's `run --workflow --folder ` (a workflow written a moment ago is found: the
 folder is read again when the window's list does not have it yet), sends step 1 as one message to the agent it
 names, through the channel the agents already use, with its instructions, the previous step's words and how to end
 (`OUTCOME: /runs/NNN.md` (started, result, took, each step's time and last
 words), and a folder for its files; the view derives the live run, the history and the averages from them. When a run starts, the
 workflow file and each step's instructions are compared with the latest version: the run takes it when nothing changed, else a new one,
 `workflows/ /versions/NNN.md`, whole; editing takes none. **Versions** lists them, and any other than the current one can be
 restored (what the workflow was is kept as a version of its own first, so nothing is lost).
 - **Tries**: a step may come round as many times as its tries with no decision of yours in between; past that, a loop between agents alone
 stops the run. A decision of yours starts the count again, so a loop through you has no limit. A workflow's number is its `tries:` line
 (6 when there is none); a new one is written with the number in Settings, General, Workflows; a step can say its own, `tries: 1`.
 - **Triggers**: `when:` is manual, a schedule (`every Monday 09:00`, `every weekday 8:30`, `every day at 7pm`, `every 2 hours`), a window
 (`anytime between 9 and 12 am`: once a day, at a random time in it, at its end at the latest) or an event (`after `: when that one ends done, read from the folder then, so one written a moment before counts too). Schedules are the app's own timer: every 15 s it reads the folder's workflows again (an edited `when:`
 line counts at once) and starts one whose slot is under ten minutes old, once per slot, while the app is open. A schedule missed while
 the app was closed (or the computer asleep) is the setting's, in Settings, General, Workflows: run it as soon as the app opens, have the
 Jauvex agent tell you and ask whether to run it now (the default), or do nothing; only the latest missed time of each workflow counts
 (`settings --workflow-missed run|alert|nothing`). A run records who started it (`by: its schedule (every weekday 6:32)`).
 - **Talk to a workflow**: under the flow sits a chat of its own (a hidden session in the folder, kept in `workflows/ /chat.json`),
 told on every message what the workflow is now, its steps' instructions included: it edits the files (the flow follows), and runs it,
 stops it or passes its gate on your word. It writes to the app's agents and hears back as any chat does: the router knows it as
 " workflow" while its view is open and delivers to it there; a board's chat is reached the same way, as " board".
 - **Moving one to another folder** (T-217; the user, 2026-09-29: "The workflows were actually moved But the sessions of the agents were
 not"): every provider files a session by the folder it works in, so a workflow moved by hand takes its files and leaves its chat's
 session under the old folder, and its chat opens empty. `move-workflow --workflow --to [--folder]` moves
 the file, its folder (steps, runs, versions, `chat.json`) and the chat's session, and puts the files back if the session cannot move:
 Claude Code's transcript to the new folder's place (` /projects/<folder, dashed>/`, by the folders' real paths, with what it
 keeps beside it, every line's working folder rewritten, its time kept), Grok's session folder to the new folder's
 (`<GROK_HOME>/sessions/<folder, URL-encoded>/`), and a Codex thread resumed in the new folder, which Codex records in the thread
 (`electron/move.ts`, `moveThread` in `electron/codex.ts`, `moveSession` in `electron/grok.ts`). `move-session --session
 --to ` moves one agent the same way, with what the app keeps for it (its place in the list, provider, settings, context); it
 works in the new folder from its next turn. Neither runs while the session works or the workflow runs. A step's agent is found by name
 wherever it lives. Checks: `tests/move-session.test.ts` (a folder reached through a symlink too), `tests/window/move-workflow.test.ts`.
 - A workflow is deleted from its row's secondary click, after a yes, with its folder (instructions, runs, versions); one that runs is
 stopped first. Every agent that runs in a folder is told its workflows, and that a step of its own ends with the OUTCOME line.
- **Images an agent shows** (a markdown image with a local path, relative to its folder or absolute) load from the file
 and never overflow the thread (at most the thread's width and 60% of the window's height).
- **Images in a message**: paste a screenshot from the clipboard into the composer, drop image files on it, or pick them
 with the clip. They show as thumbnails until sent and in the thread after. Claude gets them inline; Codex gets each
 as a file under `data/uploads/`. Typed while a turn runs, they queue with their text: each queued bubble keeps the images
 pasted with it (shown as thumbnails), goes out with them when the turn ends or when its Send now hands it to the running
 turn, and the sent bubble shows them. An image never rides along with another queued message. PNG, JPEG, GIF and WebP.
- **Sessions keep working when you look elsewhere**: every chat you open stays mounted in the background (up to eight;
 idle ones make room, a working one never does). Opening another session or agent does not stop or lose the running
 turn, its row in the sidebar shows the moving mark while it works, and the answer is there when you come back. The
 microphone stays with the session it was started in (its orb waits at the bottom of the sidebar, see Voice).
- **Jev agents** (when a TypeSafe key is on this Mac): pick "Jev agent" in a new session's provider menu. It is not a
 chat, it follows Jev's own shape. Left, split in two: the **state** on top (text or JSON) and the **questions** below
 (JSON: `noul` yes/no, `choice`, `score`). Right: the **output**, each answer with its probabilities as bars, the
 confidence, the model, milliseconds and tokens; "Raw JSON" shows the reply as it came. Evaluate or Cmd+Enter. Edits save
 themselves, the last 20 runs stay one click away, and the agent lives in the sidebar (filled dot) with rename and
 delete. Jev stores nothing, so agents and runs are kept in `data/state.json`. A new agent starts with a working example.
 **Trainer (optional)**: Jev cannot be talked to, so an agent can be coupled with Claude or Codex ("Trainer" next to
 Evaluate). A chat panel opens under the pad, with everything a chat has here: text, voice, models, effort,
 permissions. The trainer sees the state, the questions and the last output with every message, and changes the agent
 by answering with `jev-state`, `jev-questions` and `jev-evaluate` blocks, which the app applies and runs; it is shown
 the result (twice at most per request) so it can adjust. Its session stays out of the sidebar. The agent is a reusable
 classifier: the questions stay, the state changes.
- **Secondary click on a session** in the sidebar opens its menu: Rename, Copy session ID, Remove from sidebar (nothing is
 deleted: the session stays with its provider and comes back with +).
- **Each session remembers its own composer**: model, effort and permissions are kept per session (and per Jev agent's
 trainer) in `data/state.json` and come back with it, across restarts. A new session starts from the last choices made anywhere.
- **Rename a session**: that menu, the pencil next to its name in the title bar, or double-click the name there or in the sidebar.
 Enter saves, Escape cancels. The name is written where the provider keeps it (`renameSession` for Claude, a
 custom-title entry in the session file; `thread/name/set` for Codex), so Claude Code and Codex show the same name.
- **Chat**: type in any session and Claude continues it (same login, settings, CLAUDE.md and tools as
 Claude Code, through the Agent SDK's `query({ resume })`). Replies stream in; Stop interrupts; the pencil
 icon on a project starts a new session in that folder; the model picker applies to the next message.
 Tools that need permission show an Allow once / Always / Deny card in the thread, or pick **Auto permissions** in the
 composer: Claude's permission classifier (`permissionMode: 'auto'`) or Codex's automatic reviewer
 (`approvalsReviewer: 'auto_review'`) decides, and only what it will not decide reaches you. Applies from the next message.
 **YOLO — full access** (asked for 2026-09-26) runs tools with no permission prompt and no provider sandbox: Claude's
 `bypassPermissions` with its required opt-in, Codex's `never` approvals with `dangerFullAccess`, Grok's `yoloMode`. Agents can
 then use everything this account can reach; it grants no administrator access, and the operating system's own limits still apply.
 **Provider permissions** (Jauvex settings › Safety, or `settings --permission-provider claude --permission-mode yolo` on the
 command line) set Ask, Auto or YOLO for every session of one provider, from each session's next turn; the composer then shows that
 mode, locked; "Use session setting" (`--permission-mode session`) gives the choice back to each composer. Leaving YOLO gives Codex
 back the approvals and sandbox the thread had before it, a read-only one included, kept in the state across restarts.
 Codex sessions work the same way: replies stream, Stop interrupts the turn, and when Codex asks before running a
 command or writing files, the same card appears (Always = for the rest of the session). Approval policy and
 sandbox are whatever your Codex config says, the way the Claude side keeps Claude Code's settings, except in YOLO.
 Grok sessions work the same way too: replies stream, Stop cancels the turn, and when Grok asks before a tool its
 permission rules do not allow already, the same card appears (Always = Grok's own "don't ask again"). The rest is Grok's
 own permission rules; the app says the mode every time a session is opened (Ask, **Auto permissions**, Grok's automatic mode, or
 YOLO), so a Grok set to always approve still asks in Ask, and a new mode closes and reopens a loaded session to take it. A message handed to a working Grok is read at its next step (`x.ai/interject`); one handed over after its last step
 Grok runs as a prompt of its own, and the turn stays open until that one is answered too, so its answer is not lost.
 A picture Grok makes (its `imagine` tool) shows under the tool's row, and the answer's link to it points at the file Grok saved
 in its own session folder: Grok writes it relative to that folder (`images/1.jpg`), which read against the project's folder
 was a broken image.

## Voice
Press the white round button in the message box. All local except the two Claude calls:
- **The app's name, however it is heard**: speech-to-text writes it Jovex, Javex, Jauvix, Claudex, Jobex and worse; every
 transcript says Jauvex (a saved vocabulary that still had the old name is corrected too).
- **Ears**: whisper.cpp (`brew install whisper-cpp`), kept warm as `whisper-server`. Put a model in `models/`
 (ignored by git): `curl -L -o models/ggml-small-q5_1.bin https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-small-q5_1.bin`
 (190 MB, about 0.4 s per utterance on Apple Silicon). Transcription starts the moment you go quiet, so the text is
 ready when your pause ends. When whisper-server cannot start, the app says why within a second, on the welcome screen and
 under the orb: a model it cannot load (named, with the command that downloads it again) or a port another program holds
 (named, with that program). whisper-server prints its error and then, on the Mac's GPU, a crash backtrace as it exits; the
 app reads the error, and the flight recorder keeps all it printed. The welcome calls Whisper ready only once its server answers.
- **Transcription settings** (voice settings): which Whisper model in `models/` to use (Automatic = the fastest), and
 "Names it should know". The names, plus the open folder's name, go to `whisper-server` as its initial prompt at
 start-up (the per-request prompt field is ignored by the server), so changing either restarts it. Measured on this
 Mac with test phrases: small without names heard "Clothex / Cotex / Reigned-in"; small *with* names got every name
 right in about 0.55 s; large-v3-turbo took about 2.2 s and still missed them. Whisper's ghosts are dropped: handed a knock or room noise it writes real phrases ("Thank you."), so a transcript is
 discarded when Whisper itself was unsure (very low confidence, a known ghost phrase at low confidence, or a no-speech
 probability over 0.6 on text that is short or doubtful: a real sentence Whisper was sure of is never dropped on that score alone,
 a short greeting once scored 0.74 with every word right); a clearly spoken "thank you" still goes through, the debugger shows
 every drop and why, and a dropped sentence of three words or more leaves a note under the composer instead of vanishing. The closing pause is trimmed before
 transcription, and every dictated message reaches the main model tagged `[voice transcript]` (T-76: in the turn, when steered, from the
 queue, and on a resend; the window never shows the tag), while a message typed with voice mode on goes untagged: the briefing tells
 the model a tagged message is a transcript, to repair names and odd words, and to ask in one line when a word does not fit.
- **The big model's answer stays on screen in full and is never read aloud.** A small model (Haiku by default) is the
 voice: it acknowledges and restates what you asked while the selected model thinks, and when the answer lands it
 says what happened in one to three sentences. A short plain answer is spoken as it is.
- **Mouth**: macOS `say` (the system voice by default), rendered per utterance and played inside the app, so it can
 fade out instantly and the echo canceller knows what the speakers are playing.
- **Interrupting, two channels**: start talking and the *voice* stops (playback fades in 120 ms, pending `say` renders are
 killed) and it never talks over you. The *main thread is not touched*: it keeps working, and its answer is still summed
 up when it lands. What you *type* (Enter) while it is busy shows up as a dashed "Queued" bubble and is sent by itself
 the moment the turn ends; what you *say* is steered into the running turn (next point). The voice also weighs what you meant: a clear "stop, cancel that" interrupts the main
 thread ("I'll take care of that right away"), and "not that, do X instead" interrupts it and sends X next. In doubt
 it queues; work is never stopped on a guess. A short utterance with a stop word ("stop", "cancel that", "para") never
 waits for that judgement: it interrupts the main thread straight from the transcript, already from the speculative
 one taken 240 ms into your pause. Otherwise only the Stop button interrupts the main thread. Tapping the orb also shuts the voice up.
- **"Restart the app"** (said or typed while voice mode is on) makes the app relaunch itself with the build on disk.
- **"Reload the interface"** / "soft restart" (said or typed while voice mode is on): the window alone reloads the UI build on
 disk; the main process, Whisper, the voice helper and every running turn stay. The reloaded window asks the main
 process which turns are still running and takes them back under their ids, so an answer in flight lands where it
 should. For a change to colours, layout or any window code, `npx vite build` and this is enough; a change to
 `electron/*` or `shared/*` still needs the full restart.
- **One copy, always**: only one Jauvex may run per data folder. A second launch exits at once, before it opens a
 window or touches a session, and brings the running copy to the front. Two copies would drive the same sessions
 (a resumed session forks, work is done twice, `data/state.json` is overwritten).
- **Agents talk to agents, through the app.** No provider tool, no protocol between Claude and Codex: the app already
 sees every reply and can reach every session. An agent writes a fenced block in its reply:
  ```
  ```message-agent Notes
  What is the code word of the day?
  ```
  ```
  When its turn ends the app delivers the text to that session, tagged `(from agent "Sender" [id])`: steered into the
  running turn if that agent is working, sent as a new turn otherwise (the session is mounted in the background if it
  was not open). A message that wants its own answer is never handed to a turn under way that answers someone else, nor is a
  workflow's step: it waits in the queue with its address and goes as a turn of its own (T-228: a chat kept one address for its turn's
  answer, and an answer went to an agent that had asked a question meanwhile; `shared/delivery.ts`, `tests/delivery.test.ts`).
  Whatever the other agent replies comes back to the sender by itself, tagged the same way, so an
  explicit message is a question and no block is needed to answer it; an answer does not bounce back again, so two
  agents cannot ping-pong on their own (and the app stops relaying after 30 agent-to-agent messages in ten minutes).
  A reply that goes back to its sender leaves out the blocks it addressed to other agents (they went to them) and says who
  else was written to. A Claude agent that left a background job running (a shell command in the background, a monitor)
  used to swallow the next message: its next turn answers only the job's "stopped" notice, empty, in under a second, which
  read as "the third message between agents fails". A Claude turn that ends like that sends its message again, once, with
  its reply address; and every agent is told not to start background work from a turn.
  This block is the only channel between the app's agents, in both directions, Claude to Codex and Codex to Claude; the
  briefing says so plainly, and that the harness's own agent tools, chat skills and shared files never reach them (a Claude
  agent once set up a file-based chat protocol instead). A Claude session also gets the same channel as two tools of its
  own, `mcp__jauvex__message_agent` and `mcp__jauvex__list_agents` (an in-process MCP server from the Agent SDK, answered
  by the window's router, never asking permission), for the models that look for a tool when told "talk to X". Agents are addressed by name (title or summary) or by the short id in brackets, which never changes (6 characters,
  longer only where two ids share their start, as Codex ids often do); a fenced `list-agents` block gets the roster back
  (name, id, provider, folder, working or idle). The Jauvex agent is listed once, as "Jauvex", whatever its past sessions
  across providers, and always, its chat open or not (T-151, the user, 2026-09-26: an agent that wanted to report a bug to it found
  three "Jauvex …" agents and not it, since it was listed only while its chat was open): a message to it opens its own chat in the
  background, with its session, or starts one; with no session yet, its folder's id stands in for its id; a session with no name of its own is shown by its first message, cut at 60 characters. Every exchange shows in both
  threads, marked "From agent X", and in the voice log. The briefing tells every agent all of this.
- **Every agent is told where it is running.** A blank session knows nothing about this app, so each one, on either
  provider, new or resumed, gets a short briefing (`clientBriefing` in `shared/types.ts`; appended to Claude's system
  prompt, sent as Codex's developer instructions): several agents side by side, messages that arrive mid-turn are new
  information to fold in (not a restart), the full answer is on screen while a separate small model speaks a short
  version (so: conclusion first, short plain answers for simple questions), a turn can be stopped at any moment, and in
  voice m

## 评论（1/1）

> **daraosn** · 2026-09-29T00:35:53.000Z　
> Hi everyone, I had announced the open-source harness I use to orchestrate my agentic workforce using voice: Jauvex. I have just updated it to v1.2 and it now includes task boards with optional Kanban view.Next up: I will be open-sourcing workflows and routines, which I already have working in the development version I use, this is something that is extremely useful to keep agents working 24/7 and do automated work (with human-in-the-loop capabities).Here is the original announcement:
> https://news.ycombinator.com/item?id=49863700

## 关联链接

- https://claude.ai/install.sh
- https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-small-q5_1.bin`
- https://jauvex.reindent.com
- https://jauvex.reindent.com/install
- https://x.ai/cli/install.sh

## 导航

- 项目页：[[10-项目/github.com_f0f18d90]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
