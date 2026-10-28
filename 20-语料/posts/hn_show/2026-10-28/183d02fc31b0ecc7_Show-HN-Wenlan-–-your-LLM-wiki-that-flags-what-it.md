---
type: "corpus"
item_id: "183d02fc31b0ecc7"
title: "Show HN: Wenlan – your LLM wiki that flags what it can't back up"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50263033"
project_url: "https://github.com/wenlan-app/wenlan"
author: "h164654156465"
published_at: "2026-10-27T17:50:33Z"
captured_at: "2026-10-28T09:39:16+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-28"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_h164654156465
  - story_50263033
  - show_hn
metrics: {"points": 2, "comments": 3, "engagement_velocity": 2}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:3d"
---

# Show HN: Wenlan – your LLM wiki that flags what it can't back up

> [!info] 一句话导读
> A living personal wiki. Wenlan turns your documents, notes, and AI chats into pages with links to their sources, and updates them as sources change without over…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50263033>
> 指标：点赞=2 · 评论=3 · engagement_velocity=2
> 作者：h164654156465　|　发布：2026-10-27T17:50:33Z
> 项目链接：<https://github.com/wenlan-app/wenlan>
> 采集：2026-10-28T09:39:16+08:00　|　id：`183d02fc31b0ecc7`

## 正文

# wenlan-app/wenlan

A living personal wiki. Wenlan turns your documents, notes, and AI chats into pages with links to their sources, and updates them as sources change without overwriting your edits. Claude Code, Codex and other AI tools can build on it.

- Stars: 80
- Forks: 8
- Watchers: 80
- Open issues: 13
- License: Apache License 2.0
- Homepage: https://wenlan.app
- Default branch: main
- Created: 2026-04-19T22:07:06Z

## Languages

- CSS
- HTML
- JavaScript
- NSIS
- Objective-C
- PowerShell
- Python
- Rust
- Shell
- Swift
- TypeScript

## Topics

- ai-memory
- claude
- claude-code
- claude-code-plugin
- codex
- knowledge-base
- knowledge-graph
- llm-wiki
- local-first
- mcp-server
- second-brain

## Top Contributors

- 7xuanlu (1050 contributions)
- github-actions[bot] (6 contributions)
- webbrain-one (1 contributions)

---

## README

Wenlan turns your documents, notes, and AI conversations into editable pages with links to their sources, so you and your AI tools can keep building on them.

As sources change, you can ask AI to update the pages or enable background updates. If you’ve edited a page, Wenlan proposes revisions for you to review instead of automatically overwriting your work.

 English | 简体中文 | 繁體中文 | Español

 Get started ·
 What is this? ·
 Capabilities ·
 Daily workflow ·
 Evaluation ·
 Learn more

https://github.com/user-attachments/assets/35f06749-00e5-484d-a9f4-5e462de8d11e

 The opening frame is a composed preview, not a native three-pane view. The rest shows the app in use, including pages and source citations.

## Get started

### 1. Download and open Wenlan

Download the app, then open it:

- **macOS (Apple Silicon):** open the `.dmg` and drag Wenlan to Applications. The app is signed and notarized.
- **Windows x64:** run the `-setup.exe`. It is not signed yet. If SmartScreen warns you, confirm you downloaded it from the official Releases page before choosing "More info" → "Run anyway".
- **Linux:** no desktop build yet; follow the setup guide to use Wenlan with your AI tools without the app.

First launch downloads a model for local search, so keep an internet connection until setup finishes. Download and privacy details.

### 2. Start with your own note

Choose **Open notes** to enter Wenlan, then create a page of your own. The welcome screen also offers a sample to explore first. You can start writing without importing material, connecting an AI tool, or setting up an AI model.

### 3. Bring in sources when you want

You can import notes or ChatGPT / Claude conversation exports whenever you are ready. Import is optional; you can begin with a page of your own.

### 4. Connect AI tools when you want AI help

Connect Claude Code, Codex, or other supported AI tools when you want them to use the same knowledge. A connected AI can write pages without an additional local language model.

 Need help connecting? Ask your AI

Restart your AI tool if prompted. For help with setup, paste this into Claude Code, Codex, or another tool that can follow a setup guide:

```text
Connect this AI tool to Wenlan by following:
https://raw.githubusercontent.com/wenlan-app/wenlan/main/docs/setup-with-ai.md

Reuse my existing Wenlan installation if available.
Set up only this AI tool, then check that it can save and find a test memory.
```

To organize a topic with a connected AI, open a work conversation worth keeping and ask:

