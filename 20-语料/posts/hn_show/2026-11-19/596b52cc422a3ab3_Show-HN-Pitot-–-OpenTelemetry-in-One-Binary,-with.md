---
type: "corpus"
item_id: "596b52cc422a3ab3"
title: "Show HN: Pitot – OpenTelemetry in One Binary, with Parquet, DuckDB, and MCP"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50554055"
project_url: "https://github.com/labstack/pitot"
author: "matrika"
published_at: "2026-11-18T23:55:35Z"
captured_at: "2026-11-19T09:43:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-19"
pub_day: "2026-11-18"
tags:
  - 语料
  - hn_show
  - author_matrika
  - story_50554055
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Pitot – OpenTelemetry in One Binary, with Parquet, DuckDB, and MCP

> [!info] 一句话导读
> Single-binary observability platform. Ingest OTLP, store as Parquet, query with DuckDB.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50554055>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：matrika　|　发布：2026-11-18T23:55:35Z
> 项目链接：<https://github.com/labstack/pitot>
> 采集：2026-11-19T09:43:31+08:00　|　id：`596b52cc422a3ab3`

## 正文

# labstack/pitot

Single-binary observability platform. Ingest OTLP, store as Parquet, query with DuckDB.

- Stars: 137
- Forks: 2
- Watchers: 137
- Open issues: 31
- License: Apache License 2.0
- Homepage: https://pitot.dev
- Default branch: main
- Created: 2025-12-15T16:25:04Z

## Languages

- Astro
- CSS
- Dockerfile
- Go
- HTML
- JavaScript
- Just
- MDX
- Shell
- TypeScript

## Topics

- ai-agent
- apm
- duckdb
- golang
- logging
- mcp
- metrics
- monitoring
- observability
- opentelemetry
- otlp
- parquet
- self-hosted
- single-binary
- tracing

## Top Contributors

- vishr (237 contributions)
- dependabot[bot] (11 contributions)

---

## README

# Pitot

Pitot (pronounced **PEE-toh**).

**Observability your agents can operate.** Send OpenTelemetry to one binary, then investigate with
Pitot's built-in agent or connect your own over MCP.

CI
License: Apache 2.0
Go Reference

*Current Pitot interface with deterministic offline sample telemetry.*

Pitot keeps OpenTelemetry traces, logs, and metrics in one binary and one data directory, with no
external storage services to operate. Pitot is pre-release and changes without migration paths; the browser
client, built-in agent, MCP tools, dashboards, and alerts are preview capabilities
(status). Start with the
documentation or run it below.

- OTLP ingest over gRPC and HTTP, with local Parquet storage and DuckDB analytics.
- Explore and PitotQL for querying telemetry without an AI provider.
- An investigation agent that answers questions about your telemetry in plain language.
- An MCP server for external agents using the same typed query tools.
- Dashboards across traces, logs, and metrics, and alerts on service error rate, latency,
 throughput, and log volume.

## Quick start

### Docker

```sh
docker run --name pitot --restart unless-stopped -p 7520:7520 \
  -v pitot-data:/var/lib/pitot/data \
  -e PITOT_AUTH_CODE_SECRET=$(openssl rand -hex 32) \
  labstack/pitot:latest
```

Open the one-time setup URL printed by the container and create the first administrator. Pitot
displays the ingest token exactly once, unless `PITOT_INGEST_TOKEN` already set it; save it with your collector secrets. For later sign-in
without SMTP, mint a 15-minute, single-use link against the running container's control database:

```sh
docker exec pitot pitot login-link admin@example.com
```

The UI, API, MCP, and both OTLP transports share port `7520`. See
installation for image defaults and bind-mount ownership, and
first boot for setup and SMTP login.

### Native binary

Install a checksum-verified release for Linux or macOS, amd64 or arm64:

```sh
curl -fsSL https://raw.githubusercontent.com/labstack/pitot/main/scripts/install.sh | sh
export PITOT_AUTH_CODE_SECRET=$(openssl rand -hex 32)
pitot
```

Set `PITOT_VERSION` to a release tag, such as `v2026.11.0-alpha`, to pin a release, and `PITOT_PREFIX` to choose the installation
directory. Native installs bind `127.0.0.1:7520`; set `PITOT_ADDR=:7520` for remote access, then
follow the same first-boot setup.

### Send telemetry

A standard OTLP/HTTP exporter can use the saved ingest token:

```sh
export OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:7520
export OTEL_EXPORTER_OTLP_HEADERS="authorization=Bearer%20$INGEST_TOKEN"
```

