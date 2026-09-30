---
type: "corpus"
item_id: "45534d6918c3fb53"
title: "Show HN: OpenDots – model agnostic alternative to OpenAI's Dots"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49897591"
project_url: "https://github.com/diggerhq/opendots"
author: "iacguy"
published_at: "2026-09-29T17:58:22Z"
captured_at: "2026-09-30T18:57:07+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-30"
pub_day: "2026-09-29"
tags:
  - 语料
  - hn_show
  - author_iacguy
  - story_49897591
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: OpenDots – model agnostic alternative to OpenAI's Dots

> [!info] 一句话导读
> An always-on personal agent you own, on the model you choose. A model-agnostic alternative to OpenAI's Dots, built on OpenComputer Serverless Agents.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49897591>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：iacguy　|　发布：2026-09-29T17:58:22Z
> 项目链接：<https://github.com/diggerhq/opendots>
> 采集：2026-09-30T18:57:07+08:00　|　id：`45534d6918c3fb53`

## 正文

# diggerhq/opendots

An always-on personal agent you own, on the model you choose. A model-agnostic alternative to OpenAI's Dots, built on OpenComputer Serverless Agents.

- Stars: 6
- Forks: 3
- Watchers: 6
- Open issues: 0
- License: MIT License
- Homepage: opencomputer.dev
- Default branch: main
- Created: 2026-09-29T17:35:28Z

## Languages

- CSS
- Dockerfile
- JavaScript
- TypeScript

## Topics

- agents
- dots-alternative
- model-agnostic
- opencomputer
- personal-assistant

## Top Contributors

- ZIJ (5 contributions)
- UtpalJayNadiger (3 contributions)

---

## README

# OpenDots

**An always-on personal agent you own, on the model you choose.**

A personal assistant you deploy for yourself, and a model-agnostic alternative
to OpenAI's Dots. Hand it work, keep talking,
and get the results back in the same conversation.

Longer jobs get a **topic**: its own conversation, notes you can read and
edit, and a cloud computer when needed. Work continues when you close the
browser.

A TanStack Start web app and two agents defined with React-style TypeScript
hooks. OpenComputer Serverless Agents
runs the agents, provisions their computers and stores their conversations
and notes in your own
OpenComputer project. No separate agent infrastructure to operate.

A request for Greece island-hopping options is delegated to a topic; the completed research returns to the main conversation, beside the owner's saved preferences.

## Try a task

Setup includes a **Workshop demo** topic linked to a
sample application's quickstart.
Ask in the main conversation:

> In Workshop demo, run the quickstart from a clean checkout. Fix anything
> that fails, rerun it, and save the verified commands in the topic notes.

Open the topic to watch the commands and inspect its notes. You can ask for
something else while it runs; the worker's result comes back to the main
conversation. Then follow up:

> The workshop attendees use Node 20. Check that too.

The worker continues the same topic. You can also correct its notes directly
before the next task. Those notes survive replacing the topic's computer
and are readable through the OpenComputer API and CLI independently of this app.

## Run locally

You need **Node.js 22**, an OpenComputer account and an HTTPS tunnel to your
machine. The app runs locally; the agents run on OpenComputer.

```sh
git clone https://github.com/diggerhq/opendots.git
cd opendots
npm ci
npx opencomputer login
```

Start a tunnel to port 3100 and leave it running. For example:

```sh
ngrok http 3100
```

In another terminal in the repository, replace `https://YOUR-TUNNEL-HOST`
with the HTTPS URL the tunnel printed:

```sh
npm run setup -- --origin https://YOUR-TUNNEL-HOST
npm run dev
```

Setup links or creates the OpenComputer project, generates the login and
application secrets in `.env.local`, deploys both agents to Development,
and seeds the example notes. The public URL lets the coordinator call the
app's delegation tool.

Open that HTTPS URL and sign in with `OPENDOTS_OWNER_SECRET` from
`.env.local`. Keep both terminals running. If the tunnel URL changes, rerun
setup with the new origin, restart the app, sign in again and replace the
coordinator from the owner menu so its callback uses the new origin.

## Deploy

Deploy to Cloudflare
Deploy to Render

Follow the host guide for secrets and agent setup:
Cloudflare Workers ·
Render ·
Docker ·
Fly.io.
The guides record which paths have been tested; the Cloudflare button
requires a public repository.

Access to your app is protected by an owner login.
See configuration and owner access for storage,
origins and secret rotation; .env.example lists the settings.

## Choose your model

OpenDots is not tied to one model provider. Each agent names its model in
one line, and OpenComputer
handles provider credentials, so no API key goes into the code:

```ts
useModel("anthropic/claude-sonnet-4.6");      // default
useModel("openai/<model>");                   // through your connected Codex account
useModel("openrouter/<provider>/<model>");    // any managed OpenRouter model
```

Change the literal in
`coordinator/agent.ts` (and the
`MODEL` constant beside it, which the coordinator reports when asked) and in
`topic-worker/agent.ts`, then
run `npm run deploy:agents`. The coordinator and the workers can use
different models. OpenAI models through your own account need
BYOK on a Pro or Max plan.

## How it's built

An agent is a TypeScript function that declares what it needs and returns
its instructions. The coordinator
starts with:

```ts
useModel("anthropic/claude-sonnet-4.6");
const input = useInput();
const owner = useMemory(profile);
const overview = useMemory(topics);
useTool(startTopic);
```

It answers directly or calls
start_topic
to create or reuse a worker session. The
worker uses a computer for its
task and saves useful knowledge with `memory_save`.

Both agents read project memory through
`useMemory`: the coordinator sees the owner profile and topic summaries;
each worker sees the profile and its own topic's notes. Conversation history
belongs to the session; saved notes remain available to later sessions.

The app owns login, the session index and delegation. The browser attaches
to sessions through authenticated routes using
`useAgent`; the OpenComputer key
stays on the server. Worker outcomes return through platform event
subscriptions, with an app-side fallback
while those routes are unavailable.

## Development

Run `npm run check` for typechecking, lint, unit tests and agent validation.
Development notes cover the live Playwright suite,
local transcripts and redeploying the agents.

Early preview: the interface, agents and platform APIs are still changing.

## License

MIT

## 关联链接

- https://YOUR-TUNNEL-HOST
- https://YOUR-TUNNEL-HOST`
- https://github.com/diggerhq/opendots.git

## 导航

- 项目页：[[10-项目/github.com_17a1f6ae]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
