---
type: "corpus"
item_id: "a3d2b4a6ee7b57b8"
title: "Show HN: Scalix World – AI native Neo cloud built by two engineers in Rust"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49109227"
project_url: "https://scalix.world/"
author: "kiran-ravi"
published_at: "2026-07-30T12:42:39Z"
captured_at: "2026-09-21T03:11:20+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-30"
tags:
  - 语料
  - hn_show
  - author_kiran-ravi
  - story_49109227
  - show_hn
metrics: {"points": 3, "comments": 5, "engagement_velocity": 3}
comments_count: 5
comments_total: 5
discovered_via: "hn:show_hn:83d"
---

# Show HN: Scalix World – AI native Neo cloud built by two engineers in Rust

> [!info] 一句话导读
> Scalix World Products Scalix Cloud

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49109227>
> 指标：点赞=3 · 评论=5 · engagement_velocity=3
> 作者：kiran-ravi　|　发布：2026-07-30T12:42:39Z
> 项目链接：<https://scalix.world/>
> 采集：2026-09-21T03:11:20+08:00　|　id：`a3d2b4a6ee7b57b8`

## 正文

Scalix World Products Scalix Cloud
 Managed cloud, one API key, one credit pool
 ScalixNova
 Serverless PostgreSQL with branching & PITR
 Scalix AI
 Scalix models, OpenAI-compatible endpoint
 Scalix Prime Early Access
 Graph-relational database
 Scalix Coder
 AI coding agent, 40 tools, free
 Scalix IDE
 AI-native desktop code editor
 Scalix Shield
 AI crawler control for your apps
 Scalix Functions
 Serverless with hardware-isolated microVMs
 Scalix Run
 Docker containers, auto-scaling
 Sandboxes
 Isolated environments for AI agents
 Computers
 Persistent Linux machines with real ssh
View Pricing
Docs Overview Quickstart API Reference CLI Reference All Documentation
Pricing GitHub Sign in Start free
The AI-native
 neocloud
 Scalix is the AI-native neocloud. Your database, AI, functions, storage, and compute, all on one platform. Just one key, one bill . And it speaks MCP , so your AI agents can set up, deploy, and run everything for you, not just write the code.
 Start building free Contact sales
 No credit card required to start.
 Start free. $1 in credits, AI inference included, no credit card.
Dedicated EU infrastructure · Built from London & Kerala
ScalixNova AI Inference Functions Scalix Run Storage Auth KV & Events Domains & SSL Sandboxes Scalix Shield Agent Tools (MCP)
AI Inference Database Deploy
 connected · eu-central
01 Agent-native AI agents operate the entire platform
Every Scalix service is exposed through the Model Context Protocol: 50 tools covering database, computers, services, storage, functions, KV, events, cron, domains, builds, and auth. Point any MCP client at api.scalix.world/v1/mcp , or call tools over plain HTTP. Agents provision infrastructure, query data, deploy services, and roll back releases through tool calls, with the same permissions and metering as any API key.
 Provision a database branch, run migrations, and query it, in one agent session
 Deploy and scale services, then roll back a bad revision
 Same API key, same audit trail, same credit pool as human usage
 Connect your agent MCP server docs
agent tool call one HTTP endpoint, any agent
 POST https://api.scalix.world/api/v1/mcp/call
 Authorization: Bearer sk_live_...
 {
 "name" : "scalix_db_query" ,
 "arguments" : { "sql" : "SELECT count(*) FROM orders" }
 }
 List every tool with GET /api/v1/mcp, or connect Claude Code, Cursor, or any MCP client to /v1/mcp. Your agent can call:
 scalix_db_query · scalix_db_sandbox · scalix_fn_deploy
 scalix_run_deploy · scalix_run_rollback · scalix_storage_upload …
02 Product family One platform. One neocloud.
 Each stands on its own. Together they make AI a first-class operator of your infrastructure.
Scalix Cloud
 The managed platform
From $0/mo
 Database, AI, functions, containers, storage, and auth: one API key, one credit pool, operable by humans and AI agents over MCP.
 Database AI Functions Containers Storage Auth KV Events Domains
 Open Console
 ScalixNova
 Own Rust engine
 Serverless PostgreSQL: database branching, PITR, scale-to-zero, query firewall.
 Learn more
Scalix AI
 One OpenAI-compatible endpoint, pay per token.
 Explore Scalix Prime
 Early Access SQL + Cypher, one transaction.
 Get access
 Scalix Coder
 Free
 AI coding agent for your terminal. 40 built-in tools, 4 permission modes, VS Code extension.
 Learn more
Scalix Shield
 New
 AI crawler control: allow, block, or rate-limit 49 known crawlers (43 AI + 6 search), with IP verification.
 Learn more
