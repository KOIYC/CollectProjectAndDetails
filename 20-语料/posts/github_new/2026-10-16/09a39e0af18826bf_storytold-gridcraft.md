---
type: "corpus"
item_id: "09a39e0af18826bf"
title: "storytold/gridcraft"
source: "github_new"
source_name: "GitHub 新星仓库"
url: "https://github.com/storytold/gridcraft"
project_url: "https://github.com/storytold/gridcraft"
author: "storytold"
published_at: "2026-10-07T05:18:16Z"
captured_at: "2026-10-16T09:37:25+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-16"
pub_day: "2026-10-07"
tags:
  - 语料
  - github_new
  - Rust
  - created:>2026-10-02
metrics: {"stars": 5195, "forks": 2353, "open_issues": 934}
comments_count: 0
comments_total: 0
discovered_via: "github:14d"
---

# storytold/gridcraft

> [!info] 一句话导读
> <a href="https://getartcraft.com/">

> [!meta]- 语料信息（点开展开）
> 来源：GitHub 新星仓库（post）
> 原帖：<https://github.com/storytold/gridcraft>
> 指标：stars=5195 · forks=2353 · open_issues=934
> 作者：storytold　|　发布：2026-10-07T05:18:16Z
> 项目链接：<https://github.com/storytold/gridcraft>
> 采集：2026-10-16T09:37:25+08:00　|　id：`09a39e0af18826bf`

## 正文

GridCraft

  Spreadsheets and data; an open-source, clean-room reimplementation of Microsoft Excel, rebuilt in pure Rust.

  A fast, open-source, clean-room take on the Excel workflow. It runs natively on macOS,
  Windows, Linux and BSD, and in the browser via WebAssembly.
  By the ArtCraft team.

  GridCraft on getartcraft.com ·
  ArtCraft ·
  All Crafting Apps

  Quarterly Sales Dashboard: a table with a totals row, conditional formatting, sparklines and two live charts — built entirely from GridCraft commands (File → New → Sample).

> [!NOTE]
> **ArtCraft is a community of artists from all walks of life.** Painters, photographers,
> filmmakers, illustrators, designers, animators, hobbyists, and people who picked up a pencil
> last week. If you make things, you're one of us. **[Come say hi on Discord](https://discord.gg/artcraft).**

  A look around ·
  Why GridCraft ·
  Quick start ·
  For agents ·
  Architecture ·
  Roadmap ·
  The Crafting Apps ·
  License and credits

## A look around

Formatting. Accounting formats, cell styles, conditional rules and colour scales, frozen headers and a bar chart.
Formulas. 500+ functions, dynamic arrays, LET and LAMBDA, structured table references.

Dark mode and the Insert tab: tables, charts, sparklines, pictures, shapes, links and comments.
PivotTables. Field list, filters, layouts, date grouping and show-values-as, saved to and read from XLSX.

Charts. Seventeen chart types, Chart Design tab and a Format pane; selecting a chart outlines its source data.
Page Break Preview, print settings, and PDF export and printing.

## Why GridCraft

- **Familiar.** Excel's ribbon, formula bar, Name Box, sheet tabs, keyboard shortcuts, fill
  handle, point-mode formula entry with coloured references, Format Cells, Paste Special,
  conditional formatting, tables, charts and more. If you know Excel, you already know GridCraft.
- **Compatible.** XLSX is the native format: styles, themes, formulas (including dynamic arrays),
  tables, conditional formats, validation, comments, hyperlinks, charts, pictures, sparklines,
  PivotTables and print settings round-trip. CSV and TSV too.
  Excel 97-2003 `.xls` workbooks open with their values, formulas and number formats (formatting and objects not yet).
  [XLSB worksheet data can be imported](docs/xlsb-import.md), using saved values instead of formulas.
  [ODS worksheet data can be imported](docs/ods-import.md), using saved values instead of formulas.
  [Static pictures can live inside cells](docs/cell-pictures.md), fitting their size and moving with the data.
