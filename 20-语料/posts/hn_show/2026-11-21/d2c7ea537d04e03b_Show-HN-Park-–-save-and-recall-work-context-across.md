---
type: "corpus"
item_id: "d2c7ea537d04e03b"
title: "Show HN: Park – save and recall work context across repos and machines"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50583988"
project_url: "https://svandragt.github.io/park"
author: "pacifika"
published_at: "2026-11-20T23:43:20Z"
captured_at: "2026-11-21T14:45:01+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-21"
pub_day: "2026-11-20"
tags:
  - 语料
  - hn_show
  - author_pacifika
  - story_50583988
  - show_hn
metrics: {"points": 4, "comments": 3, "engagement_velocity": 4}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:3d"
---

# Show HN: Park – save and recall work context across repos and machines

> [!info] 一句话导读
> Getting started with park

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50583988>
> 指标：点赞=4 · 评论=3 · engagement_velocity=4
> 作者：pacifika　|　发布：2026-11-20T23:43:20Z
> 项目链接：<https://svandragt.github.io/park>
> 采集：2026-11-21T14:45:01+08:00　|　id：`d2c7ea537d04e03b`

## 正文

P
Getting started with park
Save where you were, so you or your agent can pick it up later. Source on GitHub
Progress 0 of 7
Step 1 · About 2 minutes
Install park
park is one Go binary. It keeps your parked items in a local SQLite database.
Terminal Copy
 $ go install github.com/svandragt/park@latest
 $ command -v park
 $ park version
Check that command -v park points into $(go env GOPATH)/bin or your GOBIN . If another park comes earlier on your PATH , that one runs instead.
Where your items live
The database is at ~/.local/share/park/park.db , or under $XDG_DATA_HOME when that is set. Set PARK_DB to use another file.
Trying park in a throwaway database? Unset PARK_SYNC_DIR as well as changing PARK_DB . While PARK_SYNC_DIR is set, every database you point park at reads and writes the same sync log, so test items reach your real items.
Terminal Copy
 $ env -u PARK_SYNC_DIR PARK_DB=/tmp/park-test.db park list
Step 2 · About 3 minutes
Park your first item
Park the thing you are in the middle of. Write it for the person who picks it up next, who may be you in a week or an agent with no memory of today.
Run this inside a git repository:
Terminal Copy
 $ park add --name "Fix login redirect loop" \
 --desc "Users bounce between /login and /dashboard" \
 --why "Blocks the release" \
 --how "Start at auth/session.go:42" \
 --tags auth
Output
 parked #1: Fix login redirect loop
What each field is for
--name is the one line you see in lists. It is the only required field.
--desc says what is wrong or what the work is.
--why says why it matters, so you can decide later whether it still does.
--how names the exact next step: a file and line, a command, a person to ask.
--body holds longer notes. park edit 1 --append-body "..." adds to it later.
park records the hostname, the git remote and the current branch for you.
Step 3 · About 3 minutes
Find it again
Three commands cover most lookups: list what is open, search for a word, then show one item in full.
Terminal Copy
 $ park list # every active item, in every repo
 $ park list --current # only this repo and branch
 $ park search redirect # full-text search, active items
Output of park search redirect
 #1 [active] Fix login redirect loop
 Users bounce between /login and /dashboard
 https://github.com/me/my-app (main)
Terminal Copy
 $ park show 1
 $ park show - # the item you added last
Output of park show 1
 # Fix login redirect loop [#1 · active]
**Users bounce between /login and /dashboard**
Why: Blocks the release
How to apply: Start at auth/session.go:42
Type: task Tags: auth
Repo: https://github.com/me/my-app Branch: main
Device: my-laptop Parked: 2026-11-20 11:01
Search covers the name, description, body, why, how and tags. Add --status all to include resolved items.
Step 4 · About 1 minute
Close the loop
Resolve an item as soon as the work is done. A short list of open items is one you will read.
Terminal Copy
 $ park done 1 # resolved
 $ park archive 1 # no longer relevant, kept for the record
 $ park reopen 1 # back to active
Output of park done 1
 #1 marked as resolved
Removing items for good
Terminal Copy
 $ park add --name "Try out park delete"
 $ park delete - # removes the item you added last
 $ park prune --days 30 # removes resolved and archived items older than 30 days
Both commands are permanent. Use done or archive when you are unsure.
Step 5 · About 3 minutes
Organise with tags, types and milestones
Tags group related items. Types say what kind of work an item is. A milestone collects the items that ship together.
Tags
Tag every item for a ticket with the ticket key, so one command finds them all:
Terminal Copy
 $ park edit 1 --tags "auth,ABC-123"
 $ park list --tag ABC-123
Types
The default type is task . The others are project , bug , feature , chore and docs . Filter with park list --type bug .
Milestones
A milestone is an item of type project . Point other items at it with --parent , and park show counts how many are done.
Terminal Copy
 $ park add --name "Q3 release" --type project
 $ park add --name "Write migration notes" --type docs --parent -
 $ park show 2
