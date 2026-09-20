---
type: "corpus"
item_id: "f02a13e30472e298"
title: "Show HN: Arkloop – Open-source, local-first Agent client"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47959945"
project_url: "https://github.com/qqqqqf-q/arkloop"
author: "qqqqqf"
published_at: "2026-04-30T09:01:27Z"
captured_at: "2026-09-21T02:52:29+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_qqqqqf
  - story_47959945
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: Arkloop – Open-source, local-first Agent client

> [!info] 一句话导读
> 干净、强大、属于你的 AI Agent 平台 --AI agents, without the clutter.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47959945>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：qqqqqf　|　发布：2026-04-30T09:01:27Z
> 项目链接：<https://github.com/qqqqqf-q/arkloop>
> 采集：2026-09-21T02:52:29+08:00　|　id：`f02a13e30472e298`

## 正文

# qqqqqf-q/Arkloop

干净、强大、属于你的 AI Agent 平台 --AI agents, without the clutter.

- Stars: 374
- Forks: 36
- Watchers: 374
- Open issues: 11
- License: Other
- Homepage: https://arkloop.io
- Default branch: main
- Created: 2026-01-25T07:06:00Z

## Languages

- CSS
- Dockerfile
- Go
- HTML
- JavaScript
- Lua
- Makefile
- Objective-C
- PLpgSQL
- Python
- Ruby
- Shell
- TypeScript

## Topics

- acp
- agent
- ai
- anthropic
- chat
- chatbot
- deepseek
- electron
- mcp
- openai
- openclaw
- personal
- saas

## Top Contributors

- qqqqqf-q (2620 contributions)
- kilockok (37 contributions)
- DivXPro (17 contributions)
- SkyAerope (7 contributions)
- alexma233 (4 contributions)
- tageniu (2 contributions)
- Fodesu (1 contributions)
- namphamdev (1 contributions)
- Pleasurecruise (1 contributions)
- mizorewww (1 contributions)

---

## README

 Open-source / Clean / Powerful — Your AI Agent Platform

---

Arkloop is a design-focused open-source AI Agent platform. Multi-model routing, sandboxed execution, persistent memory — a clean desktop app that works out of the box.

## Download

Download the latest version from GitHub Releases, supporting macOS, Linux, and Windows.

The desktop app bundles the full runtime — no Docker, no configuration. Just open and use. Automatic updates via GitHub Releases.

On first launch, Desktop can install the `ark` command-line tool. After that, you can start the same local runtime without the Desktop window:

```bash
ark web
```

### CLI via Homebrew

Homebrew installs the Arkloop CLI only:

```bash
brew install qqqqqf-q/arkloop/arkloop && ark web
```

For a headless Linux machine, use one command:

```bash
sh -c 'set -e; arch="$(uname -m)"; case "$arch" in x86_64|amd64) arch=amd64 ;; aarch64|arm64) arch=arm64 ;; *) echo "unsupported architecture: $arch" >&2; exit 1 ;; esac; name="ark-linux-${arch}"; rm -rf "$name"; curl -fsSL "https://github.com/qqqqqf-q/Arkloop/releases/latest/download/${name}.tar.gz" | tar -xz; cd "$name"; exec ./ark web --host 0.0.0.0 --no-open'
```

## Features

Arkloop does what other AI chat tools do — multi-model support, tool calling, code execution, memory — but we focus on doing it cleanly:

- **Multi-Model Routing** — OpenAI, Anthropic, and any compatible API; priority-based automatic routing with rate limit handling
- **Sandboxed Execution** — Code runs in Firecracker microVMs or Docker containers with strict resource limits
- **Persistent Memory** — System constraints, long-term facts, and session context preserved across conversations
- **Prompt Injection Protection** — Semantic-level scanning that detects and blocks injection attacks
- **Channel Integration** — Telegram integration with media handling and group context
- **Custom Personas** — Independent system prompts, tool sets, and behavior configs; Lua scripting supported
- **MCP / ACP** — Model Context Protocol and Agent Communication Protocol support
- **Skill Ecosystem** — Import skills from ClawHub, compatible with OpenClaw SKILL.md format

Full documentation at docs.

## Contributing

We welcome contributions of all kinds.

Even if you're not a developer, just a regular user — if anything feels off while using it, even a bit of spacing, a color, a tiny detail, or a big-picture direction — please open an issue. We take every UX detail seriously, and your feedback makes the experience better for everyone.

See CONTRIBUTING.md for commit conventions and development workflow.

## Sponsors

Thanks to the following friends for their support, keeping Arkloop going:

- @Jinnkunn — Bought me a domain
- @jeck — Treated me to an iced Americano
- @chuichui — Covered my AI costs for two weeks
- @薄荷奶昔 — Covered AI costs for Clover and Chiffon

## Contributors

## If you can, give us a Star
wkwUSiE3xZw1NeDrSFqJYDkkSEDULMfu

## Architecture

| Service | Stack | Role |
|---------|-------|------|
| API | Go | Authentication, RBAC, resource management, audit logging |
| Gateway | Go | Reverse proxy, rate limiting, risk scoring |
| Worker | Go | Job execution, LLM routing, tool dispatch, agent loop |
| Sandbox | Go | Code execution isolation |
| Desktop | Electron + Go | Native desktop app with embedded sidecar |
| Web | React / TypeScript | User interface |
| Console | React / TypeScript | Admin dashboard |

Infrastructure: PostgreSQL, Redis, SeaweedFS (or filesystem), OpenViking (vector memory).

## Development

```bash
bin/ci-local quick        # Quick local CI
bin/ci-local integration  # Go integration tests
bin/ci-local full          # Full check
```

## Self-Hosting

> The self-hosting deployment path is still in development. While included in the current release, availability is not guaranteed. We are not focusing on this during the Alpha phase. We plan to provide full server deployment support once the desktop version stabilizes.

## Star History

Star History Chart

## Security

To report vulnerabilities, please email qingf622@outlook.com instead of opening a public issue. See SECURITY.md for our disclosure policy.

## License

Licensed under the Arkloop License, a modified Apache License 2.0 with additional conditions:

- **Multi-tenant restriction** — Source code may not be used to operate a multi-tenant SaaS without written authorization.
- **Brand protection** — LOGO and copyright information in the frontend components must not be removed or modified.

# rogerwelin/pg_column_tetris

## 关联链接

- https://arkloop.io
- https://github.com/qqqqqf-q/Arkloop/releases/latest/download/${name}.tar.gz

## 导航

- 项目页：[[10-项目/github.com_11d62bd9]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
