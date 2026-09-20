---
type: "corpus"
item_id: "7da08fa0f069a374"
title: "Show HN: SCIP MIP solver bindings for Go, ported from russcip"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49714495"
project_url: "https://github.com/egoisutolabs/scipgo"
author: "generalist_dev"
published_at: "2026-09-15T15:56:14Z"
captured_at: "2026-09-20T09:37:11+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_generalist_dev
  - story_49714495
  - show_hn
metrics: {"points": 11, "comments": 0, "engagement_velocity": 11}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: SCIP MIP solver bindings for Go, ported from russcip

> [!info] 一句话导读
> Go Bindings for SCIP

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49714495>
> 指标：点赞=11 · 评论=0 · engagement_velocity=11
> 作者：generalist_dev　|　发布：2026-09-15T15:56:14Z
> 项目链接：<https://github.com/egoisutolabs/scipgo>
> 采集：2026-09-20T09:37:11+08:00　|　id：`7da08fa0f069a374`

## 正文

# egoisutolabs/scipgo

Go Bindings for SCIP

- Stars: 8
- Forks: 0
- Watchers: 8
- Open issues: 7
- License: MIT License
- Homepage: https://pkg.go.dev/github.com/egoisutolabs/scipgo/scip
- Default branch: main
- Created: 2026-09-03T07:44:37Z

## Languages

- C
- Go
- Linear Programming
- Mathematical Programming System

## Topics

- golang
- mixed-integer-programming
- optimization

## Top Contributors

- gendev1 (59 contributions)

---

## README

# scipgo

Go Reference
CI
Go Report Card
License: MIT

Go bindings for SCIP, one of the fastest
non-commercial solvers for mixed integer programming (MIP) and mixed
integer nonlinear programming (MINLP). scipgo is a port of the Rust crate
russcip and follows its API closely,
so the two are easy to move between.

```go
model := scip.DefaultModel().HideOutput().Maximize()
x := scip.NewVar().Name("x").Int().Obj(3).AddTo(model)
y := scip.NewVar().Name("y").Int().Obj(4).AddTo(model)
model.Add(
	scip.NewCons().Coef(x, 2).Coef(y, 1).Le(100),
	scip.NewCons().Coef(x, 1).Coef(y, 2).Le(80),
)

solved := model.Solve()
sol, _ := solved.BestSol()
fmt.Println(solved.Status(), sol.ObjVal(), sol.Val(x), sol.Val(y))
// Optimal 200 40 20
```

## Features

- **The whole modeling surface.** Continuous, integer, binary and implicit
 integer variables; linear, set partitioning, packing and covering,
 cardinality, SOS1, indicator, quadratic and general nonlinear
 constraints; expression trees and SCIP's own expression syntax; reading
 and writing LP, MPS and the other formats SCIP knows.
- **Plugins in Go.** Branching rules, primal heuristics, separators,
 pricers, constraint handlers, event handlers and node selectors are Go
 interfaces, registered with a builder. Panics in callbacks are captured
 and re-raised from `Solve` instead of crashing the process.
- **Safe by construction.** Methods that can fail against SCIP come in a
 panicking and an error-returning form, so you choose per call site.
 Every query checks the solver stage and the
 liveness of the model and handle before touching SCIP, so a call in the
 wrong stage, on a freed model, or with a handle from a freed or replaced
 problem produces a Go error instead of undefined behaviour.
- **Fits a Go service.** Solves stop on a `context.Context`. SCIP's log
 routes into an `io.Writer`, a `*slog.Logger` or a callback. Memory is
 released explicitly with `Free` or by a finalizer.
- **Concurrent and exact solving.** SCIP's parallel portfolio through
 `SolveConcurrent`, and end-to-end rational arithmetic through
 `EnableExactSolving` with `*big.Rat` results.

## Installation

scipgo links against an installed SCIP 10 through cgo. Nothing is bundled.

```bash
# macOS
brew install scip

# Ubuntu 22.04 (packages for other distributions on the SCIP releases page)
wget https://github.com/scipopt/scip/releases/download/v10.0.2/scipoptsuite_10.0.2-1+jammy_amd64.deb
sudo apt-get install -y ./scipoptsuite_10.0.2-1+jammy_amd64.deb

go get github.com/egoisutolabs/scipgo/scip
```

Go 1.25 or newer and a C compiler are required. SCIP in a custom location,
Docker images and build errors are covered in the
installation guide.

## Documentation

The documentation walks through the binding from the
first model to branch-and-price; the
API reference
documents every method.

| Guide | Covers |
| --- | --- |
| Getting started | A first model, builders, reading a file, controlling the solve |
| Modeling | Variables, every constraint kind, nonlinear expressions, file I/O |
| Solving | Statuses, limits, stopping a solve, statistics, re-solving, concurrent and exact modes |
| Solutions | Reading solutions, MIP starts, partial solutions |
| Parameters | The parameter API and the parameters worth knowing |
| Logging | Routing SCIP's log and error output |
| Errors | `Try` and panicking forms, error types, liveness |
| Model lifecycle | Stages, handles, memory, goroutines |
| Plugins | Writing branch rules, heuristics, separators, pricers, constraint handlers, event handlers and node selectors |
| Coming from russcip | The mapping between the Rust API and this one |

## Examples

Eleven complete programs live under `examples/`,
each solving a real problem and checking its answer: a first MIP, a
knapsack, custom branching, node selection, event handling, a rounding
heuristic, a clique separator, TSP with subtour elimination, cutting stock
and bin packing by branch-and-price, and a concurrent solve. Run one from
its directory with `go run .`.

## Repository layout

| Path | Contents |
| --- | --- |
| `scip/` | The library, a single Go package. cgo glue, the `Model` API, builders and plugin callbacks live together because cgo's exported trampolines must sit in the package that owns the C helpers |
| `examples/` | Example programs |
| `docs/` | The guides |
| `data/test/` | Small LP and MPS instances used by the tests and examples |

## Status

scipgo is pre-1.0. The API is stable in shape, and renames ship with
deprecated aliases that stay until the next major version; see the
changelog. It is tested on macOS and Linux against SCIP
10 on every push.

## Contributing

Bug reports, questions and pull requests are welcome. The
contributing guide covers the development setup, the
test suite and the conventions the code follows.

## License

scipgo is licensed under the MIT License, Copyright (c) 2026
Egoisuto Labs.

It is a port of russcip by Mohammed
Ghannam and contributors, licensed under the Apache License 2.0. The
derived parts (API design, tests, examples, `data/test`) keep that
license; see `LICENSE-russcip` and `NOTICE`,
and keep both files with any redistribution. SCIP
itself is Apache-2.0 and is linked, not bundled.

# Lokutor | Full-Stack Voice AI on CPU

## 关联链接

- https://github.com/scipopt/scip/releases/download/v10.0.2/scipoptsuite_10.0.2-1+jammy_amd64.deb
- https://pkg.go.dev/github.com/egoisutolabs/scipgo/scip

## 导航

- 项目页：[[10-项目/github.com_a03f8a13]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
