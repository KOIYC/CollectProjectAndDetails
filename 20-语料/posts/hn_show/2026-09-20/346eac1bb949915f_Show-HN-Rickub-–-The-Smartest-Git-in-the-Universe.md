---
type: "corpus"
item_id: "346eac1bb949915f"
title: "Show HN: Rickub – The Smartest Git in the Universe"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49755312"
project_url: "https://rickub.com/"
author: "ssaboum"
published_at: "2026-09-18T14:56:41Z"
captured_at: "2026-09-20T09:37:45+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - hn_show
  - author_ssaboum
  - story_49755312
  - show_hn
metrics: {"points": 23, "comments": 20, "engagement_velocity": 23}
comments_count: 20
comments_total: 20
discovered_via: "hn:show_hn:90d"
---

# Show HN: Rickub – The Smartest Git in the Universe

> [!info] 一句话导读
> rickub — the git that's never gonna let you down

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49755312>
> 指标：点赞=23 · 评论=20 · engagement_velocity=23
> 作者：ssaboum　|　发布：2026-09-18T14:56:41Z
> 项目链接：<https://rickub.com/>
> 采集：2026-09-20T09:37:45+08:00　|　id：`346eac1bb949915f`

## 正文

rickub — the git that's never gonna let you down

# The smartest git in the universe.

A new home for your projects. Fast, independent, cheaper than GitHub and GitLab with no compromise on your data.

 rickub.com/rickub/web

## A full workflow, out of the box.

From your first push to your hundredth release — the tools your team works in every day.

 rickub.com/rick/portal/cmd/ciguest/main.go

Orgs, members and repositories — everything you need to work and to keep that work secured.

 rickub.com/rick/portal/merge/42/files

The familiar files-changed, diffs and inline comments — plus an intent marker on every comment, so it is never ambiguous what blocks a merge and what is a passing remark.

 rickub.com/rick/portal/actions/runs/318

GitHub Actions workflows run unchanged, so a migration is a push rather than a rewrite — and the .rickub dialect adds what Actions has no syntax for, like test reports built into the run page.

 rickub.com/rick/portal/merge/42

A reviewer you trigger on a merge request: a summary, inline notes where they belong, and a clear verdict. Included on every plan, processed in the EU, never used for training.

 ~/code/portal

# same namespace, same token as your git remote

$ docker push rickub.com/rick/portal:1.2.0

1.2.0: digest sha256:9f3a… size 2841

$ helm push portal-1.2.0.tgz oci://rickub.com/rick/charts

Pushed: rickub.com/rick/charts/portal:1.2.0

$ oras push rickub.com/rick/portal:1.2.0-sbom sbom.spdx.json

Pushed · artifact type application/spdx+json

Publish and pull any OCI artifact — container images, Helm charts, SBOMs, WASM — from the same namespace as your code, with one login and one permission model.

 ~/code/portal

$ rickub mr create --title "portal: stabilise diffs"

→ !42 opened · Athena review requested

$ curl -H "Authorization: Bearer $TOKEN" rickub.com/api/v1/repos/rick/portal/merge/42

{ "number": 42, "state": "open", "athena": { "issues": 2 } }

# MCP: rickub.com/mcp — same token, same permissions

Drive everything from the rickub CLI or the token-authenticated JSON API. A hosted MCP endpoint lets your agents open, review and merge — under the same permissions you have.

 rickub.com/rick/portal/releases

Track large files with standard Git LFS, cut releases from any tag, and share downloads with your users.

Jobs 6 Logs Tests 4,317 Artifacts 1

4,317 tests 4,314 passed 3 failed 8m28s duration

rickub/web/actions 98 passed 10ms

rickub/engine/pack 412 passed 3 failed 2.1s

Test reports, built in

## Embedded test reports

Use the rickub Actions syntax and every run gets a Tests tab — totals, per-suite timings, and each failing test's own output, to make a review easier.

Athena · AI code review

## A reviewer on every merge request.

Athena is rickub's built-in AI review agent. Run it on a merge request to get direct feedback, without a never-ending thread of comments.

Athena AI

Billing change touching invoice rounding and a seat-index migration. Logic is sound; two things worth a look before merge.

- Requested at Sep 7, 07:07
- Review time 45s

★ Kudos @rick src/lib.rs · L42

Nice — deriving the archive set from what `rollback` actually restores is exactly right.

ℹ Info @summer src/lib.rs · L88

FYI this path is also hit by the nightly job; no change needed.

✋ Request change @morty migrations/0042.sql · L3

Needs `CONCURRENTLY` — this takes a write lock on a 40M-row table.

## Say what you mean.

Every inline comment carries an intent, so a request for change is unambiguous and praise never goes unnoticed.

# Quokka — A Deterministic, Self-Hosted Programming Language for AI Workflows

## 评论（20/20）

> **woodrowbarlow** · 2026-09-18T15:50:00.000Z　
> yet another gitea/forgejo instance with some extra plumbing, hosted in the EU. this is a github alternative, not a git alternative. rickub's conflation of the two seems deliberate.

---

