---
type: "corpus"
item_id: "464fa68b9c7e12f9"
title: "Show HN: Cutesy HTML Formatter and Linter"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50279383"
project_url: "https://github.com/chasefinch/cutesy"
author: "chasefinch"
published_at: "2026-10-28T19:20:20Z"
captured_at: "2026-10-29T20:41:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-29"
pub_day: "2026-10-28"
tags:
  - 语料
  - hn_show
  - author_chasefinch
  - story_50279383
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Cutesy HTML Formatter and Linter

> [!info] 一句话导读
> A linter & formatter for clean HTML code, or else. 🥰

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50279383>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：chasefinch　|　发布：2026-10-28T19:20:20Z
> 项目链接：<https://github.com/chasefinch/cutesy>
> 采集：2026-10-29T20:41:52+08:00　|　id：`464fa68b9c7e12f9`

## 正文

# chasefinch/cutesy

A linter & formatter for clean HTML code, or else. 🥰

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 31
- License: Apache License 2.0
- Default branch: main
- Created: 2022-07-09T01:11:17Z

## Languages

- HTML
- Makefile
- Python
- Ruby
- Rust

## Topics

- alpinejs
- django-templates
- formatter
- html
- htmx
- jinja2
- linter
- tailwindcss

## Top Contributors

- chasefinch (338 contributions)
- dependabot[bot] (101 contributions)

---

## README

# Cutesy 🥰

A cute little HTML linter, until y̵ou ma̴k̵e i̴͌ͅt̴̖̀ a̵̤̤͕̰͐̅͘͘n̶̦̣͙̑̌̆̄ǵ̷̗̗̀͝r̷̭̈́͂͘ẙ̶͔̟̞̊̈…̴̢͘

**Cutesy reformats & lints HTML documents**, including HTML templates. It ensures consistent indentation, line breaks, and formatting while automatically fixing most issues.

## First-class support for your favorite frameworks ❤️

- Full support for Django templates 🐍💕
- Sorts classes for TailwindCSS 💖✨
- Works with AlpineJS and HTMX ⚡💘

## Features ✨

- **Auto-fix**: Automatically corrects most formatting issues
- **Configurable**: Extensive configuration options for your project's needs
- **Fast**: Rust core for high performance

## Status

Build Status Coverage: 92% PyPI - Version

## Table of Contents

- Quick Start
- Installation
- Basic Usage
- Configuration
- Framework Support
- Examples
- Documentation
- When to Use Cutesy
- Benefits
- Badge
- License
- Contributing

## 🚀 Quick Start

**Install:**
```bash
pip install cutesy
```

**Format your HTML files:**
```bash
cutesy "*.html" --fix
```

**For Django projects with TailwindCSS:**
```bash
cutesy "templates/**/*.html" --fix --extras=[django,tailwind]
```

## Installation

Cutesy requires **Python 3.12+** and works on Linux, macOS, and Windows.

**Basic Installation:**
```bash
pip install cutesy
```

**For system-wide CLI tool:**
```bash
pipx install cutesy
```

**Development Installation:**
```bash
git clone https://github.com/chasefinch/cutesy.git
cd cutesy
pip install -e .
```

> 📚 **Detailed guide**: See Installation Documentation for editor integration, pre-commit hooks, and CI/CD setup.

## Basic Usage

### Command Line

**Check files for issues:**
```bash
cutesy "*.html"                    # Check all HTML files
cutesy "templates/**/*.html"       # Check recursively
cutesy --code '<div>test</div>'    # Check code string
```

**Fix issues automatically:**
```bash
cutesy "*.html" --fix              # Fix all issues
cutesy "*.html" --fix --quiet      # Fix quietly
cutesy "*.html" --return-zero      # Don't fail CI on issues
```

### Key Options

| Option | Description | Example |
|--------|-------------|---------|
| `--fix` | Auto-fix issues (recommended) | `cutesy "*.html" --fix` |
| `--extras` | Enable template/framework support | `--extras=[django,tailwind]` |
| `--ignore` | Ignore specific rules | `--ignore=[F1,D5]` |
| `--quiet` | Suppress detailed output | `--quiet` |
| `--check-doctype` | Process non-HTML5 files | `--check-doctype` |

## Configuration

### Configuration Files

Create a `cutesy.toml` file in your project:

```toml
fix = true
extras = ["django", "tailwind"]
indentation_type = "spaces"
line_length = 99
ignore = ["F1"]  # Ignore specific rules
```

**Also supports:**
- `pyproject.toml` (under `[tool.cutesy]`)
- `setup.cfg` (under `[cutesy]`)

### Common Configurations

**Django + TailwindCSS:**
```toml
fix = true
extras = ["django", "tailwind"]
line_length = 120
max_items_per_line = 6
```

> 📚 **Complete guide**: See Configuration Documentation for all options and examples.

## Framework Support

### Django Templates

Enable Django template processing:

```bash
cutesy "templates/*.html" --fix --extras=django
```

**Supports:**
- `{% %}` template tags with proper indentation
- `{{ }}` variables
- Template inheritance (`{% extends %}`, `{% block %}`)
- Complex template logic with nested HTML

**Example transformation:**
```html
<!-- Before -->
{% if user.is_authenticated %}
<div class="welcome">
        <h1>Welcome, {{ user.name }}!</h1>
{% endif %}

<!-- After -->
{% if user.is_authenticated %}
    <div class="welcome">
        <h1>Welcome, {{ user.name }}!</h1>
    </div>
{% endif %}
```

### TailwindCSS

Automatic class sorting and organization:

```bash
cutesy "*.html" --fix --extras=tailwind
```

