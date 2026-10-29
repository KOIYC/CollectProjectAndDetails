---
type: "corpus"
item_id: "e9f6a67b7b5e1ad8"
title: "Show HN: Kavach – Replay production crashes locally without a DB or network"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50279502"
project_url: "https://github.com/kavachlabs/kavach"
author: "eulerkochy"
published_at: "2026-10-28T19:28:18Z"
captured_at: "2026-10-29T20:41:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-29"
pub_day: "2026-10-28"
tags:
  - 语料
  - hn_show
  - author_eulerkochy
  - story_50279502
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Kavach – Replay production crashes locally without a DB or network

> [!info] 一句话导读
> Replay the crash. Prove the fix. 81ns in-process flight recorder, 61µs deterministic replay, and 5.9ms variant fix verification for journal-driven services and …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50279502>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：eulerkochy　|　发布：2026-10-28T19:28:18Z
> 项目链接：<https://github.com/kavachlabs/kavach>
> 采集：2026-10-29T20:41:52+08:00　|　id：`e9f6a67b7b5e1ad8`

## 正文

# kavachlabs/kavach

Replay the crash. Prove the fix. 81ns in-process flight recorder, 61µs deterministic replay, and 5.9ms variant fix verification for journal-driven services and AI coding agents.

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 1
- License: Apache License 2.0
- Homepage: https://www.thekavachlabs.com
- Default branch: main
- Created: 2026-10-06T13:58:52Z

## Languages

- C
- C++
- CMake
- CSS
- Dockerfile
- Dune
- Elixir
- Go
- HTML
- Haskell
- Java
- JavaScript
- Julia
- OCaml
- PHP
- Python
- Ruby
- Rust
- Shell
- TypeScript

## Topics

- claude-code
- coding-agents
- debugging
- deterministic-simulation-testing
- event-sourcing
- fault-injection
- golang
- mcp
- mcp-server
- property-based-testing
- python
- replay
- rust
- testing
- typescript

## Top Contributors

- eulerkochy (272 contributions)

---

## README

ci
sdk
release
codecov

**Replay the crash. Prove the fix.**

Kavach records every input, clock read, and random read a service makes. When a step panics, returns an error, or breaks a declared invariant, it flushes a compact `.kavach` fixture that replays byte for byte in microseconds—with no broker, database, or network—and rejects narrow patches that fail across perturbed variants of the incident.

| Metric | Measured | How |
| --- | --- | --- |
| Recorder overhead per event (shared-memory ring) | **81.2 ns** | Median of 5 runs (BENCHMARKS.md) |
| Full incident replay, in-process | **61.1 µs** | 33 records, 8 steps, 2 invariants/step |
| Fix verification across 56 variants, in-process | **5.9 ms** | `kavach diff` (`196.4 ms` end-to-end across 105 binary runs) |
| Narrow single-event fixes rejected | **10 / 10** | Ten planted bugs in `bench/`, `1,000 / 1,000` byte-identical replays |

**Scope:** deterministic replay, variant fix verification, and contract-first feature verification for single-writer, journal-driven services in **12 languages** (sdk) or over two small wire protocols (INTEGRATING.md). Explore multi-arm coding agent runs on real open-source incidents at benchmark.kavachlabs.dev.

> **Status: pre-alpha.** The journal format (SPEC.md), the flight
> recorder, replay and the CLI work on the demo service. APIs and the format
> will change before 1.0. Every performance number this project publishes is in
> BENCHMARKS.md with the command that measured it.

## Install

Install prebuilt `kavach` and `kavach-recorder` binaries **plus all four Kavach agent skills** on Linux or macOS (`amd64` / `arm64`) in a single command (no Go toolchain required):

```bash
curl -fsSL https://www.thekavachlabs.com/install.sh | sh
```

Or install only the agent skills via `npx skills`, or build the CLI from source with Go 1.24+:

```bash
npx skills add kavachlabs/kavach
go install github.com/kavachlabs/kavach/cmd/kavach@latest
go install github.com/kavachlabs/kavach/cmd/kavach-recorder@latest
```

