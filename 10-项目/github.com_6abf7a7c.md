---
type: "project"
title: "Show HN: Link proof assistant Lean to Claude, fix your code's hidden assumptions"
project_url: "https://github.com/savarin/lean-agent"
first_seen: "2026-09-24T23:57:22+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_kurinikku
  - story_49829771
  - show_hn
lang: "en"
---

# Show HN: Link proof assistant Lean to Claude, fix your code's hidden assumptions

> [!info] 一句话导读
> License: MIT License

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/savarin/lean-agent>
> 首次收录：2026-09-24T23:57:22+08:00
> 来源渠道：HN Show HN
> 标签：author_kurinikku, story_49829771, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-24T23:57:22+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-24/af3efeacdb8df246_Show-HN-Link-proof-assistant-Lean-to-Claude,-fix-y]] |

## 摘要正文

# savarin/lean-agent  - Stars: 1 - Forks: 0 - Watchers: 1 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-04-04T18:56:27Z  ## Languages  - Python  ## Top Contributors  - savarin (4 contributions)  ---  ## README  # lean-agent  **lean-agent** finds the assumptions your code makes but doesn't enforce — then fixes them. It measures each assumption as an Invariant Enforcement Score (IES), iterates until the score plateaus, and leaves you a branch to review. Your tests run every iteration; failures are discarded.  ```python # before — IES: 0.00 def transfer(self, from_id, to_id, amount):     self.accounts[from_id] -= amount     self.accounts[to_id] += amount ```  ```python # after — IES: 1.00 def transfer(self, from_id: AccountId, to_id: AccountId, amount: PositiveAmount) -> None:     # ... validates existence, positivity, sufficient balance ...     self.accounts = {         **self.accounts,         from_id: self.accounts[from_id] - amount,         to_id: self.accounts[to_id] + amount,     } ```  ```bash uv pip install lean-agent lean-agent enforce <repo> lean-agent score <repo> --min-ies 0.80  # CI gate ```  ---  Here's a 13-line ledger.  ```python class …
