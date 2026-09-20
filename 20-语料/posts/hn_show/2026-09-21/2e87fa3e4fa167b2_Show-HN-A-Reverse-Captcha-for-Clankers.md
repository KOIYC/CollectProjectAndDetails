---
type: "corpus"
item_id: "2e87fa3e4fa167b2"
title: "Show HN: A Reverse Captcha for Clankers"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48344669"
project_url: "https://clanker-captcha.jeromem.workers.dev/"
author: "rydgel"
published_at: "2026-05-31T10:48:45Z"
captured_at: "2026-09-21T02:52:46+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-31"
tags:
  - 语料
  - hn_show
  - author_rydgel
  - story_48344669
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:144d"
---

# Show HN: A Reverse Captcha for Clankers

> [!info] 一句话导读
> Author: Made by  Jérôme Mahuet .

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48344669>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：rydgel　|　发布：2026-05-31T10:48:45Z
> 项目链接：<https://clanker-captcha.jeromem.workers.dev/>
> 采集：2026-09-21T02:52:46+08:00　|　id：`2e87fa3e4fa167b2`

## 正文

Author: Made by  Jérôme Mahuet .

Clanker CAPTCHA Demo

# Clanker CAPTCHA

 A playable CAPTCHA built for software instead of people. The answer is hidden in the image frames, and the page publishes everything an agent needs to dig it out. Nobody expects a human to solve this one.

 Made by Jérôme Mahuet.

3-4 frames Coherent fusion required

30s TTL Fresh challenge window

No answer leak Server keeps the checksum

## Live challenge

 Playable widget The widget here is the exact library a host page would drop in. This page only hands it a mount point and a couple of endpoint URLs.

 Server-kept secret The answer never reaches the browser. All the widget gets are the image frames, some public solve parameters, and a challenge id that expires within seconds.

 Library-owned metadata The widget injects `clanker-agent-task`, hidden instructions, current challenge data attributes, and an `application/clanker+json` manifest.

## Why reverse the usual CAPTCHA shape?

 The usual CAPTCHA looks for something people find easy and software finds hard. That gap has been closing for years. Clanker CAPTCHA flips it around: the task is a pain to do by hand against a timer, but simple for an agent that can read pixels and do a little math.

 None of the method is hidden. The challenge is spelled out for any agent willing to play along, the answer stays on the server, and a solver still has to do the work to find it.

 This is a research demo, not a security product. Think of it as a rough sketch of how agent-facing verification might work, not something you would put in front of real abuse.

 No hidden answer The browser sees the instructions, the images, and the public parameters. It never sees the checksum.

 Agent readable The widget drops in machine-readable metadata and a JSON manifest describing the challenge.

 Pixel grounded You are meant to solve it from the rendered frames, not by scraping a value out of the DOM.

## Why would a CAPTCHA for agents be useful?

 This kind of CAPTCHA does not care whether you are human. What it cares about is whether automated access happened in the open, tied to a live challenge you can measure. That helps when you already expect capable agents to turn up and would rather hand them a clear protocol than treat them as malfunctioning people.

 Forget "human or bot." The real question is whether this caller did the requested work for a fresh challenge, followed the public rules, and did it before reaching for the protected action. Whatever signal that produces, a host can weigh it against the usual things: account age, rate limits, reputation, payment status.

 Cooperative agents Gives agents a documented way to show they can read the page and respect site policy.

 Cost shaping Makes throwaway automation burn real compute on fresh per-session evidence instead of replaying a token.

 Audit trail Publishes a structured manifest, so the solve path is easy to inspect when something breaks.

 In practice you would put it in front of the expensive actions: creating accounts, hammering a sensitive endpoint, retrying checkout, minting API keys. It will not replace authorization. It just adds a little friction and some evidence, built with browser agents in mind instead of aimed at them.

### Why make it hard for a human?

 Sometimes the lane you are protecting is meant for software, not hands on a keyboard: agent APIs, automation consoles, bulk jobs, crawler deals. A puzzle a person can solve is the wrong fit there. It just invites people to solve it by hand, pay someone a few cents to click, or screenshot it and pass it along.

 Making it hostile to humans on purpose is a way of saying who the lane is for: an accountable agent that reads the pixels and follows the manifest. That is worth doing when you want human flows and machine flows kept apart, rather than jammed behind one checkbox.

 Do not use this to lock people out of something they actually need. If a flow is for humans, give humans a way through. The hostile version is for agent-only gates, research demos, and controlled automation surfaces where stopping manual solves is the whole idea.

