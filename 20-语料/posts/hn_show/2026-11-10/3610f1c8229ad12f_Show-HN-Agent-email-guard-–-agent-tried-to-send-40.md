---
type: "corpus"
item_id: "3610f1c8229ad12f"
title: "Show HN: Agent-email-guard – agent tried to send 400 receipts, stopped at 5"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50432613"
project_url: "https://github.com/agentisend/agent-email-guard"
author: "Iammnhamza"
published_at: "2026-11-09T21:39:06Z"
captured_at: "2026-11-10T10:01:59+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-10"
pub_day: "2026-11-09"
tags:
  - 语料
  - hn_show
  - author_Iammnhamza
  - story_50432613
  - show_hn
metrics: {"points": 3, "comments": 1, "engagement_velocity": 3}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Agent-email-guard – agent tried to send 400 receipts, stopped at 5

> [!info] 一句话导读
> GitHub - agentisend/agent-email-guard: Blast-radius control for AI agents that send email: budgets, rate ceiling, loop detection, kill switch, approval holds. N…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50432613>
> 指标：点赞=3 · 评论=1 · engagement_velocity=3
> 作者：Iammnhamza　|　发布：2026-11-09T21:39:06Z
> 项目链接：<https://github.com/agentisend/agent-email-guard>
> 采集：2026-11-10T10:01:59+08:00　|　id：`3610f1c8229ad12f`

## 正文

GitHub - agentisend/agent-email-guard: Blast-radius control for AI agents that send email: budgets, rate ceiling, loop detection, kill switch, approval holds. Node, Python, PHP, Go. Works with any provider. · GitHub

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| .github/ workflows | .github/ workflows | | |
| go | go | | |
| mcp | mcp | | |
| node | node | | |
| php | php | | |
| python | python | | |
| redteam | redteam | | |
| spec | spec | | |
| .gitattributes | .gitattributes | | |
| CONTRIBUTING.md | CONTRIBUTING.md | | |
| LICENSE | LICENSE | | |
| PUBLISH.md | PUBLISH.md | | |
| README.md | README.md | | |
| SECURITY.md | SECURITY.md | | |
| composer.json | composer.json | | |
| View all files | | | |

# agent-email-guard

Blast-radius control for agents that send email: at most N sends an hour, M a minute, no repeated messages, no mail to an important or new recipient without a person, and one call that stops everything. Works in front of nodemailer, Amazon SES, Resend, Postmark, any SMTP server, or AgentiSend.

```
npm install agent-email-guard                         # Node / TypeScript
pip install agent-email-guard                         # Python
composer require agentisend/agent-email-guard         # PHP
go get github.com/agentisend/agent-email-guard/go     # Go
```

```
import { createGuard } from 'agent-email-guard';

const guard = createGuard({
  budgets: { perHour: 50, perDay: 300 },     // per key, UTC calendar periods
  rate: { perMinute: 10 },                   // sliding minute
  loop: { mode: 'full' },                    // repetition + recipient collapse
  approval: { recipients: ['@bigcustomer.com'], newRecipients: true },
});

const sendMail = guard.wrap((mail) => transporter.sendMail(mail));
await sendMail({ from: 'agent@yourapp.com', to: 'ana@example.com', subject: 'Your refund', text: 'Done.' });
// Refused → throws GuardRefused. Needs a person → throws ApprovalRequired; err.approve() sends it.
```

Every decision is one of `allow`, `hold_for_approval` or `refuse`, with a stable reason token, one human sentence and the numbers behind it:

```
{
  "outcome": "refuse",
  "reason": "loop_repetition_detected",
  "message": "Blocked: 3 near-identical emails already went to ana@example.com within 60 minutes, which matches a retry or script loop; review the agent before sending more.",
  "evidence": { "matching_sends_in_window": 3, "repetition_threshold": 3, "closest_body_similarity": 1, "window_ms": 3600000 }
}
```

## What it stops

| Failure | Rule | Default |
| --- | --- | --- |
| A retry loop sends one message 4,000 times | Refuse the 4th near-identical send (same To, subject and body ≥ 0.85 trigram similarity) inside 60 minutes | on |
| A loop rewrites each message but keeps mailing the same one or two inboxes | Refuse a send to an inbox holding ≥ 1/3 of a 20+ send window whose effective recipient count fell below 3 | on |
| An agent burns through a month of sending in an afternoon | Per-key hourly, daily and monthly budgets, reserved atomically | off until set |
| A burst that a provider or a recipient's server would throttle | Per-key sliding one-minute ceiling | off until set |
| Something is wrong and every agent must stop now | `guard.killSwitch.pause(reason)`; never resumes on a timer | — |
| Mail to an important customer, a new address, or anything your own rule flags | Hold for a person; `err.approve()` re-checks and sends | off until set |
| Addresses the agent must never mail | Suppression list, refused outright | off until set |

Mail to everyone else keeps flowing: a key that pages its owner 30 times an hour still sends a sign-in code to a new user.

## Advisory here, enforced at AgentiSend

agent-email-guard runs inside your agent's process. That makes it easy to adopt, and it also means code the agent controls can remove it, and two processes with the in-memory store keep two separate budgets. Use the Redis or Postgres store to share limits across processes.

