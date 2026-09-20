---
type: "corpus"
item_id: "682a403142e8bf94"
title: "Show HN: Blue – open-source governance for coding agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49728525"
project_url: "https://bluee.sh/"
author: "tomislavs"
published_at: "2026-09-16T15:27:19Z"
captured_at: "2026-09-20T09:37:01+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_tomislavs
  - story_49728525
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Blue – open-source governance for coding agents

> [!info] 一句话导读
> Blue

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49728525>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：tomislavs　|　发布：2026-09-16T15:27:19Z
> 项目链接：<https://bluee.sh/>
> 采集：2026-09-20T09:37:01+08:00　|　id：`682a403142e8bf94`

## 正文

Blue | One harness to rule them all

# One harness to rule them all.

Give every team one trusted way to use Codex, Claude Code, Kimi Code, and OpenCode, while every developer keeps the native CLI they chose.

## Govern the work, not the way people work.

Blue sits between organization policy and the coding-agent CLIs developers already know. It adds control without replacing their tools or terminal experience.

Codex Claude Code Kimi Code OpenCode

### Your agent stays your agent.

Keep personal configuration, native terminal behavior, and the CLI workflow you already use. Blue handles policy before launch and then gets out of the way.

Explore supported harnesses

### One place to set the rules.

Publish policy, manage extensions, control versions, connect identity, and see client health across every supported agent.

Explore administration

## One terminal. Every governed workflow.

Authenticate, ship trusted tooling, move between agents, and pick up remote sessions without giving up the native CLI.

Resume anywhere Authenticate Governed launch Extensions Switch agents Gateway / direct

›/resume

Resume remote session · 4 available

Refactor OAuth refresh · Codex owned by you · ~/work/blue · 2 minutes ago

Diagnose deploy drift · Claude Code shared by maya@acme.dev · ~/work/platform

Improve gateway tracing · Kimi Code owned by you · ~/work/proxy

Ship auth docs · OpenCode shared by ren@acme.dev · ~/work/docs

✓ Portable bundle downloaded and verified

✓ Native Codex session restored atomically

Launching Codex · codex resume 0195…

$ blue login

Confirmation code: BLUE-7K9P

Opened your browser to authorize the CLI.

✓ Device authorization approved

✓ Rotating credentials stored with owner-only permissions

Logged in as alex@acme.dev (org acme).

$ blue codex -- --model gpt-5

✓ Identity verified · alex@acme.dev

✓ Personalized policy revision 42 loaded

✓ Codex 0.145.0 is installed, allowed, and verified

✓ Managed overlay reconciled; personal config preserved

✓ 6 managed extensions ready

Launching the native Codex CLI

✓ secure-review@8c41f7 · SHA-256 verified

✓ Linear MCP server activated

✓ Skills, hooks, and plugins projected for Codex

✓ Unmanaged local extensions left untouched

Applied revision 42 · all managed packages healthy

›/agent

Kimi Code installed and allowed

OpenCode installed and allowed

Quit and reload now gracefully stop the current agent

Launching the native Kimi Code CLI

✓ Current route · organization gateway

Session-bound inference JWT active · provider credentials stay server-side

Keep current session use direct mode after the next Blue restart

Quit and reload now gracefully stop the current agent

✓ Direct mode selected · governance remains active

Run /direct again to restore organization gateway routing.

## Everything teams need to govern agentic coding.

Set policy once, ship trusted tooling, connect identity and inference, and maintain visibility across every supported coding agent.

### Harness governance

Choose which coding agents and versions can run, then reject incompatible installations before launch.

02

### Managed extensions

Ship digest-pinned MCP servers, skills, plugins, hooks, subagents, and helper binaries from one catalog.

03

### Configuration policy

Reconcile organization settings into launch-scoped overlays without replacing developers’ personal configuration.

04

### Identity and access

Connect CLI device authorization and dashboard access with invitations, OIDC, and SCIM provisioning.

05

### Bring your own gateway

Connect your organization’s inference gateway and keep provider credentials server-side. LiteLLM is the first supported gateway.

06

### Session visibility

Opt in to native transcript capture using short-lived uploads to operator-controlled object storage.

Blue manages configuration while each agent talks directly to its provider using the developer’s existing credentials.

Connect your organization-operated gateway and route inference with a session-bound inference JWT. LiteLLM is supported first; provider credentials remain on your server.

## Self-host the reference stack. Replace the pieces you need.

Deploy with Docker Compose, Helm, and OpenTofu. Keep state in PostgreSQL and S3-compatible storage, or implement the published governance contract in your own services.

Docker Compose Kubernetes OpenTofu PostgreSQL S3 OpenAPI

## Latest from Blue.

Architecture, operations, and lessons from building a common control plane for coding agents.

## Install Blue to get started.

Connect to your organization and keep using the coding-agent CLI you already know, now with governance built in.

$`curl --proto '=https' --tlsv1.2 -LsSf https://github.com/BlocksOrg/blue/releases/latest/download/install.sh | sh`

# Word to Markdown converter with page references | DOCX Editor

## 关联链接

- https://github.com/BlocksOrg/blue/releases/latest/download/install.sh

## 导航

- 项目页：[[10-项目/bluee.sh_8fa5b2e1]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
