---
type: "project"
title: "Show HN: My AI spent $15 on a test order, so I built a payment guardrail"
project_url: "https://github.com/felixpg13-glitch/spendshield"
first_seen: "2026-09-21T03:11:20+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_felixpg13
  - story_49511045
  - show_hn
lang: "en"
---

# Show HN: My AI spent $15 on a test order, so I built a payment guardrail

> [!info] 一句话导读
> felixpg13-glitch/spendshield

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/felixpg13-glitch/spendshield>
> 首次收录：2026-09-21T03:11:20+08:00
> 来源渠道：HN Show HN
> 标签：author_felixpg13, story_49511045, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:33:52+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/d89de75dea3212be_Show-HN-My-AI-spent-$15-on-a-test-order,-so-I-buil]] |
| 2026-09-21T03:11:20+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/d89de75dea3212be_Show-HN-My-AI-spent-$15-on-a-test-order,-so-I-buil]] |

## 摘要正文

# felixpg13-glitch/spendshield  AI Agent 付款安全层: 身份/意图/密钥 三道信任支柱 + 四道闸门。给 AI 定义带消费上限的数字身份(Spend-Capped Identity), 防提示注入, 密钥不落盘。Python + MCP。  - Stars: 1 - Forks: 0 - Watchers: 1 - Open issues: 0 - Default branch: main - Created: 2026-08-31T08:52:54Z  ## Languages  - Dockerfile - Python  ## Topics  - agent-security - ai-agents - guardrails - llm-security - mcp - payment-security - python - python-library  ## Top Contributors  - felixpg13-glitch (27 contributions)  ---  ## README  # 💰 SpendShield — Payment Guardrails for AI Agents  > **Before your AI spends real money, it passes through SpendShield.**  An open-source payment safety layer for Python and MCP. Give your AI agent a **spend-capped digital identity (KYA)**, run every payment through four deterministic gates, defend against prompt injection, and keep secrets in an encrypted vault.  ## 🩸 Why this project exists (a real incident)  On August 9, 2026, my automation system ran a test order. I sent `dry: true`, expecting a price preview. The server only honored `?dry=1` — **4 orders of ¥99 were charged for real, and the money was gone.**  This is not just my problem. AI agents are about to order food, top up accounts, and call pai…