- **Capable.** A dependency-graph calculation engine with dynamic arrays and spilling,
  500+ worksheet functions plus LET, LAMBDA, MAP, REDUCE, SCAN, BYROW, BYCOL and MAKEARRAY,
  structured table references, Excel's full number-format language, sort and AutoFilter,
  Flash Fill, data validation, outlining and subtotals.
- **Fast.** Copy-on-write workbooks (undo snapshots are nearly free), incremental recalculation,
  and a virtualised grid that only lays out what's on screen.
- **Agent-native.** Every ribbon button, menu item, dialog, keystroke and mouse gesture is a
  command that agents can run over a JSON control channel, an **MCP server**, or the CLI.
- **Everywhere.** One Rust codebase for desktop and the web. No subscription, no licence server,
  no telemetry.

## Quick start

```sh
cargo run --release -p gridcraft                              # desktop app
cargo run --release -p gridcraft -- --sample sales            # open a sample (sales, budget, grades)
cargo run --release -p gridcraft -- book.xlsx                 # open a workbook
cargo run --release -p gridcraft -- --sample sales --control 7979   # + JSON control channel
cargo xtask ci                                                 # fmt, clippy, tests, assets, layering, wasm
```

Choose Español under View → Interface language for [Spanish formula names, decimal commas, and semicolon arguments](docs/formula-input.md).
Workbooks, clipboard exchange, and programmatic APIs retain canonical English syntax.

### Web

```sh
cd apps/gridcraft-web && trunk build --release     # → dist/web (serve it with any static server)
cd apps/gridcraft-web && trunk serve --release     # http://127.0.0.1:8771  (?sample=sales opens a sample)
```

