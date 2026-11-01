---
type: "corpus"
item_id: "ecd1bdf5cf6568c5"
title: "Show HN: Run Claude Code inside OpenCode through the official CLI"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50318664"
project_url: "https://github.com/khalilgharbaoui/opencode-claude-code-plugin"
author: "kaygeee"
published_at: "2026-10-31T18:32:12Z"
captured_at: "2026-11-01T09:38:09+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-01"
pub_day: "2026-10-31"
tags:
  - 语料
  - hn_show
  - author_kaygeee
  - story_50318664
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Run Claude Code inside OpenCode through the official CLI

> [!info] 一句话导读
> khalilgharbaoui/opencode-claude-code-plugin

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50318664>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：kaygeee　|　发布：2026-10-31T18:32:12Z
> 项目链接：<https://github.com/khalilgharbaoui/opencode-claude-code-plugin>
> 采集：2026-11-01T09:38:09+08:00　|　id：`ecd1bdf5cf6568c5`

## 正文

# khalilgharbaoui/opencode-claude-code-plugin

Use claude code in opencode officially

- Stars: 103
- Forks: 28
- Watchers: 103
- Open issues: 0
- License: MIT License
- Homepage: https://opencode-claude-code-plugin.dev
- Default branch: master
- Created: 2026-03-31T09:23:25Z

## Languages

- Astro
- CSS
- JavaScript
- MDX
- TypeScript

## Topics

- ai-sdk
- anthropic
- claude
- claude-code
- llm-provider
- opencode
- opencode-claude-code-plugin
- opencode-plugin
- plugin
- provider
- typescript

## Top Contributors

- khalilgharbaoui (715 contributions)
- broskees (17 contributions)
- Aptul9 (6 contributions)
- unixfox (5 contributions)
- jknlsn (4 contributions)
- internetisalie (2 contributions)
- PyGuy2 (2 contributions)
- galvani (2 contributions)
- nic-lan (2 contributions)
- bangnh1 (2 contributions)

---

## README

# @khalilgharbaoui/opencode-claude-code-plugin

npm version
npm downloads per month
npm downloads total
GitHub stars
GitHub forks
Contributors
Tests
Models
Publish
License
Buy me a coffee

**Claude Code is the provider.** This opencode plugin runs Anthropic's Claude models through the official **Claude Code CLI** (`claude`) as a subprocess instead of calling the HTTP API. opencode inherits whatever that CLI is logged in as (a Claude subscription, an API key, Bedrock or Vertex), gets Claude's own tools, MCP servers and skills, and keeps running the tools that touch your machine itself, behind its own permission prompts. One package serves opencode 1.x and 2.x.

- **Your CLI's login, untouched.** The plugin never reads, stores or replays a token. Lifting the OAuth session out of the official client is what proxy-style plugins do, and Anthropic disallowed that for third-party Claude use in February 2026. This plugin structurally cannot do it.
- **opencode runs the tools.** `Bash`, `Edit`, `Write`, `WebFetch` and `Task` are proxied by default: Claude calls an in-process MCP tool and opencode executes it, under its own permissions and audit log.
- **Billed as your CLI bills.** Headless `claude --print` on a subscription draws from the plan's ordinary usage limits; an API key bills pay as you go. The CLI's `apiKeySource` says which, every session, and the plugin warns when a stray `ANTHROPIC_API_KEY` would move the bill.

**Docs:** (the same pages are the markdown under `docs/`, which GitHub renders on its own).

## Quickstart

1. **Install and log in the Claude Code CLI.** The plugin drives an existing `claude`; it does not bundle one.

   ```bash
   claude --version      # e.g. 2.1.284 (Claude Code)
   claude auth status    # which account you are signed in as
   claude auth login     # only if you are not signed in yet
   ```

2. **Add the package to opencode's global config.** That spec is the whole install. Do not `npm install` it yourself: opencode resolves and caches plugin packages on its own.

   ```json
   {
     "plugin": ["@khalilgharbaoui/opencode-claude-code-plugin"]
   }
   ```

 `~/.config/opencode/opencode.json` on opencode 1.x. opencode 2 reads the same key; its native spelling is `plugins`.

3. **Quit opencode fully and relaunch.** Plugins load once, at process start. The model picker now has a **Claude Code (Default)** provider with entries such as `Claude Sonnet 5.5 (2×)` and `Claude Opus 5 (5×)`; the suffix is each model's list price relative to Haiku.

Nothing in the picker? Troubleshooting is keyed on the first thing you see. `/claude-code-doctor` in any session prints what the plugin thinks is happening, without calling a model.

## What you get

