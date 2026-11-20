---
type: "corpus"
item_id: "40e67faed9597c5c"
title: "Show HN: Detect and mask PII, payment data and secrets in logs for Go"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50560084"
project_url: "https://github.com/nao1215/embargo"
author: "nchika"
published_at: "2026-11-19T13:49:55Z"
captured_at: "2026-11-20T09:45:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-20"
pub_day: "2026-11-19"
tags:
  - 语料
  - hn_show
  - author_nchika
  - story_50560084
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Detect and mask PII, payment data and secrets in logs for Go

> [!info] 一句话导读
> Detect and mask personal data, payment data and secrets in text and logs for Go. Zero dependencies, cross-platform.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50560084>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：nchika　|　发布：2026-11-19T13:49:55Z
> 项目链接：<https://github.com/nao1215/embargo>
> 采集：2026-11-20T09:45:52+08:00　|　id：`40e67faed9597c5c`

## 正文

# nao1215/embargo

Detect and mask personal data, payment data and secrets in text and logs for Go. Zero dependencies, cross-platform.

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-02-08T03:32:46Z

## Languages

- Go
- Makefile
- Python

## Topics

- data-masking
- go
- golang
- logging
- pii
- redaction
- secrets
- security
- sensitive-data
- zero-dependency

## Top Contributors

- nao1215 (65 contributions)
- dependabot[bot] (4 contributions)

---

## README

# embargo

All Contributors

Go Reference
MultiPlatformUnitTest
reviewdog
Gosec
Trivy
Coverage
OpenSSF Scorecard

embargo detects and masks sensitive text in Go programs, logs and test output.

- Mask card numbers and emails before logs leave your service.
- Check in tests that an HTTP handler or child process never writes a secret.
- Scan support messages and imported files for personal data.
- Detect Japanese phone numbers and My Number, including full-width digits.

## Quick start

These examples use the unreleased API on main (Go 1.26.11 or later).

```sh
go get github.com/nao1215/embargo@main
```

```go
package main

import (
	"fmt"

	"github.com/nao1215/embargo"
)

func main() {
	text := "email=alice@example.com card=4111111111111111"
	scanner := embargo.NewScanner(embargo.WithKinds(embargo.KindEmail, embargo.KindPAN))

	fmt.Println(embargo.Mask(text, scanner.ScanString(text)))

	// Output: email=[REDACTED] card=[REDACTED]
}
```

Scanner options and custom detectors.

## Why embargo?

gitleaks and trufflehog scan repositories and files; Presidio provides Python analyzers. Secret wrappers hide marked values without detecting sensitive text. embargo runs inside Go to mask logs, hide Secret values, and check real output with canaries and detectors.

| Inside your Go program | What happens |
|---|---|
| `NewSlogHandler` | `email=alice@example.com` → `email=[REDACTED]` |
| `NewSecret` | `fake-key` → `[REDACTED]` |
| `embargotest` | A canary in logs, HTTP or child output fails the test. |

How the pieces fit.

## Scanning and masking

| Operation | Actual text |
|---|---|
| Input | `INFO checkout email=alice@example.com card=4111111111111111` |
| Mask | `INFO checkout email=[REDACTED] card=[REDACTED]` |
| MaskFunc: keep last four | `INFO checkout email=[REDACTED] card=[REDACTED]1111` |
| Overlapping matches | `token=abcdef` with `abcd cdef` → `token=[REDACTED]` |

Scanner options, custom replacements and overlapping matches.

## Values that must not be displayed

Wrap a value with `Secret` before passing it to a logger or encoder.

```go
key := embargo.NewSecret("fake-key")

fmt.Println(key)

// Output: [REDACTED]
```

Formatting, decoding with Input, and deliberate access with Reveal.

## Mask logs

`next` is the handler your logger already uses.

```go
scanner := embargo.NewScanner(embargo.WithKinds(embargo.KindEmail))
logger := slog.New(embargo.NewSlogHandler(next, scanner))

logger.Info("checkout", "email", "alice@example.com")

// Output: {"level":"INFO","msg":"checkout","email":"[REDACTED]"}
```

Full runnable example · Groups, value handling and output failures.

## Logger adapters

