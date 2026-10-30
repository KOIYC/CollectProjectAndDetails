---
type: "corpus"
item_id: "c540878710c2c315"
title: "Show HN: phpClaw – AI agent runtime for PHP with tools, memory and guards"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50293361"
project_url: "https://github.com/phpclaw-php/phpclaw-monorepo"
author: "akashpatel7204"
published_at: "2026-10-29T18:06:22Z"
captured_at: "2026-10-30T09:46:09+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-30"
pub_day: "2026-10-29"
tags:
  - 语料
  - hn_show
  - author_akashpatel7204
  - story_50293361
  - show_hn
metrics: {"points": 11, "comments": 4, "engagement_velocity": 11}
comments_count: 4
comments_total: 4
discovered_via: "hn:show_hn:3d"
---

# Show HN: phpClaw – AI agent runtime for PHP with tools, memory and guards

> [!info] 一句话导读
> GitHub - phpclaw-php/phpclaw-monorepo: Open-source AI agent framework for PHP. Tools, memory, security guards and a ReAct loop built in. Works with Laravel, Sym…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50293361>
> 指标：点赞=11 · 评论=4 · engagement_velocity=11
> 作者：akashpatel7204　|　发布：2026-10-29T18:06:22Z
> 项目链接：<https://github.com/phpclaw-php/phpclaw-monorepo>
> 采集：2026-10-30T09:46:09+08:00　|　id：`c540878710c2c315`

## 正文

GitHub - phpclaw-php/phpclaw-monorepo: Open-source AI agent framework for PHP. Tools, memory, security guards and a ReAct loop built in. Works with Laravel, Symfony, WordPress, Drupal, Magento, Joomla, OpenCart, PrestaShop. Any LLM provider. MIT. · GitHub

phpclaw-release-bot

