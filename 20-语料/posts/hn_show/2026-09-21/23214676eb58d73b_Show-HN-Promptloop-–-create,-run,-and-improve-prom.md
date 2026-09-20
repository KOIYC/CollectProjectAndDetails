---
type: "corpus"
item_id: "23214676eb58d73b"
title: "Show HN: Promptloop – create, run, and improve prompt evals from the terminal"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48325073"
project_url: "https://github.com/Bella3202019/promptloop"
author: "velapod"
published_at: "2026-05-29T16:06:46Z"
captured_at: "2026-09-21T02:52:59+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-29"
tags:
  - 语料
  - hn_show
  - author_velapod
  - story_48325073
  - show_hn
metrics: {"points": 13, "comments": 3, "engagement_velocity": 13}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:144d"
---

# Show HN: Promptloop – create, run, and improve prompt evals from the terminal

> [!info] 一句话导读
> Bella3202019/promptloop

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48325073>
> 指标：点赞=13 · 评论=3 · engagement_velocity=13
> 作者：velapod　|　发布：2026-05-29T16:06:46Z
> 项目链接：<https://github.com/Bella3202019/promptloop>
> 采集：2026-09-21T02:52:59+08:00　|　id：`23214676eb58d73b`

## 正文

# Bella3202019/promptloop

Claude Code for prompt eval

- Stars: 23
- Forks: 2
- Watchers: 23
- Open issues: 0
- Default branch: main
- Created: 2026-03-19T13:54:05Z

## Languages

- Python

## Top Contributors

- Bella3202019 (22 contributions)

---

## README

# Promptloop

An interactive CLI agent for the full prompt-eval loop: create test cases, run evals, generate reports, and approve prompt diffs without leaving your terminal.

## The Prompt Eval Loop

Agent harnesses are getting better, but prompts still shape what they do. promptloop turns a prompt and eval intent into a repeatable loop:

It saves the methodology, test cases, reports, prompt history, and chat checkpoints under `.evals/` in the target project.

```text
.evals/
  prompts/        # registered prompts + version history
  test_cases/     # per-prompt test suites
  eval_configs/   # methodology (metrics, models, judges)
  results/        # eval runs and reports
  chat.db         # SQLite checkpoint of conversation threads
```

Example metrics:

- `latency`: response time
- `json_schema`: validates structured output
- `fuzzy_match`: compares text similarity
- `llm_judge`: scores output with a judge prompt

## Install and Run

```bash
git clone <this repo>
cd promptloop
uv sync
uv run promptloop --project-dir /path/to/your/project
```

You'll get an interactive chat. Try things like:

- *"Evaluate the prompt at `src/prompts/summarize.txt`"*
- *"Add three more test cases for edge cases"*
- *"Re-run with `openai:gpt-4o-mini` and compare to the last run"*
- *"Propose a fix for the failing JSON schema cases"*

## Commands

| Command | Description |
| --- | --- |
| `/help` | Show help |
| `/clear` | Start a new conversation thread |
| `/threads` | List saved threads |
| `/thread ` | Switch to a thread in-session |
| `/quit` | Exit |

Resume past sessions with `promptloop --thread `. Press **Esc** to interrupt a streaming response.

## Quick Demo

**Stage 1: Register a prompt** — point promptloop at a prompt file and it registers it with version tracking:

register prompt

**Stage 2: Add test cases** — the agent proposes test cases based on your prompt and intent; you pick what to keep:

add test cases

**Stage 3: Run the eval** — see pass/fail results per test case with metrics and latency:

run eval

**Stage 4: Review and update the prompt** — when cases fail, ask for a fix. promptloop reads the report, shows a colored diff in the terminal, and waits for a keypress (`y`/`n`) before writing anything:

propose and update prompt

**Stage 5: Next iteration** — re-run the eval on the new prompt version and keep iterating:

next iteration

Every run persists the full loop — versioned prompts, test cases, eval configs, and reports — so nothing is lost between sessions:

promptloop show result

## How It Works

The agent has a small set of typed tools on top of deepagents' filesystem access:

- `register_prompt`, `edit_prompt`, `show_prompt_history`
- `add_test_case`, `infer_json_schema`, `save_eval_config`
- `run_eval`, `list_eval_runs`
- `generate_report`, `read_report`, `compare_runs`

For more detail on the agent runtime behind this project, see The Harness Behind Deep Agent.

Early / experimental. Feedback and issues welcome.

## What's Next

This is a starting point. A few directions I'm thinking about:

**1. Interface** — the CLI works, but the prompt loop deserves a less friction interface. Extending toward a richer chat UI or editor integration so the loop feels more natural to run.

**2. Less human in the loop** — the current flow still relies on you to drive each stage.

> *"It would be extremely cool to be able to write one or two lines of prompt in my harness, and have a light model iterate with me a few times writing/proposing requirements, guidelines and explanations, refining the prompt until it's ready to be sent to the actual LLM."* ---- HN commenters:

Ideally it would be a lightweight thing(could be tool, skill, cli, chat interface or a snippet) that co-authors the prompt with you, proposes requirements, flags gaps, and tightens the spec before it ever hits your production model.

Built on LangChain deepagents.

# fynyky/elemental

## 评论（3/3）

> **tacone** · 2026-05-29T20:54:42.000Z　
> I don't really understand why the comment has been downvoted.We actually need more of this, perhaps not in this exact shape, but similar.It would be extremely cool to be able to write one or two lines of prompt in my harness, and have a light model iterate with me a few times writing/proposing requirements, guidelines and explanations, refining the prompt until it's ready to be sent to the actual LLM.Lack of specifications in the prompt is (imho?) one of the main drivers that lead the LLMs astray, and it often happens because it's not realistic to always type or even thing every angle before submitting each prompt.Think of it as the missing link between a single-shot prompt and a skill.It should be ideally integrated in the chat, for quick access.This project is probably different in aim, but I still find it interesting.

---

> **CharlesW** · 2026-05-30T03:33:25.000Z　
> > It would be extremely cool to be able to write one or two lines of prompt in my harness, and have a light model iterate with me a few times writing/proposing requirements, guidelines and explanations, refining the prompt until it's ready to be sent to the actual LLM.It is cool and (IMO) necessary, and most AI-using coders I know do this using skill suites like Superpowers (see: /superpowers:brainstorming). https://github.com/obra/superpowers

---

> **velapod** · 2026-05-31T22:15:04.000Z　
> yea i can imagine it could be possibly moved to skills

## 导航

- 项目页：[[10-项目/github.com_40108bcf]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
