---
type: "corpus"
item_id: "8c74792d0d4add2a"
title: "Show HN: whenever.dev - Vercel and v0 for Workflows"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50255119"
project_url: "https://whenever.dev/"
author: "tprupsys"
published_at: "2026-10-27T05:51:17Z"
captured_at: "2026-10-27T23:46:32+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-27"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_tprupsys
  - story_50255119
  - show_hn
metrics: {"points": 3, "comments": 5, "engagement_velocity": 3}
comments_count: 5
comments_total: 5
discovered_via: "hn:show_hn:3d"
---

# Show HN: whenever.dev - Vercel and v0 for Workflows

> [!info] 一句话导读
> Deploy Templates Integrations Pricing Docs Compare

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50255119>
> 指标：点赞=3 · 评论=5 · engagement_velocity=3
> 作者：tprupsys　|　发布：2026-10-27T05:51:17Z
> 项目链接：<https://whenever.dev/>
> 采集：2026-10-27T23:46:32+08:00　|　id：`8c74792d0d4add2a`

## 正文

Skip to content
 Deploy Templates Integrations Pricing Docs Compare
 Sign in Start building
Deploy Templates Integrations Pricing Docs Compare
 Sign in Start building Keep the team in sync Sort incoming mail Track new orders Summarize refunds Update your contacts Organize your notes Keep reports current Follow up on leads Triage new issues Sync your records Plan the week Keep sales up to date
 The platform for AI workflow automation .
 Build, deploy, and run deterministic flows, AI steps, and full agents in one place.
 Build workflow
 Deploy from your agent
No credit card required. Deploy from Claude Code, Codex, or Cursor.
Acknowledge contact form leads within minutes Ready Run Turn on
Workflow 01 TRIGGER Typeform New contact form response
02 Google Sheets Log the lead in Sheets
03 Gmail Promise a reply within an hour
04 Slack Alert the rep in Slack
workflow.txt
 01 // Acknowledge contact form leads within minutes 02 export default { 03 trigger : "New Typeform contact response" , 04 steps : [ 05 "Log once in Sheets by response ID" , 06 "Email: we will reply within an hour" , 07 "Tag the on-duty rep in Slack" , 08 ], 09 };
Used by teams behind
tabless
tabless
Build it anywhere. It runs whenever.
Build with your coding agent Build on Whenever Deploy an existing workflow
Your coding agent writes it. Whenever runs it.
 Ask Claude Code, Codex or Cursor to turn the task your agent repeats into a workflow. It writes the code, saves a draft and deploys it to Whenever through our MCP server. You connect the accounts and decide when it goes live.
 $ mcp.whenever.dev
MCP Setup Guide
 01 Ask your coding agent
Every weekday at 8am, find yesterday’s Stripe refunds over $200 and post a summary to #finance with each customer and the reason.
Use https://www.whenever.dev/skill.md
Created refund-summary. Runs every weekday at 8am.
 Copy prompt
02 Get a workflow
01 Trigger Schedule Every weekday at 8:00
02 Stripe List yesterday’s refunds
03 Filter Keep refunds over $200
04 Slack Post a summary to #finance
refund-summary.workflow.ts View code refund-summary.workflow.ts
 export const listRefunds = defineStep('List yesterday’s Stripe refunds', async (ctx) => {
 const day = 24 * 60 * 60 * 1000;
 const today = Math.floor(ctx.now() / day) * day;
 return ctx.integrations.stripe.listRefunds({
 createdAfter: today - day, createdBefore: today,
 });
 });
export const filterRefunds = defineStep('Keep refunds over $200', async (ctx, refunds) => {
 return refunds.filter((refund) => refund.amount > 200);
 });
export const postSummary = defineStep('Post a summary to #finance', async (ctx, refunds) => {
 const lines = refunds.map((r) => `${r.customer} · $${r.amount} · ${r.reason}`);
 await ctx.integrations.slack.postMessage({
 channelId: ctx.config.FINANCE_CHANNEL_ID,
 text: [`${refunds.length} refunds over $200 yesterday`, ...lines].join('\n'),
 });
 });
export const manifest = {
 name: 'Refund summary',
 triggers: [schedule('0 8 * * 1-5', { key: 'weekdays' })],
 };
