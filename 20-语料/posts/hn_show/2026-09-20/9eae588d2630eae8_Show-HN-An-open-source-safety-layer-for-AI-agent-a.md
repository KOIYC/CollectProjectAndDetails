---
type: "corpus"
item_id: "9eae588d2630eae8"
title: "Show HN: An open source safety layer for AI agent actions"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49714619"
project_url: "https://github.com/CTRLRun/ctrlrun"
author: "arpanghoshal"
published_at: "2026-09-15T16:03:31Z"
captured_at: "2026-09-20T14:06:04+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_arpanghoshal
  - story_49714619
  - show_hn
metrics: {"points": 4, "comments": 1, "engagement_velocity": 4}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:90d"
---

# Show HN: An open source safety layer for AI agent actions

> [!info] 一句话导读
> The execution safety layer for AI agents.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49714619>
> 指标：点赞=4 · 评论=1 · engagement_velocity=4
> 作者：arpanghoshal　|　发布：2026-09-15T16:03:31Z
> 项目链接：<https://github.com/CTRLRun/ctrlrun>
> 采集：2026-09-20T14:06:04+08:00　|　id：`9eae588d2630eae8`

## 正文

# CTRLRun/ctrlrun

The execution safety layer for AI agents.

- Stars: 22
- Forks: 0
- Watchers: 22
- Open issues: 8
- License: Apache License 2.0
- Homepage: https://ctrlrun.dev/docs
- Default branch: main
- Created: 2026-09-03T05:41:58Z

## Languages

- MDX
- Python
- Shell

## Topics

- agent-control-standard
- agent-security
- agentic-ai
- ai-agents
- ai-safety
- audit-log
- human-in-the-loop
- langgraph
- llm
- llm-security
- mcp
- mcp-server
- model-context-protocol
- openai-agents
- opentelemetry
- owasp
- python
- tool-calling

## Top Contributors

- arpanghoshal (555 contributions)
- rohanrkamath (91 contributions)
- dependabot[bot] (6 contributions)
- mintlify[bot] (1 contributions)

---

## README

 ctrlrun stops AI agents from taking wrong, restricted, or malicious actions in your workflows.
 Every action is checked against your rules before it runs. Allowed actions go through.
 Sensitive ones wait for a person. Forbidden ones are blocked.

 Execution safety for AI agents. A Python library that sits between the decision to act and the call that acts.
 A consequential action happens at most once, exactly as approved, and leaves a receipt.
 When the outcome is unknown, ctrlrun says so instead of guessing.

 Runs in production on a single file, or on Postgres across hosts. Apache-2.0.

```bash
pip install ctrlrun && ctrlrun demo
```

## What it does

**The model guesses. ctrlrun does not.** The ticket says refund €500. The agent asks for
€5,000, one extra zero. The tool is in its list, the arguments are well formed, and the model
is completely confident. Nothing above the call disagrees, because nothing above the call is a
check: a tool being callable is not permission to call it with those arguments.

| Without ctrlrun | With ctrlrun |
|---|---|
| Nothing checks the amount. The call goes through. **€4,500 too much.** | Your rule checks the amount. The call never leaves. **€0 wrongly paid.** |

ctrlrun is that check. It reads the arguments about to leave your process and answers what may
happen to them: let it run, ask a human, or stop it cold. Four rules do the work, and each one
is a test in this repository before it is a sentence here.

| | |
|---|---|
| **Exact means exact** | Changed arguments need a new approval. |
| **Once stays once** | Same effect key, shared store, no repeat. |
| **Unknown means wait** | Confirm the outcome before retrying. |
| **Every answer is kept** | Requests, decisions and results, refusals included. |

The third one is the half people forget. A correct €500 refund commits at the provider and the
reply is lost coming back, so the agent retries. Retry libraries, agent frameworks and tool
loops collapse *this failed* into *I do not know what happened*. ctrlrun keeps them apart: a
lost reply is `AMBIGUOUS`, never `FAILED`, and a retry against an `AMBIGUOUS` effect is refused
until a human, or a `reconcile` hook, says what happened.

 What ctrlrun demo shows: five failures and five refusals, byte for byte

