---
type: "corpus"
item_id: "1eff0532efaf5002"
title: "Show HN: Proxy-benchmark – is it the proxy, the browser, or your machine?"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49752694"
project_url: "https://github.com/nodemaven/proxy-benchmark"
author: "pia-nm"
published_at: "2026-09-18T11:13:46Z"
captured_at: "2026-09-21T21:59:53+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - hn_show
  - author_pia-nm
  - story_49752694
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Proxy-benchmark – is it the proxy, the browser, or your machine?

> [!info] 一句话导读
> nodemaven/proxy-benchmark

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49752694>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：pia-nm　|　发布：2026-09-18T11:13:46Z
> 项目链接：<https://github.com/nodemaven/proxy-benchmark>
> 采集：2026-09-21T21:59:53+08:00　|　id：`1eff0532efaf5002`

## 正文

# nodemaven/proxy-benchmark

Measurement harness for proxy providers, browser engines and scraping targets. Every claim carries the run it came from.

- Stars: 14
- Forks: 0
- Watchers: 14
- Open issues: 0
- License: MIT License
- Homepage: https://go.nodemaven.com/ghbenchmark
- Default branch: main
- Created: 2026-08-25T13:18:31Z

## Languages

- Makefile
- Python

## Topics

- anti-detect-browser
- benchmark
- bot-detection
- browser-fingerprinting
- playwright
- proxy
- python
- reproducible-research
- residential-proxy
- scraping
- tls-fingerprinting
- web-scraping

## Top Contributors

- alkaz-nodemaven (79 contributions)

---

## README

# proxy-benchmark

**Find out what is blocking your requests - the proxy, the browser, the host, or
the target itself.**

Built and maintained by NodeMaven, who sell
proxies. Every number here is generated from the run files in `data/runs/`,
which are committed, so a reader can recompute any of them rather than take
them.

gate
license

python
rows

Six targets, chosen because they fail differently rather than because they are
popular: `google_serp`, `bing_serp`, `ddg_serp`, `amazon_search`,
`walmart_search`, and `ipinfo` - which is not a target but an echo service, used
to prove the path works before anything is concluded from a refusal.

## What the rows carry

Every attempt writes one JSONL row: engine and engine version, target, provider
and gateway parameters, country, preset, headful, geo, entry shape, warm-up rung,
session and query, the machine it ran on, the verdict and the marker counts
behind it, the failure reason, timing, and bytes. `ROW_FIELDS` in
`nmbench/engines/base.py` is the schema. Those files are the source of truth, and
the tables in this README and in `RESULTS.md` are generated from them - a number
nobody has to remember to update is a number that cannot drift.

**Verdicts come from page content, not HTTP status.** The same Google reCAPTCHA
page arrived once as 429 and once as 200, so a run judged by status
scores the second as a success. There is no boolean `success` column:

| verdict | what it means |
|---|---|
| `ok` | the target returned the page that was asked for |
| `captcha` | a challenge stood in front of the result |
| `consent` | a consent or cookie wall stood in front of the result |
| `block` | the target refused explicitly |
| `empty` | a body arrived and the result was not in it |
| `error` | the attempt never completed - the harness, never the target |

The last two are the ones that decide whether a benchmark measures anything:

- **`empty` is not `block`.** Google hands a scriptless client a 92 KB "enable
 JavaScript" scaffold that stays on `/search` and rejects nothing, so scoring it
 as a block credits Google with a refusal it never made. 14 of 14 such rows
 carried `enablejs` and none carried `recaptcha`.
- **`error` is ours.** A timed-out selector, a browser that would not launch and
 a query that never reached the box produced no evidence, so they produce no
 verdict. A harness that counts its own crashes as target refusals can
 manufacture a very convincing result while measuring almost nothing.

Seven more columns are easy to misread:

- **`host` was added on 2026-09-02, so an absent one means "nobody wrote it
 down", not "the machine was unknown".** Every row before that date is
 attributed to a machine by its timestamp, which works only because the two
 machines here happened to run at different times - host and date are one
 variable under two names in every table built from those rows. This matters
 more than a provenance column usually would: the largest unexplained result in
 this repository is a difference between two computers, 39% (24/61) against 0%
 (0/84) at p = 3.7e-11 on the same target, engine, entry shape and gateway
 parameters, and nothing on disk could name which computer. `host_os` and
 `host_cpus` sit beside it because a label groups rows and does not explain
 them. Set `NMBENCH_HOST` to the machine's name in the notes; unset, the column
 holds a hash of the hostname, because these files are public and a hostname
 names somebody's infrastructure.
