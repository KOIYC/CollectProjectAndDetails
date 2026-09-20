---
type: "corpus"
item_id: "69a62d8695ef5d18"
title: "Show HN: Agent Deck: Native Mac app for managing AI coding agents| powered by PI"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48344519"
project_url: "https://agentdeck.site/"
author: "streetcoder"
published_at: "2026-05-31T10:23:44Z"
captured_at: "2026-09-21T02:52:46+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-31"
tags:
  - 语料
  - hn_show
  - author_streetcoder
  - story_48344519
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:144d"
---

# Show HN: Agent Deck: Native Mac app for managing AI coding agents| powered by PI

> [!info] 一句话导读
> Features FAQ Download

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48344519>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：streetcoder　|　发布：2026-05-31T10:23:44Z
> 项目链接：<https://agentdeck.site/>
> 采集：2026-09-21T02:52:46+08:00　|　id：`69a62d8695ef5d18`

## 正文

Agent Deck
 Features FAQ Download
Built on the
CLI.
 A native Mac app for AI coding agents.
 Agent Deck is the native macOS app for Pi CLI – a supercharged cockpit that turns terminal-based agent sessions into a visual, project-aware workflow. Author specialist AI coding agents, curate per-project skills, and run parallel sessions in isolated git worktrees, all from a native Mac interface that sits next to your editor, not inside it.
 Watch every plan, tool call, and diff stream live in a color-coded transcript.
 Launch a session from any GitHub issue, run it in an isolated worktree, and
 merge the result back when it's done.
Download for macOS
GitHub 114
 from the terminal $ curl -fsSL https://raw.githubusercontent.com/a-streetcoder/agent-deck/main/install.sh | bash
 Free & open source
 macOS 26+
 Release v5.1.3 24 Jul 2026
What you get
 Color-coded transcript with plan, diffs, and approvals
 Cherry-pick skills from any repo or URL
 Author per-project agents with custom prompts and tools
 Parallel sessions in isolated worktrees, merged back in one click
 GitHub issues launch as ready sessions
 Per-project memory that learns from each session
 The interface
 Cockpit
 A Mac app you can actually use.
 Projects, sessions, and GitHub issues stay one click apart, not one terminal apart. You see what every session is doing, in real time, in a window that lives next to your editor.
 Color-coded streaming transcript with plan, tool calls, and inline diffs
 Project and session sidebar with multi-window, idle-parking, and terminal handoff
 Built-in Doctor that diagnoses your Pi CLI setup
Branch
 Fork the conversation, not your focus.
 Any session can branch. Fork it to explore a different direction with the transcript carried over, retry a prompt in a fresh session, or open a 1:1 with a single agent on its own model. Your context never gets cornered.
 Fork a session with the parent transcript captured as context
 Retry the same prompt without rebuilding the conversation
 1:1 sessions with any agent, each with its own model and thinking level
Your agents
 Library
 A real library for what your agents use.
 Cherry-pick individual skills from any GitHub repo or skills.sh URL. No need to clone the whole package. Keep upstream in sync. Decide which prompts, skills, and slash commands are active per project.
 Import individual skills from GitHub or skills.sh URLs
 Builtin, Global, Library, and Project scopes for what is active where
 AI-generated summaries so you know what each skill does before enabling it
Prompts
 Write it once, run it everywhere.
 Saved prompts and slash commands live in the same library as skills. Ship with builtins like investigate-a-bug and plan-a-feature, add your own, and assign them per project so the right shortcuts are always one keystroke away.
 Builtin prompts for everyday workflows, plus your own
 Slash browser in the composer: commands, prompts, and skills in one menu
 Per-project assignment, same as skills and agents
Author
 Build agents, run them in parallel.
 Agents are first-class objects with their own prompt, tools, skills, model, and avatar. Run them side by side in isolated worktrees, then merge completed work back with one click.
 Custom prompt, tools, skills, model, and avatar per agent
 Per-session git branch and worktree isolation
 One-click merge of completed worktrees back to the source branch
Your workflow
 Triage
 Issues are the start, not a detour.
 Browse repo issues inside a native board, pick one, and launch a session with the title, description, labels, and comments already loaded as context. Triage and execution stay connected.
 Native GitHub issue board inside the app
 Issue context auto-loaded into the session
 Sub-issue progress tracked alongside execution
Memory
 Your projects remember what matters.
 Turn on memory per project and sessions quietly accumulate the preferences, decisions, and gotchas that usually get retyped. Memories are plain files you can read, edit, and delete, recalled on demand instead of stuffed into every prompt.
 Per-project memory you can switch on or off
 Every memory is a readable file with type, scope, and history
 Recalled only when relevant, so it never bloats your context window
Autopilot
 The chores run themselves.
 Sessions name themselves with AI and keep their titles fresh as plans change. Commit and push from the toolbar with a model-written message. Let each new session run in its own branch and worktree, merged back when the work lands.
 AI-generated session titles that update as the plan evolves
 Commit and push toolbar actions with model-written messages
 Optional worktree isolation: every session on its own git branch
