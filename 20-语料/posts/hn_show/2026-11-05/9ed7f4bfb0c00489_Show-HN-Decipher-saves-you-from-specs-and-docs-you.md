---
type: "corpus"
item_id: "9ed7f4bfb0c00489"
title: "Show HN: Decipher saves you from specs and docs you rubber stamp"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50366976"
project_url: "https://github.com/amirimi/decipher"
author: "amk9978"
published_at: "2026-11-04T15:28:57Z"
captured_at: "2026-11-05T11:21:45+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-05"
pub_day: "2026-11-04"
tags:
  - 语料
  - hn_show
  - author_amk9978
  - story_50366976
  - show_hn
metrics: {"points": 3, "comments": 1, "engagement_velocity": 3}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Decipher saves you from specs and docs you rubber stamp

> [!info] 一句话导读
> Rewrites agent-written specs, PRs, and reports into plain English, gist first, with one question that checks you still follow.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50366976>
> 指标：点赞=3 · 评论=1 · engagement_velocity=3
> 作者：amk9978　|　发布：2026-11-04T15:28:57Z
> 项目链接：<https://github.com/amirimi/decipher>
> 采集：2026-11-05T11:21:45+08:00　|　id：`9ed7f4bfb0c00489`

## 正文

# amirimi/decipher

Rewrites agent-written specs, PRs, and reports into plain English, gist first, with one question that checks you still follow.

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 1
- License: MIT License
- Homepage: https://claude.ai/customize/plugins/id/cba64762-9a2d-42c8-914b-859aaa270617%40anthropic-plugin-directory
- Default branch: main
- Created: 2026-09-29T13:19:35Z

## Languages

- HTML

## Topics

- agent-skills
- agentic-coding
- ai-agents
- anthropic
- claude
- claude-code
- claude-code-plugin
- claude-code-plugins
- claude-code-skills
- claude-plugin
- claude-skills
- code-review
- codex
- cursor
- developer-tools
- opencode
- skill-md
- spec-driven-development
- summarization
- technical-writing

## Top Contributors

- amirimi (37 contributions)

---

## README

**Gist.** agent-written specs decoded, gist first, plain English after, one unskimmable question, every caveat kept

**Bottom line.** Your agent writes a 1,600-word spec, and you approve it after a skim. decipher rewrites any agent-written document so its first three parts carry the whole idea in plain English, in about 120 words. The rest waits below as reference.

**Self-check.** You approved your agent's last spec. Could you name its riskiest assumption without opening it?

validate
License: MIT
Claude Code plugin

## Install

decipher is listed in Claude's plugin directory and on cursor.directory.

**Claude Code** gets the skill and an always-on output style.

```text
/plugin marketplace add amirimi/decipher
/plugin install decipher@decipher
```

**Codex, OpenCode, and Cursor** each have their own install in INSTALL.md. So does any other agent that reads `SKILL.md`.

Tested with Claude Code 2.1.307, Codex 0.149.1, OpenCode 1.19.3, and the Cursor CLI 2026.10.19.

## Use

Point it at a document, or say "decipher" after a reply that lost you.

```text
/decipher:decipher specs/govern-every-model-call.md
```

A clone install shortens the command to `/decipher`, and Codex uses `$decipher`.

| Say | Get |
|---|---|
| decipher, simplify this | The latest reply or a named document, rewritten |
| decipher, again on the same document | A new angle with none of the earlier sentences |
| walk me through a spec, PR, or report | Three to five parts, one per turn, with a bookmark |
| continue, back, all at once, stop | Moves through the walkthrough |
| I'm lost | The goal again, from a different angle |

Specs and design docs are home turf. PRs, reports, incident write-ups, READMEs, and agent replies work too.

## Every answer, same shape

```text
Gist.                a few words that carry the whole idea
Bottom line.         what it does, where it stands, what backs it
Self-check.          one question you answer to yourself
-------------------  most readers stop here
Terms.               only when the jargon would lose you
Needs you.           decisions, blockers, risks
How it works.        the steps, in order
Hollow?              a one-line warning when it hedges, dodges your ask, or builds on a guess
Make sure you know:  a foundation you may be missing, only when your questions show it
```

The Self-check is the point. It comes from the document's own premise and asks for your judgment, so scrolling back won't answer it. Can't answer it? You've stopped steering. Take the wheel back before you approve anything.

When the document dodges what you asked or builds on something it is unsure of, one line near the end warns you and names where. Pin those premises down before you build on them.

When a follow-up shows you are missing a concept the document never explains, the last line names it. Learn that first, and the document reads differently.

## "Can't I just tell Claude to be concise?"

Go ahead. A concision rule shapes the next thing your agent writes. The 1,600-word spec already in your repo stays 1,600 words, and so does the PR a teammate's agent opened. decipher works on what already exists. It defines the jargon from the source, keeps what the document claims apart from what anyone verified, and checks that you still follow.