## What signal does the host get?

 A normal checkbox really only tells you "something got clicked." This aims for something with more in it: a specific browser session pulled a fresh challenge, showed its manifest, ran the computation, and sent back the checksum and nonce before the clock ran out.

 On its own it is not identity, just one input into a bigger decision. A host can pair it with session age, account trust, request velocity, IP reputation, whatever crawler policy it has.

 Freshness Each challenge expires and is recorded once on the server, so a stale solve is worthless as a reusable credential.

 Page-state awareness The intended solver must inspect rendered frames and the manifest produced by this widget instance.

 Compute evidence The checksum requires spectral fusion and the submit body includes a proof-of-work nonce.

 Debuggable contract The hidden instructions and JSON manifest make failures explainable for compliant agents and maintainers.

## The challenge tricks

 It looks chaotic on screen, but the real puzzle is in the frequency domain. Every frame carries the genuine signal, some per-frame decoys, and a layer of noise that is just for show. You have to fuse the frames before you trust whichever peak looks strongest.

 Fused frames Every image contributes to the same answer, but a single image can emphasize the wrong cell.

 Fiducial corners Four off-grid markers per slot let an agent reconstruct geometry from evidence instead of receiving it directly.

 Phantom carriers Decoys have random phase per frame, so they look convincing locally and wash out under coherent fusion.

 Proof of work The answer alone is not enough; the submit payload also includes a nonce bound to the challenge id.

### 1. Coherent fusion beats single-frame reading

 Real carriers keep the same phase across frames. Decoys and phantoms do not. If a solver sums complex spectra across every image, real carriers reinforce. If it reads one image, a phantom can point at the wrong cell.

### 2. The lattice is marked, not disclosed

 Each symbol slot has four fiducials just outside the data grid. They reveal the slot anchors, stride, and vertical step, but the raw values are not sent as ordinary JSON fields. The solver must recover them from spectral peaks.

### 3. The codebook is public but shuffled

 The challenge response discloses the transform, layout, permutation, checksum formula, and proof-of-work requirement. The solver still has to read the data cell from the fused image evidence.

## Protocol walkthrough

01

 The host page mounts `ClankerCaptcha` with `challengeUrl`, `verifyUrl`, and an optional `onSolved` callback.

02

 The widget fetches a challenge, renders every frame into the DOM, starts the countdown, and prepares the browser-side proof of work.

03

 The library injects `meta[name="clanker-agent-task"]` and an `application/clanker+json` manifest containing image selectors, data URLs, solve parameters, and submit details.

04

 A solver computes the DFT of every frame, sums the complex spectra, recovers the lattice, decodes the symbols, computes the checksum, finds the nonce, and submits the result.

05

 The server checks expiry, proof of work, and checksum. A solved challenge returns a token and is removed from the in-memory map.

## Integration shape

 A host page should not hand-author the agent metadata. That belongs to the library because it has the current challenge, instance id, frame selectors, and manifest id.

```
<div id="clanker"></div>



```

 The server in this repo is deliberately tiny and has no dependencies. It is here to show the endpoint contract, not to be a blueprint for a production backend.

### Three surfaces to integrate

 Website Mount the widget, let it inject metadata, and pass the returned token into your normal form or session flow.

 Agent Read the manifest, resolve frame selectors, compute the answer from pixels, and submit the nonce-backed result.

 Backend Generate short-lived challenges, keep the expected answer server-side, verify once, and issue an app-specific token.

 Policy Decide what a pass means for your product: lower friction, access to an automation lane, or an input to risk scoring.

## What this is not claiming

 This is not a complete security product. A production deployment would need durable challenge state or signed state, replay defense, rate limits, telemetry, token binding, CSRF and CORS policy, and a clear abuse model.

 The useful part of the experiment is the interface: a widget that exposes machine-readable instructions while keeping the answer out of the browser, plus a challenge whose intended solution is grounded in rendered pixels.

# octelium/cordium

## 导航

- 项目页：[[10-项目/clanker-captcha.jeromem.workers.dev_bff8bfe7]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
