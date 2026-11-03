---
type: "corpus"
item_id: "4d374ab22f0c8860"
title: "Show HN: Election-vibe – US midterm results in your terminal and Claude Code"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50338267"
project_url: "https://npmjs.com/package/election-vibe"
author: "arturogarrido"
published_at: "2026-11-02T15:35:50Z"
captured_at: "2026-11-03T09:40:36+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-03"
pub_day: "2026-11-02"
tags:
  - 语料
  - hn_show
  - author_arturogarrido
  - story_50338267
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Election-vibe – US midterm results in your terminal and Claude Code

> [!info] 一句话导读
> US election night, Nov 3, 2026, in your terminal and in Claude Code: unofficial results from official free sources and civicAPI, kept on your machine. Never cal…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50338267>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：arturogarrido　|　发布：2026-11-02T15:35:50Z
> 项目链接：<https://npmjs.com/package/election-vibe>
> 采集：2026-11-03T09:40:36+08:00　|　id：`4d374ab22f0c8860`

## 正文

# election-vibe

US election night, Nov 3, 2026, in your terminal and in Claude Code: unofficial results from official free sources and civicAPI, kept on your machine. Never calls a race. Unofficial results. Not an election authority. Not affiliated with any government, c

- Version: 0.1.1
- License: MIT
- Author: Arturo Garrido
- Created: 2026-11-02T07:41:13.788Z
- Updated: 2026-11-02T15:42:52.896Z

## Keywords

- election
- midterms
- 2026
- results
- terminal
- cli
- statusline
- claude-code

## Dev Dependencies

| Package | Version |
| --- | --- |
| @types/node | ^22.20.5 |
| tsup | ^9.0.0 |
| tsx | ^4.23.15 |
| typescript | ^5.7.0 |
| vitest | ^5.0.5 |

## Version History

| Version | Published | Deps |
| --- | --- | --- |
| 0.0.0-stage | 2026-11-02T07:41:13.788Z | 0 |
| 0.1.0 | 2026-11-02T07:43:21.115Z | 0 |
| 0.1.1 | 2026-11-02T15:42:52.648Z | 0 |

---

## README

# election-vibe: election night in your terminal and in Claude Code (Nov 3, 2026)