03 Why Scalix Built different, priced honest.
Infrastructure without markup
 Scalix runs on dedicated EU infrastructure that we operate ourselves, so no reseller margin on every layer. Transparent per-unit rates and free ingress on storage.
Security and compliance
 Designed for GDPR and India DPDP Act requirements. AES-256 encryption at rest, TLS 1.3 in transit, query firewall, EU data hosting.
Standard APIs, no lock-in
 PostgreSQL wire protocol. OpenAI-compatible AI endpoint. S3-compatible storage. Your code works with us and without us.
We engineered the stack ourselves, in Rust, on dedicated EU infrastructure. Read how Scalix is built →
04 Security Security on every plan
 Enforced at the gateway every request passes through, not added as an afterthought.
SSO & SAML
 Single sign-on for organizations. Available on Pro and above.
Audit logs
 Every console action, API call, and agent tool call recorded with actor, time, and origin.
WAF & rate limiting
 Web application firewall and per-key rate limits enforced at the gateway, before traffic reaches your services.
Scalix Shield
 AI crawler control for your apps: allow, block, or rate-limit 49 known crawlers across 6 categories, with IP verification.
Encryption everywhere
 AES-256 at rest, TLS in transit, and mTLS between platform services via our fleet CA.
GDPR & DPDP by design
 Designed for EU GDPR and India DPDP Act requirements. Data hosted on dedicated EU infrastructure.
05 Pricing One pool. Every service.
 Your plan price is your credit pool. All services draw from one balance.
Free
 $0
 $1 trial credit
 AI inference (free tier)
 1 project · 1 domain
 Community support
 Start Free
Starter
 $19 /mo
 $19/mo credit pool
 AI inference (broad catalog)
 5 projects · 3 domains
 Email support (48h)
 Get Starter
Popular
 Pro
 $49 /mo
 $49 credit pool + optional overage
 AI inference (broad catalog)
 20 projects · 10 domains
 Email support (24h)
 Get Pro
Team
 $149 /mo
 $149 credit pool + optional overage
 AI inference (broad catalog)
 Unlimited projects & domains
 Chat support (4h)
 Get Team
Business ($299/mo) and Enterprise (custom) also available. Contact sales →
From the blog
 All posts →
 Sovereignty
 Sovereignty Is Now Law, Not Sentiment
 Data residency went from preference to legal mandate. We built a cloud for the jurisdictions that enforce it.
 Launch
 Meet Scalix World: The AI-Native Neocloud
 After a year of building, we're taking Scalix World public: one platform AI agents can operate, on sovereign European infrastructure.
Get started with Scalix Cloud
 $1 free credit. No credit card. Start building in minutes.
 Get started free Documentation
 EU data hosting, designed for GDPR + DPDP PostgreSQL wire-compatible Agent-operable via MCP
Scalix World The AI-native neocloud.
Products
 Scalix Cloud ScalixNova Scalix AI Scalix Prime Scalix IDE Scalix Coder Scalix Shield
 Platform
 Functions Scalix Run Sandboxes Computers Storage Auth Pricing
 Developers
 Documentation API Reference CLI Reference MCP Server
 Company
 About Blog Research Newsroom Contact
 Legal
 Terms Privacy DPA Refund & Cancellation Security
Scalix Updates
 Launch news, benchmarks, changelog. Double opt-in, unsubscribe anytime.
Subscribe
 © 2026 Scalix World Pvt Ltd (CIN U72100KL2026PTC102006) · Energy FW Ltd (Co. No. 14600160) X LinkedIn Discord GitHub YouTube

## 评论（5/5）

> **Akhil0294** · 2026-07-30T13:23:45.000Z　
> Akhil here, the other engineer. I built the deployment layer and container runtime, so happy to answer anything about how deploys work, cold-start behaviour, or the boot path end-to-end. Containers boot in about 76ms on the default tier, and that's the part I'd most want people to poke holes in.

---

> **unavaneet** · 2026-07-30T13:37:54.000Z　
> I see your database tech is unique. Can i use Postgress 18 in Scalix Nova?

---

> **jithinjprasad** · 2026-07-30T15:59:56.000Z　
> Hi, I am using Scalix to host my personal website, and it's easy to use compared to how it was when I was using other services.

---

> **kishorekailas1** · 2026-07-30T19:38:38.000Z　
> I tried it out, I am able to use database, sandbox, computer and even send transaction emails via the console. The cloud MCP is perfect for agents. I have one doubt for the team, what's the real benefit for using enclave instead of nova?

---

> **kiran-ravi** · 2026-07-30T14:22:26.000Z　
> Yes, The database engine Scalix Nova speaks the Postgres wire protocol and runs 16, 17 and 18.

## 关联链接

- https://api.scalix.world/api/v1/mcp/call

## 导航

- 项目页：[[10-项目/scalix.world_1007714d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
