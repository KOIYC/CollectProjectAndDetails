---
type: "corpus"
item_id: "8bb085276c1dd3c9"
title: "Show HN: Kival – A self-hosted knowledge system for organizations"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49724109"
project_url: "https://github.com/selemis-com/kival"
author: "zerosnacks"
published_at: "2026-09-16T09:48:32Z"
captured_at: "2026-09-20T14:04:30+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_zerosnacks
  - story_49724109
  - show_hn
metrics: {"points": 5, "comments": 4, "engagement_velocity": 5}
comments_count: 4
comments_total: 4
discovered_via: "hn:show_hn:90d"
---

# Show HN: Kival – A self-hosted knowledge system for organizations

> [!info] 一句话导读
> Self-hosted collaborative knowledge system for organizations.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49724109>
> 指标：点赞=5 · 评论=4 · engagement_velocity=5
> 作者：zerosnacks　|　发布：2026-09-16T09:48:32Z
> 项目链接：<https://github.com/selemis-com/kival>
> 采集：2026-09-20T14:04:30+08:00　|　id：`8bb085276c1dd3c9`

## 正文

# selemis-com/kival

Self-hosted collaborative knowledge system for organizations.

- Stars: 12
- Forks: 0
- Watchers: 12
- Open issues: 10
- License: Apache License 2.0
- Homepage: https://selemis.com
- Default branch: master
- Created: 2026-08-24T07:51:49Z

## Languages

- HTML
- Makefile
- PLpgSQL
- Rust
- Shell
- TypeScript

## Topics

- agent-memory
- agents
- ai-agents
- collaboration
- knowledge-base
- knowledge-graph
- knowledge-management
- mcp
- persistent-memory
- postgres
- rust
- self-hosted
- wiki

## Top Contributors

- zerosnacks (79 contributions)
- dependabot[bot] (8 contributions)

---

## README

 Self-hosted collaborative knowledge system for organizations

 Overview ·
 Setup ·
 Resources ·
 SDKs ·
 Community ·
 Contributing

## Overview

Kival is Selemis's self-hosted collaborative knowledge system for organizations.

Organizations constantly produce messages, documents, decisions, and records, yet the understanding that connects them is easily lost. Sources become detached from conclusions, decisions outlive their reasoning, and knowledge fragments across tools or leaves with the people who carried it.

Kival gives people and agents a shared place to deliberately create, edit, discuss, connect, version, and govern knowledge. History, relationships, discussions, authorship, and provenance remain connected as that knowledge develops, preserving the context needed to understand how something came to be and build on it over time.

* **Shared knowledge**: people and agents work against the same organizational knowledge rather than maintaining separate copies of context.
* **Continuity**: history, relationships, discussions, and provenance remain connected as knowledge develops, preserving how it came to be rather than only its latest state.
* **Deliberate authorship**: knowledge is explicitly created and maintained as organizational work, with clear authorship, access, and governance.
* **Durable context**: knowledge remains understandable even as the people, agents, models, applications, and tools around it change.
* **Self-hosted ownership**: the organization retains control over the knowledge and infrastructure on which its work depends.

## Setup

### Installation

Install `kivalup` from the latest stable release:

```sh
curl --proto '=https' --tlsv1.2 -fsSL \
  https://github.com/selemis-com/kival/releases/latest/download/install | bash
```

Then run:

```sh
kivalup
```

If your shell has not picked up the updated `PATH` yet, use `$HOME/.kival/bin/kivalup` or start a new shell.

To build and run Kival from source, see the development setup.

### Supported platforms

Prebuilt releases are available for Linux x86_64 and ARM64, macOS on Apple Silicon, and Windows through WSL.

Native Windows and Intel Mac releases are not currently provided.

### Quick start

Start PostgreSQL in the background with persistent local storage:

```sh
docker run -d \
  --name kival-postgres \
  -e POSTGRES_USER=kival \
  -e POSTGRES_PASSWORD=kival \
  -e POSTGRES_DB=kival \
  -p 5432:5432 \
  -v kival-postgres-data:/var/lib/postgresql \
  postgres:18
```

Point Kival at the database and start the server:

```sh
export DATABASE_URL=postgres://kival:kival@localhost:5432/kival
kivald serve
```

In another terminal, bootstrap the first global administrator:

```sh
export DATABASE_URL=postgres://kival:kival@localhost:5432/kival
kivald admin bootstrap \
  --username admin \
  --display-name "Admin"
```