## Always on

Always-on mode puts every reply in plain English, and decipher's format still waits until you ask for an explanation.

**Claude Code** turns it on with the plugin's output style. Select it in `~/.claude/settings.json`. A plugin install names it `decipher:decipher`, and a clone install names it `decipher`.

```json
{ "outputStyle": "decipher:decipher" }
```

**Every other agent** turns it on with this block in the instruction file it reads every session.

```markdown
## decipher
Use decipher's always-on mode. Before your first reply in a session, load the decipher skill and follow its rules for always-on mode. Explain a source in decipher's format only when I ask. Load the skill again whenever its rules leave your context.
```

| Agent | Instruction file |
|---|---|
| Codex | `~/.codex/AGENTS.md` |
| OpenCode | `~/.config/opencode/AGENTS.md` |
| Cursor | `.cursor/rules/decipher.mdc` in each repository, with `alwaysApply: true` in its front matter |

While decipher's rules apply, its own limits replace brevity budgets from other output styles, `CLAUDE.md`, and `AGENTS.md`. Your accuracy and punctuation rules still win.

## A real run

decipher on a 2,601-word agent-written spec for litellm-brownout, a LiteLLM plugin that switches a team to a cheaper model once its spend crosses a set line. The reply runs 354 words, and the three parts you read first run 129.

 Full reply

**Gist.** checks extend beyond chat, Claude Code now downgraded, embeddings never swapped, unlisted calls refused, assistants endpoints escape

**Bottom line.** Brownout used to check and downgrade only `/v1/chat/completions`. As a result, Claude Code on `/v1/messages` and Codex on `/v1/responses` were never downgraded, and their unpriced models were served at $0. The spec sorts every LiteLLM call type into five kinds, checks team and key on all of them, and swaps models only for text generation. It shipped in commit 7822bbf, and the spec reports lab runs on LiteLLM 1.101.6 to 1.104.2 that downgraded all five text endpoints.

**Self-check.** Brownout refuses any call type that a future LiteLLM release adds until someone reviews it. Would your governed teams rather hit that 503 than have a new endpoint skip the downgrade?

**Needs you.**
- Decide whether to block the assistants, threads and runs endpoints inside LiteLLM, because LiteLLM runs no plugin hook there and brownout cannot see or refuse them.
- Check that every fallback deployment that uses an `openai/` model implements the Responses API, because LiteLLM forwards `/v1/messages` there as a Responses call. A server without that API answers 404 and LiteLLM then puts the deployment on cooldown.
- Weigh that images, speech, transcription, moderation, rerank, OCR and video skip the price check, because an unpriced model on those endpoints records $0 spend.

**How it works.**
1. The pre-call hook looks up each call's LiteLLM `call_type` in one table in `bridge.py` and gets back one kind.
2. Every allowed call gets the team and key checks. A call that names a model also gets the model checks and the spend-tier decision.
3. Only `text` calls switch to the team's cheaper fallback once spend passes `degrade_at`. These are chat, text completion, `/v1/messages`, `/v1/responses` and Gemini `generate_content`.
4. Embeddings and `/v1/responses/compact` keep the model the caller named. Another model would produce incompatible vectors or an unreadable summary.
5. Calls that name no model, such as MCP tool calls and file reads, get only the team and key checks.
6. Provider pass-through, realtime, batches, fine-tuning and every unlisted call type get a 503 that names the call type.

## Feedback

decipher left you lost? That's a bug. Open an issue with the original text and the reply.

Anything else, such as a reply that helped or a section you never read, goes in Discussions.

**If you find decipher useful, please star the repo.** It helps other engineers who review agent-written specs find it.

## License

MIT

## 评论（1/1）

> **amk9978** · 2026-11-04T15:35:48.000Z　
> I've done spec-driven development with Claude Code for almost all of the past year. The agent writes a spec, I approve it, and the agent builds it. The specs run beyond thousands of words, and I started approving them after skimming one or two. I have ADHD, so a wall of agent prose loses me fast.decipher rewrites an agent-written spec, PR, report, or reply for a reader who lost the thread. You get a gist of a few words, a bottom line, and one question you answer to yourself. Then come the decisions and risks that are yours, and the steps in order. It also tries to warn you, in one line, when a doc dodges what you asked or builds on a guess.I used to use i-have-adhd, caveman, etc, but none of them would give me what I needed. It's been some weeks since I've been using decipher, and recently open-sourced it.Install in Claude Code: /plugin marketplace add amirimi/decipher
>  /plugin install decipher@decipher
>
> It also works in Codex, OpenCode, and Cursor.It's free and MIT-licensed. Eager to hear your feedback!

## 关联链接

- https://claude.ai/customize/plugins/id/cba64762-9a2d-42c8-914b-859aaa270617%40anthropic-plugin-directory

## 导航

- 项目页：[[10-项目/github.com_e2d14405]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
