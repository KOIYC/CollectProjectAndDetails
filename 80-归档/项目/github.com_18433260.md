---
type: "project"
title: "derniercri/snatch"
project_url: "https://github.com/derniercri/snatch"
first_seen: "2026-09-20T03:27:59+08:00"
sources:
  - github_new
tags:
  - 项目
  - github_new
  - Rust
  - topic:side-project
lang: "en"
stale: true
---

# derniercri/snatch

- **项目链接**：https://github.com/derniercri/snatch
- **首次收录**：2026-09-20T03:27:59+08:00
- **来源渠道**：GitHub 新星仓库
- **标签**：Rust, topic:side-project
- **最新指标**：stars=685 · forks=39 · open_issues=11

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T02:35:56+08:00 | GitHub 新星仓库 | stars=685 · forks=39 · open_issues=11 | [[80-归档/posts/github_new/2026-09-20/184332603281f77a_derniercri-snatch]] |
| 2026-09-20T02:56:53+08:00 | GitHub 新星仓库 | stars=685 · forks=39 · open_issues=11 | [[80-归档/posts/github_new/2026-09-20/184332603281f77a_derniercri-snatch]] |
| 2026-09-20T03:05:42+08:00 | GitHub 新星仓库 | stars=685 · forks=39 · open_issues=11 | [[80-归档/posts/github_new/2026-09-20/184332603281f77a_derniercri-snatch]] |
| 2026-09-20T03:16:34+08:00 | GitHub 新星仓库 | stars=685 · forks=39 · open_issues=11 | [[80-归档/posts/github_new/2026-09-20/184332603281f77a_derniercri-snatch]] |
| 2026-09-20T03:18:21+08:00 | GitHub 新星仓库 | stars=685 · forks=39 · open_issues=11 | [[80-归档/posts/github_new/2026-09-20/184332603281f77a_derniercri-snatch]] |
| 2026-09-20T03:27:59+08:00 | GitHub 新星仓库 | stars=685 · forks=39 · open_issues=11 | [[80-归档/posts/github_new/2026-09-20/184332603281f77a_derniercri-snatch]] |

## 摘要正文

![build status](https://api.travis-ci.org/derniercri/snatch.svg?branch=devel)  # snatch A simple, fast and interruptable download accelerator, written in Rust  ## WARNING  **This project is no longer maintained by @k0pernicus and @jean-serge.**   **Instead of Snatch, you can use, report features or issues and/or contribute to [Zou](https://github.com/k0pernicus/zou).**  ![Snatch logo](./img/snatch-horizontal.png)  (A special thanks to [@fh-d](https://github.com/fh-d) for this awesome logo !)  ## Current features  * **Simple**: a command line tool to manage easily your downloads ; * **Fast**: multithreading support.  **NOTE**: _Snatch_ is on _alpha_ version. This version runs well on remote contents with a length known **before** the download (with the `content-length` header from the server response) - also, the _Interruptable_ feature is not implemented yet.  ## Installation  1. Install Rust and Cargo using [rustup](https://www.rustup.rs/) ; 2. You can download two versions of _Snatch_ :     * the latest build from [crates.io](https://crates.io/): `cargo install     snatch` ;   * the last commit version from Github: `cargo install --git https://github.com/derniercri/snatch.git --b…