- **`tls_ja4` is empty on most rows for a structural reason, not a missing
 one.** It is the engine's JA4, read off the ClientHello as it passes through
 the local CONNECT relay, so only the engines that need that relay have one -
 `zendriver`, `seleniumbase` and `botasaurus`. The Playwright-driven engines
 take proxy credentials directly and never send a handshake through this
 process, so their rows carry `null` and the `relayed` column beside it says
 why. Measured 2026-09-02 over `data/runs/`, that is 3815 of 16579 attempt
 rows. The fingerprint is computed in `nmbench/tlsfp.py` rather than asked of
 an echo service, and it was checked against one: on the same client,
 `tls.peet.ws` and this repository agree character for character.

 Every engine can still be fingerprinted, off the run, with
 `python scripts/probes/tls_clienthello.py`. It points each engine in turn at
 a listener on this machine that answers nothing, so it needs no live host and
 spends no traffic, and it reaches the Playwright-driven engines the relay
 route cannot.
- **A JA4 is a property of the browser build at least as much as of the
 engine.** Measured 2026-09-02 with the `chromium` engine and nothing varied
 but the binary: Playwright's bundled Chromium 151.0.7922.34 gives
 `t13d1516h2_8daaf6152771_806a8c22fdea`, and the installed Chrome
 149.0.7827.201, reached with `--channel chrome`, gives
 `t13d1516h2_8daaf6152771_d8a2da3f94cd`. The extension lists are byte for byte
 the same and so is the cipher hash; the whole difference is three signature
 algorithms, `0904,0905,0906`, that the newer build offers and the older one
 does not. That is why the same probe puts `chromium` and `patchright` in one
 group and `zendriver`, `seleniumbase`, `botasaurus`, `cloak` and `curl_cffi`
 in another - it is the Chrome version each happened to launch, not anything
 the libraries do differently. Read `engine_version` beside this column before
 treating a split as a property of the engine.

- **A refused address diverts the request, and the status does not say so.**
 Google answers a refusal by sending the request to `/sorry/`, with a 200 about
 a quarter of the time. `report.was_served` - a 200 whose final URL keeps the
 host and path asked for - is the test, and it is a property of the exchange, so
 nothing has to know a target's name.
- **A batch is one session, and a session is the unit.** Ten queries through one
 browser is one identity doing ten searches; ten browsers doing one query each
 is a different experiment. The claim has been false once - until 2026-08-11
 Camoufox opened a fresh context per query and discarded its cookie jar while
 every other engine carried one - and `session-continuity` is the offline probe
 that caught it.
- **`bytes` is two measurements and `relayed` says which.** Playwright engines
 count through `page.route` and see page resources; the relay counts sockets and
 sees request headers and TLS overhead as well. Never pool them. The relay figure
 is what a provider bills, and it adds a loopback hop, so `elapsed_ms` is not
 comparable across `relayed`.
- **The matrix carries an unmodified control.** `chromium` is Playwright's
 Chromium with no arguments, no user agent override and no patches;
 `navigator.webdriver` is `true` and stays that way, because without it a pass
 rate cannot be told apart from the target letting everything through.
 `tests/test_engines.py` reads the source of `ChromiumEngine.open` and fails if
 `args=` or `user_agent` appear.

**Response bodies are kept, gzipped.** A verdict is one word about 92 KB of
markup, and the question that decides a report is usually asked after the run.
Non-`ok` bodies plus a sample of the passes, controlled by `--no-bodies` and
`--sample-ok`. The archive is gitignored, unlike `data/runs/`, because exit
addresses appear in embedded links. Re-reading 250 stored Amazon bodies offline
found an Akamai interstitial and an AWS WAF challenge filed as refusals, and moved
21 historical rows at no traffic cost.

## Results at a glance

What the current evidence supports, engine by engine and target by target, from the 10432 attempt rows in `data/runs/benchmark_*.jsonl`. `pass` is `ok` over judged attempts - harness and path failures are counted separately and excluded from the denominator, because an engine that crashes is not an engine the target refused.

| target | best | worst | rows |
|---|---|---|---|
| `amazon_search` | `chromium/none` 96% (419/436) | `patchright/none` 63% (288/457) | 3816 |
| `google_serp` | every engine below 5%, best is 1.1% (5/460) - **not an engine comparison - the whole column is one browser on one host that this target refuses** | - | 3811 |
| `bing_serp` | `chromium/light` 100% (45/45) | `http-direct` 76% (34/45) | 372 |
| `ddg_serp` | `camoufox/light` 100% (44/44) | `chromium-direct/light` 22% (10/45) | 339 |
| `walmart_search` | no cell reaches 30 judged attempts, so no engine is named | - | 35 |