The command prints a one-time enrollment link. Open it in your browser to register a passkey and complete the initial administrator setup.

Kival is now available at `http://localhost:3000`.

### Create a workspace

Create a workspace from the web application, or explore Kival using the built-in fictional ACME workspace:

```sh
kivald admin workspaces create --name "ACME" --demo acme
```

The demo includes connected documents, discussions, access boundaries, history, and shared agent skills for exploring Kival before adding your own knowledge.

> [!IMPORTANT]
> The ACME workspace is intended for exploration and evaluation only. Do not use it as the basis for a production workspace or build real organizational knowledge on top of it.

### Configure CLI access

From the web application, create an API key for the administrator and allow it access to the workspace.

Then configure the local CLI:

```sh
export KIVAL_API_KEY=<API_KEY>
```

Verify the CLI is authenticated and can access the workspace:

```sh
kival whoami
kival workspaces list
```

### Explore with an agent

Agents can use the same CLI and access model to inspect existing knowledge, follow relationships, and contribute new material.

**Trace a decision and its supporting context**

> Use the Kival CLI to explore the ACME workspace. Find an important decision, explain what was decided and why, trace the supporting knowledge that led to it, and include links to the relevant Kival objects.

**Synthesize project state into new knowledge**

> Use the Kival CLI to inspect Project Relay and RFC 024. Create a new object titled "Project Relay rollout review" summarizing the current rollout state, remaining risks, and next decision point, then link it to the relevant existing Kival objects. Show me what you created and include links to the objects you used.

**Turn operational history into follow-up knowledge**

> Use the Kival CLI to find a recent ACME incident and its related runbook. Create a short follow-up object with the key operational lesson and recommended next action, link it to both the incident and runbook, and include links to the resulting Kival objects.

## Resources

The Kival resources cover how Kival works, how to use it, how to connect it to other systems, and how to run it in production.

### Understand Kival

* Core concepts
* Objects and versions
* Relations and context
* History and provenance
* Access model

### Use Kival

* Creating and organizing knowledge
* Search and navigation
* Discussions and collaboration
* Working with others
* Practical workflows
* Using Kival with agents

### Connect Kival

* CLI
* API
* SDKs
* Agent access
* Automation
* Integrations

### Deployment & administration

* Deployment
* Administration

## SDKs

Kival provides official SDKs for Rust and TypeScript:

* Rust SDK
* TypeScript SDK

Both use scoped API keys and expose the same underlying system as the CLI.

They are intended for applications, integrations, automation, and agents that need programmatic access to Kival.

## Sponsors

Kival is developed and maintained by Selemis.

Sponsorship supports the continued development and long-term maintenance of Kival. Organizations interested in sponsoring the project can contact hello@selemis.com.

## Community

Join the conversation in GitHub Discussions to ask questions, share ideas, and discuss how Kival is being used.

## Contributing

See the Contributing Guide for information on reporting bugs, proposing features, and contributing to Kival.

At this time, we do **not accept pull requests or other code contributions from external contributors**.

## Security Policy

If you believe you have found a security vulnerability, please do not report it through GitHub Issues.

See the Security Policy for reporting instructions.

## License

Licensed under either of Apache License, Version 2.0 or MIT license at your option.

This software includes third-party components subject to separate license terms. See THIRD_PARTY_NOTICES.md.

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in this project by you, as defined in the Apache-2.0 license, shall be dual licensed as above, without any additional terms or conditions.

# dimonomid/salmon

## 评论（4/4）

> **nikolovv** · 2026-09-16T09:51:30.000Z　
> this is crazyy, lately I am playing with nobodywho and build a local hosted journal so my data stays with me. Here you can check it out https://github.com/nikolovv861/reflect but I think you can definetely integrate some parts from nobodywho image this aka Obsidian on steroids + local AI model

---

> **brodouevencode** · 2026-09-16T13:30:06.000Z　
> A lot of orgs seem to be implementing their own version of this (we are), but having an out of the box solution is a great starting point.

---

> **powermax3001** · 2026-09-16T13:42:49.000Z　
> Looks nice, would help me, if there where some real world examples on the website.

---

> **timothydl** · 2026-09-16T13:41:44.000Z　
> What's the out-of-the-box solution you are using?

## 关联链接

- http://localhost:3000`.
- https://github.com/selemis-com/kival/releases/latest/download/install
- https://selemis.com

## 导航

- 项目页：[[10-项目/github.com_de250669]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
