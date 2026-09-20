---
type: "corpus"
item_id: "1aea37756476ef99"
title: "Show HN: Amika – Multiplayer cloud workstations for coding agents and humans"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49716282"
project_url: "https://amika.dev/"
author: "dbmikus"
published_at: "2026-09-15T17:58:41Z"
captured_at: "2026-09-20T14:05:56+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_dbmikus
  - story_49716282
  - show_hn
metrics: {"points": 7, "comments": 5, "engagement_velocity": 7}
comments_count: 5
comments_total: 5
discovered_via: "hn:show_hn:90d"
---

# Show HN: Amika – Multiplayer cloud workstations for coding agents and humans

> [!info] 一句话导读
> Amika — The control plane for sandboxed cloud agents

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49716282>
> 指标：点赞=7 · 评论=5 · engagement_velocity=7
> 作者：dbmikus　|　发布：2026-09-15T17:58:41Z
> 项目链接：<https://amika.dev/>
> 采集：2026-09-20T14:05:56+08:00　|　id：`1aea37756476ef99`

## 正文

Amika — The control plane for sandboxed cloud agents

Backed by

# The control plane for sandboxed cloud agents

Create a sandbox VM on any any computer computer

Run any any agent agent on the sandbox

Message your agents and trigger workflows from any any surface surface

Give your agents the the best best environment environment to automate automate their their work work

Share your sandboxes with your team, or open them anywhere anywhere

## One platform, three ways to put it to work

It's the same sandbox and agent underneath, so you can move between all three without starting over.

### engineering: devboxes

Cloud devboxes with SSH and VPN access, preloaded with your stack.

02

### team: cloud background agents

Interactive cloud agents anyone can drive from Slack, Linear, or the web.

### automation: APIs + agentic workflows

Programmatic background agents and workflows that run on their own.

### devboxes

Give every developer a cloud devbox that mirrors production. SSH straight in or put it on your VPN, and code against your real services and seeded data.

- SSH, VPN, URLs. SSH straight in or attach the box to your VPN, so it's reachable like any host. Expose services via URLs to view them from the outside.
- Preloaded stack. Services, tooling, and seeded data are up on boot, so you and your agents work against a real environment.
- Fast snapshots. Boot in seconds from a snapshot that preserves your whole environment.

devbox · acme-web ready

Preloaded stack

postgres:16 redis node:20 acme/api acme/web

- You
- Priya
- agent

### cloud background agents

Let engineers and non-engineers spin up agents from the tools they already use, and collaborate with them in a multiplayer chat as the work happens.

- Every entry point. Start an agent from Slack, Linear, GitHub, the CLI, or the web.
- Multiplayer. Teammates watch, redirect, or take over the same live session.
- No setup needed. Non-technical teammates put agents to work without any local config.

- Slack@amika fix the flaky checkout test
- Linear Assigned: ENG-482
- GitHub@amika address review comments
- CLI$ amika start --task …
- API POST /v1/tasks

### APIs + agentic workflows

Control sandboxes and agents directly via API, CLI, and SDKs, or run higher-level workflows that trigger on events and schedules. Auto-fix incidents, keep docs in sync, or run a software factory that ships verified code.

- API + CLI + SDKs. Control the sandboxes and agents via API, CLI, or SDKs for total programmatic control.
- Event-driven workflows as code. Define multi-step agent workflows programmatically and version them with your repo. Trigger from webhooks, cron, or API.
- Verified output. Gate shipping on automated tests and custom checks, or step in as a human reviewer to approve and continue the work.

workflow · auto-fix running

on: sentry.alert

- 1. reproduce in sandbox
- 2. run tests
- 3. open PR if green

devbox · acme-web ready

Preloaded stack

postgres:16 redis node:20 acme/api acme/web

- You
- Priya
- agent

- Slack@amika fix the flaky checkout test
- Linear Assigned: ENG-482
- GitHub@amika address review comments
- CLI$ amika start --task …
- API POST /v1/tasks

- 1. reproduce in sandbox
- 2. run tests
- 3. open PR if green

## Examples of what you can build

A few of the workflows teams stand up on Amika. Each one is an agent (or a fleet of them) wired into your tools, your data, and your stack.

- pick up ticket · ENG-482
- write code in sandbox
- tests + typecheck · pass
- open PR #847

### Run your software factory

Background agents pick up tickets in a sandbox with every tool and service they need to implement and verify the work, then loop until checks pass and open a PR.

- Sentry · TypeError in checkout
- pull logs · GCP + AWS
- reproduce in sandbox
- open PR #481

### Auto-fix production bugs

Background agents watch Sentry, pull matching logs from GCP or AWS, reproduce the issue in a sandbox, and open a GitHub PR with the fix.

team-env.config shared toolchain hooks skills MCP servers

### Standardized cloud dev environment for humans and agents

One person sets up the whole stack, dependencies, services, and tools, plus agent hooks, skills, and MCP servers, and the whole team (humans and agents) boots the same environment.

### An agent across all your tools

Start an agent in Slack, dive deeper on your computer, then share results for a teammate to inspect on their phone.

Revenue by week+18%

### Agents for non-technical teammates

Ops, analytics, and customer-success agents (and more!) that connect to your data and build dynamic dashboards, no engineer required.

### Run agents on the machine in your closet

