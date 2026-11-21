---
type: "corpus"
item_id: "1f4577d836e86412"
title: "Show HN: OpenComputer – an open source alternative to Devin"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50581403"
project_url: "https://github.com/diggerhq/opencomputer"
author: "iacguy"
published_at: "2026-11-20T20:19:56Z"
captured_at: "2026-11-21T14:45:01+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-21"
pub_day: "2026-11-20"
tags:
  - 语料
  - hn_show
  - author_iacguy
  - story_50581403
  - show_hn
  - front_page
metrics: {"points": 96, "comments": 24, "engagement_velocity": 96}
comments_count: 24
comments_total: 24
discovered_via: "hn:show_hn:3d"
---

# Show HN: OpenComputer – an open source alternative to Devin

> [!info] 一句话导读
> Hi HN!Utpal here, I'm one of the founders of OpenComputer.OpenComputer is an open source cloud coding agent for teams that can run in your own cloud account (AW…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50581403>
> 指标：点赞=96 · 评论=24 · engagement_velocity=96
> 作者：iacguy　|　发布：2026-11-20T20:19:56Z
> 项目链接：<https://github.com/diggerhq/opencomputer>
> 采集：2026-11-21T14:45:01+08:00　|　id：`1f4577d836e86412`

## 正文

Hi HN!Utpal here, I'm one of the founders of OpenComputer.OpenComputer is an open source cloud coding agent for teams that can run in your own cloud account (AWS, GCP, Azure).We run the agent harness and the sandbox on the same durable VM (architecture in the docs [1]). First commit lands in 24s; the alternatives we benchmarked took 53-72s (benchmarks below [2]).Two other choices:- One VM per team, scalable horizontally. Sessions are isolated in git worktrees.
- Session files are backed up to a repo after every turn, so any session can resume on another VM.We noticed that past ~640 session-hours a month, one always-on 4 vCPU VM is cheaper than per-session E2B sandboxes, for example. So at scale, this setup would not only be faster than current SOTA coding agents, but also more cost-efficient.Feel free to try via cloud for free [4] or self host. We would love any and all feedback, and happy to answer any questions! Full demo below [3].[1]: https://docs.opencomputer.dev/getting-started/architecture
[2]: https://opencomputer.dev/blog/cloud-agents-as-fast-as-local/
[3]: https://x.com/IgorZIJ/status/2121309785882591711
[4]: https://app.opencomputer.dev

## 评论（24/24）

> **taudas** · 2026-11-20T20:48:47.000Z　
> New product name please, your current name tells us nothing and is already taken. But I am still going to try it :)

---

> **namanyayg** · 2026-11-20T21:21:34.000Z　
> Open source is amazing! Any insights how you've made something so cheap and fast? Are the margins charged by Devin really this insane?

---

> **sleepytimetea** · 2026-11-20T21:30:38.000Z　
> Don't have Slack, will it work with Discord ?

---

> **andyjtyler** · 2026-11-20T21:42:47.000Z　
> is the whole thign open source? like can i spin it up in my own infra or just the harnesss code?

---

> **hasbot** · 2026-11-20T23:01:39.000Z　
> Probably best to explain what this is directly without expecting people to know what Devin is.

---

> **SilentM68** · 2026-11-21T00:11:28.000Z　
> I see the word self-hosted but don't see any mention of Ollama or dedicated home self-hosting scenario.What if somebody wants to just self-host on a home pc, say using Ollama to serve the models? Does OC work w/ Ollama directly, providing "its own agent capabilities" rather than relying on other agents e.g. ClaudeCode, Codex, OpenCode, etc?Will any of the above be supported in the future?

---

