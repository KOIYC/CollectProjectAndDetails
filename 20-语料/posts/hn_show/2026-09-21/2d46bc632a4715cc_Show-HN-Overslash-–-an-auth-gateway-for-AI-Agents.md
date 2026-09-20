---
type: "corpus"
item_id: "2d46bc632a4715cc"
title: "Show HN: Overslash – an auth gateway for AI Agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48344584"
project_url: "https://overslash.com/"
author: "arturogoosnargh"
published_at: "2026-05-31T10:34:23Z"
captured_at: "2026-09-21T02:52:46+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-31"
tags:
  - 语料
  - hn_show
  - author_arturogoosnargh
  - story_48344584
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:144d"
---

# Show HN: Overslash – an auth gateway for AI Agents

> [!info] 一句话导读
> Overs / ash beta Features How it works Pricing Docs Install

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48344584>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：arturogoosnargh　|　发布：2026-05-31T10:34:23Z
> 项目链接：<https://overslash.com/>
> 采集：2026-09-21T02:52:46+08:00　|　id：`2d46bc632a4715cc`

## 正文

Overs / ash beta Features How it works Pricing Docs Install
EN ▾
 ☀ GitHub ↗ Open Cloud ↗
Your agent acts. Overs / ash controls.
 One gateway to every service your agent touches. You decide: deny, approve once, or approve all.
 Start free on Cloud read on ↓
 Free for individuals · no card required
What it does One gateway between your agent and everything else.
 Overslash sits between agents and the outside world. It handles secrets, OAuth, MCP, human approvals, and authenticated HTTP execution. The agent doesn't hold keys. You don't hold your breath.
✓
 Human approvals, on tap
 The first time an agent wants a permission, you approve or deny. Allow & Remember at the scope ladder you choose.
◫
 OAuth & secrets, handled
 One place for client IDs, tokens, signing keys. Rotate, revoke, per-agent. No credentials ever touch the agent's context window.
☰
 Audit that reads like prose
 Every call, every bubble-up, every deny. Streaming, searchable, exportable.
⌘
 MCP-native
 Enroll any MCP client in a click — Claude Desktop, your own. Overslash brokers the tools, the credentials, and the approvals. The agent just asks.
How it works Agents ask. Overslash mediates. Services respond.
 Any MCP-capable agent — Claude Code, Overfolder, OpenClaw, or your own — connects to Overslash once. Overslash holds the credentials, enforces the rules, and hands each service an authenticated, audited request.
agent:henry agent:deploy-bot agent:research-bot
Gateway Overs / ash Checks rules. Injects credentials. Bubbles unknowns to parent agents or humans. Records every call.
authed request ↓
 Service github.com Receives a normal authenticated request. Knows nothing about the agent.
GitHub, Slack, AWS, Google Workspace, Notion, Linear, Vercel, PostgreSQL — and any HTTP API.
Pricing Free in self-hosted. Cloud free for individuals. Paid for teams.
 Three ways to use Overslash. Self-hosted gives you everything for free. Your Personal org on Cloud is free, forever. When you want to bring colleagues, create a Team org at €3 per seat.
SELF-HOSTED Free
 €0 forever
 MIT · Elastic-2.0 · no telemetry
Run it yourself. Full features — no gating, no license keys, no telemetry. Elastic License 2.0.
 All features, no gating
 Unlimited agents, actions, integrations
 Local secrets vault
 Clone the repo
 PERSONAL Free for one
 €0 forever
A hosted Personal org, just for you. Always free, no card required.
 Personal org with all integrations
 Hosted backups & upgrades
 Personal audit log
 All Cloud features for one user
 Try Personal — free
 TEAM Per seat
 €3.63 / month
 1 seat · Every seat : € 3 · + 21% VAT
 1 seat 20 seats
Create Team orgs and bring your colleagues. Every seat €3. Your own Personal org stays free.
 Everything in Personal
 Multiple Team orgs
 SSO (Google, GitHub, SAML)
 Shared connections & secrets
 Audit log export
 Pooled usage with metered overages
 Start a Team
OSS, research, or education? Email sales@overslash.com — we usually say yes.
Install · get started Give this to your agent.
 Paste the block below into Claude, Cursor, Open Interpreter, or any MCP-capable agent. It will follow the skill, enroll itself under your Overslash account, and ask you for permissions as they come up.
skill · agent enrollment Copy
 Your Human wants to give you access to external services via Overslash.
To connect, follow the instructions at: https://www.overslash.com/SKILL.md
Open Cloud ↗ Contact sales
 1. Paste
Drop the block into any MCP-capable agent.
 2. Connect
Give the agent an identity and grant it services.
 3. Use
Start using integrations. Dangerous actions bubble up for approval.
Overs / ash Actions & authentication gateway for AI agents. One hop between your agent and everything else.
 A product by Overspiral S.L. 🇪🇸
Product
 Features
 How it works
 Integrations
 Pricing
Developers
 Docs
 SKILL.md
 GitHub
 Status
Company
 Dispatches
 Overspiral
 Contact
 Security
 Privacy
 Terms
© 2026 Overspiral S.L. · registered in spain · all rights reserved
 beta · source-available

## 评论（1/1）

> **arturogoosnargh** · 2026-05-31T10:34:55.000Z　
> Author here. Overslash is an authorization gateway for AI agents (or any programmatic user, really).Overslash can register as a service any HTTP API or MCP server, defined as an OpenAPI document with some small extensions. Once that's done you can share access to those services with agents or teammates. Agents start with no write permissions (and no read permissions either, if you choose). Every time an agent attempts an action, a set of permission keys based on the action and its fields is generated; if the agent is missing any, an approval request is created. The approver can inspect the request — which has human-readable descriptions for the action and fields, taken from the OpenAPI doc — and deny or approve, either just this time or for similar requests in the future (choosing coarser or finer permission keys to remember).Overslash itself can be used as an MCP server, via REST, via CLI, or via the dashboard (think of it as an authenticated, shareable, auditable Postman).It's a single Rust binary, persistence on Postgres. Self-hosting will always be free; cloud at https://app.overslash.com is free for individuals, cheap for teams.I wrote a longer post (with a video demo) on the origins of Overslash: https://www.angelmartin.name/2026/05/29/why-did-i-build-an-a...Repo: https://github.com/overfolder/overslashNote: had to use an old HN account since i dont have enough karma on my new one

## 关联链接

- https://www.overslash.com/SKILL.md

## 导航

- 项目页：[[10-项目/overslash.com_6e4fbdc6]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
