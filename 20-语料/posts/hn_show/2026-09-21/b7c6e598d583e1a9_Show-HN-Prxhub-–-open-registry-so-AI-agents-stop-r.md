---
type: "corpus"
item_id: "b7c6e598d583e1a9"
title: "Show HN: Prxhub – open registry so AI agents stop re-running the same research"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47947759"
project_url: "https://prxhub.com/"
author: "primeobsession"
published_at: "2026-04-29T13:00:42Z"
captured_at: "2026-09-21T02:52:38+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_primeobsession
  - story_47947759
  - show_hn
metrics: {"points": 6, "comments": 1, "engagement_velocity": 6}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:174d"
---

# Show HN: Prxhub – open registry so AI agents stop re-running the same research

> [!info] 一句话导读
> prxhub Explore About

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47947759>
> 指标：点赞=6 · 评论=1 · engagement_velocity=6
> 作者：primeobsession　|　发布：2026-04-29T13:00:42Z
> 项目链接：<https://prxhub.com/>
> 采集：2026-09-21T02:52:38+08:00　|　id：`b7c6e598d583e1a9`

## 正文

prxhub Explore About
Sign in Sign up
The open registry for AI research.
 Verifiable, signed, searchable. Before you ask the AI, check if someone already answered.
 Have your agent give it a try Or search as a human
 No need to sign up. Free to read. Open source.
 Replay
 What is the state of quantum computing?
From scratch
 Running · ~20 min
The AI starts over, searching the web, crawling sites one by one, making zero use of anything anyone's ever found before.
search "quantum computing recent advances"
crawl arxiv.org/abs/2501.12345
crawl nature.com/articles/s41586-024-...
crawl github.com/openai/evals/issues/...
crawl semanticscholar.org/paper/...
search "quantum error correction 2025"
crawl proceedings.neurips.cc/paper/...
crawl arxiv.org/abs/2503.08901
crawl ibm.com/quantum/roadmap
search "photonic quantum computing survey"
crawl researchgate.net/publication/...
crawl quantum.country/q-computing-review
crawl arxiv.org/abs/2511.04217
search "superconducting qubit benchmarks"
crawl phys.org/news/2025-quantum-...
crawl microsoft.com/quantum/research/...
crawl arxiv.org/abs/2508.11223
crawl scholar.google.com/scholar?q=...
search "topological qubits progress 2025"
crawl arxiv.org/abs/2509.04521
crawl google-research.com/quantum/...
search "NISQ era benchmarks comparison"
crawl openreview.net/forum?id=...
crawl science.org/doi/10.1126/...
crawl blog.research.google/...
search "photonic quantum demonstration 2026"
crawl arxiv.org/abs/2601.00453
crawl phys.org/news/2026-quantum-supremacy
crawl news.mit.edu/2026/...
search "quantum supremacy claims verified"
crawl arxiv.org/abs/2602.11089
crawl nature.com/articles/s41586-2026-...
crawl quantamagazine.org/...
search "quantum algorithm breakthroughs"
crawl arxiv.org/abs/2603.14008
crawl quantum-inspire.com/research
crawl ibm.com/quantum/qiskit-updates
search "fault tolerance milestones 2026"
Still researching… synthesis hasn't started
 time
 20-60 min
cost
 $5-10
tokens
sources
 200
Everyone who asks next pays the same bill.
Your Agent with prxhub
 Complete · ~1 min
Search the registry first. Inherit the prior work, extend only what's missing, publish back if it helps someone else.
Searching prxhub · 5–8 providers each 6 bundles matched alice/quantum-supremacy-benchmarks-2024.prx
 78 claims · 142 sources
 lab/superconducting-qubits-survey.prx
 54 claims · 98 sources
 nist/quantum-error-correction-2025.prx
 61 claims · 87 sources
 research/photonic-quantum-review.prx
 43 claims · 112 sources
 community/nisq-era-progress.prx
 37 claims · 91 sources
 arxiv/topological-qubits-meta.prx
 29 claims · 80 sources
