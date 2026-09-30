---
type: "project"
title: "Show HN: Resterm - A terminal-based REST, GraphQL and gRPC client"
project_url: "https://resterm.app/"
first_seen: "2026-09-30T18:57:07+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_unkn0wn_root
  - story_49899872
  - show_hn
lang: "en"
---

# Show HN: Resterm - A terminal-based REST, GraphQL and gRPC client

> [!info] 一句话导读
> Skip to content >_ RESTERM │ ▣ docs λ restermscript ⇄ cli ⬢ install ◇ github / search docs Ctrl K v1.10.2 │ ◐ theme ? Help

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://resterm.app/>
> 首次收录：2026-09-30T18:57:07+08:00
> 来源渠道：HN Show HN
> 标签：author_unkn0wn_root, story_49899872, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-30T18:28:30+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-30/9543edcbe384f73c_Show-HN-Resterm-A-terminal-based-REST,-GraphQL-and]] |
| 2026-09-30T18:57:07+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-30/9543edcbe384f73c_Show-HN-Resterm-A-terminal-based-REST,-GraphQL-and]] |

## 摘要正文

Skip to content >_ RESTERM │ ▣ docs λ restermscript ⇄ cli ⬢ install ◇ github / search docs Ctrl K v1.10.2 │ ◐ theme ? Help / Search g d Docs j/k Scroll t Theme ? Help  An API-as-code workbench for the terminal.  Resterm is an API client that keeps requests in plain .http files next to your code. Send them from a keyboard-driven TUI, or run the same files in CI with resterm run .  $ brew install resterm copy  Quick start ▸ Read the docs  HTTP GraphQL gRPC WebSocket SSE macOS, Linux, Windows Apache-2.0  Screens Editor Workflow Timeline Profiler Explain RestermScript ### Requests are plain text  Resterm works with the tools you already use. Edit requests in any text editor and track changes in Git. Keep requests, mocks, workflows and environments alongside your code. Use the terminal UI with autocomplete to edit and send requests, or run the same files in CI with resterm run .  requests.http ### Mock: say hello  # @mock method = POST path = /hello  # @match json = {"kind":"greeting"}  HTTP/1.1 200 OK  Content-Type: application/json {"message":"hello from the mock","name":{{json.body.name}}} ### Mock: create a member  # @mock method = POST path = /users  # @match headers = {"Authorizat…