> Turn the conclusions, reasoning, and sources about [topic] in this conversation into a Wenlan page with source citations.

You can also ask your AI to organize a topic from material you imported into a page.

When it's ready, open the new page in Wenlan, click a citation to check its source, and add your own thoughts. Next time you work on that topic, ask your AI to read this page before continuing.

Background organization and automatic updates are optional and need a configured model. For terminal installation, other platforms, and updates, see the setup guide.

Need help? Setup guide · Report a problem. Issues are public: redact secrets, credentials, access tokens, identifiers, private or personal content from anything you share, including logs.

## Your wiki, for you and your AI

- **Turn scattered material into connected topics.** Bring documents, notes, and AI conversations together in linked pages, with citations you can open and check.
- **Read it yourself. Use it with your AI.** Read and edit your pages, or ask Claude Code or Codex to use them for your next task.
- **Maintain knowledge without starting over.** Track source changes, update related pages, and keep their history. AI proposes revisions to pages you've edited for you to review.

Your pages are local Markdown files you can read, edit, and take with you.

The illustration shows a reusable working rule, not customer results or an automated page-generation test. How sources, memories, and pages work together.

### Follow the connections behind a page

The Agent Loop example connects a retry rule, a lesson from a UI review, and an acceptance checklist you can reuse.

Follow a page to related concepts and evidence. How graph and search work.

### Knowledge changes. History stays.

New experience improves your notes without hiding earlier decisions. This example replaces “tests passed, so the UI is done” with “check tests and the desktop and mobile views,” keeping the reason and evidence for the change.

Review applies to AI updates; direct file edits and forced regeneration follow different rules. Updates, review, and local files.

### Already using Obsidian with AI plugins?

You can use Copilot for AI-assisted reading and editing, Smart Connections to find related notes, and Obsidian Git to keep version history. That gives you flexibility, but choosing how the plugins work together, when to organize new material, and how to update older pages is still a workflow you arrange.

Wenlan connects topic-page creation, source-change tracking, page updates, and revision history in one workflow, saving you the work of assembling and maintaining those steps yourself. You can read the resulting knowledge directly or let Claude Code, Codex, and other tools build on it.

Ask your connected AI to update a page, or configure a model to enable background updates. When AI updates a page you've edited, Wenlan proposes a revision for you to review.

Connect your existing Obsidian vault as a read-only source without moving your notes. Wenlan does not modify the vault or sync changes back to it.

## Capabilities

### Bring your material in

- **Keep useful AI conversations:** Import ChatGPT or Claude export ZIPs without duplicating conversations already imported.
- **Bring your existing notes:** Import Markdown, text files, or text-extractable PDFs, by file or folder; connect an Obsidian vault as a source. Scanned PDFs need text extraction first.
- **Quick Capture:** Save a thought or decision directly in the desktop app without opening an AI chat.
- **Capture decisions with your AI:** Ask your AI tool to save decisions, lessons, corrections, preferences, and facts, with their sources and what they replace.
- **Bring in another wiki:** Import an external OKF wiki through the CLI or API, preserving source references and links. Reimporting Wenlan's own OKF exports is not supported.

### Explore your personal wiki

- **Editable, source-linked Pages:** Turn related documents and Memories into Markdown Pages with citations and links to other Pages.
- **Cards or lists:** Browse Pages, Entities, and Spaces in the view that suits you.
- **Knowledge graph:** Explore connections between people, projects, claims, and the Memories supporting them.

### Use it with your AI tools

- **Pick up in another AI tool:** Connected Claude Code, Codex, and other MCP clients can use the same local Pages and Memories as the desktop app and CLI.
- **Search by words and meaning:** Combine exact matches with local semantic search; graph connections can add relevant context.
- **Optional deeper search:** Search Pages and finer-grained Memories, with optional reranking to refine results.
- **Keep projects separate:** Use Spaces to choose which work, personal, client, or repository knowledge your AI searches.
- **Web access (experimental):** Connect a supported web AI client to your whole library, or to one Space you choose, while your computer is online. Queries and results pass through a relay; see how access works and its privacy limits.
- **Connect your own tools:** Send prepared text, webpage content, or Memories through the local HTTP API. It accepts content, not URLs to fetch.

### Keep knowledge current

Optional background organization and Page updates need a configured model.

