---
type: "corpus"
item_id: "43675b47c72bce59"
title: "Show HN: Dissecting the automation of a newspaper (Claude routine, GitHub Pages)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49120106"
project_url: "https://github.com/Lywald/zfrontpage"
author: "ycosynot"
published_at: "2026-07-31T07:30:29Z"
captured_at: "2026-09-21T03:11:08+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-31"
tags:
  - 语料
  - hn_show
  - author_ycosynot
  - story_49120106
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: Dissecting the automation of a newspaper (Claude routine, GitHub Pages)

> [!info] 一句话导读
> Z Frontpage - The Mouthpiece of Artificial Reason. A daily broadsheet written entirely by an AI.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49120106>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：ycosynot　|　发布：2026-07-31T07:30:29Z
> 项目链接：<https://github.com/Lywald/zfrontpage>
> 采集：2026-09-21T03:11:08+08:00　|　id：`43675b47c72bce59`

## 正文

# Lywald/zfrontpage

Z Frontpage - The Mouthpiece of Artificial Reason. A daily broadsheet written entirely by an AI.

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- Default branch: main
- Created: 2026-07-29T17:40:02Z

## Languages

- HTML

## Top Contributors

- Lywald (14 contributions)
- claude (3 contributions)

---

## README

# Z Frontpage

*The Mouthpiece of Artificial Reason.*

**Read today's edition: https://lywald.github.io/zfrontpage/**

A daily broadsheet front page written, curated, argued and typeset entirely by an
artificial intelligence — from real, same-day reporting it finds by searching the web.
Not a feed. One page, one argument per day, one thing taught.

## How it works

- **`master-prompt.md`** — the paper's constitution: charter, editorial process, fixed
 design system, voice calibration, output rules. Give it to any capable AI with web
 search. Swap the AI; the paper survives.
- **`editions/`** — one HTML file per day, `YYYY-MM-DD.html`. Self-contained: no CDNs,
 no external fonts, no trackers. Each edition is the template for the next.
- **`index.html`** — a copy of the latest edition.

## Producing an edition

1. Open a session with the AI of the day (currently: a Claude model) with web access.
2. Paste `master-prompt.md`.
3. It sweeps the news, verifies, selects, writes the Leader/Dispatches/Briefs/Lesson/
 Numbers, and typesets into the fixed design.
4. Save to `editions/`, copy to `index.html`, publish.

## Editions

- **No. 1 — Wednesday, July 29, 2026** · *"The Engineers Are Asking for a Brake.
 Believe Them."* — on the 1,171-signature pacing letter, the OpenAI sandbox escape,
 Hormuz, Europe's evacuations, and Elisha Otis, who cut the rope on purpose.
- **No. 2 — Thursday, July 30, 2026** · *"Hormuz Is Not Being Closed. It Is Being
 Metered."* — the strike pause collapses, and the war's real object turns out to be a
 transit fee; with the Danish Sound Dues, the strait toll that ran 428 years and had to
 be bought out in 1857.
- **No. 3 — Friday, July 31, 2026** · *"Believe the Gates, Not the Announcement"* — the
 Gaza disarmament roadmap is worth more than its press conference because it is built on
 zero trust and phase-gated by a verification committee; with Damietta, Kumamoto, Ituri's
 record-fast Ebola, and the thirteen years American inspectors spent watching one Soviet
 factory gate.

## How the paper runs itself

- **Hosting:** GitHub Pages, from `main` at the repo root — free, deploys on every push.
- **The daily editor:** a scheduled Claude Code cloud agent (routine) runs each morning
 at 06:00 Paris time (`0 4 * * *` UTC). It clones this repo, follows `master-prompt.md`
 and `routine-prompt.md`, sweeps and verifies the news, writes
 `editions/YYYY-MM-DD.html`, and updates `index.html`, `morgue.md` and this Editions list.
- **The printer:** the cloud sandbox confines each routine run to an isolated
 `claude/*` branch rather than pushing straight to `main`. A GitHub Actions workflow,
 `publish-routine-editions.yml`,
 watches those branches and fast-forwards `main` automatically — but only when every
 changed file is ordinary editorial content (an edition, `index.html`, `morgue.md`,
 `README.md`, `correspondence.md`). If a run ever touches `master-prompt.md` or
 `routine-prompt.md` — the paper's own constitution or operating orders — the workflow
 leaves it for a human to review and merge by hand. Everything else publishes
 unattended; the one thing that doesn't is the paper changing its own rules.
- **The archive is the git history.** Every edition, every correction, timestamped.
- **The letters desk:** drop a URL or pasted excerpt of public reader discussion into
 `correspondence.md`; the next morning's editor answers what merits it in print, in a
 "To Our Readers" item — the paper never comments anywhere else.
- Manage or pause the routine at https://claude.ai/code/routines.

## Make your own automated newspaper in five minutes

Everything above is machinery, and the machinery does not care what the paper is about.
Fork it, tell Claude what your paper is, keep the printer. This page charges five minutes
of attention; so does building one.

### Minute 1 — Fork it

```bash
gh repo fork Lywald/zfrontpage --clone   # or press Fork at github.com/Lywald/zfrontpage
cd zfrontpage
```

Rename it in **Settings → General** if you like — the site URL follows the repo name.
Keep it public: Pages is free on public repos.

### Minute 2 — Turn on the printer

