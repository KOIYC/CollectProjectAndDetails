---
type: "project"
title: "Show HN: Yengi, a local-first AIdevelopment environment for coding,Blender/Unity"
project_url: "https://github.com/mdaiWorks/yengi"
first_seen: "2026-09-29T09:42:55+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_mdaiWorks
  - story_49879268
  - show_hn
lang: "en"
---

# Show HN: Yengi, a local-first AIdevelopment environment for coding,Blender/Unity

> [!info] 一句话导读
> I've been working on Yengi for several months. I am a teacher, not a professional software developer. My path here started with Microsoft Small Basic, Scratch, …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/mdaiWorks/yengi>
> 首次收录：2026-09-29T09:42:55+08:00
> 来源渠道：HN Show HN
> 标签：author_mdaiWorks, story_49879268, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-29T09:42:55+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-29/ded5b97c1e75e522_Show-HN-Yengi,-a-local-first-AIdevelopment-environ]] |

## 摘要正文

I've been working on Yengi for several months. I am a teacher, not a professional software developer. My path here started with Microsoft Small Basic, Scratch, and MIT App Inventor, which I used to teach children.I originally started it for a simple reason: I was using VS Code + Copilot, Trae, Cursor and Google Antigravity, and I kept running into usage limits and provider-specific workflows.I wanted something where I could choose my own model or API, including local models running through Ollama, and build without being tied to one provider.It grew considerably beyond that original idea.Yengi is a .NET 10 / WPF desktop application with:* Agent and tool system for files, terminal, Git, builds and tests * RAG and LSP integration * Verification loops with checkpoints and rollback * 30+ agent tools * Support for local models and external APIs * A custom 1.5B router model that I fine-tuned on thousands of examples of Yengi-specific agent decisions * 200+ automated testsIt also has three additional modes besides the coding environment:*Blender:* Yengi can communicate with Blender, generate `bpy` scripts, keep conversational scene context, and optionally inspect Blender viewport screensh…
