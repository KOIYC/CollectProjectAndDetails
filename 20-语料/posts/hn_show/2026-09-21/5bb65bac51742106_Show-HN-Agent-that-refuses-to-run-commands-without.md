---
type: "corpus"
item_id: "5bb65bac51742106"
title: "Show HN: Agent that refuses to run commands without human approval"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47957127"
project_url: "https://github.com/few-sh/fewshell"
author: "hexer303"
published_at: "2026-04-30T01:49:44Z"
captured_at: "2026-09-21T01:41:21+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_hexer303
  - story_47957127
  - show_hn
metrics: {"points": 12, "comments": 5, "engagement_velocity": 12}
comments_count: 5
comments_total: 5
discovered_via: "hn:show_hn:174d"
---

# Show HN: Agent that refuses to run commands without human approval

> [!info] 一句话导读
> In light of recent news about an agent deleting a production database, I thought now would be a good time to share this.As the use of AI tools in production is …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47957127>
> 指标：点赞=12 · 评论=5 · engagement_velocity=12
> 作者：hexer303　|　发布：2026-04-30T01:49:44Z
> 项目链接：<https://github.com/few-sh/fewshell>
> 采集：2026-09-21T01:41:21+08:00　|　id：`5bb65bac51742106`

## 正文

In light of recent news about an agent deleting a production database, I thought now would be a good time to share this.As the use of AI tools in production is becoming more common, sadly so will the high profile incidents like the one mentioned.Fewshell is a terminal agent specifically designed to avoid this.There is no setting to enable command auto-approval. This is by-design, so that the user never has to second-guess or worry about accidentally having it enabled.Originally my intention was to build an AI mobile terminal to make typing shell commands easy. But with so many mobile-enabled 'claw' agents being available, I decided to make Fewshell the opposite of an autonomous agent.Please star if you like, let me know what you think. Happy to answer questions.About me: I'm an ex Amazon Sr. SDE for Alexa AI, and currently am working in AI safety research for agentic RLVR. I use this tool to run and check on my lab experiments.

## 评论（5/5）

> **hasperdi** · 2026-04-30T08:15:01.000Z　
> Numerous prompting will cause prompt fatigue, similar to pressing yes on a dialog boxes.LLM, like fire is a powerful tool. Some people play with fire and achieved great things, some play with fire and got burned. A number of them achieved great things and got burned. We need to understand that and learn from our mistakes.

---

> **embedding-shape** · 2026-04-30T11:11:12.000Z　
> Maybe it's just me, but if I had to approve each command of the agent, that'd remove 90% of the benefits of using an agent in the first place. Almost the whole point is that I can fire off a prompt, it can do whatever and then I come back later.Instead, wrap the agent in a way so it cannot destroy stuff in the first place. And if you still want it to "be able to destroy databases in production", do so by copy-pasting stuff out of the isolated environment. I've run codex as root, as "dangerously as possible" with zero approvals, since the launch of the TUI, and never hit a snag, because the agent literally don't have access to snag things up.Agents WILL make mistakes, it's up to you to set things up in a way that you don't get utterly fucked when that eventually happens. Avoiding adding 10s of MCPs tools, avoiding authenticating with all platforms, services and databases and not giving it access to all directories on your computer solves 99% of the issues people are having, and there are numerous of simple ways of doing this.

---

> **natloz** · 2026-05-01T14:23:45.000Z　
> I feel this is not the trajectory we want to go with automation. Perhaps better checks and balances within the automation, or "thresholds" that trip breakers would be a good approach?

---

> **moritzwarhier** · 2026-05-02T17:43:46.000Z　
> I refuse to read this, on behalf of my agent.

---

> **jguarnelli** · 2026-05-06T12:39:17.000Z　
> it's a fair point sandboxing is necessary. But not sufficient for agents that
> legitimately need write access. A payment agent needs Stripe. A maintenance agent
> needs DB writes. You can't sandbox those away. The missing layer is between has access and executes

## 导航

- 项目页：[[10-项目/github.com_9a93112f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
