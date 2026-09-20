---
type: "project"
title: "Btrfs/ZFS/bcachefs under workloads classic benchmarks skip"
project_url: "https://bartosz.fenski.pl/modern-fs-benchmark"
first_seen: "2026-09-20T03:41:55+08:00"
sources:
  - hn_front
tags:
  - 项目
  - hn_front
  - author_farlight
  - story_49768833
  - front_page
lang: "en"
stale: true
---

# Btrfs/ZFS/bcachefs under workloads classic benchmarks skip

- **项目链接**：https://bartosz.fenski.pl/modern-fs-benchmark
- **首次收录**：2026-09-20T03:41:55+08:00
- **来源渠道**：HN 首页（非 Show HN）
- **标签**：author_farlight, story_49768833, front_page
- **最新指标**：点赞=30 · 评论=23 · engagement_velocity=30

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T03:21:04+08:00 | HN 首页（非 Show HN） | 点赞=23 · 评论=15 · engagement_velocity=23 | [[80-归档/posts/hn_front/2026-09-20/c541f5a56808b3b9_Btrfs-ZFS-bcachefs-under-workloads-classic-benchma]] |
| 2026-09-20T03:32:45+08:00 | HN 首页（非 Show HN） | 点赞=23 · 评论=20 · engagement_velocity=23 | [[80-归档/posts/hn_front/2026-09-20/c541f5a56808b3b9_Btrfs-ZFS-bcachefs-under-workloads-classic-benchma]] |
| 2026-09-20T03:41:55+08:00 | HN 首页（非 Show HN） | 点赞=30 · 评论=23 · engagement_velocity=30 | [[80-归档/posts/hn_front/2026-09-20/c541f5a56808b3b9_Btrfs-ZFS-bcachefs-under-workloads-classic-benchma]] |

## 摘要正文

modern-fs-benchmark  # modern-fs-benchmark  Multi-device CoW filesystems under workloads classic benchmarks skip — latest run 2026-09-07 13:24:30 UTC, kernel 7.0.0-1012-azure, 552 runs recorded · 141 trend points shown · repository  CI runs use loop devices on shared ephemeral VMs (one VM per filesystem): compare shapes and ratios, not absolute MB/s. Each job records a host-calibration anchor — see the table.  ext4/single ext4/md-raid10 ext4/lvm-raid10 xfs/single xfs/md-raid10 xfs/lvm-raid10 xfs/zvol xfs/lvm-raid10-int zfs/mirror zfs/mirror-8k zfs/single zfs/raidz2 zfs/raidz1 btrfs/raid1 btrfs/single btrfs/raid6 bcachefs/replicas2 bcachefs/single bcachefs/ec ext4/md-raid10-luks ext4/md-raid6 zfs/mirror-enc zfs/raidz1-enc zfs/raidz2-enc btrfs/raid1-luks bcachefs/replicas2-enc  ## Summary indices  Score model v1: 100 = the selected cohort median. Metrics are normalized by direction, then geometric-meaned with equal subgroup and group weight. Using 8 recent complete selected-cohort runs; integrity is never averaged. Click a column header to sort; select a score to expand its normalized contributions.  | configuration | Overall Core | Core I/O | Responsiveness | Metadata | Integrity | …