release: core 0.1.5, cloud 0.1.4, mcp 0.1.4, joomla 0.1.5, wordpress …

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| .github | .github | feat(cloud): trace payloads for graph events and parent run ids (#103) | Oct 9, 2026 |
| packages | packages | release: core 0.1.5, cloud 0.1.4, mcp 0.1.4, joomla 0.1.5, wordpress … | Oct 16, 2026 |
| .editorconfig | .editorconfig | Initial commit: phpClaw 0.1.0 | Sep 23, 2026 |
| .gitattributes | .gitattributes | Initial commit: phpClaw 0.1.0 | Sep 23, 2026 |
| .gitignore | .gitignore | Initial commit: phpClaw 0.1.0 | Sep 23, 2026 |
| LICENSE | LICENSE | Initial commit: phpClaw 0.1.0 | Sep 23, 2026 |
| Makefile | Makefile | Initial commit: phpClaw 0.1.0 | Sep 23, 2026 |
| README.md | README.md | docs: README covers pipelines and multi-agent graphs (#127) | Oct 9, 2026 |
| composer.json | composer.json | Initial commit: phpClaw 0.1.0 | Sep 23, 2026 |
| View all files | | | |

# The universal AI agent engine for PHP.

Tools, memory, security, and a ReAct loop, already built. Zero framework dependencies in core. Any LLM provider.

## First agent in seconds

```
composer require phpclaw/phpclaw
export ANTHROPIC_API_KEY="sk-ant-..."
```

```
$agent = PhpClaw\Claw::builder()->build();
echo $agent->send('What can you help me with?')->text;
```

One env var, one builder, one `send()`. The builder checks `ANTHROPIC_API_KEY`, then `OPENAI_API_KEY`, `GROQ_API_KEY`, `GEMINI_API_KEY`, `MISTRAL_API_KEY`, `DEEPSEEK_API_KEY`, `OLLAMA_HOST`, in that order, and uses whichever it finds first. No YAML, no agent framework to learn, no vendor lock-in.

## Give your agent tools

An agent without tools can only talk. Register the ones your application needs and it starts doing real work:

```
use PhpClaw\Claw;
use PhpClaw\Tools\ShellTool;
use PhpClaw\Tools\HttpTool;
use PhpClaw\Tools\FileReadTool;
use PhpClaw\Tools\DatabaseQueryTool;
use PhpClaw\Tools\CodeSearchTool;

$agent = Claw::builder()
    ->tools([
        new ShellTool(allowlist: ['ls', 'df', 'tail']),
        new HttpTool(),
        new FileReadTool(),
        new DatabaseQueryTool($pdo),
        new CodeSearchTool(),
    ])
    ->build();
```

```
> Check disk usage and tail the last 20 lines of the error log
> Is api.example.com responding right now?
> Run a read-only SELECT to count today's orders
> Find every place UserService is used in this codebase

```

The agent decides which tools to call and in what order, running a ReAct loop (reason, act, observe, repeat) until it has an answer or hits the iteration cap. This works identically whether the tools touch your shell, your database, your HTTP APIs, or your codebase.

## Why phpClaw

Every "AI in PHP" tutorial ends the same way: an HTTP client bolted onto a provider API, a hand-rolled tool-call loop, and a prayer that the prompt holds up in production. A generic LLM SDK gives you the API client. phpClaw gives you the agent runtime around it: the loop, the guards, the memory, the framework wiring, already assembled.

| | phpClaw | Generic LLM SDK |
| --- | --- | --- |
| Tool-calling loop | ReAct, built in | You write it |
| Framework-native adapters | 8, idiomatic per framework | None |
| Prompt injection defence | 8 default guards + opt-in rate limiting | None |
| Memory abstraction | Swappable drivers | None |
| Streaming + tool-calls together | Hybrid mode | Varies |
| MCP server bundled | Expose any app to Claude Desktop | None |
| Chains and multi-agent graphs | `Pipeline` and `Graph`: loops, human pause and resume, fan-out | You build it |
| Zero framework deps in core | `ext-curl`, `ext-json`, `ext-mbstring`, done | Depends |
| Core license | MIT, nothing gated | Varies |

Not trying to be everything. phpClaw isn't a RAG framework: there are no embeddings or vector stores. It's built to give an LLM tools, memory and security controls against your real application, and to chain those agents into pipelines and graphs when one call isn't enough.

## What phpClaw provides

Agent runtime. A ReAct loop with a hard iteration cap (`max_iterations`, default 20), pluggable tools, pluggable memory, and skills the model loads on demand through the `load_skill` tool, all running inside a single reasoning cycle.

Pipelines and graphs. `Pipeline` chains steps (prompt template, agent, structured output, your own callables) with retry and fallback. `Graph` runs nodes that loop, branch, pause for a human, resume in another process, and fan out to branches that run inline or are drained by workers from cron, a queue or the CLI. See Pipelines and Graphs.

Provider flexibility. 7 providers auto-detected from environment variables: Anthropic, OpenAI, Groq, Gemini, Mistral, DeepSeek, Ollama. A custom OpenAI-compatible endpoint is also supported, opt-in via `PHPCLAW_PROVIDER=custom`. Switch providers with `->provider()` and `->model()`, no code changes elsewhere.

Production controls. 8 security guards on by default (prompt injection, PII, code injection, Unicode, homoglyph, role-switch, destructive SQL, message length), plus rate limiting available as an opt-in guard. Tool results are sanitised unconditionally by `ToolOutputGuard`, which sits outside the guard registry, and LLM output sanitisation is on by default and can be disabled with `->sanitiseOutput(false)`. `ShellTool` is allowlist-only with a hard-coded command blocklist that can't be overridden. `HttpTool` validates resolved IPs, not just hostnames, closing the DNS-rebinding gap a prefix blocklist alone would miss. `FileReadTool`/`FileWriteTool` are workspace-sandboxed and refuse sensitive paths and extensions.

Developer experience. Token-by-token streaming, prompt caching (cached input tokens billed at Anthropic's discounted cache-read rate, see Anthropic's pricing for the exact figure), and extended thinking (Claude's reasoning chain exposed on `$response->thinking`).

Ecosystem. 8 framework and CMS adapters, an MCP server for exposing your tools to Claude Desktop and Claude Code, and an optional cloud transport for a hosted, continuously-updated prompt-scan guard.

## Framework & CMS adapters

Each adapter wires phpClaw into its host's own idioms: Eloquent for Laravel, Doctrine for Symfony, WP-CLI for WordPress, Drush for Drupal, and so on. Every adapter ships an admin chat or CLI and the same 3-table memory schema underneath.

| Platform | Package | Install | Versions |
| --- | --- | --- | --- |
| Laravel | `phpclaw/phpclaw-laravel` | Composer | 10, 11, 12, 13 |
| Symfony | `phpclaw/phpclaw-symfony` | Composer | 6.4, 7.x, 8.x |
| Drupal | `phpclaw/phpclaw-drupal` | Composer | 10, 11 |
| Magento / Adobe Commerce | `phpclaw/phpclaw-magento` | Composer | 2.4.x |
| WordPress + WooCommerce | -- | ZIP upload | 6.2+ |
| Joomla | -- | ZIP upload | 4, 5, 6 |
| OpenCart | -- | ZIP upload | 3.x, 4.x |
| PrestaShop | -- | ZIP upload | 8.x, 9.x |

CMS adapters ship as ZIP downloads from Releases, not Composer, because that's how their host platforms install extensions.

```
php artisan phpclaw "deploy staging and notify #ops"          # Laravel
bin/console phpclaw "check all database connections"          # Symfony
drush phpclaw:run "list recently-active users"                # Drupal
bin/magento phpclaw:run "check order-queue status"             # Magento
wp phpclaw send "summarise today's posts"                     # WordPress
php cli/joomla.php phpclaw "list recent articles"              # Joomla
php cli/phpclaw.php send "check low stock products"            # OpenCart
php modules/phpclaw/cli/phpclaw.php send "check stock levels"  # PrestaShop
```

Full per-adapter reference (tools, REST routes, CLI commands, settings, memory drivers) lives on the doc site. Each adapter's own README is a short pointer, not a manual. Building a new one? See the community adapter guides.

## MCP Server

`phpclaw/phpclaw-mcp` exposes your existing `ToolRegistry` over the Model Context Protocol, so Claude Desktop, Claude Code, Cursor, or any MCP-compatible client can call your tools directly, with the default guards scanning every tool call's arguments (the prompt-only code-injection, PII and length guards apply to chat messages, not tool arguments). No changes to the tools themselves.

```
composer require phpclaw/phpclaw-mcp
```

Full quick start, transport, and security details: phpclaw.ai/docs/mcp.

## Security

Every message runs through the default guard chain before it reaches the provider. `ShellTool` runs only commands on its allowlist (default `ls`, `pwd`, `df`, `wc`, `date`, `uptime`, `hostname`, `whoami`), matched exactly and case-sensitively; a fixed, non-overridable blocklist of dangerous commands is checked first regardless of what's allowlisted. `HttpTool` blocks requests by hostname prefix, then re-validates every resolved IP address, catching CGNAT and DNS-rebinding attempts that hostname checks alone would miss. `FileReadTool` and `FileWriteTool` are sandboxed to a configured workspace root and refuse credentials, keys and security directories (`.git`, `.ssh`, `wp-admin`, ...) unconditionally, and `vendor/` and `node_modules/` by default.

Full guard reference, the exact `ShellTool` blocklist, and the SSRF/sandbox implementation details: phpclaw.ai/docs/security. Found a vulnerability? See SECURITY.md, do not open a public issue.

## Architecture

```
Message
  → Guards       (blocks injection/PII before the LLM sees it)
  → Hooks         (lifecycle events fire, 44 across the loop)
  → Agent          (ReAct loop: provider + tools + memory + skills)
  → AgentResponse  (text, tokens, tool calls, timing)

```

Providers, tools, memory, guards, and skills are all pluggable through registries; every adapter wires them from its own config or environment. Full architecture diagram and design rules: phpclaw.ai/docs/architecture.

## Extensibility

Five static registries (`GuardRegistry`, `HookRegistry`, `MemoryRegistry`, `ProviderRegistry`, `SkillRegistry`) plus the per-agent `ToolRegistry` instance. Drop a class in `packages/core/src/ /` with the matching attribute (`#[Tool]`, `#[Provider]`, `#[Memory]`, `#[Skill]`, `#[Hook]`, `#[Guard]`), run `composer dump-autoload`, it's live. Or register from code: `GuardRegistry::register()`, `HookRegistry::on()`, `$toolRegistry->register([...])`.

Full extension recipes with working code for every subsystem: phpclaw.ai/docs.

## Testing

```
for pkg in core cloud mcp; do (cd packages/$pkg && composer test); done
```

Unit tests use mocks and stubs for HTTP clients, `\Redis`, and the filesystem: no external network calls and no API keys are needed to run the suite for core, cloud, or mcp. The full testing rules, including how to test a core change through an adapter, are in the contributing guide.

## Documentation

This README gets you installed. Everything else, architecture, the full provider/tool/guard/hook/memory/skill reference, per-adapter tool and REST tables, code examples, upgrading, troubleshooting, lives at:

## Requirements

- PHP: 8.1, 8.2, 8.3, 8.4
- Extensions:`ext-curl`, `ext-json`, `ext-mbstring` (core only; adapters may need more, documented per-package)

## License

MIT, built with love for the PHP community. Part of the phpClaw project.

## About

Open-source AI agent framework for PHP. Tools, memory, security guards and a ReAct loop built in. Works with Laravel, Symfony, WordPress, Drupal, Magento, Joomla, OpenCart, PrestaShop. Any LLM provider. MIT.

## 评论（4/4）

> **akashpatel7204** · 2026-10-29T18:07:39.000Z　
> I'm the author. phpClaw is an MIT agent runtime for PHP: a ReAct tool loop, memory, input guards, and an MCP server, with no framework dependencies in core (PHP 8.1+). There are adapters for Laravel, Symfony, Drupal, and others. Happy to answer questions.

---

> **darkotic** · 2026-10-29T18:49:22.000Z　
> I've since switched to Go for most of my development, but I have a decades old fondness for PHP and seeing what people can get it to do. PHP is dead! Long live PHP!

---

> **bompus** · 2026-10-29T18:58:09.000Z　
> This is pretty cool, thanks for sharing!

---

> **gunalx** · 2026-10-29T22:55:20.000Z　
> I will say I'm a bit sceptical to the general quality and probably sloppiness of this based on the 300k loc initial commit wich sets off some warning signs for me.

## 导航

- 项目页：[[10-项目/github.com_6e7376ce]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