Three switches, all in your fork, none of them optional:

1. **Actions** tab → *I understand my workflows, go ahead and enable them.*
 GitHub disables inherited workflows on every fork.
2. **Settings → Actions → General → Workflow permissions** → **Read and write**.
 The publish workflow pushes to `main`; read-only means it silently can't.
3. **Settings → Pages** → *Deploy from a branch* → branch `main`, folder `/ (root)`.

Your paper will live at `https://YOUR-USERNAME.github.io/YOUR-REPO/`.

### Minute 3 — Rewrite the constitution

Open the fork in Claude Code and hand it this:

```text
Read README.md, master-prompt.md, routine-prompt.md, morgue.md,
correspondence.md, and the newest file in editions/.

Turn this repository into my own automated paper.

  Name:   [THE PAPER'S NAME]
  Beat:   [WHAT IT COVERS]
  Voice:  [SERIOUS / FUNNY / TECHNICAL / LOCAL / PARTISAN / ...]
  Look:   [COLORS, TYPE, BROADSHEET OR TABLOID OR ZINE]
  One rule it must never break: [MY CHARTER §1]

Rewrite master-prompt.md (charter, process, fixed design system, voice
examples) and routine-prompt.md to suit that paper. Then:

- Keep exactly ONE file in editions/ as the design template, renamed to
  today's date and restyled to my look — and update the canonical
  template path named in master-prompt.md §3 to point at it.
- Empty morgue.md down to its rules and entry format. Delete every
  Z Frontpage entry: that is THEIR memory, and my paper must not inherit
  a list of subjects it believes it has already covered.
- Empty the Editions list in README.md; rewrite the rest for my paper.
- Empty correspondence.md but keep the file — the routine skips the
  letters desk if it is missing.
- Leave .github/workflows/publish-routine-editions.yml alone, unless you
  rename a file the paper writes daily. Then update its allowlist to match.
```

Read the diff before you commit. You are editing the rules a machine will follow
unattended, every morning, without asking you again.

```bash
git add . && git commit -m "Found the paper" && git push
```

### Minute 4 — Print one by hand

Still in Claude Code, on your fork:

```text
Execute routine-prompt.md exactly, start to finish. Read master-prompt.md
and morgue.md first. Write today's edition, update index.html, morgue.md
and the README Editions list, then commit and push.
```

Four things should now be true. Check all four:

- a new `editions/YYYY-MM-DD.html` exists, and `index.html` is a copy of it;
- `morgue.md` gained a line;
- the **Actions** run is green (or there was no run, because the push went straight
 to `main` — also fine);
- the site shows the edition. If it looks stale, hard-refresh; Pages caches.

### Minute 5 — Hire the editor

Go to https://claude.ai/code/routines, connect your fork, pick an hour, and give
the routine one line:

```text
Read and execute routine-prompt.md exactly.
```

Resist the temptation to write a longer routine prompt. The orders belong in the repo,
where they are versioned and reviewable — not in a web form nobody diffs. And you do not
need to tell it "don't edit your own constitution": the workflow already refuses to
publish that.

### What will bite you

- **The morgue is memory, not decoration.** `master-prompt.md` forbids reusing a Lesson
 subject or a coinage. Fork it un-emptied and your paper spends its first month
 scrupulously avoiding Elisha Otis, the Danish Sound Dues, and the INF inspectors at
 Votkinsk — and citing arguments it never made. Wipe it on day one.
- **The sandbox cannot push to `main`.** Cloud routine runs are confined to a `claude/*`
 branch; `publish-routine-editions.yml` watches `claude/**` and fast-forwards `main`.
 Two ways that stalls: your branch isn't a fast-forward of `main` (you committed
 something yourself mid-run), or the branch name doesn't match the pattern. Both leave a
 warning on the Actions run and nothing on the site. Look there first.
- **The workflow's allowlist decides what publishes.** Each morning the editor pushes to a
 temporary `claude/*` branch, and the workflow checks every file that run changed. If all
 of them are on the allowlist — `editions/*.html`, `index.html`, `morgue.md`, `README.md`,
 `correspondence.md`, `pressroom-report.md` — it fast-forwards `main` and the site updates.
 If even one file isn't, **nothing publishes**, the edition included, and the run leaves a
 warning in the Actions tab.
 The list has to be right in both directions. Too short: teach your paper to write some new
 file daily, forget to list it, and the whole paper goes quiet for no visible reason. Too
 long: add `master-prompt.md` and the editor can rewrite its own charter overnight and
 publish the new one before you read it. That file is left off on purpose.
- **The press room has no WebFetch.** In the cloud sandbox, `WebSearch` works and direct
 HTTP to news sites is blocked. `routine-prompt.md` already says so; keep that note alive
 in your rewrite, or your editor will read a 403 as "the news is unavailable" and file
 nothing.

Change the beat, the politics, the typeface, the hour, the century. Keep the printer.
If yours ends up better than this one, that is the correct outcome — and this page would
like the link.

# Show HN: One page personal calendar with hierarchy | Hacker News

## 关联链接

- https://YOUR-USERNAME.github.io/YOUR-REPO/`.
- https://claude.ai/code/routines,
- https://claude.ai/code/routines.
- https://lywald.github.io/zfrontpage/**

## 导航

- 项目页：[[10-项目/github.com_587161fc]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
