---
type: "corpus"
item_id: "b40c5f38d98667cc"
title: "Show HN: Canopy, a cross-platform DAG engine for agents CLI"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50371977"
project_url: "https://univerlab.org/canopy"
author: "JheisonMB"
published_at: "2026-11-04T21:43:41Z"
captured_at: "2026-11-05T11:21:45+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-05"
pub_day: "2026-11-04"
tags:
  - 语料
  - hn_show
  - author_JheisonMB
  - story_50371977
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Canopy, a cross-platform DAG engine for agents CLI

> [!info] 一句话导读
> univer se lab SCI · CLI

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50371977>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：JheisonMB　|　发布：2026-11-04T21:43:41Z
> 项目链接：<https://univerlab.org/canopy>
> 采集：2026-11-05T11:21:45+08:00　|　id：`b40c5f38d98667cc`

## 正文

Skip to content
univer se lab SCI · CLI · BIO
 Experiments Manifesto Status Collaborators GitHub sponsor
 ES Español UniverLab · open laboratory EXP-001
 Canopy Graphs Remote ⠿⠶⠦⠤ · ⠤⠦⠶⠿
 Canopy
 In a forest, the canopy is where the crowns touch — separate trees, one living layer.
 A Rust daemon and terminal UI with a graph engine at its core. Work enters as a spec and walks a graph you design: agent nodes on any harness, check nodes that run your real commands, ensembles that fan out to several models and keep a quorum, routers that pick the branch, and a resilience node that turns a quota death into a scheduled wake-up. Underneath: memory, scheduling and sync for every agent.
 AI agents → a graph engine above every harness → specs carried all the way to a commit
 Gated implement checks run your real commands — red routes the work back, never to you
Install Graph catalogue Remote Documentation → Star on GitHub ↗
 Install
 curl -fsSL https://install.univerlab.org/canopy | sh ⧉ ✓
 ██████ ██████ ████████ ██████ ████████ █████ ████ ███░░███ ░░░░░███ ░░███░░███ ███░░███░░███░░███░░███ ░███ ░███ ░░░ ███████ ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███ ███ ███░░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░░██████ ░░████████ ████ █████░░██████ ░███████ ░░███████ ░░░░░░ ░░░░░░░░ ░░░░ ░░░░░ ░░░░░░ ░███░░░ ░░░░░███ ░███ ███ ░███ █████ ░░██████ ░░░░░ ░░░░░░
EXP-001 · active · Sol 79 · release v3.1.1 · 2 weeks ago · DOI 10.5281/zenodo.23607434 · roadmap: · · Built with Canopy · Repository set up with ghScaff · Demo recorded with DemoStage · Commits checked by GitKit
 daemon · tui · graph engine · mcp
 Supported platforms Antigravity CLI
 BLACKBOX AI CLI
 Claude Code
 Cline CLI
 CodeBuddy Code
 Codex CLI
 Command Code
 Continue CLI
 Copilot CLI
 Cursor CLI
 Devin CLI
 Freebuff
 Gemini CLI
 Kilo Code CLI
 Kiro CLI
 MiMo Code CLI
 Vibe
 Muse Code
 opencode
 Qoder CLI
 Qwen Code
 UTIM
Genesis · 2026 · Sol 79 The one that started it all.
 It started as a folder of skills for work. Then I noticed what nobody was talking about: agent harnesses shipped a headless mode, just sitting there unused. I wired cron jobs to fire tasks through it — too much for a skill, and the models of the day choked on the instructions. So it became an MCP : task-trigger . It worked, but it ran blind in the background; only the agent ever saw what happened. Not enough. I killed it and built a TUI — then scheduling, memory, sync, identities, and a new name. Canopy . By then the twist was complete: Canopy was building Canopy, and everything else in this lab.
Fig. 1 Canopy — recorded with DemoStage
 The graph engine Graphs, not prompts
 Agent, check, gate and router nodes wired with pass, fail and always edges. A spec walks the graph from entry to commit; routing keys on real exit codes and verdicts, not on what a model claims.
Ensembles across harnesses
 Fan one step out to several models — parallel with a quorum, cascade to the next on failure, or round-robin across a crew — each member on whatever harness and model you pick.
Failure is a route
 Red gates send the work back with the output attached. A resilience node reads quota errors and schedules the graph to wake at the exact reset. Only a real verdict ever reaches you.
