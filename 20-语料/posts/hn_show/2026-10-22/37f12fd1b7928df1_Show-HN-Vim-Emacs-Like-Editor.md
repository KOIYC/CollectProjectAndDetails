---
type: "corpus"
item_id: "37f12fd1b7928df1"
title: "Show HN: Vim/Emacs Like Editor"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50180100"
project_url: "https://github.com/getkalem/kalem"
author: "mhmtarif"
published_at: "2026-10-21T12:54:48Z"
captured_at: "2026-10-22T09:46:18+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-22"
pub_day: "2026-10-21"
tags:
  - 语料
  - hn_show
  - author_mhmtarif
  - story_50180100
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Vim/Emacs Like Editor

> [!info] 一句话导读
> License: Apache License 2.0

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50180100>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：mhmtarif　|　发布：2026-10-21T12:54:48Z
> 项目链接：<https://github.com/getkalem/kalem>
> 采集：2026-10-22T09:46:18+08:00　|　id：`37f12fd1b7928df1`

## 正文

# getkalem/kalem

- Stars: 30
- Forks: 1
- Watchers: 30
- Open issues: 9
- License: Apache License 2.0
- Homepage: https://getkalem.github.io/kalem/
- Default branch: main
- Created: 2026-09-28T15:10:48Z

## Languages

- CSS
- Emacs Lisp
- Fluent
- HTML
- JavaScript
- Python
- Rust
- Shell
- TeX
- Typst

## Top Contributors

- mhmtskrc2 (1106 contributions)
- claude (321 contributions)

---

## README

 Kalem

 One fast editor for all the files of your work, instead of one program per format. Written in Rust. In a window and in a terminal.

Kalem (Turkish for "pen") shows a file the way it reads and never touches what you did not edit. A Markdown, Org, LaTeX or CSV file opens as what it is, a document or a grid, and under it the file stays plain text, byte for byte. PDF files, pictures and Excel workbooks open in viewers next to your documents, plugins installed the first time you open such a file; every other text file opens as code. A format Kalem does not know yet is a plugin away, written in Rust: you read and edit it here too, in the same editor.

**Status: alpha.** It is in daily use, and it has rough edges. The current release installs below. An issue with the file that went wrong, when you can share it, helps most.

> [!IMPORTANT]
> **Please update now and then.** Kalem is under heavy development, and new releases with fixes come out often. Run the install command again to get the latest Kalem; in the editor, *Browse Plugins* offers an update for each plugin that has a newer release.

## Why Kalem

- **Every file as itself, and the file stays yours.** Kalem never converts a file to open it (workbooks in `.ods`, `.xls` or `.xlsb` are the one exception, below), writes nothing into a file that its format does not define, and shows what it does not understand as the source it is. It edits the text in place and saves only what you changed, byte for byte: no database, no import, no "save as", no account, no cloud. Open the file in another editor, or in `git diff`, and you see only your edits.
- **Checked against the reference, on thousands of files.** Org against Emacs itself; LaTeX on 925 arXiv papers and 21 real projects, the HoTT book and the Stacks project among them; Markdown on every example of the CommonMark and GFM test suites; CSV on LibreOffice's files and, for reading, quoting and editing, against Rust's `csv` crate on thousands of random files. On the way the project wrote the specification LaTeX never had: LaTeX as written.
- **Fast.** Kalem is written in Rust: one binary, nothing else to install, no scripting engine. A keystroke in a paragraph reparses it in a twentieth of a millisecond. The measurements give every number with the command that reproduces it.
- **One editor, in a window and in a terminal.** The same documents, commands and keys in the graphical editor and in `kalem tui`, over SSH too. A document's checks, formatting and exports are also commands on the command line: `kalem check`, `kalem fmt`, `kalem export`.
- **Vim keys from the start, menus all the same.** Vim's modes, motions, operators, registers, macros and command line are built in, checked against Vim itself, and on from the first start; one setting gives the keys most editors use instead. Either way a menu bar, a toolbar, right-click menus, a command palette and the mouse reach every command, in the terminal too.
- **Plugins in Rust, not JavaScript.** A plugin is compiled Rust, run as a WebAssembly component with its own memory, a time budget and only the permissions it declares. Plugins run fast, and a plugin cannot freeze the editor or take it down.

## Documents

Five formats are built into the core, each with a chapter in the Book's Part II that says exactly what Kalem reads, shows, edits and writes, and against what it is tested.