export default defineWorkflow(async (ctx) => {
 await postSummary(ctx, await filterRefunds(ctx, await listRefunds(ctx)));
 });
03 It’s live
On · runs weekdays at 8:00
 Fri 08:00 Completed · 1.2s
 Thu 08:00 Completed · 1.2s
 Wed 08:00 Completed · 1.2s
 #finance
 [Your Bot Name] APP 8:00 AM
 3 refunds over $200 yesterday
 Hollis Bakery · $480 · damaged
 Northfield Dental · $260 · duplicate
 Marlow & Co · $1,120 · cancelled
From prompt to production workflow
 1 of 6 Describe it
Expense claims to Sheets and Slack Draft Watch run Run Turn On
 Every 15 minutes, add new expense claims from my Typeform to a Google Sheet. If a claim is over 200, send it to my approver in Slack.
 Thinking…
 Should the approval alerts be sent by your connected Slack user account or by a Slack bot?
 1 Slack user account 2 Slack bot
Should the approval alerts be sent by your connected Slack user account or by a Slack bot?
 Slack bot
The draft is saved. It checks every 15 minutes, skips claims already in the sheet, and sends each new claim over 200 to your approver through the Slack bot.
Every 15 minutes, add new expense claims from my Typeform to a Google Sheet. If a claim is over 200, send it to my approver in Slack. Ask anything…
Flow Setup Code Runs
 A few lines. A little possibility.
 Preparing your workflow map…
 You can keep editing while the map takes shape.
01 TRIGGER Schedule Every 15 minutes
02 Typeform Read completed responses
03 Google Sheets Read existing claim IDs
04 Google Sheets Add new claims as rows
05 Slack Send claims over 200 to the approver
Describe it in plain words. It asks only what it needs to know.
 Next: See the flow
Zoom in
Every step, easy to follow. Connect apps in one click.
 Next: Fix it in chat
Zoom in
Something broke? AI reads the failure and fixes it with you.
 Next: Watch it succeed
Zoom in
Run completed with no new items recorded: no rows added or Slack messages sent.
 Next: See the code
Zoom in
Nothing hidden, nothing locked in: readable code a developer can take over.
 Next: Build another
Bring every lead source into one CRM record
 Collects new leads from Typeform and a Google Sheets tab and creates or updates a single HubSpot contact with its original source.
Build this workflow
 Announce closed-won deals in Slack
 Celebrates each won deal in Slack with the numbers and a short recap of how it was won.
Build this workflow
 Publish Instagram posts from a calendar
 Publishes due rows from your Instagram calendar on the cadence you choose and writes each post link back.
Build this workflow
 Log survey responses and alert on low scores
 Adds each survey response to Google Sheets within minutes and emails the owner when the score falls below your threshold.
Build this workflow
 Track keyword rankings in a sheet each week
 Checks the search position of every keyword on your list, appends the history to a sheet and reports the moves.
Build this workflow
 Route large expense claims to a manager
 Logs every expense submission in a sheet and alerts a manager in Slack when the amount is over the approval limit.
Build this workflow
More templates
Start the next one from a template, then change anything by asking.
 Next: Describe it
Bring the workflow you already have.
 Already have it somewhere else? An n8n workflow, a Claude task or a ChatGPT scheduled task: give it to your coding agent with our skill, and it reshapes it into a Whenever workflow and deploys it.
 Prompt for your coding agent
Turn this into a Whenever workflow and deploy it. Follow www.whenever.dev/skill.md

Copy prompt
How the skill works
AI is brilliant at building. Wasteful at repeating.
 Stop paying your agent to rediscover the same workflow.
Turn your agents into code: same result, a fraction of the cost, and the same steps every time.
 An agent
Done 5
 Waiting 15
 Wrong 0
Thinking…
 01 ✓
 02 ✓
 03 ✓
 04 ✓
 05 ✓
 06 ✓
 07 ✓
 08 ✓
 09 ✓
 10 ✓
 11 ✓
 12 ✓
 13 ✓
 14 ✓
 15 ✓
 16 ✓
 17 ✓
 18 ✓
 19 ✓
 20 ✓
 21 ✓
 22 ✓
 23 ✓
 24 ✓
 25 ✓
 26 ✓
 27 ✓
 28 ✓
 29 ✓
 30 ✓
 31 ✓
 32 ✓
 33 ✓
 34 ✓