```console
$ ctrlrun demo
ctrlrun demo — five ways an agent action goes wrong, and what stops it.
Policy: refunds up to €1,000 are autonomous, up to €10,000 need a human, above that are denied.

1. Duplicate effect after a lost response

   refund €500  →  remote commits  →  response lost  →  effect: AMBIGUOUS
   agent retries the same refund
   ✗ BLOCKED — effect may already have committed; blind retry refused
   remote refund calls: 1
   only a human moves it on:  ctrlrun resolve refund:txn_1 --committed|--failed

2. Approval mutation

   agent proposes refund €2,000  →  human approves apr_0aa78e0380ba55d77a601dc782f57095 (bound to the action hash)
   agent executes refund €5,000  →
   ✗ BLOCKED — approved action ≠ requested action (mismatch)

3. Concurrent agents, same effect

   Agent A  reserve refund:txn_123  →  ACQUIRED  →  executes
   Agent B  reserve refund:txn_123  →
   ✗ BLOCKED — already reserved (in_progress)

4. Approval replay

   approval apr_dbc8bc6f06690cdf2e2c55a4e591ef3b used once  →  consumed
   same approval presented again                            →
   ✗ BLOCKED — single-use approval already consumed

5. Authority escalation

   human €100,000 delegable  →  finance agent €25,000  →  support agent €2,000
   support agent's grant: dlg_5f8d41938a3f29972d5489d676cd9edb
   support agent requests €50,000  →
   ✗ BLOCKED — outside the delegated grant (authority_constraint)
   remote refund calls: 0
   finance agent tries to delegate €50,000 under its own €25,000  →  refused (containment: constraints)
   support agent requests €1,500  →  authority permits it, and the policy asks a human (apr_f86eca24dd80206ab5189ccb1b62aa55)
   two axes, and an action needs both: the stricter of the pair wins

Receipts (8): .ctrlrun/demo/receipts.jsonl
Events:       .ctrlrun/demo/events.jsonl

Read them:    CTRLRUN_STATE=.ctrlrun/demo/state.db ctrlrun receipts
```

Approval and delegation ids are generated per run; everything else is exactly what the demo
prints, and a test fails if the two drift apart. No network, no external service, under a
second. `pip install ctrlrun && ctrlrun demo` runs it locally in about the same time.

**Where it stops.** It does not detect prompt injection: it contains the consequence rather
than reading the cause. It cannot promise exactly-once against a remote it does not control, it
refuses to *knowingly* act twice, and it rolls nothing back. Receipts are chained, so an alteration
is detected; a truncation at the end and a forged append are not, because the head that would catch
them is a row in the same database, and closing that is what `ctrlrun anchor` is for. They are not
signed: alteration is not authorship. The badge above means the
**declared guarantees pass** in the setup they ran against, and it does not mean secure, safe,
compliant, certified or audited:
what the badge means
· `OWASP-AGENTIC-TOP10.md`
names the four entries this does not address.

If an agent only reads and answers, you do not need ctrlrun. The moment it can **send, pay,
refund, delete, deploy, grant, revoke, approve, submit, purchase or cancel**, you do.

## Use it in three steps

The animation above is this section, recorded against the real library: one policy file, two
short programs, four commands, nothing staged.

**1. Install it.**

```bash
pip install ctrlrun
```

**2. Write down what the agent may do.** One file, `ctrlrun.yaml`. Amounts are integer minor
units, so `50000` is €500. Both ends of every band are bound, because an upper bound alone lets
a negative amount through, and a refund of a negative amount is a charge. Anything not listed is
denied; there is no default-allow.

```yaml runnable
schema: ctrlrun.policy/v2

actions:
  stripe.refund:
    effect: "refund:{payment_id}"
    rules:
      - when: { amount_gte: 0, amount_lte: 50000 }
        decision: allow      # up to €500: the agent acts alone
      - when: { amount_gte: 0, amount_lte: 1000000 }
        decision: approve    # up to €10,000: a human decides
      - decision: deny       # above that: never
```

**3. Wrap the call that has the consequence.** The decorator names the action, the effect key
names the consequence it has in the world, and the context names who is acting. `stripe` here
is a stand-in that records calls instead of making them.