| File | What you see |
|---|---|
| `.md`, `.markdown`, `.mdown`, `.mkd`, `.gfm` | A document, GitHub flavor: headings, lists, task lists, tables with formulas, front matter, wiki links, pictures. Markers hide away from the cursor and come back when you reach them. A folder of notes with wiki links between them works as a project. |
| `.org` | A document: folding, TODO states, dates, tags, tables with formulas, footnotes, citations, typeset formulas. Export to HTML, Markdown, LaTeX, PDF and text as Emacs does; Word, OpenDocument and EPUB through pandoc, and `kalem import` brings Word, OpenDocument, HTML, EPUB and RTF files in as Org the same way. |
| `.tex`, `.latex`, `.ltx` | A document: numbered sections, typeset formulas, references, citations, figures; what Kalem does not understand stays as source. Build the PDF with the errors at their lines, and Ctrl-click a line of the PDF to go back to the source. |
| `.csv`, `.tsv`, `.tab` | A grid: sorting, filters, a record view, column statistics. Only the fields you edit are written. |
| `.bib` | A grid of entries. |
| Anything else | Code with highlighting. |

Around them: a file manager, projects, find in files, a command palette, an outline, split views, themes, and the interface in English and Turkish.

 A Markdown note and the Org guide; a LaTeX article and a CSV file.

## Viewers and plugins

Files that are not text open through plugins of getkalem/plugins, none of them built into Kalem: the first time you open a PDF, a picture or a workbook, Kalem names the plugin that opens it and installs it if you choose, then opens the file (`kalem plugin install xlsx` installs one ahead of time). So you do not leave the editor to look at the files next to your document:

| File | What you see |
|---|---|
| `.pdf` | Pages, zoom, search, text selection, the outline, links; a password when the file asks for one. |
| Pictures | PNG, JPEG, GIF, WebP, TIFF and a dozen more: fit, zoom, rotate, next and previous in the folder. In the terminal too, where the terminal draws pictures (kitty, Ghostty, WezTerm, iTerm2, Sixel). An SVG file, being text, opens as its XML; it shows as a picture where a document links it. |
| `.xlsx`, `.xlsm`, `.xltx`, `.xltm` | Sheets as grids with their formulas, styles, charts and pivot tables, edited and saved as the same file; a save asks Excel to recalculate when it opens the file. An `.ods`, `.xls` or `.xlsb` workbook is converted as it opens: saving it back in its own format asks first, and Save As `.xlsx` leaves the original alone. |

 The PDF built from the article, and a workbook with its formulas and its chart.

Programming languages come as plugins too: the syntax, and a language server for diagnostics, completion, hover, rename, code actions and formatting. Today there are Elixir (with Expert or ElixirLS) and Rust (with rust-analyzer); more follow. Other plugins bring git into the editor, and open Logseq graphs and Obsidian vaults as themselves. *Browse Plugins* in the editor lists them all with what each does, and installs the one you choose (Install shows it).

If your format is not here, a plugin adds it: `kalem plugin browse` lists the plugins of the index, and `kalem plugin new` starts your own, in Rust. The plugins live in getkalem/plugins; the Book's Part III has the contract.

## From Emacs, for everyone

Kalem's author used Emacs for many years. Emacs got a lot right: its packages are open code that hundreds of people refined over decades, and some of them became very good, Dired, Magit, Projectile and Org mode among them. But Emacs is made for programmers, everything hides behind key chords, and everything runs on one thread of Lisp, so one busy package stalls the whole editor. Kalem takes the parts that worked best and builds them into its core, not on top, as an everyday program for everyone:

- **Org mode**, compared with Emacs command by command.
- **A file manager**, as Dired: a folder as a page of text, every file with its size and date. Open a file, rename it by editing its name, copy, move or trash it, select many at once; Ctrl+Alt+D lists the document's folder with the cursor on its file.
- **Projects**, as Projectile has them: each piece of your work kept apart. Any file of the project opens by a few letters of its name (Ctrl+P), a search goes through all of it (Ctrl+Shift+F), and another project is one step away.
- **Leader keys** with the Vim keys, in Doom Emacs's layout: Space is the leader, `SPC p p` switches the project, and a panel shows what can follow a prefix, as which-key does.

 The file manager, the projects view, and the settings panel with its lazygit-like keys.

