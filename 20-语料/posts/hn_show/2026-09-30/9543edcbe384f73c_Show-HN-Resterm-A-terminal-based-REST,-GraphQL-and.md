---
type: "corpus"
item_id: "9543edcbe384f73c"
title: "Show HN: Resterm - A terminal-based REST, GraphQL and gRPC client"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49899872"
project_url: "https://resterm.app/"
author: "unkn0wn_root"
published_at: "2026-09-29T20:23:57Z"
captured_at: "2026-09-30T18:57:07+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-30"
pub_day: "2026-09-29"
tags:
  - 语料
  - hn_show
  - author_unkn0wn_root
  - story_49899872
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Resterm - A terminal-based REST, GraphQL and gRPC client

> [!info] 一句话导读
> Skip to content >_ RESTERM │ ▣ docs λ restermscript ⇄ cli ⬢ install ◇ github / search docs Ctrl K v1.10.2 │ ◐ theme ? Help

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49899872>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：unkn0wn_root　|　发布：2026-09-29T20:23:57Z
> 项目链接：<https://resterm.app/>
> 采集：2026-09-30T18:57:07+08:00　|　id：`9543edcbe384f73c`

## 正文

Skip to content >_ RESTERM │ ▣ docs λ restermscript ⇄ cli ⬢ install ◇ github / search docs Ctrl K v1.10.2 │ ◐ theme ? Help
/ Search g d Docs j/k Scroll t Theme ? Help
 An API-as-code workbench for the terminal.
 Resterm is an API client that keeps requests in plain .http files next to your code. Send them from a keyboard-driven TUI, or run the same files in CI with resterm run .
 $ brew install resterm copy
 Quick start ▸ Read the docs
 HTTP GraphQL gRPC WebSocket SSE macOS, Linux, Windows Apache-2.0
 Screens Editor Workflow Timeline Profiler Explain RestermScript
### Requests are plain text
 Resterm works with the tools you already use. Edit requests in any text editor and track changes in Git. Keep requests, mocks, workflows and environments alongside your code. Use the terminal UI with autocomplete to edit and send requests, or run the same files in CI with resterm run .
 requests.http ### Mock: say hello
 # @mock method = POST path = /hello
 # @match json = {"kind":"greeting"}
 HTTP/1.1 200 OK
 Content-Type: application/json
{"message":"hello from the mock","name":{{json.body.name}}}
### Mock: create a member
 # @mock method = POST path = /users
 # @match headers = {"Authorization":{"prefix":"Bearer "}} json = {"role":"member"}
 HTTP/1.1 201 Created
 Content-Type: application/json
{"id":{{json.body.id}},"name":{{json.body.name}}}
### Say hello
 # @name Hello
 # @assert response.statusCode == 200
 # @assert response.json("name") == "Resterm"
 POST {{base.url}}/hello
 Content-Type: application/json
{"kind":"greeting","name":"Resterm"}
### Create users from a list of names
 # @name CreateUsers
 # @for-each ["ada","linus","grace"] as name
 # @auth bearer {{auth.token}}
 # @assert response.statusCode == 201
 # @assert response.json("name") == name
 POST {{base.url}}/users
 Content-Type: application/json
{"id":"user-{{= name }}","name":"{{= name }}","role":"member"}
Terminal $ resterm mock requests.http &
Mock server listening on http://127.0.0.1:8080 (2 routes, 2 scenarios)
$ resterm run --env dev --all requests.http
Running 2 target(s) from requests.http with env dev
PASS POST Hello [200 OK in 12.5625ms]
 Source Target: {{base.url}}/hello
 Effective Target: http://127.0.0.1:8080/hello
PASS FOR-EACH POST CreateUsers [3 passed, 0 failed, 0 skipped in 2.807625ms]
 1. PASS POST CreateUsers (1/3) [201 Created in 958.5µs]
 2. PASS POST CreateUsers (2/3) [201 Created in 789.708µs]
 3. PASS POST CreateUsers (3/3) [201 Created in 928.375µs]
