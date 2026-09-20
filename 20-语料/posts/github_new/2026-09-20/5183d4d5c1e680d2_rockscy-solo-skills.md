---
type: "corpus"
item_id: "5183d4d5c1e680d2"
title: "rockscy/solo-skills"
source: "github_new"
source_name: "GitHub 新星仓库"
url: "https://github.com/rockscy/solo-skills"
project_url: "https://github.com/rockscy/solo-skills"
author: "rockscy"
published_at: "2026-04-30T07:58:41Z"
captured_at: "2026-09-20T09:36:28+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-04-30"
tags:
  - 语料
  - github_new
  - Shell
  - topic:indie-hacker
metrics: {"stars": 8, "forks": 0, "open_issues": 0}
comments_count: 0
comments_total: 0
discovered_via: "github:14d"
---

# rockscy/solo-skills

> [!info] 一句话导读
> Claude Code skills for people who ship alone.

> [!meta]- 语料信息（点开展开）
> 来源：GitHub 新星仓库（post）
> 原帖：<https://github.com/rockscy/solo-skills>
> 指标：stars=8 · forks=0 · open_issues=0
> 作者：rockscy　|　发布：2026-04-30T07:58:41Z
> 项目链接：<https://github.com/rockscy/solo-skills>
> 采集：2026-09-20T09:36:28+08:00　|　id：`5183d4d5c1e680d2`

## 正文

# solo-skills

> Claude Code skills for people who ship alone.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-7-blue.svg)](#skills)

English | [简体中文](README.zh.md)

```bash
curl -fsSL https://raw.githubusercontent.com/rockscy/solo-skills/main/install.sh | bash
```

---

## What is this?

A small, opinionated set of [Claude Code](https://claude.com/claude-code) skills for the tasks solo founders and indie devs actually do every day: writing launch tweets, replying to awkward customer emails, running a 5-minute personal standup, turning a vague bug report into something actionable, deciding what to ship next when you're alone with the call.

Most skill packs assume you have a team. **This one assumes you don't.**

---

## Why?

| | Most skill packs | solo-skills |
|---|---|---|
| Audience | "Real engineers" (broad) | Solo founders, indie devs |
| Boundaries | "Use when…" only | "Use when…" **AND "Do NOT use when…"** |
| Examples | Often abstract | Worked input → output for every skill |
| Install | Manual copy | One-line `curl \| bash` |

The **"Do NOT use when…"** section is the core differentiator. Force-applying a framework when it doesn't fit is the #1 way solo devs waste a Saturday. Every skill in this pack tells you when it should *not* fire.

---

## Skills

| Skill | What it does |
|---|---|
| [ship-decision](skills/ship-decision/SKILL.md) | Force a fast, regret-minimizing call between 2–3 product options. |
| [launch-tweet](skills/launch-tweet/SKILL.md) | Draft a launch tweet or 3–4 tweet thread, no hype words. |
| [changelog-from-commits](skills/changelog-from-commits/SKILL.md) | Convert raw git log into user-facing release notes. |
| [bug-from-user](skills/bug-from-user/SKILL.md) | Convert a confusing customer message into a reproducible bug report. |
| [standup-solo](skills/standup-solo/SKILL.md) | 5-minute personal standup: shipped / blocked / today's #1. |
| [email-customer](skills/email-customer/SKILL.md) | Polite-but-firm reply to refunds, scope creep, complaints. |
| [postmortem-solo](skills/postmortem-solo/SKILL.md) | ≤350-word blame-free postmortem after a missed deadline or outage. |

---

## Install

### Option 1: One-liner (recommended)

```bash
curl -fsSL https://raw.githubusercontent.com/rockscy/solo-skills/main/install.sh | bash
```

This drops the seven skill directories into `~/.claude/skills/`. Existing files of the same name are **never** overwritten — the installer skips them and tells you which.

### Option 2: Manual

```bash
git clone https://github.com/rockscy/solo-skills.git
cp -r solo-skills/skills/* ~/.claude/skills/
```

### Verify

Open Claude Code and type `/`. You should see `ship-decision`, `launch-tweet`, etc. in the skill list.

---

## How to use

Inside any Claude Code session, the skills auto-trigger when you describe a matching situation. You can also invoke explicitly:

```
/ship-decision

I'm stuck choosing between rebuilding my landing page in Framer or sticking with my hand-coded Next.js page. I have ~6 hours of focused time this weekend.
```

Claude reads `SKILL.md`, applies the framework, and responds in the prescribed format.

---

## Design principles

1. **Boundaries first.** Every skill leads with *when not to use*. Wrong skill > no skill.
2. **One sentence beats one paragraph.** Output formats enforce brevity.
3. **Show input → output.** Every skill includes a worked example, not just guidelines.
4. **No corporate voice.** No "I'm excited", no "per our policy", no emoji decoration.

---

## Contributing

PRs welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md). The bar:

- Skill solves a real problem a solo dev hits **monthly or more often**.
- Has a "When NOT to use" section. (Hard requirement.)
- Has at least one worked input → output example.
- Output format is concrete (table, structured text, fixed sections) — no "be helpful" vibes.

---

## License

[MIT](LICENSE) — copy, modify, ship, sell. No attribution required, but it's appreciated.

## 关联链接

- https://claude.com/claude-code
- https://github.com/rockscy/solo-skills.git
- https://img.shields.io/badge/License-MIT-yellow.svg
- https://img.shields.io/badge/skills-7-blue.svg
- https://raw.githubusercontent.com/rockscy/solo-skills/main/install.sh

## 导航

- 项目页：[[10-项目/github.com_5183d4d5]]
- 渠道页：[[50-渠道/github_new]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