> **bfung** · 2026-09-18T16:00:28.000Z　
> Don’t know about the backend, but site looks generated from aistudio.google.com or Gemini 3.8 flash.I happened to be messing around with aistudio and site looks eerily similar.https://luggage-packing-optimizer.ai.studio/

---

> **ivanjermakov** · 2026-09-18T16:00:36.000Z　
> I'm not using proprietary git hosting again.

---

> **haburka** · 2026-09-18T16:08:16.000Z　
> Can’t tell if this is satire or just a vibe coded landing page. I really hope this is not a VC backed company.

---

> **SrslyJosh** · 2026-09-18T16:16:29.000Z　
> > The tools we host code on were designed for a different era — before AI wrote half the diff, before half our time went on reviews or waiting for CI, and before data sovereignty and protection was a concern.Hello, slop. closes tab

---

> **adityamishra241** · 2026-09-18T16:23:11.000Z　
> Curious how much of this is actually a new version-control model versus a much better abstraction over Git. The latter could still be valuable, but I'd love to see where the underlying primitives change.

---

> **daniels1006** · 2026-09-18T16:24:10.000Z　
> I find these AI generated UXs so tiring to the eyes. Not sure if it's the ubiquity of them, the similarity or the excess of elements on the screen.

---

> **fny** · 2026-09-18T16:30:30.000Z　
> While I'm excited for more entrants in this space. It's depressing that there's no way to measure how much effort was put in a piece of software.The distrust I feel for "Show HN" posts is depressing.I know this will sound absurd, but in the good old days, even the claim of having built something indicated quality. This hubris is not limited to the front page, I've experience new products from well establish companies that are horseshit because they vibe code without doing any real QA or UX polish.The convergence of claim with product as opposed vaporware is toxic.

---

> **manewitz** · 2026-09-18T16:36:43.000Z　
> I'm in favor of GitHub alternatives in general. When we looked at what moving or mirroring our repos off of GitHub would look like since their uptime has been falling, the real bottleneck was all the dependencies that still live there. If (when) GH has an outage and we NEED to deploy, we would have to be mirroring all of those dependencies in an accessible way to get a deploy out. In that (sort of) hypothetical situation, the lowest-tech hot fix would be a manual code-edit across servers.

---

> **ghthor** · 2026-09-18T17:08:37.000Z　
> Excellent, I always wanted forge to be down from litigation

---

> **CodeMage** · 2026-09-18T19:53:38.000Z　
> > "with no compromise on your data"And yet it says there's an AI reviewer on every merge request and I don't see any documentation on whether that can be disabled.

---

> **spennant** · 2026-09-18T16:20:32.000Z　
> Luggage Packing Optimizer? The nerdiness level is awesome and I'm here for all of it!

---

> **ASalazarMX** · 2026-09-18T20:04:20.000Z　
> The explode slider only raises the height of two green boxes, it has the same energy as those impressive Chinese robots when they trip and fall.I'm worried that I'm starting to find those glitches endearing.

---

> **sshine** · 2026-09-18T17:47:29.000Z　
> Forgejo/gitea are just so damn CVE ridden, and GitLab asks for 16G RAM as a minimum. All Rust-written forges have terrible web UI.

---

> **ssaboum** · 2026-09-18T16:43:56.000Z　
> it's not

---

> **kristianc** · 2026-09-18T16:28:11.000Z　
> For me it's a trust gap. Because I know the website UI has been automatically generated, I can't be sure of how much of the product is actually real, or how closely the claims on the page have been audited.

---

> **biohazard2** · 2026-09-18T16:48:08.000Z　
> I get the same feeling, it's difficult to estimate if it's just a vibe-coded platform, or a carefully crafted project; if it's a one-man job that can crumble at any time, or a stable service powered by a motivated team. The comparison with other services is also not super honest, cherry-picking elements to put in bold (e.g. the higher price than GitLab that is highlighted, or the Agent access), when it has nothing to be ashamed of.OP seems quite knowledgeable (e.g. https://ogirardot.writizzy.blog/p/rickub-1-8-faster-then-git...), and their company ARUKU has been established in 2011, which makes me a bit more confident in this platform. But there are no details about the team, the software, since how much time they're working on it, etc.At the same time, if you just use public repositories and synchronize them somewhere else for backup, there's not much risk in testing it. There's a free tier, they do have some neat features (that they don't really advertise) if you come from GitHub, like an import process that can copy PRs and issues or good compatibility with Actions.The UI definitely needs a bit of love. While it's quite similar to other forges (you're not lost in the interface), it feels a bit rough. And the scrollbar presence or absence pushing the whole page left or right really bothers me.

---

> **ssaboum** · 2026-09-18T20:10:14.000Z　
> it's disabled by default and only on MRs if you launch it

---

> **bfung** · 2026-09-18T19:35:44.000Z　
> yep, I belong here on HN, haha!

---

> **daniels1006** · 2026-09-18T16:52:11.000Z　
> Sure it is! Instantly feels like some subset of all those elements on the screen are not real or have not been properly tested. More often than not that's the case.

## 导航

- 项目页：[[10-项目/rickub.com_49d019bd]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
