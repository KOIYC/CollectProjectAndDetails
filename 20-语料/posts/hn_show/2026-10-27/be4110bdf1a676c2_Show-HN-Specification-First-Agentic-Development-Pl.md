---
type: "corpus"
item_id: "be4110bdf1a676c2"
title: "Show HN: Specification First Agentic Development Plugin and Prove"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50260571"
project_url: "https://spec-first.dev/"
author: "hleichsenring"
published_at: "2026-10-27T15:12:20Z"
captured_at: "2026-10-28T00:14:41+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-27"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_hleichsenring
  - story_50260571
  - show_hn
  - front_page
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Specification First Agentic Development Plugin and Prove

> [!info] 一句话导读
> May we count your visit?

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50260571>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：hleichsenring　|　发布：2026-10-27T15:12:20Z
> 项目链接：<https://spec-first.dev/>
> 采集：2026-10-28T00:14:41+08:00　|　id：`be4110bdf1a676c2`

## 正文

May we count your visit?
We'd like to use Google Analytics to see how many people visit and which pages they read. It sets cookies and sends data to Google. Nothing loads unless you say yes, and you can change your mind under Privacy settings at the bottom of every page.
Decline
 Accept
Details in the privacy policy .
§ spec-first
The method
Review
The gate
Agent Smith
GitHub
Install
Spec-first agentic development
Vibe coding is dead. Talk it through, the rest is guided.
Describe the feature in your own words. Four commands write the spec, check it against your code, build it in its own worktree and deliver it through your checks. Run several side by side and get back verified pull requests.
/plugin marketplace add holgerleichsenring/specification-first-agentic-development
 Copy
Install
MIT licensed Plain YAML and Markdown in your repo Claude Code plugin, or any agent
1 Describe
 2 /create-spec
 3 /review-spec
 4 /apply-spec
 5 /deliver-spec
You talk, it listens You describe the app in your own words. Before asking anything, the agent reads your memory and the repository, so it only asks what neither can answer.
The spec comes first create-spec writes goal, facts with file and line, steps and done criteria, on a fresh branch in its own worktree. No code yet.
A second pair of eyes A script checks that every cited file and line exists. Then a new agent with no chat history attacks the spec against the code, and its cuts are applied before anything is built.
Built by the spec apply-spec works through the steps, writes the tests the spec names, and logs every choice that wasn't obvious in decisions/.
Only green lands The commit goes through the gate: build and tests have to pass. Then the branch is pushed and the pull request opens with the spec inside.
todo-app
Explorer
todo-app
.spec-first
decisions
2026-10-27-7b2d.yaml
memory
feedback-stack.md
MEMORY.md
specs
planned
active
done
2026-10-27-7b2d-todos-first-version.yaml
src
todos.ts
todos.test.ts
TodoList.ts
main.ts
package.json
main.ts
 2026-10-27-7b2d-todos-first-version.yaml
 todos.ts
 Simple Browser · localhost:5173
src › main.ts
.spec-first › specs › planned › 2026-10-27-7b2d-todos-first-version.yaml
src › todos.ts
import './style.css'
const app = document.querySelector< HTMLDivElement >( '#app' )!
 app.innerHTML = `<h1>Todos</h1>`
// Vite starter: nothing else here yet
 spec: 2026-10-27-7b2d
 goal: "A first todo app: add, tick off, filter, kept on reload"
 facts:
 - claim: "The app is an empty Vite starter"
 evidence: src/main.ts:1-6 ✓
 - claim: "TypeScript, tests with Vitest"
 evidence: .spec-first/memory/feedback-stack.md ✓
 steps:
 - id: store # todos.ts, saved to localStorage
 - id: list # TodoList.ts: add, tick, filter
 - id: drag-to-reorder cut by review: not asked for
 done:
 - "Add, tick off and delete a todo"
 - "Filter all, open, done"
 - "Todos survive a reload"
 - "An empty title is rejected" added by review
 export type Todo = { id: string ; title: string ; done: boolean }
const KEY = 'todos'
export function load(): Todo [] {
 return JSON.parse(localStorage.getItem(KEY) ?? '[]' )
 }
