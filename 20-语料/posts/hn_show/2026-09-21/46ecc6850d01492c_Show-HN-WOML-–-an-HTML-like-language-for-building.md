---
type: "corpus"
item_id: "46ecc6850d01492c"
title: "Show HN: WOML – an HTML-like language for building workflows"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49510333"
project_url: "https://woml.org/"
author: "dalibenothmen"
published_at: "2026-08-31T14:38:42Z"
captured_at: "2026-09-21T03:11:21+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - hn_show
  - author_dalibenothmen
  - story_49510333
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:52d"
---

# Show HN: WOML – an HTML-like language for building workflows

> [!info] 一句话导读
> < woml /> Quick Start Documentation Examples Search WOML ⌘ K View on GitHub

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49510333>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：dalibenothmen　|　发布：2026-08-31T14:38:42Z
> 项目链接：<https://woml.org/>
> 采集：2026-09-21T03:11:21+08:00　|　id：`46ecc6850d01492c`

## 正文

< woml /> Quick Start Documentation Examples Search WOML ⌘ K View on GitHub
Workflow Orchestration Markup Language
 If you can read HTML, you can use WOML to automate anything, literally anything.
 WOML is an open, executable format for durable workflow applications. Write workflow structure like HTML, use JavaScript whenever you need real logic, and run it anywhere—with reliable execution, deployment, inspection, control, and recovery built in.
curl npm bun pnpm
 $ curl -fsSL https://woml.org/install | bash Copy
 $ npm install --global woml-cli Copy
 $ bun add --global woml-cli Copy
 $ pnpm add --global woml-cli Copy
What WOML is
 Workflow applications as readable documents.
WOML is an HTML-inspired language and self-hosted runtime for durable automation. Open a .woml file and its triggers, steps, decisions, approvals, and execution policy read from top to bottom. Run that same file and WOML turns it into an operational workflow backed by real JavaScript and a durable engine.
 The source is not an export of the workflow. It is the workflow.
How WOML works
 From readable workflow to durable execution.
 Write the structure in a .woml file, start it from a trigger or command, and let WOML execute each step while preserving the decisions and results needed to inspect, control, and continue the run.
workflow.woml Writing workflow Readable source Real JavaScript One executable document Terminal Waiting for source $
Validate Activate Execute durably
 The document you write is the workflow WOML validates, activates, and executes.
The idea in one file
 The graph gets crowded. The source stays clear.
 A visual builder looks clean in the demo and turns into spaghetti in production. The same workflow in WOML is just text, linear, searchable, and diffable no matter how big it gets. Growth adds lines to a file, not tangles to a canvas.
process-order.woml writing WOML

 Linear Searchable Diffable
 Visual workflow builder Waiting for workflow structure
With every node, readability drops and maintenance multiplies.
Beyond the connector catalog
 Your workflow shouldn't stop at “integration unavailable.”
 Sooner or later, every no-code platform tells you "not supported" and your automation stops at the edge of someone else's roadmap. WOML has no edge. Any API, any library, any custom logic becomes a capability you define yourself and call like it shipped with the tool. Your workflow's limits are yours, not the platform's.
workflow.woml google-maps.ts local module · explicit import

  Define the capability Import it explicitly Keep building
 Visual workflow builder Choose the next node
 Search integrations
 Google Maps isn't available yet. Request this integration and wait for a future release. We'll notify you when it's ready.
Waiting for the platform
Only available integrations become nodes. Google Maps never reaches the canvas, while the WOML files beside it already contain the missing capability.
 In this workflow, google-maps.ts becomes services.googleMaps . The source names the dependency, the graph keeps its vertical sequence, and the third step no longer depends on someone else's integration roadmap.
Not just a syntax
 One file. The whole workflow system.
 WOML keeps the definition, execution, and operation of a workflow connected. Describe it once in a readable .woml file, then let the engine run it and the runtime give you the controls to operate it reliably.
Source of truth WOML
 < .woml />
One readable, executable definition.
 01 Describe
 Readable language
 Describe workflow structure like a document. Use JavaScript wherever the logic needs real code.
02 Execute
 Durable engine
 Execute the same file as a reliable workflow application—not as a diagram or static configuration.
03 Operate
 Operational runtime
 Deploy, inspect, control, and recover workflows through a runtime that understands their definition.
One file, many responsibilities
 The same artifact remains useful from the first idea to production operation.
Program What executes
 Architecture diagram How work connects
 Automation configuration What the workflow needs
 Execution policy How it runs
 Documentation What people understand
 Shared artifact What developers and AI agents create, review, and run
The diagram, the code, the configuration, and the production workflow never drift apart. In WOML, they are the same artifact.
Built to grow
 Start with one workflow. Grow into a system.
 Begin with one .woml file and one useful automation. As the work expands, add decisions, concurrent work, approvals, state, and services inside the workflow—or compose it with other WOML workflows that return results, continue independently, or react to durable events. The system gets bigger without hiding its structure.
