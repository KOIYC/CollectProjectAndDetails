---
type: "corpus"
item_id: "89059d2bc7175f24"
title: "Show HN: Run manual QA test cases in a real browser with an AI agent"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49123489"
project_url: "https://github.com/broxhq/qpilot"
author: "Muhammad-21"
published_at: "2026-07-31T14:19:43Z"
captured_at: "2026-09-21T03:11:06+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-31"
tags:
  - 语料
  - hn_show
  - author_Muhammad-21
  - story_49123489
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: Run manual QA test cases in a real browser with an AI agent

> [!info] 一句话导读
> AI agent that runs your manual test cases in a real browser

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49123489>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：Muhammad-21　|　发布：2026-07-31T14:19:43Z
> 项目链接：<https://github.com/broxhq/qpilot>
> 采集：2026-09-21T03:11:06+08:00　|　id：`89059d2bc7175f24`

## 正文

# broxhq/qpilot

AI agent that runs your manual test cases in a real browser

- Stars: 7
- Forks: 1
- Watchers: 7
- Open issues: 0
- License: MIT License
- Homepage: https://brox.sh/
- Default branch: main
- Created: 2026-06-03T07:37:55Z

## Languages

- CSS
- JavaScript
- TypeScript

## Top Contributors

- Muhammad-21 (32 contributions)
- Lord-of-world (4 contributions)

---

## README

# qpilot

**AI agent that runs your manual test cases in a real browser**

npm
GitHub stars
node
license

> If qpilot saved you time → **⭐ Star it on GitHub**. It helps more than you'd think.

---

## How it works

1. You paste a plain-text test case
2. The agent opens Chrome and executes each step
3. You watch results appear live — `pass`, `fail`, or `warn` per step
4. If it hits a captcha or OTP, it pauses and asks you directly

No code. No Selenium. No config files.

| | Manual testing | Selenium / Playwright scripts | **qpilot** |
|---|---|---|---|
| Setup | none | write + maintain a test suite | paste plain text |
| Survives UI changes | n/a (a human adapts) | breaks on selector/layout changes | reads the page like a human, via ARIA semantics |
| Who can write a test | anyone | someone who codes | anyone who can write a step-by-step description |
| OTP / captcha | human handles it | usually blocks the run | pauses and asks you, then continues |
| Result | you watched it yourself | pass/fail, no narrative | pass/fail/warn per step, with evidence |

---

## Quick start

**Requirements:** Node.js 20.12+, Google Chrome, an Anthropic API key — or any OpenAI-compatible model endpoint (Qwen, vLLM, Ollama, corporate gateway)

```bash
npx qpilot
```

That's it. On first run qpilot walks you through a quick provider setup (arrow-key menu), then every launch shows your config and a Start menu.

Browser opens automatically at `http://localhost:3847`.

---

## Models & providers

On first run qpilot asks which model to use. You can re-run setup anytime:

```bash
npx qpilot config
```

Two options:

- **Anthropic (Claude)** — enter your `sk-ant-…` key. Default model is `claude-haiku-4-5`.
 Base URL is optional — set it if you reach Claude through a corporate proxy/gateway.
- **Custom** — any **OpenAI-compatible** endpoint: Qwen, vLLM, Ollama, a corporate
 gateway, OpenRouter, or OpenAI itself. You provide a **base URL**, **API token**
 and **model id**, e.g.:

  ```
  Base URL: https://dashscope-intl.aliyuncs.com/compatible-mode/v1
  Model id: qwen2.5-72b-instruct
  ```

Your choice is saved to `~/.qpilot/config.json` (mode `600`) and reused on every run.

> The custom path speaks the OpenAI `/chat/completions` protocol with tool calling —
> so the model must support function/tool calling for the agent to drive the browser.

### API key (Anthropic shortcut)

For the Anthropic provider you can skip setup by supplying the key via env:

1. `ANTHROPIC_API_KEY` environment variable
2. `.env.local` file in the current directory

```bash
echo "ANTHROPIC_API_KEY=sk-ant-..." > .env.local
```

The key is never stored except in `~/.qpilot/config.json` when you run setup.

---

## Options

| Command | Description |
|------|-------------|
| `qpilot config` | Re-run provider setup (Anthropic or custom model) |

```bash
npx qpilot config
```

Browser visibility is a per-run choice in the UI, not a CLI flag: hit **Run** to
stay headless, or **Run with preview** to watch Chrome click through the page.

---

## Writing a test case

```
TC-001 — Login and add item to cart

## 关联链接

- http://localhost:3847`.
- https://brox.sh/
- https://dashscope-intl.aliyuncs.com/compatible-mode/v1

## 导航

- 项目页：[[10-项目/github.com_0e4dacaf]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