export function add(todos: Todo [], title: string ): Todo [] {
 if (!title.trim()) return todos // done criterion: empty title rejected
 return [...todos, { id: crypto.randomUUID(), title: title.trim(), done: false }]
 }
Todos
What needs doing? Add
All Open Done
Write the spec
Review it against the code
Buy coffee beans
Book the train to Hamburg
2 open · saved in this browser
Claude Code
I want a small todo app. Add todos, tick them off, filter open and done. Browser only, no backend.
Read .spec-first/memory/MEMORY.md
Read src/main.ts
It's an empty Vite starter, and I'll use TypeScript and Vitest as you prefer. Should todos survive a reload?
Yes, localStorage is fine.
/spec-first:create-spec
Write 2026-10-27-7b2d-todos-first-version.yaml
Here is the spec. Shall I put it on its own branch?
Looks right, go.
Bash git worktree add -b spec/2026-10-27-7b2d …
Spec 2026-10-27-7b2d is on its own branch: 3 steps, 3 done criteria.
/spec-first:review-spec
Bash check-evidence.py evidence resolves: 1 spec
Agent Review spec 2026-10-27-7b2d fresh context
Edit 2026-10-27-7b2d-todos-first-version.yaml
BUILD WITH CUTS. Drag to reorder is out, a check for empty titles is in. Both applied.
/spec-first:apply-spec
Plan: the store first, then the list, then the tests. Go?
Go.
Write src/todos.ts
Write src/TodoList.ts
Write src/todos.test.ts
Bash npm test 9 passed
Write .spec-first/decisions/2026-10-27-7b2d.yaml
Built and tested. One decision on record: localStorage over IndexedDB, because a few hundred todos fit easily.
/spec-first:deliver-spec
Bash git commit -m "feat: a first todo app (2026-10-27-7b2d)" gate: build, test passed
Bash gh pr create #12
Bash npm run dev localhost:5173
The gate passed and pull request #12 is open. The app runs on localhost:5173.
/spec-first:apply-spec
⎇ main spec/2026-10-27-7b2d ⊘ 0 problems Claude Code
The rows with a dot are what the skills do on their own: reading, writing, checking, building. You type the lines in boxes.
9 skills 1 commit gate a worktree per spec ids minted offline, safe in parallel Claude Code · Codex · Cursor · Copilot
§ 1
What changes when agents work from specs
This is how Agent Smith is built every day, across more than a thousand specs.
Verified
 A fresh reviewer checks the spec against the code before the build. A gate runs your checks before the commit.
Parallel
 One branch and worktree per spec. Ids come from the clock, so two agents never take the same one.
Uninterrupted
 A reviewed spec has already answered the open questions, so the agent builds to its done criteria instead of coming back to ask.
Structured
 One spec, one branch, one commit. A pull request carries one spec or a whole series, and every change has the same shape.
Resumable
 State lives in context.yaml . Restart the machine or the agent and the work picks up where it stopped.
Explained , as a side effect
 Each choice is logged with what it beat and why, so the reasoning stays next to the code.
§ 2
A whole series, side by side
Cut a bigger change into a series of specs. /spec-first:deliver-series reviews all of them, builds the groups that share no file at the same time, verifies the merged tree and opens one pull request.
deliver-series 2026-10-27-8a3f 5 specs · 3 groups building
Spec Group review build gate merge
a tickets-provider-contract requires nothing 1
b tickets-github-provider requires a 1
c tickets-jira-provider requires a 1
d settings-provider-page requires nothing 2
e ci-restore-cache requires nothing 3
3 worktrees building in parallel · every spec commit through the gate
 PR #42
An example run of /spec-first:deliver-series . Specs that share no file are built at the same time; specs that depend on each other share a group.
§ 3
One spec, from idea to pull request
Four skills take a piece of work through its own branch and worktree. Each one leaves a file behind for the next step and for whoever reads the history later.
create-spec
 Goal, steps, facts with file and line, what done means. No code yet.
 specs/planned/{id}.yaml
review-spec
 Every citation resolved, then a reviewer who never saw the chat attacks it.
 BUILD · CUTS · REFUSE
