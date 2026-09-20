---
type: "corpus"
item_id: "681894a435ba2e29"
title: "Show HN: A lightweight compiler for untrusted AI Agent scripts"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48336380"
project_url: "https://autolang.vercel.app/docs/philosophy-vision"
author: "hoansdz"
published_at: "2026-05-30T14:09:27Z"
captured_at: "2026-09-21T02:52:53+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-30"
tags:
  - 语料
  - hn_show
  - author_hoansdz
  - story_48336380
  - show_hn
metrics: {"points": 2, "comments": 2, "engagement_velocity": 2}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:144d"
---

# Show HN: A lightweight compiler for untrusted AI Agent scripts

> [!info] 一句话导读
> Philosophy & Vision

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48336380>
> 指标：点赞=2 · 评论=2 · engagement_velocity=2
> 作者：hoansdz　|　发布：2026-05-30T14:09:27Z
> 项目链接：<https://autolang.vercel.app/docs/philosophy-vision>
> 采集：2026-09-21T02:52:53+08:00　|　id：`681894a435ba2e29`

## 正文

Author: hoansdz

Philosophy & Vision | Autolang Docs

# Why Autolang exists

LLMs are no longer just answering questions — they are executing business workflows, querying enterprise data, and acting on internal systems. The moment an AI starts executing code instead of generating text, its execution environment becomes part of your security model, whether you designed it to be or not.

## The standard approach, and its costs

A common approach is to execute AI-generated code inside a general-purpose runtime (such as Python or Node.js), often isolated using Docker, microVMs, or language-level sandboxes. That works, but it borrows costs that don't disappear at scale.

### Full runtime overhead

The isolation layer boots a complete runtime underneath it. Each session costs real memory and startup time before any AI logic runs.

### Lifecycle plumbing

Someone has to own the orchestration code that bridges host and container — startup, teardown, data marshaling across the isolation boundary.

### Unbounded surface area

Locking down a general-purpose runtime means auditing every standard library surface an AI-generated script could reach — file I/O, sockets, subprocesses, dynamic imports.

Autolang takes a different approach: give the AI a language that was never capable of touching anything it wasn't explicitly handed, and that can never consume more than it was explicitly budgeted — instead of giving it a general-purpose language and fencing it in after the fact.

## Architecture

The AI generates a script. The VM executes it. The VM can only call bindings you registered. Your bindings talk to your systems. At no point does the AI hold a connection string, a file handle, or a socket.

`Prompt
 │
 ▼
LLM ──generates──▶ Autolang script
 │
 ▼
 Autolang VM
 │
 (calls only registered bindings,
 within its instruction & memory budget)
 ▼
 Bindings
 │
 ▼
 Your business system (DB, CRM, ERP, APIs...)`

## Four core ideas

Everything in Autolang — the language, the compiler, the VM, the binding system — exists to enforce these four principles.

#### AI is untrusted

Not because it is malicious, but because it is non-deterministic. The same prompt can produce different code, so the environment has to hold the line the model cannot.

#### The host owns authority

Every credential, connection, and side effect lives in code you wrote and control. Autolang scripts never hold authority directly.

#### Every permission is explicit

If a script can call it, someone on your team registered it on purpose. Nothing is reachable by default.

#### Execution is deterministic and bounded

Given the same script and inputs, the VM does the same thing every time — and it can never run longer or consume more than the budget you set for it.

## Why a dedicated language, not just exposed functions

The natural objection: "I can expose functions to Python too."

The difference is what surrounds the function call. A general-purpose runtime still gives the script access to a much larger execution model than an AI agent actually needs — file I/O, sockets, dynamic imports, arbitrary subprocess calls, unbounded CPU and memory. Locking all of that down after the fact means auditing every standard library surface for what an AI-generated script could reach or consume through it.

Autolang starts from the other direction: default-deny. Built-in capabilities and libraries (such as network access, filesystem, or dynamic bindings) can be selectively enabled, disabled, or configured by the host application. A script can never access unexposed features or run past the resource budget you configured.

## Capabilities, not access

AI does not receive access to your systems. It receives capabilities. A capability is a single, explicitly exposed operation, implemented by your host application and registered with the VM. The AI can invoke a capability it was given — it cannot discover, infer, or reach any operation it wasn't.

Host application (Node.js)

`// Host application (Node.js) — capability boundary
compiler.registerBuiltInLibrary(
 "crm",
 `
 @native("getCustomers")
 fun getCustomers(segment: String): Array
 `,
 { autoImport: true },
 {
 getCustomers: (segment) => crm.getCustomers(segment),
 }
);

compiler.registerBuiltInLibrary(
 "reporting",
 `
 @native("calculateRevenue")
 fun calculateRevenue(customers: Array): Float

 @native("generateReport")
 fun generateReport(data: Float): Report
 `,
 { autoImport: true },
 {
 calculateRevenue: (customers) => reporting.calcRevenue(customers),
 generateReport: (data) => reporting.buildReport(data),
 }
);

compiler.registerBuiltInLibrary(
 "mail",
 `
 @native("sendEmail")
 fun sendEmail(to: String, report: Report): Void
 `,
 { autoImport: true },
 {
 sendEmail: (to, report) => mailer.send(to, report),
 }
);`

What the AI writes

`@import("crm")
@import("reporting")
@import("mail")

val customers = crm.getCustomers("enterprise")
val revenue = reporting.calculateRevenue(customers)
val report = reporting.generateReport(revenue)
mail.sendEmail("cfo@company.com", report)`

