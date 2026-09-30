---
type: "project"
title: "Show HN: Kguardian – seccomp profiles and NetworkPolicies from eBPF traces"
project_url: "https://github.com/kguardian-dev/kguardian"
first_seen: "2026-09-30T18:28:30+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_mrayas
  - story_49905667
  - show_hn
lang: "en"
---

# Show HN: Kguardian – seccomp profiles and NetworkPolicies from eBPF traces

> [!info] 一句话导读
> At the place where I work, we use the runtime’s default seccomp profile. My colleague and I wanted to see which syscalls our pods actually make, so we decided t…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/kguardian-dev/kguardian>
> 首次收录：2026-09-30T18:28:30+08:00
> 来源渠道：HN Show HN
> 标签：author_mrayas, story_49905667, show_hn
> 最新指标：点赞=2 · 评论=1 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-30T18:28:30+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-30/98856171e1daddaf_Show-HN-Kguardian-–-seccomp-profiles-and-NetworkPo]] |

## 摘要正文

At the place where I work, we use the runtime’s default seccomp profile. My colleague and I wanted to see which syscalls our pods actually make, so we decided to capture and audit them and then generate a workload-specific list of syscalls.We ended up building a feature in our security tool that does exactly that.Blog post: https://dev.to/maheshrayas/part-2-the-seccomp-profile-nobody...
