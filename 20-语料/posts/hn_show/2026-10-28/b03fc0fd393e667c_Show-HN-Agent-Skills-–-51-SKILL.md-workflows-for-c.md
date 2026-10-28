---
type: "corpus"
item_id: "b03fc0fd393e667c"
title: "Show HN: Agent Skills – 51 SKILL.md workflows for coding agents and marketers"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50265176"
project_url: "https://github.com/milad-ahmd/agent-skills"
author: "milad_ahmd"
published_at: "2026-10-27T20:16:56Z"
captured_at: "2026-10-28T09:39:16+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-28"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_milad_ahmd
  - story_50265176
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Agent Skills – 51 SKILL.md workflows for coding agents and marketers

> [!info] 一句话导读
> milad-ahmd/agent-skills

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50265176>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：milad_ahmd　|　发布：2026-10-27T20:16:56Z
> 项目链接：<https://github.com/milad-ahmd/agent-skills>
> 采集：2026-10-28T09:39:16+08:00　|　id：`b03fc0fd393e667c`

## 正文

# milad-ahmd/agent-skills

🧰 51 Agent Skills: roast your GitHub, an AI agent for every social platform, senior-engineer dev workflows. Role packs + one-line install. Claude Code, Cline, Cursor, Codex

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- License: MIT License
- Homepage: https://milad-ahmd.github.io/agent-skills/
- Default branch: main
- Created: 2026-10-25T13:31:35Z

## Languages

- HTML
- Python
- Shell

## Topics

- agent-skills
- agent-skills-collection
- ai-agents
- ai-tools
- claude-code
- claude-code-plugin
- claude-skills
- cline
- cursor
- facebook
- instagram
- linkedin
- marketing
- pinterest
- skill-md
- social-media
- telegram
- tiktok
- whatsapp
- youtube

## Top Contributors

- milad-ahmd (9 contributions)

---

## README

# 🧰 Agent Skills

### 51 Agent Skills that give your AI superpowers: senior-engineer workflows, an agent for every social platform, and a few that are just fun.

**Works with Claude Code · Cline · Cursor · Codex · any agent that reads `SKILL.md`**

Stars
License: MIT
Skills
PRs Welcome

🌐 Website · Install · Demos · Packs · Platform agents · Marketing skills · Developer skills · What is a skill? · Awesome list

---

## ⚡ Install in 10 seconds

### Option 1: Claude Code plugin (recommended)

```text
/plugin install all-skills --marketplace milad-ahmd/agent-skills
```

Or install just one pack:

```text
/plugin install creator-pack --marketplace milad-ahmd/agent-skills
/plugin install marketer-pack --marketplace milad-ahmd/agent-skills
/plugin install indie-hacker-pack --marketplace milad-ahmd/agent-skills
/plugin install local-business-pack --marketplace milad-ahmd/agent-skills
/plugin install startup-cto-pack --marketplace milad-ahmd/agent-skills
/plugin install developer-pack --marketplace milad-ahmd/agent-skills
/plugin install skill-builder-pack --marketplace milad-ahmd/agent-skills
/plugin install fun-pack --marketplace milad-ahmd/agent-skills
```

On older Claude Code versions, run `/plugin marketplace add milad-ahmd/agent-skills` first.

### Option 2: `npx skills` (Cursor, Codex, Cline, Windsurf, Copilot and 75+ agents)

```bash
npx skills add milad-ahmd/agent-skills                          # pick skills interactively
npx skills add milad-ahmd/agent-skills --skill roast-my-github  # one skill
```

### Option 3: shell installer

```bash
# all 51 skills
curl -fsSL https://raw.githubusercontent.com/milad-ahmd/agent-skills/main/install.sh | bash

# or a role-based pack
curl -fsSL https://raw.githubusercontent.com/milad-ahmd/agent-skills/main/install.sh | bash -s -- --pack creator

# or only the ones you want
curl -fsSL https://raw.githubusercontent.com/milad-ahmd/agent-skills/main/install.sh | bash -s -- pr-reviewer-pro env-secrets-guard

# project-local install (commit it so your whole team gets the skills)
curl -fsSL https://raw.githubusercontent.com/milad-ahmd/agent-skills/main/install.sh | SKILLS_DIR=.claude/skills bash
```

