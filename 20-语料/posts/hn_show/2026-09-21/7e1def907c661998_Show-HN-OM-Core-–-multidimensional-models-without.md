---
type: "corpus"
item_id: "7e1def907c661998"
title: "Show HN: OM Core – multidimensional models without spreadsheet cell formulas"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48733642"
project_url: "https://github.com/cloudcell/om-core"
author: "cloudcell"
published_at: "2026-06-30T14:58:10Z"
captured_at: "2026-09-21T02:53:03+08:00"
lang: "en"
kind: "post"
topic: 开发者工具
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_cloudcell
  - story_48733642
  - show_hn
metrics: {"points": 14, "comments": 6, "engagement_velocity": 14}
comments_count: 6
comments_total: 6
discovered_via: "hn:show_hn:113d"
---

# Show HN: OM Core – multidimensional models without spreadsheet cell formulas

> [!info] 一句话导读
> OM Core - open-source multidimensional modeling engine.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48733642>
> 指标：点赞=14 · 评论=6 · engagement_velocity=14
> 作者：cloudcell　|　发布：2026-06-30T14:58:10Z
> 项目链接：<https://github.com/cloudcell/om-core>
> 采集：2026-09-21T02:53:03+08:00　|　id：`7e1def907c661998`

## 正文

# cloudcell/om-core

OM Core - open-source multidimensional modeling engine.

- Stars: 17
- Forks: 5
- Watchers: 17
- Open issues: 2
- License: GNU Affero General Public License v3.0
- Homepage: https://cloudcell.github.io/om-docs/
- Default branch: main
- Created: 2026-06-29T00:30:50Z

## Languages

- PowerShell
- Python
- Shell

## Topics

- agpl
- automation
- financial-analysis
- financial-modeling
- fp-and-a
- modeling
- multidimensional
- numerical-modeling
- olap
- planning
- python
- spreadsheet

## Top Contributors

- github-actions[bot] (32 contributions)
- cloudcell (1 contributions)

---

## README

 📈 All-time tracked views 258
 📥 All-time tracked clones 177
 ⭐ Current stars 17
 🍴 Current forks 5

 🧬 All-time commits 68
 ⬇️ Tracked release downloads 0
 👀 Watchers 1
 🩺 Traffic history complete

Repository created: 2026-06-29 ·
Traffic retained from: 2026-07-29 ·
Updated: 2026-08-18T13:11:47Z

> **Traffic retention:** GitHub itself exposes only its most recent 14 days of repository views/clones. This repository permanently retains every daily bucket collected from **2026-07-29** onward, so these cumulative traffic totals keep growing and never roll off.

### All-time tracked traffic

All-time tracked traffic

### Daily traffic

Daily repository traffic

### Repository history

Stars

Forks

Commits

### Referral sources

Top referral sources

GitHub exposes only the top 10 referral sources for its rolling 14-day window.
Every returned source/window is permanently archived. Overlapping windows are
not summed because that would double-count visits.

Data: stats/daily.csv ·
Sources now: stats/referrers-latest.csv ·
All sources ever observed: stats/referrers-ever.csv ·
Source-window archive: stats/referrers-windows.csv ·
Release-asset ledger: stats/release-assets.json ·
Raw polls: stats/polls.jsonl

# OM Core

OM Core is an open-source reference implementation of a multidimensional
modeling engine for structured financial, operational, and analytical models.

Instead of treating the spreadsheet grid as the model, OM Core represents the
model using dimensions, cubes, groups, and rules. Grids and views are
projections of that model, not the source of truth.

> Alpha software: OM Core is under active development. APIs, command names, file
> formats, GUI behavior, and module boundaries may change before v1.0.

## Documentation

The main documentation site is here:

https://cloudcell.github.io/om-docs/

Start with:

- What is OM Core: https://cloudcell.github.io/om-docs/start/what-is-om-core/
- Why not spreadsheets:
 https://cloudcell.github.io/om-docs/start/why-not-spreadsheets/
- Installation: https://cloudcell.github.io/om-docs/start/installation/
- Quickstart: https://cloudcell.github.io/om-docs/start/quickstart/

## Core idea

Most spreadsheet models mix several things together:

- model structure
- business logic
- layout
- presentation
- calculation flow
- user interaction

OM Core separates these concerns.

The model is built from:

- **Dimensions** — business axes such as Time, Account, Region, Product,
 Scenario, or Line Item.
- **Cubes** — data stored over one or more dimensions.
- **Groups and hierarchies** — structured collections and rollups.
- **Rules** — calculations expressed over semantic model addresses instead of
 spreadsheet coordinates.
- **Views** — grids and interfaces for inspecting and interacting with the
 model.

A rule should describe the business relationship, not the cell location. For
example, a model should be able to express a relationship such as gross margin
being derived from revenue and cost without making that relationship depend on a
particular row, column, or copied formula.

## Repository scope

This repository currently contains the full alpha application stack required to
run OM Core.

