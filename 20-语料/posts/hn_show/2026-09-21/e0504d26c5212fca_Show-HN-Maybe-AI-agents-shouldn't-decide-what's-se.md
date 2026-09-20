---
type: "corpus"
item_id: "e0504d26c5212fca"
title: "Show HN: Maybe AI agents shouldn't decide what's sensitive"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49112171"
project_url: "https://github.com/softcane/hamza"
author: "pradeep1177"
published_at: "2026-07-30T16:21:00Z"
captured_at: "2026-09-21T03:11:15+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-30"
tags:
  - 语料
  - hn_show
  - author_pradeep1177
  - story_49112171
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: Maybe AI agents shouldn't decide what's sensitive

> [!info] 一句话导读
> An egress gate for CLI coding agents. Masks secrets and customer data in the request body before it reaches the model provider, and the agent keeps working.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49112171>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：pradeep1177　|　发布：2026-07-30T16:21:00Z
> 项目链接：<https://github.com/softcane/hamza>
> 采集：2026-09-21T03:11:15+08:00　|　id：`e0504d26c5212fca`

## 正文

# softcane/hamza

An egress gate for CLI coding agents. Masks secrets and customer data in the request body before it reaches the model provider, and the agent keeps working.

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- License: Apache License 2.0
- Default branch: main
- Created: 2026-07-28T15:39:08Z

## Languages

- Dockerfile
- HTML
- Java
- Python

## Topics

- ai-agents
- claude-code
- dlp
- envoy
- llm-security
- pii
- secrets-detection

## Top Contributors

- softcane (7 contributions)

---

## README

# Hamza

Hamza masking sensitive data before it reaches an AI service

*The name Hamza is inspired by the undercover operative in
*Dhurandhar*.*

Hamza is a proxy for Claude Code and Codex. It masks detected secrets and
approved types of personal data before sending prompts to Anthropic or OpenAI.

https://github.com/user-attachments/assets/be336248-ba3f-4597-a05c-fb1af8b3124e

An agent debugging an import job may read a CSV, an `.env` file, and application
logs. That context can contain customer data and credentials. Hamza masks
detected values while leaving the rest of the prompt intact:

```text
Before: patient=priya.fixture@example.com  key=AKIAABCDEFGHIJKLMNOP
After:  patient=<EMAIL_482191>             key=<SECRET_730044>
```

The same value gets the same placeholder within a request. This lets the model
follow references without receiving the original value.

## Why this is an organization problem

Existing security tools may not see the final request assembled by a coding
agent.

| Control | What it sees | What it can miss |
|---|---|---|
| Git secret scanning | Committed files | A key read from `.env` but never committed |
| Endpoint DLP | Files, email, and removable storage | Data inside an allowed HTTPS request |
| Web security tools | Browser traffic | A CLI process calling an approved API |
| Code review | Source-code changes | Logs and files added to a prompt |

A developer may ask an agent to debug an import job without knowing which files
the agent will read. Customer records or credentials can then leave the network
inside a normal request to an approved AI service.

This creates work for security and compliance teams. They may need to rotate a
credential, investigate which records left the network, or change the contract
with the AI vendor. Hamza reduces that exposure by masking detected values
before the request leaves.

Hamza does not replace access controls, retention rules, or legal agreements.

## How it works

```mermaid
flowchart LR
    A["Claude Code or Codex"] --> B["Hamza proxy"]
    B --> C["Find secrets and personal data"]
    C --> D["Apply the configured action"]
    D -->|"mask"| E["Replace the detected value"]
    D -->|"allow"| F["Anthropic or OpenAI"]
    D -->|"block"| G["Stop the request"]
    E --> F
```

1. Hamza inspects supported request bodies from Claude Code or Codex.
2. It finds the text sent to the AI service.
3. The secret scanner, registered-value detector, and Presidio inspect that
 text.
4. Depending on the rule, Hamza records, masks, or blocks the finding.
5. For masking rules, it replaces the detected value with a placeholder such as
 `<SECRET_1>` or `<EMAIL_1>`.

Hamza also writes an audit record with the action, detector, and byte counts.
The record contains no prompt text or matched values.

## What Hamza detects

| Detector | Finds |
|---|---|
| Secret scanner | Cloud, source-control, package-registry, and SaaS credentials |
| Presidio | Email, phone, payment-card, IP, and other approved data types |

You can also register customer values that Hamza should recognize.

The full Presidio entity list and thresholds are in
`detector/presidio/approved-profile.json`.

## Run it

You need Docker Compose.

```bash
HAMZA_POSTURE=MASK docker compose up -d --build
```

The first start may take a minute while Presidio loads.

### Claude Code

Set the Anthropic base URL:

```bash
export ANTHROPIC_BASE_URL=http://127.0.0.1:10000
claude
```

Add the export to your shell profile if you want to keep it across sessions.
Claude Code also accepts `ANTHROPIC_BASE_URL` in the `env` section of
`settings.json`.

### Codex

Add this to `~/.codex/config.toml`:

```toml
[model_providers.hamza]
name = "hamza"
base_url = "http://127.0.0.1:10000/backend-api/codex"
wire_api = "responses"
requires_openai_auth = true

[profiles.hamza]
model_provider = "hamza"
```

Then start Codex with the profile:

```bash
codex --profile hamza
```

## Services

| Address | Service |
|---|---|
| `http://127.0.0.1:10000` | Proxy used by Claude Code and Codex |
| `http://127.0.0.1:3000` | Grafana dashboard |
| `http://127.0.0.1:8080/actuator/prometheus` | Prometheus metrics |

Presidio runs inside the Docker network and has no host port.

To disable Presidio:

```bash
HAMZA_PRESIDIO_ENABLED=false \
  HAMZA_POSTURE=MASK \
  docker compose up -d --build --scale presidio=0
```

## Build and test

Hamza requires Java 25 and Maven 3.9.11.

```bash
mvn -B clean verify
docker build .
```

See `CONTEXT.md` for the domain model and
`AGENTS.md` for the complete test suite.

# openmetaharness/openmetaharness

## 关联链接

- http://127.0.0.1:10000
- http://127.0.0.1:10000/backend-api/codex
- http://127.0.0.1:10000`
- http://127.0.0.1:3000`
- http://127.0.0.1:8080/actuator/prometheus`
- https://github.com/user-attachments/assets/be336248-ba3f-4597-a05c-fb1af8b3124e

## 导航

- 项目页：[[10-项目/github.com_9eb6404c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