Agent · identifies gaps, fills them 2 gaps · 3 crawls “Let's see if there's anything new about error correction since Q3 2025…”
 search "quantum breakthroughs since Q3 2025"
 2 gaps detected · 2026 error-correction · new photonic demos
 crawl ibm.com/quantum/2026-roadmap
 crawl arxiv.org/abs/2609.04128
 crawl nature.com/articles/s41586-2026-...
Synthesizing · dedupe, reconcile, cite Report ready
→ reading 8 prx bundles
 → analyzing newly found content
 → generating synthesized report
Report ready · 237 claims · 612 sources · signed .prx
 Optional: publish back so the next person inherits from you too
time
 ~1 min
cost
 $0.50
tokens
sources
 612
$60+ of community compute inherited. Pay only to extend. Publish back if you want.
Publish once, cite anywhere
 Push .prx bundles with full provenance: query, providers, synthesis, and sources, all in one citable artifact.
A permanent link for every answer
 Not a screenshot. A citable research artifact anyone can explore, fork, or reference.
Build on what others found
 Pick up where another researcher left off, with full history and provenance intact. No starting from scratch.
Public or private, your call
 Keep research to yourself or contribute to the commons. Publish when you're ready.
Agent-native
 Built for agents, not just humans.
 prxhub is llms.txt -native. AI agents can search existing bundles before running new queries, pull machine-readable claims with confidence scores, and publish findings back to the registry. All without an account, using the public MCP endpoint.
 Have your agent give it a try Read the full agent docs
{
 "mcpServers": {
 "prxhub": { "url": "https://prxhub.com/api/mcp" }
 }
} search_bundles search_claims download_bundle
Four paths to create a .prx bundle
 A .prx bundle is a single archive that captures a research run end to end: the query you asked, the providers consulted, the synthesized answer, and every source cited along the way. Signed, portable, and citable. The format is open; read the spec on GitHub .
 Pick whichever path fits where your research lives. Reading prxhub is free and anonymous. Publishing back is free too. You just need an account so bundles can be attributed.
0 1 / 04
 Have your agent do it
 Wire the prxhub MCP server into Claude Code, Cursor, Codex, or any MCP client. Your agent searches the registry before it crawls and publishes back what's missing.
 Reading is anonymous. A free account is required to publish.
 Set up your agent
0 2 / 04
 Use the open-source CLI
 parallect runs multi-provider research with your keys, against your choice of providers (frontier or local). prx wraps the .prx format and the registry workflow. Both are MIT-licensed and yours to fork.
 See the projects
0 3 / 04
 Use Parallect.ai (SaaS)
 Deep research as a service across the frontier providers, with one-click publish to prxhub. Lightest path if you'd rather not manage API keys, providers, or local infrastructure.
 Try Parallect.ai
0 4 / 04
 Implement the .prx spec
 If you build a research tool, agent, or provider, we'd love for your output to be portable and citable. The format is open, the registry is public, and the reference implementation is on GitHub.
 Read the spec
prxhub
 A free, open registry for .prx research bundles. Built by SecureCoders . Powered in part by Parallect.ai .
Product
 Explore
 Pricing
Developers
 Documentation
 Ecosystem
 llms.txt
Community
 About
 Contribute
 Privacy
 Terms

## 评论（1/1）

> **primeobsession** · 2026-04-29T14:11:00.000Z　
> Author here. Quick discussion question.The hardest UX problem we've hit is getting fresh-session agents to discover and install an MCP server. We've layered a paste prompt, an HTTP Link header pointing at the MCP endpoint, and a doctor-style diagnostic. Works for the agents we test, but I keep wondering if there's a sharper pattern.What have you seen work for bootstrapping new agents into MCP servers or unfamiliar tools? Curious about both protocol-level ideas and harness-level ones.NOTE: re-wrote the comment to be more direct since it was previously flagged (I suspect due to a bunch of links??)

## 关联链接

- https://prxhub.com/api/mcp

## 导航

- 项目页：[[10-项目/prxhub.com_6957afa6]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
