---
type: "project"
title: "Show HN: Evaluation Context Protocol (ECP)"
project_url: "https://evaluationcontextprotocol.io/"
first_seen: "2026-09-21T02:53:01+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_aniketwattawmar
  - story_48734561
  - show_hn
lang: "en"
---

# Show HN: Evaluation Context Protocol (ECP)

> [!info] 一句话导读
> Evaluation Context Protocol ⌘K

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://evaluationcontextprotocol.io/>
> 首次收录：2026-09-21T02:53:01+08:00
> 来源渠道：HN Show HN
> 标签：author_aniketwattawmar, story_48734561, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:29:55+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/b5f3659625361aee_Show-HN-Evaluation-Context-Protocol-(ECP)]] |
| 2026-09-21T02:53:01+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/b5f3659625361aee_Show-HN-Evaluation-Context-Protocol-(ECP)]] |

## 摘要正文

Evaluation Context Protocol ⌘K Home Protocol Specification Python SDK CLI Tool Examples Community v0.7.0 · JSON-RPC 2.0  Portable evaluations  for AI agents.  ECP is a vendor-neutral protocol for testing agent outputs, tool calls, and evaluator-visible audit context — across frameworks, models, eval platforms, and CI systems.  Get started Read the spec GitHub terminal  $ pip install "ecp-runtime==0.7.0" "ecp-sdk==0.7.0"  $ ecp init  $ ecp run --manifest ecp_eval/manifest.yaml --json # 3 scenarios · 7 graders · all passed ✓  The evaluation contract layer  MCP is for tools. ECP is for evals. MCP gives agents a common way to use tools. ECP gives evaluators a common way to inspect what an agent returned, what tools it used, and what audit evidence it exposed — independent of the framework that built the agent or the platform that runs the test. What ECP checks  Beyond the final answer.  Most evals start with the final answer. ECP also checks the behavior behind it. public_output Did the user-visible answer satisfy the task? tool_calls Did the agent call the required tool with the right arguments? evaluation_context Did the agent expose evaluator-safe audit evidence? ecp run --manifest …