Primary workflow customer-onboarding.woml 01 Trigger New customer
02 Validate customer Check required data
03 Parallel checks Call two workflows for results
04 Choose onboarding route Branch from customer context
05 Wait for approval Pause for a durable decision
06 Store progress Keep durable workflow state
07 Coordinate workflows Start work and publish an event
Call · returns result risk-assessment.woml
 Risk score returned Call · returns result identity-verification.woml
 Identity result returned Start · independent welcome-sequence.woml
 Continues on its own Event · customer.ready crm-sync.woml
 Subscriber activated Event · customer.ready customer-analytics.woml
 Subscriber activated
Scale by adding structure when it belongs together, and new workflows when it does not.
 A workflow can call another for a result, start it independently, or publish an event to multiple subscribers. Every part remains a readable .woml document.
Executable examples
 See these applications take shape as readable source.
 Explore complete .woml files that combine workflow structure, JavaScript, services, state, decisions, and human input.
View all examples
01 .woml

 Business Parallel Approval
 Orchestrate high-value order fulfillment
 Validate orders, check inventory and fraud concurrently, route risky purchases to a durable human decision, and publish one auditable outcome.
 View example
 02 .woml

 Data For each PostgreSQL
 Import thousands of customers with durable per-row progress
 Validate a dataset, process up to ten thousand customers with bounded concurrency, upsert valid rows, and preserve ordered results.
 View example
 04 .woml

 Human operations Approval Storage
 Automate expense compliance without hiding the human decision
 Apply deterministic expense policy, archive receipts, share one approval across providers, and publish the accounting decision.
 View example
 05 .woml

 Backend Webhook Idempotency
 Process payment webhooks into an idempotent ledger
 Turn repeated payment deliveries into an idempotent ledger, exact event routing, and independently durable fulfillment work.
 View example
 06 .woml

Content AI Fork
 Research, approve, and distribute content from one workflow
 Research and draft with AI, wait for editorial approval, then publish through independent multi-step channel branches.
 View example
 09 .woml

 const db = services.db ({
 Local SQLite Schedule
 Generate a local operations report with no cloud account
 Query local SQLite, calculate metrics in JavaScript, generate CSV, and store a versioned report without a cloud account.
 View example
 10 .woml

 Platform Workflow calls AI
 Build a multi-workflow document processing API
 Expose one product endpoint and route tenant jobs to independently durable invoice, contract, and summarization workflows.
 View example
 11 .woml

 const response = await services.http.request ({
 Interval Parallel HTTP
 Monitor services in parallel
 Check several live endpoints on one durable interval, then turn their individual results into one readable health report.
 View example
 12 .woml

 Webhook Approval Durability
 Hold an order for human approval
 Accept a validated order webhook, pause durably for a decision, and make the approved and rejected paths explicit.
 View example
 13 .woml

 {
 "type" : "object" ,
 "required" : [ "customerId" , "change" ],
 "properties" : {
 "customerId" : { "type" : "string" },
 "change" : { "type" : "string" }
 Events SQLite Validation
 Record customer events in SQLite
 Subscribe to an internal event, validate its payload, and write an auditable record through WOML’s supervised database service.
 View example
WOML vs Alternatives
 Most workflow tools optimize for either visual simplicity or engineering power. WOML is designed to keep both: readable workflow structure for the whole team and real JavaScript whenever the automation needs it.
Tool How you build workflows Readable by the whole team Self-hosted Logic without a ceiling
 WOML Markup + JavaScript ✅ Clear, document-like structure ✅ ✅ Inline JavaScript, modules, and services
 n8n Visual canvas ⚠️ Easy at first; harder as the canvas grows ✅ ⚠️ Code and custom nodes
 Zapier Visual canvas ⚠️ Friendly for smaller automations ❌ ⚠️ Platform actions and code steps
 Temporal Code with language SDKs ❌ Primarily readable by engineers ✅ ✅ Full programming languages
 AWS Step Functions JSON/YAML with ASL ❌ Requires ASL and AWS knowledge ❌ ⚠️ Extended through AWS services and functions
 Apache Airflow Python DAGs ❌ Primarily readable by Python/data teams ✅ ✅ Python and operators
WOML's difference: it combines document-like readability, self-hosted ownership, and full JavaScript flexibility in the same workflow file.
 One readable file. A durable runtime behind it.
 Get started Read the documentation
< woml /> Quick Start Documentation Examples GitHub
 © 2026 WOML
 Back to top ↑

## 关联链接

- https://woml.org/install

## 导航

- 项目页：[[10-项目/woml.org_2f420815]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