On the one target with enough evidence to rank engines, the top of the table is a **tie and not a podium**: `chromium`, `rebrowser`, `botasaurus`, `camoufox`, `zendriver`, `seleniumbase` sit within 4 points of each other and a two-sided Fisher exact, corrected for the 7 comparisons made, separates none of them. The first of them is `chromium`, which is the unmodified control.

Amazon and the two smaller search engines are a win. **The Google row is not an engine comparison and must not be quoted as one.** Every cell of it was taken on one Linux VPS. Run again with the same engine through the same gateway, a Windows workstation was served 39% (24/61) against 0% (0/84) from the VPS, two-sided Fisher p = 3.7e-11; cut to the one window where both machines were running at once it is 36% (8/22) against 0% (0/10), p = 0.035. The floor is real, it belongs to that client, and it is not a property of the proxies.

**Full tables -> RESULTS.md** - the 130-hour run (`benchmark_20260819T055927Z`, 2026-08-19 06:00 to 2026-08-24 16:12 UTC) engine by engine, Google day by day, and everything measured before it, split by host and by path.

**Three row counts appear on this page and they count different things.** The
badge counts every line in the committed `data/runs/*.jsonl` - matrix runs,
probe-and-hold windows, fingerprints, gateway checks. The table above counts only
matrix attempts that carried a query, which is `benchmark_*.jsonl` minus the
plan and summary lines. The `rows` column is per target within that. Each is
generated from the files and a test fails when the badge and the files disagree.

## Research findings

Everything below was measured with this harness between 10 August and 1 September
2026, and none of it is a standing fact about the internet: a target's defences
move, so a rate measured in that window is evidence about that window. The dates
sit here once rather than on each line, because a reader deciding whether to
trust one of these needs the run id and the denominator, and those live in the
section each line links to along with the date it stopped being true.

- **Chrome spends 43 MB per fresh profile talking to Google before you ask it
 for anything.** 43.2 MB of a 43.4 MB idle window on
 `optimizationguide-pa.googleapis.com`, on a browser parked on `about:blank`.
 At one profile per attempt that is about 43 GB per thousand attempts, billed
 as residential traffic, for a file no target ever sees.
 How it was counted
- **On Amazon the unmodified browser finished in the leading group.** Stock
 Chromium 96% (419/436) against 63% (288/457) for the lowest anti-detect
 engine, over 3530 judged Amazon attempts in one 7630-row run. Six engines sit
 within four points at the top and no test separates them, so the top of that
 table is a tie rather than a ranking - and the control is inside it.
 Full table
- **The same code, gateway and target scored 39% on one machine and 0% on
 another.** 24/61 from a Windows workstation against 0/84 from a Linux VPS in
 overlapping hours, Fisher p = 3.7e-11. The client machine is a variable a
 proxy comparison usually holds fixed without saying so.
 The split
- **On DuckDuckGo one substring in the User-Agent accounted for the whole
 split.** 95 of 95 pass for engines whose UA omits `HeadlessChrome`, 0 of 50
 for the two that carry it, across three browser families and two drivers.
 Nothing else varied moved it, so a headless Chromium measured there is
 reporting its own UA rather than its exit.
 The split
- **On Google the exit address dominated everything else we varied.** Given a
 served page, pass was 83 of 83 and did not vary by country, while the chance
 of being served ran from 13% to 62% depending on the exit. The browser did not
 separate the cells, and no absolute rate here should be read as current.
 The decomposition
- **The TLS handshake explains neither Google nor Amazon.** Chromium, Patchright
 and Obscura emit a byte-identical ClientHello and their pass rates differ by
 44 points. If you do compare, compare JA4 - Chrome shuffles extension order
 per connection, so a JA3 difference between two Chromium engines is noise.
 What was read
- **None of the Chromium-driving engines changes its TLS fingerprint, and the
 fingerprint tracks the Chrome version instead.** Measured 2026-09-02 over nine
 engines on one host: `rebrowser` on Chrome 136, `cloak` on 146 and
 `seleniumbase` on 149 emit one identical JA4, `chromium` and `patchright` on
 151 emit a different one, and the split follows the browser version with
 nothing left over for the library. Their HTTP/2 fingerprint is identical too.
 So a JA4 being compared between these tools is a stock Chrome's, because
 underneath it there is one - and if a target is refusing you, the handshake is
 not what told it. `curl_cffi` is the exception that shows the rule: it is the
 only engine here that picks a fingerprint deliberately, and it picked Chrome's.
 The groups
