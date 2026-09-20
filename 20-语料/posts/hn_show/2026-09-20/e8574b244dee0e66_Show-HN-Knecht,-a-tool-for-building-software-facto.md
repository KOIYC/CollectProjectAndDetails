---
type: "corpus"
item_id: "e8574b244dee0e66"
title: "Show HN: Knecht, a tool for building software factories for agencies"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49709714"
project_url: "https://knecht.works/"
author: "samuelreichor"
published_at: "2026-09-15T09:01:56Z"
captured_at: "2026-09-20T09:37:30+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_samuelreichor
  - story_49709714
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Knecht, a tool for building software factories for agencies

> [!info] 一句话导读
> AI Workflows for DDEV Projects

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49709714>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：samuelreichor　|　发布：2026-09-15T09:01:56Z
> 项目链接：<https://knecht.works/>
> 采集：2026-09-20T09:37:30+08:00　|　id：`e8574b244dee0e66`

## 正文

AI Workflows for DDEV Projects | Knecht

# Your Agency's Maintenance Robot.

A ticket starts a workflow. Knecht boots the project, does the task inside it, and opens a pull request with a preview. Self-hosted, for agencies that maintain many projects.

These teams are testing Knecht in the beta right now.

## Knecht Connects to the Tools You Already Use.

A ticket comes in, a result goes out. Knecht boots your project and does the work in a real dev environment.

Trigger

GitHub From an issue, a label, or a mention.

Jira From a ticket or a label.

Cron & Webhook On a schedule or a security advisory.

Let the Knecht Work

For every ticket, Knecht boots the project and runs the workflow inside it.

1. Project Boots with Database
2. Workflow Steps Run in Order
3. AI Agent Where Needed

Pull Request Branch, commits, and description.

Preview Environment Clickable, with a real database.

Comment in the Ticket Links to the preview and the PR.

## Use Cases for Agency Life.

Knecht does every task that you can describe as a workflow. These three show what such a run looks like, from the trigger to the pull request.

1. CMS Update with Database.

Every Monday Knecht boots the project with its database, updates Craft, and checks every link. The PR comes back ready.

Craft Update Workflow Play

1. 1

Schedule Fires Monday 06:00, project craft-shop

Trigger
2. 2

Project Boots with Database ddev composer install, DB dump imported

Boot
3. 3

ddev craft update all craftcms/cms 5.10.1 → 5.10.2, 3 migrations applied

Shell
4. 4

Link Check on the Preview 142 pages checked, 0 broken

Links

Pull request #84 on knecht/craft-update-1042

Update Craft CMS and plugins (run 1042). Link check after the update, 0 of 142 pages broken. Preview runs with a real database.

Preview: 84.preview.knecht.works
2. Estimate Tickets Up Front.

One label on the Jira ticket is enough. Knecht reproduces the problem and writes effort, risk, and a fix back to the ticket.
3. Fix Bugs from the Issue.

The issue gets a label. The agent reproduces the bug in the running app, fixes it there, and opens a PR with a preview.

Craft Update Workflow Play

1. 1

Schedule Fires Monday 06:00, project craft-shop

Trigger
2. 2

Project Boots with Database ddev composer install, DB dump imported

Boot
3. 3

ddev craft update all craftcms/cms 5.10.1 → 5.10.2, 3 migrations applied

Shell
4. 4

Link Check on the Preview 142 pages checked, 0 broken

Links

## Many Projects. One Knecht.

Projects, workflows, and runs in one place on your server. A workflow is written once and runs on as many projects as you connect, and every run keeps its log, preview, and result.

01 Projects 02 Project Detail 03 Workflow Editor 04 Test Workflows

 /projekte

 Vorschau

## Knecht Now Has a Discord Server.

Questions about the setup, feedback on workflows, show your first runs. We build in the open and answer ourselves.

1. Samuel today 09:12

v0.7.0 is out. Jira triggers can now filter by label.
2. Matthias today 09:40

First security update run across 6 Craft projects is done. All PRs green 🎉
3. Bruno today 10:03

Question: can the estimate workflow also run on GitHub issues?

## Where Knecht Stands.

What Knecht can do today, what we are working on, and what comes next.

Progress to the public release 0%

The beta is running. Next up are the Jira integration and more beta testers.

### Idea Validation

We tested the concept in a reduced scope. It works.

Done

### Branding and Organization

The name, the logo, the website, and the social media presence are complete.

### Tech Stack and Architecture

We made the basic technology decisions and validated them.

### Dashboard Design

The design for the dashboard is complete. In the dashboard, you make projects and workflows.

### Build the Prototype

A prototype exists. In it, you can make projects and workflows with an AI agent.

### Installer

You can install the dashboard on each Linux server.

### Update Service

You can install updates from the control panel.

### GitHub Trigger

You can set GitHub triggers that start workflows.

### Knecht Is Alive

You can install the Knecht dashboard on a Linux server with low effort, and it gets updates.

### Jira Trigger

Jira tickets can start workflows.

### SSH and IDE

You can make changes in the live preview containers through SSH and an IDE.

### Feedback Loop

After a workflow run, different feedback functions are necessary to make the output better.

### Langdock Support

The agent also runs through Langdock. One API key covers GPT and Claude models, and every request stays in the EU.

### Agent History

Every issue gets its own session. The agent keeps its environment and conversation across multiple runs.

### Managed Hosting

Beta testers do not have to install Knecht themselves. We host the instance for them and take care of updates and operations.

### Documentation and Onboarding

The docs cover the setup, workflows, and troubleshooting.

### Projects Without DDEV

Knecht boots projects that do not use DDEV as well.

### Improve Jira Integration

The Jira trigger gets more options and better comments back in the ticket.

### Find Beta Testers

We look for a sufficient number of beta testers to find problems early and build the final product.

### Test Actions

Workflows can run tests for projects. A fix is complete only when the tests are green.

### Browser Validation

The agent examines the bug in the preview and supplies screenshots as proof.

### Notifications

Slack or email sends a message when a run is complete or when it fails.

### Price Model and Licenses

You can officially buy Knecht. The price model, the license, and the payment are complete.

## Building in Public.

We build Knecht in the open. Each milestone is published here.

1. September 11, 2026 Engine

### Every Repo Boots, Even Without a DDEV Config

Knecht now builds the environment from the repo files when there is no DDEV config. A dev server becomes the live preview, with hot reload.

Read More
2. September 10, 2026 Project

### The Docs Are Online

Knecht now has documentation with search, a chat assistant, and feedback on every page. And a Discord server where we collect your reports.

Read More
3. August 18, 2026 Engine

### Langdock as an AI Provider

The agent now also runs through Langdock. One API key covers GPT and Claude models, and every request stays in the EU or in the US.

Read More
4. August 17, 2026 Engine

### Knecht Now Replies on GitHub

Every issue gets its own session with an environment and a conversation, the agent replies and labels directly in the thread, and a mention sends it back to work.

Read More

## Build Knecht with Us from the Start.

Knecht is in development. Become a beta tester and give feedback directly, or get the updates only.

 Knecht

Boot each project. Let Knecht do the work.

# backmeup.loomlabs.au

## 导航

- 项目页：[[10-项目/knecht.works_cdde344b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
