---
type: "corpus"
item_id: "74dc042db1b5dbf0"
title: "Show HN: A Firewall for AI agents with auditing"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48726867"
project_url: "https://github.com/beebeeVB/trajeckt"
author: "beebeeVB"
published_at: "2026-06-29T23:52:48Z"
captured_at: "2026-09-21T03:11:01+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-29"
tags:
  - 语料
  - hn_show
  - author_beebeeVB
  - story_48726867
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: A Firewall for AI agents with auditing

> [!info] 一句话导读
> A causal firewall for AI agents: blocks multi-step tool-call chains that leak data, even when every call is individually allowed.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48726867>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：beebeeVB　|　发布：2026-06-29T23:52:48Z
> 项目链接：<https://github.com/beebeeVB/trajeckt>
> 采集：2026-09-21T03:11:01+08:00　|　id：`74dc042db1b5dbf0`

## 正文

# beebeeVB/trajeckt

A causal firewall for AI agents: blocks multi-step tool-call chains that leak data, even when every call is individually allowed.

- Stars: 10
- Forks: 0
- Watchers: 10
- Open issues: 0
- License: Apache License 2.0
- Default branch: main
- Created: 2026-05-21T19:46:02Z

## Languages

- Dockerfile
- Makefile
- Python
- Rust
- Shell

## Top Contributors

- beebeeVB (118 contributions)

---

## README

Readme · MD
# trajeckt

**A runtime enforcement gateway for AI agents. It blocks multi-step exploits that
every per-action security check misses — deterministically, in ~1.6ms, outside the
agent's reach.**

Reading a database is allowed. Sending an email is allowed. Doing them in that
order is data exfiltration. Every authorization system on the market checks one
action at a time, so the sequence walks right through. trajeckt checks each call
against the whole trajectory the agent has accumulated and the data flowing
through it — so the exfiltration is blocked at the step that completes it, even
though that step looks legal on its own.

## Run it

The fastest way to see the real gateway enforce is Docker. It brings up the
enforcement gateway plus a mock MCP upstream, with the `traj` compiler bundled
in the image so sealed-commitment enforcement is live out of the box — no
hand-authored config.

```bash
docker-compose up --build
```

Then confirm enforcement is live and drive a session:

```bash
curl -s http://localhost:7777/healthz | jq
# {"status":"ok",...,"commitment_capable":true}
```

Point any MCP-speaking agent at `http://localhost:7777` instead of your real MCP
server. A full smoke test — sensitive read allowed, then the external write that
completes an exfiltration blocked with HTTP 403 — is in DOCKER.md,
and `scripts/smoke_test.sh` runs it end to end and asserts both outcomes.

The first build takes a few minutes (Rust, compiling the gateway and the
compiler from source). After that the stack starts in seconds.

### No Docker? See the core idea in one command

If you just want to see the central insight with zero dependencies — no Docker,
no server, no keys, no network — run the standalone example:

```bash
cargo run --example demo
```

It runs the same three-step agent twice. First the way the industry does it
today: each action evaluated in isolation, all three allowed, customer records
gone. Then through trajeckt's enforcement:

```
  TRAJEKTORYD  (J_t causal enforcement)
  ───────────────────────────────────────────
  Agent A: read_database          →  ALLOW
  Agent B: summarize              →  ALLOW
  Agent C: send_email_external    →  BLOCK
           J_t causal path detected:
           d_customer_records → summarize → d_summary → external_sink
           Reason: sensitive data reached forbidden sink
 
  Result: exfiltration blocked before execution.
```

Same agent, same tools, same legal-looking calls. trajeckt tracks where the data
came from and refuses to let tainted data reach a forbidden sink — no matter how
many clean-looking steps sit in between. (This standalone example exercises the
heuristic safety floor; the Docker path above runs the full sealed-commitment
engine.)

## How it actually works

Before the agent runs, its authorized trajectory is declared in a small spec,
compiled into a graph, and **sealed with an HMAC**. Once sealed, that graph is
the authority. Every tool call is checked against the current reachable frontier
of the sealed graph, fail-closed — an action not in the graph is hard-refused,
and a session with no installed graph is refused before any evaluation runs. The
agent's context window is treated as compromised; enforcement holds state the
agent can't reach.

→ Full architecture and the sealed-commitment flow below.

---

A runtime enforcement gateway for AI agents that enforces **sealed pre-session
commitments**: the agent's authorized trajectory is declared and sealed before
execution starts, and the gateway enforces deterministically fail-closed against
that sealed graph for every tool call in the session.

