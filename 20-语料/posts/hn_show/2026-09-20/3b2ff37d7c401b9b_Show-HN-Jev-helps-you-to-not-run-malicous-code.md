---
type: "corpus"
item_id: "3b2ff37d7c401b9b"
title: "Show HN: Jev helps you to not run malicous code"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49756921"
project_url: "https://github.com/luantak/is-malicious"
author: "lu4p"
published_at: "2026-09-18T16:44:17Z"
captured_at: "2026-09-20T09:36:38+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - hn_show
  - author_lu4p
  - story_49756921
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Jev helps you to not run malicous code

> [!info] 一句话导读
> luantak/is-malicious

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49756921>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：lu4p　|　发布：2026-09-18T16:44:17Z
> 项目链接：<https://github.com/luantak/is-malicious>
> 采集：2026-09-20T09:36:38+08:00　|　id：`3b2ff37d7c401b9b`

## 正文

# luantak/is-malicious

A codebase scanner that helps you not run malicous code

- Stars: 13
- Forks: 1
- Watchers: 13
- Open issues: 0
- License: MIT License
- Default branch: master
- Created: 2026-09-18T11:40:17Z

## Languages

- JavaScript
- Shell
- TypeScript

## Topics

- jev
- security-scanner
- typesafe-ai

## Top Contributors

- luantak (16 contributions)

---

## README

# is-malicious?

Scan a codebase for hidden, deceptive, or data-stealing behavior with TypeSafe Jev. The CLI sends source, configuration, build, and CI files to Jev for review, then points you to suspicious files and lines.

Use it as a second opinion before running unfamiliar code. A clean report is not proof that a project is safe.

## Quick start

You need Node.js 20 or later and a TypeSafe API key.

```bash
export TYPESAFE_API_KEY=your-api-key
npx is-malicious /path/to/project
```

Omit the path to scan the current directory. Scans send file contents to the TypeSafe API and use paid input tokens. The report includes token usage and a calculated input cost.

To install the CLI globally:

```bash
npm install -g is-malicious
is-malicious /path/to/project
```

## Reading the report

Findings include a file, line range, category, probability, confidence, and a short reason label. Use these to decide which code to read first.

Telemetry appears separately as `info`, including documented analytics, crash reports, and feature-flag pings. Telemetry alone does not cause a failing exit code.

| Exit code | Meaning |
| --- | --- |
| `0` | No high-severity findings. The report may still contain other findings. |
| `1` | At least one high-severity finding. |
| `2` | The command failed, for example because of an invalid flag or a scan error. |

Both high and low scores can be wrong. Review the flagged code and the scan's coverage before deciding whether to run a project.

## What it checks

Jev reviews file contents for behavior and context. Ordinary credential use, documented services, and normal deployment jobs are intended to score low.

The checks cover:

| Area | Behaviors |
| --- | --- |
| Data theft and collection | Credential theft, unexpected data uploads, covert fingerprinting, excessive collection, and surveillance of input or devices |
| Network and execution | Hidden network activity, downloading and running hidden code, remote commands, and command-and-control channels |
| Access and persistence | Permission abuse, hidden startup or background processes, authentication bypasses, backdoors, and resistance to removal |
| Concealment | Obfuscation, anti-analysis checks, impersonation, and other deceptive behavior |
| System abuse | Destruction or sabotage, weakened security controls, cryptomining, unwanted proxying, and spreading to other machines |
| Build and dependencies | Suspicious build or CI steps and supply-chain manipulation |
| Telemetry | Usage analytics, diagnostics, crash reports, and feature-flag pings, reported as advisory findings |

The check definitions live in `src/checks/builtin.ts`. To add a check, add and register a definition. The scanner handles checks through the same interface.

## Limits and coverage

The scanner reads selected text files. It does not inspect binaries, disk images, installers, or running processes.

It respects `.gitignore` and skips files such as:

- Images, binaries, and lockfiles.
- Generated bundles and compiled `dist`, `lib`, and `build` output.
- TypeScript declarations, `tsconfig`, and JSON configuration that its filters exclude.
- Files larger than 400,000 bytes and unsupported file types.

Malicious behavior in skipped files will not appear in the scan.

This tool also does not audit known dependency vulnerabilities or inventory committed secrets. Use a dependency auditor for known vulnerabilities and a secret scanner for exposed keys.

It does not sandbox code. Install scripts and postinstall hooks can still run when you install a project, even after a clean report.

## GitHub Actions

1. Copy a workflow from `examples/github-actions/` to `.github/workflows/is-malicious.yml`.
2. Add a repository secret named `TYPESAFE_API_KEY`.
3. Make the PR base available with `fetch-depth: 0` or an explicit fetch of the base branch.

Choose the workflow that fits your needs:

| Workflow | Behavior |
| --- | --- |
| `scan-pr.yml` | Scan files changed against the PR base and fail on high-severity findings. |
| `scan-pr-comment.yml` | Run the same scan and post or update a report comment. |

Both use this command to scan the PR's changed files:

```bash
npx --yes is-malicious . --diff-from "origin/${{ github.base_ref }}"
```

Fork PRs do not receive the API secret by default. Do not switch to `pull_request_target` just to expose the key to a fork PR. Running untrusted PR code in that context can expose your secrets.

## Agent skill

skills.sh

The agent skill instructs an agent to scan a repository after cloning it, or when asked whether it is safe. The scan should happen before installing dependencies or running the project.

Install the skill for the current project:

```bash
npx skills add luantak/is-malicious
```

Or install it globally:

```bash
npx skills add -g luantak/is-malicious
```

The agent runs `npx is-malicious`, so `TYPESAFE_API_KEY` must be set in its environment. See the skills CLI docs for listing, updating, and removing skills.

## How a scan works

1. Find eligible files under the requested path, respecting ignore rules and file filters.
2. Group files by directory into chunks that fit the character budget. Split larger files into consecutive slices.
3. Send each chunk to Jev with all check categories in one request. The first pass includes the full contents of each selected file, with extra blank lines collapsed.
4. Run a second pass on suspicious or uncertain chunks, or chunks with a high overall risk score. This pass focuses on line windows in the file Jev identified.
5. Print findings, token usage, and the calculated input cost.

If Jev returns `max_tokens_exceeded`, the scanner splits the chunk and retries.

Jev answers typed questions using `noul`, `choice`, and `score`. Noul answers have no separate confidence field, so the report calculates confidence as `2 * |p - 0.5|`. Probabilities of `0.91` and `0.09` therefore have the same confidence, though they point to opposite answers.

## Usage

```text
is-malicious [path] [options]
```

| Option | What it does | Default |
| --- | --- | --- |
| `--json` | Print the full report as JSON | Off |
| `--model ` | Choose a Jev model | `jev-latest` |
| `--concurrency ` | Set the number of parallel chunk requests | `12` |
| `--min-prob ` | Set the minimum category probability to report | `0.40` |
| `--diff-from ` | Scan only files changed since a Git ref | Scan all eligible files |
| `-h`, `--help` | Show help | |

For example, scan files changed since `origin/main`:

```bash
is-malicious . --diff-from origin/main
```

This scans the changed files, not just the changed lines, so you can review a PR without paying to rescan the whole project.

## Development

From a checkout:

```bash
npm install
npm run build
npx tsx src/cli.ts /path/to/project
```

Run the tests:

```bash
npm test
```

Scan tests use a scripted Jev client, so they spend no API credits. Fixtures under `fixtures/` cover benign code, suspicious behavior such as remote `eval` and secret theft, and telemetry.

# Your text editor

## 导航

- 项目页：[[10-项目/github.com_74ff9e11]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