You need [trunk](https://trunkrs.dev) and the `wasm32-unknown-unknown` target. Open uses the
browser's file picker (dropping files works too) and Save downloads the workbook.

### Ribbon access keys

Press and release **left Alt** on Windows/Linux/BSD, or press **F10** on any platform,
then type a sequence below one key at a time. Keytips appear on the supported Home
controls and menu items. On macOS, use F10 (Fn+F10 if required by your keyboard); Option
remains available for entering accented characters.

| Sequence after Alt/F10 | Action |
|---|---|
| `H A L` / `H A C` / `H A R` | Align left / center / right |
| `H V S` or legacy `E S` | Open Paste Special |
| `H O I` or legacy `O C A` | AutoFit selected columns |

In Paste Special, **T/V/F/C** select formats/values/formulas/comments, and **E** toggles
Transpose. **Enter** applies the selected options; **Escape** cancels the dialog.
These letters also work with Alt held on Windows/Linux/BSD.

Escape backs out one keytip level; Alt/F10 again exits keytips. Clicking, scrolling,
or switching windows cancels navigation. Access keys do not start while editing text
or using another dialog. This is initial support for these Home and legacy paths;
other ribbon commands and full mouse-free navigation remain to be implemented.
Browsers or desktop environments may reserve Alt/F10 for their own menus.

### Logs

The desktop app writes its log to standard error and to `gridcraft.log` in the `logs` folder
next to its settings: `~/.config/gridcraft/logs` on Linux and BSD (`$XDG_CONFIG_HOME/gridcraft/logs`
when set), `~/Library/Application Support/GridCraft/logs` on macOS and
`%APPDATA%\GridCraft\logs` on Windows. Each start moves the previous log to `gridcraft.1.log` and
that one to `gridcraft.2.log`, so the log of a run that crashed survives the next start; attach
them to a bug report. A log file stops growing at 16 MiB. By default GridCraft's own crates log
at `info` and everything else at `warn`; `RUST_LOG` replaces that with env_logger-style
directives, e.g. `RUST_LOG=debug` or `RUST_LOG=warn,gridcraft_engine=debug` (a trailing `*`
matches a prefix: `gridcraft*=debug`). Runs with `GRIDCRAFT_NO_PREFS` set (no saved settings)
log to standard error only.

## For agents: MCP, CLI and the control channel

```sh
claude mcp add gridcraft -- gridcraft-cli mcp                 # headless MCP server
gridcraft-cli mcp --connect 7979                               # MCP bridged to a running window
gridcraft-cli eval '=XLOOKUP("b",{"a","b"},{1,2})'             # → 2
gridcraft-cli run --sample budget --cmd 'home.bold={"range":"B4:F4"}' --out budget.xlsx
gridcraft-cli cat budget.xlsx --range B4:F15                   # aligned text table
gridcraft-cli commands --search chart                          # every command and its params
```

The MCP server offers tools such as `read_range`, `write_range`, `set_cell`, `evaluate_formula`,
`format_range`, `insert_chart`, `create_table`, `sort_range`, `filter` and `execute_command`
(which reaches every one of GridCraft's commands). The desktop app's control channel adds real
pointer and keyboard input, dialogs and screenshots. See [`docs/mcp.md`](docs/mcp.md),
[`docs/cli.md`](docs/cli.md) and [`docs/control-protocol.md`](docs/control-protocol.md).

## Architecture

GridCraft is an engine-first Cargo workspace with enforced layering (`cargo xtask layers`). The
egui frontend is a separate crate, so the UI can be swapped without touching the engine.

| Layer | Crates |
|---|---|
| L0 | `core` (addresses, values, errors, dates, input parsing) · `numfmt` (number format codes) |
| L1 | `formula` (lexer, parser, printer, reference adjustment) · `functions` (worksheet function library) |
| L2 | `model` (workbook, sheets, copy-on-write cells, styles, tables, charts…) · `calc` (dependency graph, evaluator, dynamic arrays) · `xlsx` (XLSX, CSV, plus XLSB and ODS data import) |
| L3 | `chart` (toolkit-free chart layout and rendering) |
| L5 | `engine` (session, commands, history, clipboard, fill, sort, filter, file I/O) |
| L6 | `ui-egui` (Excel-style UI, control channel) · `mcp` (MCP server) |
| L7 | `apps/gridcraft`, `apps/gridcraft-cli`, `apps/gridcraft-web` |

- **Contributor and agent rules** (clean-room, asset policy, never-crash, quality gates): [`AGENTS.md`](AGENTS.md)
- **Bundled assets:** each one is listed with its licence in [`ATTRIBUTION.md`](ATTRIBUTION.md)
- **Releases:** signed macOS, Windows, Linux, BSD and web builds; see [`docs/releasing.md`](docs/releasing.md)

## Roadmap

GridCraft is in **alpha**: the core workflow works end to end, but depth, fidelity and file
compatibility are still rough. It covers 89% of the Excel ribbon commands in our catalog
([`docs/parity-checklist.md`](docs/parity-checklist.md)) and 513 of Excel's 523 worksheet functions
([`docs/function-parity.md`](docs/function-parity.md)); weighted by what Excel users rely on, we
estimate it is about 50% ready for real work. Next up: XLSX fidelity on real-world files, very large
workbooks and multi-threaded recalc, chart depth, text in every script, and `.xls` import. Stage,
numbers and estimates are in [ROADMAP.md](ROADMAP.md); the ranked work list is [`docs/gaps.md`](docs/gaps.md).

## Downloads

**Download GridCraft** from GitHub: the [latest release](https://github.com/storytold/gridcraft/releases/latest) has every build listed below, and [all releases](https://github.com/storytold/gridcraft/releases) has earlier versions and their notes. `<ver>` in the file names is the version number, and `SHA256SUMS.txt` lists a checksum for every file.

### Windows

| Build | Installer | Portable |
|---|---|---|
| x64 (64-bit Intel/AMD) | `gridcraft-<ver>-windows-x64.msi` | `gridcraft-<ver>-windows-x64-portable.zip` |
| arm64 (Snapdragon and other ARM PCs) | `gridcraft-<ver>-windows-arm64.msi` | `gridcraft-<ver>-windows-arm64-portable.zip` |
| x86 (32-bit) | `gridcraft-<ver>-windows-x86.msi` | `gridcraft-<ver>-windows-x86-portable.zip` |

Installers and executables are code-signed. The MSI installer offers an optional desktop shortcut
(unchecked on a new installation).

**If the app doesn't open on Windows:** the desktop app initializes only DirectX 12 by default.
Letting wgpu also create an OpenGL instance can crash some graphics drivers (AMD's
`atio6axx.dll`) before the window appears, so the app would flash in Task Manager and quit.
`WGPU_BACKEND` overrides the default for troubleshooting (for example `dx12` or `vulkan`). In
PowerShell, from the folder containing the executable:

```powershell
$env:WGPU_BACKEND = "vulkan"
& .\gridcraft.exe
Remove-Item Env:WGPU_BACKEND                     # restore the default for later launches
```

An explicit `gl` override can bring the driver crash back on affected systems, and `vulkan` can
bring back a crash in some Intel UHD Graphics drivers (`igvk64.dll`, #120). The macOS, Linux and
web backend defaults are unchanged.

**If the app is slow on an older Windows PC, or DirectX 12 can't start:** when DirectX 12 finds no
graphics card with a driver for it, it only offers Microsoft's software renderer, which draws every
frame on the processor. In that case GridCraft uses OpenGL instead, without setting anything; if
the first renderer fails to start, it tries the other one once. The log file records the choice
(lines starting with `graphics:`). `WGPU_BACKEND` still overrides it (and then nothing else is
tried), e.g. `$env:WGPU_BACKEND = "gl"` or `"dx12"`.

DirectX 12 shaders are compiled with FXC, which is part of Windows, so no `dxcompiler.dll` or
`dxil.dll` is needed, and a copy another program put on `PATH` can no longer stop the app at start
("Parent device is lost", #339). `$env:WGPU_DX12_COMPILER = "dxc"` (or `"auto"`) selects wgpu's DXC
handling again for troubleshooting.

### macOS

| Build | File | Notes |
|---|---|---|
| App, universal (Apple silicon + Intel) | `gridcraft-<ver>-macos-universal.dmg` | Signed and notarized |
| Command-line tool, universal | `gridcraft-cli-<ver>-macos-universal.zip` | Signed and notarized |

### Linux

| Format | x86_64 | aarch64 (ARM64) | Notes |
|---|---|---|---|
| AppImage | `gridcraft-<ver>-linux-x86_64.AppImage` | `gridcraft-<ver>-linux-aarch64.AppImage` | Runs anywhere; updates itself with [AppImageUpdate](https://github.com/AppImageCommunity/AppImageUpdate) (`.zsync` files) |
| Flatpak | `gridcraft-<ver>-linux-x86_64.flatpak` | `gridcraft-<ver>-linux-aarch64.flatpak` | Sandboxed; `flatpak install --user <file>` |
| Debian/Ubuntu | `gridcraft-<ver>-linux-x86_64.deb` | `gridcraft-<ver>-linux-aarch64.deb` | |
| Fedora/RHEL/openSUSE | `gridcraft-<ver>-linux-x86_64.rpm` | `gridcraft-<ver>-linux-aarch64.rpm` | |
| Tarball | `gridcraft-<ver>-linux-x86_64.tar.gz` | `gridcraft-<ver>-linux-aarch64.tar.gz` | Unpack anywhere |

### FreeBSD

| Build | File |
|---|---|
| x86_64 | `gridcraft-<ver>-freebsd-x86_64.tar.gz` |

### Web (WebAssembly)

| Build | File | Notes |
|---|---|---|
| Static site | `gridcraft-web-<ver>.zip` | Runs in a modern browser; host it on any static server |

## The Crafting Apps

GridCraft is one of the **Crafting Apps**: free, open-source creative tools from the
[ArtCraft](https://getartcraft.com/) team, each written from scratch in Rust and each able to
stand on its own.

| | App | What it's for | Code | Learn more |
|:-:|---|---|---|---|
|  | **PhotoCraft** | Image editing: layers, masks, type and real PSD files | [GitHub](https://github.com/storytold/photocraft) | [Website](https://getartcraft.com/apps/photocraft) |
|  | **VectorCraft** | Vector illustration | [GitHub](https://github.com/storytold/vectorcraft) | [Website](https://getartcraft.com/apps/vectorcraft) |
|  | **FilmCraft** | Video editing, color and sound | [GitHub](https://github.com/storytold/filmcraft) | [Website](https://getartcraft.com/apps/filmcraft) |
|  | **LightCraft** | Photo library and raw development | [GitHub](https://github.com/storytold/lightcraft) | [Website](https://getartcraft.com/apps/lightcraft) |
|  | **PdfCraft** | Reading, organizing and protecting PDFs | [GitHub](https://github.com/storytold/pdfcraft) | [Website](https://getartcraft.com/apps/pdfcraft) |
|  | **EffectCraft** | Motion graphics and visual effects | [GitHub](https://github.com/storytold/effectcraft) | [Website](https://getartcraft.com/apps/effectcraft) |
|  | **DesignCraft** | Page layout and publishing | [GitHub](https://github.com/storytold/designcraft) | [Website](https://getartcraft.com/apps/designcraft) |
|  | **GridCraft** | **Spreadsheets and data · you are here** | [GitHub](https://github.com/storytold/gridcraft) | [Website](https://getartcraft.com/apps/gridcraft) |

And [**ArtCraft**](https://getartcraft.com/) itself, our AI image and video studio for artists who want real control.

Come make things with us

  Our Discord is where artists of every kind hang out: people who paint, shoot, draw, cut film,
  set type, and people still figuring out what they like to make. Share what you're working on,
  ask for help, tell us what's broken, or tell us what you wish these tools could do.
  Whatever your medium and however long you've been at it, you're welcome here.

  discord.gg/artcraft ·
  getartcraft.com ·
  The Crafting Apps ·
  GridCraft

## License and credits

GridCraft is dual-licensed under [MIT](LICENSE-MIT) or [Apache-2.0](LICENSE-APACHE), at your option.
Copyright (c) 2026 ArtCraft Team and the GridCraft contributors. Required notices are in [NOTICE](NOTICE).

Bundled fonts, icons, images and other assets keep their own open licenses; each one is listed
with its author, source and license in [ATTRIBUTION.md](ATTRIBUTION.md).

All UI icons are drawn in code and are original; the sample workbooks and every screenshot in
this README were made with GridCraft itself. GridCraft bundles no fonts: it uses the fonts
installed on your system.

The ArtCraft name, wordmark and logos in [`docs/brand/`](docs/brand/) are trademarks of the
ArtCraft Team and are not covered by this license. They may be used only unmodified, and only as
part of this repository and GridCraft, under [`docs/brand/LICENSE-brand.txt`](docs/brand/LICENSE-brand.txt).
Forks and modified versions must remove them.

Microsoft, Excel and Microsoft 365 are trademarks or registered trademarks of Microsoft Corporation in the United States and/or other countries. GridCraft is an independent, open-source project and is not affiliated with, sponsored by or endorsed by Microsoft Corporation; these names are used only to describe the workflows it is compatible with.

  Made by the ArtCraft team and community.

## 关联链接

- http://127.0.0.1:8771
- https://discord.gg/artcraft
- https://getartcraft.com/
- https://getartcraft.com/apps
- https://getartcraft.com/apps/designcraft
- https://getartcraft.com/apps/effectcraft
- https://getartcraft.com/apps/filmcraft
- https://getartcraft.com/apps/gridcraft
- https://getartcraft.com/apps/lightcraft
- https://getartcraft.com/apps/pdfcraft
- https://getartcraft.com/apps/photocraft
- https://getartcraft.com/apps/vectorcraft
- https://github.com/AppImageCommunity/AppImageUpdate
- https://github.com/storytold/designcraft
- https://github.com/storytold/effectcraft
- https://github.com/storytold/filmcraft
- https://github.com/storytold/gridcraft/releases
- https://github.com/storytold/gridcraft/releases/latest
- https://github.com/storytold/lightcraft
- https://github.com/storytold/pdfcraft
- https://github.com/storytold/photocraft
- https://github.com/storytold/vectorcraft
- https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white
- https://img.shields.io/badge/agents-MCP-1f9d55?style=flat-square
- https://img.shields.io/badge/license-MIT%20%2F%20Apache--2.0-147a40?style=flat-square

## 导航

- 项目页：[[10-项目/github.com_09a39e0a]]
- 渠道页：[[50-渠道/github_new]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