- **Timezone and locale alignment did not pay off in either arm we ran.** Flat
 on Patchright (34% against 35%), and zendriver lost six sevenths of its yield,
 57% down to 9%, p = 0.0008. Two engines is a thin basis for a rule, but
 nothing measured here argues for switching it on.
 Both arms
- **Our own harness was getting the pool banned.** One unauthenticated CONNECT
 per session, sent by the browser before anything else, was tripping an IP ban
 that looked like a gateway floor for days.
 How it was found
- **One page of warm-up moved nothing in our window.** 32% against 30%,
 intervals almost coincident. This refutes nobody: the protocol came to us from
 an operator, and the 75% that travels with it was mentioned in conversation as
 a figure once reached - not as a before-and-after pair, and with no
 denominator behind it. What our arm rules out is one page, which is what the
 ladder now goes past.
 The ladder
- **Six pages of warm-up moved a great deal, and it held on three separate
 days.** Four rungs interleaved inside one run, because the hour is the largest
 confound here: **11%, 24%, 33% and 82%** at warm depths 0, 2, 4 and 7, over
 35, 34, 33 and 33 judged attempts, cold against deepest z = 5.82. Two later
 runs carried the cold rung and the deepest rung alone and read 24% against 86%
 over 88 and 86 attempts, and 19% against 84% over 42 and 61. Pooled over the
 three days, **20.0% (33/165) cold against 84.4% (152/180) at depth 7**,
 z = 12.0. Every attempt is Chrome 151.0.7922.34, headful, through Patchright,
 on one host, and every figure is the probe phase judged as served against
 challenged. What the depth is *doing* is not in these rows: four of the six
 pages are Google's own, so "Google's infrastructure was told about this exit"
 and "the browser lived through six navigations" both fit every row. The rung
 that separates them holds the depth at six and swaps the four Google surfaces
 for third-party pages carrying the same tags; it is declared in the target and
 has no rows on disk, so what is published here is an effect without a
 mechanism.
 `data/runs/probehold_20260831T222129Z.jsonl`,
 `data/runs/probehold_20260901T210934Z.jsonl`,
 `data/runs/probehold_20260904T000605Z.jsonl`

**Five of these eleven replaced an earlier claim of ours, and both versions are
still in the notebook** - Amazon, the warm-up, the Google levels, the idle
traffic and the ban. The Amazon one reversed outright: on a workstation in early
August, Camoufox was served 90% while every Chromium engine met the throttle,
which read as a Firefox-against-Chromium result. On the server the unmodified
control came out on top and the Firefox reading was gone. A number here is a
reading of the hours it was taken in, and the ones that changed are labelled
rather than quietly edited.

## Setup

Python 3.11 or newer, run from a checkout. There is no `[project]` section to
install, because the committed query lists and `data/` are part of the instrument.

 python -m venv .venv
 .venv\Scripts\Activate.ps1 # macOS, Linux: . .venv/bin/activate
 pip install -r requirements-dev.txt
 python -m playwright install chromium
 python -m patchright install chromium
 python -m rebrowser_playwright install chromium
 python -c "import cloakbrowser; cloakbrowser.ensure_binary()"
 camoufox fetch
 copy .env.example .env # macOS, Linux: cp .env.example .env

Playwright, Patchright, rebrowser and cloakbrowser pin four different Chromium
builds and **no two share a download**, so a fresh machine fetches four browsers -
the build is what several findings here are about. `zendriver`, `seleniumbase` and
`botasaurus` download nothing and drive the host's installed Chrome, so a machine
without Chrome loses three engines and the rest carry a build nobody pins.

None of it is mandatory. An engine whose dependency is missing reports itself
unavailable and names the install command; the rest of the matrix runs.
`--dry-run` prints that list, so run it first on a new machine.

**Headful on a headless host needs `xvfb-run -a`.** `--headful` is the difference
between `Chrome/...` and `HeadlessChrome/...` on the wire, which is the whole of
the DuckDuckGo finding. A virtual display does not restore the GPU, so WebGL falls
back to software and a headful server run is not a headful workstation run.

Obscura is not on PyPI. Download the **`-stealth`** archive, unpack it, put the
directory on PATH. The plain archive is a different build and the stealth patches
are the thing being measured.

`.env` holds `NODEMAVEN_LOGIN`, `NODEMAVEN_PASSWORD`, `NODEMAVEN_HOST` and
`NODEMAVEN_PORT`. **The prefix is the provider id**, so `oxylabs.toml` reads
`OXYLABS_LOGIN` and two accounts sit in one `.env` - which is what a matrix
interleaving two providers needs. `.env` is gitignored, `config.py` is the only
reader, and it resolves on first use so everything else imports and tests on a
machine with no account.

