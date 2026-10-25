---
type: "project"
title: "Show HN: Wasi-Python – CPython, NumPy, and Pandas in a WebAssembly Sandbox"
project_url: "https://github.com/ClayGendron/wasi-python"
first_seen: "2026-10-25T23:24:35+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_clay-gendron
  - story_50224777
  - show_hn
lang: "en"
---

# Show HN: Wasi-Python – CPython, NumPy, and Pandas in a WebAssembly Sandbox

> [!info] 一句话导读
> ClayGendron/wasi-python

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/ClayGendron/wasi-python>
> 首次收录：2026-10-25T23:24:35+08:00
> 来源渠道：HN Show HN
> 标签：author_clay-gendron, story_50224777, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-25T23:24:35+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-25/436024cea3a79a21_Show-HN-Wasi-Python-–-CPython,-NumPy,-and-Pandas-i]] |

## 摘要正文

# ClayGendron/wasi-python  A statically linked CPython for WebAssembly hosts (wasm32-wasip1) with numpy, pandas, scipy, and more compiled in. Built for running untrusted agent code server-side in web applications.  - Stars: 1 - Forks: 0 - Watchers: 1 - Open issues: 0 - License: Apache License 2.0 - Homepage: https://claygendron.github.io/wasi-python/ - Default branch: main - Created: 2026-10-16T16:52:04Z  ## Languages  - C - C++ - Dockerfile - Fortran - LLVM - Python - Rust - Shell - WebAssembly  ## Top Contributors  - ClayGendron (1175 contributions) - claude (86 contributions)  ---  ## README  **A secure Python sandbox for agent-generated code with the scientific stack inside.**  wasi-python is CPython 3.15 compiled to WebAssembly as one static binary. It includes numpy, pandas, scipy, scikit-learn, statsmodels, matplotlib, and forty plus other packages.  It is built to run code that AI agents generate, or any other code that is untrusted and must be kept apart from the host process. By default, the sandbox sees no host files and has no network access.  Run it from Python with one `pip install`, or load the same binary into any WebAssembly host that supports exception handling.  …
