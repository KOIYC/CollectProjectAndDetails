---
type: "corpus"
item_id: "aa70c5a7feea536b"
title: "Show HN: Forward newsletters to an address, get a typeset paper on your Kindle"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49712017"
project_url: "https://wholemind.tech/briefing/services.html"
author: "jps330"
published_at: "2026-09-15T13:11:32Z"
captured_at: "2026-09-20T09:37:18+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_jps330
  - story_49712017
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Forward newsletters to an address, get a typeset paper on your Kindle

> [!info] 一句话导读
> Briefing Service: AI-enabled data services for e-ink readers and agents

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49712017>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：jps330　|　发布：2026-09-15T13:11:32Z
> 项目链接：<https://wholemind.tech/briefing/services.html>
> 采集：2026-09-20T09:37:18+08:00　|　id：`aa70c5a7feea536b`

## 正文

Briefing Service: AI-enabled data services for e-ink readers and agents

# The news, ranked by an editor that never sleeps, delivered wherever you read.

Every hour an LLM editor reads about a hundred feeds per topic and picks what matters, with a why-it-matters line and the facts. You get the result as JSON and MCP for your agents, or as a typeset morning paper on your reMarkable or Kindle. Ten briefings, three of them new this week.

Free tier, no key No card for trials MIT MCP server on npm x402 for agents that pay per call

Live: the AI briefing front page, exactly as an e-ink device sees it.

## Pick a service. Each one starts with one command or one form.

Same editor, same data, different delivery. Everything below is live today; the code blocks are copy-paste real, not illustrations.

### Briefings API and MCP

for agents and developers

Ten ranked briefings as structured JSON: lead, stories, why it matters, key points, sources. Rendered e-ink pages, a free summary, and the full candidate pool with provenance.

- Keys: ai, labs, finance, sports, soccer, us, world, crypto (hourly), grants and slow-es-b1 (daily)
- Six MCP tools: list, get, summary, candidates, page, render
- Local server on npm, or the remote endpoint with no install
- Every story links to its source; facts are constrained to the candidate text

25 free calls per IP per day · then a $9/month key or $0.002 per call over x402

```
curl https://briefing-service.wholemind.workers.dev/v1/briefings/ai
```

```
{ "mcpServers": { "briefings": {
    "url": "https://briefing-service.wholemind.workers.dev/mcp" } } }
```

Full reference: llms.txt · openapi.json · github.com/jshelley/briefing-mcp

### Morning Paper

for reMarkable and Kindle

Any briefing as a multi-page paper on your device at 07:00 ET every day. Story text inside the file, not links out. PDF for reMarkable and Scribe, reflowable EPUB for Kindle.

- Pushed to a reMarkable folder, or emailed to your Send-to-Kindle address
- Optional personal front sheet: date, weather, calendar, checklist
- Free PDF and EPUB downloads for every briefing, any time

7-day trial, no card · then $9/month (Reader key)

```
open https://wholemind.tech/briefing/paper.html
# pick a briefing, paste your Kindle address or reMarkable code, done
```

### Opportunity Paper

grants and funding, matched to you

Newly posted federal grants from grants.gov, NIH, NSF and the Federal Register, plus SAM.gov contract notices with their set-asides, ranked for your organisation. Every story carries Deadline, Amount and Eligible, and says "not stated" instead of guessing.

- Paste an organisation profile; the whole day's pool (about 70 grants and contracts) is ranked for it
- The plain Grants & Funding briefing is free to read, as web, PDF or EPUB
- Daily at 07:00 ET on Kindle or reMarkable, JSON for your own tools

```
open https://wholemind.tech/briefing/paper.html?plan=opps
# fill "Organisation profile" (who you are, what you fund, where)
```

```
curl -O https://briefing-service.wholemind.workers.dev/v1/briefings/slow-es-b1/paper.epub
```

Preview today's edition: the rendered pages

### Custom render and Team Briefing

Send any feeds and a persona through the same editor and get JSON, e-ink pages and a PDF under a private path. Teams get it daily to Slack, email or MCP; agents call it as the `render_briefing` tool.

```
curl -X POST https://briefing-service.wholemind.workers.dev/v1/render \
  -H "authorization: Bearer $BRIEFING_KEY" -H 'content-type: application/json' \
  -d '{"feeds":["https://blog.cloudflare.com/rss/"],"persona":"editor for a platform team","name":"Platform Brief"}'
```

## How a trial works

No account, no card. A paper trial is tied to one Kindle address or one reMarkable; the API tier needs nothing at all.

### Start

Sign up on the form or with one curl. Today's paper goes out immediately, then every morning at 07:00 ET. You get an id; that id is your account.

### Decide

The last two papers carry a one-page notice with the end date and a one-click keep link. Nothing is charged unless you use it.

### Keep or stop

Keep it with a $9/month Reader key (or the $29 Opportunity Paper if you set a profile). Or do nothing and delivery simply stops. Cancel any time from the billing portal below.

## Pricing

Two ways to pay: a monthly key through Stripe, or per call in USDC on Base through x402 for agents that would rather not have an account.

## Already a customer? Manage it here.

There is no login. A Reader, Opportunity or Team key is your billing account; a paper subscription is managed with the id you got at signup.

### Billing: cancel, change card, invoices

Paste your key. You go straight to your Stripe customer portal; the key never leaves your browser except to open that page.

Paste the subscription id from your signup. Status shows deliveries, trial end, your inbox address and profile.

To change or stop it, use PATCH or DELETE on the same URL, or write to hello@wholemind.tech with the id.

# andreylukin/bough

## 关联链接

- https://blog.cloudflare.com/rss/
- https://briefing-service.wholemind.workers.dev/mcp
- https://briefing-service.wholemind.workers.dev/v1/briefings/ai
- https://briefing-service.wholemind.workers.dev/v1/briefings/slow-es-b1/paper.epub
- https://briefing-service.wholemind.workers.dev/v1/render
- https://wholemind.tech/briefing/paper.html
- https://wholemind.tech/briefing/paper.html?plan=opps

## 导航

- 项目页：[[10-项目/wholemind.tech_8a7f17db]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
