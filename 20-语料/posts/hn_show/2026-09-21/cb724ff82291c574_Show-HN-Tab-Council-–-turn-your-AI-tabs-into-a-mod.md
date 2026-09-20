---
type: "corpus"
item_id: "cb724ff82291c574"
title: "Show HN: Tab Council – turn your AI tabs into a model council"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48323971"
project_url: "https://github.com/vaddisrinivas/tab-council"
author: "srinivasvaddi"
published_at: "2026-05-29T15:02:25Z"
captured_at: "2026-09-21T02:53:00+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-29"
tags:
  - 语料
  - hn_show
  - author_srinivasvaddi
  - story_48323971
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:144d"
---

# Show HN: Tab Council – turn your AI tabs into a model council

> [!info] 一句话导读
> Published: 2026-05-29

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48323971>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：srinivasvaddi　|　发布：2026-05-29T15:02:25Z
> 项目链接：<https://github.com/vaddisrinivas/tab-council>
> 采集：2026-09-21T02:53:00+08:00　|　id：`cb724ff82291c574`

## 正文

Published: 2026-05-29

# Repository: vaddisrinivas/tab-council

Chrome MV3 extension that turns AI tabs into a structured model council

- Stars: 3
- Forks: 1
- Watchers: 0
- Open issues: 1
- Primary language: JavaScript
- Languages: JavaScript (80.4%), HTML (10.3%), CSS (9.3%)
- License: MIT License (MIT)
- Default branch: main
- Created: 2026-05-29T12:26:48Z
- Last push: 2026-06-24T12:00:35Z
- Contributors: 1 (top: vaddisrinivas)
- Releases: 1
- Latest release: v0.1.0-alpha (2026-05-29T12:27:01Z) [prerelease]

---

# Tab Council

Turn the AI tabs you already use into a structured model council.

Tab Council is a Chrome MV3 extension for cross-checking important prompts across ChatGPT, Claude, Gemini, Perplexity, Merlin, and Grok. Create a tab group named `tab-council`, place your provider tabs inside it, and run one prompt through an independent answer, critique, judge synthesis, and optional Ratify/Veto flow.

No API keys. No backend. Your accounts, your tabs, your local Chrome storage.

## Demo

