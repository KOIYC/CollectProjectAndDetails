---
type: "corpus"
item_id: "af3efeacdb8df246"
title: "Show HN: Link proof assistant Lean to Claude, fix your code's hidden assumptions"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49829771"
project_url: "https://github.com/savarin/lean-agent"
author: "kurinikku"
published_at: "2026-09-24T12:37:45Z"
captured_at: "2026-09-24T23:57:22+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-24"
pub_day: "2026-09-24"
tags:
  - 语料
  - hn_show
  - author_kurinikku
  - story_49829771
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Link proof assistant Lean to Claude, fix your code's hidden assumptions

> [!info] 一句话导读
> License: MIT License

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49829771>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：kurinikku　|　发布：2026-09-24T12:37:45Z
> 项目链接：<https://github.com/savarin/lean-agent>
> 采集：2026-09-24T23:57:22+08:00　|　id：`af3efeacdb8df246`

## 正文

# savarin/lean-agent

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-04-04T18:56:27Z

## Languages

- Python

## Top Contributors

- savarin (4 contributions)

---

## README

# lean-agent

**lean-agent** finds the assumptions your code makes but doesn't enforce — then fixes them. It measures each assumption as an Invariant Enforcement Score (IES), iterates until the score plateaus, and leaves you a branch to review. Your tests run every iteration; failures are discarded.

```python
# before — IES: 0.00
def transfer(self, from_id, to_id, amount):
    self.accounts[from_id] -= amount
    self.accounts[to_id] += amount
```

```python
# after — IES: 1.00
def transfer(self, from_id: AccountId, to_id: AccountId, amount: PositiveAmount) -> None:
    # ... validates existence, positivity, sufficient balance ...
    self.accounts = {
        **self.accounts,
        from_id: self.accounts[from_id] - amount,
        to_id: self.accounts[to_id] + amount,
    }
```

```bash
uv pip install lean-agent
lean-agent enforce <repo>
lean-agent score <repo> --min-ies 0.80  # CI gate
```

---

Here's a 13-line ledger.

```python
class Ledger:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id, opening_balance):
        self.accounts[account_id] = opening_balance

    def transfer(self, from_id, to_id, amount):
        self.accounts[from_id] -= amount
        self.accounts[to_id] += amount

    def balance(self, account_id):
        return self.accounts[account_id]
```

Read the `transfer` method. Two lines. Say `from_id` is `"alice"` and `to_id` is `"bob"`. Alice has $100, Bob has $50. We transfer $30.

Line 1: `self.accounts["alice"] -= 30`. Alice now has $70. This is in the dict.

Line 2: `self.accounts["bob"] += 30`. Bob now has $80. Total was $150, still $150.

Now: what if `to_id` doesn't exist? Line 1 succeeds — Alice has $70. Line 2 throws `KeyError`. Total was $150. Total is now $120. The $30 is gone.

If the caller catches the exception, they see the `KeyError`. They don't see that line 1 already succeeded. The error says nothing about the debit. The ledger is silently unbalanced — money debited, never credited.

This is the class of bug that matters most. Not the ones that crash loudly — the ones where the damage is done before anything visibly fails. The system keeps running. The ledger keeps serving balances. The numbers just don't add up anymore.

Every codebase is full of these. The question is: how do you find them?

## What code assumes but doesn't enforce

Look at `transfer` again. It makes five assumptions:

1. `from_id` exists in `self.accounts`
2. `to_id` exists in `self.accounts`
3. `amount` is positive (negative reverses the direction — silently)
4. `amount` is numeric (pass a string, get `TypeError` deep in arithmetic)
5. The source has enough balance (no overdraft protection)

None are checked. None are documented. None are enforced by the type system. They're just... hoped for.

We'll call these **invariants** — properties that must be true for the system to produce correct results. Each invariant sits at some enforcement level:

| Score | Level | What it means |
|-------|-------|---------------|
| 0 | Unguarded | Nothing prevents violation. The code trusts the caller completely. |
| 1 | Convention | A comment or naming convention hints at the rule. |
| 2 | Validated | A runtime check raises on violation. The code defends itself. |
| 3 | Structural | The type system makes violation impossible. You can't express the wrong thing. |

The **Invariant Enforcement Score** (IES) is the average, normalized to 0–1:

```
IES = Σ(scores) / (3 × N)
```

The ledger scores 0.00. Every invariant unguarded.

The interesting thing isn't the number. It's what happens when you try to move it. I want to follow one of these — transfer atomicity — all the way through: how formalization surfaces it, how it scores, and what the fix looks like at each enforcement level.

## What Lean reveals about atomicity

You could stare at `transfer` and eventually notice the atomicity bug. For 13 lines, maybe. For 13,000 lines across multiple modules, probably not.

