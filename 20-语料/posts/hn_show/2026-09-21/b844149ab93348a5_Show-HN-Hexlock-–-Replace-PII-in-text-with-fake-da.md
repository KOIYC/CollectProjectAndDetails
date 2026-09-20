---
type: "corpus"
item_id: "b844149ab93348a5"
title: "Show HN: Hexlock – Replace PII in text with fake data that has the same format"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47963789"
project_url: "https://github.com/ttarvis/hexlock"
author: "lemaudit"
published_at: "2026-04-30T15:15:03Z"
captured_at: "2026-09-21T02:52:22+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_lemaudit
  - story_47963789
  - show_hn
metrics: {"points": 5, "comments": 0, "engagement_velocity": 5}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: Hexlock – Replace PII in text with fake data that has the same format

> [!info] 一句话导读
> PII redaction that preserves data format, tokenized values stay usable in LLM pipelines

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47963789>
> 指标：点赞=5 · 评论=0 · engagement_velocity=5
> 作者：lemaudit　|　发布：2026-04-30T15:15:03Z
> 项目链接：<https://github.com/ttarvis/hexlock>
> 采集：2026-09-21T02:52:22+08:00　|　id：`b844149ab93348a5`

## 正文

# ttarvis/hexlock

PII redaction that preserves data format, tokenized values stay usable in LLM pipelines

- Stars: 7
- Forks: 0
- Watchers: 7
- Open issues: 0
- License: Apache License 2.0
- Homepage: https://hexlock.xyz
- Default branch: master
- Created: 2026-04-28T21:37:30Z

## Languages

- C
- Makefile
- Python
- Shell

## Topics

- ai-tools
- compliance
- data
- encryption
- format-preserving-encryption
- llm
- llm-security
- llm-tools
- pii
- pii-redaction
- privacy
- python
- security
- sensitive-data
- text-processing

## Top Contributors

- ttarvis (5 contributions)

---

## README

# hexlock

`hexlock` transforms sensitive data before it reaches your LLM. Phone numbers, emails, and card numbers become realistic tokens that your prompt still understands, and can be restored after.

## What is it?

`hexlock` is a tool for preventing sensitive data from being used with LLMs.
It replaces sensitive data but preserves the format so the LLM understands it still.
Then it rehydrates the response with the original data. The sensitive data never gets
sent to the LLM.

Data types protected include email, phone, SSNs, driver's license identifiers,
passport IDs, credit card, GitHub tokens, Anthropic tokens, AWS keys, and more.
See CONFIG for more types.

## Install

```bash
pip install hexlock
```

## Usage

```python
import hexlock

# ephemeral — no key needed, deanonymize in the same session
client = hexlock.Client()
anonymized = client.anonymize(
    "You can each me at jane.smith@acme.com or 415-555-0192."
)
original = client.deanonymize(llm_response)

# persistent — save and restore across sessions
key = hexlock.generate_key()  # store this securely
client = hexlock.Client(key=key)
anonymized = client.anonymize(
    "My credit card number is 4111 1111 1111 1111"
)
blob = client.save_session()  # store this alongside your key

# later, in a new process
client = hexlock.Client(key=key, session=blob)
original = client.deanonymize(llm_response)
```

## Configuration

see CONFIG

# srijansk/agent-relay

## 关联链接

- https://hexlock.xyz

## 导航

- 项目页：[[10-项目/github.com_9d88f302]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