```python runnable file=agent.py
import sys

import ctrlrun

class FakeStripe:
    """Stands in for the provider: it records calls instead of making them."""

    def __init__(self) -> None:
        self.calls: list[tuple[str, int]] = []

    def refund(self, payment_id: str, amount: int) -> dict:
        self.calls.append((payment_id, amount))
        return {"id": f"re_{payment_id}", "amount": amount, "status": "succeeded"}

stripe = FakeStripe()

@ctrlrun.protect("stripe.refund", effect="refund:{payment_id}")
def refund(payment_id: str, amount: int) -> dict:
    return stripe.refund(payment_id, amount)

if __name__ == "__main__":
    with ctrlrun.context(agent="support-agent"):
        print("€500   ->", refund(payment_id="txn_1", amount=50_000)["status"])
        try:
            refund(payment_id="txn_2", amount=500_000)
        except ctrlrun.ApprovalRequired as pending:
            print("€5,000 -> a human decides:", pending.request_id)
            with open("request_id.txt", "w") as handle:
                handle.write(pending.request_id)
        else:
            sys.exit("the €5,000 refund ran without a human; the policy is not in force")
    print("calls that reached the provider:", len(stripe.calls))
```

The €500 refund runs on its own. The €5,000 one stops and names the request a human answers:

```text
€500   -> succeeded
€5,000 -> a human decides: apr_63e80076f2cccfee52b17491a4b2e125
calls that reached the provider: 1
```

**A human answers from the shell.** The grant names the hash of the exact action the human
read, and when it lapses. Ids, hashes and dates are generated per run; yours differ.

```bash runnable
ctrlrun approve "$(cat request_id.txt)"
```

```text
granted apr_63e80076f2cccfee52b17491a4b2e125 for sha256:22ec1c398e4b93d080b6cba61e5e11b0e21879552ac5dbf63c192d2b2e6af752
expires 2026-09-13T20:10:11.367Z
```

**The agent presents it, then tries to spend it on something else.** The first call is exactly
what the human approved, and it runs. The second is the same approval with one digit changed,
and it matches nothing:

```python runnable file=approved.py
import sys

import ctrlrun

from agent import refund, stripe

with open("request_id.txt") as handle:
    request_id = handle.read().strip()

with ctrlrun.context(agent="support-agent"), ctrlrun.with_approval(request_id):
    # Exactly what the human read: €5,000 on txn_2.
    print("€5,000 with the approval ->", refund(payment_id="txn_2", amount=500_000)["status"])

    # The same approval, one digit changed.
    try:
        refund(payment_id="txn_2", amount=900_000)
    except ctrlrun.ApprovalMismatch:
        print("€9,000 on that same approval -> refused")
    else:
        sys.exit("a mutated action ran on a human's approval; that is the bug this exists to stop")

print("calls that reached the provider:", len(stripe.calls), "(the €9,000 never left)")
```

```text
€5,000 with the approval -> succeeded
€9,000 on that same approval -> refused
calls that reached the provider: 1 (the €9,000 never left)
```

Every attempt, refusals included, left a receipt, and `ctrlrun receipts` lists them. That is the
whole integration: a policy file, a decorator, a context, and `with_approval` to present a grant.
Money is the example, not the scope. A condition is ` _ `, so the same policy
language reads `role_in: [reader, viewer]` or `replicas_lte: 10` as easily as `amount_lte`, and
nine domains below have one policy each.
Protect your first action walks the same path
with every output explained ·
Policy YAML reference ·
Cookbook: refunds, deploys, IAM, deletions, email, MCP.

## Three ways to use it

**You probably do not need an adapter.** `@protect` covers anything running in this process: a
raw model call, a LangChain tool, a hand-rolled loop, a cron job. The gateway covers anything
that reaches its tools over MCP, in any language.

| You have | Use | Needs |
|---|---|---|
| Python in this process | the `@protect` decorator, shown above | nothing beyond `pip install ctrlrun` |
| Tools behind an MCP server, in any language | the gateway: `pip install "ctrlrun[gateway]"` | one command, no change to agent or server code |
| A framework with its own approval interrupt | an adapter | the framework to have a human-in-the-loop primitive |

**It works with agents you can and can't modify.** WhatsApp, Slack and Teams bots, ChatGPT,
Cursor, Codex, OpenAI Agents: any AI agent you have. ctrlrun checks the action, not the
agent, so if the agent acts through a tool server or an API you run, the action is checked, and
the agent is not rebuilt, redeployed or told.
Agents you can't modify says where the
boundary goes for each kind.

