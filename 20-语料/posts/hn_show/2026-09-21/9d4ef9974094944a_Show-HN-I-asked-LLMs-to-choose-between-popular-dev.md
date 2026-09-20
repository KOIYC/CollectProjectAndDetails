---
type: "corpus"
item_id: "9d4ef9974094944a"
title: "Show HN: I asked LLMs to choose between popular developer tools"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49504947"
project_url: "https://github.com/betocmn/preseason"
author: "thedreammachine"
published_at: "2026-08-31T02:29:25Z"
captured_at: "2026-09-21T03:11:27+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - hn_show
  - author_thedreammachine
  - story_49504947
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:52d"
---

# Show HN: I asked LLMs to choose between popular developer tools

> [!info] 一句话导读
> Open-source benchmark that measures which developer tools LLMs recommend when asked to build real web apps.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49504947>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：thedreammachine　|　发布：2026-08-31T02:29:25Z
> 项目链接：<https://github.com/betocmn/preseason>
> 采集：2026-09-21T03:11:27+08:00　|　id：`9d4ef9974094944a`

## 正文

# betocmn/preseason

Open-source benchmark that measures which developer tools LLMs recommend when asked to build real web apps.

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 0
- License: MIT License
- Homepage: https://preseason.ai
- Default branch: main
- Created: 2026-02-26T09:58:30Z

## Languages

- CSS
- JavaScript
- TypeScript

## Topics

- benchmark
- devtools
- llm

## Top Contributors

- betocmn (717 contributions)

---

## README

# Preseason

**Measure which developer tools LLMs recommend when asked to build real web apps.**

CI
CodeQL
License: MIT
PRs Welcome

Preseason is an open-source benchmark that measures which developer tools
LLMs recommend when asked to build real web apps.

We run a fixed set of web-app prompts against a fixed panel of models, parse
each answer for recommended tools and services, then publish rankings,
head-to-head comparisons, and methodology notes.

The goal is to make AI-driven developer-tool recommendations inspectable,
reproducible, and contestable, so you can see which tools AI coding assistants
are most likely to put in front of developers.

🌐 **Live demo:**

Preseason homepage

## What it tracks

Preseason currently tracks recommendations across categories like:

- databases
- auth
- hosting
- analytics
- payments
- email
- background jobs
- UI/component libraries
- observability
- AI/model providers

For each prompt × model run, we record whether the model recommended a known
tool, no tool, or an invalid/unrecognized answer.

## Example questions Preseason can answer

- Which database does each model recommend most often for a new SaaS app?
- Does GPT-4.1 prefer Supabase, Firebase, Neon, or plain Postgres?
- Which tools win head-to-head when two options appear in similar prompts?
- Are some models more likely to recommend "no tool" or hallucinate unknown
 tools?

## Why open source?

Recommendations from AI coding assistants shape developer tool adoption
faster than blog posts or Twitter threads. If a foundation model quietly
favors one database or hosting provider, that preference scales to every
developer using it. We think the methodology behind that should be open,
reproducible, and contestable, not a private dashboard.

Preseason exists so anyone can:

- See **what** today's LLMs recommend, with frozen prompts and model
 snapshots that are inspectable in this repo
- Run **their own** benchmark on their own prompts or model panel
- Submit **issues** when results look off and have an open paper trail

## Current limitations

- The benchmark measures recommendations, not whether a tool is objectively
 better.
- Results depend on the frozen prompt set and model snapshots.
- Tool-name parsing is intentionally strict; unknown names go to review instead
 of being guessed.
- The project is early, so rankings should be treated as directional rather
 than definitive.

## Quick start

```bash
pnpm run setup                  # installs deps and starts local Supabase
cp .env.example .env.local      # fill with `supabase status` + OpenRouter key
pnpm run db:migrate
pnpm run db:seed
pnpm run db:seed-dev
pnpm run dev
```

App is at. Full setup details, including the env
var table and troubleshooting, are in `docs/SETUP.md`.

## Deploy

Deploy with Vercel

The supported launch path is Vercel + Supabase Cloud. Docker Compose and plain
Postgres self-hosting are not supported yet because Preseason currently depends
on Supabase Auth. See `docs/SELF_HOSTING.md`.

## How it works

```
   ┌────────────┐        ┌──────────────┐        ┌─────────────┐
   │  Cron      │───────▶│  OpenRouter  │───────▶│  Response   │
   │  /api/cron │ prompt │  (one model) │ answer │  parser     │
   │  /benchmark│        └──────────────┘        └──────┬──────┘
   └────────────┘                                        │
         ▲                                               ▼
         │ every 6 min                          ┌────────────────┐
         │                                      │  Case decision │
         │                                      │  tool / none / │
         │                                      │  invalid       │
         │                                      └────────┬───────┘
         │                                               │
         │                                               ▼
   ┌─────┴──────┐    QC pass    ┌─────────────────────────────┐
   │  Season    │◀──────────────│  Rankings + head-to-head    │
   │  (frozen)  │               │  matches (public)           │
   └────────────┘               └─────────────────────────────┘
```

Every active **season** freezes a set of prompt versions and model
snapshots. The cron route at `/api/cron/benchmark-run` walks every
prompt × model combination, requires the model to produce a strict
machine-readable appendix, parses each response into a case decision
(`tool` / `none` / `invalid`), and publishes runs that pass QC.

Public pages, including rankings, category indexes, and head-to-head matches,
only read from published benchmark data. Unrecognized tool names are held in a
candidate queue for admin review rather than guessed at.

## Tech stack

- **Next.js 15** (App Router, React Server Components)
- **tRPC v11**: typed API
- **Drizzle ORM** + **Supabase** (Postgres + email-OTP auth)
- **OpenRouter**: model gateway
- **Tailwind CSS v4** + **shadcn/ui**
- **Vitest** + Testcontainers for an integration-tested Postgres
- **Biome** for lint + format

## Documentation

### Get started

- `docs/SETUP.md`: local development environment
- `docs/SELF_HOSTING.md`: supported deployment path
- `docs/CONFIGURATION.md`: every env var explained

### Learn more

- `docs/ARCHITECTURE.md`: system overview
- `docs/CONCEPTS.md`: glossary of project terms
- `docs/METHODOLOGY.md`: how rankings are produced
- `docs/ROADMAP.md`: what's planned next

### Deep dives
- How Benchmarks Work
- How Prompts Work
- How Rankings Work
- How Cron Benchmarks Work
- How Matches Work
- How LLM Service Works
- How Evals Work
- Recommendation Methodology

## Contributing

Pull requests are very welcome. See `CONTRIBUTING.md` for
how to set up, what we look for in PRs, and our triage SLA. New to the
project? Look for issues labelled
`good first issue`.

We follow the Contributor Covenant. Security reports
go through `SECURITY.md`.

## License

MIT. See the `LICENSE` file. Third-party tool logos under
`public/logos/` are used under nominative fair use; see
`docs/LOGO_POLICY.md`.

# Recommender Query Language (RecQL)

## 关联链接

- https://preseason.ai

## 导航

- 项目页：[[10-项目/github.com_a5d6f579]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
