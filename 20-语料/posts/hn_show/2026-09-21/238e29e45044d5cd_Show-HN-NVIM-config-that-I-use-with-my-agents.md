---
type: "corpus"
item_id: "238e29e45044d5cd"
title: "Show HN: NVIM config that I use with my agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47961215"
project_url: "https://github.com/NishantJoshi00/nvim-config"
author: "cat-whisperer"
published_at: "2026-04-30T12:04:35Z"
captured_at: "2026-09-21T02:52:27+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_cat-whisperer
  - story_47961215
  - show_hn
metrics: {"points": 5, "comments": 0, "engagement_velocity": 5}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: NVIM config that I use with my agents

> [!info] 一句话导读
> Published: 2022-11-04

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47961215>
> 指标：点赞=5 · 评论=0 · engagement_velocity=5
> 作者：cat-whisperer　|　发布：2026-04-30T12:04:35Z
> 项目链接：<https://github.com/NishantJoshi00/nvim-config>
> 采集：2026-09-21T02:52:27+08:00　|　id：`238e29e45044d5cd`

## 正文

Published: 2022-11-04

# Repository: NishantJoshi00/nvim-config

- Stars: 6
- Forks: 0
- Watchers: 1
- Open issues: 1
- Primary language: Lua
- Languages: Lua
- License: Apache License 2.0 (Apache-2.0)
- Topics: config, setup
- Default branch: main
- Created: 2022-11-04T19:56:50Z
- Last push: 2026-05-04T11:29:36Z
- Contributors: 1 (top: NishantJoshi00)
- Releases: 4
- Latest release: v0.4.0 (2026-04-01T04:39:33Z)

---

# Neovim Configuration

## Overview

A modular Neovim configuration with 80+ plugins, built for performance using lazy.nvim and event-driven loading. Features comprehensive LSP integration, cross-platform support, and a clear separation between core configuration, plugins, and keybindings.

**Architecture:**

- Modular design with dedicated directories for plugins, configs, and keybinds
- Event-driven lazy loading using `event = "VeryLazy"` and file-type triggers
- Platform-specific customizations for Linux, macOS, and Windows
- Strict initialization order: bootstrap → theme → plugins → config → mappings
- Mason-managed LSP servers, formatters, and linters

**Tested on:**

- Neovim v0.11.2+ (requires Neovim 0.10+)
- macOS (Darwin 24.2.0)
- 80+ plugins tested and configured for stability

## Installation

1. Ensure Neovim 0.10+ is installed

1. Back up existing configuration:

```bash
   mv ~/.config/nvim ~/.config/nvim.bak
   ```

1. Clone this repository:

```bash
   # Linux/macOS
   git clone https://github.com/NishantJoshi00/nvim-config.git ~/.config/nvim

# Windows (PowerShell)
   git clone https://github.com/NishantJoshi00/nvim-config.git $env:LOCALAPPDATA\nvim
   ```

1. Install dependencies:

- Git (plugin management)
 - C compiler (certain plugins require compilation)
 - Node.js (LSP features)
 - Ripgrep (telescope search)
 - Nerd Font (icon rendering)

1. Launch Neovim. The configuration will automatically:

- Install lazy.nvim plugin manager
 - Download and configure all plugins
 - Set up LSP servers via Mason

## Features

**Core Capabilities:**

- LSP integration with nvim-lspconfig and Mason
- Multi-source completion via nvim-cmp (LSP, buffer, path, snippets)
- Git integration with gitsigns, vim-fugitive, and diffview
- File navigation using Telescope, nvim-tree, and oil.nvim
- TreeSitter syntax highlighting and code analysis
- Terminal integration via toggleterm.nvim
- Session management with persistence.nvim
- Enhanced diagnostics with lsp_lines and virtual text

**Language Support:**

- Rust (rustaceanvim with enhanced tooling)
- Haskell (haskell-tools.nvim)
- Zig (zig.vim)
- Lua (lazydev.nvim for Neovim API development)
- TLA+ (vim-tla for specifications)
- General purpose via Mason LSP management

**Key Bindings:**

- Leader key: ` `
- Consistent namespacing: ` f*` (find/file), ` g*` (git), ` m*` (misc)
- Plugin-specific bindings isolated in `lua/plugins/keybinds/`

## Project Structure

```
.
├── init.lua                # Entry point with strict loading order
├── lua/
│   ├── bootstrap.lua       # lazy.nvim setup (auto-installs if missing)
│   ├── theme.lua          # Core vim options (loaded before plugins)
│   ├── config.lua         # LSP setup, diagnostics, autocmds
│   ├── mappings.lua       # Keybinding loader
│   ├── functions.lua      # Utility functions
│   ├── plugins/
│   │   ├── init.lua       # Plugin specifications (80+)
│   │   ├── config/        # Plugin configurations (return functions)
│   │   └── keybinds/      # Plugin keybindings (return functions)
│   ├── custom/
│   │   ├── init.lua       # Platform-specific loader
│   │   └── os/            # OS-specific configurations
│   └── functions/
│       └── up-to-date.lua # Auto-update checking
└── docs/
    └── plugins.md         # Complete plugin catalog
```

## Development Workflow

**Adding New Plugins:**

1. Add plugin specification to `lua/plugins/init.lua`:

```lua
   {
       "author/plugin-name",
       event = "VeryLazy",
       dependencies = { ... },
       config = require("plugins.config.plugin-name"),
   }
   ```

1. Create configuration in `lua/plugins/config/plugin-name.lua`:

```lua
   return function()
       require("plugin-name").setup({ ... })
   end
   ```

1. Create keybindings in `lua/plugins/keybinds/plugin-name.lua`:

```lua
   return function()
       vim.keymap.set("n", "<leader>xx", function() ... end, { desc = "..." })
   end
   ```

1. Load keybindings in `lua/mappings.lua`:

```lua
   require("plugins.keybinds.plugin-name")()
   ```

1. Test with `:Lazy reload plugin-name`

**Debugging Tools:**

- `:checkhealth` - Verify installation and plugin health
- `:Lazy profile` - Analyze startup performance
- `:TSCaptureUnderCursor` - Debug TreeSitter highlighting
- `:LuaToBuffer ` - Execute Lua and append output to buffer
- `require("functions").point_search()` - Navigate to file:line:col

## Documentation

[Complete Plugin Catalog](docs/plugins.md) - All 80+ plugins organized by category with GitHub links and descriptions.

## Contributing

1. Fork the repository and create a feature branch
2. Follow the modular architecture:

- Plugin configs return functions for lazy loading
 - Use consistent leader key namespacing
 - Maintain separation between config and keybinds

1. Test changes:

- Run `:checkhealth` to verify plugin health
 - Run `:Lazy profile` to check performance impact
 - Ensure no startup errors with `:messages`

1. Submit a pull request with clear description

# From Linear to Lanes: A Two-MCP Workflow

## 关联链接

- https://github.com/NishantJoshi00/nvim-config.git

## 导航

- 项目页：[[10-项目/github.com_2cf6a0fe]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
