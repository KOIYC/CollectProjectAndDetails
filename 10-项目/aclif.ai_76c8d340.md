---
type: "project"
title: "Show HN: Aclif – Agent CLI framework: one grammar, canonical names across SaaS"
project_url: "https://aclif.ai/"
first_seen: "2026-09-20T14:03:17+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_chris_marino
  - story_49743382
  - show_hn
lang: "en"
---

# Show HN: Aclif – Agent CLI framework: one grammar, canonical names across SaaS

> [!info] 一句话导读
> aclif, the Agent CLI Framework

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://aclif.ai/>
> 首次收录：2026-09-20T14:03:17+08:00
> 来源渠道：HN Show HN
> 标签：author_chris_marino, story_49743382, show_hn
> 最新指标：点赞=34 · 评论=17 · engagement_velocity=34

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=34 · 评论=17 · engagement_velocity=34 | [[20-语料/posts/hn_show/2026-09-20/b06bf4c938bddbcf_Show-HN-Aclif-–-Agent-CLI-framework-one-grammar,-c]] |
| 2026-09-20T09:36:50+08:00 | HN Show HN | 点赞=34 · 评论=17 · engagement_velocity=34 | [[20-语料/posts/hn_show/2026-09-20/b06bf4c938bddbcf_Show-HN-Aclif-–-Agent-CLI-framework-one-grammar,-c]] |
| 2026-09-20T14:03:11+08:00 | HN Show HN | 点赞=34 · 评论=17 · engagement_velocity=34 | [[20-语料/posts/hn_show/2026-09-20/b06bf4c938bddbcf_Show-HN-Aclif-–-Agent-CLI-framework-one-grammar,-c]] |
| 2026-09-20T14:03:17+08:00 | HN Show HN | 点赞=34 · 评论=17 · engagement_velocity=34 | [[20-语料/posts/hn_show/2026-09-20/b06bf4c938bddbcf_Show-HN-Aclif-–-Agent-CLI-framework-one-grammar,-c]] |

## 摘要正文

aclif, the Agent CLI Framework  # The Agent CLI Framework  aclif builds command-line tools for AI agents. An agent gets a single tool that provides a unified abstraction across every SaaS provider: one grammar, and canonical names that reach the same record by the same name on any platform.  ## Try it now  Install the binary, list the providers, and read a command's schema, examples, and safety metadata.  ``` npm install -g @aclif/core  aclif discover --json aclif learn salesforce --json aclif learn servicenow --json aclif salesforce data query --schema aclif salesforce data query --examples aclif salesforce data query --query "SELECT Id FROM Account LIMIT 3" --dry-run aclif servicenow data query --table incident --query "active=true^priority=1" --dry-run ```  ## Why agents need their own CLI  An MCP server publishes a fixed list of tools, and every tool on the list occupies the agent's context on every turn. The server's author trades coverage for cost when the server is built. Publishing every operation (a typical API has hundreds of definitions) keeps the whole API reachable and consumes tokens for all of it on every turn. Publishing a handful of broad operations keeps the token…
