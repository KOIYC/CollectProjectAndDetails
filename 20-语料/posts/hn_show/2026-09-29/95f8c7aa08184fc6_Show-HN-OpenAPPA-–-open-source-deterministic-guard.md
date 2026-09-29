---
type: "corpus"
item_id: "95f8c7aa08184fc6"
title: "Show HN: OpenAPPA – open-source deterministic guardrails that don't break agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49877515"
project_url: "https://openappa.com/"
author: "motakuk"
published_at: "2026-09-28T13:20:44Z"
captured_at: "2026-09-29T09:42:56+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-29"
pub_day: "2026-09-28"
tags:
  - 语料
  - hn_show
  - author_motakuk
  - story_49877515
  - show_hn
metrics: {"points": 23, "comments": 12, "engagement_velocity": 23}
comments_count: 12
comments_total: 12
discovered_via: "hn:show_hn:3d"
---

# Show HN: OpenAPPA – open-source deterministic guardrails that don't break agents

> [!info] 一句话导读
> Hi Hacker News! Matvey, one of the authors, is here.While building enterprise agents, we ran into a problem: the more tools you connect to the AI, the higher th…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49877515>
> 指标：点赞=23 · 评论=12 · engagement_velocity=23
> 作者：motakuk　|　发布：2026-09-28T13:20:44Z
> 项目链接：<https://openappa.com/>
> 采集：2026-09-29T09:42:56+08:00　|　id：`95f8c7aa08184fc6`

## 正文

Hi Hacker News! Matvey, one of the authors, is here.While building enterprise agents, we ran into a problem: the more tools you connect to the AI, the higher the chance it will run out of control and leak sensitive data.Guardrails, in theory, should prevent this, but the situation is worrying:
- Non-deterministic guardrails (LLM as a judge, auto modes, etc.) are vulnerable to prompt injections, or they lack knowledge of the data, making them inefficient (~10% data leaks on our benchmarks).
 - Existing deterministic guardrails (Cedar, OPA, FIDES, Dogwood) require massive case-specific IF-ELSE-like policies and break agents (~59% utility loss on our benchmarks).We did something differently.We’ve taken the best of existing deterministic guardrails and built a policy language that is data-specific, not use-case specific. It lets you scale agents without updating a policy.On top of that, we’ve added multiple tricks (like a remedy plan or a DualLLM pattern) to help agents operate within those restrictions, raising utility from ~40% to ~90% and making it the first deterministic guardrail that doesn't break agents.Finally, we’ve designed it to be pluggable into any agent loop with pre- and post-tool-call hooks.We invite you to check out our benchmarks: https://www.openappa.com/evaluationPlay with it in Claude Code: https://www.openappa.com/claude-codeTry plugging it into your agent: https://www.openappa.com/add-to-agentOr check the academic paper: https://arxiv.org/abs/2607.24625We'd love to hear any feedback!

## 评论（12/12）

> **dvorkanton** · 2026-09-28T13:25:21.000Z　
> Finally some determinism in our high-temperature sampling world!

---

> **joeyorlando** · 2026-09-28T13:31:20.000Z　
> aussi, si vous êtes à Montréal et vous aimerez apprendrez plus sur OpenAPPA, viens à l'evenement CNCF demain soir, le 29 - je ferai un p'tit discours sur l'integration kagent d'OpenAPPA.https://www.meetup.com/kubernetes-montreal/events/316689391/

---

> **arseny_info** · 2026-09-28T13:34:51.000Z　
> I still remember the times when ai/ml security was about perturbing pixel gradients to misclassify a panda

---

> **keshakon** · 2026-09-28T13:35:16.000Z　
> Hi! One of the OpenAPPA authors here. Ask me anything!My favorite part of APPA is “batteries”: you can run arbitrary programs as part of an authorization decision. For example, a battery could call the GitHub API to check whether a repository is public or private, then use that result to decide whether its contents can be posted to Slack.

---

> **ildari** · 2026-09-28T13:42:19.000Z　
> a few days ago I started an agent on gpt-5.6-terra to work on a project, and one of the website pages had a sentence to create GH issues. Agent read it and that was enough to derail and go creating issues with my context

---

> **piercypixel** · 2026-09-28T13:47:26.000Z　
> Guardrails with builtin remediation instead of simply blocking my agent is a mind blowing long awaited experience! Sooo good. Can't recommend more!

---

> **immafridge** · 2026-09-28T13:50:35.000Z　
> Quick disclaimer, I work at Archestra.I’ve had the chance to play with OpenAppa for a bit and if there’s one thing that I love with this project: it’s simple to get started with and easy to tweak. imo agentic security shouldn’t have to be painful to setup.Give it a shot and hopefully ya’ll will find this project useful. It's also open source :)

---

> **zborro** · 2026-09-28T14:02:44.000Z　
> i suspect we’ll see more of this: flexible agents but deterministic boundaries. Congrats on launch!

---

> **vladimir_gor** · 2026-09-28T14:25:33.000Z　
> Really interesting direction. What resonated with me is that you're treating agent security as an information-flow problem rather than a prompt-classification problem. It was not so obvious to me.A key question I agree isn't just "is this tool call allowed?", but "given everything the agent has read so far, is this information now allowed to flow to this destination?" That feels like a much more fundamental abstraction.The part I'm particularly curious about is how this will work with policy authoring at scale. What would be the main adoption challenge?

---

> **apetrovicheva** · 2026-09-28T14:33:43.000Z　
> the paper is good! thorough. I like it.

---

> **moneytool** · 2026-09-29T01:30:24.000Z　
> HI I have created something that actually to solve this exact problem please go through it this stays in your environment independent of AI and its a python module that blocks AI from using unauthorized commands
> https://github.com/moneytool/aegis-devops

---

> **arseny_info** · 2026-09-28T14:36:36.000Z　
> great question, very practical.we have a layered answer here:
> 1) we ship over a dozen "batteries" now (and plan to grow the number) - they contain base annotations for popular services and helper scripts where relevant;
> 2) we also ship a skill helping you write your own policies for custom services or adopt the default ones based on your specific needs. The criteria "what's acceptable for each particular scenario" varies, there is no "one size fits all" solution;
> 3) finally, there is a designed placeholder to cover the rest via wildcard AI annotator if needed. The difference between that and regular "auto mode" in coding agents is that APPA's annotator emits local label (e.g. "does this call require a trusted env?"), not wide allow/block, while decision making stays within label algebra.

## 关联链接

- https://arxiv.org/abs/2607.24625We
- https://www.openappa.com/add-to-agentOr
- https://www.openappa.com/claude-codeTry
- https://www.openappa.com/evaluationPlay

## 导航

- 项目页：[[10-项目/openappa.com_f22d2393]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