Before spending anything:

 make check # ruff plus the offline suite
 python scripts/benchmark.py --dry-run

The suite is offline. A green suite is the precondition for spending traffic.

## Running it

`python -m nmbench` lists every command, what it answers, and which ones spend
traffic. It is a dispatcher: the remaining flags go to the script untouched, and
every script still runs directly by path.

 python -m nmbench # what exists, and what it costs
 python -m nmbench benchmark --dry-run
 python -m nmbench engine-fingerprint # offline, sends nothing

A first matrix, one engine against the unmodified control:

 python scripts/benchmark.py --engines patchright,chromium \
 --targets google_serp --queries 40 --batch 10 --headful

The `:direct` suffix puts the same browser on both sides of the gateway inside one
window; two runs an hour apart would measure the hour as well. A global `--direct`
forces every cell direct and cannot be partly undone by a spec that omitted the
suffix.

 python scripts/benchmark.py --engines chromium,chromium:direct,camoufox \
 --targets amazon_search --queries 100 --batch 10

Resume skips attempts already judged, so an interrupted run does not re-ask the
targets:

 python scripts/benchmark.py --resume data/runs/benchmark_.jsonl

Then read what it said, and what it really cost:

 python scripts/analysis/report.py
 python scripts/analysis/calibrate.py

### Entering through the front page

Arriving at `/search?q=` is one request carrying a query string, with no keystroke
behind it, no referrer and no form submission - a shape no person produces. It is
now an axis: `entry` is on every row, `url` for that shape and `home` for landing
on the front page and typing into the box.

 python scripts/probes/probe_and_hold.py --engines patchright,zendriver \
 --identities 20 --series 3

The protocol is an operator's: one sticky exit per session, type on the front
page, drop the address if the probe is refused, hold it for a series if the probe
is served. Read the result with `scripts/analysis/held.py`.

### The warm-up ladder

The operator's protocol above includes opening a page or two on the target before
asking it anything, and a figure of 75% travels with it. Measured here, one page
moved 32% to 30%.

Be careful what that is being compared against, because this document was not for
two days. The 75% reached us in conversation, as a number an operator had once
seen on their own pool, country mix and hour. It was never stated as a
before-and-after pair, so there is no 20%-to-75% effect to fail to replicate and
no claim of anyone's to refute. What this arm has is its own denominator, and
that is all it has.

That result has two readings and one arm cannot tell them apart: either warming
does nothing, or **one page is not warming**. `--warm` is a ladder rather than a
switch so the second reading gets a denominator.

| rung | what it opens | what a gap to the rung below isolates |
|---|---|---|
| `L0` | nothing. The exit meets the target for the first time at the probe | the baseline every row taken before 2026-08-26 was measured at |
| `L1` | one page of the target's own | whether being seen once before the query is worth anything |
| `L2` | several of the target's surfaces, on more than one host | one visit against several. Separates "seen at all" from "seen more than once" |
| `L3` | `L2`, preceded by third-party pages | whether an exit is better off arriving from somewhere else. The third-party pages carry the target's own analytics and ad tags, so the exit is reported to its infrastructure without a navigation to it |
| `N1` | one third-party page, not the target's | against `L1`: whether one visit has to be the target's own to be worth anything |
| `N3` | six third-party pages | against `L3`: whether the 82% is the depth or the four Google surfaces inside it |

`N1` and `N3` are controls on **composition**, not steps in depth. Each matches
the delivered page count of the chain rung it answers and shares none of that
rung's target-owned pages, which is why they are excluded from the cumulativeness
rule below - being a superset of the rung they control is the one thing they must
not be. Neither is a Google-free arm and the output should not be read as one:
`entry=home` navigates to the front page before it can type, so every arm
contacts the target immediately before the probe.

Three things make the gaps readable rather than decorative:

- **The rungs are cumulative and each ends on the same page.** `L3` is a strict
 superset of `L2`, which is a strict superset of `L1`, and all three finish on
 the page `L1` visits before the front page. So whatever `L1` buys is held while
 the rungs above it vary, `warm_depth` is an ordering, and a difference between
 two rungs is a difference in **what was added** rather than in two unrelated
 sequences. A test enforces this rather than a comment asking for it.
- **All rungs interleave in one process.** The hour is the largest confound this
 repository has: the same gateway, country and browser moved 69 points to 52
 between two windows of one afternoon, and the same target went
 39% on one host and 0% on another in overlapping hours. Rungs run one after
 another would price the hour and call it depth.