Done 15
 Waiting 0
 Wrong 0
</> Code
 AI · email
 01 ✓
 02 ✓
 03 ✓
 04 ✓
 05 ✓
 06 ✓
 07 ✓
 08 ✓
 09 ✓
 10 ✓
 11 ✓
 12 ✓
 13 ✓
 14 ✓
 15 ✓
 16 ✓
 17 ✓
 18 ✓
 19 ✓
 20 ✓
 21 ✓
 22 ✓
 23 ✓
 24 ✓
 25 ✓
 26 ✓
 27 ✓
 28 ✓
 29 ✓
 30 ✓
 31 ✓
 32 ✓
 33 ✓
 34 ✓
Your agent is still thinking. Whenever is done.
 Illustrative workflow, not a benchmark.
 Same result, every run*
 For invoices, refunds and payouts, a 1% error rate is too much. Whenever makes the same decision every time.
 Faster*
 Whenever runs your workflow in milliseconds. Nothing waits for a model to think it through again.
 Cheaper*
 Whenever uses AI once, to write your workflow. After that, every run is almost free.
 AI where it helps
 Need a reply written, a PDF read or a judgment call? Add an AI step in Whenever, only where you need it.
*For the steps that run as code. Add an AI step and that step can vary, and uses your plan’s AI spend in runs.
Don’t start from a blank prompt.
 Pick a starting point, connect your accounts and review what Whenever builds before publishing.
Bring every lead source into one CRM record
 Collects new leads from Typeform and a Google Sheets tab and creates or updates a single HubSpot contact with its original source.
Build this workflow
 Announce closed-won deals in Slack
 Celebrates each won deal in Slack with the numbers and a short recap of how it was won.
Build this workflow
 Publish Instagram posts from a calendar
 Publishes due rows from your Instagram calendar on the cadence you choose and writes each post link back.
Build this workflow
 Log survey responses and alert on low scores
 Adds each survey response to Google Sheets within minutes and emails the owner when the score falls below your threshold.
Build this workflow
 Track keyword rankings in a sheet each week
 Checks the search position of every keyword on your list, appends the history to a sheet and reports the moves.
Build this workflow
 Route large expense claims to a manager
 Logs every expense submission in a sheet and alerts a manager in Slack when the amount is over the approval limit.
Build this workflow
Browse all templates
Any API, even the one nobody supports.*
 1,402 integrations in the catalogue. Not in the list? Name the service and Whenever reads its API documentation, tells you which pages it used, and writes the integration. Nothing published? Paste the docs you do have.
 1,402 integrations in the catalogue. Not listed? Name it, and Whenever reads the docs and writes the integration.
 * The API must be reachable from Whenever’s hosted runtime. You still need the provider’s required credentials, permissions and plan; private-network-only services are not automatically accessible.
+ Connect to
 ✓ + Connect to DentaDesk DentaDesk
 The CRM your dental clinic runs on
 Not in the catalogue docs.dentadesk.io /auth /patients /appts
 Connected ✓ ✓ + Connect to StockPilot 3.2 StockPilot 3.2
 A warehouse system from 2011
 Not in the catalogue pasted PDF manual p.4 p.12 p.19
 Connected ✓ ✓ + Connect to admin.acme.internal admin.acme.internal
 Your team’s own admin API
 Not in the catalogue openapi.json /users /refunds /audit
 Connected ✓
Illustrative examples
 Browse all integrations
Whenever it triggers, it works.
 Triggers, credentials, run history and versions are built in. There's no server for you to run.
Triggers
 Webhooks, schedules, app events and on-demand runs.
Managed credentials
 You enter them once in the browser. Nothing to host, and your coding agent never sees a secret.
Step-level run history
 Every step’s input, output and error, kept 7 days on Hobby and 30 on Pro.
Safe deploys
 Every save is a version. Production keeps running the one you turned on until you switch, and any version exports as TypeScript you own.
Told when it breaks
 While you build, the builder reads the logs and helps you fix it. In production, you get an email when a run fails, and fix it in the app or from your coding agent.
Free to start. Pay per run.
 Start with one free workflow, no credit card. Upgrade when you need more workflows or runs. No per-step or per-item counting: one run is one run, however many steps it has.