lean-agent uses Lean 4 — a proof assistant — to formalize the domain. Not to prove theorems. The proofs are all `sorry` (Lean's way of saying "trust me on this"). The value is in writing the types.

To formalize transfer, you start by defining its preconditions — what must be true before a transfer can happen?

```lean
structure TransferPrecondition (l : Ledger) (from_id to_id : AccountId) (amt : PosAmount) where
  sourceExists : l.hasAccount from_id
  destExists : l.hasAccount to_id
  sufficientBalance : ∃ (bal : Amount), l.lookup from_id = some bal ∧ bal ≥ amt.val
```

Three fields. Three assumptions. To construct a `TransferPrecondition`, you must provide all three. The Python code checks none of them.

Now try to write the conservation theorem — total balance is unchanged after transfer:

```lean
theorem transfer_conserves_total
    (l : Ledger) (from_id to_id : AccountId) (amt : PosAmount)
    (pre : TransferPrecondition l from_id to_id amt) :
    True := by
  sorry
```

The proof is `sorry`. But look at the signature. It requires `TransferPrecondition` as an argument. Why? Because without it, the theorem doesn't type-check. If the source account might not exist, `l.lookup from_id` returns `none`, and you can't do arithmetic on `none`. Conservation literally cannot be stated without the precondition that both accounts exist.

This is the discovery moment. You weren't looking for the atomicity bug. You were trying to state what "correct transfer" means. And the type checker told you: you can't state it unless both sides are guaranteed to succeed. If either side might fail, conservation is not a property of this code — it's a wish.

You don't need Lean for this. You could write the preconditions on a whiteboard. The value of the tool is that it won't let you be vague. `hasAccount from_id` — yes or no? The code either checks or it doesn't.

## Scoring it: 0, then 2, then 3

The invariant: transfer must be atomic. Both sides happen, or neither does. The code doesn't enforce this. Score: **0**.

**Validated (score 2).** Add checks before either mutation:

```python
def transfer(self, from_id, to_id, amount):
    if from_id not in self.accounts:
        raise ValueError(f"source account {from_id} does not exist")
    if to_id not in self.accounts:
        raise ValueError(f"destination account {to_id} does not exist")
    if self.accounts[from_id] < amount:
        raise ValueError(f"insufficient balance")
    self.accounts[from_id] -= amount
    self.accounts[to_id] += amount
```

All checks above the mutations. If any fails, we raise before touching the dict. The partial mutation can't happen. Score: **2**.

Good defensive programming. But notice what it relies on: the *ordering* of statements. The checks must come before the mutations. A future refactor that reorders them breaks the invariant. The enforcement is in the control flow, not in the structure of the data.

**Structural (score 3).** Replace two mutations with one expression:

```python
self.accounts = {
    **self.accounts,
    from_id: self.accounts[from_id] - amount,
    to_id: self.accounts[to_id] + amount,
}
```

One expression. No intermediate state. The old dict has Alice at $100, the new dict has Alice at $70 and Bob at $80. `self.accounts` points to the old dict, then the new dict. There's no moment where Alice is at $70 and Bob is still at $50.

Score: **3**. The invariant isn't checked — it's structurally guaranteed. You can't write a partial mutation because there's only one mutation.

That's one invariant, start to finish: surfaced by formalization, scored at 0, hardened to 2, promoted to 3. The same process runs on every invariant lean-agent finds.

## The result

On the ledger, this takes the 13-line class from the top of this page to:

```python
from types import MappingProxyType
from typing import NewType, TypeAlias

AccountId = NewType("AccountId", str)
PositiveAmount = NewType("PositiveAmount", float)
Account: TypeAlias = int | float

class Ledger:
    """Double-entry ledger. Balance is NonNeg — enforced by transfer validation."""

    def __init__(self) -> None:
        self.accounts: dict[AccountId, Account] = {}

    @property
    def accounts_view(self) -> MappingProxyType:
        """Read-only view of accounts. External code should use this."""
        return MappingProxyType(self.accounts)

    def create_account(self, account_id: AccountId, opening_balance: int | float) -> None:
        if not isinstance(opening_balance, (int, float)):
            raise TypeError(f"opening_balance must be numeric, got {type(opening_balance).__name__}")
        if account_id in self.accounts:
            raise ValueError(f"account {account_id} already exists")
        self.accounts[account_id] = opening_balance

    def transfer(self, from_id: AccountId, to_id: AccountId, amount: PositiveAmount) -> None:
        if amount <= 0:
            raise ValueError(f"transfer amount must be positive, got {amount}")
        if from_id not in self.accounts:
            raise ValueError(f"source account {from_id} does not exist")
        if to_id not in self.accounts:
            raise ValueError(f"destination account {to_id} does not exist")
        if self.accounts[from_id] < amount:
            raise ValueError(
                f"insufficient balance: account {from_id} has {self.accounts[from_id]}, need {amount}"
            )
        self.accounts = {
            **self.accounts,
            from_id: self.accounts[from_id] - amount,
            to_id: self.accounts[to_id] + amount,
        }

    def balance(self, account_id: AccountId) -> float | None:
        return self.accounts.get(account_id)
```

IES: 0.00 → 1.00. Eight invariants, all structural. The dict-spread on the transfer is the atomicity fix — one expression, no intermediate state where the debit happened but the credit hasn't. The `MappingProxyType` view means external code can't mutate the accounts dict directly. The `PositiveAmount` NewType means a type checker will flag negative amounts at the call site, not at runtime.

Full source: before → after

## The iteration log

How the score moves. IES: 0.00 → 1.00 in 8 iterations (6 kept, 2 discarded).

| Iter | IES | Δ | What changed |
|------|-----|---|--------------|
| 0 | 0.00 | — | Baseline: 8 unguarded |
| 1 | 0.75 | +0.75 | All 8 invariants: runtime guards + NewType AccountId + isinstance checks |
| 2 | 0.79 | +0.04 | Atomic transfer via `self.accounts = {**self.accounts, ...}` |
| 3 | 0.83 | +0.04 | `balance()` returns `float | None` instead of raising |
| 4 | 0.88 | +0.04 | `PositiveAmount` NewType on amount parameter |
| 5 | — | discard | `type Account = ...` — Python 3.12 syntax, system ast.parse is 3.10 |
| 6 | 0.92 | +0.04 | `Account: TypeAlias` + typed container annotation |
| 7 | 0.96 | +0.04 | `MappingProxyType` read-only accounts view |
| 8 | 1.00 | +0.04 | All 8 invariants at structural enforcement |

The big jump is iteration 1 — going from "nothing is checked" to "everything is checked at runtime" is the highest-leverage change. Iterations 2–8 are promotions: runtime checks (score 2) → type-level enforcement (score 3). Each promotion is smaller in score but deeper in safety. A runtime check catches the bug. A type makes the bug impossible to write.

## How it works

Three phases. Each is a different kind of work.

**Analyze.** Read the codebase. Optionally formalize in Lean. Identify 5–15 critical invariants, prioritized by "invisible when broken" — things that fail silently, not things that crash loudly. Build a frozen evaluation harness (`prepare.py`) that scores each invariant by examining the source code. This harness is the ground truth for the entire run. It doesn't execute the code — it reads it, using AST parsing and pattern matching to detect enforcement levels. Once frozen, it never changes.

**Execute.** Work through pre-planned improvements. Each iteration: implement the change, commit, run the harness, run the test suite. If tests pass and the score improves, keep. If not, `git reset --hard` and move on. The simplicity criterion applies: prefer a 3-line runtime check (score 2) over 50 lines of type machinery (score 3). Cheapest improvement that reaches the target score wins.

**Explore.** The plan is exhausted. Now search for what was missed. Cross-module contracts, invariants that hide at boundaries, validated checks that could be promoted to structural. Run at least 3 iterations. Stop when the score plateaus, or when every invariant is at structural.

## Safety

- **Branch isolation.** All work happens on `lean-agent/ `. Never touches main.
- **Frozen harness.** `prepare.py` is SHA256-locked after analysis. Every score is reproducible.
- **Test-gated.** Your existing tests run every iteration. Failures trigger automatic discard.
- **Dirty-worktree guard.** Won't start with uncommitted changes (the loop uses `git reset --hard`).
- **You merge.** Review the diff. Run your own checks. Merge when satisfied.

## Install

```bash
uv pip install lean-agent
```

```bash
lean-agent enforce <repo>              # full loop: analyze + execute + explore
lean-agent enforce <repo> --direct     # skip Lean formalization
lean-agent enforce <repo> --tag my-run # branch: lean-agent/my-run
lean-agent analyze <repo>              # Phase 0 only — discover invariants, build harness
lean-agent score <repo>                # run harness on current state
lean-agent score <repo> --min-ies 0.80 # CI gate: exit 1 if below threshold
```

Or as a Claude Code plugin:

```
/plugin marketplace add savarin/lean-agent
/plugin install lean-agent@lean-agent
/lean-agent:enforce
```

## Requirements

- Claude Code CLI
- Python ≥ 3.10
- Lean 4 for default mode (not needed with `--direct`)

# pguyot/la_machine

## 导航

- 项目页：[[10-项目/github.com_6abf7a7c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