> **swyx** · 2026-11-21T01:13:31.000Z　
> how do you compare your approach to OpenHands (fka OpenDevin)? (https://ai.engineer/talks/iH_wV8BbS24)

---

> **iacguy** · 2026-11-20T20:51:18.000Z　
> Curious which other product you're referring to? But valid will take a look on the naming conflict.And yes please give it a shot and let us know what you think!

---

> **rl3** · 2026-11-20T21:14:24.000Z　
> >... your current name tells us nothing ...A little harsh, but at least it's leagues ahead of Devin.

---

> **igorzij** · 2026-11-20T21:33:38.000Z　
> thanks!! we'll seriously consider, fr

---

> **igorzij** · 2026-11-20T21:32:56.000Z　
> thanks!!we've invested heavily into infra
> one of the non-trivial things we did there is 2 levels of isolation instead of one
> there are VMs with fast NVMe disks and then inside VMs lighter rootless podman sandboxes - and each organisation gets a fleet of N VMs dedicated, N>=1this way the VMs serve as a "soft" concurrency limit and all sessions are still isolated, guaranteed to run on your VM, and start fast

---

> **Atotalnoob** · 2026-11-20T22:26:07.000Z　
> Devin charges a premium markup and has switched their default model to a very cheap, low quality model.At my organization, all of the skilled engineers use Claude Code and the bad ones use Devin cause it’s “easier”.It shows in the code thats written

---

> **cadamsdotcom** · 2026-11-21T05:02:30.000Z　
> Sorry but this comes off as sycophantic and thus inauthentic.If you invested in the company, or are affiliated somehow, consider disclosing..

---

> **motatoes** · 2026-11-20T21:36:31.000Z　
> hey! founder here. We have a web ui and a cli as alternatives, you can also integrate the cli with local coding agents or things like openbot. Discord can be on the roadmap! Hope you can try it and file feature request for us

---

> **igorzij** · 2026-11-20T22:02:43.000Z　
> not yet but on the roadmap!

---

> **iacguy** · 2026-11-20T21:57:52.000Z　
> Yes - the repo is Apache 2.0. For the harness specifically, you byo Claude Code/ Codex.You need one VM in your cloud plus Cloudflare Workers (the runtime of which is also open source as workerd) for Slack events.

---

> **izalutski** · 2026-11-21T00:45:53.000Z　
> this makes Devin an OpenComputer alternative!right?
> right..?

---

> **nitroedge** · 2026-11-21T01:56:06.000Z　
> Have you heard of Windsurf?

---

> **izalutski** · 2026-11-21T00:45:10.000Z　
> we're planning to give at-home setups more attention at some point! for now meaning self hosting as in "in my team's cloud acct"

---

> **iacguy** · 2026-11-21T01:39:15.000Z　
> Big fans of OpenHands.The main difference from our pov is that OpenHands is an agent with its own harness. We’re unopinionated on the harness and more focused on the infrastructure it runs in. In fact we started as one of the first “persistent” sandbox providers [1].
> OpenComputer runs the user’s Claude Code or Codex (you pick per thread), and you can bring your own ChatGPT/Codex subscription.Our focus is predominantly on building high perf specialised infra for cloud coding agents. eg: each Slack thread gets its own rootless Podman container, with state written to local disk and then persisted to a git backed store. That’s why it feels like Claude Code on your laptop: in our benchmark it opened PRs 3.3x faster than Devin, with first push in 24s vs a 62s average across the 4 most popular cloud agents [2]. It's also cheaper at at scale, we've found, than an ephemeral sandbox per session [3].[1] https://x.com/utpalnadiger/status/2047436177016537251
> [2] https://opencomputer.dev/blog/cloud-agents-as-fast-as-local/
> [3] https://opencomputer.dev/blog/opencomputer-open-source-devin...

---

> **nasso_dev** · 2026-11-20T23:13:41.000Z　
> personally i think of OpenComputers, a minecraft mod

---

> **iacguy** · 2026-11-21T04:44:29.000Z　
> fwiw - Devin is a great name and we have a lot of respect for what they’ve built!

---

> **jkelleyrtp** · 2026-11-21T01:58:06.000Z　
> > Devin charges a premium markup and has switched their default model to a very cheap, low quality model.I work at Cognition. This is not true. The picker currently has:- Normal: Balances cost and intelligence with models like Opus 5.5 and GPT-6.2 Sol- Ultra: Highest intelligence available with Fable 5.2 and GPT-6.2 Astra- Lite: Fast lightweight models- Fusion: Multi-model harness that pairs frontier models like Opus 5.5, Fable 5.2, and GPT-6.2 Astra with a cost efficient sidekick for up to 30% cost savingsAnd then you can select any of the "preview" models like SWE-2, GPT 6.2, Gemini 4 Neon, Fable 5.2, etc.The built-in modes are basically just "best model at xyz on cost curve" and then we have individual models people can select.

---

> **dabit3** · 2026-11-21T02:11:23.000Z　
> Hi, I work with the Devin team at Cognition:"Premium markup." If you go past the usage included in a paid plan, extra usage is billed at API pricing. In September Devin also got 30–40% cheaper in Fusion and Normal mode and 15–20% cheaper in Ultra while quality held or improved at every mode."Cheap, low-quality default model." Devin isn't tied to one model. Our normal router uses Opus 5.5 at the moment (or GPT-6.2 Sol high on GPT plan), and Ultra uses Fable 5.2 (or GPT-6.2 Astra high on GPT plan), only when someone chooses the light mode specifically are they routed to SWE-2 which is actually a great model trained specifically for software engineering that benches really well and developers really love (and SWE-2 inference / usage is currently free)."Only the bad engineers use it." Our users include engineers from Nvidia, Exa, Modal, OpenRouter, Mercor, Ramp, and hundreds of other companies with a high bar for engineering talent, and the best ones seem to really love and appreciate the quality and shipping velocity they get with Devin.I encourage anyone reading this to consider asking someone they know who's used Devin within the past few months for their opinion.

## 关联链接

- https://app.opencomputer.dev
- https://docs.opencomputer.dev/getting-started/architecture
- https://opencomputer.dev/blog/cloud-agents-as-fast-as-local/
- https://x.com/IgorZIJ/status/2121309785882591711

## 导航

- 项目页：[[10-项目/github.com_00dcab6d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
