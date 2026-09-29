---
type: "corpus"
item_id: "29c8d6426d5176a6"
title: "Show HN: Beside.nvim – Live preview in Neovim using leaf, glow or pandoc"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49879004"
project_url: "https://github.com/mariocesar/beside.nvim"
author: "mariocesar"
published_at: "2026-09-28T14:54:27Z"
captured_at: "2026-09-29T09:42:55+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-29"
pub_day: "2026-09-28"
tags:
  - 语料
  - hn_show
  - author_mariocesar
  - story_49879004
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Beside.nvim – Live preview in Neovim using leaf, glow or pandoc

> [!info] 一句话导读
> mariocesar/beside.nvim

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49879004>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：mariocesar　|　发布：2026-09-28T14:54:27Z
> 项目链接：<https://github.com/mariocesar/beside.nvim>
> 采集：2026-09-29T09:42:55+08:00　|　id：`29c8d6426d5176a6`

## 正文

# mariocesar/beside.nvim

A live rendering of the document you are editing, in a split beside it: leaf, glow, pandoc or any renderer you add

- Stars: 16
- Forks: 0
- Watchers: 16
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-09-26T18:09:21Z

## Languages

- Lua
- Makefile

## Topics

- asciidoc
- glow
- live-preview
- lua
- markdown
- neovim
- neovim-plugin
- org-mode
- pandoc
- preview
- rst
- typst

## Top Contributors

- mariocesar (34 contributions)
- dependabot[bot] (2 contributions)

---

## README

# beside.nvim

A live rendering of the document you are editing, in a split beside it. The
preview follows your cursor, scrolling the preview scrolls the source, and it
re-renders as you type. Rendering is done by a terminal renderer you already
have: leaf, glow, pandoc or carve, see Supported renderers.

Editing a markdown document with its leaf rendering beside it; scrolling either side scrolls the other
*Markdown rendered by leaf. Moving in either side scrolls the other.*

## Why another preview

The existing previews are each tied to one renderer, and some need node or a
browser. I like glow's output for some documents and leaf's for others, so
beside runs whichever renderer is installed and lets you switch with
`:Beside glow`. In-buffer renderers like render-markdown.nvim are a
different thing and work fine alongside it.

## Supported renderers

| Renderer | Renders | Install |
| --- | --- | --- |
| leaf | Markdown | github.com/RivoLink/leaf |
| glow | Markdown | github.com/charmbracelet/glow |
| pandoc 3.1.10+ | Markdown, reStructuredText, AsciiDoc, Org, Textile, Typst, Djot | pandoc.org/installing |
| carve | Carve | markup-carve.github.io/carve/get-started |

Markdown tries leaf, then glow, then pandoc; the first one installed renders.
Any other renderer is one table entry away, see
Adding a renderer. When someone creates the next great
markup language, beside will be ready for it!

A reStructuredText document rendered by pandoc
*reStructuredText rendered by pandoc.*

A Carve document rendered by carve
*Carve rendered by carve.*

## Requirements

- Neovim 0.10 or newer
- At least one of the supported renderers on `$PATH`.
 `:checkhealth beside` shows which are found and what each filetype would be
 rendered with.

## Install

With lazy.nvim:

```lua
{ 'mariocesar/beside.nvim', cmd = 'Beside', opts = {} }
```

`setup()` is optional; the defaults below apply without it. `:h beside` has
the full documentation.

## Use

`:Beside` toggles the preview for the current buffer. `:Beside glow` opens it
with that renderer, or switches to it; renderer names complete. While the
preview is open:

- moving or scrolling in the source keeps the preview at the same place, and
 scrolling the preview scrolls the source
- edits re-render 100 ms after you stop typing, unsaved
- opening another document in the same tab moves the preview to it; when no
 window shows the document any more, the preview closes
- `q` in the preview closes it

Switching the preview from leaf to glow with :Beside glow
*`:Beside glow` switches the preview from leaf to glow.*

## Configuration

The defaults:

```lua
require('beside').setup({
  -- Preview width: fraction of the screen, or a column count when 2 or more
  width = 0.4,

  -- Milliseconds after the last change before re-rendering
  delay = 100,

  -- Renderers to try first, per filetype. Any other renderer declaring the
  -- filetype follows, by name; the first one installed renders.
  prefer = {
    markdown = { 'leaf', 'glow', 'pandoc' },
  },

  -- Renderers by name; the builtins are leaf, glow, pandoc and carve
  renderers = require('beside.renderers'),
})
```

User entries deep-merge into the defaults, so an option is set with
`renderers = { glow = { style = 'dracula' } }` and a filetype's order is
replaced with `prefer = { markdown = { 'glow' } }`.

### Adding a renderer

A renderer is a table with the filetypes it renders and a function building
the command that renders stdin to ANSI-colored text on stdout:

```lua
require('beside').setup({
  renderers = {
    mdcat = {
      filetypes = { markdown = true },
      command = function(context)
        return { 'mdcat', '--columns', tostring(context.width), '-' }
      end,
    },
  },
})
```

- `filetypes` maps each filetype to the format name the command needs, or to
 `true` when that is the filetype itself. pandoc's entry maps `markdown` to
 `gfm`, for example.
- `command(context)` returns the argv. `context` has `filetype`, `format` (what
 `filetypes` maps it to), `width` (columns to render at), `background`
 (`light` or `dark`) and `renderer` (the entry itself, with any user options
 merged in).
- `env`, optional, is extra environment for the command.
- `executable`, optional, is what must be on `$PATH`; the renderer's name by
 default.

The same shape is what `lua/beside/renderers.lua` uses for the builtins, so a
renderer worth sharing is a pull request adding an entry there; see
CONTRIBUTING.md.

### Per filetype

A buffer can override the settings in `vim.b.beside_config`, a table of the
same shape. Set one in `after/ftplugin/.lua` to configure a filetype:

```lua
-- after/ftplugin/rst.lua
vim.b.beside_config = { prefer = { rst = { 'pandoc' } }, width = 0.5 }
```

Buffer variables cannot hold functions, so renderers themselves are added in
`setup()`.

## How the sync works

Renderers change the line count: a table becomes a box, a paragraph wraps, a
code block grows a frame. There is no line-for-line map, so beside matches the
text of each source line to the rendered output and interpolates between
matches. Headings, list items, code lines and table cells anchor exactly;
inside a wrapped paragraph the preview lands within a line or two.

## Contributing

Bug reports, fixes and new renderers are welcome. CONTRIBUTING.md
covers the dev setup, adding a renderer with its demo tape, and the renderer
quirks worth knowing about.

## License

MIT

# PragmaTwice/jeva.cpp

## 导航

- 项目页：[[10-项目/github.com_912252dc]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
