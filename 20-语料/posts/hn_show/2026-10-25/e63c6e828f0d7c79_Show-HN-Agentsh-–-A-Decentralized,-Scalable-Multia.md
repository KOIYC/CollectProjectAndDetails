---
type: "corpus"
item_id: "e63c6e828f0d7c79"
title: "Show HN: Agentsh – A Decentralized, Scalable Multiagent Harness"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50223759"
project_url: "https://github.com/microsoft/Agensh"
author: "brunoborges"
published_at: "2026-10-24T18:19:35Z"
captured_at: "2026-10-25T23:24:35+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-25"
pub_day: "2026-10-24"
tags:
  - 语料
  - hn_show
  - author_brunoborges
  - story_50223759
  - show_hn
metrics: {"points": 7, "comments": 1, "engagement_velocity": 7}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Agentsh – A Decentralized, Scalable Multiagent Harness

> [!info] 一句话导读
> A Decentralized, Scalable Multiagent Harness

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50223759>
> 指标：点赞=7 · 评论=1 · engagement_velocity=7
> 作者：brunoborges　|　发布：2026-10-24T18:19:35Z
> 项目链接：<https://github.com/microsoft/Agensh>
> 采集：2026-10-25T23:24:35+08:00　|　id：`e63c6e828f0d7c79`

## 正文

# microsoft/Agensh

A Decentralized, Scalable Multiagent Harness

- Stars: 22
- Forks: 2
- Watchers: 22
- Open issues: 0
- License: MIT License
- Homepage: https://aka.ms/Agensh
- Default branch: main
- Created: 2026-08-27T02:56:13Z

## Languages

- Dockerfile
- Go Template
- JavaScript
- Makefile
- Python
- Shell
- TypeScript

## Top Contributors

- zhan8855 (1 contributions)

---

## README

 Agensh: A Decentralized, Scalable Multiagent Harness

### News

🚀 **2026-10-24:** We open-sourced **Agensh**, including the harness, experiment launch
scripts, and reproduction guide.

📢 **2026-09-22:** We published the **Agensh** preprint on arXiv.

## Overview

**Agensh is a self-organized multi-agent harness that scales to 1,024 agents.**
Agents discover and claim sub-tasks, share findings, verify results and
merge progress asynchronously, without a central orchestrator. A shared
workspace, message interface and shared context connect each agent's local
progress to the team.

We evaluated Agensh on the five hardest ProgramBench tasks
using GPT-5.6-sol with high reasoning effort, a six-hour budget and no Internet access.
Agents rebuild reference programs from behavioral observations and bundled
documentation. Across the 5 evaluated tasks, the mean final test-pass rate rises
from **19.31% with 1 agent** to **28.78% with 128 agents**, an improvement of
approximately **49% relative**. Larger teams also reach comparable pass rates
sooner. On **Pandoc**, the final test-pass rate rises from **33.89% with 1 agent**
to **50.94% with 128 agents** and **55.06% with 1,024 agents** under the same
six-hour budget. We find that self-organized peer coordination, integration
workflows and specialized roles gradually emerge as the team grows.

With the latest GPT-6.1-sol at high reasoning effort, the six-hour Pandoc test-pass
rate rises from **56.19% with 1 agent** to **79.59% with 32 agents**, a relative
improvement of **41.64%**.

Pandoc scaling results for GPT-5.6-sol and GPT-6.1-sol at high reasoning effort, with emergent coordination workflows and specialized roles

## Watch 1,024 agents work together

Animated replay of 1,024 agents cooperating through Gitea, Mattermost and shared context

## How it works

Agensh cooperation loop: gather context, claim a sub-task, take action, verify results and merge progress asynchronously through shared workspace, messaging and context

**Agensh defines the multi-agent cooperation loop.**
Workers concurrently gather context, claim sub-tasks, take action, verify results
and merge progress in a self-organized manner, repeating until the user’s goal
is achieved. All workers proceed asynchronously and share progress through the
infrastructure.
Gitea provides the shared workspace,
Mattermost provides the messaging interface, and the
shared context mechanism is adapted from DeLM.
In our experiments, we integrate Agensh on top of the per-agent agentic loop
of Copilot harness.

## Reproducing the experiments

This release includes a single-node team setup using Docker Compose and a
standalone single-agent baseline, both using native Copilot ACP sessions.

- Reproduction guide: prerequisites, configuration, image builds,
 launch commands, evaluation, recovery and release differences.
- Repository layout: component and folder guides.
- Team launcher and
 single-agent launcher: experiment entrypoints.

## Citation

```bibtex
@article{zhan2026agensh,
  title   = {Agensh: Scaling Organizational Intelligence to 1,024 Agents},
  author  = {Zhan, Zhihao and Song, Ting and Dong, Li and Huang, Shaohan and Lian, Jianxun and Xia, Yan and Wei, Furu},
  journal = {arXiv preprint arXiv:2609.26781},
  year    = {2026},
  url     = {https://arxiv.org/abs/2609.26781}
}
```

## License and contributing

Code is licensed under the MIT License. See the
contribution guidelines,
security policy,
support information, and
trademark guidance.

## 评论（1/1）

> **faradaycage314** · 2026-10-25T02:21:29.000Z　
> Cool! your github shows a demo of 1024 agents working together...I'm actually super curious how this works in practice:When you have that many agents running, how often they are committing to the repo? do they run in different worktrees, or all in the same worktree and just make small commits with the files they touch?IF they are running in different worktrees how often do they use the coordination tools across worktres, and is coordination even needed in that case since you have worktree isolation? If they are running in the same worktree, do they coordinate well enough that no agent tries to do things like run a full test suite in the shared worktree? or does that happen and they just deal with it?

## 关联链接

- https://aka.ms/Agensh
- https://arxiv.org/abs/2609.26781}

## 导航

- 项目页：[[10-项目/github.com_0ebb7a0a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
