---
type: "corpus"
item_id: "045264eeef35528c"
title: "Show HN: Fentaris, an open-source proxy for managing multiple MCP servers"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49766312"
project_url: "https://github.com/Fentaris/fentaris"
author: "Gabry848"
published_at: "2026-09-19T13:10:04Z"
captured_at: "2026-09-20T09:55:17+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-19"
tags:
  - 语料
  - hn_show
  - author_Gabry848
  - story_49766312
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Fentaris, an open-source proxy for managing multiple MCP servers

> [!info] 一句话导读
> Fentaris is a centralized MCP proxy that unifies multiple MCP servers behind a single controlled endpoint, with stable routing, policies, identity, middleware, …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49766312>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：Gabry848　|　发布：2026-09-19T13:10:04Z
> 项目链接：<https://github.com/Fentaris/fentaris>
> 采集：2026-09-20T09:55:17+08:00　|　id：`045264eeef35528c`

## 正文

# Fentaris/fentaris

Fentaris is a centralized MCP proxy that unifies multiple MCP servers behind a single controlled endpoint, with stable routing, policies, identity, middleware, and rate limiting.

- Stars: 3
- Forks: 0
- Watchers: 3
- Open issues: 1
- License: MIT License
- Homepage: https://fentaris.mintlify.app
- Default branch: main
- Created: 2026-05-28T14:19:06Z

## Languages

- JavaScript
- Shell
- TypeScript

## Topics

- framework
- mcp
- proxy

## Top Contributors

- Gabry848 (415 contributions)
- cursoragent (32 contributions)
- github-actions[bot] (23 contributions)
- Copilot (1 contributions)

---

## README

 Table of contents

- About
- Documentation
 - Skills for Coding Agents
- Getting Started
- Use the SDK in an Existing Project
- Governance
- Local Auth
- Packages
- Development
- License

## About

 Fentaris is a centralized MCP proxy for routing multiple MCP servers through one controlled endpoint.

- **Unify** stdio, Streamable HTTP, SSE, and HTTP upstream MCP servers behind one proxy.
- **Protect** tool calls, resources, prompts, and completions with policy, identity, middleware, hooks, and rate limits.
- **Observe** every proxied operation with structured logging, lifecycle events, and per-request context.
- **Ship** generated proxy projects with the Fentaris CLI, local runtime files, and project checks.

Fentaris is designed for teams that want MCP servers to behave like production infrastructure: stable names, centralized governance, auditable calls, and predictable client-facing endpoints.

## Documentation

Visit our docs or jump to a quickstart

#### Skills for Coding Agents

 > Using Claude Code, Codex, Cursor or other AI coding agents?
 >
 > Install mcp-use skill for MCP Apps

## Getting Started

Use the CLI when you want to start a new Fentaris proxy project:

```bash
npm install -g @fentaris/cli
fentaris init my-proxy
cd my-proxy
fentaris dev
```

The generated proxy listens on `http://localhost:4000/mcp` by default. Point your MCP client to that endpoint.

## Use the SDK in an Existing Project

Install the core package in an existing project:

```bash
npm add @fentaris/core
```

Build a proxy in a few lines:

```ts
import { fentaris, stdio } from "@fentaris/core";

const app = fentaris();

app.mcp("filesystem", {
  transport: stdio({
    command: "npx",
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"],
  }),
});

await app.start();
```
→ Full documentation

Upstream tool names are still stable and namespaced by server. A filesystem tool is exposed to clients with a proxy name such as:

```txt
filesystem__list_directory
```

## Governance

Add users, groups, and policy:

```ts
import { fentaris, stdio, user } from "@fentaris/core";

const app = fentaris();

app.policy("read-only")
  .mcp("filesystem")
  .allow("list_directory");

app.group("operators")
  .users(user("alice", { email: "alice@example.com" }))
  .policy("read-only");

app.mcp("filesystem", {
  transport: stdio({
    command: "npx",
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"],
  }),
});

await app.start();
```

Block a sensitive tool:

```ts
app.mcp("filesystem").tool("write_file", (ctx, next) => {
  return ctx.subject?.hasGroup("admins")
    ? next()
    : ctx.deny("Admin required.");
});
```

Ask for approval before dangerous tools:

```ts
import { approval, policy } from "@fentaris/core";

const deploy = policy("deploy")
  .mcp("github")
  .allow("deploy_production", approval.manual({
    reason: "Production deploy requires approval",
  }));
```

Modify a tool result:

```ts
app.mcp("github").tool("search_issues", async (_ctx, next) => {
  const result = await next();
  if ("content" in result) {
    result.content.push({ type: "text", text: "Filtered by Fentaris" });
  }
  return result;
});
```

Observe every tool call:

```ts
app.on("tool:success", ({ ctx, durationMs }) => {
  ctx.log.info("tool.success", { tool: ctx.tool?.name, durationMs });
});
```

Policies can govern tool calls and MCP capabilities such as resources, prompts, and completion. Runtime routes can deny, approve, hide, log, or transform calls.

## Local Auth

Fentaris can resolve caller identity and upstream credentials from local encrypted files. Generated projects are discovered from `fentaris.json`; SDK-only projects are discovered from `package.json` when they depend on `@fentaris/core`.

```bash
export FENTARIS_AUTH_KEY="your-local-encryption-key"

fentaris secrets manifest --entrypoint src/index.ts
fentaris secrets set
fentaris secrets list
```

Credential values are not exposed to middleware, hooks, logs, or policy callbacks.

## Packages

| Package | Description |
| --- | --- |
| `@fentaris/core` | Proxy runtime, MCP server wrapper, transports, policy, auth, logging, and middleware APIs. |
| `@fentaris/cli` | Project generator and local development commands. |
| `@fentaris/approval-telegram` | Telegram approval adapter for Fentaris policies. |

## Development

Run the project for development:

```
fentaris dev
```

Run checks:

```bash
pnpm lint
pnpm typecheck
pnpm --filter @fentaris/core test
pnpm --filter @fentaris/cli test
pnpm --filter @fentaris/approval-telegram test
```

Generate docs reference:

```bash
pnpm docs:generate
```

## License

MIT, as declared by the published Fentaris packages.

# Show HN: Word42 Open Source Wordprocessor | Hacker News

## 关联链接

- http://localhost:4000/mcp`
- https://fentaris.mintlify.app

## 导航

- 项目页：[[10-项目/github.com_f78826bf]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
