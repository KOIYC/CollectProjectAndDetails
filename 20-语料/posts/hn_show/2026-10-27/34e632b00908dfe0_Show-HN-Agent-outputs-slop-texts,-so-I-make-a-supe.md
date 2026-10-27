---
type: "corpus"
item_id: "34e632b00908dfe0"
title: "Show HN: Agent outputs slop texts, so I make a superfast HTML skill visualize it"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50253981"
project_url: "https://github.com/QingYunA/answer-me-with-html"
author: "sorlia7z"
published_at: "2026-10-27T02:19:30Z"
captured_at: "2026-10-27T23:46:32+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-27"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_sorlia7z
  - story_50253981
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Agent outputs slop texts, so I make a superfast HTML skill visualize it

> [!info] 一句话导读
> QingYunA/answer-me-with-html

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50253981>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：sorlia7z　|　发布：2026-10-27T02:19:30Z
> 项目链接：<https://github.com/QingYunA/answer-me-with-html>
> 采集：2026-10-27T23:46:32+08:00　|　id：`34e632b00908dfe0`

## 正文

# QingYunA/answer-me-with-html

Answer me with HTML — an agent skill that answers hard questions with a one-page HTML you can actually read. 让 AI Agent 用一页 HTML 回答复杂问题。

- Stars: 4482
- Forks: 303
- Watchers: 4482
- Open issues: 4
- License: MIT License
- Homepage: https://answer-me-with-html.com/
- Default branch: main
- Created: 2026-10-02T09:57:40Z

## Languages

- CSS
- HTML
- JavaScript

## Topics

- agent-skill
- ai-agent
- claude-code
- claude-code-skill
- claude-skill
- claude-skills
- cli
- diagram
- dsh-plugin
- explainer
- html
- llm
- ste100

## Top Contributors

- QingYunA (235 contributions)
- SU-AN-coder (14 contributions)
- netanelyasi (4 contributions)
- xianull (4 contributions)
- Cham1229 (3 contributions)
- zhaidewei (3 contributions)
- scqwq (2 contributions)
- jijichen (2 contributions)
- takaburi (2 contributions)
- Xpectuer (1 contributions)

---

## README

 Answer me with HTML

 Super Fast  |  ASD-STE100  |  Explainer Videos  |  One File, Offline

 An agent skill. Ask a hard question, get a page you can actually read instead of a wall of text. The model writes about 1/8 of the tokens it would need to hand-write the HTML.

 Website · Install · Examples · Videos · Always-on mode · Reference · 简体中文

Once installed, ask questions the way you always do:

```
> Explain the TCP three-way handshake
> Map out how the modules in this repo fit together
> Redis or Memcached for our cache?
```

The agent writes a short Markdown draft and hands it to the CLI that ships with the skill. About 50 ms later you have a page:

https://github.com/user-attachments/assets/d3063a28-5dfd-4c44-a562-be901c49b249

 24-second demo. Turn the sound on for the music.

## Why not just ask for HTML?

You can. Models write decent HTML now. But most of what they write is not content. We counted the tokens in 9 pages the model wrote by hand, 4,893 tokens on average:

| Part of the page | Share | With this skill |
| :--- | ---: | :--- |
| SVG diagrams: coordinates and paths | 47% | The CLI writes it |
| CSS | 15% | The CLI writes it |
| HTML tags | 17% | The CLI writes it |
| Text | 21% | The model writes it, as Markdown |

With this skill the model writes only a Markdown draft. For the same questions that was 612 tokens on average, **about 1/8 of the hand-written HTML**. Less to write means less to wait for (3 topics × 3 runs, medians, Claude Sonnet 5.5, a plain Claude Code setup):

| | Ask for HTML directly | Answer me with HTML | |
| :--- | ---: | ---: | :--- |
| Tokens the model writes | 4,893 | **612** | **8× fewer** |
| Time | 31 s | **12 s** | **2.6× faster** |

 The same question, the same model, answered both ways. Both pages are usable.

The token counts are saved in bench/corpus/tokens.json, so `node bench/corpus.mjs` gives the same numbers every time. The pages themselves are a download. The bill drops less than the writing, about 15% here, because every turn also reads the system prompt, your question and the conversation, with or without the skill. See where the cost goes.

Explainer videos save even more: about 18× fewer output tokens and 12× faster in a small test.

## Install