apply-spec
 Contracts, code, wiring, tests, following the project's own rules.
 decisions/{id}.yaml
deliver-spec
 One commit through the gate, pushed, pull request opened.
 feat: … ({id})
The record grows with every spec, read before every step
specs/ Every spec, from planned to done, with its facts and done criteria.
decisions/ What each spec chose, what it chose over, and why.
memory/ What you told the agent once, so you don't say it twice.
/spec-first:bootstrap-project writes the contexts once from your code: stack, rules and the checks a commit must pass. After that, each spec adds one line of state.
§ 4
A spec is reviewed before anyone builds it
A REFUSE costs you one spec. Without the review, the same mistake would have cost you the branch.
Spec 2026-10-27-8a3f
Applies to server
Branch spec/8a3f
Goal Ticket providers so pipelines can pull work from GitHub and Jira.
Facts, read in the code
 Pipelines take work only from the CLI today Program.cs:40-58
Config already carries a tracker section AppConfig.cs:12-19
Decision
 Adapter over repository: read-mostly data, no unit of work needed.
Done when
 GitHub provider returns tickets end to end
 Jira provider behind the same interface
 verify: stages green
REVIEWED · BUILD fresh reviewer · 27 OCT
review-spec · 2026-10-27-8a3f 2 cuts
✓ src/Host/Program.cs:40-58 resolves
✓ src/Config/AppConfig.cs:12-19 resolves
evidence resolves: 1 spec
BUILD WITH CUTS the spec holds once two steps change
CUT 1 Step jira needs a second auth mode the config can't hold yet. AppConfig.cs:15 Move it to its own spec.
CUT 2 Paging is missing: GitHub returns 30 issues per page. GitHubClient.cs:88 Add a done criterion.
Every citation is checked
 A script opens each file and line the spec cites. A claim nobody checked in the code has to be listed as an assumption.
The reviewer starts fresh
 A new agent with no conversation history reads the code as it is, not as the spec says it is.
One verdict, with cuts named
 BUILD, BUILD WITH CUTS or REFUSE, and every finding names a file and a line.
§ 5
The reasoning comes along for free
Nobody has to write documentation afterwards. While it builds, the agent logs each choice that wasn't obvious: what it chose, what it chose over, and why. One file per spec, next to the code.
decisions/2026-10-27-8a3f.yaml
spec: 2026-10-27-8a3f
 decisions:
 - category: TradeOff
 chose: "Raw HttpClient for the GitHub API"
 over: "Octokit"
 reason: "Three megabytes of dependencies
 for four calls."
 - category: Architecture
 chose: "One ITicketProvider per tracker"
 over: "A generic REST mapper"
 reason: "Each tracker pages and authenticates
 differently; the mapper would leak it."
