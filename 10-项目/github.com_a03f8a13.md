---
type: "project"
title: "Show HN: SCIP MIP solver bindings for Go, ported from russcip"
project_url: "https://github.com/egoisutolabs/scipgo"
first_seen: "2026-09-20T09:37:11+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_generalist_dev
  - story_49714495
  - show_hn
lang: "en"
---

# Show HN: SCIP MIP solver bindings for Go, ported from russcip

> [!info] 一句话导读
> Go Bindings for SCIP

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/egoisutolabs/scipgo>
> 首次收录：2026-09-20T09:37:11+08:00
> 来源渠道：HN Show HN
> 标签：author_generalist_dev, story_49714495, show_hn
> 最新指标：点赞=11 · 评论=0 · engagement_velocity=11

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=11 · 评论=0 · engagement_velocity=11 | [[20-语料/posts/hn_show/2026-09-20/7da08fa0f069a374_Show-HN-SCIP-MIP-solver-bindings-for-Go,-ported-fr]] |
| 2026-09-20T09:37:11+08:00 | HN Show HN | 点赞=11 · 评论=0 · engagement_velocity=11 | [[20-语料/posts/hn_show/2026-09-20/7da08fa0f069a374_Show-HN-SCIP-MIP-solver-bindings-for-Go,-ported-fr]] |

## 摘要正文

# egoisutolabs/scipgo  Go Bindings for SCIP  - Stars: 8 - Forks: 0 - Watchers: 8 - Open issues: 7 - License: MIT License - Homepage: https://pkg.go.dev/github.com/egoisutolabs/scipgo/scip - Default branch: main - Created: 2026-09-03T07:44:37Z  ## Languages  - C - Go - Linear Programming - Mathematical Programming System  ## Topics  - golang - mixed-integer-programming - optimization  ## Top Contributors  - gendev1 (59 contributions)  ---  ## README  # scipgo  Go Reference CI Go Report Card License: MIT  Go bindings for SCIP, one of the fastest non-commercial solvers for mixed integer programming (MIP) and mixed integer nonlinear programming (MINLP). scipgo is a port of the Rust crate russcip and follows its API closely, so the two are easy to move between.  ```go model := scip.DefaultModel().HideOutput().Maximize() x := scip.NewVar().Name("x").Int().Obj(3).AddTo(model) y := scip.NewVar().Name("y").Int().Obj(4).AddTo(model) model.Add( 	scip.NewCons().Coef(x, 2).Coef(y, 1).Le(100), 	scip.NewCons().Coef(x, 1).Coef(y, 2).Le(80), )  solved := model.Solve() sol, _ := solved.BestSol() fmt.Println(solved.Status(), sol.ObjVal(), sol.Val(x), sol.Val(y)) // Optimal 200 40 20 ```  ## Features …
