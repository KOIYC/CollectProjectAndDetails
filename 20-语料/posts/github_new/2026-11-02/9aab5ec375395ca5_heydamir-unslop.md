---
type: "corpus"
item_id: "9aab5ec375395ca5"
title: "heydamir/unslop"
source: "github_new"
source_name: "GitHub 新星仓库"
url: "https://github.com/heydamir/unslop"
project_url: "https://github.com/heydamir/unslop"
author: "heydamir"
published_at: "2026-10-29T15:41:21Z"
captured_at: "2026-11-02T09:40:41+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-02"
pub_day: "2026-10-29"
tags:
  - 语料
  - github_new
  - JavaScript
  - created:>2026-10-19
metrics: {"stars": 4903, "forks": 244, "open_issues": 3}
comments_count: 0
comments_total: 0
discovered_via: "github:14d"
---

# heydamir/unslop

> [!info] 一句话导读
> Created by Damir Sokolovsky ([@heydamir](https://x.com/heydamir)), who started the [Unslopping series](https://x.com/heydamir/status/2115063463063998736) on X.

> [!meta]- 语料信息（点开展开）
> 来源：GitHub 新星仓库（post）
> 原帖：<https://github.com/heydamir/unslop>
> 指标：stars=4903 · forks=244 · open_issues=3
> 作者：heydamir　|　发布：2026-10-29T15:41:21Z
> 项目链接：<https://github.com/heydamir/unslop>
> 采集：2026-11-02T09:40:41+08:00　|　id：`9aab5ec375395ca5`

## 正文

# unslop

Created by Damir Sokolovsky ([@heydamir](https://x.com/heydamir)), who started the [Unslopping series](https://x.com/heydamir/status/2115063463063998736) on X.

![A vibecoded dashboard unslopping itself, frame by frame](skills/unslop/references/refs/story-dashboard-frames.webp)

unslop is a skill for Claude Code and Codex that turns vibecoded, AI-looking UI into a designed interface with its own character. It finds the slop first, the purple gradients, glows, emoji labels, shouty copy and uneven spacing, then sets a direction from your product and fixes the screen pass by pass like a designer doing a redline review. It works in whatever your screen is built with, like Next.js, React, Vue, Svelte, Tailwind or plain HTML and CSS, on dashboards, apps and landing pages, and even on a live site when all you have is a link.

## Install

For Claude Code, copy the skill into your skills folder.

```bash
git clone https://github.com/heydamir/unslop
mkdir -p ~/.claude/skills && cp -r unslop/skills/unslop ~/.claude/skills/
```

For a single project, copy it into `.claude/skills/` inside that project instead.

For Codex, ask it to install the skill straight from this repo.

```
$skill-installer install https://github.com/heydamir/unslop/tree/main/skills/unslop
```

Or copy it by hand into `~/.agents/skills/`, or into `.agents/skills/` inside a single project.

```bash
git clone https://github.com/heydamir/unslop
mkdir -p ~/.agents/skills && cp -r unslop/skills/unslop ~/.agents/skills/
```

To snapshot a live site or create a story video, install Playwright and its Chromium browser from the project directory where you run the skill:

```bash
npm install -D playwright
npx playwright install chromium
```

Story videos also require ffmpeg installed and available on your PATH.

## Use

In Claude Code, type `/unslop` with what you want. In Codex, type `$unslop` the same way. Or just ask in your own words and the agent picks the skill up by itself.

```
/unslop this dashboard
/unslop the hero of https://example.com
/unslop my landing page and make the story video so I can post it
```

It audits the screen and proposes a direction before it edits anything, so you can steer it early. If the screen is already good, it tells you so and suggests a few small refinements instead of redesigning it.

## What it does

- **Audit.** Lists every sign of slop with where it lives.
- **Direction.** Character, world, the one or two moments that carry the color, and a signature detail, all taken from your product.
- **Passes.** Spacing, color, icons, copy, type, layout, details, visuals and motion, in that order.
- **Visuals.** Shows your product instead of a glossy blob. When a hero needs a scene or an object, it can generate one through an image service like fal, Replicate, OpenAI images or Higgsfield. If none is connected, it offers to connect one as an MCP server, and it shows the prompt and asks before every paid generation. Dashboards and apps rarely need one.
- **Story video.** A square video under 10 seconds of your screen unslopping itself, ready to post. It needs Playwright and ffmpeg.

Try it on the two vibecoded screens in [examples](examples).

## Hire the unslopper

Would rather have a designer do it? Damir unslops one key screen in 3 days, built in your stack, at [heydamir.design/unslop](https://heydamir.design/unslop).

## License

[CC BY 4.0](LICENSE). Use it, change it and share it, including commercially, as long as you credit Damir Sokolovsky ([@heydamir](https://x.com/heydamir)) and link back to this repository.

## 关联链接

- https://example.com
- https://github.com/heydamir/unslop/tree/main/skills/unslop
- https://heydamir.design/unslop
- https://x.com/heydamir
- https://x.com/heydamir/status/2115063463063998736

## 导航

- 项目页：[[10-项目/github.com_9aab5ec3]]
- 渠道页：[[50-渠道/github_new]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