## Try it

 1080p 60fps video:
 Hero cut (dark, 0:24) ·
 Hero cut (light, 0:24) ·
 Full walkthrough (dark, 0:47) ·
 Full walkthrough (light, 0:47)

The demo is a wallet ledger that crashes when upstream sends `"amount": null`.
The commands below use its Go version; every SDK under sdk has a port
with the same bug. The CLI and the recorder are written in Go, so building them
from source needs Go; your service does not.

```bash
git clone https://github.com/kavachlabs/kavach && cd kavach
go install ./cmd/kavach ./cmd/kavach-recorder   # or use install.sh above
go build -o ledger-old ./examples/ledger/sdk
go build -tags ledgerfix -o ledger-new ./examples/ledger/sdk   # the fixed build
go build -tags ledgerpartialfix -o ledger-partial ./examples/ledger/sdk  # a fix that is too narrow

./ledger-old -in examples/ledger/testdata/events.jsonl     # crashes, writes kavach/fixtures/ledger-*.kavach
kavach inspect kavach/fixtures/ledger-*.kavach                 # what happened, record by record
kavach replay  kavach/fixtures/ledger-*.kavach --bin ./ledger-old # still_failing@32
kavach diff    kavach/fixtures/ledger-*.kavach --old ./ledger-old --new ./ledger-new      # fixed
kavach diff    kavach/fixtures/ledger-*.kavach --old ./ledger-old --new ./ledger-partial  # variant_failed(7)@23
```

The partial fix guards only deposits, the event type in the incident. It
passes the recorded crash, but `diff` also replays 56 variants of it, and the
old build crashes the same way on 47 of them; the partial fix crashes on 8,
starting with the same event as a `transfer`.

Replay runs no external services: the fixture holds every input, clock read and
random read the handler made.

The same demo reads from Kafka through franz-go.
The topic is the ledger's journal: on every start the service folds it from the
first offset. With a local broker (for example
`docker run -p 9092:9092 apache/kafka:3.9.0`):

```bash
./ledger-old -kafka localhost:9092 -seed examples/ledger/testdata/events.jsonl  # load the topic once
./ledger-old -kafka localhost:9092                                              # crashes at offset 0:7
```

The fixture's inputs carry their Kafka positions (`kafka:wallet-events @ 0:7`),
and it still replays with no broker running. Kafka is a dependency of the demo
only, not of the SDK.

## With an AI agent

`kavach mcp` is a Model Context Protocol
server with six tools (`kavach_list_incidents`, `kavach_replay`,
`kavach_time_travel`, `kavach_diff`, `kavach_contract_show`, and
`kavach_contract_check`) returning the same verdicts as the CLI as structured
JSON:

```bash
claude mcp add kavach -- kavach mcp
npx skills add kavachlabs/kavach
```

Kavach ships with four Agent Skills (installed automatically by `install.sh` or `npx skills add kavachlabs/kavach`):

| Skill | What it teaches your agent |
| --- | --- |
| `/kavach-fix` | Reproduce a `.kavach` crash fixture and generalize the fix until `kavach diff` returns `fixed` across all incident and regression variants. |
| `/kavach-implement` | Build a new feature contract-first: record baseline traffic, declare spec invariants, stop for human `kavach contract approve`, and iterate until `pass`. |
| `/kavach-setup` | Map state boundaries into `.kavach/plan/state-map.md`, then instrument a handler or build a `kavach-host` harness in any of the 12 language SDKs. |
| `/kavach-invariants` | Write a reviewable invariant blueprint to `.kavach/plan/invariants.md`, declare the invariants, and mutation-test each one in milliseconds with `kavach replay` and `kavach diff`. |

See AGENTS.md for the complete verdict loop and rules.

## Using it in a service

| Language | SDK |
| --- | --- |
| Go | sdk/go |
| Python | sdk/python |
| TypeScript / JavaScript | sdk/typescript |
| Rust | sdk/rust |
| Java | sdk/java |
| C and C++ | sdk/c |
| Julia | sdk/julia |
| Ruby | sdk/ruby |
| PHP | sdk/php |
| Elixir | sdk/elixir |
| Haskell | sdk/haskell |
| OCaml | sdk/ocaml |

Every SDK has the same shape:

