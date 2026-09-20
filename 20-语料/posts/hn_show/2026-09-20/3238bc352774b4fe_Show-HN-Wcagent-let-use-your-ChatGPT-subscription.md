---
type: "corpus"
item_id: "3238bc352774b4fe"
title: "Show HN: Wcagent let use your ChatGPT subscription for coding"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49761790"
project_url: "https://wcagent.ai/"
author: "losalah"
published_at: "2026-09-18T23:46:17Z"
captured_at: "2026-09-20T14:01:30+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - hn_show
  - author_losalah
  - story_49761790
  - show_hn
metrics: {"points": 3, "comments": 2, "engagement_velocity": 3}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:90d"
---

# Show HN: Wcagent let use your ChatGPT subscription for coding

> [!info] 一句话导读
> wcagent — AI coding with local tools and verifiable results

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49761790>
> 指标：点赞=3 · 评论=2 · engagement_velocity=3
> 作者：losalah　|　发布：2026-09-18T23:46:17Z
> 项目链接：<https://wcagent.ai/>
> 采集：2026-09-20T14:01:30+08:00　|　id：`3238bc352774b4fe`

## 正文

wcagent — AI coding with local tools and verifiable results

# An AI coding agent. Local tools. Verifiable results.

wcagent connects an eligible AI service to task-relevant repository context, developer-approved commands and file changes, and verification through tests, builds, diagnostics, and diffs.

Model access is separate · Local actions follow your approval settings · Provider terms and usage limits always apply

ChatGPT Claude Gemini Grok DeepSeek

Independent third-party services · Availability and eligibility depend on provider and account type

## From model response to verified change

You provide eligible AI access. wcagent provides the repository context, controlled local tools, task coordination, and evidence inside VS Code.

### Connect eligible AI access

Choose an AI service and connection method you are authorized to use. Availability depends on the provider, account type, and applicable terms.

payments-api — Visual Studio Code

refund.ts refund.test.ts

```
export async function retryRefund(id) {
  return withBackoff(async () => {
    const result = await capture(id);
    if (!result.ok) throw result;
    return result;
  }, { attempts: 3 });
}
```

WebCodingAgent

Make refund retries safe, then prove they work.

✓ Read refund flow ✓ Edit retry boundary ✓ Run pnpm test ✓ Review concurrency risk

✓ Verified · 18 tests passed · diff recorded

### Give the model only what it needs

The context engine ranks repository paths, symbols, diagnostics, active editors, and project instructions, then sends focused task context to the AI service you select.

Context map Ready · 1.4s

▾ src ▾ billing refund.ts retry.ts checkout.ts ▾ tests refund.test.ts package.json

Ranked for “safe refund retries”

src/billing/refund.ts

tests/refund.test.ts

src/billing/retry.ts

package.json

2 diagnostics 5 symbols AGENTS.md active editor

03 / PROOF

### Turn model responses into working code

VS Code applies approved changes, runs tests and builds locally, and records diffs and diagnostics. A model response alone is never treated as completion.

See the trust model ↗

Test suite 18 / 18 All required checks passed

Change set+48 −6 4 files · hashes verified

Specialist review

Concurrency boundary cleared

Completion gate Ready Every acceptance criterion has evidence

### Connect AI access you are authorized to use.

Select an eligible connection, then give wcagent the coding outcome you want inside the VS Code workspace that owns the repository.

0 model access resold 1 eligible AI account

### Give the model relevant repository context.

wcagent selects task-relevant files, symbols, diagnostics, and instructions without replacing your editor workflow.

### The model suggests. VS Code verifies.

Commands, edits, tests, and approvals remain local while an eligible AI connection supplies the reasoning.

1 selected AI connection 4 forms of completion evidence 100% local command control

## AI reasoning. Local authority.

A wcagent plan covers the VS Code extension, context selection, task coordination, local tool controls, recovery, and evidence history. AI model access is supplied separately by the user.

01

Connect eligible AI access Use a provider, account type, and connection method permitted for your account.

Keep execution where the code lives Commands, mutations, redaction, and workspace confinement stay authoritative inside desktop VS Code.

03

Keep one editor workflow Use an available eligible connection without rebuilding your local development setup.

Finish with repository evidence Tests, builds, diffs, and diagnostics—not model confidence—decide when the work is done.

## Provider controls always apply.

wcagent does not increase, reset, conceal, or bypass provider usage limits. It does not defeat authentication, CAPTCHAs, safety systems, geographic restrictions, or other technical access controls.

### You supply the AI account

wcagent does not include, sell, or resell access to an AI model.

### Authorization depends on the provider

An eligible connection uses a provider, account type, and integration method whose terms permit its use with wcagent.

### A refusal pauses the connection

If a provider refuses or limits a request, wcagent reports that result and cannot make the provider accept it.

### Provider terms remain in force

You must maintain your own eligible account and comply with its plan limits, policies, and applicable terms.

## Bring AI into your VS Code workflow.

Install wcagent from the Visual Studio Marketplace, connect eligible AI access, and keep repository actions under your local approval settings.

One wcagent plan. AI model access is supplied and billed separately.

## 评论（2/2）

> **botataiapp** · 2026-09-19T13:48:29.000Z　
> Will it keep my files changes and commands directly inside VS Code?
> if yes, that is really brilliant.

---

> **losalah** · 2026-09-19T14:24:42.000Z　
> Yes it does, everything inside vscode

## 导航

- 项目页：[[10-项目/wcagent.ai_f883dabc]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
