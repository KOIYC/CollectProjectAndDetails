---
type: "corpus"
item_id: "b5f3659625361aee"
title: "Show HN: Evaluation Context Protocol (ECP)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48734561"
project_url: "https://evaluationcontextprotocol.io/"
author: "aniketwattawmar"
published_at: "2026-06-30T15:56:33Z"
captured_at: "2026-09-21T02:53:01+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_aniketwattawmar
  - story_48734561
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: Evaluation Context Protocol (ECP)

> [!info] 一句话导读
> Evaluation Context Protocol ⌘K

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48734561>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：aniketwattawmar　|　发布：2026-06-30T15:56:33Z
> 项目链接：<https://evaluationcontextprotocol.io/>
> 采集：2026-09-21T02:53:01+08:00　|　id：`b5f3659625361aee`

## 正文

Evaluation Context Protocol ⌘K
Home Protocol Specification Python SDK CLI Tool Examples Community
v0.7.0 · JSON-RPC 2.0
 Portable evaluations
 for AI agents.
 ECP is a vendor-neutral protocol for testing agent outputs, tool calls, and evaluator-visible audit context — across frameworks, models, eval platforms, and CI systems.
 Get started Read the spec GitHub
terminal
 $ pip install "ecp-runtime==0.7.0" "ecp-sdk==0.7.0"
 $ ecp init
 $ ecp run --manifest ecp_eval/manifest.yaml --json
# 3 scenarios · 7 graders · all passed ✓
 The evaluation contract layer
 MCP is for tools. ECP is for evals.
MCP gives agents a common way to use tools. ECP gives evaluators a common way to inspect what an agent returned, what tools it used, and what audit evidence it exposed — independent of the framework that built the agent or the platform that runs the test.
What ECP checks
 Beyond the final answer.
 Most evals start with the final answer. ECP also checks the behavior behind it.
public_output Did the user-visible answer satisfy the task?
tool_calls Did the agent call the required tool with the right arguments?
evaluation_context Did the agent expose evaluator-safe audit evidence?
ecp run --manifest Can this run in CI and fail a build?
Runs anywhere
 Run evals locally or wire ecp run into your CI. Exits non-zero on failure, so a regression breaks the build.
Framework neutral
 Wrap agents built with plain Python, LangChain, LlamaIndex, CrewAI, or PydanticAI behind one evaluation contract.
JSON-RPC contract
 Implement the protocol in any language: agent/initialize, agent/step, agent/reset over stdio or Streamable HTTP.
Works with
 Your existing agent stack.
Plain Python LangChain LlamaIndex CrewAI PydanticAI Streamable HTTP
 Start grading agents in five commands.
 Install the runtime, initialize a starter manifest, and run your first eval.
 Quickstart Read the docs
Evaluation Context Protocol · Open source
 Spec Quickstart GitHub

## 导航

- 项目页：[[10-项目/evaluationcontextprotocol.io_b73c096e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