- **The pages belong to the target, not to the probe.** A probe that knew a
 domain would be a probe that could warm one target better than another. A rung
 a target has not declared is refused rather than answered with a shorter one,
 because a row labelled `L3` whose warm-up was `L1`'s is a wrong result and not
 an error - it looks exactly like the deeper warm-up not helping. `amazon_search`
 declares `L1` only: the rungs above it were designed against Google's refusal
 and nothing here says they transfer.

 python scripts/probes/probe_and_hold.py --targets google_serp \
 --warm off,L1,L2,L3 --identities 24 --series 5 --dwell 20,45

For a run nobody is going to watch, `scripts/run_ladder.py` wraps that one
command. It does not change the shape of the experiment - the rungs still
interleave inside a single process, because a supervisor that ran them in turn
would reintroduce the confound the interleaving exists to remove. What it adds
is a preflight that refuses a bad plan or a dead pool in seconds rather than at
hour three, a log per attempt under `data/logs/`, and a restart rule that is
deliberately narrow: an attempt is retried only if it died within ten minutes,
because a run that fell over on startup has lost nothing while one that fell
over at hour two is worth more than a second attempt at a different hour. Two
attempts are two run files, and the summary says not to pool them.

It also defaults to `--engines patchright` rather than to the registry default,
for a reason that is a measurement: through the pool at
`google_serp`, patchright answered 96 ok of 223 while botasaurus managed 1 of
87, seleniumbase 0 of 86 and camoufox 0 of 33. A ladder on an engine that cannot
reach the target compares four zeroes.

 python scripts/run_ladder.py --identities 12

**What this run cannot do, stated before it is run.** At 24 identities per rung,
a move from 39% to 60% is Fisher p ~ 0.25 - not a result. The ladder is a sieve
on **direction**: it says which rung is worth 90 identities, and the confirming
run is a separate one. Quoting a rung ordering off 24 apiece would be the same
error as the four discordant pairs at p = 0.125 elsewhere in this repository.

Cost is dwell, and it is most of the run: at `--dwell 20,45` the three warm rungs
average 65, 130 and 195 seconds per identity, so 24 identities is about 2.6 hours
of dwell before a single probe, hold or gap is counted.

**What the ladder does not reach.** Every rung is a sequence of navigations -
`visit()` is one `goto`, which is the one method every engine's page object has,
which is why warming needs no engine support. Clicking a link, clicking a result
and refining a query are a different shape of session and none of them is here.
If the ladder comes back flat, that is the next thing to build rather than a
conclusion that history does not matter.

### Bringing your own proxy

Any proxy works - bought from anyone, or running on a box you own - and no account
with anybody is needed. Four values in `.env`:

 CUSTOM_HOST=1.2.3.4
 CUSTOM_PORT=8000
 CUSTOM_LOGIN=your_login
 CUSTOM_PASSWORD=your_password

Check it before spending anything on it. Ten CONNECTs, a few hundred bytes,
nothing sent to any target. It is the only check that separates a wrong password
from an unreachable host, because the gateway answers both with a status that
names neither:

 python -m nmbench gateway-health --provider custom

Then run whatever you like through it:

 python scripts/benchmark.py --providers custom \
 --engines http --targets bing_serp --queries 20 --preset none

`data/providers/custom.toml` is already written for the shape most proxies have:
one endpoint, a login, a password, no settings encoded in the username. Nothing to
transcribe, no code.

A gateway with no session parameter cannot be asked for a different exit, so every
attempt leaves from one address. The runner prints this on the plan line:

| Still answerable | Closed |
|---|---|
| which browser gets past which target, what a target costs in bytes, whether your setup announces itself | exit yield, how many queries burn an address, whether rotation helps |

If your provider does sell countries or sticky sessions inside the username, copy
`_template.toml` and write the dialect down there instead.

### Adding a provider

A provider is a username format: gateways take country, sticky session and quality
filter inside the proxy username, and every vendor picks its own separators and
names. So it is a file rather than a module - data cannot branch, and
`tests/test_repository.py` reads the runner's source and fails if it ever compares
against a provider name.

 cp data/providers/_template.toml data/providers/oxylabs.toml
 # fill in the dialect, then set OXYLABS_LOGIN and OXYLABS_PASSWORD in .env
 python scripts/benchmark.py --providers nodemaven,oxylabs \
 --engines patchright --targets google_serp --queries 40 --batch 1

`--providers` is an axis like every other one: cells interleave at batch
granularity, because provider A at 10:00 against provider B at 14:00 measures the
afternoon. The cell key names the provider only when the axis is varied, so runs
recorded before the axis existed still match `--resume`.

**Every definition declares its provenance, and it is the first field to read.**
`status = "measured"` means rows in `data/runs/` came through that gateway;
`status = "documented"` means the dialect was transcribed from the vendor's
documentation and never sent a byte. `--dry-run` prints it.

