---
type: "project"
title: "Show HN: Maybe AI agents shouldn't decide what's sensitive"
project_url: "https://github.com/softcane/hamza"
first_seen: "2026-09-21T03:11:15+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_pradeep1177
  - story_49112171
  - show_hn
lang: "en"
---

# Show HN: Maybe AI agents shouldn't decide what's sensitive

> [!info] 一句话导读
> An egress gate for CLI coding agents. Masks secrets and customer data in the request body before it reaches the model provider, and the agent keeps working.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/softcane/hamza>
> 首次收录：2026-09-21T03:11:15+08:00
> 来源渠道：HN Show HN
> 标签：author_pradeep1177, story_49112171, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:31:46+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/e0504d26c5212fca_Show-HN-Maybe-AI-agents-shouldn't-decide-what's-se]] |
| 2026-09-21T03:11:15+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/e0504d26c5212fca_Show-HN-Maybe-AI-agents-shouldn't-decide-what's-se]] |

## 摘要正文

# softcane/hamza  An egress gate for CLI coding agents. Masks secrets and customer data in the request body before it reaches the model provider, and the agent keeps working.  - Stars: 1 - Forks: 0 - Watchers: 1 - Open issues: 0 - License: Apache License 2.0 - Default branch: main - Created: 2026-07-28T15:39:08Z  ## Languages  - Dockerfile - HTML - Java - Python  ## Topics  - ai-agents - claude-code - dlp - envoy - llm-security - pii - secrets-detection  ## Top Contributors  - softcane (7 contributions)  ---  ## README  # Hamza  Hamza masking sensitive data before it reaches an AI service  *The name Hamza is inspired by the undercover operative in *Dhurandhar*.*  Hamza is a proxy for Claude Code and Codex. It masks detected secrets and approved types of personal data before sending prompts to Anthropic or OpenAI.  https://github.com/user-attachments/assets/be336248-ba3f-4597-a05c-fb1af8b3124e  An agent debugging an import job may read a CSV, an `.env` file, and application logs. That context can contain customer data and credentials. Hamza masks detected values while leaving the rest of the prompt intact:  ```text Before: patient=priya.fixture@example.com  key=AKIAABCDEFGHIJKLMNOP …
