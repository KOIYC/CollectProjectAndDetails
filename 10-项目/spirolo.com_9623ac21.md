---
type: "project"
title: "Show HN: Static analysis for JavaScript/TS test suites, written in Rust"
project_url: "https://spirolo.com/"
first_seen: "2026-11-10T09:49:42+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_AlexFromTwelve
  - story_50431297
  - show_hn
lang: "en"
---

# Show HN: Static analysis for JavaScript/TS test suites, written in Rust

> [!info] 一句话导读
> Advisory alpha · JavaScript and TypeScript test suites

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://spirolo.com/>
> 首次收录：2026-11-10T09:49:42+08:00
> 来源渠道：HN Show HN
> 标签：author_AlexFromTwelve, story_50431297, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-10T09:49:42+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-11-10/a5304b40b394476d_Show-HN-Static-analysis-for-JavaScript-TS-test-sui]] |

## 摘要正文

Docs  简体中文  Search ⌘ K Advisory alpha · JavaScript and TypeScript test suites  The missing layer of your test suite.  A passing suite tells you the tests ran. Spirolo reads the whole suite, with its setup files and CI, and shows where a pass proves nothing. It never runs your tests.  $ npm install -D spirolo@alpha Copy  $ npx spirolo check Copy Install and first run 52 findings  styled-components · 395 ms 748 findings across 11 open-source projects.  53,372 tests read in about 16 seconds.  weak tests 314 weak tests  missing guards 136 missing guards  skips nobody tracks 98 skips nobody tracks  duplicate tests 200 duplicate tests Project Tests Findings Read in  styled-components 3,845 52 395 ms  expo 12,649 156 4.5 s  gatsby 3,509 117 862 ms  material-ui 4,832 14 3.1 s  carbon 4,662 110 1.1 s  mantine 5,013 72 2.6 s  Replayed at real speed: full runs of the alpha, start to exit, median of seven on one Linux machine at pinned commits. Findings are advisory, not confirmed bugs. Agents write tests faster than anyone can check them  An agent can add hundreds of tests in an afternoon, and they all come back green. A reviewer cannot read them all, and CI only reports that they passed. Ver…