That is load-bearing because **a wrong username is invisible**. The gateway
measured here answers an unrecognised parameter name with HTTP 200 and the setting
silently dropped, so the run completes and every row claims a setting that was
never applied. A name outside `known_params` is refused before a request exists,
and `--param` is validated against every provider in the matrix before the first
cell opens.

Only `nodemaven.toml` ships, and it is the only gateway any number here was
measured through.

### The axes

An option only some engines implement is the failure this harness is built
against: the run would compare a humanized Camoufox against an unhumanized
everything else, and that reads as an engine difference. Every engine declares
what it supports and the runner refuses a mixed matrix outright.

| Flag | Declared by | Engines that have it |
|---|---|---|
| `--preset` | `supports_blocking` | the Playwright-driven ones plus obscura - `page.route` is a Playwright API and obscura has its own |
| `--headful` | `supports_headful` | everything with a window, so everything except the two scriptless clients and obscura, whose `serve` has no such flag |
| `--geo align` | `supports_geo_align` | camoufox, patchright, rebrowser, cloak, zendriver, botasaurus |
| `--humanize engine` | `humanize_modes` | camoufox, cloak |
| `--humanize trueman` | `humanize_modes` | chromium, patchright, rebrowser, cloak, camoufox |
| `--chrome-binary` | `supports_chrome_binary` | chromium, patchright, rebrowser, zendriver, botasaurus, seleniumbase |
| typed entry | `supports_typing` | camoufox, chromium, patchright, rebrowser, cloak, zendriver |

The table is a summary and the code is the authority: `--dry-run` refuses a matrix
before it starts, rather than leaving a reader to check a list that has rotted.

**`--humanize` has three values and two of them are different clients, not two
settings of one.** `engine` is the browser synthesising its own input - Camoufox
and cloak do this inside the binary and nothing outside can see how. `trueman` is
a pointer model in `nmbench/pointer.py` driven from outside through `page.mouse`,
so it works on any Playwright-driven engine including the unmodified control,
which is the point: a cursor axis measurable only on the two anti-detect engines
would confound the pointer with everything else those binaries change. They are
alternatives and never stacked - running both would compose two hands into one
path and produce a movement neither model describes - and `camoufox` and `cloak`
launch with their own humanization off under `trueman`.

**`trueman` runs only in `scripts/probes/probe_and_hold.py --entry home`**, and
both runners refuse it elsewhere rather than accepting it. A pointer exists only
where something is clicked: `benchmark.py` navigates to a search URL and clicks
nothing, and so does `--entry url`. Accepting the flag there would write
`humanize_mode=trueman` on rows whose cursor never moved, which is the failure
this whole section is built against.

**Pass both arms at once - `--humanize off,trueman` - rather than running two
commands.** It takes a comma list there the way `--warm`, `--geo` and `--entry`
do, and the arms interleave at identity granularity inside one window. It was a
single value until 2026-09-03, which meant the only way to get a control was to
run it again afterwards, and on this target the hour between two runs moves the
yield further than any flag in this table has: 69% to 52% between two windows of
one afternoon. A sequential pair would have measured that and called it the
cursor. The mode joins the cell key as `/hand-off` or `/hand-trueman` only when
more than one is asked for, so a run with a single mode still matches `--resume`
against every file taken before the axis existed.

Rows carry five columns for it. `humanize_mode` is the string, beside the older
boolean `humanize` which stays for the runs already on disk. `pointer_ms` is how
much of `elapsed_ms` was spent walking - a deliberate walk to a search box is on
the order of a second - so `elapsed_ms - pointer_ms` is the number comparable
against an unhumanized arm. `pointer_device` is which of the two fitted device
profiles the session drew, without which two rows of one arm are not comparable
on any timing metric. `pointer_overruns` against `pointer_points` says whether
the intervals the page saw were the model's or this host's driver's, which is
the headless question below in a column.

All four are null, not zero, when no pointer was driven. Zero is a different
statement and a reachable one: a walk of zero length emits no paced points, so
`pointer_points = 0` means the cursor was already on the target.

**Pair it with `--headful`, or half the model does not reach the page.**
Measured 2026-09-03 on a local Chromium and a `data:` URL, four arms of 18 paced
points: headful the delivered interval median is 7.00-7.15 ms against a model
asking 7.11-7.22, with 1 overrun of 18; headless it is 16.65 ms with 14-16
overruns, because `page.mouse.move()` awaits a CDP reply that is frame-bound at
one 60 Hz frame with no window. The positions are the model's either way. The
intervals are the driver's when headless, and two of the detector's 19 metrics
are about intervals - so a headless `trueman` arm is a geometry experiment and
has to be reported as one. On a server `--headful` means `xvfb-run -a`, and
whether a virtual display gives the real frame clock is not yet measured.

