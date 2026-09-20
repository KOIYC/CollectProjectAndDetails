---
type: "corpus"
item_id: "75db65a88b83b998"
title: "Show HN: OpenCode2 HUD"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49500245"
project_url: "https://github.com/ndom91/opencode-hud"
author: "ndom91"
published_at: "2026-08-30T16:42:03Z"
captured_at: "2026-09-21T03:11:29+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-30"
tags:
  - 语料
  - hn_show
  - author_ndom91
  - story_49500245
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:52d"
---

# Show HN: OpenCode2 HUD

> [!info] 一句话导读
> OpenCode2 plugin to show more detailed state below the text input

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49500245>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：ndom91　|　发布：2026-08-30T16:42:03Z
> 项目链接：<https://github.com/ndom91/opencode-hud>
> 采集：2026-09-21T03:11:29+08:00　|　id：`75db65a88b83b998`

## 正文

# ndom91/opencode-hud

OpenCode2 plugin to show more detailed state below the text input

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-08-29T12:33:06Z

## Languages

- TypeScript

## Topics

- hud
- opencode
- opencode-plugin

## Top Contributors

- ndom91 (46 contributions)

---

## README

# OpenCode HUD

npm version
npm downloads
license
OpenCode 2 plugin

OpenCode 2 plugin that displays a persistent status HUD below the text input in
the TUI. It is a native TUI plugin, not an assistant-message renderer, so it
does not add HUD content to a session transcript.

## Install

Add it to the `plugins` array in `~/.config/opencode/cli.json`, for example:

```json
{
  "plugins": [
    "@ndom91/opencode-hud"
  ]
}
```

OpenCode downloads and loads the package. Restart OpenCode after changing the configuration.

> [!WARNING]
> To show `5h` and `weekly` Codex subscription usage, the HUD plugin queries the OpenAI endpoint through
> your system's Codex authorization. This is disabled by default. See PRIVACY.md before
> enabling it with the `codexUsage` package option. This is the same mechanism as used by
> CodexBar and others.

## Status Rows

The default HUD can show the following native TUI data:

- Project path, branch, dirty state, and local change summary.
- Session context usage, including an amber `compaction likely soon` warning at
 80% usage and the active compaction state.
- Up to two running shell commands and the four most recent tool activities.
- The most recent failed tool for 15 seconds. A new user turn clears the
 failure row.
- Up to three running subagents, including elapsed time and their own context
 percentage.
- Optional Codex 5-hour and weekly usage limits.

## Configuration

The default HUD shows all available status rows. Disable individual groups with
package options in `~/.config/opencode/cli.json`:

```json
{
  "plugins": [
    {
      "package": "@ndom91/opencode-hud",
      "options": {
        "agents": false,
        "codexUsage": true,
        "compaction": false,
        "context": true,
        "git": true,
        "shell": true,
        "tools": true
      }
    }
  ]
}
```

| Option | Controls |
| --- | --- |
| `agents` | Running subagents, elapsed time, and context usage |
| `codexUsage` | Disabled by default. Set to `true` to show Codex 5-hour and weekly usage limits. |
| `compaction` | Active compaction state and the 80% context warning |
| `context` | Current session context usage |
| `git` | Branch, dirty state, and change summary |
| `shell` | Running shell commands |
| `tools` | Recent tool activity and brief tool-failure row |

## Local Development

Requirements:

- `opencode2`
- Node.js 24+

Install dependencies and validate the project:

```sh
pnpm install
pnpm format
pnpm typecheck
pnpm test
```

Start OpenCode from this repository:

```sh
opencode2 .
```

OpenCode discovers `.opencode/plugins/tui/status.tsx` automatically. Start or
open a session to see the HUD under the prompt.

> [!NOTE]
> The OpenCode 2 plugin API is beta and liable to change. Please check NOTES.md and validate
against the installed `@opencode-ai/plugin` runtime types if making changes.

## License

MIT

# yevhens-hue/claude-skills-starter-kit

## 导航

- 项目页：[[10-项目/github.com_22e2e927]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