Message agents and sandboxes running on hardware you own, even the desktop in your closet, from anywhere.

### Use any agent and model

Run Codex, Claude Code, or OpenCode in the same sandbox. No model lock-in, and no markup on token usage.

### Run anywhere, isolated by default

Use our cloud, your cloud, or a machine you own. Every agent gets its own standardized environment, so they never step on each other and nobody burns a day on setup.

### Agents that verify their own work

Agents get the same tools and environment a person develops in, so they test and validate as they go, then attach evidence of a working implementation right on your PRs.

### Guardrails that enforce correctness

When agents ship 10x more code, review load explodes. Codify your rules (tests, type checks, custom validators) so only ready-to-ship work surfaces.

### Automate workflows, keep humans in the loop

Compose higher-level workflows that run on their own, from auto-fixing Sentry issues to turning Slack requests into shareable prototypes. Step in with human-in-the-loop whenever you want.

### Collaborate from anywhere

Talk to agents from the tools your team already uses. Every sandbox has multiplayer chat so teammates can work alongside them.

### Every session, recorded

Save every agent run with full transcripts, tool calls, and token costs. Replay any session, mine the best ones for rules and guardrails, and set cost ceilings or rate limits to keep usage in check.

## How it works

Your sandbox and agents are defined in your git repos as code

Each sandbox and agent boots from a git repo whose config defines your whole environment: the base image, services, seeded data, and which agents run where.

- Reproducible. Every devbox boots from the same config, so nothing drifts.
- Reviewable. Changes go through code review like anything else in your repo.
- Versioned. The config lives and moves alongside the code it works on.

Your custom agents are just a bundle: a VM, a model + harness, and your software

An agent is three composable pieces: a VM to run in, a model paired with a harness, and your software and source code.

- Any harness, any model. Claude Code, Codex, OpenCode, or one you built, with open source or frontier-lab models.
- Reuse environments. Run many agents on top of one shared environment.
- Use and extend your tools. Agents run your existing software tools or write their own, committing the changes back to your repo.

Create sandboxes on our hosted cloud or on infra you own

The Amika control plane spins up sandboxes wherever you want them to run.

- Any cloud. Provision on any cloud sandbox provider or Kubernetes cluster.
- Your own machines. Slice a machine you own into sandboxes with libkrun micro-VMs or Docker containers.
- Move later. Start hosted and migrate to your own infrastructure without rewriting anything.

Message agents and run commands over a networked channel

Send shell and exec commands to a VM and natural-language messages to its agents — all over one channel.

- Run anything. Execute programs or workflows directly on the VM.
- Multiplayer. You and your teammates can talk to the same agent at once.
- Agent-to-agent. A sandboxed agent can message other sandboxes and agents to coordinate.

Full network access: SSH, VPNs, and exposed services

Every sandbox is reachable like any other host on your network.

- SSH in. Connect to any sandbox directly over SSH.
- On your VPN. Bring a sandbox onto your VPN so it's addressable from anywhere.
- Live previews. Expose ports and services so a preview of what the agent is running is one URL away.

Sandboxes and agents boot fast from VM snapshots

Amika snapshots the full VM state, installed tools, running services, and warm caches, so every agent starts from the same point and nothing rebuilds from scratch.

- Resume in seconds. Sandboxes and their agents come back almost instantly.
- Preserved exactly. Your environment returns just as you left it.
- No cold starts. Skip reinstalling tools and rewarming caches on every boot.

Security: hide secrets and control every network request (coming soon)

You decide exactly what an agent can see and where it can reach.

- Hidden secrets. Keep secrets out of the agent's reach while its programs still use them.
- Network control. Approve inbound and outbound requests and data.

Is Amika open source?

How is this different from Cursor, Claude Code, or Codex?

Which models can agents use?

Can I run Amika on my own infrastructure?

How are sandboxes isolated? Is it secure?

Does Amika see my code?

## Start building and running sandboxed cloud agents with total control

Amika — The control plane for sandboxed cloud agents

Error fetching https://claude.ai/artifact/1rTtc9idTXFBcsuhPqJDoU: CRAWL_UNKNOWN_ERROR

## 评论（5/5）

> **jdc123** · 2026-09-15T18:00:47.000Z　
> Hey I'm Jakub, one of the co-founders. Let me know if you have any questions!

---

> **hrigar** · 2026-09-15T20:39:29.000Z　
> Been using Amika for a while now and really like it, one of the best options I've felt good about using as a devbox.

---

> **bhayashi** · 2026-09-16T05:37:14.000Z　
> Depending on how user friendly this is for non-technical people, this could be the perfect solution for how my team could collaborate on features with the designer and PM.How well does it work for mobile app development?

---

> **dbmikus** · 2026-09-15T20:42:07.000Z　
> Thanks! Have definitely appreciated your feedback as a user

---

> **dbmikus** · 2026-09-16T13:32:56.000Z　
> If you need xcode or macOS specific stuff, our VMs are all currently Linux basedWe're working on a "bring your own computer" feature which lets you take a spare Mac and slice it up into devbox VMs you can access from the cloud.We could also integrate https://limrun.com/ as a simulator for xcode, etc on top of Amika VMs

## 关联链接

- https://claude.ai/artifact/1rTtc9idTXFBcsuhPqJDoU:

## 导航

- 项目页：[[10-项目/amika.dev_de28d0e1]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
