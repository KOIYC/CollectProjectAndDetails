---
type: "corpus"
item_id: "ae20084a45773df7"
title: "Show HN: Multimeter – Git-native REST client and API tests in VS Code"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49711744"
project_url: "https://mmt.dev/"
author: "mshobeyri"
published_at: "2026-09-15T12:49:52Z"
captured_at: "2026-09-20T09:37:19+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_mshobeyri
  - story_49711744
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Multimeter – Git-native REST client and API tests in VS Code

> [!info] 一句话导读
> Multimeter — API Test Tools

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49711744>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：mshobeyri　|　发布：2026-09-15T12:49:52Z
> 项目链接：<https://mmt.dev/>
> 采集：2026-09-20T09:37:19+08:00　|　id：`ae20084a45773df7`

## 正文

Multimeter — API Test Tools
# Git-nativeAPI TestGit-native|API Testright in your repo.
Start with a request. Grow into a testing platform. Never switch tools.
Build Your First FlowView on GitHub
VS Code
api.mmttest.mmtsuite.mmt
API definition
POST
https://test.mmt.dev/echo
Body
Params
Headers
Request Body
{
"name": "Multimeter",
"message": "Hello from mmt!"
}
Response Body
{
"body": {
"name": "Multimeter",
"message": "Hello from mmt!"
}
}
142ms200
## Everything you need. Nothing you don't.
Multimeter gives you the power of enterprise testing tools with the simplicity of a single VS Code extension.
### Free & Open Source
100% free and open source under BSL license. No subscriptions, no feature gates, no restrictions.
### Git-Native & YAML
Tests are plain YAML files versioned in Git alongside your code. PRs, reviews, and diffs work naturally.
### AI Test Generation
Ask the built-in AI assistant to generate tests from descriptions, OpenAPI specs, or existing APIs.
### Drag & Drop Test Builder
Build functional test flows visually — no scripting required.
### Flowchart Test View
See every test as a flowchart, making branches, loops, calls, and assertions easier to understand and review.
### One Replaces Many
API testing, beta load testing, mock servers, documentation — one tool instead of Postman, JMeter, and more.
### Secure & Private
Everything stays local. No cloud sync, no data collection, no external uploads. Your credentials are safe.
### Built-in Mock Server
Spin up HTTP and WebSocket mock servers instantly. Perfect for frontend development and integration testing.
### CI/CD Ready
Run the same .mmt, .http-backed, and Bruno-backed flows in pipelines with testlight, export reports, and keep automation version-controlled.
### Different Reports
Export runs as HTML, Markdown, JUnit XML, or MMT reports depending on whether you need CI output, shareable docs, or interactive review.
### Native Fuzzy Tests
Create variation-heavy API and flow checks directly in Multimeter instead of bolting fuzz-style coverage onto a separate toolchain.
### Auto-Generated Docs
Generate beautiful HTML or Markdown API documentation directly from your .mmt test files.
### Load Testing (Beta)
Run one .mmt test scenario with threads, ramp-up, repeat limits, and load-oriented reports.
### VS Code Native
Design, run, debug, and review API tests inside VS Code with native panels and Git-friendly files.
### Other tools support
Convert or reuse Postman, OpenAPI / Swagger, WSDL / SOAP, Bruno, .http / .rest request files, and curl commands.
Test Flows## Reusable test flows
that run everywhere
Chain API calls, assertions, loops, and delays into complete test flows. Write them in YAML, reuse existing `.http` and `.bru` request files, build them with drag-and-drop, or inspect the same logic as a flowchart — either way you get portable `.mmt` files that run inside VS Code, in CI pipelines with `testlight`, or anywhere Node runs.
* Compose flows from reusable API definitions — call, assert, loop, branch
* Switch to a flowchart view to review paths, branches, and loops at a glance
* Import other tests, .http request files, Bruno requests, and CSV data to build complex scenarios
* Run locally in VS Code or in CI/CD with a single CLI command
* Simpler than JMeter or Postman Runner — no GUI required in pipelines
* Plain YAML files live in your repo, versioned and reviewed like code
login-flow.mmt
◎Overview
⊞Flow
{ }Code
⇢call
login
⋮⠿
✓assert
login.status == 200
⋮⠿
⏸delay
1s
⋮⠿
▾for
user of users
⋮⠿
⇢call
getProfile
⋮⠿
✓check
profile.name == user.name
⋮⠿
▾if
user.admin == true
⋮⠿
⇢call
getPermissions
⋮⠿
▸print
"All done"
⋮⠿
Multimeter tests versioned in Git
$
Version Controlled## Collaborate via Git
Tests are plain YAML `.mmt` files stored right next to your source code. No proprietary formats, no cloud sync — just files in your repo, versioned and reviewed like everything else.
* Code and tests reviewed in the same pull request
* Check out an older branch and run its tests — they always match that version
* Share a reproduced bug as a committed test — anyone can pull and re-run it
* No separate user management — your Git permissions are enough
* Works with any VCS: Git, SVN, Mercurial — they are just files
Multi-Protocol## Every protocol you need
Test REST APIs, WebSocket connections, GraphQL endpoints, gRPC services, and SOAP endpoints — all from the same tool. Existing .http and Bruno request files can run as test flows too.
HTTP / REST / SOAP
### HTTP / REST / SOAP
Full HTTP / REST / SOAP support with all methods, headers, auth, JSON / XML bodies, and .http / Bruno file compatibility.
WebSocket
### WebSocket
Real-time WebSocket testing with connection management, message sending, and event listening.
GraphQL
### GraphQL
GraphQL support with operations, variables, and response extraction for queries and mutations.
gRPC
### gRPC
gRPC protocol support with proto files, server reflection, and streaming modes.
AI-Powered## Let AI write your tests
The built-in `@Multimeter` chat participant in VS Code can generate complete test flows from natural language descriptions, OpenAPI specs, or existing API definitions.
login.mmt
Generated API✓
type: api
url: https://test.mmt.dev/echo
method: post
format: json
body:
username: mehrdad
password: 123456
Copilot Chat
U
@Multimeter generate a sample login api with username and password. url should be https://test.mmt.dev/echo
Generating API…
Mock Server## Spin up mock APIs instantly
Define HTTP and WebSocket mock servers as simple YAML files. They start in milliseconds and support dynamic responses, path parameters, request body mirroring, and reflect mode — all without any external tools.
* Define routes, status codes, headers, and response bodies in YAML
* Dynamic responses with template variables (params, body, random, date)
* Reflect mode — echo back exactly what the client sends
* Start from suites with the servers: field for integration testing
* Start from tests with the run step for self-contained test scenarios
* HTTP and WebSocket protocols supported
* History panel shows every request received by the mock server
user-service.mmt
terminal
$ npm install -g mmt-testlight
✓ installed mmt-testlight@0.4.0
$ npx testlight run tests/smoke-suite.mmt
Running suite: smoke-suite
✓ login-test (342ms)
✓ get-users-test (128ms)
✓ create-order-test (256ms)
✓ websocket-test (89ms)
4 passed | 0 failed | 815ms
✓ Report written: reports/results.xml
CI/CD Ready## Run tests in any pipeline
The `testlight` CLI runs your exact same `.mmt` test files in CI/CD pipelines. No separate test configuration needed — what you test in VS Code is what runs in CI.
* GitHub Actions, Jenkins, GitLab CI, Azure DevOps
* JUnit XML, HTML, and Markdown report generation
* Auto-export reports via suite export: field — no extra flags
* Environment variables via --env-file or -e flags
* Preset switching for dev/staging/production
* Exit codes for pass/fail pipeline gating
* Same YAML files, same results — everywhere
API Documentation## Docs that write themselves
Multimeter auto-generates polished, interactive API documentation straight from your `.mmt` files. No extra tooling, no separate doc repo — your docs live alongside your tests and stay in sync automatically.
* Auto-generated from the same YAML you already write
* Dark and light themes with syntax-highlighted examples
* Interactive request/response previews for every endpoint
* Export as self-contained HTML or Markdown
* Group endpoints by tags, show inputs, outputs, and examples
View sample documentation↗
sample\_doc.html