You need Node.js 20 or newer. There is no `npm install` step. The CLI is bundled inside the skill. No Node.js yet? With the recommended install below, your agent asks you and then installs it.

### Let your agent install it (recommended)

Paste this into Claude Code, Codex, Cursor, OpenCode or any other agent:

> Install Answer me with HTML: read https://raw.githubusercontent.com/QingYunA/answer-me-with-html/main/INSTALL.md and follow it.

INSTALL.md is written for agents. It installs the plugin in Claude Code and the skill in other agents, keeps an existing install, asks you nothing unless Node.js is missing or older than 20, and ends with one report after checking the result with the TCP three-way handshake page. If your agent cannot open links, use `npx -y skills add QingYunA/answer-me-with-html -g -y -a ` (for Claude Code, `-a claude-code`).

### Claude Code plugin

Run this inside Claude Code:

```
/plugin marketplace add QingYunA/answer-me-with-html
/plugin install answer-me-with-html@answer-me-with-html
```

### DeepSeek Harness plugin

Run this in a terminal, with the profile you run in (`web` is the shipped one):

```bash
dsh plugin --profile web add github:QingYunA/answer-me-with-html
```

### One command

```bash
npx skills add QingYunA/answer-me-with-html
```

It asks which agents to install into. The installer, vercel-labs/skills, supports more than 70 agents.

 Manual install

Copy the `skills/answer-me-with-html` folder into your agent's skill folder. For Claude Code:

```bash
git clone --depth 1 https://github.com/QingYunA/answer-me-with-html.git /tmp/answer-me-with-html
cp -R /tmp/answer-me-with-html/skills/answer-me-with-html ~/.claude/skills/answer-me-with-html
```

Skill folders for other agents: Codex `~/.codex/skills/`, Cursor `~/.cursor/skills/`, OpenCode `~/.config/opencode/skill/`.

No setup is needed after install. **We recommend turning on always-on mode**: the agent then adds a page to every conclusion, not only the hard ones. It takes one rule in your rules file.

## What you ask, what you get

| You ask | You get |
| :--- | :--- |
| "Explain the TCP three-way handshake" | A sequence diagram, a state diagram and a flag table |
| "How are the modules in this repo organized?" | A folder tree plus a call graph |
| "Redis or Memcached?" | A comparison table with ✓ and ✗, then a verdict |
| "What's wrong with this paragraph?" | Each sentence annotated, with the problem words and fixes |
| "How did Kubernetes come about?" | A timeline with the key moments highlighted |
| "Plan the cache change" | The real code from your files, and the open decisions as options you answer on the page |
| "How do I show hidden files with `ls`?" | No page. A one-line question gets a one-line answer |

The agent decides when a page is worth it: related concepts, multi-step flows, multi-way comparisons. You can also just say "explain it in HTML".

Pages are saved in `~/.answer-me-with-html/pages/`. The buttons in the top-right corner switch the theme and light/dark mode, collect your reply, and copy the Markdown that produced the page.

## How is this different from Archify or GenUI plugins?

Archify makes one interactive diagram from a JSON spec. GenUI plugins such as dsh-genui show components inside one chat app. This skill answers the whole question as one page: text, tables, code and diagrams, from a Markdown draft, in any agent that can run a shell command. See the full comparison.

## Explainer videos

Karpathy's ladder for understanding LLM output ends with explainer videos. Ask for one in 3Blue1Brown style: "make a 3b1b-style video on the TCP handshake".

The agent writes the same kind of draft as for a page, plus one line of narration per beat. Nothing else:

````markdown
## Both sides wait
```sequence
Client -> Server: SYN
Server -> Client: SYN-ACK
```
> The client sends a SYN to ask for a connection.
> The [Server] answers with a SYN-ACK.
````

`am video` turns it into a player page. The diagram builds step by step with the narration, and the camera follows the node named in brackets. The voice is inside the page, so it plays offline. The player has a chapter strip to jump between scenes, a speed button, and an export button that encodes the video in the browser and downloads it (a local file or `localhost`, no ffmpeg). Add `--mp4` for an MP4 file (needs ffmpeg), or `--webm` for a WebM file the page encodes itself (no ffmpeg). The agent only makes videos when you ask. Details: video guide.

## Settings

Change settings with a slash command. There are no config files to edit by hand.