An adapter exists for one reason: to route an `approve` decision through the framework's own
interrupt, so a human answers where they already answer. There is never a second place to say
yes. `ctrlrun-langgraph`
gives **prevention**, because the resumption carries the arguments and core re-checks them
against the hash.
`ctrlrun-openai-agents`
gives **attribution**, because that SDK records *that* a call was approved and not what its
arguments were. None of the three is only for agents: a worker, a webhook handler and a
scheduled job cannot tell a first attempt from a retry either.

## How it works

Every protected call, whichever way it arrives, goes through the same seven steps. Only then
does it reach your systems.

```text
  normalize  →  decide  →  approve  →  reserve  →  execute  →  resolve  →  record
```

1. **Normalize: one action, one id.** The call becomes an `Action`: a name, canonical arguments
 (sorted keys, no floats), a resource, the principal. Its SHA-256 is the action hash.
2. **Decide: allow, ask or block.** Authority first (may *this principal* propose this at all,
 and within what bounds?), then policy (how much autonomy does *this action* get?). Unknown
 action, missing policy or missing principal is `deny`. Silence is never permission.
3. **Approve: bound to this action.** A human answers against the action hash. The approval is
 single-use, expires, and matches nothing but that exact action, so arguments changed after
 the answer void it and a person answers again. Name a `preconditions=` provider and the
 approval is also bound to the resource state it was granted against, rechecked strictly
 before the reservation: that **narrows** the window between the answer and the execution,
 from minutes of deliberation to milliseconds. It does not close it, because the recheck is a
 network call and cannot run inside the atomic write.
4. **Reserve: claimed once.** The effect key, `refund:txn_1` or `namespace:prod-eu:checkout`, is
 taken in one atomic write. A second caller, in another process or on another host, is refused.
5. **Execute: your code runs.** Only `NotExecuted`, raised by you, means `FAILED`; every other
 exception and every timeout means `AMBIGUOUS`. Deciding which one you are looking at is the
 hard part, so `ctrlrun.transport` does it for you: `urlopen`, `HTTPConnection` and
 `HTTPSConnection` from stdlib `urllib` and `http.client`, which raise `NotExecuted` only where
 the connection they opened was handed no request byte. After one byte, every failure stays the
 exception it was, and the outcome is `AMBIGUOUS`. No setting widens that.
6. **Resolve: unknown is not failed.** An `AMBIGUOUS` effect keeps its key and refuses a retry
 until `ctrlrun resolve`, or a `reconcile` hook that asked the remote, says what happened.
 Nothing runs twice on a guess.
7. **Record: a receipt either way.** A portable JSON receipt: who, what, decision, approval,
 effect key, outcome, and the hash of the policy that decided it, chained to the receipt
 before it. Refusals get one too.

**Who may ask, and how much.** The policy decides the action and cannot see who is asking. Who
may ask at all is a second axis, authority: every principal needs a grant, a delegation cannot
widen one, and an action needs both axes, the stricter of the pair. Since 0.9 a grant can also
carry a **budget**, a metric with a limit over a rolling window, consumed on reserve inside the
same write, so a thousand refunds that each pass `amount_lte` cannot add up to more than the
grant allows. An `AMBIGUOUS` effect holds its budget until it is resolved, because otherwise an
agent that can manufacture ambiguity could manufacture authority. A budget bounds what the next
reservation may do; it cannot recall an action already in flight.
Authority has the whole model.

State lives in SQLite by default, a file with no server and no ops, and the reservation holds
across processes rather than merely across threads. Point it at Postgres when more than one
host writes: `pip install "ctrlrun[postgres]"`, one URL, the same guarantees graded by the same
suite. Prove it in your own setup with `ctrlrun verify`, which runs the kernel's own failure
scenarios against *your* policy in a scratch store. It reaches no network: the only sockets it
opens are to the store you named and to loopback listeners it bound itself, which is how it
grades the transport classifier.

| Guarantee | `@protect` | Gateway | Adapter |
|---|---|---|---|
| **Approval binding** — An approval is bound to the exact action; a mutated or replayed one is refused. | yes | yes | prevention or attribution, per adapter |
| **One effect, once** — One logical effect happens at most once, across threads, processes and hosts. | yes | yes | yes |
| **Unknown is not failed** — An unknown outcome is AMBIGUOUS, never FAILED, and blocks a blind retry. | yes | yes | yes |
| **Fail closed** — An unknown action, a missing policy or a missing principal is denied. | yes | yes | yes |
| **Authority and delegation** — Every principal needs a grant, delegation cannot widen one, and a grant bounds the total. | yes | yes | yes |
| **Receipts** — Every executed action leaves a portable JSON receipt of who, what and outcome. | yes | yes | yes |