Open full preview ↗

## How Multimeter compares
See how we stack up against other popular API testing tools
|Feature|
MultimeterMultimeter
|
PostmanPostman
|
InsomniaInsomnia
|
BrunoBruno
|
Robot FrameworkRobot Framework
|
CucumberCucumber
|
JMeterJMeter
|
NeoLoadNeoLoad
|
PlaywrightPlaywright
|
|Price|Free|$14/user/mo|$12/user/mo|$6/user/mo|Free|Free|Free|Enterprise|Free|
|Open Source|||Partial|Partial||||||
|HTTP / REST||||||Via code||||
|WebSocket||||Partial|Via library|Via code|Plugins|Partial|Via browser|
|GraphQL|||||Via library|Via code|Plugins|Partial|Via API|
|gRPC|||||Via library|Via code|Plugins|Partial||
|CI/CD CLI||||||||||
|Load Testing|Beta|Limited|||Via library|Via code||||
|Git-Native Files|||||||XML|||
|.http / Bruno File Support||||||||||
|Drag & Drop Test Builder||||||||||
|Test Flow Flowchart View||||||||Partial||
|Functional Test Flows||Scripts|Scripts|Scripts||||||
|Test Suites (Parallel / Sequential)||Sequential||||||||
|Reusing / Chaining Tests||||||||||
|Data Extraction (JSONPath/XPath/Regex)||Scripting|Scripting|Scripting|Via library|Via code|||Via code|
|AI Test Generation||||||||||
|Declarative Test Flows (YAML)||||||||||
|BDD / Human-Readable Specs||||||||||
|Interactive API Docs (HTML)||||||||||
|Mock Server||Cloud only||||||||
|Environment Variables / Presets|||||Variables|Via code||||
|Dynamic Tokens (random, date, uuid)|||||Via library|Via code|||Via code|
|JS Helper Module Imports||||||||||
|CSV Data-Driven Testing|||||||||Via code|
|HTML Report||||||||||
|Markdown Report||||||||||
|JUnit Report||||||||||
|Fully Offline||||||||||
|Feature|
MultimeterMultimeter
|
PostmanPostman
|
InsomniaInsomnia
|
BrunoBruno
|
Robot FrameworkRobot Framework
|
CucumberCucumber
|
JMeterJMeter
|
NeoLoadNeoLoad
|
PlaywrightPlaywright
|
|Price|Free|$14/user/mo|$12/user/mo|$6/user/mo|Free|Free|Free|Enterprise|Free|
|Open Source|||Partial|Partial||||||
|HTTP / REST||||||Via code||||
|WebSocket||||Partial|Via library|Via code|Plugins|Partial|Via browser|
|GraphQL|||||Via library|Via code|Plugins|Partial|Via API|
|gRPC|||||Via library|Via code|Plugins|Partial||
|CI/CD CLI||||||||||
|Load Testing|Beta|Limited|||Via library|Via code||||
|Git-Native Files|||||||XML|||
|.http / Bruno File Support||||||||||
|Drag & Drop Test Builder||||||||||
|Test Flow Flowchart View||||||||Partial||
|Functional Test Flows||Scripts|Scripts|Scripts||||||
|Test Suites (Parallel / Sequential)||Sequential||||||||
|Reusing / Chaining Tests||||||||||
|Data Extraction (JSONPath/XPath/Regex)||Scripting|Scripting|Scripting|Via library|Via code|||Via code|
|AI Test Generation||||||||||
|Declarative Test Flows (YAML)||||||||||
|BDD / Human-Readable Specs||||||||||
|Interactive API Docs (HTML)||||||||||
|Mock Server||Cloud only||||||||
|Environment Variables / Presets|||||Variables|Via code||||
|Dynamic Tokens (random, date, uuid)|||||Via library|Via code|||Via code|
|JS Helper Module Imports||||||||||
|CSV Data-Driven Testing|||||||||Via code|
|HTML Report||||||||||
|Markdown Report||||||||||
|JUnit Report||||||||||
|Fully Offline||||||||||
## Frequently Asked Questions
Everything you need to know about Multimeter
Is Multimeter free?
Yes! Multimeter is 100% free and open source under the BSL (Business Source License). You can use it for personal projects, commercial work, and enterprise deployments without any cost or restrictions.
Do I need to create an account?
No. Multimeter requires zero setup — no login, no account, no cloud registration. Install the VS Code extension and start testing immediately. Access control is handled naturally through your Git repository permissions.
How does collaboration work?
Your tests are plain YAML files (.mmt), and you can also reuse existing .http and Bruno request files, stored in your Git repository alongside your code. Collaboration works exactly like code collaboration — through pull requests, code reviews, branches, and merges. No proprietary sync needed.
How do I use Multimeter in CI/CD?
Use the testlight CLI tool. Install it via npm (npm install -g testlight), then run your tests with "npx testlight run path/to/test.mmt" or run .http and .bru files that Multimeter converts to test flows. It integrates with any CI/CD system — GitHub Actions, Jenkins, GitLab CI, Azure DevOps, and more.
What formats can I import from?
Multimeter can import or convert Postman collections, OpenAPI / Swagger specifications, WSDL / SOAP definitions, .http / .https request files, Bruno .bru / .bruno files, and curl commands. Use external request files directly from Open With, or convert them into editable MMT tests and APIs.
Does Multimeter upload any data externally?
No. Multimeter is fully local. Your API tests, environment variables, credentials, and all data stay on your machine and in your repository. Nothing is ever sent to external servers.
What protocols are supported?
Multimeter supports HTTP/REST, WebSocket, SOAP/XML, GraphQL, and gRPC protocols. You can test any API endpoint with full control over headers, body, authentication, response validation, and existing .http or Bruno file workflows.
What report formats are available?
Multimeter generates reports in four formats: JUnit XML (for CI/CD tools like Jenkins, GitHub Actions, GitLab CI), HTML (self-contained visual reports), Markdown (for PRs and documentation), and MMT Report (YAML format that opens in the built-in viewer). Generate them from the CLI with --report, from the VS Code Export button, or automatically via the suite export: field.
How does the mock server work?
Define mock servers as simple YAML files (type: server) with routes, status codes, and response bodies. They support dynamic responses via template variables (params, body, random, date), reflect mode (echo back requests), and both HTTP and WebSocket protocols. Start them from suites with the servers: field, from tests with the run step, or manually from the VS Code panel.
## Ready to simplify your
API testing?
Install Multimeter in VS Code and start testing in seconds. No account needed. No complex setup.
Install ExtensionStar on GitHub ⭐

# neverstored

## 关联链接

- https://test.mmt.dev/echo

## 导航

- 项目页：[[10-项目/mmt.dev_23cc1c12]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