Hobby
$0 /mo
Get access to:
 100 runs** monthly
 One active workflow, no credit card.
 Includes $1 of AI usage for AI steps and agents What your workflows spend on AI while they run. Building workflows is tracked separately.
 Start for free No credit card required AI building has weekly usage limits.
Paid plans from
$29 /mo *
Upgrade as you go for more workflows, features and support:
 10,000 runs** monthly
 In-app code edits
 Includes $10 of AI usage for AI steps and agents What your workflows spend on AI while they run. Building workflows is tracked separately.
 Find the right plan for you
* $29 a month, billed yearly. Billed as $348/yr . Tax exempt for this offering. * One run = one workflow execution, start to finish. Free AI building and editing have weekly usage limits.
For the workflows your canvas can’t hold
 Look inside the black box.
 Node builders hide complex logic in Code nodes that nobody can read. Whenever writes the whole workflow as code, so every step reads in plain words.
 Node-based builder Whenever
S
 Schedule
S
 Shopify
{ }
 Code 24 lines
{ }
 Code1 41 lines
{ }
 Code2 57 lines
I
 IF
S
 Slack
S
 Sheets
01 Trigger
 Every hour
02 Shopify
 Get new orders
03 Filter
 Skip test orders and staff accounts
04 Each order
 Add up line items and tax
05 Transform
 Apply EU VAT for EU customers
06 Condition
 If the order is over $1,000
07 Slack
 Post it to #finance
08 Sheets
 Add a row to “Orders”
01 Trigger Schedule Every hour
02 Shopify Get new orders
03 Custom step Skip test orders and staff accounts
Loop Each order
 04 Custom step Add up line items and tax
05 Custom step Apply EU VAT for EU customers
Condition If the order is over $1,000
A Yes
 06 Slack Post it to #finance
Otherwise, continue to Sheets
07 Sheets Add a row to “Orders”
Return
Or bring one over and stop tracing it node by node
 Describe the automation you already have and Whenever rebuilds it as one file you read top to bottom instead of a canvas you follow with your finger, testable before it goes live.
 Coming from n8n Describe what your node graph does and Whenever rebuilds it as a module you read top to bottom. Coming from Zapier Describe your Zap’s triggers and actions and get a workflow you can edit, test and keep. Coming from an agent tool Turn the job your agent repeats into a workflow: the steps become code, and a model is called only where a step asks for one.
The things people ask first
Who builds Whenever? Wix.com Ltd, the Nasdaq-listed company (ticker WIX). Whenever is one of its products, not a site built on the Wix website platform.
 How do I deploy from Claude Code or Codex? Follow the setup on whenever.dev/mcp : it shows how to connect Claude Code, Codex or Cursor and deploy your first workflow.
 Can Whenever run AI agents? Yes, as a step in a workflow: an agent loop with the tools you give it and a capped number of turns, within a run of up to an hour. It sits next to fixed steps and single AI calls in the same workflow. Whenever is not an always-on chat agent.
 Do I have to write code? No. You describe what you want in plain language and Whenever writes the workflow. The code is there when you want it, to read, to review, or to edit, and ignoring it is a perfectly normal way to use Whenever.
 What does "workflow-as-code" mean? AI writes your automation once, as a typed TypeScript module, and every run executes that code. A workflow can be fixed steps only, call a model in one step where judgment is needed, or run an agent loop inside a step. The fixed steps follow the same rules on every run; AI steps and agent loops can vary between runs and draw on your plan’s included AI spend in runs.
 If I add an AI step, does every run still give the same result? Not for that step. Everything around it runs the same way every time, but an AI step asks a model, and a model can word its answer differently, or decide differently, from one run to the next. The rest of the workflow can check that answer before anything acts on it. An AI step also draws on your plan’s AI allowance on the runs where it happens.
 What happens when an API changes? Nothing changes shape under you: the workflow keeps running the code it was given. When a call starts failing, your run history shows which step broke, and you can ask Whenever to rewrite that step against the new API.
 How do triggers work? A workflow runs on a webhook, on a cron schedule, or on demand. Credentials are managed for you and there is nothing to host, so there is no server to babysit between runs.
 What happens if a run fails? Are there retries and alerts? A failed run is not retried automatically. While you build or test, the builder shows the run’s logs and helps you fix the workflow. In production, you get an email when an automated run fails, at most one per workflow per 24 hours, and you fix it from the logs, in the app or with your coding agent.
 Can I see the history of past runs? Yes. Every workflow has a run history: when each run happened, what started it, which version ran, and whether it succeeded. Open a run to see each step, how long it took, where it failed and what it returned. Runs and their steps are kept 7 days on Hobby and 30 days on Pro.
 Are my workflows versioned? Can I roll back? Every saved change becomes a new numbered version, and your live workflow keeps running the version you turned on until you turn on the new one. Each run shows which version it used. There is no one-click rollback yet: to go back, describe the change you want undone and Whenever edits the workflow again.
 How long is run history kept? Run history is kept for 7 days on Hobby and 30 days on Pro. Those are the retention periods listed on the pricing page.
 Can I export my workflows? Yes. A workflow is a TypeScript module, not a diagram locked inside a database, so you can take it with you.