Then just talk to your agent normally. It picks the right skill automatically.

### 🎒 Packs: install by who you are

| Pack | For | Includes |
|---|---|---|
| `indie-hacker` | Solo founders | idea validation, landing page roast, launch posts, ASO, SEO, X & Reddit |
| `creator` | Creators & influencers | Instagram, TikTok, YouTube, repurposing, hooks, calendar, analytics |
| `marketer` | Marketing teams | brand voice, ads, email, SEO, competitors, influencers, analytics |
| `local-business` | Shops, clinics, restaurants | Google Business Profile, WhatsApp, Facebook, Instagram |
| `startup-cto` | Engineering leads | PR review, incidents, cost cutting, secrets, deps, migrations |
| `developer` | Every dev | the 12 core dev workflow skills |
| `skill-builder` | Skill authors | skill-creator-pro, skills-doctor, agent-memory-keeper |
| `fun` | Everyone | roast-my-github, codebase-time-machine, landing-page-roaster, ai-slop-detector |

Run `install.sh --list` to see every skill and pack.

## 🎬 See them in action (real output, not mockups)

| 🔥 roast-my-github | ⏳ codebase-time-machine |
|---|---|
| | |
| **🔐 env-secrets-guard** | **🧹 ai-slop-detector** |
| | |
| **🩺 skills-doctor** | **📊 social-analytics-reporter** |
| | |

## 🎉 Fun & Viral (new!)

| Skill | What it does | Try saying |
|---|---|---|
| 🔥 **roast-my-github** | Get your GitHub profile roasted with real data, then a scorecard and glow-up plan | *"Roast my GitHub: milad-ahmd"* |
| 🦈 **startup-idea-validator** | Stress-test a startup idea with a VC, customer and competitor panel, cheap experiments and a verdict | *"Validate my startup idea: ..."* |
| ⏳ **codebase-time-machine** | The story of your repo from git history, as a documentary: eras, cast, plot twists, cursed files | *"Tell me the story of this codebase"* |
| 🧹 **ai-slop-detector** | Score text for AI-sounding writing and rewrite it to sound human, keeping the author's voice | *"De-slop this blog post"* |

## 🦸 Agent Superpowers (new!)

| Skill | What it does | Try saying |
|---|---|---|
| 🧠 **agent-memory-keeper** | Persistent project memory (MEMORY.md) so your agent stops repeating the same mistakes | *"Remember that we use pnpm, not npm"* |
| 🛠️ **skill-creator-pro** | Turn any workflow into a well-written SKILL.md, with a linter to validate it | *"Create a skill for our release process"* |
| 🩺 **skills-doctor** | Audit your installed skills for broken frontmatter, vague triggers, conflicts and leaked secrets | *"Check my installed skills"* |

## 🛠️ Ops & Growth (new!)

| Skill | What it does | Try saying |
|---|---|---|
| 💸 **cost-cutter** | Cut cloud, SaaS and LLM API bills with dollar estimates, effort, risk and exact fixes | *"Why is our AWS bill so high?"* |
| 🚨 **incident-commander** | Run a production outage from triage to mitigation, status updates and a blameless postmortem | *"Production is down, help me"* |
| 📱 **app-store-optimizer** | App Store and Google Play ASO: keywords, titles, screenshot captions, review replies, A/B tests | *"Optimize my App Store listing"* |

## 🤖 Social Platform Agents

One complete agent skill per platform. Each one handles profile setup, content, engagement and analytics for its platform. Start with **social-media-manager**, which decides which platforms you need and coordinates the rest.