- **Incremental sync:** File and folder Sources track changes in the background. Obsidian vaults stay read-only and resync on demand.
- **Organize saved knowledge:** A configured model can add types, structured details, relevant dates, tags, search cues, and graph links to Memories.
- **Updates backed by sources:** Automatic refresh rejects drafts with insufficient citations. AI-generated Pages can update; changes to Pages you have edited become review proposals.
- **Review where judgment matters:** Review protected conflicts, Page revisions, entity merges, and new vocabulary.
- **See what is happening:** Check progress and blockers in Activity. Configured sync, Steep (background enrichment), and eligible Page updates can continue after the app window closes while the local service runs.

### Keep ownership and control

- **Local, inspectable knowledge:** Keep Markdown Pages, citations, revisions, and Obsidian exports; Memories and graph data live in local libSQL.
- **Take your wiki with you:** Export eligible Pages across Spaces as an OKF v0.2 wiki from Settings or the CLI. This is a wiki export, not a full database backup.
- **Model choice:** Base retrieval stays local. Steep, the optional background enrichment and synthesis, can use on-device Qwen, a local endpoint, or a cloud model; remote providers receive the content needed for their tasks.
- **Health checks and reviewed repairs:** Doctor and lint report problems without rewriting knowledge. For supported findings, the app lets you preview and explicitly apply a repair, then verify it.

**Start with a note you want to keep.** Get started. Star this repo if you'd like to come back and try it later.

## Daily workflow

Once your AI tool is connected, you can ask in plain language:

With the Wenlan plugin installed, you can also use the slash commands below.

### Before starting a task

> Find what I've saved in Wenlan about [topic], including earlier decisions and their sources.

Shortcut: `/recall [topic]`

### When you reach a useful conclusion

> Save this decision and why we made it in Wenlan, with its sources.

Shortcut: `/capture [decision, reasons, and sources]`

### When a topic deserves a page

> Create or update a Wenlan page on [topic] from the material we've saved. Keep the citations.

To organize saved knowledge into pages: `/distill`

Open the page in Wenlan to read, edit, and check its sources. Next time, ask your AI to use it for your next task.

### When you wrap up

> Save this session's progress, decisions, and open questions in Wenlan so we can pick up next time.

Shortcut: `/handoff`

 Plugin commands and maintenance

- **Read the project summary:** `/brief [topic]` reads the current Space's project summary; an optional topic adds related context from that Space.
- **Check and review:** `/lint` checks knowledge health; `/curate` reviews pending captures or revisions.

These shortcuts are available through the Wenlan plugins. Other connected clients use the equivalent MCP tools. Optional background organization and Page updates need a configured model.

Full command reference.

CLI offline writes and replay.

### Models and privacy

Use your connected AI to write pages without installing an additional local language model. Background organization and automatic updates are optional and need a configured model.

- **Search stays local.** The search model downloads at first launch and runs on your machine, without an API key.
- **Connected AI can receive your knowledge.** A cloud AI client can send retrieved content to its provider. Choosing a cloud model for background organization also sends the material needed for that task. Local storage does not make those interactions local.
- **Usage statistics are off by default.** If you opt in, Wenlan sends limited operation counts, version, and platform, not your knowledge content or an installation ID. Details.

See network and privacy details for downloads, update checks, remote images, and optional remote access.

Model choices and configuration.

### Your data and uninstall

Your pages and session notes are Markdown files; memories and the graph live in a local database. You can keep your knowledge when you uninstall the app.

File locations, backup, and removal.

## Evaluation

This is a retrieval-only snapshot, not a claim about end-to-end answer quality. Method, environment receipts, and the update workflow live in docs/eval.

| Benchmark | Recall@5 | MRR | NDCG@10 |
|---|---:|---:|---:|
| LME_Oracle (500 Q) | 93.6% | 0.857 | 0.883 |
| LME_S (deep, 90 Q) | 87.7% | 0.815 | 0.822 |

## Learn more

More detailed documentation, concepts, and comparisons:

### Docs

- Get started: install and verify the first local loop.
- Daily workflow: brief, capture, recall, handoff, distill, lint, and curate.
- MCP clients: connect Claude Code, Codex, Cursor, Claude Desktop, and other clients.

### Workflow guides

- Build your first LLM Wiki: work through a three-source example, check its citations, and review what changes when a source is updated.
- Build a client project knowledge base for consulting
- Build an investment research knowledge base
- Build a product research knowledge base before writing a PRD
- Build an SRE incident knowledge base
- Build a business metric definition knowledge base: turn approved KPI specifications into a source-backed data dictionary with formula text, grain, exclusions, owners, revisions, and review state.

### Concepts

- Why a living wiki, not just AI memory: the problem and product model in depth.
- MCP memory server: how Wenlan exposes knowledge across AI tools.
- Local-first AI memory: data, privacy, and control.
- Markdown and local index: storage, retrieval, and ownership.
- AI agent handoff loop: carrying work cleanly into the next session.
- Research knowledge base from papers: build an inspectable literature matrix and source-backed synthesis from papers you already have.