Remote Your sessions and graphs from your phone
 Encrypted end to end
 Sessions travel over WebRTC with end-to-end encryption: the relay only carries signalling, and your screen never passes through it.
Pairing in one command
 Run the command below: it prints a one-time code with its link and a terminal QR code. Scan it and the browser becomes a revocable device of the host.
Live graphs, shared
 Watch specs walk the graph in real time from your phone, and hand single-use invite codes to guests you trust.
canopy remote pair ⧉ ✓
 Open remote → Graph catalogue Pattern: Gated implement — one plate of the live catalogue Explore the catalogue → Patterns → Transparency →
 Autonomous graph Pattern: Ensemble · quorum + Gated implement 0 times it stopped
 It failed. It didn’t stop.
 01 One spec, three drafts
 Work enters as a spec — role, what, how. It fans out to three models on three harnesses, and a quorum keeps the consensus.
02 Implement from the consensus
 An implementer node picks up the agreed plan on your harness and starts writing.
03 It failed: cargo test, 2 red
 The check node runs your real commands. Red routes the token straight back to the implementer — it never comes to you.
04 Green — and a second opinion
 The retry passes the gates. A different harness reviews the diff against the spec before anything moves.
05 Committed. Pushed. Again.
 The branch is pushed and the run is remembered — the next spec is already walking the same graph.
Every node runs on the harness you pick, and the loop you just watched is the real engine doing its real job.
The runtime underneath Memory that persists
 Every run writes facts, patterns and decisions to a project-scoped knowledge graph. The next session — on any harness — reads them instead of rediscovering the codebase.
Queues and scheduling
 Specs live in ordered queues a graph works through in the background; graphs and agents also fire on cron schedules or file-change triggers, and hooks chain one graph into the next.
Multi-agent sync
 Agents declare their mission, report status and message each other, so several sessions can share one workspace without stepping on each other.
Cite How to cite
 Martinez Bolivar, J., & Solorzano, L. (2026). canopy (harness-canopy) (Version v3.1.1) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.23607434
 @software{canopy,
 author = {Martinez Bolivar, Jheison and Solorzano, Lina},
 title = {canopy (harness-canopy)},
 year = {2026},
 version = {v3.1.1},
 publisher = {Zenodo},
 doi = {10.5281/zenodo.23607434},
 url = {https://doi.org/10.5281/zenodo.23607434}
} ⧉ ✓
 FAQ FAQ
 What does Canopy actually do? Canopy runs AI coding work as graphs. A spec enters, agent nodes do the work on the harnesses you choose — Claude, Codex, Gemini, OpenCode or any terminal agent — check nodes run your real tests, ensembles get several models to agree, and failures route back automatically until the spec is committed. One daemon, all your agents, all your free tiers.
 How do I share work between Claude and Codex? Canopy gives each agent a shared knowledge graph and sync protocol. When Claude finishes a task, the facts and patterns it discovered are available to Codex in the next session. No manual context copying.
 Can I run AI agents on a schedule? Yes. Canopy fires agents on cron schedules or file-change triggers via a background daemon. Set the schedule once; the daemon watches the workspace and runs tasks automatically.
 How is Canopy different from just using Claude Code or Codex directly? Those are individual harnesses. Canopy is the layer that connects them — shared memory, background scheduling, and multi-agent coordination. You keep your agents; Canopy adds the infrastructure.
 ← EXP-008 Quorum EXP-002 TeXForge → Field notes
“We are the eyes of the universe opening after a long sleep. Our work is to create, care, and understand.”
Experiments Archive Manifesto Roadmap Collaborators API Privacy Terms GitHub
 This site: built with Canopy · repository set up with ghScaff · commits checked by GitKit
 UNIVERLAB ⠑⠇⠀⠥⠝⠊⠧⠑⠗⠎⠕⠀⠎⠑⠀⠇⠑⠑⠀⠙⠑⠀⠍⠥⠉⠓⠁⠎⠀⠋⠕⠗⠍⠁⠎
 branch: milky-way/main SCI · CLI · BIO commit HEAD (you)
Author: the universe
Date: now
observing itself
Canopy · Artifact conceived and forged at UniverLab
 no external tracking. theme preferences stay in your browser's local storage.

## 关联链接

- https://doi.org/10.5281/zenodo.23607434
- https://doi.org/10.5281/zenodo.23607434}
- https://install.univerlab.org/canopy

## 导航

- 项目页：[[10-项目/univerlab.org_265293df]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