**Features:**
- **Smart sorting**: Groups utility classes logically
- **Responsive prefixes**: Maintains `sm:`, `md:`, `lg:` order
- **Pseudo-classes**: Preserves `hover:`, `focus:`, etc.
- **Custom classes**: Keeps your custom classes at the end

**Example:**
```html
<!-- Before -->
<div class="text-red-500 p-4 bg-white hover:bg-gray-100 md:p-8 rounded-lg">

<!-- After -->
<div class="bg-white hover:bg-gray-100 p-4 md:p-8 rounded-lg text-red-500">
```

### AlpineJS & HTMX

Cutesy works great with attribute-heavy frameworks:

- **Proper indentation** for multi-line attributes
- **Whitespace normalization** inside attributes
- **Consistent formatting** across your components

## Examples

Cutesy ensures that HTML documents contain consistent whitespace, follow best practices, and adhere to common conventions. In `--fix` mode, Cutesy turns this:

```html
    <!doctype html>
<html>
                    <head>
        <title>Cutesy 🥰 demo</title>
    </head>
<body>
            <h1>Hi     there!</h1>

            {% if request.user.is_authenticated %}
                    <p>Cutesy is so happy      when your code is neat.</p>
                            {% endif %}

                <div     class='danger-zone'
                        id="lintTrap"   ></div    >
                    </body>
</html>
```

…into this:

```html
<!doctype html>
<html>
<head>
    <title>Cutesy 🥰 demo</title>
</head>
<body>
    <h1>Hi there!</h1>

    {% if request.user.is_authenticated %}
        <p>Cutesy is so happy when your code is neat.</p>
    {% endif %}

    <div id="lintTrap" class="danger-zone"></div>
</body>
</html>
```

### Real-World Usage

**Django Project:**
```bash
# Format all templates
cutesy "templates/**/*.html" --fix --extras=[django,tailwind]

# Check before committing
cutesy "templates/**/*.html" --quiet
```

**Static Site:**
```bash
# Format with custom config
cutesy "src/**/*.html" --fix --line-length=120

# Format specific files
cutesy "src/components/*.html" --fix --extras=tailwind
```

## Documentation

| Document | Description |
|----------|-------------|
| **Installation Guide** | Complete installation instructions, editor integration, CI/CD setup |
| **Configuration Guide** | All configuration options, file formats, project examples |
| **Rules Reference** | Complete list of all rules with examples and fixes |
| **Development Guide** | Contributing, testing, development setup, Rust extensions |
| **Distribution Guide** | PyPI publishing, Homebrew formula, package management |

## When to Use Cutesy

Cutesy is great for:

- **Server-rendered HTML templates** with Django, Jinja2, ERB, Liquid, and other template engines
- **Attribute-heavy patterns** like AlpineJS and HTMX, with smart attribute reordering and formatting
- **Component frameworks** like Svelte and Vue (`.svelte`, `.vue` files) with HTMLX-style syntax
- **Speed-focused static analysis for HTML** — fast, with additional linting and best-practice checks beyond formatting
- **Pluggability** — better hooks for custom attribute ordering, validation, and transformation
- **AI code validation** — an all-in validation strategy to maximize code quality and catch errors, which agents can use to validate and update their own output

### Not for

- **JSX / TSX files** — Cutesy formats HTML templates, not JavaScript files.
- **Standalone JS / CSS files** — Cutesy’s just for HTML, the templates that generate it, and the styles & scripts inside it. Use a CSS/JS toolchain for external files. Avoid JS or CSS “templates” which accept server instructions; Keep this in your HTML.

**Why not Prettier, Stylelint & ESLint?** Cutesy uses all three under the hood for formatting scripts & styles, and it will even respect your configuration for each. Cutesy provides access to these tools (as well as Typescript and automated testing) for server-rendered HTML templates, for and blocks inside of HTML documents, and for styles & scripts inside of HTML attributes.

Aside from that, Cutesy enforces an opinionated style for the HTML itself, along with any template-language tags, and it includes additional post-format analysis such as HTML & framework best practices. (Think image sizing, load order, template tag formatting, Tailwind theme setup, etc.)

## Benefits

- ✅ **Validate AI code output** - Catch inconsistencies in generated HTML
- ✅ **Enforce team standards** - Consistent formatting across all developers
- ✅ **Catch errors early** - Find malformed HTML and template syntax issues
- ✅ **Save time** - No more manual formatting or style discussions
- ✅ **Better code reviews** - Focus on logic, not formatting
- ✅ **Framework integration** - Works with your existing tools and workflows

## Badge

Show off how Cutesy keeps you in line.

code style: cutesy

```markdown
code style: cutesy
```

## License

MIT License - see LICENSE file for details.

## Contributing

We welcome contributions! Whether it's:

- 🐛 **Bug reports** via GitHub Issues
- 💡 **Feature requests** via GitHub Discussions
- 🔧 **Code contributions** via Pull Requests
- 📖 **Documentation improvements**

See our Development Guide for getting started.

---

**Keep your HTML tidy with Cutesy! 🥰**

or els̴͔e

# Rocus - AI Knowledge Graph & Collaborative Bookmark Manager

## 评论（1/1）

> **chasefinch** · 2026-10-28T19:20:49.000Z　
> Hi everyone! I'm sharing a linter I've been working on for a few years.This is Cutesy, a formatter & linter for HTML documents, including HTML templates.The obvious thing that makes it unique (from, say, Prettier) is that it supports HTML templates; We run it on Django templates.A non-obvious thing that makes it unique is the “extras”, which customize the processing with more features, such as Django template tag formatting, Tailwind class sorting, and HTML best practices.Don’t make it angry.

## 关联链接

- https://github.com/chasefinch/cutesy.git

## 导航

- 项目页：[[10-项目/github.com_ecb488cb]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
