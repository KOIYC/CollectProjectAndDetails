---
type: "corpus"
item_id: "4d26d8ac3b91e83d"
title: "Show HN: DispatchSEO – open-source SEO manager tool for Claude Code"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49109315"
project_url: "https://github.com/NeoZi12/dispatchseo"
author: "neozino"
published_at: "2026-07-30T12:52:23Z"
captured_at: "2026-09-21T03:11:19+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-30"
tags:
  - 语料
  - hn_show
  - author_neozino
  - story_49109315
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: DispatchSEO – open-source SEO manager tool for Claude Code

> [!info] 一句话导读
> Turn Claude Code into your SEO manager - the open-source alternative to SEObot and Outrank

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49109315>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：neozino　|　发布：2026-07-30T12:52:23Z
> 项目链接：<https://github.com/NeoZi12/dispatchseo>
> 采集：2026-09-21T03:11:19+08:00　|　id：`4d26d8ac3b91e83d`

## 正文

# NeoZi12/dispatchseo

Turn Claude Code into your SEO manager - the open-source alternative to SEObot and Outrank

- Stars: 1
- Forks: 1
- Watchers: 1
- Open issues: 0
- License: GNU Affero General Public License v3.0
- Homepage: https://dispatchseo.com
- Default branch: main
- Created: 2026-07-19T12:36:00Z

## Languages

- CSS
- Dockerfile
- JavaScript
- MDX
- PLpgSQL
- Shell
- TypeScript

## Topics

- ai-agents
- ai-seo
- claude
- claude-code
- content-marketing
- mcp
- nextjs
- open-source
- self-hosted
- seo
- seo-automation
- seo-tools

## Top Contributors

- NeoZi12 (260 contributions)
- github-actions[bot] (6 contributions)

---

## README

 DispatchSEO

 Turn Claude Code into your SEO manager.

 Website
  · 
 Quickstart
  · 
 Self-hosting guide
  · 
 Discussions
  · 
 Hosted version

The open-source alternative to SEObot and Outrank, built for Claude Code.
Other SEO tools learn about your product by crawling your homepage. Your
Claude Code already knows your product, because it probably built half of it.
DispatchSEO gives that agent the missing pieces: a research playbook, a
content pipeline that ships pull requests, rank tracking, and a dashboard
where you stay in control.

 Self-hosting is one command on any machine with Docker -
run it from any plain folder (not inside your website's repo; it creates
its own dispatchseo folder):

```bash
git clone https://github.com/NeoZi12/dispatchseo &&
  cd dispatchseo &&
  sh start.sh
```

 When it finishes it prints your dashboard URL - open it
and the setup wizard takes it from there. Your laptop is fine for trying
it out; for the real always-on autopilot, use any machine that stays
awake - a $5 VPS, a Raspberry Pi, a desktop that never sleeps
( the guide
explains the difference honestly). On Windows, paste this in WSL or Git
Bash.

 Step-by-step walkthroughs:
 on your computer
 · 
 on a VPS

 Self-hosted has zero feature limitations. Everything the
paid cloud will do, this repo does today, in your own accounts, at $0.

## How it works

1. **Your agent researches.** Claude Code connects to DispatchSEO over MCP,
 reads the served playbook, and mines keywords from your Search Console
 data, Google Autocomplete, and what it already knows about your product.
 Ideas land in a queue with the reasoning attached.
2. **You approve, or don't.** Each idea is a card on the dashboard: the
 keyword, why it's winnable, the angle. Approve, reject, or reorder.
 Prefer full autopilot? Flip on auto mode and skip the queue entirely.
3. **The pipeline builds.** Every morning a GitHub Action picks the oldest
 approved idea and builds it into a real pull request against your site's
 repo: a guide or a small free tool, checked against the live SERP and run
 through a sameness reviewer so page twelve doesn't read like page three.
4. **It tracks what happened.** Daily rank checks, hourly Search Console
 snapshots, index verification, and a journey view that tells you which
 SEO stage you're actually in. When a scheduled job breaks, you get a red
 banner and an email instead of silence.

