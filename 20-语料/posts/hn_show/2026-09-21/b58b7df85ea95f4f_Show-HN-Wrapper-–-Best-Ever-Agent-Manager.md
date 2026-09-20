---
type: "corpus"
item_id: "b58b7df85ea95f4f"
title: "Show HN: Wrapper – Best Ever Agent Manager"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49110318"
project_url: "https://github.com/xatuke/wrapper"
author: "satuke"
published_at: "2026-07-30T14:12:42Z"
captured_at: "2026-09-21T03:11:17+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-30"
tags:
  - 语料
  - hn_show
  - author_satuke
  - story_49110318
  - show_hn
metrics: {"points": 6, "comments": 0, "engagement_velocity": 6}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: Wrapper – Best Ever Agent Manager

> [!info] 一句话导读
> Default branch: main

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49110318>
> 指标：点赞=6 · 评论=0 · engagement_velocity=6
> 作者：satuke　|　发布：2026-07-30T14:12:42Z
> 项目链接：<https://github.com/xatuke/wrapper>
> 采集：2026-09-21T03:11:17+08:00　|　id：`b58b7df85ea95f4f`

## 正文

# xatuke/wrapper

wrap your agents

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- Default branch: main
- Created: 2026-07-13T11:50:47Z

## Languages

- Dockerfile
- JavaScript
- TypeScript

## Top Contributors

- xatuke (2 contributions)

---

## README

# wrapper

Host, manage, and observe pi agents on Slack — each agent in
its own hardened container, with Langfuse tracing
(tokens, cost, tool spans), managed by one CLI.

**An agent is config + tools; everything else is a shared runtime.** Adding an
agent means writing an `agent.yaml`, optionally dropping tool modules in a
folder, and running `wrapper agent add` — not writing a new service.

```
agents/support-bot/
├── agent.yaml     # model, prompt, channels, tools, features
├── prompt.md      # system prompt
├── tools/*.ts     # custom tools (TypeBox schema + execute)
├── slack/         # slack-cli project (manifest.json, app registry)
└── .env           # Slack tokens + keys (gitignored)
```

Each agent gets its own Slack app (Socket Mode — outbound only, no public
ingress), a persistent volume for conversation history, and per-turn traces.
Opt-in runtime features give agents self-managed cron schedules, persistent
memory, and a file workspace. Custom Dockerfiles bake in extra CLIs or npm
packages; multi-line secrets go in base64 via `wrapper env set-file`.

## Quick start

```bash
npm install --ignore-scripts && npm run build
cp wrapper.example.yaml wrapper.yaml          # set your Slack team ID
alias wrapper="node $PWD/packages/cli/dist/index.js"

wrapper init --team-id T0XXXXXXXXX            # starts Langfuse, provisions org
echo 'ANTHROPIC_API_KEY=sk-ant-...' >> agents/.env

wrapper agent add support-bot --channels "#support"
wrapper up support-bot                        # then /invite @support-bot in Slack
```

Full walkthrough: docs/getting-started.md.

## Documentation

| Doc | What |
|---|---|
| docs/getting-started.md | Local setup end to end (prereqs, init, first agent, day-to-day) |
| docs/agents.md | Creating agents: `agent.yaml` reference, custom tools, cron/memory/workspace features, custom images |
| docs/langfuse.md | Tracing: the bundled stack, **using an existing Langfuse deployment**, or Langfuse Cloud |
| docs/deploy-vm.md | Running 24/7 on a plain cloud VM (AWS EC2 / GCP GCE) — no Kubernetes |
| docs/deploy-k8s-aws.md | Kubernetes on AWS: EKS, ECR, Bedrock via IRSA, hardening |
| docs/deploy-k8s-gcp.md | Kubernetes on GCP: GKE, Artifact Registry, Workload Identity, hardening |
| docs/k8s-manifests.md | The generated Kubernetes manifests, annotated, and how to customize them |
| DESIGN.md | Architecture and dated design decisions |
| AGENTS.md | Orientation for AI coding agents working in this repo |

## Deploy targets

`wrapper.yaml` sets `target: local | k8s` — **same commands either way**:

- **local** — docker compose on your machine or a cloud VM,
 with a bundled self-hosted Langfuse (or your existing one).
- **k8s** — `wrapper up` builds and pushes images (ECR
 or Artifact Registry) and deploys each agent as a
 hardened Deployment (no Service/Ingress) with a PVC for sessions and a
 Secret synced from the agent's `.env`.

## Day-to-day

```bash
wrapper ui                      # web console at localhost:3020 (status, logs, env)
wrapper status                  # containers/pods + langfuse health
wrapper logs support-bot -f
wrapper env set support-bot K=V && wrapper restart support-bot
wrapper agent remove support-bot [--purge]
```

## What's tracked where

- **This repo is the framework.** `docker-compose.yml`, `k8s/`, and each
 agent's `.slack/` app registry are **generated** — gitignored, regenerated
 by the CLI, never edited by hand. `wrapper.yaml` (deployment config) and
 `wrapper.secrets.json` are yours and gitignored too; create them from
 `wrapper.example.yaml` / `wrapper.secrets.example.json`.
- **Your agents are yours.** The entire `agents/` folder is ignored by
 wrapper's git — keep your agents (and optionally your `wrapper.yaml`) in
 their own repo nested inside it, so `git pull` here updates the framework
 without touching them. `wrapper agent add` scaffolds the folder with a
 README and secret-excluding `.gitignore`s; see
 docs/agents.md.

A fresh machine needs: clone wrapper, clone your agents into `agents/`,
`npm install --ignore-scripts && npm run build`, a `wrapper.yaml`,
`wrapper init`, restore `.env` secrets, `wrapper up`.

# alibaba/skill-up

## 导航

- 项目页：[[10-项目/github.com_1d3995ae]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