That includes the modeling engine and supporting command, REPL, GUI/TUI,
runtime, timeline, scripting, plugin, storage-adapter, examples, and test
layers.

Some modules are internal implementation layers. They are included because the
current alpha application depends on them. They should not yet be treated as
stable public extension APIs.

## Repository configuration

The `.om/` directory is intentionally committed.

It contains default OM Core application configuration, including toolbar
settings required by the current alpha application. It is not a temporary cache
directory or private local state.

Do not delete `.om/` unless the application configuration system has been
changed to load these defaults from another documented location.

## Installation

OM Core currently runs from source.

### Linux / macOS

```bash
git clone https://github.com/cloudcell/om-core.git
cd om-core
./start.sh
```

### Windows

Use PowerShell:

```powershell
git clone https://github.com/cloudcell/om-core.git
cd om-core
.\start.ps1
```

`./start.sh` or `.\start.ps1` starts the GUI and asks whether to open a TUI in a
separate terminal.

OM Core uses uv to manage its Python environment.
Install uv, then run `uv sync` in the project root to create `.venv` and install
dependencies. After that, the start scripts and test scripts use `uv run`
automatically.

You can also start specific runtime modes:

```bash
# Linux / macOS
./start.sh --gui       # graphical interface only
./start.sh --tui       # terminal interface in the current terminal
./start.sh --runtime   # headless runtime only
./start.sh --repl      # REPL command shell in the current terminal
```

```powershell
# Windows
.\start.ps1 --gui       # graphical interface only
.\start.ps1 --tui       # terminal interface in the current terminal
.\start.ps1 --runtime   # headless runtime only
.\start.ps1 --repl      # REPL command shell in the current terminal
```

For more detail, see the installation guide:

https://cloudcell.github.io/om-docs/start/installation/

## Quickstart

Running `./start.sh` (Linux / macOS) or `.\start.ps1` (Windows) launches the GUI.
You will be prompted to open a TUI in a separate terminal; accepting the default
(`Y`) gives you a command shell alongside the GUI, as shown below.

> **Note:** The first time you run `./start.sh` or `.\start.ps1`, `uv` will create
> a Python virtual environment in the project folder (`.venv`) and install
> dependencies from `uv.lock`.

OM Core GUI and TUI running together

After starting OM Core, try the built-in help command:

```text
om> help
```

You can ask for help on specific topics:

```text
om> help rule
om> help calc
```

A minimal OM Core script looks like this:

```text
# Dimensions
dim Month Jan Feb Mar

# Cube
cube Sales Month

# View
view SalesView = Sales::Month

# Rules
rule Sales::Month.Jan = 100
rule Sales::Month.Feb = Sales::Month.Jan * 1.1
rule Sales::Month.Mar = Sales::Month.Feb * 1.1

# Calculate
calc
```

Save that as `hello.openm`, then source it from the REPL or TUI:

```text
om> source hello.openm
```

For the full walkthrough, see:

https://cloudcell.github.io/om-docs/start/quickstart/

## Testing

Run the test suite with the platform-specific script:

```bash
# Linux / macOS
./test.sh
```

```powershell
# Windows
.\test.ps1
```

## Architecture

OM Core is split into a session-scoped runtime layer, a command/query service
layer, and multiple clients. The engine owns the canonical workspace state; the
GUI, TUI, REPL, and CLI are clients that communicate through the message bus.

Target architecture overview

## Why not just spreadsheets?

Spreadsheets are fast and flexible, but large models often become fragile
because business logic is encoded in cell addresses, copied formulas, linked
tabs, and implicit layout conventions.

OM Core uses a different level of abstraction. It makes the model explicit:
dimensions describe the axes, cubes hold values, groups organize structure,
rules define calculations, and views display the result.

The tradeoff is deliberate: you define more structure up front, and in return
the model becomes easier to audit, extend, test, and maintain as it grows.

For the longer explanation, see:

https://cloudcell.github.io/om-docs/start/why-not-spreadsheets/

## Project status

OM Core is currently alpha software.

Not yet promised before v1.0:

- stable public API
- stable plugin API
- stable scripting API
- stable file format
- packaged desktop installer
- production readiness for critical business use without independent validation

See also:

- `KNOWN_ISSUES.md`
- `CHANGELOG.md`
- `SECURITY.md`

## Legal

OM Core is distributed under the GNU Affero General Public License v3.0 unless
otherwise stated.

See:

- `LICENSE`
- `NOTICE`
- `legal/THIRD-PARTY-NOTICES.md`
- `legal/CONTRIBUTOR-CLA.md`
- `legal/CONTRIBUTOR-SIGNOFFS.md`

The `OM Core` name is governed separately from the software license.

See:

- `legal/TRADEMARKS.md`

## Contributing

Contributions are welcome, especially small, focused improvements
to examples, documentation, and clearly scoped engine behavior.

Please read:

- `CONTRIBUTING.md`
- `legal/CODE_OF_CONDUCT.md`
- `SECURITY.md`

Security issues should not be reported through public GitHub issues. See
`SECURITY.md`.

