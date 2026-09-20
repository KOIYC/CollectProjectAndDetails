---
type: "corpus"
item_id: "5a64b4d9e62ae74c"
title: "Show HN: Figranium – Open-source visual Playwright control plane (Docker, API)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49110169"
project_url: "https://figranium.dev/"
author: "asernasr"
published_at: "2026-07-30T14:00:58Z"
captured_at: "2026-09-21T03:11:17+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-30"
tags:
  - 语料
  - hn_show
  - author_asernasr
  - story_49110169
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: Figranium – Open-source visual Playwright control plane (Docker, API)

> [!info] 一句话导读
> Docs Blog Templates Releases Integrations GitHub —

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49110169>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：asernasr　|　发布：2026-07-30T14:00:58Z
> 项目链接：<https://figranium.dev/>
> 采集：2026-09-21T03:11:17+08:00　|　id：`5a64b4d9e62ae74c`

## 正文

Docs Blog Templates Releases Integrations GitHub —
 Open menu Docs Discord Blog Templates Releases Integrations GitHub
Build complex browser workflows visually
Figranium is an open-source visual browser automation platform with a block-based editor, built-in scheduling, proxy rotation, and a REST API to run everything.
Get Started
 View on GitHub
Backed By
How It Works
 From drag-and-drop to API call
 Stack action blocks in a visual canvas, wire in control flow and variables, then trigger runs over HTTP or on a schedule.
01
 Design visually
 Drag action blocks onto the canvas -- click, type, scroll, navigate, extract, screenshot. Each block is a configurable step in your workflow.
02
 Add logic & variables
 Use if/else branches, while loops, foreach iteration, and {$variables} to build dynamic flows. Drop in JavaScript blocks for custom logic.
03
 Run via API or schedule
 POST to /api/tasks/:id/api with variables, or set a cron schedule. Get structured JSON results, screenshots, and video captures back.
Capabilities
 Everything ships in one binary
Visual editor, task scheduler, proxy manager, video capture, stealth evasions, and a full REST API -- no plugins required. Self-host on your own infrastructure and keep your data local.
Action Blocks
 Click, type, scroll, hover, press, select, navigate, wait, screenshot, and more. Plus control-flow blocks: if/else, while, foreach, repeat.
Built-in Scheduling
 Set tasks to run every X minutes, daily at a specific time, weekly, monthly, or with raw cron expressions. No external scheduler needed.
Proxy Rotation
 Import HTTP and SOCKS5 proxies, set a default, and enable round-robin or random rotation per task. Credentials supported.
Stealth & Anti-Detection
 Natural typing, cursor glide, idle movements, dead clicks, overscroll, fatigue simulation, and 13-point browser fingerprint evasion.
Captures & Recording
 Automatic screenshots and .webm video recording for every run. Browse captures in the dashboard with full playback.
Variables & Templating
 Define runtime variables and interpolate them anywhere with {$varName}. Nested access, reserved tokens like {$now}, and per-block output piping.
JavaScript Blocks
 Run arbitrary JS in the browser context for custom extraction, page manipulation, or data transformation between steps.
REST API
 Create, list, update, and execute tasks. Fetch execution history, manage schedules, and clear captures -- all via authenticated HTTP endpoints.
Use Cases
 Workflows that ship to production
 Build once in the visual editor, schedule or trigger via API. Every run produces structured output, captures, and execution logs.
 Read the docs
Data Extraction
 Navigate to pages, interact with dynamic content, and extract structured data using CSS selectors or JavaScript. Output as JSON or push directly to Baserow.
QA & Regression Testing
 Record multi-step user flows visually, schedule them to run on cron, and review video captures when assertions fail.
Lead Enrichment
 Chain multiple sites in a single workflow using variables. Collect public signals, merge results, and export structured records.
Price & Change Monitoring
 Schedule tasks to run daily or hourly. Compare extracted values across runs and pipe results to external systems via the API.
API
 Full REST API for every operation
 Authenticate with a Bearer token or x-api-key header. Create tasks, trigger runs with variables, poll execution status, manage schedules, and fetch captures -- all programmatically.
Execute POST /api/tasks/:id/api with runtime variables to trigger any saved workflow.
Manage CRUD tasks, list executions, create or delete cron schedules.
Collect Fetch execution history, structured JSON output, screenshots, and video recordings.
API Reference
Built for the real web
 Keep going when simple scripts stop
 Production browser automation has to survive challenge pages, authenticated portals, dynamic interfaces, and partial failures. Figranium makes those conditions part of the workflow instead of leaving you to patch around them.
Solve CAPTCHAs in the workflow
 Auto-detect reCAPTCHA, hCaptcha, and Turnstile after navigation, clicks, or typing. Use Figranium’s resource-aware local solver or connect a compatible remote provider, with sensitive browser context sharing kept opt-in.
Stay signed in across runs
 Complete login or MFA in the live headful browser, save the isolated browser profile, and reuse its cookies in scheduled, API-triggered, or agent-triggered workflows.
Recover and diagnose
 Combine selector-aware waits and on-error branches with execution queues, schedules, and webhooks. Inspect step logs, screenshots, video recordings, and run history when a site changes.
Agents & ecosystem
 One browser runtime for your whole stack
 Build a deterministic workflow once, then make it available to AI agents, application code, low-code automations, schedules, and webhooks.
 Explore integrations
MCP
 Give AI agents browser tools
 Connect compatible AI clients to create and run tasks, manage schedules, inspect results, and diagnose automation through the Figranium MCP server.
 Get the MCP server
JS / TS SDK
 Build typed browser automation
 Create tasks, pass runtime variables, follow execution progress, and manage the automation lifecycle from JavaScript or TypeScript.
 Explore the SDK
REST & integrations
 Connect the tools you already use
 Trigger any saved workflow over authenticated HTTP, connect it to n8n, or route results into custom apps, databases, and automation platforms.
 View the ecosystem
Free & self-hosted
 Run it on your infrastructure
 Figranium itself is free, GPLv3 open-source software with no platform credits or per-run fees. Deploy with Docker, keep data local, and protect access with sessions, API keys, rate limits, IP allowlists, and SSRF safeguards.
 Deployment guide
From authenticated reports to agent research
 Use Figranium for portal automation, price monitoring, QA journeys, lead enrichment, and scheduled file collection.
Browse templates
Open source, forever
 Self-host on your infrastructure. Audit the code, contribute features, or fork it. Node.js backend, React frontend, Playwright under the hood.
 Star on GitHub Read the Docs
Figranium
 Open-source browser automation control plane. Visual block editor, built-in scheduling, proxy rotation, stealth, and a full REST API. Self-host on your own infrastructure.
Blog
 Figranium 1.0 Is Coming And I’m Looking for Contributors Figranium Pro: Our Continued Commitment to Open Source Figranium v0.17: Cabinets, Uploads, and Stronger Release Qualification Figranium v0.16: Clearer Outcomes, a Redesigned App, and Better Controls Figranium Is Now an Official Verified n8n Node Figranium Now Supports CAPTCHA Solving View all blog posts
Navigate
 Home Docs Templates Discord GitHub
Figranium Deterministic Control for an Agentic World Privacy Policy • Terms of Service • © 2026 Figranium

## 导航

- 项目页：[[10-项目/figranium.dev_1c9153bb]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
