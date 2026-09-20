---
type: "corpus"
item_id: "75013fb5bd21c4c8"
title: "Show HN: Run Claude Code sessions on Linear issues via two MCP servers"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47961204"
project_url: "https://lanes.sh/blog/linear-to-lanes"
author: "s-xyz"
published_at: "2026-04-30T12:03:24Z"
captured_at: "2026-09-21T02:52:28+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_s-xyz
  - story_47961204
  - show_hn
metrics: {"points": 5, "comments": 0, "engagement_velocity": 5}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: Run Claude Code sessions on Linear issues via two MCP servers

> [!info] 一句话导读
> From Linear to Lanes: A Two-MCP Workflow

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47961204>
> 指标：点赞=5 · 评论=0 · engagement_velocity=5
> 作者：s-xyz　|　发布：2026-04-30T12:03:24Z
> 项目链接：<https://lanes.sh/blog/linear-to-lanes>
> 采集：2026-09-21T02:52:28+08:00　|　id：`75013fb5bd21c4c8`

## 正文

# From Linear to Lanes: A Two-MCP Workflow

> A short tutorial on combining the Linear MCP and the local Lanes MCP, so you can pull tickets and start agent sessions on them directly from chat.
> 2026-04-30

In this tutorial we'll walk through how to use the official Linear MCP and the local Lanes MCP together, so that an agent can pull issues out of Linear and spin up a session on them directly. The interesting part is that last word: directly. Once a Linear ticket lands on your Lanes board, starting a Claude Code, Codex, or shell session against it is one prompt away in the same chat. No copy-paste, no window swap, no second tool to learn.

The mechanic is simple. An agent that has both MCP servers connected can read your Linear backlog, drop selected tickets onto your local Lanes board, kick off a session in a fresh git worktree, and then sync the outcome back to Linear when it's done. We'll walk through each of those pieces in turn.

Watch the video

A short walkthrough of the flow described below: pulling a Linear ticket into Lanes and kicking off a session on it from a single chat.

## The two servers

It's worth a quick word on what each server actually is before we wire them up.

Linear MCP is hosted remotely by Linear at `https://mcp.linear.app/mcp`. You connect to it over OAuth and there's nothing to install locally. It exposes Linear's full read and write surface: tickets, projects, comments, labels, cycles, and so on.

Lanes MCP is the opposite shape. It runs locally, on `http://localhost:5353/sse`, served by the Lanes desktop app once you flip the toggle in Settings. It exposes everything inside your local Lanes workspace: issues, sessions, terminal scrollback, session history, git changes per issue, and the controls to start or stop a session.

The trick is that an agent connected to both has them sitting in the same context at the same time. There is no glue code between them, and no integration layer to maintain. The connective tissue is just whatever prompt you type next.

## Setup

Adding Linear's server to Claude Code is one command:

```bash
claude mcp add --transport http linear https://mcp.linear.app/mcp

```

Then run `/mcp` inside a session to complete the OAuth handshake in your browser. Once that's done, the Linear tools are available to the agent alongside everything else.

For Lanes, open the desktop app, head to Settings > Integrations > Lanes MCP, and toggle it on. The same screen has a one-click Connect button for Claude Code, which writes the entry to `~/.claude.json` for you so you don't have to hand-edit any JSON. Restart your agent and both servers should show up in `/mcp`.

## Pulling Linear issues into Lanes

With both servers connected, importing tickets becomes a single sentence in chat.

"Pull all my open Linear issues with the `frontend` label and create matching issues in Lanes tagged with `frontend`."

Here's roughly what happens behind that prompt. The agent calls `list_my_issues` on the Linear MCP, filtered by the label, and gets back the matching tickets. Then, because tags in Lanes are referenced by UUID rather than by name, it calls `lanes_list_labels` to resolve `frontend` to its actual ID in your local workspace. From there, every Linear issue becomes a `lanes_create_issue` call with the title, description, and resolved label UUID filled in. The Linear identifier (something like `ENG-742`) and the Linear permalink get stitched into the Lanes description, so the link back upstream is preserved on the issue itself.

You don't have to look up label or component IDs yourself. The agent handles that through `lanes_list_labels` and `lanes_list_components` before creating or updating issues. Refer to them by name in your prompt and trust the agent to resolve them.

The same shape works for narrower imports:

"Import the three highest-priority issues from the current cycle on team ENG, only the ones assigned to me, into the Lanes backlog."

In this case the agent stacks Linear's filter parameters (cycle, team, assignee, priority) before importing. Because both servers live in the same conversation, no list of issue IDs ever needs to leave the chat or pass through your clipboard.

## Starting a session on an imported issue

This is the part the whole setup exists for. Once a Linear ticket is on your Lanes board, you can run it as a session straight from chat.

"Find the Lanes issue for ENG-742 and start a Claude Code session in plan mode with a fresh worktree."

Three things happen behind that prompt. First, the agent searches Lanes for the imported ticket using its Linear identifier. Then it calls `lanes_update_issue` to set `worktreeStrategy` to `create` along with a sensible `worktreeName`, so that when the session spawns it lands in an isolated git branch rather than your current working tree. Finally, `lanes_start_session` actually launches the session with `cli: "claude"` and `planMode: true`. That call returns immediately, and the PTY spawns asynchronously inside the desktop app a moment later.

You can layer more onto the same prompt without changing its shape. A custom prompt override, extra environment variables, additional CLI flags, or swapping `claude` for `codex` or `shell` are all just additional fields on the same `lanes_start_session` call. The session shows up in Lanes like any other, except now it already has the full Linear ticket baked into its description.

## Syncing the result back

When a session finishes, you can close the loop from the same chat.

"Summarize the work done on ENG-742, post it as a comment on the Linear issue, and move the Linear issue to In Review."

The agent pulls everything it needs out of Lanes. `lanes_get_issue_history` returns the message timeline of the most recent session for that issue. `lanes_get_session_stats` gives you token usage, duration, and per-tool call counts. `lanes_get_issue_changes` returns the git diff of the worktree. From those three sources it composes a summary, posts it through Linear's `create_comment`, and then calls `update_issue` on Linear to transition the ticket's state. Every piece of context the agent needs already lives on the board, so the round trip back to Linear is just a translation step rather than a rewrite from memory.

## Polling a long-running session

Sessions don't have to be one-shot. Because `lanes_get_session_status` is just another MCP tool, you can also ask the agent to keep an eye on running sessions for you.

"Every five minutes, check the status of the session on ENG-742. If it's awaiting input, show me the last 50 lines of the terminal."

`lanes_get_session_status` returns the live status of each session (`starting`, `busy`, `awaiting_input`, `exited`, or `error`). When it flips to `awaiting_input`, `lanes_read_terminal` pulls the scrollback so you can see what the agent got stuck on without leaving the chat. That same pairing is also useful for end-of-day status reports across every active session at once, not just a single ticket.

## What to try

If you wire up a workflow on top of these two servers, we'd love to hear about it. Drop it in our Discord. And if a tool call feels missing or wrong, that's exactly the kind of feedback we want during the research preview.

## 关联链接

- http://localhost:5353/sse`,
- https://mcp.linear.app/mcp
- https://mcp.linear.app/mcp`.

## 导航

- 项目页：[[10-项目/lanes.sh_da5967b7]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
