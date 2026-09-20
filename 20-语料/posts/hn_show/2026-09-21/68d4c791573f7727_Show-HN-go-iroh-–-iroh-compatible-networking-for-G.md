---
type: "corpus"
item_id: "68d4c791573f7727"
title: "Show HN: go-iroh – iroh compatible networking for Go"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48725005"
project_url: "https://github.com/tmc/go-iroh"
author: "traviscline"
published_at: "2026-06-29T20:47:08Z"
captured_at: "2026-09-21T03:11:03+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-06-29"
tags:
  - 语料
  - hn_show
  - author_traviscline
  - story_48725005
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: go-iroh – iroh compatible networking for Go

> [!info] 一句话导读
> iroh networking for go

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48725005>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：traviscline　|　发布：2026-06-29T20:47:08Z
> 项目链接：<https://github.com/tmc/go-iroh>
> 采集：2026-09-21T03:11:03+08:00　|　id：`68d4c791573f7727`

## 正文

# tmc/go-iroh

iroh networking for go

- Stars: 6
- Forks: 1
- Watchers: 6
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-06-02T00:33:23Z

## Languages

- Go
- Rust
- Shell

## Top Contributors

- tmc (249 contributions)

---

## README

# go-iroh

`go-iroh` is a Go implementation of the iroh connectivity layer. It provides
peer-to-peer QUIC endpoints identified by ed25519 public keys, with direct
paths, relay fallback, QUIC Retry, multipath, QAD observed addresses, and QNT
NAT traversal support.

The module is a clean-room Go port targeting wire compatibility with upstream
Rust iroh. It is not affiliated with the n0 team.

## Packages

| Package | Purpose |
|---|---|
| `key` | endpoint IDs, Ed25519 keys, signatures |
| `netaddr` | endpoint addresses, transport addresses, relay URLs |
| `dns` | pkarr TXT encoding and stdlib/DoH/DoT lookupers |
| `relay` | public relay maps and relay configuration |
| `watch` | small generic watch values |
| `iroh` | Endpoint, Conn, Router, address lookup, metrics |
| `cmd/iroh-relay` | minimal local relay server |
| `cmd/iroh-dns-server` | minimal pkarr HTTP server |

The transport internals live under `internal/`: relay protocol/client/server,
net reports, socket path management, RFC 7250 TLS, and `qng`, the quic-go fork
used for iroh/noq compatibility.

## Install

```sh
go get github.com/tmc/go-iroh
```

This module currently declares Go 1.26 in `go.mod`.

## Use

The `iroh` package is the main entry point:

```go
ep, err := iroh.Bind(ctx, iroh.WithALPNs("example/1"))
if err != nil {
	return err
}
defer ep.Shutdown(ctx)

conn, err := ep.Connect(ctx, peerAddr, "example/1")
if err != nil {
	return err
}
defer conn.CloseWithError(0, "")
```

ALPN means Application-Layer Protocol Negotiation. It is the TLS extension that
lets peers agree which application protocol a QUIC connection will carry, such
as `"example/1"` or `"n0/iroh/transfer/example/1"`. go-iroh uses ALPN values to
route incoming connections to handlers.

The API takes ALPN values as Go strings. TLS ALPN values are byte strings on the
wire; Go strings preserve arbitrary bytes, while keeping the common printable
ASCII case simple.

See iroh/example_test.go for runnable direct-loopback
Router and Endpoint examples.

## Wire Compatibility

Relay, pkarr, DoH, and DoT connections use standard WebPKI TLS. Direct
peer-to-peer QUIC uses TLS 1.3 Raw Public Keys (RFC 7250) with mutual endpoint
authentication. Go's standard `crypto/tls` does not support RFC 7250, so this
repository carries `internal/itls/tls` and drives it from `internal/qng`.

`internal/qng` is a quic-go v0.59.1 fork extended for the iroh/noq transport
surface: multipath, QAD observed-address reporting, QNT NAT traversal, and
pre-connection QUIC Retry admission. The fork-local READMEs document when those
forks can be removed.

## Validation

Run the local suite:

```sh
go test ./...
```

For a repeatable local check:

```sh
go test ./... -count=1
```

For loopback stream/datagram latency and throughput, with raw TCP and UDP
baselines:

```sh
GOMAXPROCS=4 go test ./iroh -run '^$' -bench 'Benchmark(Conn|RawTCP|RawUDP)' -benchtime=5s -count=5
```

`BenchmarkRawUDPMagicQueuedPingPong` is the closest raw UDP latency baseline for
the magic-socket path: it uses the same receive queue depth, pooled receive
buffers, caller-buffer copy, and separate write queue shape as the direct IP
transport.

Live Rust interop gates are opt-in because they require a checked-out and built
Rust iroh tree:

```sh
GO_IROH_LIVE_RUST_INTEROP=1 \
IROH_RUST_REPO=/path/to/n0-computer/iroh \
go test ./internal/compat -run 'TestLiveRust' -count=1 -v

GO_IROH_LIVE_RUST_INTEROP=1 \
IROH_RUST_REPO=/path/to/n0-computer/iroh \
go test ./iroh -run TestLiveRustTransferFetchPingDirectPath -count=1 -v
```

## Status

The normal local suite covers the public packages, qng transport extensions, and
local relay/direct behavior. The opt-in Rust gates cover live echo, Rust
`transfer` provider/upload, direct-path selection, and qlog evidence for QNT
frames when the host environment provides the required binaries and network
topology.

GOOS=js/GOARCH=wasm builds compile. Browser runtime support is limited by the
platform: the relay WebSocket client has a js-specific dial path, but direct UDP
QUIC, direct paths, and NAT traversal are not available in browser WebAssembly.

## License

go-iroh is licensed under the MIT License. See LICENSE.

The forked quic-go code under `internal/qng` retains its upstream license notice
in `internal/qng/LICENSE`.

# matt454/agent-fleet-console

## 导航

- 项目页：[[10-项目/github.com_e2162124]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