| Where | How |
| :--- | :--- |
| Claude Code (plugin install) | `/answer-me-with-html:config` asks what to change. `/answer-me-with-html:config open off` changes it directly |
| Any agent | `/answer-me-with-html config open off`, or just say "stop opening the browser" |
| Terminal | `am config` to view, `am config set open off` to change, `am config reset` to restore defaults |

The settings are `open` (open pages in the browser), `theme`, `mode` (light or dark), `style` (writing check), `scale` (text size on the page; diagrams and charts grow with it), `update_check`, `close_after_reply` (close the tab after the reply is copied) and `voice` (video narration). Defaults and values: reference.

## Always-on mode (recommended)

With always-on mode, **every conclusion comes with a page**: whenever the agent gives a conclusion, summary, plan or comparison, even a short one, it adds a small page with 2 to 4 panels and puts the path at the end of the reply. These pages never pop open, so they don't interrupt you. Casual chat and replies with no conclusion stay as they are. Claude Code makes no pages in plan mode.

It is off by default. We recommend it: you stop asking for pages, and short answers read as well as long ones. Pages pile up in `~/.answer-me-with-html/`; clear them with `am clean`. To turn it on, paste this to your agent so it writes the rule into its rules file, such as `~/.claude/CLAUDE.md` or `AGENTS.md`:

> Turn on always-on mode for Answer me with HTML: add a global rule — "[answer-me-with-html always-on] Whenever a reply gives a conclusion, summary, plan, comparison, review or explanation, even a short one, also make a page with the answer-me-with-html skill (2 to 4 panels for routine answers), render it with --no-open before you write the reply, and end the reply with the page link in the format SKILL.md specifies for your host. Skip casual chat, one- or two-sentence replies with no conclusion, pure command output, and requests for plain text. An internal report to another agent is not a user reply: return the findings and evidence the parent asked for, and make no page unless the task explicitly asks for one."

To turn it off, delete that rule. Want fewer pages instead? See less proactive.

## Updating and cleaning up

Updates are manual. When used, the CLI checks GitHub for a new version in the background at most once a day. If one is available, it prompts the agent at most once every three days; nothing about you is sent. To update, tell your agent "update answer-me-with-html". Pages pile up in `~/.answer-me-with-html/`. Say "clean up the pages", and the agent asks before it deletes anything. Other install methods and every option: reference.

## Background

Andrej Karpathy posted that as LLMs do more of the work, keeping up with their output becomes the hard part. A diagram or a web page is far easier to take in than a long block of text.

I tried asking agents to answer in HTML directly. The pages were good, but slow: a decent page took a minute or two, mostly hundreds of lines of CSS that were nearly the same every time. Diagrams were worse. The model had to compute SVG coordinates by hand, and arrows often pointed at nothing.

So Answer me with HTML takes that work away from the model. The model writes content. The CLI handles layout, color and drawing.

## How it works

This is all the model writes:

````markdown
---
title: TCP three-way handshake
---
## A Three-way handshake {span=2}
```sequence num
Client -> Server: SYN, seq=x
Server -> Client: SYN+ACK, seq=y, ack=x+1
Client -> Server: ACK, ack=y+1
note Client, Server: ESTABLISHED
```

## C State changes {span=2}
```flow LR
(CLOSED) -> LISTEN: passive open
LISTEN -> SYN_RCVD: get SYN / send SYN+ACK
SYN_RCVD -> *ESTABLISHED: get ACK
```
````

The CLI does the rest. It picks the template, places the panels, applies the theme, lays out the flow chart with dagre and spaces the sequence diagram by label width. The full draft, examples/tcp.en.md, becomes this page:

## Features

- **Layout by code:** Panel placement and diagram coordinates are computed, not guessed. Labels don't get cut off, and there are no gaps in the grid.
- **Fixes its own mistakes:** When a draft has an error, the CLI returns the line number, the component and a correct example. The agent fixes it in one try.
- **Three themes:** `blueprint` looks like an engineering drawing, `shadcn` uses clean cards, and `paper` is set for long reading. By default the CLI picks paper for long text and blueprint for diagrams. All have light and dark modes, and you can add your own or take one from the theme catalog.
- **One file, no dependencies:** Each page is a single `.html` with no CDN links or web fonts. It opens offline and is easy to share.
- **Languages:** Chinese (Simplified and Traditional), English and Japanese get their own buttons and fonts. Other languages work with English buttons. See languages.
- **Writing check:** Drafts are checked against rules adapted from ASD-STE100: long sentences, wordy phrases, passive voice. It only warns unless you ask for strict mode.
- **Real code, not retyped:** A code block can quote lines from your files (`src=` `lines=`), so the code on the page is the real code. Files outside the folder and files that hold keys are refused.
- **Answer on the page:** Comment on any panel, and pick options in the decisions the agent asks (`ask`). The Reply button turns your answers and comments into one message to paste back to the agent.
- **Keeps its source:** Every page embeds the Markdown that made it. Click "Copy source" to get it back.

 Blueprint theme ( examples/ste100.md)
 shadcn theme, dark mode

