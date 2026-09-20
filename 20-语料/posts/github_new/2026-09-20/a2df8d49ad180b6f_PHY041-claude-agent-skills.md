---
type: "corpus"
item_id: "a2df8d49ad180b6f"
title: "PHY041/claude-agent-skills"
source: "github_new"
source_name: "GitHub 新星仓库"
url: "https://github.com/PHY041/claude-agent-skills"
project_url: "https://github.com/PHY041/claude-agent-skills"
author: "PHY041"
published_at: "2026-02-20T12:20:17Z"
captured_at: "2026-09-20T09:36:28+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-02-20"
tags:
  - 语料
  - github_new
  - topic:indie-hacker
metrics: {"stars": 18, "forks": 1, "open_issues": 0}
comments_count: 0
comments_total: 0
discovered_via: "github:14d"
---

# PHY041/claude-agent-skills

> [!info] 一句话导读
> Collection of Claude Code Agent Skills for founders, indie hackers, and growth engineers.

> [!meta]- 语料信息（点开展开）
> 来源：GitHub 新星仓库（post）
> 原帖：<https://github.com/PHY041/claude-agent-skills>
> 指标：stars=18 · forks=1 · open_issues=0
> 作者：PHY041　|　发布：2026-02-20T12:20:17Z
> 项目链接：<https://github.com/PHY041/claude-agent-skills>
> 采集：2026-09-20T09:36:28+08:00　|　id：`a2df8d49ad180b6f`

## 正文

# claude-agent-skills

Collection of Claude Code Agent Skills for founders, indie hackers, and growth engineers.

Built to work with [OpenClaw](https://openclaw.ai) and [Claude Code](https://claude.ai/code).

Inspired by [apify/agent-skills](https://github.com/apify/agent-skills).

---

## Composite Skills

Composite skills orchestrate multiple atomic skills with defined I/O contracts and feedback loops. One trigger → full workflow.

| Composite | Orchestrates | Description |
|-----------|-------------|-------------|
| [content-flywheel](composite/content-flywheel/) | ship-digest → founder-content → social-post → engagement-tracker → content-multiply | Full build-in-public content loop |
| [gtm-engine](composite/gtm-engine/) | brand-monitor → lead-generation → (scoring) → outreach | Competitive intel + lead pipeline |

---

## Atomic Skills

| Skill | Description |
|-------|-------------|
| [brand-monitor](skills/brand-monitor/) | Reddit brand & market intelligence engine. AI-powered onboarding — give it a brand name and it auto-generates the monitoring strategy. |
| [content-multiply](skills/content-multiply/) | Data-driven content multiplication engine. Detects high-performing posts and auto-generates adapted versions for other platforms. |
| [engagement-tracker](skills/engagement-tracker/) | Track engagement metrics on all posted content. Produces weekly analysis with actionable insights. |
| [exa-web-search-free](skills/exa-web-search-free/) | Free AI search via Exa MCP. Web search, code search, company research — no API key needed. |
| [founder-content](skills/founder-content/) | Complete content creation and multiplication system for founders. Social posts, threads, build-in-public updates. |
| [github-monitor](skills/github-monitor/) | Monitor your GitHub repos for new projects and updates. Auto-generates Reddit + Twitter draft posts for approval. |
| [lead-generation](skills/lead-generation/) | Find high-intent buyers in live social conversations using Xpoz MCP. |
| [reddit-cultivate](skills/reddit-cultivate/) | Reddit account cultivation via AppleScript Chrome control — undetectable by anti-bot systems. |
| [ship-digest](skills/ship-digest/) | Detect new GitHub repos and generate formatted ship announcements for social media. |
| [social-post](skills/social-post/) | Post to 9+ platforms via multi-provider API (PostForMe + LATE) with automatic fallback. |
| [twitter-cultivate](skills/twitter-cultivate/) | Twitter/X account cultivation and growth system based on the open-source algorithm analysis. |
| [xhs-image-gen](skills/xhs-image-gen/) | Generate Xiaohongshu carousel images (3:4, 1080×1440) with Chinese typography. |

---

## How to Install

### With OpenClaw

Copy any skill folder into your OpenClaw skills directory:

```bash
cp -r skills/reddit-cultivate ~/.openclaw/skills/
```

### With Claude Code

1. Clone this repo
2. In your Claude session, point to a skill:
   > "Read the SKILL.md at `./skills/reddit-cultivate/SKILL.md` and follow it to..."

---

## Platform Support

| Platform | Skills |
|----------|--------|
| Reddit | reddit-cultivate, brand-monitor, engagement-tracker |
| Twitter/X | twitter-cultivate, lead-generation, social-post |
| LinkedIn | social-post, founder-content |
| Xiaohongshu | xhs-image-gen, founder-content |
| GitHub | github-monitor, ship-digest |
| Multi-platform | content-multiply, engagement-tracker, founder-content |

---

## Platform-Specific Packages

Skills in this repo are general-purpose. For platform-specific skill packages with deeper integration:

| Package | Platform | Description |
|---------|----------|-------------|
| [claude-skill-twitter](https://github.com/PHY041/claude-skill-twitter) | Twitter/X | Account growth, keyword intel (200+ tweets), content strategy. Powered by rnet (bypasses Cloudflare) |
| [claude-skill-reddit](https://github.com/PHY041/claude-skill-reddit) | Reddit | Account cultivation, karma tracking, subreddit engagement |
| [claude-skill-devto](https://github.com/PHY041/claude-skill-devto) | DEV.to | Article publishing, CSRF API integration, tag management |

## Built by

[PHY041](https://github.com/PHY041) — founder building in public

- 🏢 [CanMarket.AI](https://canmarket.ai) — AI Brand Operating System
- 🐦 [@Phy041](https://x.com/Phy041) on X
- 📖 More skills: [clawhub.com](https://clawhub.com)

## 关联链接

- https://canmarket.ai
- https://claude.ai/code
- https://clawhub.com
- https://github.com/PHY041
- https://github.com/PHY041/claude-skill-devto
- https://github.com/PHY041/claude-skill-reddit
- https://github.com/PHY041/claude-skill-twitter
- https://github.com/apify/agent-skills
- https://openclaw.ai
- https://x.com/Phy041

## 导航

- 项目页：[[10-项目/github.com_a2df8d49]]
- 渠道页：[[50-渠道/github_new]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