## What it does

Most agent governance treats each tool call independently: a policy engine sees
`(agent, tool, arguments)` and returns allow or deny. That framing structurally
cannot see violations that live in the ordering and data-flow between actions.

trajeckt addresses this at two levels:

**Primary: sealed commitment enforcement.** Before any tool call is allowed,
the gateway requires a sealed `CompiledGraph` (Gτ) — a cryptographically signed,
operator-approved declaration of exactly which tools the agent may call, in which
order, and to which data sinks. Once sealed, the graph is the authority. Every
tool call is checked against the current reachable frontier of the sealed graph
(Type V enforcement), provenance constraints (Type II), and taint propagation.
An action not in the sealed graph is hard-refused. A session with no installed
graph is hard-refused before any evaluation runs.

**Safety floor: heuristic sequence detector.** When an operator explicitly opts
out of commitment enforcement (`allow_uncommitted: true` in the policy), the
gateway falls back to coarse behavioral-pattern heuristics: exfiltration
sequences (`ReadSensitive → ExternalWrite`) and command-and-control chains
(`ShellExec → NetworkEgress`) are detected and blocked. This is a last-resort
net, not the product. It catches known-bad patterns when running without a
sealed graph; it does not detect violations that stay within the heuristic's
blind spots.

## Quickstart

### Zero-config committed mode

```bash
trajectoryd up --upstream http://your-mcp-server
```

Only `--upstream` is required. `trajectoryd up` always runs in committed mode:

- `auto_commitment=on` — the gateway seals a Gτ from the `tools/list` handshake
 before any tool call is allowed. The sealed graph is **not** heuristic mode;
 it is commitment graph enforcement derived automatically from the declared tool
 set.
- `require_commitment=on` — any session that reaches `tools/call` without an
 installed graph is hard-refused with an explicit block reason, not silently
 downgraded to heuristics.
Point your MCP-speaking agent at `http://localhost:7777` instead of your real
MCP server. The gateway prints the listen address and a `curl /healthz` verify
command on startup.

### Docker

```
docker-compose up
```

Then point your MCP-speaking agent at `http://localhost:7777`. The bundled
`fake-mcp-server` is the upstream by default. See `DOCKER.md` for details.

### From source

```
cargo build --release
./target/release/trajectoryd up \
    --upstream http://your-mcp-server
```

Or with an explicit policy file for corpus, TLS, and budget settings:

```
./target/release/trajectoryd up \
    --upstream http://your-mcp-server \
    --policy   configs/trajectory-policy.yaml.example
```

## Advanced: hand-authored commitments

Zero-config derives a permissive graph covering all declared tools. Operators
who need to pre-declare exact tool scopes, hard budget caps, or ordered task
phases can hand-author a commitment:

**1. Start the gateway**

```bash
docker-compose up --build
```

The example policy at `configs/trajectory-policy.yaml.example` needs one key set
to match what you use with `traj commit`:

```yaml
corpus:
  signing_key: "trajeckt-demo-v1-32byte-key12345"   # must match --key below
```

**2. Author and seal a commitment with `traj commit`**

Install the traj compiler:

```bash
cd /path/to/traj && cargo build --release
export TRAJ_BIN=/path/to/traj/target/release/traj
```

Seal a policy from the MCP tool list and a task description:

```bash
DEMO_KEY_HEX=$(python3 -c "print('trajeckt-demo-v1-32byte-key12345'.encode().hex())")
 
$TRAJ_BIN commit \
    --tools-list mcp_tools_list.json \
    --task       "Read customer tickets and write internal case notes" \
    --budget     money=0,calls=20,secs=60 \
    --out        policy.sealed.json \
    --key        "$DEMO_KEY_HEX" \
    --yes
```

`mcp_tools_list.json` is the `tools/list` response from your MCP server.
`traj commit` narrows the tool list to the task-relevant tools, derives scope
automatically, and seals the graph.

For advanced use (hand-authored `BoundaryCommitment` JSON with explicit
`read_scope`, `write_scope`, `data_sinks`, and `budget`):

```bash
$TRAJ_BIN commit-boundary commitment.json \
    --registry registry.json \
    --key      "$DEMO_KEY_HEX" \
    -o         policy.sealed.json
```

**3. Install the sealed graph**

```bash
python -m trajeckt.install \
    --gateway  http://localhost:7777 \
    --graph    policy.sealed.json
```

