---
type: "corpus"
item_id: "f0af76a98c789474"
title: "kirillpolevoy/claude-saas-eval-skills"
source: "github_new"
source_name: "GitHub 新星仓库"
url: "https://github.com/kirillpolevoy/claude-saas-eval-skills"
project_url: "https://github.com/kirillpolevoy/claude-saas-eval-skills"
author: "kirillpolevoy"
published_at: "2026-01-24T19:32:06Z"
captured_at: "2026-09-20T09:36:30+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-01-24"
tags:
  - 语料
  - github_new
  - topic:indie-hacker
metrics: {"stars": 2, "forks": 1, "open_issues": 1}
comments_count: 0
comments_total: 0
discovered_via: "github:14d"
---

# kirillpolevoy/claude-saas-eval-skills

> [!info] 一句话导读
> SaaS Niche Research & Evaluation Skills

> [!meta]- 语料信息（点开展开）
> 来源：GitHub 新星仓库（post）
> 原帖：<https://github.com/kirillpolevoy/claude-saas-eval-skills>
> 指标：stars=2 · forks=1 · open_issues=1
> 作者：kirillpolevoy　|　发布：2026-01-24T19:32:06Z
> 项目链接：<https://github.com/kirillpolevoy/claude-saas-eval-skills>
> 采集：2026-09-20T09:36:30+08:00　|　id：`f0af76a98c789474`

## 正文

# SaaS Niche Research & Evaluation Skills

