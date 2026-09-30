---
type: "corpus"
item_id: "87948e388e073aaf"
title: "Show HN: Moching – AI desktop agent with 219 built-in tools (Rust)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49903470"
project_url: "https://github.com/moching-ai-dev/moching"
author: "moching_ai_dev"
published_at: "2026-09-30T02:00:13Z"
captured_at: "2026-09-30T18:57:07+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-30"
pub_day: "2026-09-30"
tags:
  - 语料
  - hn_show
  - author_moching_ai_dev
  - story_49903470
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Moching – AI desktop agent with 219 built-in tools (Rust)

> [!info] 一句话导读
> moching-ai-dev/moching

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49903470>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：moching_ai_dev　|　发布：2026-09-30T02:00:13Z
> 项目链接：<https://github.com/moching-ai-dev/moching>
> 采集：2026-09-30T18:57:07+08:00　|　id：`87948e388e073aaf`

## 正文

# moching-ai-dev/moching

Not a chatbot. Not a coding assistant. A digital operator that controls your entire PC — 219 tools, screen perception, HID control, browser automation, Office suite, AI media. One sentence in, finished work out.

- Stars: 9
- Forks: 0
- Watchers: 9
- Open issues: 1
- License: Other
- Homepage: https://mochingcode.com
- Default branch: main
- Created: 2026-07-25T13:51:00Z

## Topics

- ai-agent
- ai-assistant
- ai-tools
- automation
- browser-automation
- computer-use
- desktop-agent
- desktop-automation
- gui-agent
- llm
- macos
- mcp
- office-automation
- playwright
- productivity
- python
- rust
- screen-control
- screen-understanding
- windows

## Top Contributors

- moching-ai-dev (28 contributions)

---

## README

 English · 简体中文

# 🏔️ Moching — AI Agent for Your Entire PC

 Your browser does not support the video tag.

 ▲ Moching in action — 25s product demo

 ⭐ Star us on GitHub — every star helps Moching reach more developers

   

### Not a Coding Assistant. Not a Chatbot. A Digital Operator.

Most AI tools live inside a browser tab. **Moching lives on your desktop** — it sees your screen, moves your mouse, opens your apps, and gets work done while you watch.

**System Requirements:** Windows 10+ (x64) · macOS 12+ (Apple Silicon) · 4GB RAM · Any OpenAI-compatible API key

---

## 🧠 Capability Matrix — 219 Native Tools × 12 Domains

| Domain | Tools | What It Does |
|---|---|---|
| 🖥️ **PC System Control** | 57 | Process / Service / Registry / Window / Network / WiFi / Disk / Task Scheduler / Software Mgmt / Archive / Notifications |
| 🌐 **Browser Automation** | 57 | Full Playwright Suite: Page Ops, Cookie/Storage, Network Intercept, JS Execution, PDF Export, Device Emulation, Geolocation |
| 📄 **Office Suite** | 23 | Word / Excel / PPT / PDF — Full CRUD, Charts, Form Fill, Template Replace, PDF Merge/Split/Watermark |
| 🎬 **Media Processing** | 10 | Transcode / Trim / Merge / Extract / Thumbnail / Volume / Subtitle Extraction |
| 🎨 **AI Generation** | 6 | Text-to-Image (FLUX/SD/DALL-E/MJ), Background Removal, Resize, Watermark, TTS Synthesis, Quality Check |
| 📹 **Video Generation** | 4 | Seedance 2.0 Text-to-Video, Image-to-Video, Video Enhance, Subtitle Extraction |
| 👁️ **Screen Perception** | 12 | Real-time Capture, UI Tree, Focused Element, Element Finder, Continuous Monitor, AI Visual Analysis |
| 🖱️ **HID Control** | 15 | Mouse Move/Click/Right/Double/Drag/Scroll, Keyboard Type/Combo/Press, App Launch, Clipboard Input |
| 🧠 **Memory & Knowledge** | 10 | L1 Short-term (Full-text / Vector / Hybrid RRF), L3 Persistent KB, PDF/Word/Excel Ingestion + Auto-vectorization |
| 🔧 **LSP Code Intelligence** | 5 | Workspace Symbol Search, Diagnostics, Find References, Go-to-Definition, Hover Type Info |
| ⚙️ **Core Utilities** | 18 | File Read/Write/Search/Replace/Diff, Command Execution, Clipboard, AST/tsc/cargo Validation |
| 🧩 **Skill System** | 2 | Skill Store (30+ Official Skills), Skill Execution Engine |

---

## ⚔️ Competitive Landscape