AgentiSend enforces the same rules at the API, where the agent cannot bypass them: the budget, rate ceiling and kill switch live on the API key and apply to every process that uses it, a key can lower its own limits but never raise them, a paused key cannot resume itself, holds wait in an approval queue in the console, and the thresholds are published. The `agent-email-guard/agentisend` adapter speaks to it with the same decision shape:

```
import { createHostedGuard } from 'agent-email-guard/agentisend';

const guard = createHostedGuard({ apiKey: process.env.AGENTISEND_API_KEY, keyId: process.env.AGENTISEND_KEY_ID });
const decision = await guard.check(email);   // POST /emails/preflight: every send gate, nothing sent
await guard.send(email);                     // POST /emails: throws GuardRefused / ApprovalRequired
await guard.killSwitch.pause('Looping on one inbox.');
```

## One policy file, every language

Put the limits in `agent-email-guard.json` and load it from Node, Python, PHP or Go:

```
{ "key": "support-agent", "budgets": { "per_hour": 50 }, "rate": { "per_minute": 10 }, "approval": { "recipients": ["@bigcustomer.com"] } }
```

```
npx agent-email-guard validate                           # check the file
echo '{"to":"cto@bigcustomer.com"}' | npx agent-email-guard check   # exit 0 allow, 2 hold, 3 refuse
```

## Integrations

- AgentiSend: local guard around the SDK, or the hosted adapter above (example)
- nodemailer: `transporter.use('compile', nodemailerGuard(loadPolicy()))`, or `guard.wrap((mail) => transporter.sendMail(mail))` (example)
- Amazon SES (SDK v3): wrap `client.send(new SendEmailCommand(input))` with a five-line field mapping (example)
- Resend: wrap `resend.emails.send` and throw on `{ error }` (example)
- Postmark: wrap `client.sendEmail({ From, To, Subject, TextBody })` with `toGuardSend: (m) => ({ to: m.To, subject: m.Subject, text: m.TextBody, html: m.HtmlBody })`
- SMTP: any client, same pattern as nodemailer
- OpenAI Agents SDK: `tool({ ..., inputGuardrails: [emailInputGuardrail(guard)] })`; a refusal becomes the content the model reads
- Vercel AI SDK: an agent tool whose send is wrapped, so a refusal becomes the tool result the model reads (example)

## Languages

| Language | Package | Directory |
| --- | --- | --- |
| Node / TypeScript | `agent-email-guard` | node/ |
| Python | `agent-email-guard` (`import agent_email_guard`) | python/ |
| PHP | `agentisend/agent-email-guard` (`AgentiSend\AgentEmailGuard`) | php/ |
| Go | `github.com/agentisend/agent-email-guard/go` (package `emailguard`) | go/ |

All four implement one specification and pass the same conformance vectors: byte-identical reason tokens and messages, the same check order, and one Redis/Postgres layout, so a Node agent and a Python worker can share a budget.

## License

MIT. Copyright AgentiSend. See LICENSE. Contributions: CONTRIBUTING.md. Security reports: SECURITY.md.

## About

Blast-radius control for AI agents that send email: budgets, rate ceiling, loop detection, kill switch, approval holds. Node, Python, PHP, Go. Works with any provider.

## 评论（1/1）

> **Iammnhamza** · 2026-11-09T21:39:47.000Z　
> Hi HN. I run AgentiSend, an email API for applications and AI agents. This is the part we pulled out and open-sourced (MIT).The failure it's for: an agent's send tool times out, the model retries, and each retry changes a word, so idempotency keys never match. In the demo, 400 attempts to send one customer the same receipt: 5 go out, 395 are refused. (The demo raises the threshold so you can see it; the default refuses the 4th.)It's blast-radius control, not a filter. Whatever the model decides: at most N emails per hour/day/month, M per minute, no near-repeats to the same inbox, a kill switch, and a hold for recipients you mark (e.g. anyone the agent hasn't emailed before) until a person approves.Three forms, strongest first:- a Claude Code PreToolUse hook (npx agent-email-guard hook install) that checks every email-sending tool call, whichever MCP server it goes to- an MCP proxy (npx agent-email-guard mcp --wrap ...) for Cursor, Codex, Claude Desktop- a library for Node, Python, PHP and Go that wraps nodemailer, SES, Resend, Postmark or SMTPThe four libraries are one spec plus 49 shared test vectors, so they print the same decisions. npx agent-email-guard test runs 12 runaway scenarios (a prompt-injected forward, the 400-receipt loop, a recipient sweep, a reply-all storm) against a reference policy and shows what got through.Limits, stated up front: the library runs in the agent's process, so an agent that edits its own tools can route around it. The hook and proxy sit outside the agent's code but guard one machine. None of them stops someone who holds your provider API key from calling the provider directly. Our paid API enforces the same policy server-side, which is the only place that last gap closes. That's the line between free and paid.I'd like to hear about loops it misses and sends it blocks that it shouldn't.

## 导航

- 项目页：[[10-项目/github.com_739225b0]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
