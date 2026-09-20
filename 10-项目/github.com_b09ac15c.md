---
type: "project"
title: "Show HN: mcpguard – security scanner and firewall for MCP servers"
project_url: "https://github.com/GT-Projects256/mcpguard"
first_seen: "2026-09-21T02:52:43+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_GTprojects
  - story_48346248
  - show_hn
lang: "en"
---

# Show HN: mcpguard – security scanner and firewall for MCP servers

> [!info] 一句话导读
> GT-Projects256/mcpguard

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/GT-Projects256/mcpguard>
> 首次收录：2026-09-21T02:52:43+08:00
> 来源渠道：HN Show HN
> 标签：author_GTprojects, story_48346248, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:27:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/edcb7762610cd4a3_Show-HN-mcpguard-–-security-scanner-and-firewall-f]] |
| 2026-09-21T02:52:43+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/edcb7762610cd4a3_Show-HN-mcpguard-–-security-scanner-and-firewall-f]] |

## 摘要正文

# GT-Projects256/mcpguard  Open-source security firewall for MCP servers. Scan for OWASP MCP Top 10 vulnerabilities, enforce runtime policies on AI agent tool calls, and generate compliance audit logs.  - Stars: 6 - Forks: 0 - Watchers: 6 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-05-27T05:41:04Z  ## Languages  - JavaScript - TypeScript  ## Topics  - ai-agent - audit - compliance - firewall - llm - mcp - owasp - security - tool-poisoning - typescript  ## Top Contributors  - GT-Projects256 (10 contributions)  ---  ## README  # mcpguard  Security scanner and firewall for MCP (Model Context Protocol) servers. Checks your configs for known issues, blocks sketchy tool calls at runtime, and keeps audit logs.  Maps to the **OWASP MCP Top 10** (2026).  ## Why  MCP is everywhere now - Claude, Cursor, VS Code, OpenAI. But most setups ship with zero security review. Studies found 82% of MCP implementations have path traversal issues, 67% have code injection vectors, and about 5.5% of public servers have tool poisoning baked in.  This tool helps you catch that stuff before it bites you.  ## Quick Start  ```bash npm install -g @gtprojects/mcpguard  # scan you…