| Capability | 🏔️ **Moching** | GitHub Copilot | Cursor | Qoder |
|---|---|---|---|---|
| **Positioning** | Desktop AI Agent | IDE Code Completion | AI Code Editor | CLI Coding Tool |
| **Desktop HID Control** | ✅ Full + Screen Perception | ❌ | ❌ | ❌ |
| **System-Level Control** | ✅ Process/Service/Registry/Net | ❌ | ❌ | ❌ |
| **Browser Automation** | ✅ Playwright (57 tools) | ❌ | Basic | Limited |
| **Office Document Suite** | ✅ Word/Excel/PPT/PDF | ❌ | ❌ | ❌ |
| **Media & Video Generation** | ✅ Full Pipeline + AI Video | ❌ | ❌ | ❌ |
| **AI Image / TTS** | ✅ Multi-provider | ❌ | ❌ | ❌ |
| **Code LSP Intelligence** | ✅ Symbol/Diag/Ref/Def | ✅ Built-in | ✅ Strong | ✅ |
| **Code Editing** | ✅ Precision Replace + Diff | ✅ Completion | ✅✅ Best | ✅ |
| **Terminal Execution** | ✅ No Whitelist | ✅ Limited | ✅ | ✅ Strong |
| **Memory / Knowledge Base** | ✅ L1 + L3 + RAG Ingestion | ❌ | ✅ Code Index | Limited |
| **Screen Visual Understanding** | ✅ Real-time + AI + UI Tree | ❌ | ❌ | ❌ |
| **Extensible Skills** | ✅ Skill Store 30+ | Plugins | Plugins (MCP) | Plugins |
| **Autonomous Execution Loop** | ✅ See → Act → Verify | ❌ Advisory | ⚠️ Semi-auto | ⚠️ Semi-auto |

---

## 🎯 The Moching Difference

> **Copilot writes code for you. Cursor edits code for you.**
>
> **Moching operates your entire computer for you.**

The core moat isn't excelling at any single task — it's closing the complete human-computer loop:

```
👀 See Screen  →  🧠 Understand  →  🖱️ Take Action  →  ✅ Verify Result
```

This is the **Perceive → Decide → Execute → Verify** cycle that no other product does — because their product positioning doesn't even try.

---

## 📐 Architecture at a Glance

```
┌──────────────────────────────────────────────┐
│           Rust Core (moching.exe)            │
│  ┌──────────┐ ┌─────────┐ ┌──────────────┐   │
│  │IPC Engine│ │HID Input│ │Screen Capture│   │
│  └────┬─────┘ └─────────┘ └──────────────┘   │
│       │      Native IPC Bridge               │
│  ┌────▼──────────────────────────────────┐   │
│  │       Python Runtime (Embedded)       │   │
│  │  ┌────────┐ ┌────────┐ ┌───────────┐  │   │
│  │  │Agent   │ │Tools   │ │Knowledge  │  │   │
│  │  │Engine  │ │(219)   │ │Store      │  │   │
│  │  └────────┘ └────────┘ └───────────┘  │   │
│  └───────────────────────────────────────┘   │
└──────────────────────────────────────────────┘
```

**Rust for speed. Python for flexibility. 219 tools for capability.**

---

## 🚀 Quick Start

| Step | Action |
|:----:|--------|
| 1 | **Download** the installer for your platform |
| 2 | **Install** and launch Moching |
| 3 | **Bring your own key** — OpenAI, Claude, Gemini, or any OpenAI-compatible endpoint |
| 4 | **Type what you need done.** Watch it work. |

**No subscription. Pay as you go. From $5.**

---

## 📥 Download — v26.9.16-1

| Platform | Link | Size |
|----------|------|:----:|
| Windows x64 | GitHub Releases | 375 MB |
| macOS (Apple Silicon) | GitHub Releases | 794 MB |
| All Platforms | HuggingFace Mirror | — |

 🔐 Full SHA256 checksums

```
Windows: 994d21431e51ecdf8b04fdf53ca4bcba5ec0625e144f9b5c31015e71a09af065
macOS:   9d0c97d0a5a119c3d0f7fa0062f81e911734c737018d27d1f7e93d6b4f94816d
```

---

## 🎁 Referral Program — Refer & Earn

**Refer a friend — you both get 500,000 Credits gifted.**

1. Enter your username at ref.mochingcode.com
2. Get your unique referral link
3. Share it → Friend signs up & activates → **You both get 500,000 Credits**

👉 **Join the Referral Program →**

*The only AI agent that pays YOU to share it.*

---

## 💬 Support

| Channel | Link |
|---------|------|
| Email | noreply@mochingcode.com |
| Bug Reports | GitHub Issues |
| Website | mochingcode.com |

---

## 💎 Why We Built This

We were tired of AI tools that *talk* about doing things but can't actually *do* them.

Every other AI asks: *"What can I help you write?"*

Moching asks: ***"What can I do for you?"***

---

## 📋 Changelog

| Date | Version | Highlights |
|------|---------|------------|
| 2026-09-14 | v26.9.16-1 | Latest release. Windows 26.9.16-1 · macOS 26.9.16. |
| 2026-08-19 | v26.8.19-1 | First public GitHub release. 219 tools. Windows + macOS. |

---

**100% Independently Developed · Not a Wrapper · Not a Mod**

**🏔️ Moching** — *Your computer just got a brain.*

© 2026 Moching. Proprietary. All Rights Reserved.

Website · HuggingFace · Referral

⭐ Star this repo — it takes 1 second and helps more developers discover Moching.

# spenmcke/compress

## 关联链接

- https://mochingcode.com

## 导航

- 项目页：[[10-项目/github.com_2bd886ef]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