Make it yours
 Models
 Bring your own keys. Pi handles the auth.
 No extra subscription. Use your existing Claude, OpenAI, or local-model setup through Pi. Agent Deck adds a per-session picker, on-device drafting, and runtime tools.
 Per-session model picker across every Pi provider
 On-device Foundation Model for titles, commit messages, and summaries
 OpenAI fast mode and Exa web search built in
Yours
 Make it yours.
 Themes restyle the whole canvas, not just the accent color. Pick a preset like Tokyo Night, Nord, or Catppuccin Mocha, or build your own palette, and the entire app follows, from the sidebar to the transcript.
 Eleven built-in themes, fully custom palettes supported
 Background, surfaces, and accents all follow the theme
 Transcript display options: decide exactly what you see
Why we built Agent Deck
 AI coding agents are powerful – but running them from a terminal means context switching, lost transcripts, and manual git hygiene. Existing AI code editors bundle the agent inside the editor, forcing you into one workflow.
 We wanted something different: a dedicated cockpit that lives next to your editor, not inside it. A place where you author specialist agents per project, run them in parallel in isolated git worktrees, and merge the results when you're ready – without ever touching your working tree.
 Agent Deck is built on Pi CLI , the open-source agent harness. It is free, open source, and built by developers who use it daily.
How Agent Deck compares
 Agent Deck is the only native Mac app with a per-project skills library, GitHub issue integration, and per-project memory – features no other coding agent GUI offers.
 Capability Agent Deck T3 Code Synara Osaurus CLI alone
 Native Mac app ✓ SwiftUI Electron Electron ✓ Swift Terminal only
 Parallel worktree sessions ✓ Isolated branches One-at-a-time ✓ Isolated branches Not supported Manual setup
 Per-project skills library ✓ Cherry-pick from repos Not available Not available Not available Manual config
 GitHub issue → session ✓ Native board Not available Not available Not available Copy-paste
 Per-project memory ✓ Auto-accumulates Not available Not available Global only Not built-in
 Multi-agent support Pi CLI agents ✓ 4 agents ✓ 8+ agents ✓ Any model Single agent
 One-click PR ✓ With AI message ✓ Auto-generated ✓ Auto-generated Not available Manual
Frequently asked questions
 What makes Agent Deck different from AI code editors like Cursor? Agent Deck is not an editor – it is a dedicated cockpit for AI coding agents that sits next to your existing tools. You bring your own editor, API keys, and models through Pi. It specialises in parallel agent sessions in isolated git worktrees, per-project skill libraries, and launching sessions directly from GitHub issues.
 How does Agent Deck compare to T3 Code, Synara, or Osaurus? Agent Deck is the only native Mac app with a per-project skills library, GitHub issue integration, and per-project memory – features no other coding agent GUI offers. For a full side-by-side breakdown, see the comparison page .
 Is Agent Deck really free? Yes. Agent Deck is free and open source. You only pay for the AI model usage through your own API keys (Claude, OpenAI, or local models) – there is no Agent Deck subscription.
 What macOS versions are supported? Agent Deck requires macOS 26 (Tahoe) or later. It is a native Mac app built with SwiftUI and AppKit.
 Do I need to install anything besides Agent Deck? You need Pi CLI, the open-source agent harness that Agent Deck builds on. The install script sets up both in one command: curl -fsSL https://raw.githubusercontent.com/a-streetcoder/agent-deck/main/install.sh | bash .
 Can I use Agent Deck with my existing projects? Absolutely. Point Agent Deck at any local git repository and it will create isolated worktree branches for each session, never touching your working tree until you merge the results.
 How does per-project memory work? When enabled, Agent Deck stores preferences, decisions, and gotchas as plain Markdown files inside your project. They are recalled on demand – never automatically injected into every prompt – so your context window stays clean and relevant.
 How does Agent Deck compare to running agents directly from the terminal? The terminal gives you one session at a time with no visual transcript, no skill library, and manual git branch management. Agent Deck adds a color-coded streaming transcript, per-project skill curation, native GitHub issue integration, and automatic worktree isolation – all in a Mac-native interface. See the comparison table above for a side-by-side breakdown.
 Which AI models can I use with Agent Deck? Agent Deck works with any model supported by Pi CLI, including Claude (Anthropic), GPT (OpenAI), and local models via Ollama. You bring your own API keys – Agent Deck adds a per-session model picker, on-device drafting via the Foundation Model, and built-in Exa web search. There is no vendor lock-in.
 Try Agent Deck
 Free, open source, built for macOS 26 and later.
Download for macOS
GitHub 114
 Agent Deck The native Mac app for Pi CLI. Free and open source.
GitHub Report an issue Why Agent Deck Compare FAQ Download

## 关联链接

- https://raw.githubusercontent.com/a-streetcoder/agent-deck/main/install.sh

## 导航

- 项目页：[[10-项目/agentdeck.site_d1a8d86b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
