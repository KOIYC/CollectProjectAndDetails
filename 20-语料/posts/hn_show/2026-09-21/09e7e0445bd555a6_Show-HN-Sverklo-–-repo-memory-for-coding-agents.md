---
type: "corpus"
item_id: "09e7e0445bd555a6"
title: "Show HN: Sverklo – repo memory for coding agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48326338"
project_url: "https://sverklo.com/"
author: "nike-17"
published_at: "2026-05-29T17:25:16Z"
captured_at: "2026-09-21T02:52:58+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-29"
tags:
  - 语料
  - hn_show
  - author_nike-17
  - story_48326338
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:144d"
---

# Show HN: Sverklo – repo memory for coding agents

> [!info] 一句话导读
> /* proof receipt ◦ public benchmark ◦ visible losses ◦ local-first MIT */

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48326338>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：nike-17　|　发布：2026-05-29T17:25:16Z
> 项目链接：<https://sverklo.com/>
> 采集：2026-09-21T02:52:58+08:00　|　id：`09e7e0445bd555a6`

## 正文

Skip to content
sverklo
reports
 compare
 bench
 proof
 repo memory
 perf
 research
 playground
 blog
github
 --
v0.29.5
/* proof receipt ◦ public benchmark ◦ visible losses ◦ local-first MIT */
Run the proof before your coding agent edits.
Same task, same coding agent, better repo evidence. Sverklo gives Claude Code, Cursor, Windsurf, and Codex-style agents your repo's files, symbols, callers, tests, dependencies, diffs, and git-pinned decisions before they edit.
Inspect the public 180-task benchmark, then run a receipt on a real repo. MIT, local by default, telemetry off by default; an explicitly configured remote embedding provider may receive code chunks. Caveat: grep still wins exact strings.
$ npm exec … sverklo prove --no-write --guided --markdown copy
compare same task →
 proof guide →
 repo memory →
 read benchmark →
Run the copied command from a real repo, follow the proof guide , then paste the markdown receipt into the proof thread . No project files or MCP config are written; first run may cache the local ONNX model/index under ~/.sverklo .
180 hand-verified retrieval tasks
6 OSS codebases in the bench
5 baselines, including grep
0 code upload
MIT licensed
~/your-project
 claude code
Claude Code
 Cursor
 Antigravity
 Other
# prove first; no project files or MCP config written
 $ npm exec --yes --package=sverklo@latest -- sverklo prove --no-write --guided --markdown
✓ trial mode ← no project files or MCP config written
 ✓ guided selection ← why this symbol was picked
 ✓ repo memory proof ← central files + real caller graph
 ✓ markdown receipt ← paste into GitHub, Discord, Reddit
# paste the proof prompt into Claude/Cursor/Codex
 > Use sverklo impact on validateToken and tell me what would break if I changed its signature.
› impact symbol="validateToken"
 ─ src/routes/auth.ts:18 requireAuth() direct caller
 ─ src/middleware/auth.ts:42 authMiddleware() direct caller
 ─ src/tests/auth.test.ts:31 login flow test coverage
 ✓ caller graph in 23ms — signature change is not local
# install sverklo
 $ npm install -g sverklo
# add to .cursor/mcp.json (or Cursor Settings → MCP)
 $ cat .cursor/mcp.json
 {
 "mcpServers": {
 "sverklo": {
 "command": "sverklo",
 "args": ["mcp", "."]
 }
 }
 }
# Cursor agent picks up sverklo on next session
 > where do we handle stripe webhooks?
› context task="stripe webhook handling"
 ─ src/api/webhooks/stripe.ts:14 handleStripeEvent() score: 0.92
 ─ src/billing/events.ts:31 processCharge() score: 0.78
 ✓ bundle: 4 files, 2 memories — 1,840 tokens
# install sverklo and run init — Antigravity is auto-detected
 $ npm install -g sverklo
 $ cd your-project && sverklo init
✓ ~/.gemini/antigravity/mcp_config.json ← global MCP config
 ✓ added sverklo (project: ~/your-project)
 Restart Antigravity to pick up the new MCP server.
# Gemini in Antigravity uses sverklo via MCP
 > review my branch before I merge to main
