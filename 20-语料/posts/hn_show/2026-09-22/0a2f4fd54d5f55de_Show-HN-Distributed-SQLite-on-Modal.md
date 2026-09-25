---
type: "corpus"
item_id: "0a2f4fd54d5f55de"
title: "Show HN: Distributed SQLite on Modal"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49789058"
project_url: "https://github.com/modal-projects/sqlite-modal"
author: "botirk"
published_at: "2026-09-21T16:05:20Z"
captured_at: "2026-09-25T00:12:57+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-22"
pub_day: "2026-09-21"
tags:
  - 语料
  - hn_show
  - author_botirk
  - story_49789058
  - show_hn
metrics: {"points": 4, "comments": 1, "engagement_velocity": 4}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Distributed SQLite on Modal

> [!info] 一句话导读
> modal-projects/sqlite-modal

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49789058>
> 指标：点赞=4 · 评论=1 · engagement_velocity=4
> 作者：botirk　|　发布：2026-09-21T16:05:20Z
> 项目链接：<https://github.com/modal-projects/sqlite-modal>
> 采集：2026-09-25T00:12:57+08:00　|　id：`0a2f4fd54d5f55de`

## 正文

# modal-projects/sqlite-modal

Distributed SQLite on Modal

- Stars: 8
- Forks: 0
- Watchers: 8
- Open issues: 0
- License: Apache License 2.0
- Default branch: main
- Created: 2026-07-14T22:45:34Z

## Languages

- Python

## Top Contributors

- botirkhaltaev (4 contributions)

---

## README

# sqlite-modal

Distributed SQLite on Modal. Local SQL against a
file; `push` / `pull` to a Server in your workspace. A Volume holds the
remote file on exit. Sync uses the Turso SDK.

You create named DBs in your Modal workspace. This is not a managed
multi-tenant service.

```text
local file  --push/pull-->  SyncServer
                                |
                         exit → Volume /data
```

Local SQL stays on your machine. Sync is an explicit hop to a warm Server
in eu-west.

Reads are about 0.01 ms and 121k/s. A local commit is about 0.09 ms.

Warm push / pull is about 158 ms / 79 ms. Conflicts are last-push-wins.

## Install

Python >= 3.12 and a Modal account (`modal setup`).

```bash
uv add git+https://github.com/modal-projects/sqlite-modal.git
```

Deploy from a checkout (or editable install) so Image builds can
`add_local_python_source("sqlite_modal")`. PyPI is not set up yet.

```bash
uv sync
uv sync --group dev    # tests / lint
uv sync --group bench  # charts
```

## Usage

```python
from sqlite_modal import Sqlite

db = Sqlite.from_name("orders", create_if_missing=True)
conn = db.connect("./orders.db")
with conn:
    conn.execute("CREATE TABLE IF NOT EXISTS t (v TEXT)")
    conn.execute("INSERT INTO t VALUES (?)", ("a",))
    conn.commit()
    conn.push()
    conn.pull()
```

- `from_name` creates or looks up App `sqlite-modal-{name}` (`create_options` → `@app.server`)
- One SyncServer container per name. `max_containers` is fixed at 1.
- `connect(path)` opens a local connection and waits until the Server is up
- Sync is explicit (`push` / `pull`). Conflicts are last-push-wins.
- Use `min_containers=1` if you don't want cold starts.
- The sync URL is unauthenticated. Anyone who has it can `push` / `pull`.
- Volume persist runs when the Server exits.

## Examples

```bash
uv run python examples/notes/app.py
uv run python examples/multi/app.py
```

| Kit | When |
|-----|------|
| `examples/notes/` | One named DB |
| `examples/multi/` | Two Apps, two names |

## Development

```bash
uv run pytest
uv run ruff check sqlite_modal examples benchmarks tests
uv run ty check sqlite_modal examples benchmarks tests

uv run python benchmarks/app.py --create-remotes  # once
uv run python benchmarks/app.py
uv run python benchmarks/app.py --cold            # optional
```

Details: benchmarks/README.md.

CI is GitHub Actions on `ubuntu-latest`.

## License

Apache License 2.0

## 评论（1/1）

> **botirk** · 2026-09-21T16:05:20.000Z　
> introducing sqlite-modali wanted a database primitive on Modal for a while, so I built this project!sqlite-modal fixes this:- push/pull sync.
> - durable source of truth.
> - no database server.

## 关联链接

- https://github.com/modal-projects/sqlite-modal.git

## 导航

- 项目页：[[10-项目/github.com_404776f4]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