**Nothing here shows any target reads any of it.** The model was fitted against
one person's captured traces and scored by a 19-metric detector in
`lab/probes/trace_compare.py`; that says it is hard to tell apart from that one
person, not that it changes a verdict. The axis exists to find out.

**A mixed matrix needs `--preset none`.** The default is `light`, and blocking for
some columns and not others measured 4 KB against 9.9 MB on the same Google
refusal page - a 2000x engine difference produced entirely by the
flag. It moves verdicts too: a page that never loads its script is judged on
markup that was never finished.

**`--countries` needs no engine feature**, because the host country is the
alignment - the browser reports this machine's timezone and language list whatever
address it leaves from:

 python scripts/benchmark.py --engines camoufox,chromium,chromium:direct \
 --countries ru,us --targets bing_serp --queries 20 --preset none

A direct cell has no country, so the axis collapses for it and it is built once.

**`--geo align`** hands the browser the exit's own timezone through the browser's
emulation rather than by patching a JavaScript property, which reads back
unpatched from an iframe and from a Web Worker. The unmodified control stays at
`False`: the axis is read within one engine, aligned against unaligned, in one
window. Whichever was used is on every row.

**`--chrome-binary` holds the browser fixed** across the six engines that can be
pointed at one, so the engine is the variable rather than the build it happens to
bundle. It is off by default and that is deliberate: every row already on disk was
measured with each engine on its own browser, and a silent default would make new
rows incomparable with the old ones without any column saying so. A pinned run is
labelled `-pinned` and `engine_version` carries the build that actually launched,
so the intent and the outcome are separate columns and can be checked against each
other.

The size of what it controls, measured 2026-09-02 by `probes/tls_clienthello.py`:
unpinned, the engines run Chrome majors 136 to 151 and their TLS fingerprints
split by major and not by library. Pinned to one Chrome, all six land on one
value, and three of them changed build to get there. See "The TLS handshake,
engine by engine" in RESULTS.md.

**Each target draws from its own committed query list.** A shop and a search
engine have to run in one window and cannot take the same strings: asked
"photosynthesis exam questions", Amazon answers with an empty shelf, which is
indistinguishable from a soft refusal once it is a verdict. `--query-list` forces
one list on everything when that is the question.

## Command reference

Everything above on one page, for reading rather than for learning from. The code
is the authority: `python -m nmbench` lists every command and marks the ones that
send nothing, and `-h` prints the flags with the reasoning attached.

**Start here, by what you are trying to do.**

| I want to | Command | Spends |
|---|---|---|
| See what exists and what each thing costs | `python -m nmbench` | nothing |
| Check the tree is sane before anything else | `make check` | nothing |
| Know what a run would cost before running it | `python scripts/benchmark.py --dry-run` | nothing |
| Know which engines can run on this machine | `--dry-run` again - it prints the ones that cannot and why | nothing |
| See what each browser tells a page about itself | `python -m nmbench engine-fingerprint` | nothing |
| Check a gateway is alive and my username is right | `python -m nmbench gateway-health` | a few hundred bytes |
| Compare two engines on one target | `--engines patchright,chromium --targets google_serp` | traffic |
| Ask what the gateway itself contributes | `--engines chromium,chromium:direct` - the same browser on both sides, one window | traffic |
| Compare countries | `--countries us,any` | traffic |
| Compare two providers | `--providers nodemaven,custom` | traffic |
| Enter through the front page instead of a query URL | `python -m nmbench probe-and-hold` | traffic |
| Continue a run that was interrupted | `--resume` , or `--resume ` | traffic |
| Read what a run said | `python scripts/analysis/report.py` | nothing |
| Read one run line by line | `python scripts/analysis/peek.py ` | nothing |
| Find out what a run really cost, for the next estimate | `python scripts/analysis/calibrate.py` | nothing |

**Every flag of the matrix runner.** Defaults are what you get for saying nothing,
and two of them are worth knowing before a first run.

| Flag | Values | Default | What it changes |
|---|---|---|---|
| `--engines` | any of `http`, `curlcffi`, `chromium`, `patchright`, `rebrowser`, `cloak`, `camoufox`, `obscura`, `seleniumbase`, `zendriver`, `botasaurus`, comma separ

## 关联链接

- https://go.nodemaven.com/ghbenchmark

## 导航

- 项目页：[[10-项目/github.com_648ca450]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