[![Claude Code Skills](https://img.shields.io/badge/Claude%20Code-Skills-blue)](https://github.com/kirillpolevoy/lifestyle-saas-skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub release](https://img.shields.io/github/v/release/kirillpolevoy/lifestyle-saas-skills)](https://github.com/kirillpolevoy/lifestyle-saas-skills/releases)

Claude Code skills for discovering and evaluating niche SaaS opportunities through a lifestyle business lens.

## Who This Is For

Indie founders, solo developers, and small teams building vertical SaaS for **$1–3M ARR**—not VC-track startups chasing $100M outcomes.

If you want to build a business that:
- Runs with 1–2 people
- Doesn't require venture funding
- Generates $80K–$250K+ net income
- Has manageable support burden
- Lets you own your time

...these skills will help you avoid bad niches and identify good ones.

## Philosophy

### Distribution First

Most niche ideas die because founders can't reach buyers. These skills treat distribution as a **non-negotiable gate**—if you can't identify a concrete path to customers (buyer list, channel partner, high-intent inbound), the niche fails immediately.

### Paperwork Wedge

The best lifestyle SaaS opportunities sit on top of **mandatory workflows**: compliance filings, certification renewals, audit logs, permit applications. These create urgency, recurring need, and willingness to pay.

### Lifestyle Math

Every evaluation includes the math: How many customers at what ARPA to hit $1M ARR? $3M ARR? If the answer requires 5,000+ customers, it's probably not a lifestyle business.

### Founder Fit

A technically viable niche that makes you miserable is still a bad niche. These skills prompt you to check whether you'd actually enjoy the market long-term.

## The Skills

### 1. Niche Idea Generator

**Purpose:** Generate concrete niche SaaS ideas based on your unique advantages (expertise, access, background).

**When to use:**
- You want to discover opportunities that match your strengths
- You're exploring what niches to pursue
- You have domain expertise but need specific ideas
- You want ideas with built-in distribution advantages

**Outputs:**
- 5–10 concrete niche hypotheses
- Each with paperwork wedge, distribution path, and lifestyle math
- Ranked by founder fit
- Ready for First Pass evaluation

**Location:** `niche-idea-generator/SKILL.md`

---

### 2. Niche Research — First Pass

**Purpose:** Rapid evaluation of a niche hypothesis to determine if it's worth deeper research.

**When to use:**
- You have a one-sentence niche idea
- You want to know if it passes basic viability checks
- You need to decide whether to spend time on validation

**Outputs:**
- Structured assessment of customer, workflow, distribution, and buildability
- Clear Pursue / Hold / Kill verdict
- 7-day validation plan

**Location:** `niche-research-first-pass/SKILL.md`

---

### 3. Niche Success Scorecard

**Purpose:** Quantitative scoring of a niche after initial research is complete.

**When to use:**
- After completing a First Pass evaluation
- When you have concrete data and want a structured decision
- When comparing multiple niches

**Outputs:**
- Weighted score (0–100)
- Clear decision thresholds
- 2-week validation plan with go/no-go criteria

**Location:** `niche-success-scorecard/SKILL.md`

## How to Use

### Workflow

```
Idea Generator → 5-10 Hypotheses
                        ↓
               First Pass (each idea) → [Kill / Hold / Pursue]
                                              ↓
                                        Scorecard → [Kill / Hold / Pursue-Conditional / Pursue]
                                                          ↓
                                                    Validation Plan
```

1. **Start with Idea Generator** if you need niche hypotheses based on your background
2. **Use First Pass** to rapidly evaluate each hypothesis (or your own ideas)
3. **Run Scorecard** only on ideas that pass First Pass with Pursue or Hold
4. **Execute validation plan** from Scorecard before committing

### Installation

#### Claude Code (Recommended)

Copy the skill folders to your Claude Code skills directory:

```bash
# Clone the repo
git clone https://github.com/kirillpolevoy/lifestyle-saas-skills.git

# Copy to your skills directory
cp -r lifestyle-saas-skills/niche-idea-generator ~/.claude/skills/
cp -r lifestyle-saas-skills/niche-research-first-pass ~/.claude/skills/
cp -r lifestyle-saas-skills/niche-success-scorecard ~/.claude/skills/

# Restart Claude Code to load the new skills
```

#### Manual Use

Copy the contents of each `SKILL.md` into your Claude conversation as context before asking for an evaluation.

## Example Usage

**Idea Generator:**
```
Generate niche SaaS ideas for me. Background: 5 years as compliance officer at regional bank. Access: Former colleagues at 20+ credit unions in Southeast. Interests: Would enjoy serving financial services long-term. Geography: Southeast US.
```

**First Pass:**
```
Evaluate this niche: Software for HVAC contractors to manage EPA 608 certification renewals and refrigerant tracking logs. Geography: US.
```

**Scorecard:**
```
Score the HVAC certification tracking niche using the lifestyle SaaS scorecard. Here's the first pass data: [paste first pass output]
```

## Decision Thresholds

### First Pass Verdicts

| Verdict | Meaning |
|---------|---------|
| **Pursue** | Clear distribution + viable pricing + buildable. Move to Scorecard. |
| **Hold** | Promising but missing signal. Needs specific research. |
| **Kill** | No distribution OR requires too many customers OR unbuildable. Move on. |

### Scorecard Thresholds

| Score | Decision |
|-------|----------|
| 80–100 | Pursue aggressively |
| 65–79 | Pursue conditionally (clear specific risks first) |
| 50–64 | Hold |
| < 50 | Kill |

## Scoring Weights

| Dimension | Weight | Why |
|-----------|--------|-----|
| Distribution | 35% | Can't build a business if you can't reach buyers |
| ARPA / Path to $1–3M | 20% | Lifestyle math must work |
| Willingness to Pay | 15% | Nice-to-have software dies |
| Scope + Support | 15% | Solo/duo must be able to build and maintain |
| Expandability | 10% | Growth from $1M to $3M requires expansion vectors |
| Competition | 5% | Matters less when distribution is strong |

## What These Skills Won't Do

- Tell you the niche is guaranteed to work
- Replace customer interviews
- Build the product for you
- Make decisions for you (you still need to validate)

They will help you **discover opportunities**, **kill bad ideas faster**, and **spend validation time on better ones**.

## Background

Created by a founder building vertical SaaS after leaving a previous role. These frameworks emerged from evaluating dozens of niche opportunities and learning (often the hard way) which signals actually matter for lifestyle-scale businesses.

## Contributing

Found a gap? Have a niche pattern that should be included? Open an issue or PR.

## License

MIT — use however you want.

## 关联链接

- https://github.com/kirillpolevoy/lifestyle-saas-skills
- https://github.com/kirillpolevoy/lifestyle-saas-skills.git
- https://github.com/kirillpolevoy/lifestyle-saas-skills/releases
- https://img.shields.io/badge/Claude%20Code-Skills-blue
- https://img.shields.io/badge/License-MIT-yellow.svg
- https://img.shields.io/github/v/release/kirillpolevoy/lifestyle-saas-skills
- https://opensource.org/licenses/MIT

## 导航

- 项目页：[[10-项目/github.com_f0af76a9]]
- 渠道页：[[50-渠道/github_new]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
