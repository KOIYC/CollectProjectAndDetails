---
type: "corpus"
item_id: "1dcbb10ac3ba0532"
title: "Show HN: Use Kimi and OpenAI Subscriptions in Claude Code"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48339755"
project_url: "https://github.com/raine/claude-code-proxy"
author: "rane"
published_at: "2026-05-30T19:23:51Z"
captured_at: "2026-09-21T02:52:51+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-30"
tags:
  - 语料
  - hn_show
  - author_rane
  - story_48339755
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:144d"
---

# Show HN: Use Kimi and OpenAI Subscriptions in Claude Code

> [!info] 一句话导读
> raine/claude-code-proxy

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48339755>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：rane　|　发布：2026-05-30T19:23:51Z
> 项目链接：<https://github.com/raine/claude-code-proxy>
> 采集：2026-09-21T02:52:51+08:00　|　id：`1dcbb10ac3ba0532`

## 正文

# raine/claude-code-proxy

Use Claude Code with your ChatGPT, Kimi, Cursor or Grok subscription via a local Anthropic-compatible proxy

- Stars: 549
- Forks: 103
- Watchers: 549
- Open issues: 32
- License: MIT License
- Homepage: https://claude-code-proxy.raine.dev/
- Default branch: main
- Created: 2026-04-18T18:50:02Z

## Languages

- Just
- Nix
- Rust
- Shell

## Top Contributors

- raine (514 contributions)
- mulfyx (15 contributions)
- ItsAlbertZhang (4 contributions)
- Aotricx (3 contributions)
- thesobercoder (3 contributions)
- brocktice (2 contributions)
- wtfsayo (2 contributions)
- kevinsslin (2 contributions)
- biuworks (1 contributions)
- bottergpt (1 contributions)

---

## README

# claude-code-proxy

Claude Code, powered by **OpenAI Codex**, **Kimi**, **Grok**, **OpenCode Go**,
or **Cursor Agent**.

Docs:

LLM docs:

> [!TIP]
> I'm building aven, a local-first task manager
> for power users and agents.

## Why?

Claude Code remains an excellent coding harness, with strong tools, skills,
hooks, subagents, and editor integrations. claude-code-proxy keeps that client
experience while translating its Anthropic API traffic for subscription-backed
provider services.

One local process handles provider authentication, model-based routing,
protocol translation, streaming responses, and diagnostics. The built-in
monitor shows sessions, active and recent requests, errors, token usage, and
throughput.

## Quick start with Codex

Install on macOS or Linux:

```sh
brew install raine/claude-code-proxy/claude-code-proxy
```

Or use the release installer:

```sh
curl -fsSL https://raw.githubusercontent.com/raine/claude-code-proxy/main/scripts/install.sh | bash
```

Windows and other prebuilt artifacts are available from
GitHub Releases.

Sign in with a **ChatGPT Plus or Pro account**, not an OpenAI API account:

```sh
claude-code-proxy codex auth login
```

Start the proxy in one terminal:

```sh
claude-code-proxy serve
```

Start Claude Code in another:

```sh
ANTHROPIC_BASE_URL=http://127.0.0.1:18765 \
ANTHROPIC_AUTH_TOKEN=unused \
ANTHROPIC_MODEL=gpt-5.6-sol[1m] \
ANTHROPIC_SMALL_FAST_MODEL=gpt-5.6-luna[1m] \
CLAUDE_CODE_AUTO_COMPACT_WINDOW=272000 \
CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1 \
CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK=1 \
  claude
```

See Getting started
for the complete first session.

Optional Codex image generation and editing can reuse the same ChatGPT login:

```sh
CCP_CODEX_IMAGES_API=1 claude-code-proxy serve
curl http://127.0.0.1:18765/v1/images/generations \
  -H 'Content-Type: application/json' \
  -d '{"prompt":"A paper-cut fox","model":"gpt-image-2"}'
```

The opt-in Images API returns base64 image data and consumes the signed-in account's image quota. Image prompts and payloads are excluded from traffic captures. See the HTTP API for generation and edit schemas.

## Providers

| Provider | Account | Model selection |
| ------------ | ------------------------------ | ----------------------------------------------- |
| Codex | ChatGPT Plus or Pro | Registered `gpt-*` models and `-fast` variants |
| Kimi | kimi.com with Kimi Code access | `kimi-for-coding` and aliases |
| Grok | grok.com | Registered Grok models |
| OpenCode Go | OpenCode Go subscription | Non-conflicting IDs and `opencode-go/ ` |
| Cursor Agent | Cursor account | Cursor aliases and `cursor: ` prefixes |

Run `claude-code-proxy models` for the current catalog or
`claude-code-proxy models --full` for every dynamic Cursor alias.

> [!WARNING]
> The proxy accepts local requests without client authentication. It binds to
> `127.0.0.1` by default. Protect any non-loopback listener with a firewall or
> authenticating reverse proxy. Provider subscriptions, model access, terms,
> and account enforcement remain under each provider's control. Unofficial
> clients may carry account risk.

## Documentation

- What is claude-code-proxy?
- Choosing a provider
- Configure Claude Code
- Models and routing
- Monitor TUI
- Troubleshooting
- Command reference
- Configuration
- HTTP API
- Compatibility and limitations
- For coding agents

## Related projects

- aven: local-first task management for power
 users and agents
- claude-history: search Claude Code
 conversation history from the terminal
- git-surgeon: non-interactive
 hunk-level git staging for coding agents
- workmux: parallel coding tasks in git
 worktrees and tmux
- consult-llm: consult other AI models
 from an agent workflow

## License

MIT

# wavever/buildby

## 关联链接

- http://127.0.0.1:18765
- http://127.0.0.1:18765/v1/images/generations
- https://claude-code-proxy.raine.dev/
- https://raw.githubusercontent.com/raine/claude-code-proxy/main/scripts/install.sh

## 导航

- 项目页：[[10-项目/github.com_b6f3fee1]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
