---
type: "corpus"
item_id: "60b9b97bd3947164"
title: "Show HN: Jog – GitHub runners for 80% less"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50263941"
project_url: "https://usejog.com/"
author: "matthewgapp"
published_at: "2026-10-27T18:51:00Z"
captured_at: "2026-10-28T09:39:16+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-28"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_matthewgapp
  - story_50263941
  - show_hn
metrics: {"points": 6, "comments": 2, "engagement_velocity": 6}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Jog – GitHub runners for 80% less

> [!info] 一句话导读
> Pricing Questions Sign in with GitHub Dashboard

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50263941>
> 指标：点赞=6 · 评论=2 · engagement_velocity=6
> 作者：matthewgapp　|　发布：2026-10-27T18:51:00Z
> 项目链接：<https://usejog.com/>
> 采集：2026-10-28T09:39:16+08:00　|　id：`60b9b97bd3947164`

## 正文

Skip to content
Pricing Questions Sign in with GitHub Dashboard
Pricing Questions Ask us on Discord (new tab)
 Theme
Close
GitHub runners for agent-scale development.
 Change one line and pay 80% less.
 Get started on GitHub Or with your agent Paste it into your agent. Get started with your agent: Claude Code, Codex, Pi or OpenCode
.github/workflows/ ci.yml jobs : build : − Removed: runs-on : ubuntu-latest + Added: runs-on : jog j o g steps : - uses : actions/checkout@v4
We’ve felt your pain.
 At our last company, CI cost us over $50K a month.
80 % less than GitHub. 70 % less than Blacksmith and WarpBuild.
 1,000 minutes: $6 on GitHub, $1.20 on Jog.
5,000 free minutes every month While you have credits.
2 4 8 16 32
 jog · 2 vCPU · 8 GB
 USD per minute
 $0.002 $0.004 $0.006 $0
 Jog : $ 0.0012
Namespace : $ 0.003
Blacksmith : $ 0.004
WarpBuild : $ 0.004
 GitHub : $ 0.006
Depot : $ 0.006
Pay-as-you-go list prices, Linux x64, same vCPUs, before free minutes. Checked October 2026. Namespace has half the memory. Questions
 Do I change anything else? Not in your workflows, beyond runs-on. Jobs run on Ubuntu 24.04 with GitHub's runner tools, less a few large ones; a job that uses one needs a step that installs it.
 Which sizes can I use? Any of these. Coming from a larger GitHub runner? Use the size with the same vCPUs. runs-on vCPU RAM Per minute
 jog 2 8 GB $0.0012
 jog-4vcpu 4 16 GB $0.0024
 jog-8vcpu 8 32 GB $0.0044
 jog-16vcpu 16 64 GB $0.0088
 jog-32vcpu 32 128 GB $0.0176
Where do my jobs run? On hardware we run ourselves: every job gets a fresh VM sized to it.
 Does it work with personal GitHub accounts? Yes. Add your own GitHub account, and Jog runs its private repositories the same way it runs an organization’s.
 Are there free minutes? Yes: 5,000 a month while you have credits, used first. Bigger machines use them faster. 2 vCPU 1 ×
 4 vCPU 2 ×
 8 vCPU 4 ×
 16 vCPU 8 ×
 32 vCPU 16 ×
Can I get my credits back? Yes. Unused credits are refundable at any time. Free minutes aren’t.
That’s it, folks.
 Cheap, fast runners. No frills.
 Get started on GitHub
Jog by Machine Intelligence Company
 Ask us on Discord (new tab)
 Terms & Privacy
 [email protected]
Built with ♥ in SF and Toronto
 1550 Mission St, San Francisco, CA 94103
 Jog 2026.10.22.1
 Painting: Monet, 1882

## 评论（2/2）

> **matthewgapp** · 2026-10-27T18:54:33.000Z　
> Hey HN, I'm Matt, I founded Jog with Nathan. We spent 50K/month on CI at our last company. Agents are writing a ton of code and making the problem worse so we wanted to fix it from first principles. Jog runs on dedicated hardware - Zen 4/5 chips - in the US and EU. Happy to answer any questions.

---

> **njaremko** · 2026-10-27T19:30:25.000Z　
> Hey everyone, Nathan (other co-founder) also here.We're bootstrapped, and on a mission to give people cheap fast CI.We've already saved companies millions in CI costs (and cut CI times in a lot of cases).I'll also be around to answer questions :)

## 导航

- 项目页：[[10-项目/usejog.com_d675e7c5]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
