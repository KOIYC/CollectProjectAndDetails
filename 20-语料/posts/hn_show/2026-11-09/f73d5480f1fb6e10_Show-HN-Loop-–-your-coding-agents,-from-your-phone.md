---
type: "corpus"
item_id: "f73d5480f1fb6e10"
title: "Show HN: Loop – your coding agents, from your phone"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50413968"
project_url: "https://github.com/j-asefa/loop"
author: "jamesasefa"
published_at: "2026-11-08T15:11:43Z"
captured_at: "2026-11-09T09:39:29+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-09"
pub_day: "2026-11-08"
tags:
  - 语料
  - hn_show
  - author_jamesasefa
  - story_50413968
  - show_hn
metrics: {"points": 2, "comments": 7, "engagement_velocity": 2}
comments_count: 7
comments_total: 7
discovered_via: "hn:show_hn:3d"
---

# Show HN: Loop – your coding agents, from your phone

> [!info] 一句话导读
> Loop is a mobile-first companion workspace for the coding harnesses you already run. It aggregates results from your harnesses into a continuous feed that is ea…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50413968>
> 指标：点赞=2 · 评论=7 · engagement_velocity=2
> 作者：jamesasefa　|　发布：2026-11-08T15:11:43Z
> 项目链接：<https://github.com/j-asefa/loop>
> 采集：2026-11-09T09:39:29+08:00　|　id：`f73d5480f1fb6e10`

## 正文

Loop is a mobile-first companion workspace for the coding harnesses you already run. It aggregates results from your harnesses into a continuous feed that is easy to navigate and organize from your phone. I spent several months holding my newborn in one hand and trying to talk to agents one-handed on my phone. Every mobile UI is still based around chat, and it doesn’t scale on mobile, let alone one-handed!So I built Loop: a feed of the work your coding agents do. It’s built around agent results, not chats. You can scroll your history, get notified, save outputs, search and return to conversations later. The goal is to make interacting with agents via your phone feel familiar and intuitive based on the mobile UX we’ve all come to expect.Loop runs on your own computer — no account, no server, no app store — and pairs with your phone with one QR scan. It wraps the agents you already use (Codex, Claude Code, Pi, OpenCode, Antigravity, Muse Code, Grok Build, or any ACP agent), each keeping its own context, tools, sign-in and billing — local models through Pi or OpenCode work too.Apache-2.0, TypeScript, SQLite. I'd love feedback from anyone else who builds from a phone.

## 评论（7/7）

> **loveTech** · 2026-11-08T15:22:31.000Z　
> Congrats for the launch! Create a demo video to help people understand what it is and how it works at Fluxcut(fluxcut.dev): https://www.youtube.com/watch?v=JVBTCoruJ8o

---

> **Mangrove007** · 2026-11-08T16:19:29.000Z　
> Hi jamesasefa,Sometimes doing something completely unrelated can bring about a moment of 'I can make this easier for myself' and from it is born an idea that so many others will benefit from in the same way you have. Congrats on that!I can relate to the frustration of chat-based mobile UIs. I do a huge amount of my building and shipping directly from my phone, constantly switching between mobile browser tabs to write prompts, check PR diffs and monitor deployments can become cumbersome when on the move. A solution like Loop would be extremely helpful to someone like me.Two questions for you, from someone who relies on cloud-based workflows (I use GitHub + Jules + Cloudflare currently) because I'm not a huge fan of being tied to my desk. I'll be replacing Jules with Antigravity in the coming days which I see is on your supported list.1. Since Loop runs locally on your computer and pairs via QR code, how do you handle remote access when you leave your home/office or is remote access not in use at the moment?2. Is there a path to hook in cloud-hosted agents or is it built strictly for wrapping local CLI processes?

---

> **jamesasefa** · 2026-11-08T19:15:58.000Z　
> Should have also mentioned it supports teams and inter-agent messaging across harnesses!A manager agent delegates to worker agents. Presets cover Review code changes, Ask an LLM council, Build a feature and Investigate a bug, and you can build a custom team from existing agents across Claude, Codex, Gemini etc

---

> **seanmcdirmid** · 2026-11-08T19:29:44.000Z　
> Antigravity has this feature built in right? It’s super useful to monitor and interact with my agents on my iPhone. Getting remote to work for DSH web is a pain in comparison, and it only works on my local network, unlike antigravity.Anyways, this is a great feature that everyone should have access to, so I think this product is timely.

---

> **jamesasefa** · 2026-11-08T18:11:26.000Z　
> Thanks for the kind words Mangrove007!1. Loop uses cloudflare quick tunnels (https://try.cloudflare.com/) to create a tunnel to your local machine. So you can work remotely from your machine from anywhere. I was on another continent recently and continued working remotely. Caveat that your machine has to remain awake. More info in the docs.2. At the moment it’s only built for wrapping harness CLIs running on a machine. I haven’t put much thought into integrating cloud hosted agents. Unfortunately Anthropic/OpenAI won’t let you use their cloud instances unless you’re using their apps :(

---

> **jamesasefa** · 2026-11-08T20:51:28.000Z　
> Give it a try! Most harnesses have some remote control feature, but they’re all chat based and single-harness

---

> **seanmcdirmid** · 2026-11-09T01:23:41.000Z　
> I will definitely take a look. I have both DSH web and antigravity on my iPad right now while I’m stuck in bed, driving my computer downstairs. It’s not clear what interface I would need other than chat though, I haven’t really thought about it yet so I’m open minded about the possibilities.

## 导航

- 项目页：[[10-项目/github.com_7563e72c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
