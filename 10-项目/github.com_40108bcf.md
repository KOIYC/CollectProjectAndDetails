---
type: "project"
title: "Show HN: Promptloop – create, run, and improve prompt evals from the terminal"
project_url: "https://github.com/Bella3202019/promptloop"
first_seen: "2026-09-21T02:52:59+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_velapod
  - story_48325073
  - show_hn
lang: "en"
---

# Show HN: Promptloop – create, run, and improve prompt evals from the terminal

> [!info] 一句话导读
> Bella3202019/promptloop

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/Bella3202019/promptloop>
> 首次收录：2026-09-21T02:52:59+08:00
> 来源渠道：HN Show HN
> 标签：author_velapod, story_48325073, show_hn
> 最新指标：点赞=13 · 评论=3 · engagement_velocity=13

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:27:24+08:00 | HN Show HN | 点赞=13 · 评论=3 · engagement_velocity=13 | [[20-语料/posts/hn_show/2026-09-21/23214676eb58d73b_Show-HN-Promptloop-–-create,-run,-and-improve-prom]] |
| 2026-09-21T01:44:09+08:00 | HN Show HN | 点赞=13 · 评论=3 · engagement_velocity=13 | [[20-语料/posts/hn_show/2026-09-21/23214676eb58d73b_Show-HN-Promptloop-–-create,-run,-and-improve-prom]] |
| 2026-09-21T02:52:59+08:00 | HN Show HN | 点赞=13 · 评论=3 · engagement_velocity=13 | [[20-语料/posts/hn_show/2026-09-21/23214676eb58d73b_Show-HN-Promptloop-–-create,-run,-and-improve-prom]] |

## 摘要正文

# Bella3202019/promptloop  Claude Code for prompt eval  - Stars: 23 - Forks: 2 - Watchers: 23 - Open issues: 0 - Default branch: main - Created: 2026-03-19T13:54:05Z  ## Languages  - Python  ## Top Contributors  - Bella3202019 (22 contributions)  ---  ## README  # Promptloop  An interactive CLI agent for the full prompt-eval loop: create test cases, run evals, generate reports, and approve prompt diffs without leaving your terminal.  ## The Prompt Eval Loop  Agent harnesses are getting better, but prompts still shape what they do. promptloop turns a prompt and eval intent into a repeatable loop:  It saves the methodology, test cases, reports, prompt history, and chat checkpoints under `.evals/` in the target project.  ```text .evals/   prompts/        # registered prompts + version history   test_cases/     # per-prompt test suites   eval_configs/   # methodology (metrics, models, judges)   results/        # eval runs and reports   chat.db         # SQLite checkpoint of conversation threads ```  Example metrics:  - `latency`: response time - `json_schema`: validates structured output - `fuzzy_match`: compares text similarity - `llm_judge`: scores output with a judge prompt  ## Inst…
