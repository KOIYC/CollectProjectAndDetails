---
type: "corpus"
item_id: "1e02748dd7df65ba"
title: "Show HN: Emacs user are you waiting for mg to get UTF-8?"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49123268"
project_url: "https://github.com/nicholascarroll/emil"
author: "emil_coder"
published_at: "2026-07-31T14:02:30Z"
captured_at: "2026-09-21T03:11:07+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-07-31"
tags:
  - 语料
  - hn_show
  - author_emil_coder
  - story_49123268
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: Emacs user are you waiting for mg to get UTF-8?

> [!info] 一句话导读
> nicholascarroll/emil

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49123268>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：emil_coder　|　发布：2026-07-31T14:02:30Z
> 项目链接：<https://github.com/nicholascarroll/emil>
> 采集：2026-09-21T03:11:07+08:00　|　id：`1e02748dd7df65ba`

## 正文

# nicholascarroll/emil

Minimalist, Emacs-style text editor for the terminal

- Stars: 4
- Forks: 0
- Watchers: 4
- Open issues: 7
- License: MIT License
- Default branch: main
- Created: 2025-06-13T12:53:51Z
- Fork: yes

## Languages

- C
- Makefile
- Roff
- Shell

## Top Contributors

- japanoise (169 contributions)
- nicholascarroll (68 contributions)
- ScoreUnder (2 contributions)

---

## README

# emil (埃米尔)

OpenSSF Best Practices

`emil` is a small, portable text editor for UTF-8 files, providing a core subset of emacs commands in the terminal.

Written in standard C99, `emil` runs on any system providing a minimal POSIX.1-2001 interface (single-process subset) and a VT100-compatible terminal. It eschews common sources of complexity: scripting, plugins, configuration files, background network activity, or auto-save files.

## Functional Capabilities

- Visual text selection
- Edit rectangular text regions
- Kill ring ('clipboard history')
- Snippets (as session local registers)
- Incremental regex search and replace
- Keystroke macros
- Shell integration
- Word wrap
- Split windows
- Mark ring
- Bookmarks (as session local registers)
- Jump to symbol definition (Ctags)

## Installation

**Unix / Linux / macOS**

```bash
make && sudo make install
```

**Android (Termux)**
- Excludes shell integration.

```bash
make android
```

**Git for Windows / MSYS2**
- Run in an **MSYS2** terminal (not mingw64, which lacks termios).
- Install compilers and libraries:

```bash
pacman -S msys2-devel msys2-runtime-devel
```

* Build and install:

```bash
make && make install
```

### Internationalization Support

`emil` edits text in any any left-to-right script encoded in valid UTF-8. Right-to-left scripts such as Arabic and Hebrew are not supported.

Application messages and the man page can be set to a supported language at build time. Default is English. Other languages supported are:

| Language | CFLAG | Man Dir |
| ------------------------ | ------------ |-------- |
| Chinese (Simplified) | EMIL_LANG_ZH | zh |
| Spanish (Latin American) | EMIL_LANG_ES | es |

To build (for example, Spanish):

```bash
make CFLAGS="-DEMIL_LANG_ES"
sudo make install MAN_SOURCE=emil.es.1 MAN_SUBDIR=es
```
and to uninstall:

```
sudo make uninstall MAN_SUBDIR=es
```

## Getting Started

Open a file:

```
emil file.txt
```

### Essential Commands

| Action | Command |
| ---------------------- | ------------------- |
| Open file | `Ctrl-x Ctrl-f` |
| Save file | `Ctrl-x Ctrl-s` |
| Quit emil | `Ctrl-x Ctrl-c` |
| Mark (to select text) | `Ctrl-SPACE` |
| Cut | `Ctrl-w` |
| Copy | `Alt-w` or `Ctrl-c` |
| Paste | `Ctrl-y` |
| Undo | `Ctrl-_` |
| Search | `Ctrl-s` |
| Cancel | `Ctrl-g` |

For the complete command reference, see the man page:

```
man emil
```

## Shell-Oriented Editing

`emil` is designed to be used with the shell set to *emacs-mode* [^1] .
In Bash the mode is set in the user's `~/.bashrc`:

```bash
set -o emacs
```
An entry in `~/.inputrc` is usually also needed for the copy and kill keybindings:

