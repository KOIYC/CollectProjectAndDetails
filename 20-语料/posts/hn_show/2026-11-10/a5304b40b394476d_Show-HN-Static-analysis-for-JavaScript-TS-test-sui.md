---
type: "corpus"
item_id: "a5304b40b394476d"
title: "Show HN: Static analysis for JavaScript/TS test suites, written in Rust"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50431297"
project_url: "https://spirolo.com/"
author: "AlexFromTwelve"
published_at: "2026-11-09T20:14:09Z"
captured_at: "2026-11-10T09:49:42+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-10"
pub_day: "2026-11-09"
tags:
  - 语料
  - hn_show
  - author_AlexFromTwelve
  - story_50431297
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Static analysis for JavaScript/TS test suites, written in Rust

> [!info] 一句话导读
> Advisory alpha · JavaScript and TypeScript test suites

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50431297>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：AlexFromTwelve　|　发布：2026-11-09T20:14:09Z
> 项目链接：<https://spirolo.com/>
> 采集：2026-11-10T09:49:42+08:00　|　id：`a5304b40b394476d`

## 正文

Docs
 简体中文
 Search ⌘ K
Advisory alpha · JavaScript and TypeScript test suites
 The missing layer of your test suite.
 A passing suite tells you the tests ran. Spirolo reads the whole suite, with its setup files and CI, and shows where a pass proves nothing. It never runs your tests.
 $ npm install -D spirolo@alpha Copy
 $ npx spirolo check Copy
Install and first run
52 findings
 styled-components · 395 ms
748 findings across 11 open-source projects.
 53,372 tests read in about 16 seconds.
 weak tests 314 weak tests
 missing guards 136 missing guards
 skips nobody tracks 98 skips nobody tracks
 duplicate tests 200 duplicate tests
Project Tests Findings Read in
 styled-components 3,845 52 395 ms
 expo 12,649 156 4.5 s
 gatsby 3,509 117 862 ms
 material-ui 4,832 14 3.1 s
 carbon 4,662 110 1.1 s
 mantine 5,013 72 2.6 s
 Replayed at real speed: full runs of the alpha, start to exit, median of seven on one Linux machine at pinned commits. Findings are advisory, not confirmed bugs.
Agents write tests faster than anyone can check them
 An agent can add hundreds of tests in an afternoon, and they all come back green. A reviewer cannot read them all, and CI only reports that they passed. Verification has to keep up with the volume.
Super fast
 Keeps up with the volume
 Written in Rust. It read 53,372 tests across 11 projects, fast enough to run on every change, by every agent.
0 tests run
 Adds no load to CI
 It reads files, so it needs no browser, no database and no second test run. The 200 duplicate tests it found are time CI spends twice.
5 MCP tools
 Agents check their own tests
 An agent can call the same check while it writes, and fix a weak test before anyone reviews it.
136 missing guards
 Green means something again
 Setups with no guard against a console error or a leaked mock, so a test can pass when it should fail. When nobody reads every test, the merge gate has to hold.
New findings only
 Holds the line
 Ratchet once and CI fails only on what is new. No cleanup project first, and every new batch of tests meets the same bar.
Deterministic
 A second opinion that is not an LLM
 Same code, same report, every run. No model and no network: your code stays on your machine, and the tests are not checked by the same kind of tool that wrote them.
Five questions a green suite does not answer
 Every rule carries a public score; all 16 are on the rules page .
Weak tests 314 weak tests
 Would this test notice if the code were wrong ?
hides the item count tag when itemCount is 0
 should stay closed when index is -1
 the day %s should be hidden
does not render an unvisited lazy tab
 should not display the previous button asserts only that DOM is absent
hides the search input when hideSearch is true
search bar not rendered when options not provided
 non-custom leftItems render nothing in children
 should not populate textLabel prop when kind is not inline
does not render horizontal modifier when layout="vertical"
 when Link.Preview is not used, then does not render LinkNativeView, LinkNativePreview and LinkNativeTrigger
hides the item count tag when itemCount is 0
 should stay closed when index is -1
 the day %s should be hidden
does not render an unvisited lazy tab
 should not display the previous button asserts only that DOM is absent
hides the search input when hideSearch is true
search bar not rendered when options not provided
 non-custom leftItems render nothing in children
 should not populate textLabel prop when kind is not inline