## The same shape in nine domains

Nothing in ctrlrun knows what a refund is. An action is a **name**, **canonical arguments**, an
**effect key** and a **resource**, and the three questions asked of it are the same whichever
domain it came from: how much autonomy does *this action* get, did a human approve *this exact*
action, and has this effect already happened. Two things carry your domain, and you write both.

- **The effect key is the only domain knowledge in the system.** It is the string that says two
 calls are the same real-world consequence: `refund:{payment_id}`,
 `namespace:{cluster}:{name}`, `grant:{user_id}:{role}`, `prescription:{patient_id}:{drug}`.
 Name it well and a retry cannot act twice; leave it out and there is nothing for *at most
 once* to be about.
- **Conditions are arguments, not amounts.** The language is ` _ `, so the same
 operators read `replicas_lte: 10`, `role_in: [reader, viewer]` and `to_domain_eq: acme.com`
 as easily as `amount_lte`. A band is available to a domain that has never issued an invoice.

| Domain | Autonomous | A human decides | Never |
|---|---|---|---|
| DevOps | `k8s.scale_deployment` to 10 replicas | `terraform.apply` | `k8s.delete_namespace` |
| Security operations | `firewall.add_deny_rule` | `firewall.add_allow_rule` | `edr.disable_protection` |
| Healthcare | `appointment.reschedule` | `patient.export_record` | `prescription.change_dose` |
| Legal | `document.draft_internal` | `document.file_with_court` | `contract.execute` |
| HR | `pto.approve` within a band | `payroll.run` | `employee.delete_record` |
| Insurance | `claim.request_documents` | `claim.approve_payout` above a band | `policyholder.delete` |
| E-commerce | `inventory.adjust` within a band | `price.update` | `customer.delete` |
| Public services | `eligibility.precheck` | `benefit.terminate` | `record.delete` |
| Payments | `stripe.refund` under €500 | `stripe.refund` above it | `stripe.delete_customer` |

Read any row left to right and it is one rule wearing different nouns. The security row is the
one to read twice: adding a **deny** rule to a firewall is autonomous and adding an **allow**
rule is not, which no amount threshold would have told you. The policy is where your judgement
about your domain gets written down; ctrlrun is what makes it hold.

## Documentation

**docs.ctrlrun.dev** is the documentation: concepts, guides, a cookbook, the
full reference.

| | |
|---|---|
| Start here | Why · Protect your first action |
| The ideas, and doing something with them | Concepts · Guides · Cookbook |
| Agents and MCP | Agents you can't modify · MCP overview · The gateway in five minutes · Approve from your assistant |
| Running it for real | Production · Postgres · Recovery · Operations |
| Every key, flag and error | Reference · FAQ |
| Compared with | Idempotency keys · Framework human-in-the-loop · Guardrail libraries · Durable workflows · Governance toolkits |
| What holds, and what does not | Threat model · What `verify` proves · `CLAIMS.md`, every sentence mapped to its test · How this is built |

## Contributing

Issues and pull requests are welcome:
`CONTRIBUTING.md` and
`CODE_OF_CONDUCT.md` have the
working agreement, and
`SECURITY.md` is how to report a
vulnerability. Every claim in this file has a test behind it, so a change to the prose usually
means a change to the suite.
`CHANGELOG.md` and
`https://docs.ctrlrun.dev/ROADMAP` say
where it is going. Releases carry PyPI provenance attestations from GitHub Actions.

## License

Apache-2.0. The enforcement kernel is and will remain fully open source.

## 评论（1/1）

> **arpanghoshal** · 2026-09-15T16:13:12.000Z　
> Please let me know what you think of it. I feel like in the chaos of everyone using AI agents, people are actually neglecting how much harm consequential actions by those agents can cause, so my friend and I created this.I am available all the time for any questions you have. If you need help, take a look at the documentation here: https://ctrlrun.dev/docs/get-started/quickstartYou can also star the repo, which motivates me and my friend to keep working on this project.Thanks, HN :)

## 关联链接

- https://ctrlrun.dev/docs
- https://docs.ctrlrun.dev/ROADMAP`

## 导航

- 项目页：[[10-项目/github.com_75ee641a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