- a **handler**, called once per input, that reads the clock, random bytes,
 gateways and config, and emits its effects, only through the env it is
 given;
- a **recorder** that wraps your consume loop: one step per input, with
 effects delivered after the step succeeds;
- a **host mode**: when the program is started with `kavach-host` as its last
 argument, it serves replays to the CLI instead of consuming.

A handler can also provide snapshots, so that fixtures start from recent state
instead of from the service's first event, and declare invariants that are
checked after every step, live and in replay. Each SDK's README shows the code.

No SDK for your language? An SDK is a wrapper over the recorder and host
protocols in SPEC.md §9 and §10; INTEGRATING.md
shows how to speak them directly.

## How it works

1. **Record.** Your handler reads time and randomness, and emits effects,
 through the env the SDK gives it for each input. The SDK writes
 everything to `kavach-recorder`, a child process that keeps the journal on
 disk and writes a fixture file when the handler panics, returns an error, or
 violates an invariant, even if the service dies in the step.
2. **Replay.** `kavach replay --bin ` runs your own
 build as a host process (`--bin ./ledger`, `--bin "python -m ledger"`,
 `--bin "node dist/main.js"`)
 and folds the recorded inputs through its handler, serving every clock,
 random, gateway and config read from the fixture. Outputs are captured as
 events, never executed, so replay touches no external system.
3. **Verify.** `kavach diff --old --new ` reports the first
 output where two builds diverge. A fix only counts when the original failure
 is gone, declared invariants hold, steps before the failure still produce
 the outputs production saw, and the fix also passes at least 10 **variants**
 of the incident: perturbed copies of the journal (fields of the failing
 event changed, events reordered, dropped or redelivered, the clock shifted)
 on which the old build fails exactly as it did in production. A fix that
 only handles the recorded event does not pass. See SPEC.md §6.1.
4. **Build features against a contract.** `kavach contract check` replays
 traffic recorded before a feature on the new build. Steps outside the
 feature must produce the recorded outputs. Feature steps must change, and
 every change is listed for review. Invariants written from the spec must
 hold, on the traffic and on variants of the feature steps. See
 SPEC.md §6.4.

## In CI (GitHub Actions)

Check `.kavach` fixtures into `testdata/` and run `kavachlabs/kavach` in pull requests to replay regression fixtures or verify a candidate fix across incident variants (writing a verdict table to the workflow summary):

```yaml
- uses: kavachlabs/kavach@v0.1.0
  with:
    fixtures: testdata/*.kavach
    old: ./service-base
    new: ./service-pr
```

## Not in scope

- Multi-writer or shared-state services. Kavach assumes one writer folds the
 journal into state.
- Record-and-replay of network traffic ("tapes"). Kavach re-derives state from
 inputs; it does not stub dependencies from recorded responses.

## Repository guide

| File | What it is |
| --- | --- |
| SPEC.md | Journal and fixture format, and the host and recorder protocols, v0 |
| AGENTS.md | How an AI coding agent should use Kavach |
| INTEGRATING.md | Using Kavach from a language with no SDK |
| sdk | The SDKs, one per language |
| commands | Agent commands: `/kavach-implement` |
| action.yml | Composite GitHub Action for `kavach replay` and `kavach diff` in CI |
| scripts/install.sh | Zero-dependency installer for Linux and macOS (`amd64` / `arm64`) |
| llms.txt | Index of these docs for LLM tools |
| BENCHMARKS.md | Every measured number, with its command |
| examples/ledger | The demo service: sdk with the Go SDK, protocol in Julia with no SDK |
| bench | Ten planted bugs, each with a correct and a too-narrow fix |
| CONTRIBUTING.md | How to contribute (DCO sign-off required) |

## Open source

Kavach is licensed under Apache 2.0. The core replayer, the flight
recorder, the CLI and the MCP server are Apache 2.0 and will stay that way.
Any future commercial offering will be built around them, not by moving them.

Contributions are accepted under the Developer Certificate of Origin;
there is no CLA. Telemetry, if it is ever added, will be opt-in.

## 关联链接

- https://www.thekavachlabs.com
- https://www.thekavachlabs.com/install.sh

## 导航

- 项目页：[[10-项目/github.com_722df743]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