| Skill | What it does | Try saying |
|---|---|---|
| 🧠 **social-media-manager** | All-in-one social media manager: picks platforms, sets KPIs, plans weekly and directs every platform skill | *"Manage my brand's social media"* |
| 💼 **linkedin-growth-manager** | LinkedIn profile rewrite, post writing, comment strategy and analytics for personal brands and company pages | *"Rewrite my LinkedIn headline and About"* |
| 𝕏 **x-twitter-growth-manager** | Grow on X/Twitter with profile, daily posts, threads, a reply strategy and analytics | *"Write a thread about what I learned building X"* |
| 👍 **facebook-page-manager** | Facebook Pages and Groups: setup, posts, Reels, Messenger replies, reviews and boosting | *"Set up and plan content for my Facebook page"* |
| 📌 **pinterest-growth-manager** | Pinterest SEO: keywords, boards, Pin titles and descriptions, and seasonal plans for traffic | *"Create a Pinterest strategy for my blog"* |
| 🧵 **threads-growth-manager** | Grow on Meta Threads with conversation-starting posts, reply strategy and a content bank | *"Write 20 Threads posts for my brand"* |
| 👽 **reddit-marketing-agent** | Authentic Reddit marketing: subreddit research and rules, value-first posts and launch posts | *"Find subreddits where I can share my app"* |
| ✈️ **telegram-channel-manager** | Grow and run a Telegram channel or group: content, formatting, moderation and monetization | *"Plan a content calendar for my Telegram channel"* |
| 💬 **whatsapp-business-agent** | WhatsApp Business for sales and support: quick replies, broadcasts, API templates and chatbot flows | *"Set up WhatsApp Business replies for my shop"* |
| 📍 **google-business-profile-manager** | Rank on Google Maps: Google Business Profile optimization, posts, reviews and local SEO | *"Optimize my Google Business Profile"* |

## 📣 Marketing & Content Skills

Your AI agent can also act as a social media manager, content strategist and growth marketer.

| Skill | What it does | Try saying |
|---|---|---|
| 📸 **instagram-growth-manager** | Grow and manage Instagram with bio audits, Reels scripts, carousels, captions, hashtags and growth reviews | *"Audit my Instagram profile and plan next month"* |
| 🎵 **tiktok-viral-creator** | TikTok ideas, 2-second hooks, shot-by-shot scripts and retention analysis | *"Give me 10 TikTok ideas for my fitness app"* |
| 📺 **youtube-seo-optimizer** | YouTube titles, thumbnails, descriptions, chapters and channel audits for more views | *"Optimize the title and description for this video"* |
| 🎬 **youtube-script-writer** | High-retention YouTube and Shorts scripts with hooks, open loops and B-roll cues | *"Write a 10-minute YouTube script about X"* |
| ♻️ **content-repurposer** | One video or podcast into 15+ posts: Shorts, Reels, threads, LinkedIn, carousel, newsletter | *"Repurpose this transcript into social posts"* |
| 🗓️ **social-media-calendar** | Monthly cross-platform content calendar, exported as CSV for Notion, Sheets, Buffer or Later | *"Plan my social media calendar for November"* |
| 🪝 **hook-generator** | Scroll-stopping hooks for videos, posts, emails and ads, scored and ranked | *"Give me hooks for a video about X"* |
| 📣 **ad-copy-generator** | Ad copy for Meta, TikTok, Google and YouTube within each platform's limits, plus an A/B test matrix | *"Write Meta ads for my product"* |
| ✍️ **seo-blog-writer** | SEO blog posts that rank: intent research, outline, meta tags, FAQ and schema | *"Write an SEO article for 'best budgeting apps'"* |
| 📧 **email-campaign-writer** | Welcome, launch, cart and newsletter email sequences with subject-line tests | *"Write a 5-email welcome sequence"* |
| 🎨 **brand-voice-guide** | A brand voice, positioning and personas guide, then rewrites copy on-brand | *"Create a brand voice guide from our website"* |
| 🕵️ **competitor-spy** | Competitor analysis of pricing, messaging, socials, ads and reviews, with a SWOT and opportunities | *"Analyze my top 3 competitors"* |
| 🤝 **influencer-outreach** | Influencer and UGC campaigns: vetting, outreach DMs, briefs and tracking | *"Plan a micro-influencer campaign on TikTok"* |
| 📊 **social-analytics-reporter** | Social media analytics exports into a clear report with KPIs, reasons and next actions | *"Analyze this Instagram Insights export"* |

## 💻 Developer Skills

### 🔀 Git & Workflow
| Skill | What it does | Try saying |
|---|---|---|
| 🔎 **pr-reviewer-pro** | Senior-engineer PR reviews: severities, `file:line` evidence, suggested fixes | *"Review PR #123"* |
| 🧱 **commit-craft** | Messy changes → clean, atomic Conventional Commits | *"Commit my changes"* |
| 📋 **meeting-notes-to-tickets** | Meeting notes → de-duplicated GitHub/Linear/Jira tickets | *"Turn these notes into issues"* |
| 📝 **changelog-from-git** | Human-readable release notes from git history | *"Write release notes since v1.2"* |

