---
type: "corpus"
item_id: "818eaf25844a1b4d"
title: "Show HN: OpenATP: A platform for automated theorem proving in Lean"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48732050"
project_url: "https://github.com/henryrobbins/open-atp"
author: "henryrobbins00"
published_at: "2026-06-30T12:53:10Z"
captured_at: "2026-09-21T02:53:07+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_henryrobbins00
  - story_48732050
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: OpenATP: A platform for automated theorem proving in Lean

> [!info] 一句话导读
> henryrobbins/open-atp

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48732050>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：henryrobbins00　|　发布：2026-06-30T12:53:10Z
> 项目链接：<https://github.com/henryrobbins/open-atp>
> 采集：2026-09-21T02:53:07+08:00　|　id：`818eaf25844a1b4d`

## 正文

# henryrobbins/open-atp

OpenATP is an open-source Python package providing a common interface for Automated Theorem Proving (ATP)

- Stars: 27
- Forks: 1
- Watchers: 27
- Open issues: 4
- License: MIT License
- Homepage: https://open-atp.henryrobbins.com
- Default branch: main
- Created: 2026-06-22T19:16:10Z

## Languages

- Dockerfile
- Lean
- Makefile
- Python
- Shell

## Topics

- automated-theorem-proving
- formal-verification
- lean4
- llm-agents
- mathlib
- theorem-proving

## Top Contributors

- henryrobbins (324 contributions)
- github-actions[bot] (8 contributions)

---

## README

PyPI
Docs
CI
codecov
License: MIT
Checked with mypy
Ruff

**OpenATP** is an open-source Python package providing a common interface for **Automated Theorem Proving (ATP)**. OpenATP focuses on recent **agentic ATP methods** that prove formal statements in Lean. Each method runs in an isolated sandbox, either locally with Docker or remotely with Modal. OpenATP also provides benchmarking utilities to run methods on **common datasets**.

## Installation

```bash
pip install open-atp
```

`OpenATP` runs each prover (e.g., Claude Code, Codex, OpenCode) in a
Docker container. The image must be built before running any prover:

```bash
open-atp build-docker-image
```

Each prover has its own authentication requirements. See each prover page for its authentication instructions, and check what the host currently has with:

```bash
open-atp auth-status
```

## Quickstart

Complete the `sorry`s in a lake project (or a `.lean` file) from the CLI:

```bash
open-atp prove path/to/project runs/example claude
```

Or programmatically, here on a simple example theorem:

```python
from open_atp import standard_prover
from open_atp.backends import DockerBackend
from open_atp.examples import EXAMPLE, example_task

prover = standard_prover("claude", backend=DockerBackend())
task = example_task(EXAMPLE.MUL_REORDER)

result = prover.prove(task, output_dir="runs/example")
```

## Available provers

The `ID` is the standard prover name used by `standard_prover`, the CLI `prove` command's `prover` argument, and the `benchmark` command's `-p/--provers` option. Also see Provers.

| Prover | ID | Skills | MCP | Paper | Source |
| --- | --- | --- | --- | --- | --- |
| Claude Code | `claude` | leanprover, lean4 | ✓ | — | — |
| Codex | `codex` | leanprover | ✓ | — | GitHub |
| DeepSeek | `deepseek` | leanprover | ✓ | — | GitHub |
| Grok | `grok` | leanprover | ✓ | — | — |
| Muse Spark | `spark` | leanprover | ✓ | — | — |
| AxProverBase | `axproverbase` | — | ✗ | Requena et al. 2026 | GitHub |
| Leanstral | `leanstral` | leanprover | ✓ | Leanstral (blog) | HuggingFace |
| Kimi Code | `kimi` | leanprover | ✓ | — | GitHub |
| Numina | `numina` | — | ✓ | Liu et al. 2026 | GitHub |
| Aristotle | `aristotle` | — | — | Achim et al. 2025 | — |

## Download common datasets

OpenATP provides utilities to download common proof-synthesis benchmarks (see Downloading a dataset). The available datasets are listed in the `DATASET` enum.

| Benchmark | `DATASET` | Toolchain | Paper | Source |
| --- | --- | --- | --- | --- |
| Examples | `EXAMPLES` | `v4.28.0` | — | docs |
| PutnamBench | `PUTNAM` | `v4.27.0` | Tsoukalas et al. 2024 | trishullab/PutnamBench |
| FATE-H | `FATE_H` | `v4.28.0` | Jiang et al. 2025 | frenzymath/FATE-H |
| FATE-M | `FATE_M` | `v4.28.0` | Jiang et al. 2025 | frenzymath/FATE-M |
| FATE-X | `FATE_X` | `v4.28.0` | Jiang et al. 2025 | frenzymath/FATE-X |

## Citing

If you use `OpenATP` in your work, please cite it:

```bibtex
@software{openatp,
  title = {OpenATP: Open Automated Theorem Proving},
  author = {Henry Robbins},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/henryrobbins/open-atp}
}
```

OpenATP includes provers with associated papers and bundles popular open-source tools for improving agentic theorem proving. Please see Citations for a comprehensive list of references.

## Development

See `AGENTS.md` for development information.

## License

MIT

# gkavinrajanCodes/pulseDB

## 关联链接

- https://github.com/henryrobbins/open-atp}
- https://open-atp.henryrobbins.com

## 导航

- 项目页：[[10-项目/github.com_fbb8e1cb]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