› review_diff ref="main..HEAD"
 ─ ◆ risk 52 src/api/billing.ts
 2 removed symbols still referenced; 8 importers
 › test_map ref="main..HEAD"
 ─ 5 covered · 1 uncovered (risk 78)
 verdict: BLOCKED — fix dangling refs in 3 files
# one server, all your repos — no per-project config needed
 $ npm install -g sverklo
 $ cd ~/api && sverklo init # auto-registers
 $ cd ~/frontend && sverklo init # auto-registers
 $ sverklo setup --global # one-time global MCP config
# now every AI editor has access to all your repos
 $ sverklo list
 api ~/api 37 tools fresh
 frontend ~/frontend 37 tools fresh
Use Sverklo when relationships matter.
Your agent needs callers, dependencies, tests, diff risk, or prior repo decisions before editing. Start with the no-write proof command before installing MCP config.
Use grep/ripgrep when the string is known.
If the repo is tiny, the change is one file, or you know the exact string, grep is the sharper first move. Use the project test runner to verify behavior.
same task, same agent
What changes when the agent gets repo evidence first?
This is an illustrative capability comparison: the baseline column lists a file-search path, while the Sverklo column lists relationship evidence available before an edit. It does not measure edit quality.
Task
Change an auth helper signature without breaking callers, tests, or prior project decisions.
Baseline path
The agent greps likely names, reads a few files, and may miss indirect callers or stale decisions after context compaction.
Sverklo path
impact , refs , test_map , and recall show real callers, covered tests, dependencies, and git-pinned decisions.
Evidence changed
Files, symbols, callers, tests, dependencies, diffs, and decisions appear before the model writes code.
Scope + caveat
This is an evidence-input difference, not a measured editing outcome. If you already know the exact string or the repo is tiny, grep is still the sharper first move.
Capability source: v0.29.5 documentation plus labeled maintainer-seeded examples. No measured or external same-task editing outcome is claimed; an external receipt remains the top proof gap.
/* 90-second walkthrough — terminal then live Claude Code MCP integration */
▶
 1:36 · sverklo init → audit → compact default profile (37 tools available) → Claude Code
seeded receipts from real repos
Don't trust the claim. Run the proof.
sverklo prove --markdown prints a shareable receipt from the current repo: central files, one real symbol, real callers, and the exact prompt to paste into your coding agent.
These examples are maintainer-seeded so you can inspect the shape before installing. They are not third-party validation; external receipts and corrections are the current ask.
Sverklo
maintainer-seeded example
TypeScript MCP server, CLI, benchmark harness, telemetry worker, and site worktree in one receipt.
#79
Express
maintainer-seeded example
Middleware-heavy JavaScript repo: real entry points, core symbols, and caller relationships.
#79
Fastify
maintainer-seeded example
Large Node framework with plugin and route structure that rewards graph-aware retrieval.
comment
Zod
maintainer-seeded example
TypeScript validation library where symbol precision matters more than keyword matching.
comment
Zustand
maintainer-seeded example
Compact state library showing whether the proof remains useful when the repo is not huge.
comment
$ npm exec … sverklo prove --no-write --guided --markdown copy
paste your receipt →
 see benchmark →