| Logger | Adapter example | Output excerpt |
|---|---|---|
| zap | NewWriteSyncer | `"email":"[REDACTED]"` |
| zerolog | NewWriter | `"email":"[REDACTED]"` |
| logrus | NewFormatter | `"email":"[REDACTED]"` |

Each optional module masks the logger's encoded JSON, including nested values. Installation, APIs and encoded-binary limits.

## Check test output

A canary is a fake secret injected into the code under test. The recorder checks both that useful output exists and that canaries or detected values did not escape.

```go
func TestReadmeCheckOutput(t *testing.T) {
    t.Parallel()
    recorder := embargotest.New(t)
    logger := slog.New(slog.NewJSONHandler(recorder.Writer("logs"), nil))

    logger.Info("accepted", "token", embargo.NewSecret(recorder.Canary()))

    recorder.ExpectJSON("logs", nil, map[string]string{"token": "[REDACTED]"}, 1)
    recorder.Check()
}
```

Output includes `"token":"[REDACTED]"` and the test passes. HTTP, child processes, expectations and allowed fixtures.

## Tested outputs

Each link opens the test that produces and checks the shown output.

| Output | Actual output (excerpt for SDKs) |
|---|---|
| fmt | `[REDACTED]` |
| slog TextHandler | `level=INFO msg=event token=[REDACTED] nested.again=[REDACTED]` |
| slog JSONHandler | `{"level":"INFO","msg":"event","token":"[REDACTED]","nested":{"again":"[REDACTED]"}}` |
| encoding/json | `"[REDACTED]"` |
| encoding/xml | ` [REDACTED] ` |
| text/template | `[REDACTED]` |
| zap JSON core | `{"level":"info","msg":"event","token":"[REDACTED]"}` |
| zerolog JSON | `{"level":"info","token":"[REDACTED]","message":"event"}` |
| logrus JSON | `{"level":"info","msg":"event","token":"[REDACTED]"}` |
| OTel SDK | `{"Key":"key","Value":{"Type":"STRING","Value":"[REDACTED]"}}` |
| Sentry | `"signing":{"key":"[REDACTED]"}` |
| HTTP | `[REDACTED]` |
| Child panic | `panic: [REDACTED]` |

Complete integration checks.

## Accuracy

This chart shows the held-out synthetic set at the default minimum confidence of 0. Generation, test cases and observed misses explain the scores.

Precision and recall on held-out synthetic samples

| Detector details | | |
|---|---|---|
| aba_routing | ach_trace | awskey |
| bank_account | btc | card_expiry |
| cvv | email | eth |
| github_token | google_api_key | iban |
| ipaddr | jwt | merchant_id |
| mynumber | pan | payment_token |
| phone_jp | private_key_pem | slack_token |
| swiftbic | uk_sortcode | |

## Testing

| Technique | Bugs it catches | Tests |
|---|---|---|
| Examples and unit tests | Wrong outputs and broken contracts | Examples, masking |
| Generated properties | Checksum and boundary mistakes | Properties, Bitcoin |
| Fuzzing | Panics and broken input handling | Scanner, recorder |
| Mutation | Missing assertions | gremlins command |
| Real output tests | Leaks after encoding or buffering | Loggers, HTTP |

Coverage 96.8% · mutation score 90.68% · 7 fuzz targets, 2949231 executions.

Commands, measurement scope and conditions.

## Benchmarks

Scanner throughput and slog time

All detectors scan sensitive text at 9.89 MB/s; masking a clean slog event takes 2.26 µs, 2.7× the plain handler.

Machine, method, profiles and full results.

## Contributing

Report a bug → add a synthetic regression → open a pull request. You can also sponsor maintenance.

## License

MIT License.

The Go gopher was designed by Renee French and is licensed under CC BY 4.0.

## Contributors

Thanks to our contributors:

 CHIKAMATSU Naohiro Code Documentation

This project follows the all-contributors specification.

# ZXC v1.0.0 - Hydrogen

## 评论（1/1）

> **sambejk** · 2026-11-19T13:57:32.000Z　
> Cool! Does it scan for patterns or does it use some ML?I made an application in the past that used cryptography to pseudonymize PII allowing to reverse them as well. Source: https://belfortlabs.com/blog/smals-blind-pseudonymization

## 导航

- 项目页：[[10-项目/github.com_cbdcef6b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