does not render horizontal modifier when layout="vertical"
 when Link.Preview is not used, then does not render LinkNativeView, LinkNativePreview and LinkNativeTrigger
Merge gate 136 missing guards
 Does a broken test actually block the merge ?
Unused tests 200 duplicate tests
 Which tests add nothing the suite does not already check?
Flaky Experimental
 Which tests can pass on one run and fail on the next ?
Health Experimental
 Where does a new test pay first ?
C C grade
 61 61 of 100
Health C (61) One number to watch, not to gate on
 Every report opens with a provisional health score out of 100. Each family takes off points for the share of its subjects that have findings, up to a cap per family, and rules outside the default view count half. It is a summary to watch over time: nothing gates on it, and the machine formats do not carry it.
 Reading a report
Green is not the same as tested
 A passing suite rests on four layers. Most teams check the first and believe they have the rest. Two of them have no tool. Together they are the missing layer, and that is where Spirolo looks.
Mistakes inside a test file
 Checked by ESLint test plugins
A test with no assertion, a focused test, an unawaited query.
The setup every test runs on
 Checked by Spirolo · no other tool checks it
Whether a console error, a leaked mock or an unmatched request fails the test, or quietly lets it pass.
Whether the assertions catch a bug
 Checked by Stryker
Mutation testing plants small bugs and reruns the suite to see whether a test notices. Thorough, and slow on a big suite: one run per planted bug.
How the tests connect to the code
 Checked by Spirolo · no other tool checks it
Mocks that match no real export, absence checks with nothing proving the render happened, skips nobody tracks, gates that never gate.
This is an alpha. More rules are coming soon.
 No rule is proven yet, so the default view stays cautious: a rule shows only once at least 15 of its sampled findings were decided and at least 80% were true. The others still run, and --all shows them, labelled. How rules are measured .
spirolo check spirolo check --all
 absence-anchor Weak tests advisory 16 / 20
 fail-closed-setup Merge gate advisory 19 / 19
 dead-skip Merge gate advisory 18 / 18
 duplicate-test Unused tests advisory 15 / 18
 12 rules run but are not shown: 4 experimental, 8 hidden. spirolo check --all shows them, each labelled.
Questions
What is Spirolo? Spirolo reads a JavaScript or TypeScript test suite with its configs, setup files, mocks and CI, and points at the tests that pass without proving anything. It is a native binary from npm, Apache 2.0 licensed, in advisory alpha.
 Does it run my tests? No. It reads the files and never executes a test, so it needs no browser, database or network, only the project installed so imports resolve. It read 53,372 tests across 11 projects in 16 seconds on Linux x64.
 How is it different from the ESLint test plugins? ESLint sees one file at a time, and most of the ways a suite lies sit between files: a setup that swallows console errors, a mock that matches no export, a skip nobody tracks. Keep ESLint for the inside of a file; Spirolo reads the wiring.
 How is it different from mutation testing? Stryker plants small bugs and reruns the suite once per bug, which is thorough and slow on a big suite. Spirolo reads once and points at the structure that lets a bug through, and it can read a Stryker report to find tests that kill the same mutants.
 Which suites does it read? Jest, Vitest and Playwright, with Testing Library, MSW and nock, on Linux and macOS (x64 and arm64). The rules are measured on React and plain Node or TypeScript projects; Cypress, Vue and Windows are outside the alpha.
 What about false positives? A rule shows by default only once at least 15 of its sampled findings were decided and at least 80% were true, and that score is public. A wrong finding, reported with the file and the line, is how a rule gets better.
 Can it fail my build? Not until you ask: every finding reports at info and the exit code stays 0. Give a rule warn or error in .spirolorc.jsonc, or run ratchet once so CI fails only on new findings.
What would Spirolo find in your test suite?
 Your tests are the last check before production. In 11 popular open-source projects it found 748 findings, each project read in seconds. Install your project’s dependencies first, then run it from the root.
 $ npm install -D spirolo@alpha Copy
 $ npx spirolo check Copy
 Install and first run
Spirolo 0.1.0-alpha.1 · Apache 2.0 licence Docs Rules Source llms.txt 简体中文

## 导航

- 项目页：[[10-项目/spirolo.com_9623ac21]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
