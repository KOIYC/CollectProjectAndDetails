---
type: "project"
title: "Show HN: Panini – bundle a Gleam app and BEAM into one self-contained binary"
project_url: "https://github.com/tsirysndr/panini"
first_seen: "2026-09-21T03:11:12+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_tsiry
  - story_49115490
  - show_hn
lang: "en"
---

# Show HN: Panini – bundle a Gleam app and BEAM into one self-contained binary

> [!info] 一句话导读
> Press a Gleam (Erlang/BEAM) app into a single self-contained binary — a Burrito for Gleam.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/tsirysndr/panini>
> 首次收录：2026-09-21T03:11:12+08:00
> 来源渠道：HN Show HN
> 标签：author_tsiry, story_49115490, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:31:46+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/b00e94ac55da52c7_Show-HN-Panini-–-bundle-a-Gleam-app-and-BEAM-into]] |
| 2026-09-21T03:11:12+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/b00e94ac55da52c7_Show-HN-Panini-–-bundle-a-Gleam-app-and-BEAM-into]] |

## 摘要正文

# tsirysndr/panini  Press a Gleam (Erlang/BEAM) app into a single self-contained binary — a Burrito for Gleam.  - Stars: 3 - Forks: 1 - Watchers: 3 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-07-30T13:07:34Z  ## Languages  - Nix - Rust - Zig  ## Topics  - gleam - linux - macos - single-binary - tooling  ## Top Contributors  - tsirysndr (26 contributions)  ---  ## README  # panini 🥪  e2e nix FlakeHub  **Press a Gleam (Erlang/BEAM) app into a single, self-contained binary.**  A Burrito for Gleam. `panini` turns a Gleam project that targets Erlang into one native executable that runs on a machine with **nothing installed** — no Gleam, no Erlang, no `rebar3`. The BEAM runtime is bundled inside.  ```sh panini build ./examples/hello -o ./hello ./hello                 # => Hello from hello!  (runs with nothing installed) ```  It can select the OTP version to bundle, and **cross-compile** binaries for other platforms from a single machine.  ```sh panini build ./examples/hello --otp 27.2                       # pick the OTP version panini build ./examples/hello --target all --otp 27.2          # every platform at once ```  ## Contents  - Install - Commands…