Four capabilities, one script, one execution. The AI chains real business logic without a network round-trip to the model between every step, and without ever holding a database credential or an SMTP password. It never opened a database connection, sent an SMTP request, or implemented business logic itself. It orchestrated capabilities that already existed in the host application.

## Resource governance

Capabilities answer "What is the AI allowed to do?" Resource governance answers "How much of the host may it consume while doing it?" Both questions matter independently.

Running AI-generated code is not only a security problem — it is also a resource management problem. A script that burns CPU time, allocates unbounded memory, or never terminates can degrade a whole service, even if it never touches a database or the filesystem.

`AI
 │
 ▼
Permission ← what can it call? (capabilities)
 │
 ▼
Instruction budget ← how much CPU?
 │
 ▼
Memory budget ← how much memory?
 │
 ▼
Execution`

### Instruction budget

The VM executes a bounded number of opcodes per script. A script that exceeds its budget is terminated automatically — it never gets the chance to monopolize a CPU core.

### Managed memory quota

Memory limits apply only to VM-managed objects created by the script itself. Host-managed objects are intentionally excluded because they are owned and accounted for by the embedding application.

### Deterministic hot-restart

State resets cleanly between runs instead of persisting or relying on garbage collection. One script's execution cannot leak cost or state into the next.

#### Default deny

Nothing is reachable unless a binding explicitly registers it. The absence of a registration is not a gap — it is the intended state.

#### Static typing

Type errors are caught at compile time, before a script ever runs. AI-generated type mismatches fail early and loudly.

#### Null safety

Nullable types must be handled explicitly, closing off a common class of AI-generated runtime crashes.

#### Kotlin-inspired syntax

Models already write valid Autolang without extra prompting. The syntax is a convenience, not the point — everything above it is.

## How this compares

Autolang does not compete with WebAssembly runtimes such as Wasmtime or WasmEdge, nor with embeddable scripting engines like V8 Isolates, QuickJS, Duktape, or Lua as general-purpose scripting runtimes. Those solve a different problem well. The comparison worth making is not "Autolang vs. Docker" — it is "Autolang vs. the runtime you would otherwise have to boot inside Docker."

| | Autolang (native) | Autolang (npm/Wasm) | Node.js / Python | Docker Containers | Firecracker MicroVMs |
| --- | --- | --- | --- | --- | --- |
| RAM per instance | ~0.5MB – 0.7MB | ~10MB shared | ~30MB – 50MB+ | Process RAM only | +5MB guest kernel |
| Cold start | ~10ms | ~20ms | ~100ms – 300ms | ~50ms – 200ms | ~125ms |
| Warm / Restore start | ~1–2ms | ~1–2ms | — | — | ~50ms (Snapshot) |
| Isolation boundary | Language sandbox | Language sandbox | None (Process level) | OS (cgroups/namespaces) | Hardware (KVM hypervisor) |
| Resource governance | Opcode & memory budget | Opcode & memory budget | Unbounded by default | Host cgroup limits | Hypervisor vCPU/RAM |

Autolang measurements were collected on Windows 11, Intel Core i5 12th Gen with 16GB RAM (release build, single compiler instance). Node.js/Python baseline and Firecracker microVM figures are based on published runtime baseline specifications and AWS Firecracker microVM architecture benchmarks.

For context: a general-purpose runtime (Python/Node) isolated per session typically runs 30MB–50MB+ on its own before any container or VM overhead is added on top of that — and that overhead sits in addition to the runtime, not instead of it. The comparison worth making isn't "Autolang vs. Docker" — it's "Autolang vs. the runtime you'd otherwise have to boot inside Docker."

### Good fit if

- You are running LLM-generated code in real time and want a hard, explicit allowlist rather than a monitored general-purpose environment.
- You are running many concurrent agents and per-session runtime overhead is a real cost at your scale.
- You are using lightweight or low-cost LLMs and need static type checking to catch API hallucinations before execution.
- You want to bridge existing C++ or JS systems to an AI agent without exposing them directly.

### Not a good fit if

- You are only running a handful of agents and existing Docker overhead genuinely is not a problem.
- The AI needs to author large, complex systems. Autolang is tuned for short, focused scripts, not as a general application language.
- You need OS- or kernel-level isolation guarantees. Autolang sandboxes at the language level; it does not claim to replace that layer.

## Explore Documentation

Execution pipeline stages and host session lifecycle.

#### Security Model

Trust boundaries, default deny, and threat model guarantees.

#### Native Libraries

Registering host bindings and exposing capability interfaces.

#### Security & Sandboxing

Opcode budgets, file path rules, and domain allowlists.

#### Runtime & VM Internals

C++ interpreter, memory arena, and AObject layout.

## In short

Autolang is designed around a simple idea:

An AI should never receive more authority or consume more resources than the host application explicitly allows.

Everything else — the language, the compiler, the VM, and the binding system — exists to enforce that principle.

# Jwrede/tokentoll

## 评论（2/2）

> **hiroto_lemon** · 2026-05-30T14:35:37.000Z　
> Opcode and type limits are the easy part; the real risk is the bindings you expose — one network or payment capability lets type-safe code chain into harm.

---

> **hoansdz** · 2026-05-31T03:46:53.000Z　
> This language is used for isolation at the language level and trusts the code written by the library developer. If absolutely necessary, I think environment isolation should still be used. What do you think of this approach ?

## 导航

- 项目页：[[10-项目/autolang.vercel.app_c7ca7fe3]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
