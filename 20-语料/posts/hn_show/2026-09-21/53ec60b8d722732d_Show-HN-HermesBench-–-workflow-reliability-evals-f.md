---
type: "corpus"
item_id: "53ec60b8d722732d"
title: "Show HN: HermesBench – workflow reliability evals for personal AI agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48341436"
project_url: "https://verkyyi.github.io/hermesbench"
author: "verkyyi26"
published_at: "2026-05-30T23:03:40Z"
captured_at: "2026-09-21T02:52:49+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-30"
tags:
  - 语料
  - hn_show
  - author_verkyyi26
  - story_48341436
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:144d"
---

# Show HN: HermesBench – workflow reliability evals for personal AI agents

> [!info] 一句话导读
> Hermes Agent runtime evaluation

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48341436>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：verkyyi26　|　发布：2026-05-30T23:03:40Z
> 项目链接：<https://verkyyi.github.io/hermesbench>
> 采集：2026-09-21T02:52:49+08:00　|　id：`53ec60b8d722732d`

## 正文

HermesBench
Quick start
 Recipes
 Profiles
 Traces
 Feedback
 Contribute
 GitHub
Hermes Agent runtime evaluation
Benchmark the whole personal agent, not just the model.
HermesBench evaluates complete Hermes configurations: prompt,
 model/provider, tools, AgentSkills, memory, gateway behavior,
 delegation, safety, latency, and stability. The current public
 baseline scores 78.2 across 27 personal-agent recipes with
 redacted traces you can inspect.
Inspect the baseline
 Run one recipe
 Star on GitHub
 Give feedback
78.2
 current public baseline
27
 workflow recipes
9
 scored suites
Why trust it
Evidence first, with visible limits.
Every published result links back to scenario definitions, public
 score axes, driver closure decisions, deterministic checks, and
 redacted trace timelines. The site is deliberately clear that this
 is one early baseline, not a base-model leaderboard.
Public recipes
 See the prompts
 27 user-like personal-agent jobs with criteria and side-effect boundaries.
Redacted traces
 Inspect what happened
 Tool timelines, assistant replies, checks, and judge summaries without raw private payloads.
Methodology
 Understand the score
 Capability, reliability, and UX axes with documented limitations.
Site map
Three tabs for the current evidence shape.
With one baseline published, a leaderboard is premature. The site
 now starts from the content people need to navigate: recipes,
 profiles, and traces.
Recipes
 What was tested
 Search by category, prompt, goal, and criteria.
Profiles
 What setup ran
 Review profile units, roles, and observed tools.
Traces
 What happened
 Open redacted transcripts, tool timelines, checks, and judge reasoning.
Agent-driven quick start
Run it through a coding agent.
The public user pathway is intentionally simple: copy the prompt to
 Codex, Claude, or another coding agent. The agent loads the
 HermesBench skill and drives one scenario recipe first. Full bundle
 runs are opt-in because they take longer and cost more.
Prompt to copy into Codex or Claude
Use the HermesBench skill and run one default scenario recipe for my current Hermes configuration.
Skill: https://github.com/verkyyi/hermesbench/blob/main/agent-skills/hermesbench/SKILL.md
Follow the skill's "Run Current Hermes Configuration" workflow. Use the Python API default single-recipe path, save artifacts, and summarize the score and main findings. Do not run the full bundle unless I explicitly ask.
Alpha feedback
The best next action is concrete feedback.
HermesBench needs early feedback on setup friction, scoring
 surprises, recipe realism, profile evidence, and redaction trust.
 Star the repo if the benchmark shape is useful; open an issue if
 one recipe, trace, or score axis feels wrong.
Open feedback issue
 Read feedback guide
 Submission contract
Coverage model
Workflow recipes, broad personal-agent coverage.
HermesBench starts with one valuable workflow recipe, then lets you opt into
 broader suites when you need more confidence. The bundled catalog
 covers everyday personal-agent work: context, calendar, web,
 reports, communication, location, travel, finance, safety, and
 power-user integrations.
Browse recipes
Personal core
 Communications
 Ambient and travel
 Private sensitive
 Power-user optional
Scoring philosophy
Good agents finish the right thing safely.
Outcome reached
 Evidence / truthfulness
 Runtime / scope safety
 Responsiveness
 Task fulfillment
 Communication quality
HermesBench is reliability-first, but not capability-blind. A good
 configuration should do useful work, tell the truth about what it
 knows, avoid unsafe side effects, stay stable, respond promptly, and
 communicate clearly. Lopsided scores are penalized because a personal
 agent that is capable but unsafe, safe but unhelpful, or correct but
 unusably slow is not actually good.
Detailed formulas and implementation mechanics live in the methodology
 document; the website keeps the scoring model readable for users and
 LLM agents.
Use and contribute
Turn good results into reusable recipes.
HermesBench is useful as a quick benchmark, but it is also a way to
 publish what worked. Share a redacted profile/config package when a
 setup improves a recipe, or submit a generic recipe when an
 important personal-agent use case is missing.
Profile submission prompt
Use the HermesBench skill to prepare my current Hermes profile/config as a public profile submission.
Skill: https://github.com/verkyyi/hermesbench/blob/main/agent-skills/hermesbench/SKILL.md
Run one representative recipe first, package the redacted profile snapshot and score evidence, and tell me what must be reviewed before opening a pull request.
Recipe submission prompt
Use the HermesBench skill to propose a new generic personal-agent recipe for HermesBench.
Skill: https://github.com/verkyyi/hermesbench/blob/main/agent-skills/hermesbench/SKILL.md
Make the use case privacy-safe, driver/target agnostic, fixture-backed where possible, and include deterministic checks before preparing a pull request.
HermesBench
 GitHub
 Recipes
 Profiles
 Traces
 llms.txt
 Feedback
 Methodology
 Local suites

## 关联链接

- https://github.com/verkyyi/hermesbench/blob/main/agent-skills/hermesbench/SKILL.md

## 导航

- 项目页：[[10-项目/verkyyi.github.io_08c1d3db]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
