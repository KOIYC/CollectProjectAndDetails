---
type: "corpus"
item_id: "ff843daec01b4b24"
title: "Show HN: Komi-learn – continuous memory and self-improvement for coding agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48343216"
project_url: "https://github.com/kurikomi-labs/komi-learn"
author: "rainxchzed"
published_at: "2026-05-31T05:11:40Z"
captured_at: "2026-09-21T02:52:48+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-31"
tags:
  - 语料
  - hn_show
  - author_rainxchzed
  - story_48343216
  - show_hn
metrics: {"points": 27, "comments": 3, "engagement_velocity": 27}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:144d"
---

# Show HN: Komi-learn – continuous memory and self-improvement for coding agents

> [!info] 一句话导读
> kurikomi-labs/komi-learn

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48343216>
> 指标：点赞=27 · 评论=3 · engagement_velocity=27
> 作者：rainxchzed　|　发布：2026-05-31T05:11:40Z
> 项目链接：<https://github.com/kurikomi-labs/komi-learn>
> 采集：2026-09-21T02:52:48+08:00　|　id：`ff843daec01b4b24`

## 正文

# kurikomi-labs/komi-learn

Continuous memory + self-improvement for AI agents. Learns how you work, recalls it automatically, no commands. Claude Code & Codex.

- Stars: 76
- Forks: 3
- Watchers: 76
- Open issues: 1
- License: MIT License
- Default branch: main
- Created: 2026-05-29T09:05:28Z

## Languages

- Python

## Topics

- ai
- ai-agents
- ai-tools
- claude-code
- codex
- continuous-learning
- llm

## Top Contributors

- rainxchzed (54 contributions)

---

## README

# komi-learn

Continuous memory and self-improvement for coding agents. It learns how you work and recalls it automatically, with no commands. Works with Claude Code and Codex.

PyPI
Python
License: MIT
CI

It watches a session, distills durable lessons in the background (your style, your stack, fixes that worked), and loads the relevant ones at the start of the next session. No slash commands, nothing to save by hand.

The idea is from Hermes Agent; this is my own take, generalized across hosts with an optional shared layer (the community pool, below).

It's early. The core loop is built and CI-tested, but it hasn't been battle-tested across a lot of real sessions yet. Feedback and bug reports are welcome.

## Install

```bash
pip install komi-learn
komi-learn install            # or: komi-learn install --host codex
```

`install` runs a short interactive setup, then recall and background learning start in your next session. If you already use Claude Code you're already logged in. For scripts, `komi-learn install --yes` takes the defaults.

From source:

```bash
git clone https://github.com/kurikomi-labs/komi-learn
cd komi-learn
pip install -e .
```

## Commands

```bash
komi-learn doctor      # check the install and what to fix
komi-learn update      # upgrade komi-learn + the agent's hooks (--check to only look)
komi-learn status      # config + how much it has learned
komi-learn config      # change any setting (menu, or `config set <key> <val>`)
komi-learn sync        # pull the latest community learnings
komi-learn queue       # review/approve/reject what you'd contribute to the pool
komi-learn forget <x>  # erase learnings matching <x> (archive, or --hard to delete)
komi-learn reclassify  # re-scan memory; move newly-confidential learnings to private (.local)
komi-learn uninstall   # remove the hooks (keeps your data; --purge to wipe)
```

You can change anything after install, e.g. `komi-learn config set recall.semantic false` or leave the pool with `komi-learn config set pool.repo_url ""`.

## How it works

1. Recall: at session start, learnings relevant to the current context are loaded.
2. Distill: after the session, a background pass reads the transcript and extracts durable lessons (corrections, techniques, fixes).
3. Curate: over time it merges overlapping lessons and archives stale ones.
4. Share (optional): general lessons can be contributed to the community pool, but only ones you approve.

It tries not to learn the wrong things. Secrets, machine-specific paths, one-off failures, and "tool X is broken" complaints are filtered out by a deterministic check before the LLM ever sees them.

## Community pool (optional)

A public pool of general agent lessons, stored as a GitHub repo of signed Markdown files (no server). If you opt in, you get lessons other people's agents figured out, and you can contribute your own.

Contributions are scrubbed of anything identifying and never leave your machine without your approval (each one opens a PR you reviewed). Learnings are content-addressed (BLAKE3) and signed (Ed25519); one signed by more distinct GitHub accounts ranks higher when pulled. That account count is Sybil-resistant but not Sybil-proof, so it's an advisory signal, not a hard trust gate. Recalled community items are labelled and treated as untrusted input. Details: pool-repo-template/CONTRIBUTING.md.

## Try it offline

No setup or API key needed:

```bash
python examples/demo_loop.py
```

It runs two sessions: you correct the agent in the first, and the second shows it recalling that with nothing typed.

## Requirements

- Python 3.10+
- Claude Code or Codex (the agent it plugs into)
- A working model for the distill step: your existing Claude Code login, or `komi-learn login`, or an API key via `--api-key`.

`komi-learn install` verifies these with a real model call and stops with fix steps if something's missing. At runtime, if a hook can't reach the model it skips that learning pass rather than interrupting your session.

The engine has no required dependencies. Optional extras add real signing (`pip install komi-learn[crypto]`) and local semantic recall (`[smart]`); without them it falls back to a stdlib hash and keyword search.

To run your own pool, see pool-repo-template/.

MIT. Issues and PRs welcome.

# yeet-src/usbsnoop

## 评论（3/3）

> **loehnsberg** · 2026-05-31T06:48:55.000Z　
> It sounds like it solves the problem that everybody who vibe codes over multiple projects runs into, but it does not provide evidence that it actually works and that it is better than structured collection of md files. I think what is lacking in this field are benchmarks like LoCoMo for long sessions.

---

> **rainxchzed** · 2026-05-31T08:46:34.000Z　
> thanks for the feedback, will definitely work on it! as mentioned a little early stage of the project, so

---

> **dr_kiszonka** · 2026-05-31T20:54:54.000Z　
> > than a structured collection of md files.I think it depends on what a memory system includes. Those that automatically inject relevant information into context are in my experience better than just md docs because agents often ignore, forget to read, or don't read md files in full.

## 导航

- 项目页：[[10-项目/github.com_c9c6b37b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