Summary: total=2 passed=2 failed=0 skipped=0 $ resterm mock requests.http & Mock server listening on http://127.0.0.1:8080 (2 routes, 2 scenarios) $ resterm run --env dev --all requests.http Running 2 target(s) from requests.http with env dev PASS POST Hello [200 OK in 12.5625ms] Source Target: {{base.url}}/hello Effective Target: http://127.0.0.1:8080/hello PASS FOR-EACH POST CreateUsers [3 passed, 0 failed, 0 skipped in 2.807625ms] 1. PASS POST CreateUsers (1/3) [201 Created in 958.5µs] 2. PASS POST CreateUsers (2/3) [201 Created in 789.708µs] 3. PASS POST CreateUsers (3/3) [201 Created in 928.375µs] Summary: total=2 passed=2 failed=0 skipped=0 $
### What it does
 Send requests, build workflows and mock APIs from your terminal.
 features.http (10) HTTP request-files Plain .http and .rest files. Directives in # @ comments add names, captures, asserts and settings.
 GRPC protocols HTTP, GraphQL, gRPC, WebSocket and SSE, all from the same editor.
 WF workflows Chain requests into steps. Capture values, assert on responses, branch with @if and loop with @for-each.
 MOCK mock-servers Mock responses live next to the requests they stand in for, with matching rules and sequences.
 REC recording Point your app at the Resterm proxy and save its traffic as requests, mocks or both.
 AUTH authentication OAuth 2.0 with PKCE, or reuse tokens from CLIs you already have, like gh auth token.
 SSH tunnels @ssh and @k8s send a request through a bastion or a port-forward that Resterm opens and closes.
 TRACE tracing Timeline tracing, profiling and compare runs across environments.
 RTS restermscript A small expression language made for requests. JavaScript hooks when you want them.
 RUN resterm-run Run the same files headless in CI, with JSON and JUnit output.
### Install
 Available for macOS, Linux and Windows. One binary. No runtime required.
 Install Homebrew Script Windows Go
 $ brew install resterm copy
 macOS and Linux
$ curl -fsSL https://raw.githubusercontent.com/unkn0wn-root/resterm/main/install.sh | bash copy
 macOS and Linux
$ iwr -useb https://raw.githubusercontent.com/unkn0wn-root/resterm/main/install.ps1 | iex copy
 PowerShell
$ go install github.com/unkn0wn-root/resterm/cmd/resterm@latest copy
 Go 1.25 or newer
Release binaries for macOS, Linux and Windows are on the releases page . Installed without Homebrew? resterm --update updates in place.
Quick start $ mkdir my-api && cd my-api $ resterm init $ resterm resterm init writes a small project with local mocks. Press g Shift+M to start the mock server, then Ctrl+Enter to send the request under the cursor.
Response HTTP/1.1 200 OK
 Content-Type: text/plain
 No telemetry. No account. Resterm is free and open source under the Apache 2.0 license.
 ◇ GitHub ⇄ Releases ♥ Sponsor ▣ Docs
Press ? for help ⇄ index.http ≡ Home ▸ NORMAL Top ⎇ main ◇ v1.10.2 Apache-2.0 Search / Esc
 ↑ ↓ move Enter open Esc close
 Help These keys work like the ones in the TUI.
 / Search the docs (also Ctrl K)
 j k Scroll down and up
 g g G Jump to the top or the bottom
 [ ] Previous and next docs page
 g d Docs index
 g h Home page
 t Switch between dark and light
 ? Show this help
 Esc Close a dialog
 Esc close

## 关联链接

- http://127.0.0.1:8080
- http://127.0.0.1:8080/hello
- https://raw.githubusercontent.com/unkn0wn-root/resterm/main/install.ps1
- https://raw.githubusercontent.com/unkn0wn-root/resterm/main/install.sh

## 导航

- 项目页：[[10-项目/resterm.app_d6c69d27]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