The backend is deliberately boring: state, scheduling, and an approval gate.
The thinking happens in your agent, where your product knowledge already
lives.

## What's in the box

- **MCP server** with ~40 tools: the queue, keywords, rankings, pages, GSC
 stats, backlink prospects, trend topics, site profile. Anything the
 dashboard can do, your agent can do over MCP; parity between the two is a
 hard rule in this codebase.
- **Trend radar**: scan for rising topics in your niche, expand a topic into
 concrete guide angles, and queue the good ones.
- **Guide and tool builders**: guides publish on a pace matched to your
 site's age (so a three-week-old blog doesn't suddenly ship 30 posts);
 free-tool ideas build on approval.
- **Backlink playbook**: a prospect list prefilled with your product's copy,
 tracked per submission.
- **Multi-site**: one deployment manages any number of sites. Each project
 gets its own MCP token, its own data, its own settings.
- **A password-gated dashboard** for the one human in the loop.

## What it costs to run

Nothing, unless you want paid data. The tiers stack:

| Tier | Price | What you get |
| --- | --- | --- |
| Search Console only | $0 | Rankings from GSC, keyword ideas from Autocomplete plus your own impression data |
| + SerpApi free key | $0 | Live SERP checks, real positions weekly (250 free searches/month) |
| + DataForSEO | pay per call | Search volume, keyword difficulty, domain rating |

Free mode finds keywords you can win. Paid mode also knows which ones are
worth winning.

## What you need

- Your site's source in a GitHub repo. The pipeline ships content as pull
 requests, so git-based sites only; WordPress won't work.
- A Claude subscription with Claude Code. Your agent is the engine and it
 runs on your existing plan.
- A machine with Docker (~1 GB RAM). A laptop works for a test drive; the
 automation runs on a schedule, so day-to-day you want something that
 stays on - a $5 VPS, a Raspberry Pi, or a home server.
- Google Search Console access to your site.

## Quick start

The one command above is the whole install
(the docs are the full guide). Database,
migrations, schedules, and a headless Claude Code builder are all bundled;
open the dashboard and the setup wizard takes over. Nothing on the internet
needs to reach your machine, so there is no domain or port forwarding to
set up.

The last step is pasting one command into Claude Code inside your site's
repo. Your agent does the rest of the install itself, including writing its
own workflow files and setting its own secrets.

There's also an llms.txt and a SKILL.md if
you'd rather point an agent at this repo and let it figure the setup out.

## Developing (from source)

```bash
git clone https://github.com/NeoZi12/dispatchseo
cd dispatchseo
pnpm install
cp .env.local.example .env.local
pnpm dev
```

This is the contributor path, not the way to self-host (that's the Docker
command above). Fill in `.env.local` (Supabase + the three secrets) before
starting, then open the dashboard on **localhost:3000**.

`pnpm build` is the typecheck - run it before opening a PR. There is no
separate lint or test setup.

## Cloud version

There's a hosted version for people who'd rather not run a machine: we host
it, bundle the SERP + volume data into one bill, and replace the Google
service-account ritual with one click. It's at
dispatchseo.com. Self-hosting stays
feature-complete either way; the cloud sells convenience, not capability.

## Architecture, briefly

Next.js App Router, Postgres for state (a bundled container when
self-hosted, Supabase in the cloud version), `mcp-handler` for the MCP
server at `/api/mcp`. Schedules and builds run in-stack (cron + builder
containers) or on GitHub Actions. One deployment is multi-tenant: the MCP
bearer token selects the project, crons loop over all projects, the
dashboard switches with a cookie.
CLAUDE.md has the full conventions; it's written for agents,
which turns out to make it decent documentation for people.

## Contributing

Issues before PRs, and you must understand every line you submit, including
the AI-assisted ones. Details in CONTRIBUTING.md.
Questions go to Discussions;
vulnerabilities go through private reporting.

## License

AGPL-3.0. Use it, self-host it, fork it. If you run a modified
version as a service, share the source. That's the whole deal.

---

Star History Chart

# felixpg13-glitch/spendshield

## 关联链接

- https://dispatchseo.com

## 导航

- 项目页：[[10-项目/github.com_95e60977]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