```inputrc
$include /etc/inputrc          # retain system-wide defaults
set bind-tty-special-chars off

"\C-w": kill-region
"\ew": copy-region-as-kill 
```

### Shell Integration

Shell integration is a compile-time option (enabled by default). It enables shell commands to be used on the buffer:

- **`Alt-|`**
 Takes the current region, feeds it to the shell command you type, and **displays the output** in a `*Shell Output*` buffer.

- **`Ctrl-u Alt-|`**
 Takes the current region, feeds it to the shell command, and **replaces the region** with the output of the command.

- **`Alt-!`**
 Enter a shell command in the minibuffer and the output displays in *Shell Output*.

- **`Alt-x diff-buffer-with-file`**
 Shows unsaved changes.

Shell integration can be disabled at build time with the compiler flag `-DEMIL_DISABLE_SHELL`.

#### Example uses of Shell Integration

Below are common "recipes" using standard Unix utilities.

| Task | Command | Keys To Use |
| ---------------------- | --------------------- | --------------------------- |
| **Fill region** | `fmt` | `Ctrl-u Alt-\|` |
| **Sort lines** | `sort` | `Ctrl-u Alt-\|` |
| **Align columns** | `column -t` | `Ctrl-u Alt-\|` |
| **Align text table** | `column -t -s '\|'` -o '\|' | `Ctrl-u Alt-\|` |
| **Number lines** | `cat -n` | `Ctrl-u Alt-\|` |
| **Word count** | `wc` | `Alt-\|` |
| **Solve math** | `bc` | `Alt-\|` or `Ctrl-u Alt-\|` |
| **Format JSON** | `jq .` | `Alt-\|` or `Ctrl-u Alt-\|` |
| **Find typos** | `aspell list` | `Alt-\|` |
| **Format C code** | `make format` | `Ctrl-u Alt-\|` |
| **Lint shell script** | `shellcheck` | `Ctrl-u Alt-\|` |
| **Trim whitespace** | `sed 's/[[:space:]]\+$//'` | `Ctrl-u Alt-\|` |
| **De-duplicate lines** | `awk '!seen[$0]++'` | `Ctrl-u Alt-\|` |

### Shell Drawer
`Ctrl-x Ctrl-z` suspends `emil` while preserving the current editor screen. This permits shell commands to be executed in the terminal below the editor content, after which editing may be resumed with `fg`.

Notes:
 - `less` clears the terminal when it quits; `less -X` and `more` do not.
 - The named command `cd` (change directory) in `emil` does not also change the directory in the shell.

## System Clipboard Integration
`Ctrl-c` copies selected text to both the kill ring and the user's system clipboard when an OSC 52 enabled terminal client is used.

OSC 52 has a protocol limit of 74,993 bytes. Selections larger than this are not
sent to the clipboard and a status message is displayed. Some terminal emulators
have lower limits and will silently fail after writing only the first part of the
text to the system clipboard.

## Editing Large Files

`emil` is not designed for editing very large files. Files larger than 1 GB cannot be opened.

## Internals

Each buffer is an array of logical lines (`erow`) holding raw UTF-8 bytes. All buffers contain valid UTF-8 exclusively; files that fail validation are rejected at load time. The buffer is never modified by rendering or text layout concerns.

Display widths are cached per-row and recomputed only when a row is edited. A cumulative screen-line cache maps logical rows to screen positions, enabling efficient scrolling when word wrap is active.

On each frame, the renderer reads raw bytes from the buffer and emits terminal-ready sequences directly into an append buffer. No intermediate render buffers exist. The append buffer is written to the terminal in a single `write()` call, then truncated.

The rendering system uses only cursor positioning (CSI H), erase-to-end-of-line (CSI K), reverse video (CSI 7m / CSI 0m), and clear-below (CSI J).

All input is processed in a single loop:

1. Read keystroke
2. Execute command (may modify buffer)
3. Refresh screen: clamp window offsets, rebuild caches if stale, scroll, redraw, flush

## Contributing

Bug fixes, portability improvements, performance work, and general code quality
PRs are welcome. Please do not propose any new features.

## Credits and License

emil is a derivative of `japanoise/emsys` and is not affiliated with the Free Software Foundation or the GNU Project.
Distributed under the MIT License.

---

[^1]: Omitted from POSIX.1, see Rationale.

## 导航

- 项目页：[[10-项目/github.com_d693d2f6]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
