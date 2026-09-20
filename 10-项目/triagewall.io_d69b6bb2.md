---
type: "project"
title: "Show HN: I found a prompt injection in my own IDs triage tool – what stopped it"
project_url: "https://triagewall.io/posts/prompt-injection-phase-2"
first_seen: "2026-09-21T02:52:45+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_aaronphifer
  - story_48345230
  - show_hn
lang: "en"
---

# Show HN: I found a prompt injection in my own IDs triage tool – what stopped it

> [!info] 一句话导读
> I Found a Prompt Injection in My Own IDS Triage Tool. Here's What Actually Stopped It.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://triagewall.io/posts/prompt-injection-phase-2>
> 首次收录：2026-09-21T02:52:45+08:00
> 来源渠道：HN Show HN
> 标签：author_aaronphifer, story_48345230, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:27:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/6c62acee011ac685_Show-HN-I-found-a-prompt-injection-in-my-own-IDs-t]] |
| 2026-09-21T02:52:45+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/6c62acee011ac685_Show-HN-I-found-a-prompt-injection-in-my-own-IDs-t]] |

## 摘要正文

← All writeups  triagewall.io I Found a Prompt Injection in My Own IDS Triage Tool. Here's What Actually Stopped It. I run Triagewall on my homelab — a local LLM that reads Suricata alerts and tells me whether each one is worth waking up for. It runs Foundation-Sec-8B through Ollama, classifies alerts as real , false_positive , or uncertain , and writes the verdict back so I'm not drowning in noise from my own torrent client. When I shipped v0.1, I knew the prompt injection risk existed in theory. Suricata alerts contain attacker-controlled fields — URLs, user-agents, payloads — and I was feeding all of that straight into an LLM prompt. The classic LLM-security warning. But I'm a Navy nuclear mechanic, not a security researcher, and the whole thing was working, so I waved at the problem and moved on. For v0.2 I decided to actually attack my own system. I added some defenses I assumed would be enough, then ran four injection scenarios against them. Three held. One didn't — and the way it failed was the part I didn't expect. The attacker named the verdict and the confidence. The LLM returned exactly what they asked for. This is what happened, what I tried first that didn't work, and …
