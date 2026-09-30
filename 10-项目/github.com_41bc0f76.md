---
type: "project"
title: "Show HN: Agentcap – eBPF exporter for AI-agent activity to Grafana"
project_url: "https://github.com/yeet-src/agentcap"
first_seen: "2026-09-30T18:57:07+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_r3tr0
  - story_49898915
  - show_hn
lang: "en"
---

# Show HN: Agentcap – eBPF exporter for AI-agent activity to Grafana

> [!info] 一句话导读
> eBPF Prometheus exporter for AI-agent activity — per-agent tools, domains, ports, files, CPU & network — with a Grafana dashboard. A yeet service.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/yeet-src/agentcap>
> 首次收录：2026-09-30T18:57:07+08:00
> 来源渠道：HN Show HN
> 标签：author_r3tr0, story_49898915, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-30T18:28:30+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-30/db993c77035da73a_Show-HN-Agentcap-–-eBPF-exporter-for-AI-agent-acti]] |
| 2026-09-30T18:57:07+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-30/db993c77035da73a_Show-HN-Agentcap-–-eBPF-exporter-for-AI-agent-acti]] |

## 摘要正文

# yeet-src/agentcap  eBPF Prometheus exporter for AI-agent activity — per-agent tools, domains, ports, files, CPU & network — with a Grafana dashboard. A yeet service.  - Stars: 7 - Forks: 0 - Watchers: 7 - Open issues: 0 - Homepage: https://yeet.cx - Default branch: master - Created: 2026-09-29T16:14:23Z  ## Languages  - C - JavaScript - Makefile - Python - Shell  ## Topics  - ai-agents - aider - audit - bpf - claude-code - codex - coding-agents - cursor - ebpf - gemini - goose - grafana - observability - openclaw - opencode - prometheus - prometheus-exporter - security - yeet  ## Top Contributors  - julian-goldstein (30 contributions)  ---  ## README  # agentcap  Agent Activity dashboard — overview: hero stats, tracked tasks, tool execs/s, which agent ran what, top tools, CPU by agent  AI coding agents run shell commands, open files, and make network calls on your machine, and most of it goes unseen. agentcap records that activity from the kernel with eBPF and exposes it as per-agent Prometheus metrics with a Grafana dashboard. It needs no SDK or changes to the agents, works on agents that are already running, and attributes child processes (a `bash` or `curl` a tool spawns) to t…