## Components

The agent picks a component by the shape of the information:

| Component | Good for |
| :--- | :--- |
| `flow` | Architecture, call chains, decision branches. Auto layout, with groups, decisions and databases |
| `er` | A data model: entities with their columns (PK / FK / UK) and crow's-foot relationships |
| `sequence` | Messages going back and forth between several parties over time |
| `tree` | Folders, modules, taxonomies |
| `timeline` | History, releases, phases |
| `limits` | A value against its limit |
| `chart` | Bars, lines or a pie from a table of numbers: several series, negative values, a highlighted row |
| `annot` | Word-by-word notes on a sentence |
| `kv` | Metadata, a drawing's title block |
| `callout` | A conclusion, a tip, a warning |
| `ask` | A decision you make on the page; the agent's suggestion has a tag; nothing starts selected |
| Code block | Real code quoted from a file (`src=` `lines=`), or a sketch |
| Table | Multi-way comparison. Write `ok` / `no` / `warn` in a cell to get ✓ ✗ ! |

The draft format (frontmatter, `span`, `rows`, raw `html` / `svg` blocks) and how to call the CLI without an agent are in the reference. Full syntax for a component: `am help `.

## The STE writing check

ASD-STE100 is a controlled form of English first used for aircraft maintenance manuals. Its rules are concrete: keep sentences short, give each word one meaning, write steps as commands. Karpathy noted that asking an LLM to follow these rules makes its writing much easier to read.

Every render checks the parts a machine can check: sentence length, plain words, passive voice, and common Chinese typos and vague words. It only warns by default. Set `/answer-me-with-html:config style strict` to refuse drafts that fail, or `style:` in one draft. The full rule list: reference.

## Development

```bash
git clone https://github.com/QingYunA/answer-me-with-html.git && cd answer-me-with-html
npm install
npm test          # run the tests
AM_E2E=1 npm test # also run end-to-end video tests (system TTS, Chrome, ffmpeg)
npm run smoke:install # install for real with npx skills and validate the plugin manifests (needs network)
npm run build     # after changing src/, rebuild skills/answer-me-with-html/scripts/am.mjs
npm run snapshot  # compare rendered HTML with origin/main (refactors must not change it)
```

Maintainer conventions (generated bundle, page format, snapshot checks, reviewing PRs, releasing) are in CONTRIBUTING.md.

There are two runtime dependencies: marked parses Markdown and @dagrejs/dagre lays out flow charts. Both are bundled into `am.mjs`.

## Community

Ask questions, share pages you made, suggest features, or just say hi.

- Discord
- QQ group: `1127099407`
- LINUX DO, a Chinese-language developer forum
- AtomGit

Found a bug? Please open a GitHub issue.

## Star History

## License

MIT. The Bangers font that a theme can embed is under the SIL Open Font License 1.1.

# prasadabhishek/esp-watchtower

## 评论（1/1）

> **sorlia7z** · 2026-10-27T02:22:23.000Z　
> Hi, I'm the author of "answer-me-with-html", a html skill.I'm poor, so I can't use best model in the world (opus5.5...)My DeepSeek always output a lot complex nouns which i can't understand.So I made this skill, superfast, help me to understand what agent actually sayIf you wanna see the result of the skill, you can visit my Github to see.Thanks! My english is also poor btw...

## 关联链接

- https://answer-me-with-html.com/
- https://github.com/QingYunA/answer-me-with-html.git
- https://github.com/user-attachments/assets/d3063a28-5dfd-4c44-a562-be901c49b249
- https://raw.githubusercontent.com/QingYunA/answer-me-with-html/main/INSTALL.md

## 导航

- 项目页：[[10-项目/github.com_39a6cfc0]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