No wiki to keep alive
 cat decisions/*.yaml is the project's reasoning, spec by spec, in the same history as the code it explains.
Memory for what git can't tell
 How the operator wants things done, a constraint outside the repo, a pointer elsewhere. One fact per file, one line in an index.
Back in thirty seconds
 Restart the machine, restart the agent, open context.yaml . It knows what is done, what is active and what comes next.
§ 6
Nothing lands past a red stage
The plugin's commit gate runs every verify stage your contexts declare when a commit names its spec. All green, it commits. The first red stage blocks it, and its output goes back to the agent.
the commit
git commit -m "feat: ticket
 providers (2026-10-27-8a3f) "
 The id in parentheses triggers it. -F  , -C and --amend --no-edit are gated too.
verify: stages
✓ build dotnet build
✓ tests dotnet test
✕ web cd web && npm test
PASSED Committed
 every stage green
BLOCKED Not committed
 the first red stage stops it, and its output goes back to the agent
# spec-first-gate.log · one line per spec commit
2026-10-27T09:14:02Z blocked 2026-10-27-8a3f /work/repo a1b2c3d web
2026-10-27T09:31:47Z passed 2026-10-27-8a3f /work/repo a1b2c3d build,tests,web
A spec commit with no line in the ledger never met the gate. A project with its own gate says gate: project , and the plugin steps aside.
Built this way
Agent Smith
The open source agentic software factory: a ticket goes in, a verified pull request comes out. Agent Smith is entirely built with this method, and the method grew out of building it. Everything in the plugin ran there first.
Agent Smith runs the loop for you →
1,300+ specs done
1,190+ decision files: chose, over, why
650+ specs through the gate
Counted in the Agent Smith repository, October 2026.
§ 7
Install
In Claude Code the plugin does the bookkeeping and runs the gate. Other agents follow the same files through AGENTS.md , and a git hook runs the same gate.
Claude Code
 Codex, Cursor, Copilot and others
/plugin marketplace add holgerleichsenring/specification-first-agentic-development
 Copy
/plugin install spec-first@specification-first-agentic-development
 Copy
Then run /spec-first:bootstrap-project . It reads your code and writes the contexts and rules from what it finds.
create-spec Writes the spec on its own branch and worktree
review-spec Evidence check, then a fresh reviewer's verdict
apply-spec Builds the spec up to its done criteria
deliver-spec Commits through the gate and opens the pull request
deliver-series Takes a whole series of specs to one pull request
log-decision · update-project · bootstrap-project Decisions, upgrades, setup
Let your agent set it up
 Paste this into Codex, Cursor, Copilot or any agent that can read and write your repository.
Set up specification-first agentic development in this repository,
following the templates at
https://github.com/holgerleichsenring/specification-first-agentic-development/tree/main/templates
1. Create .{project}/contexts/default/context.yaml and coding-principles.md.
 Fill them from the code as it is: stack, architecture, limits, conventions,
 and the commands that build and test it as verify: stages. Invent nothing.
2. Create .{project}/specs/planned, active and done, .{project}/decisions/
 and .{project}/memory/MEMORY.md.
3. Write AGENTS.md from templates/prompt.md, with .{project}/ filled in.
4. Add "gate: git" at the top level of that context.yaml.
 Copy prompt
AGENTS.md carries the method
 Codex, Cursor and Copilot read AGENTS.md when a session starts. It holds the read order and the workflow, and every step says how to do it by hand, the review brief for a fresh session included.
The gate as a git hook
 Clone the spec-first repository once, then run python3 /hooks/install-git-hook.py in each clone of your project. The commit-msg hook runs your verify: stages on every commit that names a spec, from any agent or the terminal. git commit --no-verify skips it. The evidence check is skills/review-spec/scripts/check-evidence.py in the same clone and needs PyYAML.
§ 8
Questions about spec-first agentic development
Specification-driven agentic development, in short answers.
What is spec-first agentic development?
 A way of working with AI coding agents in which every change starts as a written spec in your repository. A fresh reviewer checks the spec against your code before anything is built, the agent builds it on its own branch and worktree, and the commit lands only when your checks pass.
What does specification-driven agentic development mean here?
 The spec drives the work from start to finish. It names the goal, the facts it rests on with file and line, the steps and the done criteria, and the agent builds to exactly that. Spec-first agentic development is specification-driven agentic development in which the spec is reviewed against the code before the first line is written.
Do I need Claude Code?
 No. The Claude Code plugin runs the steps as commands. Codex, Cursor, Copilot or a terminal follow the same files through AGENTS.md, and a git commit-msg hook runs the same commit gate in every clone where it is installed.
How does it differ from vibe coding?
 You still describe the feature in your own words and talk it through. After that, the agent works from a reviewed spec instead of from the last prompt, logs each decision with its reason, and a commit lands only when your build and tests pass.
What does a spec contain?
 A one-sentence goal, the facts it rests on with file and line, the steps, what an upgrade costs an operator, and the done criteria. The decisions made while building go into a separate YAML file next to it.
What does it cost?
 Nothing. The method, the templates and the Claude Code plugin are MIT licensed.
§ 9
Where it comes from
Essay The Why Never Gets Written Down
 codingsoul.org · April 2026
Essay Next Level Vibe Coding
 codingsoul.org · April 2026
spec-first · by Holger Leichsenring · MIT License · © 2026
 GitHub Agent Smith Blog Privacy Privacy settings

## 关联链接

- https://github.com/holgerleichsenring/specification-first-agentic-development/tree/main/templates

## 导航

- 项目页：[[10-项目/spec-first.dev_b54837d8]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