Output of park show 2
 # Q3 release [#2 · active]
Type: project
Repo: https://github.com/me/my-app Branch: main
Device: my-laptop Parked: 2026-11-20 11:01
Children: 0/1 done
#3 [active] Write migration notes
 https://github.com/me/my-app (main)
Another repository
To file an item under a repository you are not in, pass its remote: park add --name "x" --remote git@github.com:me/other.git .
Step 6 · About 5 minutes
Connect your coding agent
With the hooks installed, the agent sees this repo's parked items when a session starts, and again when it opens a file an item names.
Install the hooks
Terminal Copy
 $ park hook # prints the config, changes nothing
 $ park hook --install # adds it to Claude Code and Codex settings
The installer writes to ~/.claude/settings.json and ~/.codex/hooks.json , for whichever exists, and keeps the hooks already there. Hooks load when a session starts, so open a new session afterwards. In Claude Code, /hooks reloads them.
What the agent sees
At session start, the agent gets one line per active item for the current repository, most recently updated first. Claude Code passes on only the first 2 KB, so with many items the older ones may not fit:
Session context
 Parked items here (id name [tags]). Surface anything relevant; do not act on it unprompted. Before a task: park search ; for a ticket, park list --tag ; park show  for detail.
3 Write migration notes
2 Q3 release
1 Fix login redirect loop [auth,ABC-123]
In Claude Code, a second hook runs when the agent reads or edits a file. If an active item names that file, the agent sees up to five matching items and can run park show for detail. Codex gets only the session-start hook.
Let the agent park for you
The repository includes a Claude Code skill. With it installed, you can say "park this", "show parked" or "work on #2".
Terminal, from a park checkout Copy
 $ mkdir -p ~/.claude/skills/park
 $ cp .claude/skills/park/SKILL.md ~/.claude/skills/park/SKILL.md
Step 7 · Optional · About 5 minutes
Sync between machines
Skip this step if you use park on one machine. With sync, each machine writes its own log file to a shared folder and reads everyone else's.
On every machine
Point PARK_SYNC_DIR at a folder your file syncer keeps in step. Leave PARK_DB on its local default.
Shell profile Copy
 export PARK_SYNC_DIR="$HOME/sync/park"
Once, on the machine that has your items
Terminal Copy
 $ park sync-seed --i-understand-this-runs-once
A second run, or a run on a second machine, duplicates every item. The command refuses if this machine's log already has entries.
On each other machine
Terminal Copy
 $ park rebuild --yes
rebuild replaces the local database with what the logs contain. Run it only when the logs hold everything you want to keep.
Keep the database out of the synced folder SQLite stores one database in several files. A file syncer copies them one at a time, and a half-copied set fails with database disk image is malformed . A log file has one writer and only grows, which syncers handle safely.
Item numbers such as #12 are local to each machine. When two machines change the same item, the later change wins.
Step 8 · About 2 minutes
Browse and review
Open your items in a browser, and check whether parked items come back into your work.
Web view
Terminal Copy
 $ park serve # http://127.0.0.1:7654
The web view has search, a repository filter, and clickable tags and types. It is read-only and shows the items as they were when the server started.
Usage report
Terminal Copy
 $ park stats --days 7
Output
 Usage in the last 7 days
Events
 surfaced search 1
 viewed cli 2
 resolved cli 1
Surfaced items: 1
 later viewed: 1 (100%)
 later resolved: 1 (100%)
How items came back
 source surfaced viewed resolved
 session-hook 0 0 0
 file-hook 0 0 0
 search 1 1 1
 list-tag 0 0 0
 direct 0 1 0
Each view or resolve counts towards the way the item last reached you in the 2 hours before: the session hook, the file hook, a search or a tag list. direct means you went to the item without it being shown first. The record stays on this machine and does not sync.
You are set up
Next time you are interrupted, run park add before you switch. When you come back, run park list --current .
Every command and flag is listed in the README , and for commands that take flags, park  -h lists them.

## 评论（3/3）

> **pacifika** · 2026-11-20T23:43:20.000Z　
> In order to get less distracted I created park. Park the thing you are in the middle of, before context switching. You can use it yourself, browse it locally, sync it. It’s got a skill so your AI agent parks those leftovers, and park suggests them after a task is done.I’ve used this daily for half a year. Hope you’ll find it as useful.

---

> **pacifika** · 2026-11-20T23:56:37.000Z　
> Sorry forgot to prefix with Show HN. Update: thanks fixed it.

---

> **solyin** · 2026-11-21T00:04:00.000Z　
> You can't edit the url but you can edit the headline.

## 关联链接

- http://127.0.0.1:7654
- https://github.com/me/my-app

## 导航

- 项目页：[[10-项目/svandragt.github.io_9b19f9e5]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