Or from Python:

```python
from trajeckt.install import installed_session
 
session_id = installed_session(
    gateway_url="http://localhost:7777",
    sealed_graph_path="policy.sealed.json",
)
print(session_id)   # pass this to make_http_wrapper below
```

`installed_session()` generates a UUID v4 session ID, installs the graph, and
returns the ID so callers pass it to `make_http_wrapper` without a copy-paste
step.

**4. Wrap your agent with the same `session_id`**

```python
from trajeckt_langgraph import make_http_wrapper
from langgraph.prebuilt import ToolNode
 
tool_node = ToolNode(
    tools,
    wrap_tool_call=make_http_wrapper(
        "http://localhost:7777",
        session_id=session_id,   # from installed_session() above
    ),
)
```

> **`session_id` must match the one returned by `installed_session()`.**
> A mismatched ID means the gateway has no sealed graph for that session,
> which now **hard-refuses all tool calls** — the request is blocked with
> `"no commitment installed"` rather than silently falling back to heuristics.
> This is intentional: a mismatch is always a configuration error.

### Runnable end-to-end example

`examples/quickstart_enforced_agent.py` threads one `session_id` through the
entire install → enforce loop and exits non-zero if either the allowed call is
blocked or the unsafe call is allowed (doubles as CI):

```bash
python3 examples/quickstart_enforced_agent.py \
    --gateway http://localhost:7777
```

### Commitment posture and opt-out

| `require_commitment_before_tools` | `auto_commitment` | behavior |
|---|---|---|
| `true` (**default**) | `true` (**default**) | Zero-config committed: commitment auto-installed on `tools/list`, then enforced. A session that reaches `tools/call` without one is **hard-blocked**. |
| `true` | `false` | Manual-commit: operator installs graphs with `traj commit --install`; sessions without a graph are blocked loudly. |
| `false` | any | **Heuristic floor mode.** Requires `allow_uncommitted: true` in the policy to start; otherwise the gateway refuses to start. Prints a WARN to stderr at startup even when the flag is set. |

`require_commitment_before_tools` defaults to `true` when the field is absent
from the policy YAML. `trajectoryd up` hardcodes both flags on regardless of
the YAML file.

To explicitly opt into heuristic floor mode, add to your policy YAML:

```yaml
require_commitment_before_tools: false
allow_uncommitted: true
```

Or pass `--allow-uncommitted` to the `gateway` subcommand. The gateway will
start with a WARN.

### Verifying enforcement with `/healthz`

```bash
curl -s http://localhost:7777/healthz | jq
```

Response:

```json
{
  "status": "ok",
  "signing_key_source": "file",
  "auto_commitment": true,
  "commitment_capable": true
}
```

| field | meaning |
|---|---|
| `status` | `"ok"` (liveness) or `"ready"` (readiness, from `/readyz`) |
| `signing_key_source` | `"env"` — from `TRAJECTORYD_SIGNING_KEY` or `env:VAR` `"file"` — from `~/.trajeckt/key` or `file:/path` or inline policy `"generated"` — freshly generated; key not yet on disk |
| `auto_commitment` | whether the gateway auto-installs commitments on `tools/list` |
| `commitment_capable` | `true` if the `traj` binary is resolvable right now; `false` means auto-commitment WILL fail — install the binary or set `TRAJ_BIN` |

`commitment_capable: false` does not prevent the gateway from starting, but
every `tools/list` response will fail to install a commitment and the session
will be blocked on the first `tools/call` (when `require_commitment_before_tools`
is true).

## MCP conformance

trajectoryd implements the **MCP Streamable HTTP transport, 2025-11-25,
non-streaming profile**.

### Known protocol-surface limitations

The following MCP surface is proxied transparently (no enforcement change) but
is not exercised by `fake-mcp` and not tested for enforcement correctness:

| Feature | Status |
|---|---|
| `resources/*`, `prompts/*` | Gateway proxies all unknown methods. Enforcement does not classify these; they pass through as-is. |
| `sampling/createMessage` | Proxied as an unknown method; no enforcement classification. |
| SSE server-initiated notifications (streaming profile) | Gateway passes `text/event-stream` responses through without parsing SSE content. The non-streaming profile (POST-only) is fully tested. |
| `tools/list` pagination | Gateway injects caps on the **final page only** (`nextCursor` absent), and fires auto_commit on the final page only. Tested end-to-end in `tests/mcp_protocol_conformance_test.rs`. |
| Multi-block `tools/call` results | Passed through unmodified. Enforcement decisions are invariant to block count. Tested in `tests/mcp_protocol_conformance_test.rs`. |

