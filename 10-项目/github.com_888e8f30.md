---
type: "project"
title: "Show HN: An MCP proxy that sends 97% fewer tool-definition tokens per request"
project_url: "https://github.com/datolabs-io/mcp-toolsearch-proxy"
first_seen: "2026-11-04T09:51:43+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_TDabasinskas
  - story_50356916
  - show_hn
lang: "en"
---

# Show HN: An MCP proxy that sends 97% fewer tool-definition tokens per request

> [!info] 一句话导读
> datolabs-io/mcp-toolsearch-proxy

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/datolabs-io/mcp-toolsearch-proxy>
> 首次收录：2026-11-04T09:51:43+08:00
> 来源渠道：HN Show HN
> 标签：author_TDabasinskas, story_50356916, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-04T09:51:43+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-04/a54a8d3b9d3d6ed6_Show-HN-An-MCP-proxy-that-sends-97%-fewer-tool-def]] |

## 摘要正文

# datolabs-io/mcp-toolsearch-proxy  MCP server that puts search_tools, describe_tool and the call tools in front of a large MCP tool catalog  - Stars: 1 - Forks: 0 - Watchers: 1 - Open issues: 2 - License: MIT License - Default branch: main - Created: 2026-10-30T15:26:35Z  ## Languages  - Dockerfile - Go - Shell  ## Topics  - go - mcp - mcp-server - model-context-protocol - tool-search  ## Top Contributors  - tdabasinskas (7 contributions) - datolabs-automation[bot] (3 contributions) - renovate[bot] (2 contributions)  ---  ## README  # mcp-toolsearch-proxy  CI OpenSSF Scorecard Glama  **mcp-toolsearch-proxy** lets a model use hundreds or thousands of MCP tools without loading them. On 500 tools, each request carries 97% fewer tokens of tool definitions, a task costs about half as much, and the model reaches the right tool nearly as often as with every tool loaded (benchmarks).  It is an MCP server that puts five tools in front of an MCP server with far too many to list to a model, such as a gateway that aggregates dozens of servers:  | Tool | Does | | --- | --- | | `search_tools` | finds the tools that can do what a query describes, with the input schemas of the best few, for up to…
