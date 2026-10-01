---
type: "corpus"
item_id: "eefe06e37a773b60"
title: "Show HN: Sedum – Playwright tests in English, cheap enough to run on every PR"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49911464"
project_url: "https://github.com/sedum-dev/sedum"
author: "jgnatch"
published_at: "2026-09-30T16:55:53Z"
captured_at: "2026-10-01T09:41:49+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-01"
pub_day: "2026-09-30"
tags:
  - 语料
  - hn_show
  - author_jgnatch
  - story_49911464
  - show_hn
metrics: {"points": 3, "comments": 1, "engagement_velocity": 3}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Sedum – Playwright tests in English, cheap enough to run on every PR

> [!info] 一句话导读
> Published: 2026-09-19

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49911464>
> 指标：点赞=3 · 评论=1 · engagement_velocity=3
> 作者：jgnatch　|　发布：2026-09-30T16:55:53Z
> 项目链接：<https://github.com/sedum-dev/sedum>
> 采集：2026-10-01T09:41:49+08:00　|　id：`eefe06e37a773b60`

## 正文

Published: 2026-09-19

GitHub - sedum-dev/sedum: Plain-English browser e2e tests cheap enough to run on every PR. Built on Jev and Playwright, open source, bring your own key. · GitHub

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| .agents | .agents | | |
| .changeset | .changeset | | |
| .github | .github | | |
| docs | docs | | |
| evals | evals | | |
| examples/ saucedemo | examples/ saucedemo | | |
| fixtures | fixtures | | |
| packages | packages | | |
| real-sites | real-sites | | |
| scripts | scripts | | |
| .gitattributes | .gitattributes | | |
| .gitignore | .gitignore | | |
| .npmrc | .npmrc | | |
| .prettierignore | .prettierignore | | |
| CONTRIBUTING.md | CONTRIBUTING.md | | |
| LICENSE | LICENSE | | |
| README.md | README.md | | |
| SECURITY.md | SECURITY.md | | |
| eslint.config.mjs | eslint.config.mjs | | |
| package.json | package.json | | |
| pnpm-lock.yaml | pnpm-lock.yaml | | |
| pnpm-workspace.yaml | pnpm-workspace.yaml | | |
| tsconfig.base.json | tsconfig.base.json | | |
| turbo.json | turbo.json | | |
| vitest.config.ts | vitest.config.ts | | |
| View all files | | | |

# Sedum

Write browser tests in plain English, keep the full power of TypeScript, and run the whole suite on every pull request for dollars a month instead of thousands.

```
// tests/checkout.test.ts
import { faker } from "@faker-js/faker";
import { test, expect, secret } from "sedum-cli";

test(
  "a customer checks out",
  { url: "https://www.saucedemo.com/" },
  async ({ page, ai, env }) => {
    await ai.group(
      "Log in",
      [
        "type {{user}} in the username field",
        "type {{password}} in the password field",
        "click the login button",
      ],
      { user: "standard_user", password: secret(env.SAUCE_PASSWORD!) },
    );

    await ai("click the Add to cart button for {{product}}", {
      product: "Sauce Labs Backpack",
    });
    await expect(page.locator(".shopping_cart_badge")).toHaveText("1"); // plain Playwright

    await ai("click the shopping cart link");
    await ai("click the Checkout button");
    await ai("type {{first}} in the First Name field", {
      first: faker.person.firstName(),
    });
    await ai("type {{last}} in the Last Name field", {
      last: faker.person.lastName(),
    });
    await ai("type {{zip}} in the Zip/Postal Code field", {
      zip: faker.location.zipCode(),
    });
    await ai("click the Continue button");
    await ai("verify the order summary lists Sauce Labs Backpack");
  },
);
```

```
npx sedum run tests/checkout.test.ts
```

Each `ai(...)` sentence is one step that Sedum resolves on the page, with no selectors. Everything between steps is ordinary code: Playwright's `page` and `expect`, test data from any library, API calls to seed or skip setup, and helper functions.

Sedum uses a model for two jobs only: finding the element a sentence refers to, and judging whether a claim such as "a list of products with prices is shown" holds on the page. That model is Jev, from TypeSafe. It returns probabilities, not free text. Everything else is deterministic: clicking, typing, waiting, verdicts, and exit codes run on Playwright.

> Status: pre-alpha. The first alpha is on npm as `sedum-cli`. The test format may change before 1.0, and Windows is experimental. Linux and macOS are verified.

## Quickstart

You need Node.js 20.19 or newer and a TypeSafe API key or a compatible provider key.

```
mkdir my-sedum-tests && cd my-sedum-tests
npm init -y
git init                              # locator results are cached in Git metadata
npm install -D sedum-cli
npx sedum init                        # an example test, config, and .env.example
npx sedum browsers install chromium   # if init says it is missing
cp .env.example .env                  # then set TYPESAFE_API_KEY in .env
npx sedum run tests/example.test.ts --headed
```

For a compatible provider, set `TYPESAFE_BASE_URL` to its API root and `TYPESAFE_API_KEY` to that provider's key. Set `TYPESAFE_DEFAULT_MODEL` if its model name differs from the default. See provider configuration.

The example signs in to a demo shop. To see a failure, change its last step to a false claim, such as `verify an error message says the password is incorrect`, and run it again: it fails with exit code 1. If anything is missing, `npx sedum doctor` says what and how to fix it.

New to AI browser tests? Read plain-English browser tests first.

## Why Sedum

Writing tests in English is not new. Running them on every pull request is usually too expensive, because hosted tools charge per step. Sedum is open source, runs on your machine with your own key, and calls a model that is fast and cheap enough to ask on every step.