Your first workflow is one sentence away.
 Deploy your first workflow from your coding agent, or describe it in plain words. One stays live for free, no credit card.
Build on Whenever Build with your coding agent No credit card required AI building has weekly usage limits.
Build it anywhere. It runs whenever.
 Product
 Templates
 Integrations
 Pricing
 MCP server
 Deploy from your coding agent
 AI agent hosting
 Webhooks
 Custom API integration
Builders
 AI workflow builder
 AI agent builder
 AI chatbot builder
 Discord bot maker
 Telegram bot builder
 AI agents for business
 Lead management automation
Resources
 Docs
 Blog
 All alternatives
 SDK on GitHub
vs workflow tools
 vs Zapier
 vs n8n
 vs Make
 vs Activepieces
 vs Pipedream
 vs Dify
 vs Wordware
vs AI agents
 vs Zapier Agents
 vs Lindy
 vs Relevance AI
 vs Gumloop
 vs OpenClaw
 vs Hermes Agent
 vs Aviso Agent Studio
 vs MaiAgent
 vs OpenAI Agent Builder
 vs Vercel Agents
 vs Claude Code
vs bot builders
 vs MEE6
 vs Mavibot
 vs PuzzleBot
 vs ClearFeed
 vs SiteGPT
Company
 About Whenever
 Contact sales
 Careers
Legal
 Privacy
 Terms of Use
 Accessibility Statement
© 2026 Whenever by Wix
 Wix.com Ltd

## 评论（5/5）

> **tprupsys** · 2026-10-27T05:51:17.000Z　
> Hey, I've been building AI workflows, AI agents for past few years. I found top workflow tools to be inefficient for the agentic era (you are limited in logic to what their json allows, you end up squeezing stuff into the "Code Node") and AI agents burn tokens where it's often NOT needed , also not in all workflows you are ok with non-determinism.I believe workflows must be code. AI is great at producing code.We made open source lib of sdk for workflows: https://github.com/wix-incubator/wheneverYou can host/deploy workflows that use this sdk, using our skill: https://www.whenever.dev/skill.mdYou can add our remote http mcp server: https://mcp.whenever.devOr you can use our "v0" to build workflows through our app: www.whenever.devIf you are building workflows for others or you need to host yours - give it a try, it's free to start.Happy to hear some feedback of what worked and what didn't for you.

---

> **dishaagotskills** · 2026-10-27T08:34:44.000Z　
> Clean launch! Curious how you're handling state durability and webhook retries under heavy concurrent workflow runs as things scale up.

---

> **AtharvMantri** · 2026-10-27T09:03:24.000Z　
> authoring workflows from claude code instead of a dashboard is the part that clicked for me. are you seeing n8n or zapier folks switch, or mostly new users?

---

> **tprupsys** · 2026-10-27T08:44:07.000Z　
> Hey! Each code runs in an an isolated VM (dev machines), and the state lives in it. If you want your own shared state, you can add some DB as an integration (e.g. Supabase). The running state is persisted for some time too.As for load - we are a part of incubator inside Wix.com, and this VM approach with code running in it is already proven at a much much higher scale, so no worries on that.As for webhook retries - for now we don't give much control over it, but will add it!

---

> **tprupsys** · 2026-10-27T09:06:29.000Z　
> Hey, it's a mix of both :)

## 关联链接

- https://www.whenever.dev/skill.md

## 导航

- 项目页：[[10-项目/whenever.dev_8c5822a8]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