### 🧪 Testing & Quality
| Skill | What it does | Try saying |
|---|---|---|
| 🧪 **test-gap-hunter** | Finds the riskiest untested code and writes real tests | *"Find test gaps and fix the top 3"* |

### 🎨 Frontend
| Skill | What it does | Try saying |
|---|---|---|
| 🖼️ **screenshot-to-component** | Screenshot → component in *your* design system | *"Build this screenshot as a component"* |
| ♿ **a11y-fixer** | WCAG 2.2 AA audit that fixes issues in code | *"Make this app accessible"* |

### 🧙 Refactoring
| Skill | What it does | Try saying |
|---|---|---|
| 🧙 **migration-wizard** | Safe, phased migrations: JS→TS, Jest→Vitest, Pages→App Router | *"Migrate this project to TypeScript"* |

### 🔐 Security & Maintenance
| Skill | What it does | Try saying |
|---|---|---|
| 🔐 **env-secrets-guard** | Catches leaked API keys before you push | *"Scan for leaked secrets"* |
| 🩺 **dependency-doctor** | Vulnerable, outdated and unused packages with a safe upgrade plan | *"Check my dependencies"* |

### 🐳 DevOps & Backend
| Skill | What it does | Try saying |
|---|---|---|
| 🐳 **dockerize-anything** | Small, secure, multi-stage Dockerfile and compose | *"Dockerize this project"* |
| 🔌 **api-to-sdk** | Typed, idiomatic SDK from OpenAPI or your routes | *"Generate a TS SDK from openapi.yaml"* |
| ⚡ **sql-optimizer** | Explains slow queries and suggests indexes and rewrites | *"Why is this query slow?"* |

### 📚 Documentation
| Skill | What it does | Try saying |
|---|---|---|
| ✨ **readme-glow-up** | Turns any README into a star magnet | *"Glow up my README"* |
| 🗺️ **codebase-explainer** | Onboarding guide with Mermaid architecture diagrams | *"Explain this codebase"* |

### 🚀 Growth
| Skill | What it does | Try saying |
|---|---|---|
| 🚀 **launch-post-writer** | X thread, Show HN, LinkedIn and Reddit posts from your repo | *"Write launch posts for this repo"* |
| 🔥 **landing-page-roaster** | Scored, funny, honest roast of your landing page plus rewrites | *"Roast my landing page"* |

## 🤔 What is a skill?

A skill is a folder with a `SKILL.md` file: YAML frontmatter (`name`, `description`) followed by instructions, plus optional scripts. Your agent reads the description and loads the full instructions **only when the task matches**, so your context stays clean and the agent follows a proven workflow instead of improvising.

```text
~/.claude/skills/
└── pr-reviewer-pro/
    ├── SKILL.md
    └── scripts/collect_diff.sh
```

**Agent without native skill support?** Paste any `SKILL.md` into your rules file (`.clinerules`, `.cursor/rules`, `AGENTS.md`, `CLAUDE.md`).

## 🧠 Design principles

Every skill in this collection:
- ✅ **Investigates before acting.** It reads your repo and follows your conventions.
- ✅ **Never invents facts.** It cites evidence and marks unknowns as TODOs.
- ✅ **Asks before anything destructive**, such as pushing, force-pushing, deleting or posting.
- ✅ **Produces a clear, structured output** you can act on immediately.

## 🗺️ Roadmap

All 51 skills have shipped. A new skill drops every Monday (changelog). Next up is your idea:

👉 Request a skill. Popular requests get built first.

## 🤝 Contributing

Ideas, bug reports and new skills are welcome. Each skill lives in its own repo, so open issues there. You can also browse community skills in awesome-agent-skills.

## 📄 License

MIT © Milad Ahmadi

### ⭐ If these skills save you time, star the repo so other developers can find them.

## 关联链接

- https://milad-ahmd.github.io/agent-skills/
- https://raw.githubusercontent.com/milad-ahmd/agent-skills/main/install.sh

## 导航

- 项目页：[[10-项目/github.com_a3cc3f07]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