### Comparisons

- Wenlan vs Basic Memory
- Wenlan vs claude-mem
- Wenlan vs Superlocal Memory

## Contributing

Bug fixes, eval cases, docs, and features are welcome. Installing Wenlan does not require building from source. For local development, run these commands from this repository's root:

```bash
# daemon crates (default-members — the desktop app is not compiled)
cargo build
cargo test

# desktop app (Cargo target and root-level frontend tooling)
pnpm install
pnpm dev:all
pnpm build:all
```

`pnpm dev:all` is the supported development entry point for the desktop app. It keeps development ports, data, process ownership, app identity, MCP sockets, and Remote Access state separate from the installed production runtime; a debug app started without that isolation refuses to run. See this repository's AGENTS.md and CONTRIBUTING.md, plus the in-tree app/AGENTS.md, for the complete development workflow. Security reports: SECURITY.md. Privacy policy: PRIVACY.md. Please also read the Code of Conduct.

## Code signing policy

macOS desktop releases are Developer ID signed and notarized. Windows installers are not signed yet.

Releases are built from tagged commits by this repository's release workflow on GitHub-hosted runners. Maintainers must use multi-factor authentication on GitHub.

Platform signing details · Privacy policy.

## License

Wenlan uses two licenses, one per part of the repository.

- **Apache-2.0** (`LICENSE`) covers the local runtime, CLI, MCP server, shared types, and the Claude Code and Codex plugin files. Build on these freely.
- **AGPL-3.0-only** (`app/LICENSE`) covers the desktop app: the `app/` crate and the React frontend it ships. If you run a modified version of the app as a network service, the AGPL asks you to offer that modified source to its users.

The split is deliberate. Apache-2.0 code may be used inside an AGPL-3.0 program, so the desktop app builds on the runtime without either license being violated.

## Lineage and peers

Wenlan (文瀾) takes its name from 文瀾閣, an imperial library that held 四庫全書 as part of one of China's largest book collections.

Wenlan's llm-wiki v2 model is its own product direction, informed by the LLM-wiki and agent-memory lineages:

- Karpathy's LLM-wiki note established the raw-source-to-maintained-wiki pattern.
- Rohitg00's LLM Wiki v2 proposal extends that pattern with memory lifecycle, confidence, graph, and retrieval mechanisms. agentmemory is its concrete agent-memory implementation.
- nashsu/llm_wiki is a full desktop implementation of the document-centered LLM-wiki pattern.
- basic-memory, obsidian-mind, mcp-memory-service, Memoria, and OpenMemory explore adjacent local knowledge and agent-memory shapes.

# sanmak/specops

## 评论（3/3）

> **h164654156465** · 2026-10-27T18:02:29.000Z　
> Hi, this is Wenlan author. This is not another llm Wiki and here's why. We all run into indexing problem takes like an hour or so in the first install. And there's a lot of plugins that you need to install in your obsidian vault. And last but not least, you couldn't trust the pages AI wrote.That's why I built Wenlan, it's your personal wiki desktop app that compiles your notes, code, AI chat files and everything into once unified place, where statement in in the pages get checked and fixed if they are backed up. When one source changes and related pages get updated and we have the you don't need to build that upkeep to maintain the process. No extra plugins or setups. AI wrote with your knowledges and wenlan protect your pages that you've built. It will only ask for your approval when if they can't figure out it's contradictory or out of their ability to decide. Usually this is automatic when safe to do so.It's it's a free, open source and local first. On MacOS and Windows desktop app. Linux with. the the daemon and CLI.Looking forward to honest feedbacks and any improvements suggested. And hopefully help you get the most of LLM wiki that actually work and can be trust.

---

> **TristanX** · 2026-10-27T18:19:05.000Z　
> Can I sync it with my Obsidian?

---

> **h164654156465** · 2026-10-27T18:28:53.000Z　
> It can sync to to obsidian vault and without you really migrating over to Wenlan. It helps you organize your markdown files automatically what's in Obsidian. I plan to have a plug-in in obsidian to make this more streamlined experience but now the sync is working.

## 关联链接

- https://github.com/user-attachments/assets/35f06749-00e5-484d-a9f4-5e462de8d11e
- https://raw.githubusercontent.com/wenlan-app/wenlan/main/docs/setup-with-ai.md
- https://wenlan.app

## 导航

- 项目页：[[10-项目/github.com_aba1842b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