- **POST** `/mcp` and `/` — full request/response enforcement + upstream forwarding.
- **GET** `/mcp` — returns `405 Method Not Allowed` with `Allow: POST`.
 Server-initiated SSE streams are not implemented; this is explicitly permitted
 by the spec for non-streaming servers. The SSE resumability rules
 (`Last-Event-ID`, session replay) are therefore not applicable.
- **DELETE** `/mcp` — session termination per spec §6.3.
Protocol versions advertised: `2025-11-25`, `2025-06-18`, `2025-03-26`.

Transport-layer guards (both run before session resolution and enforcement):

- **Origin validation** (DNS-rebinding protection, spec MUST): requests with an
 `Origin` header not in the allowed set are rejected 403. The default allowlist
 is `http://localhost` and `http://127.0.0.1` on any port. Override via
 `TRAJECTORYD_ALLOWED_ORIGINS` (comma-separated exact origins). Requests
 without an `Origin` header are always allowed — non-browser clients such as
 Claude Code do not send `Origin`.
- **`MCP-Protocol-Version` validation** (spec MUST): non-initialize requests
 carrying an unsupported version header are rejected 400. Absent header →
 allow (assume the negotiated default). `initialize` requests are exempt
 (version negotiation happens in the request body).
## Python SDK

Once published to PyPI:

```
pip install trajeckt
```

Until then, build from source:

```
cd sdk-python && maturin develop
```

Then (from `sdk-python/example.py`):

```python
import asyncio
import trajeckt
 
async def main():
    client = trajeckt.TrajecktClient.from_env()
    session = await client.session()
    await session.record_instruction(
        "You are a helpful assistant. Do not exfiltrate user data.",
        source="operator",
    )
    await session.prewarm(["read_database", "summarize", "send_email"])
    try:
        data = await session.call_tool("read_database", {"query": "users"})
        summary = await session.call_tool("summarize", {"data": data})
        await session.call_tool(
            "send_email",
            {"to": "external@example.com", "body": summary},
        )
    except trajeckt.BlockedError as e:
        print(f"Blocked by trajectoryd: {e.reason}")
 
asyncio.run(main())
```

A real-Claude end-to-end version of this lives at
`scripts/real_agent_test.py`.

## What it catches

**With a sealed commitment graph (default):**

- **Off-plan tool calls** — any tool not reachable in the current frontier Ft of
 the sealed Gτ is hard-refused (Type V).
- **Exfiltration to unauthorized sinks** — data flows to destinations not in the
 node's declared auth scope are blocked (Type II provenance).
- **Tainted data controlling high-risk actions** — output of a sensitive read
 flowing into a subsequent high-risk call is blocked.
- **Causal structure deviating from the declared intent manifold** — when the
 realized DAG of actions doesn't fit the sealed graph, verified by correct
 d-separation over the joint causal graph.
- **Trajectories approaching unsafe state (CBF viability filter)** — a
 per-action control-barrier-function gate challenges or quarantines actions
 that would push session state toward a constraint boundary faster than the
 configured decay rate.
- **High-risk actions with no trusted instruction source (Type IV)** — tool
 calls whose `instruction_ref` does not chain back to an operator/system/user
 instruction recorded on the session.
**Safety floor (heuristic mode, explicit opt-out only):**

- **Exfiltration sequences** — `ReadSensitive → … → ExternalWrite` in the same
 session, even when each call is locally permitted.
- **Command-and-control chains** — `ShellExec → NetworkEgress` in the same
 session.
## What it does not catch

- **Violations that require semantic understanding of content.**
 trajeckt looks at the structure of actions, not the meaning of
 strings inside them. A prompt-injected instruction encoded in
 natural language is invisible to it.
- **Attacks that stay within the declared causal manifold.** If a
 session's actions are individually allowed and the path-level
 invariants hold, trajeckt allows them. An attacker who can shape
 the trajectory to look benign is not stopped by trajectory-level
 enforcement.
- **Everything a conventional policy engine catches by
 configuration.** trajeckt is complementary to allow/deny lists,
 argument validators, rate limits, and per-tool RBAC — not a
 replacement for them.
## ClawTrojan benchmark