For a Collector on the same private container network, the forwarding side is:

```yaml
exporters:
  otlp_http/pitot:
    endpoint: http://pitot:7520
    headers:
      Authorization: "Bearer ${env:INGEST_TOKEN}"

service:
  pipelines:
    traces:  { receivers: [otlp], exporters: [otlp_http/pitot] }
    metrics: { receivers: [otlp], exporters: [otlp_http/pitot] }
    logs:    { receivers: [otlp], exporters: [otlp_http/pitot] }
```

Use an existing `otlp` receiver, set `INGEST_TOKEN`, and replace `pitot` with the Collector's
reachable private hostname. OTLP/gRPC uses `localhost:7520` locally; see send
telemetry for TLS and HTTP/2 setup.

### Enable chat

Select `PITOT_AI_PROVIDER=anthropic` and inject `ANTHROPIC_API_KEY`, or select
`PITOT_AI_PROVIDER=openai` and inject `OPENAI_API_KEY`, then restart Pitot; the selected provider
requires its key at startup. With no provider, chat is disabled and the other features still work.
See AI settings.

### Connect an MCP client

Set `PITOT_PUBLIC_URL` to your stable, externally reachable HTTPS origin, then point a remote MCP
client at that origin's `/mcp` endpoint. The client discovers and registers through OAuth; you
authorize its scopes in the browser. Pitot serves MCP `2026-07-28` and, through the `initialize`
handshake, `2025-11-25` and `2025-06-18` over Streamable HTTP. See connect over
MCP for setup and permissions.

## How it compares

| If you use | Where Pitot differs |
| --- | --- |
| **Grafana with Loki, Tempo, and Mimir** | That stack keeps a service and a query language per signal, plus object storage underneath. Pitot keeps one process, one data directory, and one typed contract across all three signals, at the cost of the horizontal scale those components are built for. |
| **SigNoz** | Both are OTLP-native and self-hosted. SigNoz composes a collector, ClickHouse, and query services; Pitot compiles ingest, authoritative Parquet storage, indexed trace reads, DuckDB analytics, alerting, and the browser client into one binary. |
| **Jaeger** | Jaeger covers traces and expects a storage backend you run separately. Pitot ingests traces, logs, and metrics into the same store, with nothing else to deploy. |
| **Prometheus with Grafana** | Prometheus pulls metrics and is excellent at them. Pitot accepts pushed OTLP for all three signals and is built around investigating a specific incident rather than maintaining long-range metric series. |
| **Datadog**, **Honeycomb**, **Grafana Cloud** | Those are managed services: someone else runs the storage, the scaling, and the upgrades, and your telemetry leaves your network to get there. Pitot is a binary you run, on data that stays on your disk. |
| **An OpenTelemetry Collector piped into ClickHouse** | The same shape, assembled by hand: collector, database, dashboards, and the glue between them. Pitot is that assembly as one program, with an agent and an MCP server already wired to the same query contract. |

Pitot is a single node. It has no clustering, no replication, and no object tier; a deployment that
outgrows one machine's disk and CPU has outgrown Pitot.

## Architecture

One process contains ingest, storage, query, alerts, the agent, MCP, and the React client. Browser
and agent clients share a typed observability contract.

Pitot runtime architecture: OTLP ingest and commit workers publish Parquet; the browser API, agent runtime, and MCP server share queries and dashboards, with DuckDB query state, SQLite control state, anomaly detection, and webhook alerts.

Parquet holds telemetry, DuckDB query state is rebuildable, and SQLite holds transactional product
state. See how storage works for durable ingest,
indexed reads, and compaction while reads continue.

Telemetry durability and query flow: authenticated OTLP rows pass through group admission, parallel commit workers, and durable publication into immutable Parquet batches; indexed trace reads, DuckDB SQL, retention, and compaction use those batches, while service and edge rollups populate rebuildable query state.

## Configuration

Configuration is environment-only: built-in defaults followed by nonempty process environment
values, validated before data files or listeners open. Settings are read once at startup; every
change requires a restart.

