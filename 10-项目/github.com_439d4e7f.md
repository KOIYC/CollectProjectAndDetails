---
type: "project"
title: "GPT-Load: a self-hosted AI gateway with reversible text redaction"
project_url: "https://github.com/tbphp/gpt-load"
first_seen: "2026-10-25T23:28:44+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/selfhosted
  - Release (AI)
lang: "en"
---

# GPT-Load: a self-hosted AI gateway with reversible text redaction

> [!info] 一句话导读
> Hi, I'm the author of GPT-Load, an MIT-licensed AI gateway with 7,000+ GitHub stars.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/tbphp/gpt-load>
> 首次收录：2026-10-25T23:28:44+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/selfhosted, Release (AI)
> 最新指标：得分=38 · 评论=24 · 赞踩比=0.6759259259259259

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-25T23:28:44+08:00 | Reddit 独立开发版块 | 得分=38 · 评论=24 · 赞踩比=0.6759259259259259 | [[20-语料/posts/reddit/2026-10-25/eab22ca42e0df421_GPT-Load-a-self-hosted-AI-gateway-with-reversible]] |

## 摘要正文

Hi, I'm the author of GPT-Load, an MIT-licensed AI gateway with 7,000+ GitHub stars.  It manages API keys and supported subscription accounts in one place. Your clients connect through the gateway, which handles credential scheduling, automatic failover, access controls, request logs, and usage tracking.  It runs with Docker Compose or as a single Go binary, includes a web UI, and uses SQLite by default. You don't need a separate database to get started.  One feature I'd particularly like feedback on is **reversible request redaction**.  Configurable regex rules replace or encrypt matching text locally before it reaches an upstream service. If the model returns intact, valid ciphertext, GPT-Load can restore the original values in response text and client-side tool arguments.  For example, an email address can be encrypted before reaching the model, then restored when the model includes that ciphertext in a tool call returned to your client. The rules apply to supported text fields; image and file contents aren't covered.  There's also an optional, experimental **JEV guardrails** integration. It reviews outgoing text against custom rules and can warn or block on matches. It uses an …
