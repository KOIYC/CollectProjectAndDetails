---
type: "corpus"
item_id: "5d99e641848349e5"
title: "Show HN: Claudette - Mistral models in Claude Code"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50508283"
project_url: "https://github.com/raed667/claudette"
author: "Raed667"
published_at: "2026-11-15T16:38:41Z"
captured_at: "2026-11-16T10:00:05+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-16"
pub_day: "2026-11-15"
tags:
  - 语料
  - hn_show
  - author_Raed667
  - story_50508283
  - show_hn
metrics: {"points": 3, "comments": 1, "engagement_velocity": 3}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Claudette - Mistral models in Claude Code

> [!info] 一句话导读
> Claude Code + Mistral = 🧡

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50508283>
> 指标：点赞=3 · 评论=1 · engagement_velocity=3
> 作者：Raed667　|　发布：2026-11-15T16:38:41Z
> 项目链接：<https://github.com/raed667/claudette>
> 采集：2026-11-16T10:00:05+08:00　|　id：`5d99e641848349e5`

## 正文

# raed667/claudette

Claude Code + Mistral = 🧡

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-11-15T13:27:25Z

## Languages

- Python
- Shell

## Topics

- claude
- claude-ai
- claude-code
- mistral
- mistral-ai
- mistral-api
- mistral-large
- mistralai

## Top Contributors

- raed667 (2 contributions)

---

## README

# claudette

Run Claude Code with Mistral models.

`claudette` is a drop-in wrapper around `claude`. It starts a small local proxy
that translates Claude Code's requests for Mistral's API, then runs `claude`
against it. It keeps its own config directory, so your regular Claude Code
setup, login and history are left alone.

Anthropic doesn't support running Claude Code on non-Claude models, so treat
this as best-effort. The limitations are listed below.

## Requirements

- Claude Code
- uv
- A Mistral API key from console.mistral.ai

Tested on macOS. Linux should work but hasn't been tested, and Windows isn't
supported.

## Install

```sh
curl -fsSL https://raw.githubusercontent.com/raed667/claudette/main/install.sh | bash
```

The installer asks for your Mistral API key and stores it in
`~/.config/claudette/mistral_api_key`. If you skip the prompt, run the command
again later or export `MISTRAL_API_KEY` instead.

To update, run `claudette update` or the same install command.

## Usage

`claudette` takes the same flags and subcommands as `claude`:

```sh
claudette
claudette -p "explain this repo"
claudette --continue
```

The proxy starts on first use and keeps running in the background. Use
`claudette proxy stop` to shut it down, or `claudette proxy logs` when
requests fail.

The status line shows the model, how much of the context is used before
Claude Code compacts, an estimated cost at Mistral's prices, and the current
folder and branch:

```
mistral-large | ctx 42k/256k 16% | ~$0.96 | claudette (main)
```

The cost is the session's spend so far at Mistral's list prices, cached input
included. It doesn't count web searches or the extra requests auto mode makes
to check tool calls. A trailing `+` means part of the
session used a model without a known price. Mistral doesn't publish one for
Medium, so a Medium-only session shows no cost.

If you've set your own `statusLine` in `~/.claudette/settings.json`, yours is
used instead.

## Models

The main model is `mistral-large-latest`, and background tasks use
`mistral-small-latest`. Any chat model your key can use works.
`claudette models` lists them with their context sizes:

```sh
claudette models
CLAUDETTE_MODEL=ministral-14b-latest claudette
```

The list is cached for a day; `claudette models --refresh` fetches it again.

Large, Medium and Small are the ones that have been tested. Codestral and
`mistral-code-latest` are listed but don't call tools, which Claude Code
depends on.

Inside a session, `/model` lists Large, Medium and Small, plus your
`CLAUDETTE_MODEL` if it's something else, and `/model ` takes any other
model. Compaction is tuned to the model you start with, so prefer
`CLAUDETTE_MODEL` when switching to a model with a smaller context window. If
you've set your own `modelPicker` in `~/.claudette/settings.json`, yours is
used instead.

## Configuration

| Variable | Default | |
|---|---|---|
| `MISTRAL_API_KEY` | | Overrides the key file |
| `CLAUDETTE_MODEL` | `mistral-large-latest` | Main model |
| `CLAUDETTE_FAST_MODEL` | `mistral-small-latest` | Background tasks |
| `CLAUDETTE_COMPACT_WINDOW` | model's context, up to `256000` | Tokens before Claude Code compacts the conversation |
| `CLAUDETTE_PORT` | `4791` | Local proxy port |
| `CLAUDETTE_STATUSLINE` | `1` | Set to `0` to turn off the default status line |

## Limitations

- Web search goes through Mistral's own search instead of Anthropic's. You get
 a summarised answer with source links rather than raw results, and searches
 are billed by Mistral.
- Extended thinking, prompt caching, Remote Control, voice mode and fast mode
 aren't available.
- Your global `~/.claude/CLAUDE.md` is still loaded, which means its contents
 are sent to Mistral.

## Contributing

How it works, testing and known quirks are in CONTRIBUTING.md.

## Disclaimer

claudette is a hobby project. I wanted Claude Code's workflow with Mistral's
models, so I built it for myself and published it in case someone else wants
the same thing. I'm not affiliated with Anthropic or Mistral AI, and neither
company endorses or supports it.

Claude, Claude Code and Mistral are trademarks of their owners. claudette
doesn't include or modify Claude Code; it launches your own install against
Mistral's public API with your own key, so both companies' terms still apply
to how you use them.

## License

MIT

## 评论（1/1）

> **enjoyyourlife** · 2026-11-15T17:00:47.000Z　
> Already have https://github.com/mkornreich/llm-desktop-electron for this

## 关联链接

- https://raw.githubusercontent.com/raed667/claudette/main/install.sh

## 导航

- 项目页：[[10-项目/github.com_46c90c28]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