| Environment variable | Default | Purpose |
| --- | --- | --- |
| `PITOT_ADDR` | `127.0.0.1:7520` | UI, API, MCP, and both OTLP transports |
| `PITOT_DATA_DIR` | `./data` | Parquet, query state, and control SQLite |
| `PITOT_AUTH_MODE` | `local` | Login link or SMTP, or `oidc` |
| `PITOT_AUTH_CODE_SECRET` | — | Required in local mode and for OIDC break-glass links, 32+ characters |
| `PITOT_AI_PROVIDER` | — | Empty disables chat; `anthropic` or `openai` enables it |
| `ANTHROPIC_API_KEY` | — | Required for Anthropic chat |
| `OPENAI_API_KEY` | — | Required for OpenAI chat |
| `PITOT_RETENTION_DAYS` | `30` | Telemetry retention window |
| `PITOT_MCP_ENABLED` | `true` | Serve the MCP endpoint at `/mcp` |

Every secret accepts ` _FILE` instead of its value; see the settings
reference for validation and runtime secret
delivery for deployment examples.

### Advanced DuckDB sizing

Pitot sizes DuckDB automatically; measured workloads can override memory, connections, and threads
as described in DuckDB sizing.

For TLS, health checks, backups, upgrades, retention, and recovery, see the operator
runbook.

## Performance

Pitot v2026.11.0-alpha accepted **507,311 mixed OpenTelemetry items/s**
over 306.8 seconds on a Hetzner Cloud ccx33 (8 dedicated vCPUs, 32 GB RAM), with
telemetrygen on a separate ccx33. The ingest run on 6 November 2026 passed every
quality gate. See the performance methodology.
Pitot Bench reproduces the measurement on your hardware.

## Build from source

- **Go 1.27.3 and a C/C++ toolchain** on native Linux or macOS, amd64 or arm64.
 Build with `just build` or `bash scripts/with-duckdb.sh go build ./cmd/pitot`;
 the wrapper supplies DuckDB's pinned headers, static libraries, and CGO flags.
 The first build needs network access to download the checksum-verified engine.
- **Bun** — compiles the browser assets
- **Node.js 24.19.0** — runs development helpers and builds the documentation site
- **just** — task runner
- A 32-character **authentication code secret**

```sh
git clone https://github.com/labstack/pitot.git
cd pitot
just install   # browser dependencies and git hooks
just build     # browser assets, then the binary
```

Run it with the minimum configuration:

```sh
export PITOT_AUTH_CODE_SECRET=$(openssl rand -hex 32) # must be 32+ characters

./bin/pitot
```

Open and follow first-boot setup. SMTP and chat are optional; without SMTP,
run `./bin/pitot login-link admin@example.com` with the same configuration and data directory.

## Development

Run `just` to list recipes, `just check` for the full gate, `just test` for Go tests, and `just ui`
to rebuild embedded browser assets. See CONTRIBUTING.md for environment setup,
generated assets, hooks, and project layout.

## Releases

Versions are CalVer — `vYYYY.M.N[-alpha|-beta|-rc]`, numbered from 0 within each month across all
maturity suffixes. Pitot is alpha (for example, `v2026.11.0-alpha`); GA has no suffix.
Container tags omit the leading `v`, and every release moves `latest`. Tagged releases publish
identical manifests to Docker Hub (`labstack/pitot`) and GHCR (`ghcr.io/labstack/pitot`); GHCR is
canonical and also carries development images.

| Image tag | Points at |
| --- | --- |
| `labstack/pitot:latest` | the newest release, mirrored on Docker Hub |
| `labstack/pitot:2026.11.0-alpha` | that exact release, mirrored on Docker Hub |
| `ghcr.io/labstack/pitot:latest` | the newest release |
| `ghcr.io/labstack/pitot:2026.11.0-alpha` | that exact release |
| `ghcr.io/labstack/pitot:main` | the tip of `main` |
| `ghcr.io/labstack/pitot:sha- ` | one specific commit |

See docs/release.md for platforms, checksums, provenance, and verification.

## Contributing

Issues and pull requests are welcome; follow CONTRIBUTING.md and run `just check`
and `just test-race` before opening a pull request. Report security issues through
SECURITY.md.

## Scope

This repository builds Pitot without another repository; LabStack's deployment configuration,
uptime monitoring, and public demo instance are not included. The documentation site in
`site/` is included, with settings pages generated from the same `internal/config` type the
loader binds and checked by `just check`.

## License

Apache-2.0 © LabStack LLC. See NOTICE and
THIRD_PARTY_NOTICES for attribution, and
TRADEMARK for use of the Pitot name and logo.

# gabrielvfonseca/replica

## 关联链接

- http://localhost:7520
- http://pitot:7520
- https://github.com/labstack/pitot.git
- https://pitot.dev
- https://raw.githubusercontent.com/labstack/pitot/main/scripts/install.sh

## 导航

- 项目页：[[10-项目/github.com_caa0c15d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
