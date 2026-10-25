---
type: "corpus"
item_id: "eab22ca42e0df421"
title: "GPT-Load: a self-hosted AI gateway with reversible text redaction"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1x6lrll/gptload_a_selfhosted_ai_gateway_with_reversible/"
project_url: "https://github.com/tbphp/gpt-load"
author: "Suspicious-Tutor-881"
published_at: "2026-10-15T21:33:04+08:00"
captured_at: "2026-10-25T23:28:44+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-25"
pub_day: "2026-10-15"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Release (AI)
metrics: {"score": 38, "comments": 24, "upvote_ratio": 0.6759259259259259}
comments_count: 24
comments_total: 24
discovered_via: "reddit:14d+settle10"
---

# GPT-Load: a self-hosted AI gateway with reversible text redaction

> [!info] 一句话导读
> Hi, I'm the author of GPT-Load, an MIT-licensed AI gateway with 7,000+ GitHub stars.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1x6lrll/gptload_a_selfhosted_ai_gateway_with_reversible/>
> 指标：得分=38 · 评论=24 · 赞踩比=0.6759259259259259
> 作者：Suspicious-Tutor-881　|　发布：2026-10-15T21:33:04+08:00
> 项目链接：<https://github.com/tbphp/gpt-load>
> 采集：2026-10-25T23:28:44+08:00　|　id：`eab22ca42e0df421`

## 正文

Hi, I'm the author of GPT-Load, an MIT-licensed AI gateway with 7,000+ GitHub stars.

It manages API keys and supported subscription accounts in one place. Your clients connect through the gateway, which handles credential scheduling, automatic failover, access controls, request logs, and usage tracking.

It runs with Docker Compose or as a single Go binary, includes a web UI, and uses SQLite by default. You don't need a separate database to get started.

One feature I'd particularly like feedback on is **reversible request redaction**.

Configurable regex rules replace or encrypt matching text locally before it reaches an upstream service. If the model returns intact, valid ciphertext, GPT-Load can restore the original values in response text and client-side tool arguments.

For example, an email address can be encrypted before reaching the model, then restored when the model includes that ciphertext in a tool call returned to your client. The rules apply to supported text fields; image and file contents aren't covered.

There's also an optional, experimental **JEV guardrails** integration. It reviews outgoing text against custom rules and can warn or block on matches. It uses an external review service, is disabled by default, and failed or incomplete reviews may still allow requests through.

You host the gateway, not the cloud models behind it. Cloud providers still receive the processed requests, and you need your own upstream access.