Unofficial results for the US general election of November 3, 2026, in your terminal and in Claude Code (a results line above the prompt, the board in a pane), read from official free sources and a free public aggregator. Every governor, US Senate and US House race on the ballot nationwide (through civicAPI, and California's Secretary of State for California), with deep local coverage for eight California counties in the Bay Area and Los Angeles. It runs on your machine: one collector process reads the sources and keeps a local snapshot, and every command, the statusline and the plugin read that snapshot.

> Unofficial results. Not an election authority. Not affiliated with any government, campaign, or party.

## Get running for election night

You need Node 22 or later.

```bash
npm i -g election-vibe     # installs the `elections` command (also as `election-vibe`)
elections collect          # the collector: leave it running in its own terminal
```

Then pick how you want to watch:

- **In a terminal:** `elections watch` in another terminal (your followed and hot contests, redrawn every 10 s; q or Ctrl-C quits).
- **In Claude Code:** the plugin puts the results line above the prompt and the board in a pane (`/elections`); see In Claude Code.

Before Tuesday, follow what you care about: `elections find measure j palo alto`, then `elections follow ` (see Find a contest and follow it).

On Tuesday, after the polls close:

- **Races outside California** (civicAPI: governors, Senate, House, the 13 statewide measures, Phoenix) need nothing from you. They appear once civicAPI marks a record as real data updated after its polls closed.
- **California contests** read from the Secretary of State and the county offices need a one-time approval from you, per source, after polls close. Until then they show `awaiting production approval`. `elections admit --show` lists what is ready to approve: see the election night checklist below.

Without installing, put `npx election-vibe` where `elections` is (`npx election-vibe collect`, `npx election-vibe watch`). The statusline and the plugin need the global install.

## What you will see

Printed on Sunday, Nov 1, 2026, 9:39 PM PST, from real reads of the sources. Before the polls close, every contest looks like this: no counts yet, and the time its polls close.

`elections prompt` (the statusline line, and the line above the prompt in Claude Code):

```text
🗳 32 hot races · first polls close Nov 3, 4:00 PM PST
```

`elections board --width 72 --limit 5` (what the `/elections` pane shows, cut to 5 contests here; without `--limit` the board and the pane show up to 100, and `elections watch` is the same board, redrawn with every contest):

```text
elections · snapshot 9:39 PM PST (0m ago)

HOT
  Alaska Ballot Measure 2 - Repeal Ranked-Choice Voting and Open Primar…
    no source report dated after polls closed
  Alaska US Senate
    the source marks this as test data
  Arizona Governor
    the source marks this as test data
  Arizona Proposition 144 - Citizenship and Voter ID Requirements
    no source report dated after polls closed
  Mayor - Oakland (RCV)
    no source report dated after polls closed

+27 contests not shown: run `elections watch` in a terminal for all of
them.
```

`elections race "palo alto, transactions"` (one contest):

```text
Nov 3, 2026 · production results
Snapshot published Nov 1, 9:39 PM PST (0m ago)

Measure J - City of Palo Alto, Transactions and Use Tax
measure · no result yet
Polls close: Nov 3, 8:00 PM PST
▲ Santa Clara County Registrar of Voters: no source report dated after polls closed.

No accepted result from this source yet.

Santa Clara County Registrar of Voters · read 1h 31m ago
2026-11-03.ca.santa-clara.measure-j-city-of-palo-alto-transactions-and-use-tax.regular
Official results: https://vote.santaclaracounty.gov/view-election-results
```

"production results" in the race view's header names the store being read (results admitted after polls close), not a claim that any exist yet. A line starting with ▲ is a note about the source (here: nothing dated after polls close yet); ⚠ is a warning about the snapshot itself, and ✓ only a source's own call.

"the source marks this as test data" is civicAPI flagging its own pre-election records as test data; they become results once civicAPI serves real data after the polls close. Once counts arrive, a board row names the leader with their share, marked "leading" (never a win), and `race` shows every candidate's votes and the source's own report time.

## What it is, and what it is not

- **It shows counts as each source publishes them**, with the source named and the source's own report time (or "report time not stated" when the source states none).
- **It never calls a race.** "Leading" is computed from the counts and labeled as such. A contest shows "called by civicAPI" only when civicAPI itself flags a winner, and that is civicAPI's own call: not official, not certified. California's Secretary of State and the county sources publish no calls, so their contests show counts and leaders only.
- **No projections, no expected-vote estimates.** Precincts reporting is shown as precincts, never as votes remaining.
- **Bold and a check mark only for a source's own call.** Party colors (red Republican, blue Democratic) only on partisan contests, always beside the party letter; on a terminal only. Under `NO_COLOR`, or piped, the output is plain text with the same words.
- **Corrections are shown, not hidden.** Totals can go down in a newer report; the contest says so.
- **Late and stopped sources say so.** A contest whose source has not answered on its schedule is marked LATE, then NOT UPDATING; a source that refused access says so on its contests.
- **civicAPI is never called official.** A race view names the official results page of its source; for a civicAPI contest it names the jurisdiction's own page where one is recorded (Phoenix), and otherwise says "Results source: civicAPI (not an official source)". The `--json` twin says the same: `source.official` is false for civicAPI, and `source.officialLink` is only a link the registry holds (null otherwise).
- **Before results, the poll close.** A race view with no result yet prints when its polls close, in your display zone, with the contest's own zone beside it when they differ. The time is when the last polls in the state close (a state split across two zones closes with its later one), from a written table of each state's closing hours; civicAPI's own stated time is used only when it is later.

## Commands

```bash
elections watch            # followed and hot contests, redrawn every 10 s; q or Ctrl-C quits
elections list --preset hot
elections list --county santa-clara
elections race "palo alto unified"   # one contest; a query that matches several lists their ids
elections follow <contest id>
elections prompt           # one line for a statusline, from the local snapshot only
elections board            # the watch board printed once, 100 contests at most (what the plugin's pane shows; --color for the watch's colors)
elections sources          # each source's health, last revision and age
elections admit --show     # election night: every California source's approval state (approves nothing)
elections coverage         # what is covered and what is not
```

The collector prints one line per cycle (what it asked each source and what it kept); every other command reads the snapshot it wrote and never fetches. Before the polls close, contests read "no source report dated after polls closed" or "no result yet": that is expected. Everything served before then is test or zero-report data and goes to a separate test store, which `--store rehearsal` shows (every row marked TEST).

`list`, `race`, `find`, `sources`, `coverage` and `admit --show` take `--json` for scripts, with the same facts. `watch` is a screen: it redraws from the local snapshot only, never the network, and needs a terminal (piped, it prints one frame and says so). `prompt` and `board` print text only (`list --json` is their twin for scripts). Closing a reader never stops collection.

Times are shown in your computer's time zone; `--tz ` (for example `--tz America/New_York`) or `ELECTIONS_TZ` picks another.

### Find a contest and follow it

`find` searches the contest list on your machine (no network): every word must appear in a contest's title, county or id, and it prints each id. `race` takes its words as one phrase, punctuation included: it shows the one contest whose title or id contains that phrase (the comma in `"palo alto, transactions"` is part of it, as it is part of the title), or lists the ids when several match:

```bash
elections find measure j palo alto         # 1 match: its id and title
elections find measure j                   # 4 matches: each id and title
elections race "palo alto, transactions"   # one match: Palo Alto's Measure J, its race view
elections follow 2026-11-03.ca.santa-clara.measure-j-city-of-palo-alto-transactions-and-use-tax.regular
elections list --followed                  # what you follow; `watch` and `prompt` show it first
elections race "proposition 40"            # a statewide proposition: Yes and No counts
elections race "missouri amendment 3"      # a statewide measure outside California (civicAPI): Yes and No counts
elections list --state CA --level measure  # every California measure, statewide and local
```

`unfollow ` removes one. Follows are kept on your machine, in the data directory. A search that finds nothing means only that this list holds no such contest; `elections coverage` says what the tool covers, and `find` names a county it does not cover (Napa, San Francisco) with that county's official results page, and Virginia's ballot questions as not covered, with Virginia's official results page.

## In Claude Code

Two ways, both reading the same local snapshot. Pick one: in a terminal, using both shows the same line twice (once in the statusline, once above the prompt). Both need the global install (`npm i -g election-vibe`); `npx` leaves nothing installed for them to run.

### Option A: the statusline only

`prompt` prints one line for a statusline: your followed contests (or, with none followed, the hot races), one shown and the rest counted (`+N`). A source call or a withdrawn call from the last five minutes is shown first. It reads the local snapshot only: it never fetches, never starts the collector, and never prints an error (with no snapshot it says `no results yet · run: elections collect`). Before any of those contests' polls close it says when the first one does; a snapshot more than 10 minutes old is called out first (`⚠ results 14m old`). Same words as the board: "leading" is never a win, and ✓ marks only a named source's call. `--width N` (default 80), `--color` for color, `--store rehearsal` for the test store.

Add this `statusLine` key to `~/.claude/settings.json`, beside the settings already there; do not replace the file. A file has one `statusLine`: this replaces yours, if you have one.

```json
{
  "statusLine": { "type": "command", "command": "elections prompt --color" }
}
```

Keep a copy of your previous `statusLine` value: putting it back is the whole restore.

### Option B: the plugin (line above the prompt, board in a pane)

The package carries a Claude Code plugin: the same line above the prompt (in a terminal and in the desktop app's Code tab), and the results board in a pane with `/elections` (the `board` command's output in the watch's colors, monospaced, re-read every 10 seconds while the pane is open; `NO_COLOR` set where Claude Code runs keeps it plain). It needs no `settings.json` edit, and it installs nothing else: no statusline, no notifications. It runs the package's own `elections` from the installed package, reads the local snapshot only, and never starts the collector: start `elections collect` first, or the line says `no results yet · run: elections collect`. Install the package globally, then, in a terminal:

```bash
claude plugin marketplace add "$(npm root -g)/election-vibe"
claude plugin install election-vibe@election-vibe --config store=production   # production is the default, shown so you know the option
```

Installed at the user scope, it also loads in the desktop app's Code tab. Tested with Claude Code 2.1.316. The plugin is read from the installed package's folder, so after `npm i -g election-vibe@latest` run `/reload-plugins` (or start a new session). Its one option, the results store, is `production` (the default) or `rehearsal` (the test store, every row marked TEST): `--config store=rehearsal` on the install, or `/plugin configure election-vibe@election-vibe` later. To remove it: `claude plugin uninstall election-vibe@election-vibe`, then `claude plugin marketplace remove election-vibe`.

## Election night checklist: approving the California sources

Before the polls close, everything the sources serve is test or zero-report data and stays in a separate rehearsal store. A source that carries its own test flag (civicAPI) is admitted by itself once its record says it is not test data and was updated after its contest's polls closed: **contests read from civicAPI need no approval.**

The official sources carry no test flag, so each installation approves its first production report from each of them locally, once, after the polls close. These are the nine sources that need it (`elections sources` lists them with their state):

| Source id | Source |
|---|---|
| `ca-sos` | California Secretary of State: the California Governor, US House, State Senate and Assembly contests, and the 14 statewide propositions |
| `scc-clarity` | Santa Clara County |
| `smc-csv` | San Mateo County |
| `marin-clarity` | Marin County |
| `contra-costa-clarity` | Contra Costa County |
| `sonoma-clarity` | Sonoma County |
| `la-json` | Los Angeles County |
| `solano-html` | Solano County |
| `alameda-html` | Alameda County |

You only need the ones whose contests you watch: approve `ca-sos` for California's statewide and legislative contests, and a county for its local contests. For a California contest, civicAPI is only a cross-check: its numbers are not shown in place of an unapproved source.

What you can do before Tuesday: install, start the collector, follow your contests, and run `elections sources` to see each source answering. `admit` refuses an approval before the source's polls close (California's close at 8:00 PM PST).

On Tuesday, after 8:00 PM PST:

1. **`elections admit --show`** (no source named) lists every source that needs an approval, with its state: polls still open, no report read yet, a zero report ("do not approve yet"), ready, or already approved. Under each source with a report it prints the latest report the collector read, its report time, whether it carries votes, two or three of its contests with their counts from the test store (where an unapproved post-close report is held until you approve it; only contests the admission rule holds for approval count as evidence or are shown), and the source's official results page. It approves nothing.
2. For a source marked ready, open its official results page and check that the sample contests' counts match it (`elections race " " --store rehearsal` shows any other contest from the same report).
3. Paste the approval line printed under that source: `elections admit --revision --hash `. The line is printed only for a source whose polls are closed and whose latest report is held for approval by the admission rule (a report the source dates before polls close never is; a county report that states no time of its own is judged by the polls' close alone), is in the test store exactly as read, and carries votes. Otherwise the source says why, with no line.
4. A zero report is never approved: before counting starts, a source can serve a zero report stamped after polls close, and approving it proves nothing about the results to come. Wait for the collector's next read and run `elections admit --show` again.

`elections admit --show --json` is the twin for scripts. `elections admit --show` prints one source's latest report with its `--revision` and `--hash`, without the counts or the ready check.

Approving one report admits it and every later report from that source: you do not approve again as the counts update. If a newer report arrives while you are checking, approve the one you checked; the newer one follows it. After approval, any older report (a rehearsal file arriving late) is rejected.

Nothing is production while a contest's polls are open, whatever was approved. A clock passing a time never activates a source. Until a source is approved, its contests show "no source report dated after polls closed" before the polls close and "awaiting production approval" after. `elections admit --revoke` withdraws an approval.

## Coverage

### National and state

| Contests | Source |
|---|---|
| Outside California: 35 governors, 35 US Senate (including the Florida and Ohio specials), 383 US House | civicAPI |
| Nevada: Nevada Governor and all four U.S. House contests (part of the row above) | civicAPI |
| California Governor, 52 US House, 20 State Senate, 80 State Assembly | California Secretary of State (civicAPI as a cross-check) |
| California's 14 statewide propositions (1 to 5 and 37 to 45): Yes and No counts only, never passed or failed | California Secretary of State |
| 13 statewide ballot measures outside California: Alaska Ballot Measure 2, Arizona Proposition 144, Colorado Amendment 86, Idaho Proposition 1, Maryland Question 3, Massachusetts Question 3, Question 4 and Question 8, Missouri Amendment 3 and Proposition A, Nevada Question 6 and Question 7, Ohio Issue 3. Yes and No counts only, never passed or failed; each record checked one by one (its exact title, its state, Yes and No) | civicAPI (not an official source) |

Nationwide that is all 36 governors, 35 US Senate and 435 US House contests on the ballot. California has no US Senate race this year. Nevada's own results come through civicAPI only: the state's site refuses automated requests, and its official election information is at https://nvsos.gov/sos/elections/election-information/2026-election-information (not a results feed this tool reads).

Territorial governorships (Guam, the US Virgin Islands and the other territories) are out of scope by decision, not a coverage gap.

### Counties (local contests)

| County | Covered | Source | Official results |
|---|---|---|---|
| Santa Clara | Covered: 93 local contests | Santa Clara County Registrar of Voters | https://vote.santaclaracounty.gov/view-election-results |
| San Mateo | Covered: 91 local contests | San Mateo County Elections Office | https://smcacre.gov/elections/november-3-2026-election-results |
| Marin | Covered: 60 local contests | Marin County Elections Department | https://www.marincounty.gov/departments/elections/november-3-2026-general-election/election-results-110326 |
| Contra Costa | Covered: 71 local contests | Contra Costa County Elections Division | https://www.contracostavote.gov/november-3-2026-election-results/ |
| Sonoma | Covered: 49 local contests | Sonoma County Registrar of Voters | https://sonomacounty.gov/administrative-support-and-fiscal-services/registrar-of-voters |
| Los Angeles | Covered: 316 local contests | Los Angeles County Registrar-Recorder/County Clerk | https://results.lavote.gov/#year=2026&election=4348 |
| Solano | Covered: 38 local contests | Solano County Registrar of Voters | https://www.solanocounty.gov/unofficial-election-results |
| Alameda | Covered: 112 local contests | Alameda County Registrar of Voters | https://acvote.alamedacountyca.gov/election-information/elections?id=260 |
| Napa | Not covered: the county offers no automated results path | | https://www.napacounty.gov/402/Election-Results |
| San Francisco | Not covered: the county offers no automated results path | | https://www.sfelections.org/results/20261103w/detail.html |

| Other contests | Covered | Official results |
|---|---|---|
| Phoenix City Council districts 2, 4, 6, 8 | Covered: 4 contests (civicAPI, each record checked against the city's certified candidates; a majority wins outright, otherwise a March 9, 2027 runoff) | https://www.phoenix.gov/administration/departments/cityclerk/programs-services/elections/november-election-26.html |
| DC Mayor; DC Board of Education wards 3 and 5 | Not covered: no qualified automated source | https://electionresults.dcboe.org/ |
| Virginia ballot questions (Constitutional Amendment Questions 1, 2 and 3) | Not covered: the only automated source lists each question twice with nothing to tell the copies apart | https://results.elections.virginia.gov/ |

What "covered" means: every contest listed for a county comes from that county's own results feed. Whether each county's list is its complete local ballot is not yet reconciled, and the tool never shows a county as "fully covered". Statewide and state legislative contests for every California county come from the Secretary of State. Run `coverage` for the current statement per county.

How local results are shown:

- **Partial results say so.** A district that spans counties shows "partial jurisdiction" when only one county's share is read. A ward or trustee area is called partial only when another county's file carries the same ward; otherwise it says "scope unconfirmed", because the ward may lie wholly in one county.
- **Ranked-choice contests in Alameda County show first choices only**, as the county's results page publishes them; no rounds are computed.

## Sources and attribution

- **civicAPI** (https://civicapi.org): national contests outside California. Results data by civicAPI.
- **California Secretary of State** (https://electionresults.sos.ca.gov/): California's statewide and legislative contests and its statewide propositions.
- **County election offices** listed above: local contests.

Requests are paced per installation: one collector, a few documents per source every 5 to 10 minutes, and civicAPI one request at a time with followed and preset contests first (about 0.6 requests per second with the default pacing). A source that throttles is backed off; a source that refuses access is stopped until you look into it, and `elections enable ` asks it again (a new refusal stops it again). Any source can be silenced locally with `disable `.

## Running the collector

The collector is a foreground process: leave it in its own terminal, or run it in the background and read its log:

```bash
nohup elections collect > /dev/null 2>&1 &
tail -f ~/.local/state/elections-companion/2026-11-03/collector.log
```

It writes one line per cycle to `collector.log` in the data directory, and the same line to its terminal.

You can start it any time before Tuesday and leave it running. Until a source's first contest closes its polls, the collector reads that source about once every 6 hours (test and zero reports, kept in the test store); from then on it reads on its election-night pace. It never needs a restart for polls closing. `find`, `list` and `race` work even before the first collect: the contest list ships in the package (only the results need the collector).

On a Mac, `caffeinate -i elections collect` keeps the machine from idle sleep while the collector runs (closing a laptop's lid still sleeps it). If your laptop sleeps, the collector sleeps with it and carries on when it wakes; while it sleeps nothing is read, and the readers say how old the snapshot is (`⚠ results 14m old`). Keep the machine awake on election night if you want current results.

### Updating during election night

A running collector does not update itself. To take a fix:

1. Stop the collector: Ctrl-C in its terminal, or, for a background one, `kill ` with the process id `pgrep -f "elections collect"` prints. It finishes the read in progress, publishes, and exits.
2. Update: `npm i -g election-vibe@latest`, then `elections --version`.
3. Start it again: `elections collect`. (With npx: `npx election-vibe@latest collect`.)
4. With the plugin: `/reload-plugins` in Claude Code.

Run one collector per data directory. The lock enforces it as far as a plain file can: a running collector renews it every 30 seconds, and a collector that finds another took over, or that another collector published since its cycle began, stops without publishing. What a file lock cannot rule out is two collectors claiming within the same few milliseconds.

The snapshot survives a stop, a crash or a killed process: the restarted collector carries on from it. If the old process was killed rather than stopped, the restart takes over its lock at once; while another collector is still running on the same data directory, the start is refused and names that process.

## Operating window

Collection is supported through **Wednesday, November 4, 2026**. The collector does not stop itself on that day: stop it (Ctrl-C) when you are done. Once it stops, nothing claims to be current: every view shows the snapshot's age, contests go LATE and then NOT UPDATING as their sources' schedules pass, the statusline line warns once the snapshot is more than 10 minutes old, and nothing is ever labeled final. Counting continues for weeks (California certifies by December 11); for final results, use each source's official page.

## Where it keeps its data, and removing it

Everything lives in one data directory: `~/.local/state/elections-companion/2026-11-03/` (under `$XDG_STATE_HOME` when that is set; `--data-dir ` or `ELECTIONS_DATA_DIR` picks another). It holds the snapshots, your follows and approvals, and the collector's log: a few megabytes, plus a line per cycle in the log.

No account, no telemetry. The collector contacts only the sources listed above; every other command, the statusline line and the plugin read files on your machine and make no network request.

To remove it all, in this order (the plugin lives inside the package's folder, so remove it first):

1. Stop the collector.
2. If you installed the plugin: `claude plugin uninstall election-vibe@election-vibe`, then `claude plugin marketplace remove election-vibe`. If you changed your statusline: put your previous `statusLine` back.
3. `npm rm -g election-vibe`.
4. Delete the data directory.

## FAQ

**What is civicAPI?** A free public aggregator of election results (https://civicapi.org). It is not an official source, and this tool never calls it one. Its winner flag is civicAPI's own call, shown as "called by civicAPI". The collector asks it one request at a time, at least 1.1 seconds apart.

**What is `--preset hot`, and are there other presets?** `hot` is the only preset: 32 contests (Senate and governor races, the hot statewide measures and a few California contests), chosen by the package's author, each with a recorded reason and a public link. `elections list --preset hot` lists them. The collector reads them, and the contests you follow, first. `watch` and the pane show them after your followed contests; `prompt` shows them when you follow nothing.

**Do I need `admit` if I only follow national races?** Only if one of them is in California. Contests read from civicAPI (every governor, Senate and House race outside California, the 13 statewide measures, Phoenix) need no approval: civicAPI's own test flag and post-close time admit them. California's own contests (its Governor, its 52 US House races, its legislature, its propositions, and the county contests) come from the California sources, which each need one approval; see the checklist.

**Why are San Francisco and Napa linked instead of read?** Neither county offers an automated results path this tool can use, and it never works around a site's bot protections. Their rows link the official results pages.

**Does collection stop on November 4?** No: the collector runs until you stop it. November 4 is how long the tool is supported; see Operating window.

**Does this run on Windows?** Not tested. This release was built and tested on macOS. The CLI uses only Node, but the plugin assumes a macOS or Linux shell path, and nothing here has been tried on Windows or Linux.

**Does `race` treat the comma as part of the query?** Yes. `race` takes its words as one phrase, punctuation included, and looks for it in titles and ids: `"palo alto, transactions"` matches Palo Alto's Measure J because its title contains that phrase. `find` is the one that matches word by word.

**Does `prompt` have a `--json` twin?** No. `prompt` and `board` print text; `list --json` (with `--followed` or `--preset hot`) carries the same facts for scripts.

**Which Claude Code version?** The plugin was tested with Claude Code 2.1.316. To update: update the package, restart the collector, then `/reload-plugins`. To remove: the plugin before the package (see above).

**Does it work behind a corporate proxy?** It connects to the sources directly and does not use a proxy (`HTTPS_PROXY` is not read). On a network that inspects HTTPS or blocks direct connections, the reads fail, and `elections sources` says why for each source (for example "the connection's certificate is not trusted").

**How do I pick the display time zone?** `--tz ` on any command, or `ELECTIONS_TZ`. The default is your computer's zone.

**How much disk does it use?** A few megabytes for the snapshots, plus one log line per collector cycle.

**What license is it under?** MIT.

## Problems and contact

A broken source, a wrong display, a question: @arturogarrido on X (https://x.com/arturogarrido).

# GitHub - HYXZKAKONHNK/ViBrow: ViBrow — кастомный Python-браузер с собственным DOM, CSS и JS движками. Имеет многовкладвочный интерфейс, локальный кэш, cookies, встроенный поисковик и прокси-мост для обхода блокировок. Был создан 1 разработчиком, без сторонних библиотек. Потребляет 30-65МБ ОЗУ, нужен 700МГц процессор 1 ядро и 200МБ ОЗУ LPDDR1. Работает на чистом Python · GitHub

## 评论（1/1）

> **andunie** · 2026-11-02T16:04:29.000Z　
> interesting idea for people deep into AI psychosis, but I imagined it would offer commentary, say who is winning, what are the most important events to look up for, that kind of thing

## 关联链接

- https://acvote.alamedacountyca.gov/election-information/elections?id=260
- https://civicapi.org
- https://electionresults.dcboe.org/
- https://electionresults.sos.ca.gov/
- https://nvsos.gov/sos/elections/election-information/2026-election-information
- https://results.elections.virginia.gov/
- https://results.lavote.gov/#year=2026&election=4348
- https://smcacre.gov/elections/november-3-2026-election-results
- https://sonomacounty.gov/administrative-support-and-fiscal-services/registrar-of-voters
- https://vote.santaclaracounty.gov/view-election-results
- https://www.contracostavote.gov/november-3-2026-election-results/
- https://www.marincounty.gov/departments/elections/november-3-2026-general-election/election-results-110326
- https://www.napacounty.gov/402/Election-Results
- https://www.phoenix.gov/administration/departments/cityclerk/programs-services/elections/november-election-26.html
- https://www.sfelections.org/results/20261103w/detail.html
- https://www.solanocounty.gov/unofficial-election-results
- https://x.com/arturogarrido

## 导航

- 项目页：[[10-项目/npmjs.com_5663dd5e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
