---
type: "corpus"
item_id: "614e7eaef38ab5e2"
title: "Show HN: Graftfork: rebase fork patches onto each upstream release, test-gated"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50356948"
project_url: "https://graftfork.com/try"
author: "craigm26"
published_at: "2026-11-03T19:28:07Z"
captured_at: "2026-11-04T09:51:43+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-04"
pub_day: "2026-11-03"
tags:
  - 语料
  - hn_show
  - author_craigm26
  - story_50356948
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Graftfork: rebase fork patches onto each upstream release, test-gated

> [!info] 一句话导读
> graftfork is now in Claude's connector directory. Connect it in Claude →

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50356948>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：craigm26　|　发布：2026-11-03T19:28:07Z
> 项目链接：<https://graftfork.com/try>
> 采集：2026-11-04T09:51:43+08:00　|　id：`614e7eaef38ab5e2`

## 正文

Skip to content
 graftfork is now in Claude's connector directory. Connect it in Claude →
graftfork
 Try it How it works Rebuilds Pricing Teams Docs Security FAQ Changelog
 Sign in Sign up free
Try it, no sign-up
See what Graft would do with your fork
Paste a public GitHub fork, or any copy of an open-source project with your changes as commits on a release. Graft moves your changes onto upstream's newest release in a sandbox, runs your tests, and shows you the change it would deliver.
Try it
Trying a fork is closed until Graft opens, for everyone. Your dashboard works: connect your copy in Copies , or rebuild a program from its spec in Specs .
No fork to hand? Try a real one, in one click:
pattonw/tqdm Python, moves clarketm/pflag Go, moves sigmavirus24/requests moves guyernest/arrow stays, and says why
What a try does
Finds the facts. The upstream (a fork's parent, or the project your files name), the release your changes sit on, how many changes are yours, and upstream's newest release.
Moves your changes in a sandbox. A short-lived sandbox (a Claude Managed Agents container on Anthropic, deleted within minutes of the try ending) clones your public fork, carries each change onto the newest release, and runs your tests if it finds them (Python and Node projects, or a .graft.yml ).
Tells you what happened. Each change kept, dropped because the release already has it, or conflicting; the tests' verdict; and the change Graft would deliver, with its diff. You watch each change decided as it happens, and you can share the result: its link, a card image, or a post to X or LinkedIn.
What it can't do
Push. A try has no access to your repository beyond a public clone, no write token ever enters its sandbox, and the runner refuses to push a try whatever it's told.
Use an agent. A try runs the no-agent path. A conflict is shown as a conflict. Once you're connected, Premium resolves conflicts automatically, your first one is free, or you can use your own Anthropic key.
Run long. Ten minutes at most, up to ten tries running at once and fifty more waiting in line, ten tries a day per visitor (people on one network share them). Public repositories only. A result for the same fork and release is reused for 24 hours.
We keep the result, the repository's name and a salted hash of your IP address (for the limits) for 30 days, then delete them. See privacy .
graftfork Keep your changes. Keep getting updates. Never move onto a copy that fails your tests. Graft carries your changes to an open-source project onto each new release and delivers the moved branch only when your tests pass; it can also rebuild a program from its spec.
Product
 How it works
 Rebuilds from a spec
 Pricing
 For teams
 Getting started
 Sign up free
Resources
 Try it, no sign-up
 Examples
 A rebuild, replayed
 Results
 Compared
 Changelog
 Status
 FAQ
 Evidence and method
 For agents: graftfork.ai
Company
 About
 Security
 Privacy
 Terms
 DPA
 Agent change record
Support
 support@graftfork.com
 Your copies
 Report a vulnerability
© 2026 Craig Merry, sole proprietor. graftfork.com Status

## 评论（1/1）

> **verdverm** · 2026-11-03T20:26:53.000Z　
> this is something that can be done with a cron, script, and LLM when conflicts happen - without the middleman needing to make a profitthis is how I have done it in the past anyhow (before project abandonment)

## 导航

- 项目页：[[10-项目/graftfork.com_7a73c1b4]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