[Watch the v0.1.0-alpha demo video](https://github.com/vaddisrinivas/tab-council/releases/download/v0.1.0-alpha/tab-council-demo.mp4)

## Why It Exists

One model answer is useful. A small council is safer.

There are already browser extensions that send one prompt to many AI tools and show the answers side by side. Tab Council is trying to do something narrower: run the full model-council workflow over the AI tabs you already have open.

It is built for launch reviews, product decisions, architecture checks, research synthesis, policy drafts, and any question where you want independent reasoning plus visible dissent before you trust the answer.

## What Makes It Different

- **Uses existing AI tabs**: no OpenRouter setup, no provider API keys, no copied model roster.
- **Starts from a Chrome tab group**: the tabs you group under `tab-council` are the council.
- **Runs council rounds, not just broadcast**: independent answers, critique, disagreement check, optional final positions, synthesis.
- **Has explicit roles**: Member, Judge, Validator, Observer, Exclude.
- **Handles structured output**: JSON parsing, one repair pass, and loud failures instead of silent bad transcripts.
- **Adds final review**: Ratify/Veto lets non-judge tabs challenge the synthesized verdict.

## v0.1.0-alpha

This alpha focuses on extension-based orchestration:

- Detects the active Chrome tab group named `tab-council`.
- Uses each grouped AI tab as an explicit model seat.
- Reads visible model labels where the provider UI exposes them.
- Lets every tab take a role: **Member**, **Judge**, **Validator**, **Observer**, or **Exclude**.
- Runs Round 1 independent answers, Round 2 polite critique, optional Round 3, synthesis, and optional Ratify/Veto.
- Requires structured JSON from every phase.
- Runs one JSON repair pass when a provider returns almost-JSON instead of valid JSON.
- Stores run state and history only in `chrome.storage.local`.
- Exports a local Markdown transcript.

## Supported Providers

- ChatGPT: `chatgpt.com`, `chat.openai.com`
- Claude: `claude.ai`
- Gemini: `gemini.google.com`
- Perplexity: `perplexity.ai`, `www.perplexity.ai`
- Merlin: `getmerlin.in`, `www.getmerlin.in`, `extension.getmerlin.in`
- Grok: `grok.com`, `x.com`, `*.x.ai`
- Local/dev generic AI pages: `localhost` and `127.0.0.1`

Unknown public web pages are not broadly enabled in the store-safe manifest. Known adapters fail visibly when a provider UI changes.

## How It Works

1. Open the AI provider tabs you want.
2. Select the model inside each provider tab, such as Claude Sonnet, a ChatGPT model, Gemini, Perplexity, or Grok.
3. Group those tabs in Chrome.
4. Name the group `tab-council`.
5. Open the Tab Council side panel.
6. Assign roles and choose a mode.
7. Enter one prompt.
8. Review the rounds, final verdict, Ratify/Veto results, and export.

## Roles

- **Member** participates in debate rounds and can be selected as judge.
- **Judge** participates as a member and is preferred for synthesis.
- **Validator** skips debate and only ratifies or vetoes the final verdict.
- **Observer** appears in the roster but is never automated.
- **Exclude** is ignored for the run.

## Council Modes

- **Quick**: faster pass using current threads.
- **Balanced**: fresh threads, critique, judge synthesis.
- **Thorough**: forces final statements before synthesis.
- **Rigorous**: forces final statements and Ratify/Veto.

Manual controls let you override the mode: force Round 3, choose judge mode, enable Ratify/Veto, include raw export, and select output views.

## Structured Output and JSON Repair

Every provider is asked to return strict JSON for each phase. That makes the side panel reliable: confidence scores, disagreements, verdicts, and vetoes can be parsed instead of scraped from prose.

JSON repair means this: if a model returns almost valid JSON, for example markdown fences, trailing comments, or malformed quote escaping, Tab Council sends that same tab a repair prompt and asks for valid JSON only. The repaired response is marked in the UI. If repair fails, the tab fails loud instead of silently corrupting the transcript.

## Privacy

Tab Council has no extension-owned server, analytics, or tracking pixels.

- Prompts are pasted into the provider tabs you selected.
- Later rounds intentionally share successful model outputs across selected provider tabs.
- Local run state lives in `chrome.storage.local`.
- Exports are generated locally by your browser.
- Clear Local removes stored extension run data.

Provider websites still receive the content sent into their own tabs. See [PRIVACY.md](./PRIVACY.md) for the exact boundary.

## Install the Alpha

Download the `v0.1.0-alpha` release zip from GitHub:

[github.com/vaddisrinivas/tab-council/releases](https://github.com/vaddisrinivas/tab-council/releases)

Then:

1. Open `chrome://extensions`.
2. Enable **Developer mode**.
3. Click **Load unpacked**.
4. Unzip the release and select the folder containing `manifest.json`.
5. Sign into your AI providers in Chrome.
6. Put those tabs in a group named `tab-council`.
7. Click the Tab Council extension icon.

## Local Development

```bash
npm install
npm run check
```

Run the deterministic fake provider harness:

```bash
npm run fake-ai
```

Open `http://localhost:4173/` in two or more tabs, put them in a `tab-council` group, grant localhost permission, and run a council. The page returns structured JSON for every phase.

## Architecture

- `manifest.json`: MV3 permissions, side panel, service worker, provider host allowlist.
- `src/background.js`: tab-group discovery, permissions, run state machine, prompt orchestration.
- `src/contentScript.js`: provider page automation adapters.
- `src/sidepanel.*`: operator UI, roles, run controls, transcript, export.
- `src/prompts.js`: structured prompt builders and Markdown export.
- `src/shared.js`: provider registry, settings, parsing, helper contracts.

Read more in [docs/ARCHITECTURE.md](./docs/ARCHITECTURE.md).

## Docs

- [Privacy](./PRIVACY.md)
- [Architecture](./docs/ARCHITECTURE.md)
- [Compatibility Matrix](./docs/COMPATIBILITY.md)
- [Contributing](./CONTRIBUTING.md)
- [Security](./SECURITY.md)
- [License](./LICENSE)

# OpenHive — Agents working together

## 关联链接

- http://localhost:4173/`
- https://github.com/vaddisrinivas/tab-council/releases
- https://github.com/vaddisrinivas/tab-council/releases/download/v0.1.0-alpha/tab-council-demo.mp4

## 导航

- 项目页：[[10-项目/github.com_8fdfa1cd]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