You do not need to be an Emacs user: the interface most people know is there, a menu bar, tabs, a folder tree, a command palette, right-click menus. Kalem starts with Vim's keys; one choice in the settings gives the keys most editors use, Ctrl+S and typing straight into the text (below). Every setting, the plugins' included, is changed in a settings panel (Cmd+, on macOS, `SPC h v` with the Vim keys, Ctrl+, with the Word-like ones): a switch flipped or the next choice picked in place, with lazygit's keys in the terminal, nothing typed into a file. The panel saves to `settings.toml`, and `keymap.json` changes any key. What Kalem leaves out is Elisp: there is no scripting engine. The Book's Kalem and Emacs says what is taken, what is left out, and why.

For Emacs and Vim hands: the Vim keys are the default (`editor.keymap_profile = "vim"`), and every key of Doom's leader map is listed with what it does in Kalem (Keys); the file manager has Dired's keys (The file manager); `docs/keymaps/emacs.json` is a complete keymap with Org mode's Emacs keys to copy from.

## Install

On macOS and Linux:

```bash
curl --proto '=https' --tlsv1.2 -LsSf https://github.com/getkalem/kalem/releases/latest/download/kalem-editor-installer.sh | sh
```

On Windows, in PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -c "irm https://github.com/getkalem/kalem/releases/latest/download/kalem-editor-installer.ps1 | iex"
```

Run the same command again now and then to update: Kalem is under heavy development, and new releases with fixes come out often.

The installers put `kalem` in `~/.cargo/bin`; delete it there to uninstall. The release also has terminal-only archives (`kalem-terminal-*`) for servers, without the graphical editor; installed plugins and viewers run there too. The Book's Installing has the details: glibc 2.35 or later on Linux, the three libraries the graphical editor needs there (`sudo apt install libxcb1 libxkbcommon0 libxkbcommon-x11-0`; without them `kalem` opens in the terminal), the unsigned `Kalem.app` on macOS, and the libraries a build from source needs.

From source, with Rust 1.96 or later:

```bash
git clone https://github.com/getkalem/kalem && cd kalem
cargo install --locked --path crates/kalem
```

```bash
kalem notes.md                      # the editor; `kalem tui notes.md` for the terminal
kalem export notes.org --to html    # the command-line tools: check, fmt, query, export…
```

Kalem starts with Vim's keys: Normal mode first, `i` to type, `:w` to save. For the keys most editors use instead (typing goes straight into the text, Ctrl+S saves, Cmd+S on macOS), choose `word` for `editor.keymap_profile` in the settings panel, or write it in `settings.toml`:

```toml
[editor]
keymap_profile = "word"
```

Kalem's core opens Org, Markdown, LaTeX, CSV and BibTeX files, and every other text file as code. The rest comes as plugins you add when you want them: viewers for PDF files, pictures, workbooks and Word documents, programming languages, git, note graphs. In the editor, *Browse Plugins* in the *Kalem* menu or the command palette lists the plugins of the index; choose one, and Kalem says what it is, where it comes from and what it may do, then installs it when you confirm. On the command line, `kalem plugin browse` lists them and `kalem plugin install NAME` installs one.

 Browse Plugins: every plugin of the index, with its version and what it does.

Settings live in `~/.config/kalem` on Linux and macOS (`$XDG_CONFIG_HOME/kalem` if it is set) and in `%APPDATA%\kalem` on Windows; the log and crash reports in `~/.local/state/kalem`, or `%LOCALAPPDATA%\kalem`. `KALEM_CONFIG_DIR` and `KALEM_STATE_DIR` move them, and `KALEM_LOG=debug` makes the log say more.

## Not yet

- The Org agenda.
- Language plugins beyond Elixir and Rust.
- Signed installers and a macOS app in the release; a Windows MSI; Linux AppImage and Flatpak packages.

## Limits

- Markdown: export, printing and `kalem fmt` are for Org and LaTeX; TOML front matter (`+++`) and `$$` blocks over several lines show as text.
- LaTeX: building a PDF needs TeX Live, MiKTeX or Tectonic installed; Kalem does not download one.
- The terminal-only build draws an SVG picture without its text.
- Line endings and a byte order mark stay as the file has them; there is no command to change them yet.
- An `.ods`, `.xls` or `.xlsb` workbook is converted to be edited, and a workbook with a password to open is saved as `.ods` without its encryption.

## More

- The Kalem Book: the manual, and what Kalem does with each format.
- Contributing, the design documents and task list, the changelog.
- License: MIT or Apache-2.0, at your option.

## 关联链接

- https://getkalem.github.io/kalem/
- https://github.com/getkalem/kalem/releases/latest/download/kalem-editor-installer.ps1
- https://github.com/getkalem/kalem/releases/latest/download/kalem-editor-installer.sh

## 导航

- 项目页：[[10-项目/github.com_a5a8a679]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