/* what happened when we published the bench */
A public benchmark, two competitors, fixes shipped on both sides in 36 hours.
Apr 28
 Published 180-task bench across 6 codebases with two competing local-first MCP code-intel servers (jcodemunch-mcp, GitNexus) and the slices where sverklo lost — including FastAPI P5 dead-code (0.00 vs grep's 1.00).
May 2 → 3
 jcodemunch maintainer @jgravelle shipped v1.80.7 / 1.80.8 / 1.80.9 against specific bench findings. P5 recall 0.00 → 1.00 ; lodash P1 0/10 → 9/10 .
May 4
 Adding lodash to the bench exposed the symmetric blind spot in sverklo's parser. sverklo v0.20.2 ships the fix. Sverklo P1 0.30 → 0.73 ; overall F1 0.45 → 0.56 on that run.
"the bigger opportunity here is the potential genesis of an 'MCP Server Arena' on par with what the leading AI/LLM/Chatbot arenas provide…"
— Jake Gravelle, jcodemunch-mcp maintainer, on r/mcp
180
hand-verified tasks
6 OSS codebases · 5 baselines
0.58
overall F1
canonical May 13 bench run
35 ×
fewer input tokens
vs naive grep on that bench
losses
published too
grep and baselines still win slices
methodology + losses →
 ·
 sverklo-bench ground truth + reproducer
 ·
 preprint · Zenodo · CC BY 4.0 →
/* honest about when this helps */
Sverklo doesn't replace grep. It complements it.
SVERKLO WINS
✓ Exploratory questions ("how does the auth flow work?")
✓ Refactor blast radius ( impact )
✓ Large interconnected codebases
✓ Memory across sessions, tied to git SHAs
✓ Project audits — god nodes, dead code
VS
GREP WINS
— Focused diff review
— Exact string matching
— Reading file contents
— Build & test verification
— Anything where you already know the symbol
Sverklo is the right tool when you don't know exactly what to search for . When you do know, grep is fine.
/* diff-aware mr review */
your agent
reviews like
a senior dev.
AI coding agents are bad at code review for one reason: they read the diff, not the codebase. Sverklo's diff-aware tools fix this.
Point them at any git ref or range and get blast radius, dangling references, missing tests, and a per-file risk score in one round trip — not twenty greps.
Five reviewer workflows ship as MCP prompts. Visible in every IDE picker.
~/your-project
 review main..HEAD
> /sverklo:pre-merge
› review_diff ref="main..HEAD"
 ─ 7 files changed (12 added, 3 removed, 4 modified)
## ⚠️ Highest-risk files
 ─ ◆ risk 78 (critical) src/auth/session.ts
 no matching tests; security-sensitive; 14 importers
 ─ ◆ risk 52 (high) src/api/billing.ts
 2 removed symbols still referenced; 8 importers
› test_map ref="main..HEAD"
 ─ 5 covered · 2 uncovered
 ─ ◆ risk 78 src/auth/session.ts ← block merge
› impact symbol="oldValidateToken"
 ─ 4 dangling references in 3 files — must fix
verdict: BLOCKED — 1 critical, 4 dangling refs
per-file risk · main..HEAD
 low med high
src/auth/session.ts
 78
no tests · 14 importers · sec-sensitive
src/api/billing.ts
 52
2 dangling refs · 8 importers
src/lib/jwt.ts
 34
covered · 6 importers
src/utils/clock.ts
 12
covered · 1 importer
score = importance × untested-ness × churn × dangling-refs
v0.17 → the GitHub Action posts inline review comments on every PR alongside the sticky summary, anchored to the heuristic-flagged lines.
01
risk score
Every changed file gets a 0–100 score combining untested status, security-sensitive paths, importer fan-in, caller count, dangling references, and churn. Reasons are explicit — no black box.
02
missing-test detection
test_map walks the diff, the import graph, and filename conventions to flag changed code without matching tests — ranked by risk.
03
dangling-ref check
Every removed symbol is checked against the symbol-reference graph. If a caller still exists, the merge is blocked with file:line evidence.
04
mcp prompts
Five workflows: /sverklo:review-changes , /sverklo:pre-merge , /sverklo:onboard , /sverklo:architecture-map , /sverklo:debug-issue .
/* review-quality benchmark — published, not claimed */
METHOD
Real merge requests across 5 OSS repos (Express, FastAPI, etc). Same Claude model, same prompt, with and without sverklo's diff-aware tools. F1 vs human-written review. Harness in benchmark/ — reproducible.
RESULTS
+29% F1 after parser improvements on P1/P2 categories. 2–4× fewer tokens per review on most repos. Mixed results on small focused diffs (built-in tools win there). Honest receipts beat marketing math.
WHY WE PUBLISH MIXED
Competitors claim "5–10× fewer tokens" with no methodology. We'd rather be the tool you trust than the one you screenshot. The benchmark harness is in the repo — clone it, run it on your codebase, decide for yourself.
/* historical performance snapshot — 2026-04-08 · sverklo v0.2.11 · one Apple Silicon laptop */
SEARCH p95
26 ms
Historical v0.2.11 result on facebook/react (4,368 files, 20k chunks). Smaller measured repos were 11–14 ms. Hardware- and corpus-specific; not current-release performance.
IMPACT ANALYSIS
<1.2 ms
Historical v0.2.11 impact render result on React's most-called symbol. This snapshot does not establish current-release latency.
COLD INDEX (REACT)
152 s
Historical v0.2.11 result: 2.5 minutes for this 4k-file React corpus, about 7 ms/chunk on the measured machine. Current results may differ.
Historical 2026-04-08 snapshot: Sverklo v0.2.11 on an Apple Silicon laptop with Node 25 and --expose-gc . Steady-state RAM was ~200 MB; measured indexing peaks were 400–700 MB. Method: node --expose-gc scripts/perf-benchmark.mjs  . Source: BENCHMARKS.md at fc37202 . See the full historical snapshot .
/* repo evidence graph */
indexed.
ranked.
remembered.
Sverklo parses your codebase into files, symbols, callers, tests, dependencies, diffs, and decisions before the agent edits. Every query runs through BM25 text search + vector similarity + PageRank ranking , fused via Reciprocal Rank Fusion.
Memories are linked to git commits, so stale decisions are detected automatically instead of silently reused after compaction.
By default, the bundled ONNX provider runs locally with no API key. If you explicitly configure a remote embedding provider, code chunks may be sent to that provider. Telemetry is off by default.
01 · task
"change this auth helper safely"
→
02 · evidence
files · symbols · callers
 tests · deps · decisions
→
03 · rank
PageRank + RRF fusion
 channel weights, path × 1.5
→
04 · agent prompt
edit plan with caveats
 not a blind context dump
01
hybrid search
BM25 for precision, semantic embeddings for recall, PageRank for structural importance — fused via RRF. Built for relationship-heavy questions; use grep/ripgrep for exact strings or tiny repos.
02
local embeddings
all-MiniLM-L6-v2 via the bundled ONNX provider by default. Its 384-dimensional vectors are generated on your machine with no provider API call, so code chunks stay local on that path. An explicitly configured remote embedding provider may receive code chunks under that provider's terms.
03
pagerank ranking
Files that are imported by many others rank higher. Your agent finds the actually-important code first, not just keyword matches.
04
persistent memory
Save decisions, patterns, and preferences with git-state linking. Stale memories flagged automatically when referenced files change.
05
multi-repo + cross impact
One MCP server serves all your repos via a global registry. Trace how a change ripples across dependent repos. No per-project config needed — sverklo init in any repo, done.
06
configurable pagerank
Drop a .sverklo.yaml in your project root to tune PageRank weights, boost or penalize paths, and customize ranking to match your codebase's shape.
07
incremental
File watcher updates the index on every save. Dependency graph and PageRank recompute in real time. Always fresh.
08
24 languages
10 first-class with structural parsing, 14 via regex fallback.
/* persistent memory */
your agent
finally
remembers.
Every AI coding session starts from zero. Decisions vanish after context compaction. Sverklo fixes this with persistent memory linked to git state .
On sverklo init , your existing CLAUDE.md, .cursorrules, and ADRs get parsed into searchable memories — categorized, tagged, and embedded automatically.
Tell your agent to remember new things as they come up. Ask later. It's already there.
tuesday → thursday · two conversations, one memory
 remember + recall
# tuesday — agent saves the decision
 > we picked Prisma for the ORM because of better TypeScript types
› remember category="decision"
 ✓ memory #42 saved · main@a3f29e1
# thursday — new conversation, fresh context window
 ─────────────────────────────────────────────────────
 Loaded 3 memories: ORM choice, auth pattern, API conventions
> add a new API endpoint for user profiles
# Claude already knows: Prisma + JWT (from memories #42, #43)
 › writes endpoint with Prisma + JWT — no rediscovery
#42
 decision
"We chose Prisma over Drizzle for better TypeScript types."
kind semantic
scope workspace [ws]
tags database · orm
git main@a3f29e1
valid_from a3f29e1
confidence 1.0
v0.17 → remember scope:"workspace" writes once, surfaces across every repo in the workspace.
init
 on import
sverklo init imports your existing project knowledge:
CLAUDE.md (12)
.cursorrules (3)
docs/adr/001-prisma.md
docs/adr/002-auth.md
CONTRIBUTING.md (1)
18 memories · categorized, tagged, embedded
v0.17 → sverklo memory export pushes them to markdown / Notion / JSON.
·
bring your own docs
Auto-imports memories from CLAUDE.md, .cursorrules, AGENTS.md, CONTRIBUTING.md, and ADRs on init. Your existing project knowledge becomes semantically searchable instantly.
·
bi-temporal git memory
Every memory has valid_from_sha and valid_until_sha . Memories are never deleted, only superseded — so you can query "what we believed at commit X" and see when code drift made that advice stale.
·
staleness detection
If a memory references a file that no longer exists, it's flagged as stale. No more advice based on deleted code.
·
semantic recall
Memories are embedded and searched the same way as code. Ask "what did we decide about auth?" and get the relevant memory.
·
auto-inject on session start
An MCP resource surfaces top memories to Claude before you type anything. Your decisions travel across sessions automatically.
37 MCP tools for search, impact analysis, review, and memory — defaults to a compact core profile for common code-intelligence sessions. Full reference on GitHub.
/* comparison matrix */
what Sverklo bundles
in one local MCP server.
Use this as a starting matrix, not a winner-takes-all claim. Some tools optimize for hosted review, some for editor-native search, and some for memory only. Sverklo's lane is local repo evidence for agents before they edit.
Tool
 Code-native
 Local-first
 MCP drop-in
 Git-aware memory
 Symbol graph
 Bi-temporal
 Cross-repo
▸ sverklo
 ●
 ●
 ●
 ●
 ●
 ●
 ●
mempalace
 —
 ●
 ●
 —
 —
 ●
 —
claude-mem
 —
 ●
 CC only
 —
 —
 —
 —
Mem0
 —
 crippled
 SDK
 —
 —
 —
 —
Zep / Graphiti
 —
 Neo4j
 ●
 —
 —
 ●
 —
Augment Code
 ●
 cloud
 ●
 —
 ●
 —
 —
Greptile
 ●
 cloud
 3rd party
 —
 ●
 —
 —
Aider repo-map
 ●
 ●
 —
 —
 —
 —
 —
Zilliz claude-context
 ●
 Milvus
 ●
 —
 —
 —
 —
XRAY MCP
 ●
 ●
 ●
 —
 partial
 —
 —
Different lanes: Most "AI memory" tools (mempalace, claude-mem, Mem0, Zep) are built to remember conversations . Sverklo is built to understand code . We index 24 languages (10 first-class with structural parsing, 14 via regex fallback), build a symbol-level dependency graph, and run hybrid BM25 + vector + PageRank search — then bolt a bi-temporal memory layer on top that's tied to git commits, not wall-clock time.
The wedge: Sverklo ties code evidence and memory to git state, then warns when the code has drifted since a decision. If you want conversation memory, use mempalace. If you want local repo evidence before agent edits, run a Sverklo proof receipt.
Want a deeper dive? See side-by-side comparisons → against Serena, GitNexus, codebase-memory-mcp, Cursor @codebase, and Sourcegraph Cody.
/* install */
install.
prove.
code.
WORKS WITH
 Claude Code
 Cursor
 Windsurf
 Zed
 VS Code
 JetBrains
 Antigravity
 & any MCP client
01 — prove
Run a no-write proof receipt
npm exec --yes --package=sverklo@latest -- sverklo
prove --no-write --guided --markdown copy
 Requires Node 24+. Does not write project files, MCP config, or agent instructions. Read the proof guide.
02 — preview
Inspect setup writes first
npm install -g sverklo
sverklo init --dry-run copy
 Shows the exact project and home-directory config files before changing anything.
03 — wire
Initialize only after proof looks useful
sverklo init
sverklo doctor --agent claude copy
 Writes MCP config, agent instructions, and setup checks. Use a different agent name for Cursor, Codex, Windsurf, VS Code, Zed, or Antigravity.
/* questions we get asked */
questions,
honestly
answered.
How do I stop Claude Code from hallucinating function names that don't exist in my codebase?
 Claude Code hallucinates function names because it generates from training-data patterns rather than your actual symbol graph. It will write getUserByEmail() when your code uses findByEmail() , invent imports for packages you don't depend on, and forget yesterday's design decision because context was compacted. Sverklo solves this with a 37-tool MCP retrieval layer the agent calls before writing code: lookup resolves a name to its definition with file:line, refs proves whether a symbol exists with caller context, verify lets the agent re-check that a quoted span is still present at the cited git SHA. Run npm exec --yes --package=sverklo@latest -- sverklo prove --no-write --guided --markdown to see central files and a real caller graph before writing MCP config. The bundled ONNX provider is local and needs no API key; an explicitly configured remote embedding provider may receive code chunks.
Why would I install another MCP server?
 Most MCP servers are single-purpose wrappers around an API. Sverklo is local-first code intelligence: hybrid search (BM25 + embeddings + PageRank), symbol-level impact analysis, diff-aware PR review, and bi-temporal memory. The default bundled ONNX provider runs on your laptop with no API key. If you explicitly configure a remote embedding provider, code chunks may be sent to that provider. It works with Claude Code, Cursor, Windsurf, Zed, VS Code, JetBrains, and Google Antigravity, so if you already have an MCP client, sverklo just appears as 37 new tools alongside whatever else you run.
How is Sverklo different from Cursor's @codebase or Claude Context?
 Cursor's @codebase indexing is cloud-based and tied to the Cursor editor. Claude Context (Zilliz) requires a Milvus database. Sverklo defaults to embedded SQLite and bundled local ONNX embeddings, works across every major AI coding agent via the MCP protocol, and adds symbol-level impact analysis and bi-temporal memory that neither offers. A remote embedding provider is optional and must be explicitly configured.
Does Sverklo work offline?
 Yes, when you use the default bundled ONNX provider. After the first-run model download (~90MB, cached locally), indexing, search, embeddings, memory, and the dashboard can run offline. An explicitly configured remote embedding provider requires its endpoint and may receive code chunks. Telemetry is opt-in and off by default.
Which AI coding agents does Sverklo support?
 Sverklo works with any AI coding agent that speaks the Model Context Protocol (MCP): Claude Code, Cursor, Windsurf, Zed, VS Code, JetBrains, and Google Antigravity. The sverklo init command auto-detects which clients you have installed and writes the right config files.
Is Sverklo free and open source?
 Yes. The current server is MIT licensed. All 37 tools in the current OSS server have no usage limits and opt-in telemetry is off by default ( see /security ). A future Sverklo Pro tier may add smart auto-capture and larger embedding models, and Sverklo Team may add shared team memory; current OSS functionality should not be gated by those tiers.
How do I install Sverklo in Claude Code?
 Run npm exec --yes --package=sverklo@latest -- sverklo prove --no-write --guided --markdown from your project first. It prints a real repo-memory receipt without writing project files or MCP config. It may cache the local model/index under ~/.sverklo , but it does not mutate your project. If the proof looks useful, run npm install -g sverklo , sverklo init --dry-run , then sverklo init . Restart Claude Code and the sverklo tools appear in the /mcp list.
What programming languages does Sverklo support?
 24 languages total. 10 first-class with structural parsing: TypeScript/TSX, JavaScript, Python, Go, Rust, C# (tree-sitter), plus Vue (SFC), Markdown, and Jupyter notebooks (custom parsers). 14 more via regex fallback: Java, C, C++, Ruby, PHP, Kotlin, Scala, Swift, Dart, Elixir, Lua, Zig, Haskell, Clojure, OCaml. Hybrid search works across all 24; symbol-level impact analysis is sharpest on the first-class 10.
When is Sverklo the wrong tool?
 Sverklo is the right tool when you don't know exactly what string to search for. When you do know the literal string, plain grep is faster and more reliable. On a 30-file repo, you don't need Sverklo. It earns its place on large interconnected codebases where AI coding agents waste thousands of tokens reading the wrong files.
/* one proof receipt · local by default · MIT-licensed */
prove it on your repo.
Run the receipt, inspect the callers/tests/decisions it finds, and share the part that is wrong or useful. The bundled provider is local; an explicitly configured remote embedding provider may receive code chunks. Telemetry is off by default.
$ npm exec … sverklo prove --no-write --guided --markdown copy
inspect receipts →
sverklo
Code intelligence
for AI agents.
MIT licensed.
product
Reports
Compare
Retrieval bench
MCP code-intel index
Performance
Playground
Badge
Blog
Security
links
GitHub
npm
Issues
Changelog
Bench methodology
docs
README
CLAUDE.md
Research paper (PDF)
LISTED ON
© 2026 · sverklo (сверкло)
 ◌ built by humans who lost hours to grep

## 导航

- 项目页：[[10-项目/sverklo.com_c11f6263]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