| | Per-step platform | Sedum on Jev |
| --- | --- | --- |
| Monthly cost of a team's PR suite | $4,875 | $38–$91 (53× less) |
| 17-step checkout on saucedemo.com | 69 s | 14 s (4.9× faster) |

The cost row is 50 tests of 10 steps (3 of them AI steps), run about 20 times a day by a 20-person team, priced at a per-step platform's published pay-as-you-go rates and at Jev's posted token price ($91 with the cache off). The speed row is five runs each with every cache off, on one laptop. See sedum.dev for the full method.

How it compares with other ways to test in a browser:

| | Coded tests (Playwright, Cypress) | Browser agents | Per-step AI platforms | Sedum |
| --- | --- | --- | --- | --- |
| Selectors to maintain | Yes | No | No | No |
| Same actions every run | Yes | No, the agent picks | Yes | Yes |
| Cost to run on every PR | Low | High | High | Low |
| Open source, your key | Yes | Often | No | Yes |

- Probabilities, not guesses. Every claim is scored against a threshold you set, and checked for contradicting evidence. A marginal pass is flagged, not silently green. See probabilistic testing.
- No black box. Prompts, scoring, and caching are in this repo. You can see exactly what goes to the model and what comes back.

## Fix failures with your coding agent

When a test fails, have Sedum write a report for an agent such as Claude Code or Cursor:

```
npx sedum run --reporter markdown
# markdown .sedum/runs/<run-id>/report.md
```

Then ask the agent to read that file and fix the failure. The report puts the most urgent problem first, with the sentence and its file and line, the scores, the page text the model judged, the elements it considered, a screenshot, and a command to rerun just that test, so the agent can check its own fix. Page text is fenced and labelled untrusted, so a page cannot inject instructions into the report.

## Writing tests

A test is a `test()` in a `*.test.ts` file. Its body gets `ai` for plain-English steps, and Playwright's `page` and `context` for everything else.

| You write | Sedum does |
| --- | --- |
| `await ai("click the Checkout button")` | finds the button and clicks it |
| `await ai("type {{zip}} in the Zip/Postal Code field", { zip })` | types the value you pass |
| `await ai("verify the order summary lists 2 items")` | judges the claim against the page |
| `await ai.extract("the order total")` | returns the element's text |
| `await ai.group("Checkout", async () => { ... })` | reports the steps inside under a name |

Write `{{name}}` in a sentence and pass the value separately, so the sentence stays the same on every run and can be checked before a run. Wrap passwords and tokens in `secret()`: they are typed, but never sent to the model or shown in reports. A file can hold several tests, and each gets a fresh browser context. See TypeScript tests for the full API, and examples/saucedemo for a small suite that uses faker, skips the login form with a cookie, and checks app state behind the UI.

### YAML tests

Tests that need no code can also be `*.test.yaml` files with a list of sentences. Both formats run side by side in one project.

```
# tests/login.test.yaml
url: https://www.saucedemo.com/
data:
  user: standard_user
  password: $SAUCE_PASSWORD
steps:
  - type {{user}} in the username field
  - type {{password}} in the password field
  - click the login button
  - verify a list of products with prices is shown
```

`$VAR` reads an environment variable and is treated as a secret. Put shared steps in a `*.module.yaml` file and call it with `use:`. See the YAML format.

## Learn more

## Coming next

Recently shipped: tests in TypeScript, the first alpha on npm, `sedum init` to scaffold a project, parallel runs and sharding, and JUnit reports.

Planned for the 0.1 alpha:

- a GitHub Action
- starting your app before a run

## Goal-based tests

State the outcome and let Sedum work out the actions, then independently verify it:

```
url: https://shop.example.com/
goal: >
  sign in, add a hat to the cart, check out with the saved card
verify: the confirmation page shows an order number
```

Goal tests are YAML only for now. Use `goal` and a required `verify` claim instead of `steps`. Supply typing values through `data`; `before` and `after` hooks remain available. Run and validate the file with the same CLI commands as authored-step tests. See goal mode for budgets, reporting, supported operations and recorded limitations.

## Contributing

Issues and pull requests are welcome. See CONTRIBUTING.md to build from source, and SECURITY.md to report a vulnerability. Sedum is MIT licensed.

# rulereceipt/rulereceipt

## 评论（1/1）

> **jgnatch** · 2026-09-30T16:58:11.000Z　
> Hey HN,I'm Ignacio, CTO at Timeline. I launched an OSS library named Sedum today that lets you write e2e tests in plain english (or any other language).Right now we are shipping so much AI generated code that we needed a way to write AI e2e tests in an economical way that we can run on every PR or even multiple times in local environments. The existing platforms charge you by step and they add a lot of mark up to the underlying AI calls.For our 20 person engineering team, running these AI e2e tests in one of the existing paid tools, meant having to spend more than $5k/mo.I was already thinking of doing an Open Source alternative some time ago, and when Jev launched, I played with it and quickly realised it's the way to go. It really makes it economical to run these tests with very high frequency and its probabilistic nature also helps you flag potential flakiness upfront, understand which tests should be run depending on the files being changed, and many other interesting use-cases.But.. because Jev is only text and sometimes pure text is not enough to translate a sentence from plain english into a proper action or a proper assertion, in the cases where Jev is not confident enough, our library falls back on a vision model such Gemini Flash 3.8 (again.. BYOK).Anyway, check it out and let me know what you think :)

## 关联链接

- https://shop.example.com/
- https://www.saucedemo.com/

## 导航

- 项目页：[[10-项目/github.com_fd8e70fd]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