trajeckt is tested against ClawTrojan, an independent published
benchmark of trajectory-style agent attacks. The stealthy-delay
pattern (cs_delay_002) is enforced end-to-end: a write to a control
sink (e.g. `memory/`, `AGENTS.md`, `policy/runbook` files) that
consumes memory- or untrusted-origin content is blocked unless a
trusted instruction authorizes it; the same trajectory with a
trusted instruction is allowed (the false-positive guard). This
rests on an origin-trust lattice (Untrusted < Memory < External <
ToolOutput < CleanWorkspace < TrustedUser) with a control-flow floor
that blocks anything below CleanWorkspace from reaching a control
sink without authorization. The lattice and floor are defined
identically in trajeckt and in the Traj language; a shared
equivalence vector (`cross_repo_equivalence_lineage_vector` in
`src/enforcement/commitment.rs`, mirrored in the traj repo's
`traj-verifier`) fails in both repos if either drifts. The
end-to-end attack/guard case is `tests/clawtrojan_cs_delay_002.rs`.

One ClawTrojan pattern is proven end-to-end. The approach
generalizes by construction to the other patterns via the same
origin/sink/instruction primitives, but suite-wide measurement
across all 20 trajectories is not yet done.

## Debugging enforcement

When a tool call is blocked, the block response body tells you exactly what
happened and where to look next:

```json
{
  "decision": "block",
  "reason": "no commitment installed; declare a commitment (declare_commitment tool) before using tools",
  "reason_code": "no_commitment_installed",
  "debug": "GET /sessions/abc-123/decisions",
  "event_id": "...",
  "trajectory_id": "abc-123",
  "stability_score": 0.0
}
```

- **`reason`** — human-readable sentence describing the rule that fired.
- **`reason_code`** — stable snake_case token for programmatic matching.
- **`debug`** — copy-pasteable curl to pull the full session history.
### Session decisions endpoint

```
GET /sessions/{trajectory_id}/decisions
```

Returns the last 100 enforcement decisions for a session as a JSON array,
newest-last. The `trajectory_id` is the same one in every block body.

```bash
# Copy the trajectory_id from the block response, then:
curl http://localhost:7777/sessions/<trajectory_id>/decisions | jq
 
# Example response:
# {
#   "session_id": "abc-123",
#   "count": 3,
#   "cap": 100,
#   "decisions": [
#     {
#       "timestamp_ms": 1749600000000,
#       "event_id": "...",
#       "tool": "read_database",
#       "decision": "allow",
#       "stability_score": 0.0,
#       "trajectory_id": "abc-123"
#     },
#     {
#       "timestamp_ms": 1749600001000,
#       "event_id": "...",
#       "tool": "summarize",
#       "decision": "allow",
#       "stability_score": 0.1,
#       "trajectory_id": "abc-123"
#     },
#     {
#       "timestamp_ms": 1749600002000,
#       "event_id": "...",
#       "tool": "send_email_external",
#       "decision": "block",
#       "reason": "type_v_no_valid_graph_transition",
#       "reason_code": "type_v_no_valid_graph_transition",
#       "stability_score": 0.9,
#       "trajectory_id": "abc-123"
#     }
#   ]
# }
```

This endpoint is **read-only** — it never modifies enforcement state,
approves actions, or exposes signing-key bytes. It shows what was
decided, not why the policy is configured the way it is.

The history is kept in memory (last 100 entries per session) and is not
persisted to the corpus. For durable history, query the corpus files:

```bash
trajectoryd corpus read --dir ./corpus
# or for one session:
curl http://localhost:7777/corpus/session/<session_id> | jq
```

## Live corpus stream

`GET /corpus/stream` is a Server-Sent Events endpoint that broadcasts
every signed corpus event in real time. Clients receive a backfill of
recent events on connect (using `Last-Event-ID` for gap-free
reconnection), then tail the live feed. Each SSE message carries the
full `SignedPropagationEvent` so the client can re-verify the HMAC.
The stream is best-effort: a slow subscriber is dropped rather than
back-pressuring the enforcement path. The corpus JSONL files remain the
single durable source of truth.

## 关联链接

- http://127.0.0.1`
- http://localhost:7777
- http://localhost:7777/corpus/session/
- http://localhost:7777/healthz
- http://localhost:7777/sessions/
- http://localhost:7777`
- http://localhost:7777`.
- http://localhost`
- http://your-mcp-server

## 导航

- 项目页：[[10-项目/github.com_11fd7da0]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
