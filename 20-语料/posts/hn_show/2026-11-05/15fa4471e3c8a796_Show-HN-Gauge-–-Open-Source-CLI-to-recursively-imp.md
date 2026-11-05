---
type: "corpus"
item_id: "15fa4471e3c8a796"
title: "Show HN: Gauge – Open-Source CLI to recursively improve your docs"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50371090"
project_url: "https://github.com/gauge-sh/gauge-cli"
author: "0x63_Problems"
published_at: "2026-11-04T20:31:30Z"
captured_at: "2026-11-05T11:35:28+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-05"
pub_day: "2026-11-04"
tags:
  - 语料
  - hn_show
  - author_0x63_Problems
  - story_50371090
  - show_hn
  - front_page
metrics: {"points": 22, "comments": 4, "engagement_velocity": 22}
comments_count: 4
comments_total: 4
discovered_via: "hn:show_hn:3d"
---

# Show HN: Gauge – Open-Source CLI to recursively improve your docs

> [!info] 一句话导读
> Hi HN, I’m Evan from Gauge. We’re open-sourcing our CLI to recursively improve your docs for coding agents. The CLI includes a local execution backend, so you d…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50371090>
> 指标：点赞=22 · 评论=4 · engagement_velocity=22
> 作者：0x63_Problems　|　发布：2026-11-04T20:31:30Z
> 项目链接：<https://github.com/gauge-sh/gauge-cli>
> 采集：2026-11-05T11:35:28+08:00　|　id：`15fa4471e3c8a796`

## 正文

Hi HN, I’m Evan from Gauge. We’re open-sourcing our CLI to recursively improve your docs for coding agents. The CLI includes a local execution backend, so you don't need an account to try it. Explainer video here: https://youtu.be/zhLUlIKB1MgThe CLI supports a hillclimbing loop:- set up tasks for coding agents that would need your docs, like 'set up Gauge CI checks'- run the tasks- analyze session transcripts for friction or failures- create variants of your docs to resolve the issues- re-run the tasks with the doc variants injected (transparently, at the same hostname)- repeat until you have a variant that resolves the issuesThe same loop supports hillclimbing your Skills, CLI, and other agent-facing surfaces.We started out 2 years ago building open-source developer tools (like Tach https://github.com/tach-org/tach), then pivoted to AI Search optimization, and are now focused on the intersection of the two spaces. We were already working with awesome devtool companies, and they were the first ones to ask us how to optimize for Claude Code and Codex. We realized this would be something that eventually every company needs to do. Our CLI provides primitives for docs/devrel/eng teams to measure, analyze, and improve how coding agents use their product.The design boils down to two components: VMs and a network gateway.The VMs are straightforward, we want the agents to be highly privileged within their environment so that they are representative of developers' coding agents. Each VM generally comes with the agent harness itself, language toolchains, and a git repository.The network gateway is where we terminate TLS and swap in variants of your docs transparently. The gateway also handles credential replacement, so agents see placeholders and can't exfiltrate keys.The CLI comes with a 'local' execution backend (inference is still remote). For VMs, it uses Docker containers, and the network gateway is mitmproxy running in a sidecar container for each session.We've used the hillclimbing loop internally to find and fix coding agent issues like mistaken pricing, inaccurate product limitations, and repeated workarounds. We saw coding agents report that Gauge only supports Claude Code and Codex, traced it back to the web pages they fetched, and fixed the behavior (we support Pi, OpenCode, and Antigravity as well). For Clerk, we helped shift coding agents from their legacy 'keyless' mode to their new 'clerk init' command. They were able to validate a pre-release change to their SDK's error messages using Gauge, then saw a 3x increase in coding agents using 'clerk init' post-deploy.Due to the 'static' nature of AI models, we've realized that closed-loop optimization techniques are now possible for essentially all software products. The same agent can be simulated over and over, meaning that a high-fidelity testing environment is all you need. Achieving the best results boils down to high-quality analysis (finding generalizable friction and objections) and paired experiments (vary only the content, measure the downstream change in behavior).The repo is here: https://github.com/gauge-sh/gauge-cli and you can start using the CLI with: npm i -g @withgauge/cliWe also have documentation and a quickstart here: https://docs.withgauge.com/agents/guides/cliIf you point a coding agent at those pages, it should guide you through the initial setup - let us know if it doesn't! The intention is for your agent to run some sensible evaluations and find at least one point of friction you can fix.We'd love to know from HN: Has anyone tried to DIY this locally, or built something in-house at their company? Is this an improvement? If not, what would need to change?

## 评论（4/4）

> **esafak** · 2026-11-04T23:24:44.000Z　
> Sorry to be pedantic, but it's iteratively. Your README even calls it Iteration.Thanks for sharing.

---

> **jpease** · 2026-11-05T00:06:38.000Z　
> But what if you use recursion for iteration?

---

> **0x63_Problems** · 2026-11-05T00:10:48.000Z　
> Fair enough, maybe when we use it internally it would qualify?

---

> **choxi** · 2026-11-05T03:18:00.000Z　
> They won’t stop until the entire information capacity of the universe is consumed by autogenerated Swagger docs

## 关联链接

- https://docs.withgauge.com/agents/guides/cliIf
- https://github.com/tach-org/tach
- https://youtu.be/zhLUlIKB1MgThe

## 导航

- 项目页：[[10-项目/github.com_f106f87b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
