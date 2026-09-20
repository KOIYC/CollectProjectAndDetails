---
type: "project"
title: "Show HN: Hexlock – Replace PII in text with fake data that has the same format"
project_url: "https://github.com/ttarvis/hexlock"
first_seen: "2026-09-21T02:52:22+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_lemaudit
  - story_47963789
  - show_hn
lang: "en"
---

# Show HN: Hexlock – Replace PII in text with fake data that has the same format

> [!info] 一句话导读
> PII redaction that preserves data format, tokenized values stay usable in LLM pipelines

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/ttarvis/hexlock>
> 首次收录：2026-09-21T02:52:22+08:00
> 来源渠道：HN Show HN
> 标签：author_lemaudit, story_47963789, show_hn
> 最新指标：点赞=5 · 评论=0 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:09:14+08:00 | HN Show HN | 点赞=5 · 评论=0 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-21/b844149ab93348a5_Show-HN-Hexlock-–-Replace-PII-in-text-with-fake-da]] |
| 2026-09-21T01:13:42+08:00 | HN Show HN | 点赞=5 · 评论=0 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-21/b844149ab93348a5_Show-HN-Hexlock-–-Replace-PII-in-text-with-fake-da]] |
| 2026-09-21T02:52:22+08:00 | HN Show HN | 点赞=5 · 评论=0 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-21/b844149ab93348a5_Show-HN-Hexlock-–-Replace-PII-in-text-with-fake-da]] |

## 摘要正文

# ttarvis/hexlock  PII redaction that preserves data format, tokenized values stay usable in LLM pipelines  - Stars: 7 - Forks: 0 - Watchers: 7 - Open issues: 0 - License: Apache License 2.0 - Homepage: https://hexlock.xyz - Default branch: master - Created: 2026-04-28T21:37:30Z  ## Languages  - C - Makefile - Python - Shell  ## Topics  - ai-tools - compliance - data - encryption - format-preserving-encryption - llm - llm-security - llm-tools - pii - pii-redaction - privacy - python - security - sensitive-data - text-processing  ## Top Contributors  - ttarvis (5 contributions)  ---  ## README  # hexlock  `hexlock` transforms sensitive data before it reaches your LLM. Phone numbers, emails, and card numbers become realistic tokens that your prompt still understands, and can be restored after.  ## What is it?  `hexlock` is a tool for preventing sensitive data from being used with LLMs. It replaces sensitive data but preserves the format so the LLM understands it still. Then it rehydrates the response with the original data. The sensitive data never gets sent to the LLM.  Data types protected include email, phone, SSNs, driver's license identifiers, passport IDs, credit card, GitHub t…
