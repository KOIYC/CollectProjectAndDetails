---
type: "corpus"
item_id: "3ef5339edcc3dfef"
title: "Show HN: Rampart on CoreML"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48733651"
project_url: "https://github.com/narner/Rampart-CoreML"
author: "narner"
published_at: "2026-06-30T14:58:31Z"
captured_at: "2026-09-21T02:53:02+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_narner
  - story_48733651
  - show_hn
metrics: {"points": 6, "comments": 2, "engagement_velocity": 6}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:113d"
---

# Show HN: Rampart on CoreML

> [!info] 一句话导读
> narner/Rampart-CoreML

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48733651>
> 指标：点赞=6 · 评论=2 · engagement_velocity=6
> 作者：narner　|　发布：2026-06-30T14:58:31Z
> 项目链接：<https://github.com/narner/Rampart-CoreML>
> 采集：2026-09-21T02:53:02+08:00　|　id：`3ef5339edcc3dfef`

## 正文

# narner/Rampart-CoreML

- Stars: 9
- Forks: 0
- Watchers: 9
- Open issues: 0
- License: Creative Commons Attribution 4.0 International
- Default branch: main
- Created: 2026-06-30T01:14:07Z

## Languages

- Python
- Shell
- Swift

## Top Contributors

- narner (1 contributions)

---

## README

# Rampart Core ML

Core ML conversion and Swift package for
`nationaldesignstudio/rampart`,
a local PII token-classification model.

License: CC BY 4.0. See NOTICE.md for upstream
Rampart model attribution and a summary of local changes.

## Demo

https://github.com/user-attachments/assets/4e7a2f9f-d8e6-4724-88f3-6030480bea7a

## Model Artifacts

The model is published as a GitHub Release asset instead of committed to Git.
Swift package users can let the package download and cache it on first use:

```swift
let classifier = try await RampartCoreMLClassifier.downloaded()
```

For repo-local workflows, download the same Core ML package, vocabulary, and
config files before running the full test suite:

```sh
scripts/download_model.sh
```

This writes:

```text
artifacts/RampartTokenClassifier.mlpackage
artifacts/rampart-hf/vocab.txt
artifacts/rampart-hf/config.json
```

These files are ignored by Git.

To reproduce the Core ML package from the upstream ONNX model instead, run the
converter:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-convert.txt
python3 scripts/convert_rampart_to_coreml.py
```

The converter downloads the upstream Rampart ONNX/tokenizer/config files into
`artifacts/rampart-hf/` and writes the Core ML package to
`artifacts/RampartTokenClassifier.mlpackage`.

## Swift Package

The `RampartCoreML` package provides a
WordPiece tokenizer,
the BERT-style subword tokenizer Rampart expects, plus a Core ML inference
wrapper and deterministic SSN recognizer.

```swift
import RampartCoreML

let classifier = try await RampartCoreMLClassifier.downloaded()
let result = try classifier.classify("Alex Rivera lives at 221B Baker Street.")
let piiTokens = result.predictions.filter { $0.label != "O" }
let deterministicMatches = result.deterministicDetections
```

Run the Swift package checks with:

```sh
swift test
```

Tests that need local model artifacts skip until
`scripts/download_model.sh` or `scripts/convert_rampart_to_coreml.py` has been
run.

## CLI

Run an ad hoc classification with:

```sh
swift run RampartCLI -- "my name is nick and my ssn is 111-111-1111"
swift run RampartCLI -- --all "my name is nick and my ssn is 111-111-1111"
```

The CLI downloads the model artifacts on first run when the default local
artifact paths are missing. It prints deterministic matches separately from
model token predictions.

## iOS Example

An example SwiftUI app lives at:

```sh
Examples/RampartExampleiOS/RampartExampleiOS.xcodeproj
```

Open the project and run the app. The example downloads and caches the model on
first launch, then shows a text input, redacted-text preview, and structured
detections.

## Validation

After running the converter, compare ONNX and Core ML predictions with:

```sh
python3 scripts/validate_coreml_parity.py
```

## License

This repository is released under the Creative Commons Attribution 4.0
International license (`CC-BY-4.0`) to match the upstream Rampart model.

# cloudcell/om-core

## 评论（2/2）

> **cjc500** · 2026-06-30T15:04:49.000Z　
> sweet, checking this out!

---

> **edunteman** · 2026-06-30T23:22:31.000Z　
> Nice work! Had to do similar serverside for stripping named entities and ended up burning way too much LLM cash

## 关联链接

- https://github.com/user-attachments/assets/4e7a2f9f-d8e6-4724-88f3-6030480bea7a

## 导航

- 项目页：[[10-项目/github.com_f439c7af]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