| | |
|---|---|
| **Selective tool proxy** | Choose, per tool, whether Claude Code or opencode executes it. Proxied calls end on an event (the result, an abort, the next message, the child exiting), never on a clock. Guide |
| **Claude's own tools, MCP and skills** | `Read`, `Grep`, `Glob`, `WebSearch` run in Claude Code; your opencode MCP servers are bridged in; your opencode skills can be staged for Claude's `Skill` tool. MCP · Skills |
| **Several accounts** | `"accounts": ["personal", "work"]` becomes one provider per account. Out of usage mid-task? One line says which account, which window and when it resets in your own time zone, and names the others to pick a model from. Accounts |
| **Subagents: your account, their model** | `forceModel`, `reasoningEffort` and `cacheTtl` in an agent file, inheriting the caller's account. `task_batch` runs several subagents at once. Subagents |
| **The whole model range, reasoning variants, fast mode** | Haiku 4.5 through Opus 5.5, Fable and Mythos, each with a `(N×)` list-price suffix, `low` to `max` effort variants, and a fallback chain for a model this account cannot run today. The badge above counts them. Models |
| **`/btw` and `/claude-code-doctor`** | Side questions on the live process, and a health report whose `bundle` form is redacted by allowlist so it is safe to paste into a public issue. `/btw` · Doctor |
| **Ships its own setup skill** | Ask Claude to configure it. The bundled `claude-code-plugin` skill knows every option, env var, model id and troubleshooting rule, is staged into Claude Code on every spawn, and tests keep it in step with the code. Skills |
| **Read-only preset, plan mode** | `"permissionPreset": "read-only"` holds at the CLI, the proxy and the permission layer at once. Permissions |

## How this compares

| | opencode's native `anthropic` provider | This plugin | Proxy and token-reuse plugins |
|---|---|---|---|
| **Authentication** | A Platform API key in opencode's auth store. | Whatever the official `claude` CLI holds. No token is read, stored or replayed. | The Claude OAuth session, used outside the official client. |
| **Terms-of-service status** | The ordinary API route. | Sanctioned: the official client does the authenticating. | Disallowed. Anthropic disallowed reusing subscription authentication for third-party Claude use in February 2026, and each of those projects carries its own disclaimer. |
| **Who runs Bash, Edit, Write** | opencode. | opencode, by default; `Read`, `Grep`, `Glob` run in Claude Code. | opencode. |
| **What it costs you** | Baseline. | A `claude` child per conversation under a cap of 16; Claude Code may compact its own context behind opencode's back. | One more moving part, plus the account risk above. |

The full comparison has nine rows, names the projects in the third column, and quotes their own READMEs.

## Built from measurements

A dozen test files drive a fake `claude` through real turns: the stream parser, the proxy broker, both watchdogs, abort, respawn, account failover and the model fallback chain are exercised end to end. Every rule in `AGENTS.md` names the probe, the version and the number that produced it, and the evidence lives in `docs/agents-history.md`. Two runtime dependencies. The site reports the live numbers: it rebuilds itself after every release, on every push that moves a figure, and every six hours.

## Documentation

- **Start here:** Introduction · Getting started · opencode 2 · Models · Billing
- **Configuration:** Options · Environment variables · Accounts · Subagents · Permissions · MCP · Skills · Logging
- **Guides:** Tool proxy · Background subagents · `/btw` · `/claude-code-doctor` · Per-turn stats · Compaction and thinking · Interactive transport · Other plugins
- **Troubleshooting:** Start from the symptom · Longer cases · Which login bills what · Known limitations
- **Internals:** How a turn works · How a proxied call ends · Scratch files and security · Measurement culture · Testing · Development · Releasing

### Where the old README sections went

This README used to hold all of the above. Release notes and bookmarks point at its anchors, so:

| Old README anchor | Now at |
|---|---|
| `#configuration`, `#options-reference` | docs/configuration/options.md |
| `#environment-variables` | docs/configuration/environment.md |
| `#models`, `#fast-mode` | docs/models.md |
| `#multiple-claude-code-accounts`, `#account-failover` | docs/configuration/accounts.md |
| `#billing` | docs/billing.md |
| `#troubleshooting` | docs/troubleshooting/symptoms.md |
| `#plugin-health-with-claude-code-doctor` | docs/guides/doctor.md |
| `#selective-tool-proxy` | docs/guides/tool-proxy.md |
| `#credits` | docs/credits.md |

## Credits

Made and maintained by Khalil Gharbaoui (@khalilgharbaoui). This plugin absorbs work from its forks directly, cherry-picked with the original authorship preserved or reimplemented with the author named in the commit. The people behind the features you are using, and what each built, are on the Credits page; `git log --author` on this repo shows the preserved authorship.

## Support

This plugin is maintained, not a side project that gets abandoned when the next Claude Code or opencode release breaks something. Keeping it working means tracking CLI flag changes, opencode plugin API changes, and new model IDs as they ship.

If the plugin saves you time, you can keep it maintained here:

One-off or recurring, both help. Bug reports and PRs are welcome too; see `AGENTS.md` for the contribution rules.

## License

MIT. See LICENSE. The first version was written by Émilien (@unixfox); everything since by Khalil Gharbaoui and the people in Credits.

# interviewLint — Think Beyond Code.

## 关联链接

- https://opencode-claude-code-plugin.dev

## 导航

- 项目页：[[10-项目/github.com_63f0ca7c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
