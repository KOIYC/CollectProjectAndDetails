---
type: "corpus"
item_id: "dd959b5eb29ce0ad"
title: "Show HN: OpsGraph – evidence-first PostgreSQL investigations"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49753339"
project_url: "https://opsgraph-site-seven.vercel.app/"
author: "arittrabag"
published_at: "2026-09-18T12:20:20Z"
captured_at: "2026-09-20T09:36:40+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - hn_show
  - author_arittrabag
  - story_49753339
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: OpsGraph – evidence-first PostgreSQL investigations

> [!info] 一句话导读
> OpsGraph — Evidence-first PostgreSQL investigations

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49753339>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：arittrabag　|　发布：2026-09-18T12:20:20Z
> 项目链接：<https://opsgraph-site-seven.vercel.app/>
> 采集：2026-09-20T09:36:40+08:00　|　id：`dd959b5eb29ce0ad`

## 正文

OpsGraph — Evidence-first PostgreSQL investigations

# Ask PostgreSQL. Inspect the evidence.

 OpsGraph is a self-hosted investigation workspace for one operator. Your model plans bounded, read-only queries. Application policy controls their execution.

Built for evaluation on an authorized, non-sensitive PostgreSQL test database. Not production-ready.

 Self-hosted Read-only PostgreSQL External inference off by default One operator

Policy-controlled investigation

 Recorded execution inspectable

1. 01

Scope checked Approved tables + playbook
2. 02

Query planned Model proposes bounded SQL
3. 03

Policy enforced Read-only limits before execution
4. 04

Evidence retained SQL, rows, source + limits

 SELECT … LIMIT 100 5s timeout

 MODEL PROPOSES• APP VALIDATES• POSTGRESQL STAYS READ-ONLY• EVIDENCE REMAINS INSPECTABLE• OPERATOR DECIDES

## Evidence before certainty.

A citation does not make a conclusion true. OpsGraph keeps the work inspectable so you can review what was actually queried and captured before you act.

### See what happened

Open referenced evidence to inspect the query, source, collection time, captured rows and limits behind a finding.

Recorded execution

### Keep access bounded

Choose explicit schema-qualified tables and use a dedicated read-only role. The model cannot grant itself access or make database changes.

Policy before execution

### Keep the investigation

Reopen history, export evidence, retry failed work with fresh queries, or ask a linked follow-up while earlier evidence remains unchanged.

Saved local history

The boundary is part of the product

## The model does not get the keys.

The model can plan. OpsGraph validates and executes inside explicit application policy. Database permissions remain the final authority.

 SELECT only Approved tables Role checks Read-only transactions

Current beta defaults allow up to three queries, 100 captured rows per query, and five seconds per query. Playbooks may be stricter.

execution_boundary.policy ENFORCED

database_action SELECT allowed

table_scope approved only checked

query_budget 3 max bounded

row_capture 100 / query bounded

statement_timeout 5 seconds bounded

INSERT / UPDATE / DELETE denied blocked

 Application policy controls execution — not the model.

## Ask. Bound. Capture. Review.

The workflow is intentionally narrow. OpsGraph does not silently invent sample answers, download models, or remediate your database.

### Ask a concrete question

Pick a source and playbook. Start with a question whose columns and meanings you actually know.

### Plan inside a scope

Your configured model proposes bounded queries against tables you explicitly approved.

### Execute read-only

AST validation, role checks, approved-table scope and read-only transactions gate execution.

### Inspect the evidence

Compare the answer with captured rows and SQL. Review missing evidence and limitations before acting.

## The answer stays attached to its work.

A saved investigation can be reopened later. Findings, cited evidence, captured records and limitations remain inspectable, while follow-ups collect fresh evidence.

 SQL inspectable Rows captured Limits recorded Follow-up fresh queries

opsgraph / investigation

Saved investigation from beta validation · test data only

## Local when you want it. Explicit when it leaves the machine.

Use Ollama locally, configure another OpenAI-compatible endpoint, or connect Anthropic with explicit external-data permission. OpsGraph does not download model weights for you.

### Ollama

Tested local path. Keep model inference on your own machine when that fits your workflow.

### OpenAI-compatible

Point OpsGraph at an endpoint you operate or trust. Provider access stays explicit.

### Anthropic

External inference is opt-in. Review data handling before connecting source records.

## Choose the path that matches what you are doing.

If you are evaluating OpsGraph, the offline bundle is the shortest path. If you want to modify or contribute, use the source checkout with uv.

Evaluating? Use the beta bundle. CPython 3.11 is required; the bundle carries the app and locked dependencies, not the interpreter.

Contributing? Use the source path. Python 3.11–3.13 + uv gives you the editable environment, tests and build workflow.

 Bundle Source Docker

Best for trying the beta without a development checkout.

```
# Download the matching v0.1.0b1 bundle + .sha256
# macOS / Linux
python3.11 -I Install.py install
python3.11 -I Install.py launch

# Windows
py -3.11 -I Install.py install
py -3.11 -I Install.py launch
```

Open release assets ↗

Best for contributors and people who want the source workflow.

```
git clone --branch v0.1.0b1 --single-branch \
  https://github.com/Arittra-Bag/opsgraph.git
cd opsgraph
uv sync --locked --all-extras
uv run opsgraph launch --configure
```

PostgreSQL and model services remain separate. Configure container-reachable addresses first.

```
docker pull ghcr.io/arittra-bag/opsgraph:beta

# Or from the checkout
 docker compose --env-file .env \
  -f deploy/compose.yaml up --build -d
```

## Useful enough to evaluate. Narrow enough to be honest about its limits.

Beta 1 is a prerelease for public validation. Native installer lifecycles are checked on macOS, Ubuntu and Windows, but validation depth differs by platform. The Docker image has configuration and health checks; a complete container investigation workflow is not yet claimed as verified.

Public validation is open

## Try it on a non-sensitive test database. Challenge the evidence model.

The most useful feedback is technical: execution boundaries, evidence quality, installation friction and operator workflow.

## 关联链接

- https://github.com/Arittra-Bag/opsgraph.git

## 导航

- 项目页：[[10-项目/opsgraph-site-seven.vercel.app_b98f7d63]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
