---
type: "project"
title: "sdli1995/dlssg_for_sm86"
project_url: "https://github.com/sdli1995/dlssg_for_sm86"
first_seen: "2026-09-20T03:18:17+08:00"
sources:
  - github_new
tags:
  - 项目
  - github_new
  - created:>2026-09-06
lang: "en"
stale: true
---

# sdli1995/dlssg_for_sm86

- **项目链接**：https://github.com/sdli1995/dlssg_for_sm86
- **首次收录**：2026-09-20T03:18:17+08:00
- **来源渠道**：GitHub 新星仓库
- **标签**：created:>2026-09-06
- **最新指标**：stars=3531 · forks=207 · open_issues=141

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T02:35:53+08:00 | GitHub 新星仓库 | stars=3526 · forks=206 · open_issues=141 | [[80-归档/posts/github_new/2026-09-20/8a2c75be8fcc43cb_sdli1995-dlssg_for_sm86]] |
| 2026-09-20T02:56:49+08:00 | GitHub 新星仓库 | stars=3529 · forks=207 · open_issues=141 | [[80-归档/posts/github_new/2026-09-20/8a2c75be8fcc43cb_sdli1995-dlssg_for_sm86]] |
| 2026-09-20T03:05:39+08:00 | GitHub 新星仓库 | stars=3530 · forks=207 · open_issues=141 | [[80-归档/posts/github_new/2026-09-20/8a2c75be8fcc43cb_sdli1995-dlssg_for_sm86]] |
| 2026-09-20T03:18:17+08:00 | GitHub 新星仓库 | stars=3531 · forks=207 · open_issues=141 | [[80-归档/posts/github_new/2026-09-20/8a2c75be8fcc43cb_sdli1995-dlssg_for_sm86]] |

## 摘要正文

# DLSSG for SM86（Proxy）- 0.3.4 版本  **中文** · [English](README.en.md)  在 RTX 30 系列（SM86）和 RTX 20 系列（SM75）上启用 NVIDIA DLSS 帧生成（DLSS-G）。Windows x64 / D3D12，运行文件为 `version.dll` 和 `dlssg_sm86.ini`。  ## 本次更新说明  ### 0.3.4  - 修复 0.3.3 在 RTX 30 上的崩溃（启动或开启 DLSS 后显卡驱动重置，《极限竞速：地平线 6》表现为 FHC01；issue #535 / #538 / #540 / #542）。原因：NVIDIA App 的 DLSS 覆盖或 NGX 在线更新生效时，DLSS 超分模型也收到了本项目给 Streamline 的显卡架构改写，在 RTX 30 上走了不属于这张卡的路径，导致 GPU 挂起。现在 NVIDIA 自己的组件一律得到真实架构，改写只对 Streamline 和游戏生效。0.3.3 用户请直接替换 `version.dll`。  ### 0.3.3  - RTX 20 / 30：向游戏改写显卡架构的动作提前到游戏启动时，并改报 RTX 50。使用 Streamline 2.8 的游戏（如《最终幻想 7 重生》）此前在启动阶段就判定「本显卡不支持 DLSS-G」并卸掉帧生成插件（issue #509 / #528）；本版在那之前就装好改写，游戏内的 3X / 4X / 6X 选项也按 RTX 50 放开。 - `Optimized=1` 不再跳过同一组内重复的真实帧拷贝（`SkipRepeatedRealCopy`，各档位都默认关，需要时手动写 `1`）。该项从未在实际游戏中验证，0.3.2 上有画面闪烁报告（issue #532）。档位 `1` 画面仍与官方逐位一致。  ### 0.3.2  - 重写了部分推理内核（310.9 版）：生成画面与官方 DLSS-G 完全一致（RTX 3080 Ti 与 RTX 5070 实测逐位相同；RTX 2080 Ti 的输出与 3080 Ti 逐位相同），不再有损，并有些许加速（3080 Ti 上 0~8%）。 - 优化内核等级调整：`[FrameGeneration] Optimized` 现在是 `0`–`3` 四级。`0` 原厂内核，不加速；`1` 全部加速，画面与官方逐位一致（出厂默认）；`2` 再开有损图像内核，更快，对官方画面 PSNR 约 50 dB 以上（仅 310.9 版）；`3` 全部有损加速，最快。说明见 [`docs/INSTALL.md`](docs/INSTALL.md)。  ### 0.3.1  - 修复 RTX 20 系（Turing）开不了帧…
