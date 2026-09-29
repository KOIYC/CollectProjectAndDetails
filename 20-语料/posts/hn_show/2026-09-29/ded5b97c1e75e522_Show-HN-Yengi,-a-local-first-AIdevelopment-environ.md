---
type: "corpus"
item_id: "ded5b97c1e75e522"
title: "Show HN: Yengi, a local-first AIdevelopment environment for coding,Blender/Unity"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49879268"
project_url: "https://github.com/mdaiWorks/yengi"
author: "mdaiWorks"
published_at: "2026-09-28T15:08:28Z"
captured_at: "2026-09-29T09:42:55+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-29"
pub_day: "2026-09-28"
tags:
  - 语料
  - hn_show
  - author_mdaiWorks
  - story_49879268
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Yengi, a local-first AIdevelopment environment for coding,Blender/Unity

> [!info] 一句话导读
> I've been working on Yengi for several months. I am a teacher, not a professional software developer. My path here started with Microsoft Small Basic, Scratch, …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49879268>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：mdaiWorks　|　发布：2026-09-28T15:08:28Z
> 项目链接：<https://github.com/mdaiWorks/yengi>
> 采集：2026-09-29T09:42:55+08:00　|　id：`ded5b97c1e75e522`

## 正文

I've been working on Yengi for several months. I am a teacher, not a professional software developer. My path here started with Microsoft Small Basic, Scratch, and MIT App Inventor, which I used to teach children.I originally started it for a simple reason: I was using VS Code + Copilot, Trae, Cursor and Google Antigravity, and I kept running into usage limits and provider-specific workflows.I wanted something where I could choose my own model or API, including local models running through Ollama, and build without being tied to one provider.It grew considerably beyond that original idea.Yengi is a .NET 10 / WPF desktop application with:* Agent and tool system for files, terminal, Git, builds and tests
* RAG and LSP integration
* Verification loops with checkpoints and rollback
* 30+ agent tools
* Support for local models and external APIs
* A custom 1.5B router model that I fine-tuned on thousands of examples of Yengi-specific agent decisions
* 200+ automated testsIt also has three additional modes besides the coding environment:*Blender:* Yengi can communicate with Blender, generate `bpy` scripts, keep conversational scene context, and optionally inspect Blender viewport screenshots through a multimodal model. I also added an optional prompt-engineering layer. For example, "create a low-poly tree" is expanded into a more detailed 3D-oriented instruction before being sent to the model. A follow-up such as "add five red apples to this tree" can modify the existing scene rather than starting from scratch.*Unity:* Yengi can work with Unity projects, generate C# components and interact with the Unity Editor.*Image generation:* Images can be generated from the development environment and saved directly into the project.The unusual part is how I built it.I used AI coding tools heavily, particularly Google Antigravity and GitHub Copilot. I didn't manually type the majority of the C# code.My role was primarily architecture, agent behavior, security boundaries, verification and rollback logic, router training, testing, debugging AI-generated changes, and integrating the different systems.I'm still trying to figure out how much of this approach is genuinely useful and how much is me having fun building increasingly complicated things.The project is free and open source under AGPL-3.0:https://github.com/mdaiWorks/yengiI'd especially like feedback from people working with .NET/C#, coding agents, local models, Blender or Unity.In particular, I'm curious about:* Is a small fine-tuned local router actually useful for this kind of agent?
* Does the verification/rollback architecture make sense?
* Are the Blender/Unity integrations useful beyond being demos?
* If you were building this, what would you simplify or change?I'm not trying to claim that this replaces VS Code or Cursor. I'm interested in whether this particular approach is useful at all, and what I should change next.

## 关联链接

- https://github.com/mdaiWorks/yengiI

## 导航

- 项目页：[[10-项目/github.com_5667f90b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