GitHub: [https://github.com/tbphp/gpt-load](https://github.com/tbphp/gpt-load)

Docs: [https://www.gpt-load.com](https://www.gpt-load.com)

I'd appreciate feedback on the Docker setup and how reversible redaction behaves with the clients you use.

AI disclosure: AI helped draft this post.

## 评论（24/24）

> **asimovs-auditor**（1 分） · 2026-10-15T21:33:14+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **Suspicious-Tutor-881**（5 分） · 2026-10-15T21:35:16+08:00　
> AI coding tools are used in the development of GPT-Load. AI also helped draft and edit the English text of this post. I'm the author and maintainer of the project.

---

> **TYPICALADMINISTRATOR**（5 分） · 2026-10-15T21:46:27+08:00　
> if the model mangles or rewords the ciphertext, can the original value still be restored or is that request just lost?

---

> **Suspicious-Tutor-881**（0 分） · 2026-10-15T22:05:18+08:00　
> If the ciphertext is changed, that value can't be restored. The response still returns with the altered token as-is, so a tool call relying on it may fail.

---

> **ImplementNo7145**（-1 分） · 2026-10-15T22:26:39+08:00　
> Looks neat, might give it a try. I've been looking for something like this to mainly oversee and log LLM requests across my Codex subs, OpenRouter keys, and local inference. Quick question: How are hidden reasoning blobs handled across the various upstream providers that choose to encrypt them?

---

> **Suspicious-Tutor-881**（-1 分） · 2026-10-15T22:34:11+08:00　
> We don’t decrypt provider-encrypted reasoning. On native routes, we pass it through and preserve the upstream behavior.

---

> **Decent_Election_4597**（-8 分） · 2026-10-15T22:34:13+08:00　
> v2.0.0-dev in the sidebar is a nice touch, feels like you're actually running something bleeding edge

---

> **Suspicious-Tutor-881**（2 分） · 2026-10-15T22:35:24+08:00　
> Haha, that screenshot is from my local dev build 😄

---

> **thatboyonabike**（5 分） · 2026-10-15T23:09:19+08:00　
> It's a bot.

---

> **ethansky**（4 分） · 2026-10-15T23:16:51+08:00　
> Bot

---

> **andreeinprogress**（-2 分） · 2026-10-15T23:30:56+08:00　
> Nice, going to try this ~~as my totally not Claude sub reroute~~ because CLIProxy has been giving me some issue lately and this seems to have a proper dashboard.

---

> **Suspicious-Tutor-881**（0 分） · 2026-10-15T23:43:00+08:00　
> Thanks for giving it a try! Hope you find it useful 🙂

---

> **buldezir**（1 分） · 2026-10-16T00:28:57+08:00　
> how fast Anthropic will ban subscription account for using with such gateway?

---

> **fernandops**（0 分） · 2026-10-16T07:04:30+08:00　
> Could the client get a flag when a value couldn’t be restored, so it can stop that tool call for review? Returning the altered token as ordinary text makes the failure hard to distinguish from a valid argument. For something like a recipient address, silently passing it along would be a bad default.

---

> **wabbajack3000**（1 分） · 2026-10-16T07:18:50+08:00　
> Genuine question from some new to this - is this an alternative to litellm or serving a different purpose? If I've already setup litellm as my gateway, what are the main reasons to give this a try (or to stick to litellm)?
>
> Good job nonetheless!

---

> **Suspicious-Tutor-881**（1 分） · 2026-10-16T08:08:32+08:00　
> Thanks for the suggestion! We’ll look into how to improve this.

---

> **Suspicious-Tutor-881**（1 分） · 2026-10-16T08:12:46+08:00　
> >Hard to say with Anthropic subscriptions. There’s a risk of getting banned, so I’d be careful.

---

> **kantorcodes1**（-2 分） · 2026-10-16T09:21:18+08:00　
> The reversible-redaction design is the interesting part. One edge on the reverse pass: the model gets ciphertext, but models paraphrase. If it returns the ciphertext slightly altered or split across sentences, does GPT-Load fail closed and leave it encrypted, or does it attempt a partial restore? Curious how you handle a model that "fixes" the ciphertext's formatting.

---

> **Suspicious-Tutor-881**（0 分） · 2026-10-16T09:49:02+08:00　
> That's a very good question. We don't try to repair damaged ciphertext returned by the model; we return it as-is. Modifying content we can't reliably recover could cause bigger problems. This may cause a tool call to fail, but we won't restore plaintext from ciphertext that fails authentication.
>
> Redaction also supports fixed replacements (non-reversible), which users can choose instead.

---

> **Joncallim**（0 分） · 2026-10-16T15:25:43+08:00　
> Does redaction also cover the gateway’s request logs, or just the text sent upstream?

---

> **Suspicious-Tutor-881**（2 分） · 2026-10-16T16:36:37+08:00　
> Matching text is replaced or encrypted before being sent upstream. Request-body logging is off by default and intended for debugging. If enabled, it records the original request body.

---

> **Joncallim**（0 分） · 2026-10-16T22:17:48+08:00　
> Ah, good to know the debug logs keep the original. Thanks for clearing that up.

---

> **Future_AGI**（0 分） · 2026-10-17T00:13:18+08:00　
> is the ciphertext deterministic per value? If the same email always encrypts to the same token (AES-SIV style), the model can refer to one person consistently across turns and prompt caching keeps hitting, but anyone reading the upstream logs can tell which fields are equal. Random nonces hide that at the cost of a fresh token every turn, which tends to confuse multi-turn tool calls.

---

> **Suspicious-Tutor-881**（1 分） · 2026-10-17T00:23:36+08:00　
> Yes. We use deterministic AES-SIV encryption per access key to keep references consistent across turns and help with prompt caching. Within that scope, identical values produce identical ciphertext.

## 关联链接

- https://www.gpt-load.com

## 导航

- 项目页：[[10-项目/github.com_439d4e7f]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
