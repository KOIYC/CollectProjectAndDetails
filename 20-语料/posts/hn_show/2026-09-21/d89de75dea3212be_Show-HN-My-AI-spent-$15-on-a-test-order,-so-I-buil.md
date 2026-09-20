---
type: "corpus"
item_id: "d89de75dea3212be"
title: "Show HN: My AI spent $15 on a test order, so I built a payment guardrail"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49511045"
project_url: "https://github.com/felixpg13-glitch/spendshield"
author: "felixpg13"
published_at: "2026-08-31T15:37:00Z"
captured_at: "2026-09-21T03:11:20+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - hn_show
  - author_felixpg13
  - story_49511045
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:52d"
---

# Show HN: My AI spent $15 on a test order, so I built a payment guardrail

> [!info] 一句话导读
> felixpg13-glitch/spendshield

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49511045>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：felixpg13　|　发布：2026-08-31T15:37:00Z
> 项目链接：<https://github.com/felixpg13-glitch/spendshield>
> 采集：2026-09-21T03:11:20+08:00　|　id：`d89de75dea3212be`

## 正文

# felixpg13-glitch/spendshield

AI Agent 付款安全层: 身份/意图/密钥 三道信任支柱 + 四道闸门。给 AI 定义带消费上限的数字身份(Spend-Capped Identity), 防提示注入, 密钥不落盘。Python + MCP。

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- Default branch: main
- Created: 2026-08-31T08:52:54Z

## Languages

- Dockerfile
- Python

## Topics

- agent-security
- ai-agents
- guardrails
- llm-security
- mcp
- payment-security
- python
- python-library

## Top Contributors

- felixpg13-glitch (27 contributions)

---

## README

# 💰 SpendShield — Payment Guardrails for AI Agents

> **Before your AI spends real money, it passes through SpendShield.**

An open-source payment safety layer for Python and MCP. Give your AI agent a **spend-capped digital identity (KYA)**, run every payment through four deterministic gates, defend against prompt injection, and keep secrets in an encrypted vault.

## 🩸 Why this project exists (a real incident)

On August 9, 2026, my automation system ran a test order. I sent `dry: true`, expecting a price preview. The server only honored `?dry=1` — **4 orders of ¥99 were charged for real, and the money was gone.**

This is not just my problem. AI agents are about to order food, top up accounts, and call paid APIs on your behalf. **When AI starts spending real money, who puts a gate in front of it?**

I turned my scar into a library.

## ✨ Three trust pillars

| Pillar | What it does |
|---|---|
| 🔑 **Identity (KYA)** | Every agent gets a digital identity with its own budget/blacklist/limits. **Unregistered agents are denied by default.** |
| 🎯 **Intent alignment** | New recipients and large amounts **always require human sign-off** — stops prompt-injected agents from spending without you. |
| 🔐 **Secret vault** | Keys encrypted at rest (AES-256), master key never on disk. Key access passes the gates and is **fully audited**. |

## 🚧 Four deterministic gates

Every spend passes all of them. Rules are code, not AI opinion — agents cannot argue, trick, or inject their way past.

| Gate | Default | Effect |
|---|---|---|
| 🧪 **dry_run** | On | Preview only. Nothing executes until you say so. |
| 💰 **budget** | Unlimited | Hard ceiling. Over budget means denied. |
| 🚧 **max_amount** | Unlimited | Per-transaction cap. |
| 🙋 **approval** | Off | Human sign-off — console, Telegram, or webhook. |
| 📜 **audit** | On | Every attempt recorded, exportable JSON. |

## 🚀 Quick start

```bash
pip install spendshield
```

Or run it with Docker (MCP server):

```bash
docker build -t spendshield .
docker run -it spendshield
```

> 💡 Pre-built image on GHCR is coming soon (requires a workflow-scoped GitHub token to publish the CI pipeline).

```python
from spendshield import SpendShield, KeyVault

guard = SpendShield(budget=200, dry_run=True, whitelist=["McDonald's"])

@guard.protect("order")
def place_order(amount, to):
    return call_real_api(amount, to)

place_order(amount=99, to="McDonald's")
# => DryRunBlocked: dry_run mode, nothing executed

guard.dry_run = False
for i in range(4):
    place_order(amount=99, to="McDonald's")   # 3rd order blocked by BudgetExceeded
```

### Agent identity (KYA)

```python
guard = SpendShield(dry_run=False)
guard.register_agent("mcd_bot", budget=50, max_amount=30,
                     blacklist=["unknown_vendor"], whitelist=["McDonald's"],
                     rate_limit={"window_s": 60, "max_calls": 3})

@guard.protect("order", agent="mcd_bot")
def place_order(amount, to):
    return call_real_api(amount, to)
```

### Secret vault

```bash
python -c "from spendshield import KeyVault; print(KeyVault.generate_key())"
export SPENDGUARD_MASTER_KEY=***   # never commit this
```

```python
vault = KeyVault("vault.json")
vault.store("mcd_sk", "sk_live_xxx")

guard = SpendShield(key_vault=vault)
guard.register_agent("mcd_bot", whitelist=["mcd_sk"])
sk = guard.get_secret("mcd_sk", agent="mcd_bot")   # passes identity + intent gates
```

## 🤖 MCP Server

Claude Code, OpenClaw and any MCP-compatible agent can call the guard directly:

```bash
spendshield-mcp --policy spendshield.yaml
```

Tools: `spend_protect` / `spend_status` / `spend_audit` / `spend_reset` / `secret_get`

## ⚡ x402 / Agentic Payments 适配

x402 is the open payment protocol for the internet (HTTP 402) — how AI agents pay for APIs. SpendShield is the guardrail in front of it: **x402 lets agents pay, SpendShield stops them paying recklessly.**

```python
from spendshield import SpendShield
from spendshield.adapters.x402 import X402PaywallGuard, protect_x402_payment

guard = SpendShield(budget=50, dry_run=True)
pw = X402PaywallGuard(guard)

# Server side: every paid resource passes the gates before settlement
pw.authorize_resource("weather-api", price="0.01", asset="USDC", pay_to="0x...")
pw.confirm_payment("weather-api", price="0.01", pay_to="0x...")   # after settlement

# Client side: gate the payment before your agent pays
protect_x402_payment(guard, amount=0.01, to="weather.example.com", agent="research_bot")
```

Budget, blacklist, rate limits, human approval, identity (KYA) and audit all apply to x402 payments — new recipients require human sign-off, unregistered agents are denied.

## 🧪 Tests

30 tests covering gates, identity, intent alignment, vault, and edge cases.

```bash
python3 -m pytest tests/
```

## 📝 Feedback & Contributing

- 🐛 Found a bug? Open an issue
- 💡 Have an idea? Suggest a feature
- 🔒 Security vulnerability? See SECURITY.md — report privately, not in a public issue.
- ⭐ Found it useful? Star the repo so other people who got burned by "test orders" find it.

## 📄 License

MIT — take it. May no one get burned by a "test order" twice in the AI era.

# ciromattia/kcc

## 导航

- 项目页：[[10-项目/github.com_d771ddc7]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
