---
type: "corpus"
item_id: "dc9027c55bef1170"
title: "Show HN: Jylus – give AI systems evidence from changing data."
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49886404"
project_url: "https://jylus.ai/try"
author: "JoshJH"
published_at: "2026-09-29T00:33:11Z"
captured_at: "2026-09-29T09:42:55+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-29"
pub_day: "2026-09-29"
tags:
  - 语料
  - hn_show
  - author_JoshJH
  - story_49886404
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Jylus – give AI systems evidence from changing data.

> [!info] 一句话导读
> ™ Platform Solutions Try Jylus Developers Pricing

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49886404>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：JoshJH　|　发布：2026-09-29T00:33:11Z
> 项目链接：<https://jylus.ai/try>
> 采集：2026-09-29T09:42:55+08:00　|　id：`dc9027c55bef1170`

## 正文

™ Platform Solutions Try Jylus Developers Pricing
 Log in Start free Menu
 Developer workload access
 Test Jylus with your workload.
 Send logs, OpenTelemetry, Docker events, telemetry or awkward JSON. Measure ingest, retrieval and proof-bound Context Packs with your own data.
 Get a free API key → Read developer docs
 Using an AI coding agent? Give it the Jylus quickstart and let it wire the first event, query and Context Pack into your application.
 Open agent quickstart →
 No credit card No sales call Your data stays yours Never used to train general-purpose AI
AI / AGENTS Test better evidence.
 Ingest evidence, generate a proof-bound Context Pack, then compare model input and answers on your workload.
 Test AI evidence → AI quickstart
 DATA / REAL-TIME SYSTEMS Push the data engine.
 Send events, search retained history and test mixed structured, semantic and relationship queries.
 Test the data engine → API quickstart
Measured native stack 50.695% QASPER NDCG@10 75.130% QASPER Recall@10 36.443% FinQA execution 40.048% live TEMPO NDCG@10 Methodology →
 Free storage 1 GB
 Ingest capacity 1,000 events/sec
 Data region Sydney, Australia
 Access HTTPS API
Single-use trial
 Drop in data. Get a proof-bound result.
 No account is required. Jylus creates an isolated one-time tenant, compiles the result, blocks further access immediately, and sends the tenant through the deletion lifecycle.
 Start with a synthetic example: State over time Missing information Conflicting records Late correction
 Text, JSON or log file Maximum 32 KB. The browser reads the file into the field below.
 Data JSON: use an array or one object per line. Text: leave a blank line between records; start with [YYYY-MM-DD] to preserve the date. Dated log lines are separate records.
 Question
 State as of (UTC, optional)
 State effective as of (UTC, optional)
 Evidence known as of (UTC, optional)
Use these together to separate what happened from what was known at the time. Run single-use trial
 RESULT Your compiled evidence will appear here. The response contains source-backed facts, proof IDs, conflicts, missing evidence and the deletion state.
Test AI evidence
 See what your model gets when the evidence improves.
 Use your own current state, history and documents. Jylus returns a bounded Context Pack with facts, timeline evidence, contradictions, freshness and proof IDs.
 01 Send data Use real records, including irrelevant history and conflicting values.
 02 Ask Jylus for evidence Call /api/v1/analyze with the question your model needs answered.
 03 Inspect the Context Pack Check retained facts, proof IDs, token estimate, completeness and execution time.
 04 Compare against your model Run the same question with your current context path and the Jylus evidence.
 Generate your first Context Pack →
 QASPER · 1,335 TEST QUERIES 50.695% NDCG@10 75.130% Recall@10 · 45.663% MRR@10
 NATIVE JYLUS STACK FINQA · 1,147 TEST CASES 36.443% execution accuracy 31.473% program accuracy · zero model calls
 TEMPO · FULL LIVE API COHORT 40.048% NDCG@10 Measured on the native Jylus stack. QASPER uses the untouched mteb/QASPER test task. FinQA uses the official program executor. TEMPO is the full 1,730-question public-v1 API result. Metrics measure different tasks and are reported separately.
The complete test loop
 Ask for evidence. Inspect exactly what your model receives.
The response keeps facts, temporal evidence, contradictions, missing evidence and proof IDs explicit. Efficiency values are measured from your own request.
CONTEXT PACK REQUEST POST /api/v1/analyze
 curl https://api.jylus.ai/api/v1/analyze \
 --request POST \
 --header "Authorization: Bearer $JYLUS_READ_API_KEY" \
 --header "Content-Type: application/json" \
 --data '{
 "source": "current",
 "text": "What is the latest latency reported by edge-17?",
 "vector": {
 "text": "latest edge device response time"
 },
 "context": {
 "mode": "decision",
 "token_budget": 2000,
 "max_facts": 18,
 "max_timeline": 12,
 "include_documents": false
 },
 "scan_limit": 1000,
 "limit": 24,
 "include_results": false
 }' YOUR DATA + YOUR QUESTION Use a read-scoped API key.
 ABRIDGED EXAMPLE RESPONSE application/json
 {
 "success": true,
 "complete": true,
 "execution_mode": "native_current",
 "context": {
 "decision_context_id": "ctx_...",
 "decision_readiness": {
 "status": "ready",
 "can_answer": true
 },
 "facts": [
 {
 "statement": "edge-17 reported 12.4 ms latency",
 "proof_ids": ["evt_001"]
 }
 ],
 "timeline": [
 { "observed_at": "2026-08-21T08:00:00Z", "proof_ids": ["evt_001"] }
 ],
 "contradictions": [],
 "missing_evidence": [],
 "context_efficiency": {
 "source_tokens_estimated": 1842,
 "retained_evidence_tokens_estimated": 436,
 "estimated_token_reduction_percent": 76.33
 },
 "proof": { "event_ids": ["evt_..."], "complete": true }
 }
} PROOF-BOUND EVIDENCE Your measured values depend on the data you send.
Test the data engine
 From account to a real event in minutes.
 01 Create a free workspace Email, GitHub or Google. No payment step.
 02 Copy the one-time API key The key is scoped and shown once.
 03 Send your real payload The Developer hub includes HTTPS, NATS JetStream, Docker and OpenTelemetry setup.
 Create free workspace →
 FIRST EVENT curl
 curl https://api.jylus.ai/api/v1/events \
 -H "Authorization: Bearer $JYLUS_API_KEY" \
 -H "Idempotency-Key: try_evt_001" \
 -H "Content-Type: application/json" \
 -d '{
 "stream": "my-workload",
 "events": [{
 "id": "evt_001",
 "type": "telemetry.sample",
 "occurred_at": "2026-08-21T08:00:00Z",
 "data": { "device": "edge-17", "latency_ms": 12.4 }
 }]
 }' 202 ACCEPTED Use the awkward workload, not the easy one.
™ The governed evidence and state layer for enterprise AI.
Platform
 Evidence & state Ingest infrastructure
 Company
 About Jylus Security Platform status Privacy Service terms Subprocessors Data processing Support Contact sales
 Developers
 Documentation API reference Try Jylus API access Quickstart Log in
© 2026 Jylus. All rights reserved. Built for the speed of AI.

## 关联链接

- https://api.jylus.ai/api/v1/analyze
- https://api.jylus.ai/api/v1/events

## 导航

- 项目页：[[10-项目/jylus.ai_89205c54]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