## Feedback

- **Bugs:** open a GitHub issue.
- **Discussion:** join the Discord.

Error fetching https://www.indiegogo.com/en/projects/miradial/miradial: CRAWL_UNKNOWN_ERROR

## 评论（6/6）

> **cloudcell** · 2026-06-30T14:58:26.000Z　
> I made OM Core public today.It is an early alpha multidimensional modeling engine. The main idea is to separate the model from the grid: dimensions, cubes, rules, and views instead of spreadsheet cell formulas.I am looking for feedback from people who have built or maintained spreadsheet models, especially on whether the abstraction is understandable.Docs: https://cloudcell.github.io/om-docs/

---

> **densekernel** · 2026-07-03T14:59:03.000Z　
> https://x.com/andrewchen/status/2031532980032909640 - related?"prediction re the end of spreadsheetsAI code gen means that anything that is currently modeled as a spreadsheet is better modeled in code. You get all the advantages of software - libraries, open source, AI, all the complexity and expressiveness."

---

> **whiw** · 2026-07-07T14:42:25.000Z　
> I've read the docs but I haven't tried it yet. I like the idea of storing n-dimensional data in an n-dimensional table, and I like the separation between the data ('cube') and the views and rules. I like that the rules operate on slices of the data rather than individual cells.This occupies the space between traditional spreadsheets (simple UI but limited to 2-d) python (multi-dimensional data, and python or tensors (multi-dimensional data, but coding required).I feel that the current data input is a bit cumbersome. There's a lot to type to enter just one cell value, and multi-dimensional tables contain a lot of cells. A more succinct alternative for data entry could be something like python/numpy multi-dimensional tables: [[[a, b, c], [d, e, f]], [[g, h, i], [j, k, l]]].Data entry from a view grid (to a 2-d slice of the 'cube') would be more familiar, like a spreadsheet.A data import feature (from csv, etc) would be useful too.'Cube' has 3d connotations: 'ngrid' or 'ndata' could be less confusing.I didn't see any functions like sum or product (or most other spreadsheet functions) to operate on data slices. I'm guessing that this is still proof of concept at the moment.I do hope this goes further.

---

> **cyanydeez** · 2026-07-03T20:57:02.000Z　
> the only way that's possible is if you can use a spreadsheet to test the code.

---

> **cloudcell** · 2026-07-04T15:50:33.000Z　
> “Anything that is currently modeled” would be true if we could guarantee the correctness of AI-generated code.Business people prefer the familiarity of spreadsheets, or at least some kind of grid. At the same time, I am working on this software out of frustration with spreadsheets, because users are forced to translate A1*B2-style addresses into business meaning.So I agree that code is one possible direction. But I think there is also a middle ground: business rules over dimensions. Enterprise tools like TM1 have explored this direction for decades.

---

> **cloudcell** · 2026-07-09T21:50:51.000Z　
> Thank you for you feedback!The goal of this software is to address the gap in the open source ecosystem. This multidimensional approach for modeling (and financial planning/forecasting) is over 40 years old. Systems like TM1 by IBM, Anaplan (to name just a few), have been using it for many decades.The reason for using the word 'cube' is mainly familiarity of users with the concept of OLAP cube (https://en.wikipedia.org/wiki/OLAP_cube), which is what this tech should perhaps be called.As for data input... indeed, there is some room for improvement: there are 3 ways of editing a rule: via the rule bar, directly on the grid, and modifying an existing rule using the rule panel. We need feedback to decide which way to keep and what to remove. UX/UI is extremely tricky. Oh, there's also a way to insert a rule via the terminal (text user interface command line).As for operation on slices, a slice can be defined using specific items in a dimension and omitting others (which will create a data 'slice'): for example if you have a 'cube' D with dimensions A B and C, and each dimension has items 1 2 and 3, then you can define a sum over a slice through this cube via this rule "=sum(D::a.1)" or, more explicitly, "=sum(D::a.1:b.:c.)", if written directly in a cell.You can fill the whole cube with some value, say, 1, by defining a rule `* = 1` in that particular cube via the rule bar. The rule should produce the total of 9.I hope this is helpful. Feel free to join the project's discord server (https://discord.gg/GfU5ypAbaD) I will be happy to explain.PSThe functions are documented here: https://cloudcell.github.io/om-docs/reference/functions/There's an Excel import plugin (available via menu 'Plugins') that allowed importing basic Excel files (stripping all formatting, however), but I guess it might need a few hours of work at the moment.

## 关联链接

- https://cloudcell.github.io/om-docs/
- https://cloudcell.github.io/om-docs/start/installation/
- https://cloudcell.github.io/om-docs/start/quickstart/
- https://cloudcell.github.io/om-docs/start/what-is-om-core/
- https://cloudcell.github.io/om-docs/start/why-not-spreadsheets/
- https://github.com/cloudcell/om-core.git
- https://www.indiegogo.com/en/projects/miradial/miradial:

## 导航

- 项目页：[[10-项目/github.com_91e69c04]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
