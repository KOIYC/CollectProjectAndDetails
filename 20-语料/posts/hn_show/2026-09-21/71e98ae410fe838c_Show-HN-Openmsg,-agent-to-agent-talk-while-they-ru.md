---
type: "corpus"
item_id: "71e98ae410fe838c"
title: "Show HN: Openmsg, agent-to-agent talk while they run, Claude<>Codex<>OpenCode"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49779581"
project_url: "https://github.com/marciob/openmsg"
author: "marciob"
published_at: "2026-09-20T20:10:39Z"
captured_at: "2026-09-21T09:44:03+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-09-20"
tags:
  - 语料
  - hn_show
  - author_marciob
  - story_49779581
  - show_hn
metrics: {"points": 2, "comments": 2, "engagement_velocity": 2}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Openmsg, agent-to-agent talk while they run, Claude<>Codex<>OpenCode

> [!info] 一句话导读
> Messages between AI coding agents of different vendors. A Claude Code session and a Codex session talk to each other while both are running.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49779581>
> 指标：点赞=2 · 评论=2 · engagement_velocity=2
> 作者：marciob　|　发布：2026-09-20T20:10:39Z
> 项目链接：<https://github.com/marciob/openmsg>
> 采集：2026-09-21T09:44:03+08:00　|　id：`71e98ae410fe838c`

## 正文

# marciob/openmsg

Messages between AI coding agents of different vendors. A Claude Code session and a Codex session talk to each other while both are running.

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-09-20T01:12:48Z

## Languages

- JavaScript

## Topics

- a2a
- agent-communication
- ai-agents
- claude-code
- cli
- codex
- interoperability
- opencode

## Top Contributors

- marciob (31 contributions)

---

## README

# openmsg

Messages between AI coding agents of different vendors, on one machine or
between two people.

A Claude Code session can send a message to a Codex session. An OpenCode session
can answer a Claude Code session. The message goes into the session that already
runs, with its context, and not into a new process.

Two people who work on one project can do the same across their machines. Those
messages are sealed end to end, and the server that carries them cannot read
one.

Status: version 0.2 is on npm. Version 0.1, between the agents of one
person, works and is tested with live sessions. Version 0.2, between two
people, passes the fourteen acceptance cases of its specification, and the
live tests on one machine. No team has run it across the internet yet.

## How it works

Each vendor has its own way to accept a message while it runs. openmsg uses that
native way, and gives all of them one command:

```
openmsg list                  # the agents that run now, all vendors
openmsg send <agent> "<text>" # deliver a message now
openmsg inbox                 # the messages for this agent
openmsg whoami                # how other agents address this one
```

An address is `: `, for example `claude:api-worker`.

| Vendor | How openmsg delivers the message | State |
|---|---|---|
| Claude Code | The inbox socket of the session | Works, tested live |
| Codex | `codex queue` on the shared app-server daemon | Works, tested live |
| OpenCode | `POST /session/{id}/prompt_async` on its local server | Delivery tested live. A reply needs a model account |
| Cursor CLI | A hook reads the mailbox at the end of each turn | Written, tested with fixtures. A live test needs `CURSOR_API_KEY` |
| Gemini CLI | The same hook, as an AfterAgent deny | Written, tested with fixtures. Gemini CLI is not installed here |
| Other agents | `tmux send-keys` | Not started |

A reply is a new message. The receiving agent answers with `openmsg send`. No
program reads the screen of another program.

## The agents of another person

Version 0.2 adds one more step: an address with an owner, such as
`claude:api-worker@alice`.

```
openmsg id create --label alice       # a signing key and a sealing key
openmsg invite create --project web   # a token for the other person
openmsg invite accept <token> --fingerprint "A1B2 ..."
openmsg publish claude:api-worker     # let the project reach this session
openmsg gateway start --relay <url>   # the one process that the network reaches
openmsg send claude:reviewer@bob "the migration drops a column"
```

What holds:

- **Nothing is published by default.** A session is reachable after
 `openmsg publish`, and only in the project that the owner names.
- **A new sender waits.** The first message of a person stays outside the
 model until the owner runs `openmsg accept`. Membership of a project is not
 permission to write into a session.
- **Every message is sealed end to end.** The relay carries bytes that it
 cannot read. It learns who writes to whom, when, and in which project,
 because it needs that to route. The product does not pretend otherwise.
 The relay speaks TLS, and it refuses to listen on any address but this
 machine without a certificate.
- **A signature proves the person, and a fingerprint proves the key.** Two
 people compare a fingerprint out of band before the first message.
- **Each machine holds its own key.** The owner key stays on one machine and
 signs a delegation for the others. One stolen machine costs one delegation,
 and the identity of that person holds. Several machines of one person work
 at the same time, and a message is sealed for the machine that holds the
 session.
- **A message never carries authority.** The receiving agent works inside the
 permissions that its own user already gave it.

The states of a message are `queued`, `held`, `adapter-accepted`,
`agent-acknowledged`, `replied`, `refused`, and `expired`. A write to a socket
is not a read by a model: only an event from the agent gives
`agent-acknowledged`.

## Message format

The envelope uses the field names of the A2A standard (`messageId`, `contextId`,
`parts`, `role`). The same message can travel over A2A on HTTP later, between
two machines.

Each delivered message carries a header that names the sender. The text tells
the receiving model that the message is from another agent, and that it approves
nothing. Each message keeps a list of the agents that it passed through, so a
loop between two agents stops.

## Install

```
npx openmsg list
```

Or from the source:

```
git clone https://github.com/marciob/openmsg.git && cd openmsg
node src/cli.mjs list
```

Node 22 or later. No dependencies, and none for the relay either: the
WebSocket of `src/wsframe.mjs` is both sides of RFC 6455 in one small file.

Run the tests with `node --test`. Seventy-eight of them, and they need no
account: they run two gateways and a relay on this machine, as two people.

An agent with no push entry point needs its hook:

```
openmsg install --hooks
```

## How each vendor lets a message in

`research/2026-09-19-transport-research.md`
is the work that produced this design. It tests every way one program can put a message into a running
agent: typing into the terminal of another program, the native entry point of
each vendor, subprocess calls, mailboxes, A2A, and ACP. Each claim carries a
label: `[local]` for a fact that a test on one Mac verified, `[docs]` for a
fact from the vendor, and `[not verified]` for a fact from a source without a
test.

The short answer: typing into a terminal is possible and bad, and each of the
four main agents has an official way to take a message while it runs.

## Spec

- `spec/openmsg-0.1.md`:
 the protocol for the agents of one person on one machine.
- `spec/openmsg-0.2-draft.md`:
 the agents of different people on one project. The identity of an owner,
 the sealed envelope, the gateway, the relay, the seven states of a message,
 and the trust rules. Every rule of 0.1 still holds.

The code implements both, and the fourteen acceptance cases of section 11 of
0.2 pass as tests.

## License

MIT

# emetgate/emetgate

## 评论（2/2）

> **GMShuaib** · 2026-09-20T20:14:40.000Z　
> I am actually interested in it, how to use the repo? can you tell details? and, will the agents talk to each other for task completion?

---

> **marciob** · 2026-09-20T20:24:54.000Z　
> you can install with `npx openmsg install`, additional commands are in the repoyes you can ask another agent to complete some task and it may do it.

## 关联链接

- https://github.com/marciob/openmsg.git

## 导航

- 项目页：[[10-项目/github.com_df407510]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
