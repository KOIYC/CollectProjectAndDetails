---
type: "corpus"
item_id: "d010214e5e0cad1e"
title: "Show HN: Free token compression CLI, saves codex bills by 30%"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49902441"
project_url: "https://github.com/spenmcke/compress"
author: "srmckee"
published_at: "2026-09-29T23:49:40Z"
captured_at: "2026-09-30T18:57:42+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-09-30"
pub_day: "2026-09-29"
tags:
  - 语料
  - hn_show
  - author_srmckee
  - story_49902441
  - show_hn
metrics: {"points": 3, "comments": 1, "engagement_velocity": 3}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Free token compression CLI, saves codex bills by 30%

> [!info] 一句话导读
> Free CLI from Everest that compresses Codex tool output.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49902441>
> 指标：点赞=3 · 评论=1 · engagement_velocity=3
> 作者：srmckee　|　发布：2026-09-29T23:49:40Z
> 项目链接：<https://github.com/spenmcke/compress>
> 采集：2026-09-30T18:57:42+08:00　|　id：`d010214e5e0cad1e`

## 正文

# spenmcke/compress

Free CLI from Everest that compresses Codex tool output.

- Stars: 65
- Forks: 0
- Watchers: 65
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-09-29T18:36:31Z

## Languages

- Python
- Shell

## Top Contributors

- yolandaycao (3 contributions)
- spenmcke (2 contributions)

---

## README

# compress

`everest` reduces Codex tool output before it enters the model context. Everest
offers the service for free.

Your terminal retains the original output. If compression is unavailable or an
output cannot be compressed safely, Codex receives the original output.

## Install

`everest` requires macOS or Linux, Bash or Zsh, and please ensure codex is installed beforehand.

```
curl -fsSL https://install.everestagi.com/install.sh | sh && source ~/.config/everest/shell.sh
```

The installer verifies the package checksum, installs the `compress` command,
adds the Codex shell integration, and starts browser login through Everest.
Open a new terminal after installation, then run `codex` normally.

Useful commands:

```sh
everest savings          # show estimated savings for the latest run
everest doctor           # check the service connection
everest update --check   # check for an update
codex --uncompressed      # run Codex without compression
everest uninstall        # remove the integration and CLI
```

Uninstalling preserves local credentials, configuration, and savings history.
Use `everest uninstall --purge` to remove those as well.

## Privacy

Everest does not log your coding sessions. Eligible tool output, the associated
tool arguments, a focus description, and up to 4,000 characters of the latest
user message are sent to Everest for compression. The service processes that
content to return the compressed result; it does not store the session content.

The service records operational metadata and aggregate usage, such as request
outcomes, timing, and token counts. Local event logs contain metadata such as
hashes, counts, outcomes, and timing. Codex's own local session files can contain
the original content.

## Updates

`compress` checks for updates at most once every 24 hours when a Codex run
starts. Set `COMPRESS_AUTO_UPDATE=0` to disable automatic updates.

Savings are estimates and do not guarantee lower bills or identical model
behavior.

## Source

This repository contains the Codex CLI, installer, and published release
artifacts. The hosted compression service, model weights, customer SDKs, and
deployment configuration are not included.

## License

MIT. See LICENSE and THIRD_PARTY_NOTICES.md.

## 评论（1/1）

> **srmckee** · 2026-09-29T23:49:40.000Z　
> Hey HN! Spencer here - wanted to share a token compression tool that I’ve built for myself to save 30% costs on codex!I've been building a ton of web apps to replace saas i'm too cheap to keep paying for like chatgpt, notion, myfitnesspal, etc. and so i can get the exact features i want (+ no ads!).I was using Sol originally which was ok but also irritating because it would mess up and make a buggy ui.
> so I switched to Astra which is awesome but it inhales my resets and leaves me with luna (no point in continuing).I'm cheap as i said so instead of upgrading or switching to the hella expensive api (burned $700/day for similar amount of work on pro), I was thinking if I'm paying per token why not just reduce the tokens i use?So I built a tool that shrinks the prompts and context in codex so it costs less (!) when using on codex IRL, it cut down tokens by 29.6% and now i just leave it on by default in codex and I'm actually able to get through sessions without running out of credits.I’m making the cli free for everyone to use (https://github.com/spenmcke/compress). If you want to integrate it into your product to offer the best models at low cost, I can set you up with an sdk and api keysPS: It’s built for coding agents, not conversational agents. I optimized it for file retrieval accuracy, trajectory preservation, and quality to get up to 30% cost reduction depending on how context-heavy the task is.On security and privacy side, it's a proxy wrapping your local codex and zdr so it doesn't retain any of your queries. It’s on by default in codex and when you don’t want compression, you can use `codex --uncompress` to disable it.Give it a try, would be great to hear feedback and learn your hacky ways to save token costs too!

## 关联链接

- https://install.everestagi.com/install.sh

## 导航

- 项目页：[[10-项目/github.com_cb151dfa]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
