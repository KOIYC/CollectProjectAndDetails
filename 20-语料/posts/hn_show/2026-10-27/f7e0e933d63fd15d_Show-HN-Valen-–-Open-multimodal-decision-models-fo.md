---
type: "corpus"
item_id: "f7e0e933d63fd15d"
title: "Show HN: Valen – Open multimodal decision models for text, images and video"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50258996"
project_url: "https://valen-team.github.io/"
author: "yhzan"
published_at: "2026-10-27T13:30:15Z"
captured_at: "2026-10-27T23:46:32+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-27"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_yhzan
  - story_50258996
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Valen – Open multimodal decision models for text, images and video

> [!info] 一句话导读
> Skip to main content

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50258996>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：yhzan　|　发布：2026-10-27T13:30:15Z
> 项目链接：<https://valen-team.github.io/>
> 采集：2026-10-27T23:46:32+08:00　|　id：`f7e0e933d63fd15d`

## 正文

Skip to main content
 valen Documentation Cookbook EN 中
Developer quickstart: no model download Ask Valen
 Ask Valen Text Image Video
Output Yes / No Choices Rating
 Ask Valen
Text, images, or video. Ask away. · Inputs are sent to Valen
 A few things you can ask
 Pick a question to get started
 Read a message
 What does this customer need?
Look at an image
 What is this group of animals called?
Look at a video
 What color is the sauce on the left?
FROM PROBABILITY TO ACTION Automate the clear cases. Review the rest.
 Evaluate Valen for ticket intent routing: how much work can you automate at an acceptable error rate?
0.8B 2B 4B
 Held-out replay
 Validation error target 1.0% 2.0% 5.0% 10.0% Rules are frozen on validation data. The observed test result is shown alongside.
11.5% automated
 0.7% observed accepted error 95% CI 0.1%–3.8%
 88.5% sent to review
Accepted 147 / 1276 questions; 1 error. A validation target is not a guarantee for test or deployment.
 BANKING77 · English · 77 candidate intents · 1276 test questions · retrospective public-test replay.
 Automated coverage vs. error rate Original Calibrated
 Stated probability vs. observed accuracy Original Calibrated Dashed: ideal calibration
Why trust these numbers? Compare calibration and inspect the scope Probability distribution: how many questions fall in each range? Top probability exactly 1: 0 original, 0 calibrated.
 Same held-out test; lower is better except accuracy. Metric Original Calibrated
 ECE 0.0819 0.0518
 NLL 1.3564 1.3240
 Brier 0.5062 0.4996
 Accuracy 63.5% 63.5%
Valen-0.8B · c2c481fcb319 · 1276 test questions
 BANKING77 · English · 77 candidate intents · retrospective public-test replay. Not a production or vision guarantee.
 ECE uses 15 equal-width bins and top candidate probability. Error bars are pointwise 95% Wilson intervals; correlated questions can make them too narrow.
 Full report JSON.gz · 551 KB Study temperature artifact Dataset source Study protocol Selected routing policy
 Downloaded parameters are bound to this historical model and recipe. Refit and validate for your own workflow.
 Try ticket routing Evaluate on my data Evidence and methodology
 COMMUNITY PROJECTS Built and explored with Valen
 Community projects explore Valen through serving, experiments and datasets. Check each project’s version, license and scope.
RESEARCH EVALUATION 1 snapshot
 Jev-ToM
 Evaluates Valen-Preview-0923 on Theory of Mind benchmarks and cites its model card in the paper.
 CC BY 4.0; source data has separate terms MODEL SERVING 780 snapshot
 vLLM Jev
 Serves Valen-Preview-0923 for text, images and short video on documented Linux and Mac paths.
 Apache-2.0 REFERENCE SERVING 61 snapshot
 System1-Omni
 A Python reference worker for Valen-Preview-0923 with text and single-image inputs.
 License not specified SIMULATION CONFIGURATION 10 snapshot
 JevLight
 Traffic-signal simulation with configurations for Valen models.
 License not specified MODEL EXPERIMENTS 0 snapshot
 reflex
 Valen-0.8B reference and MLX experiments on synthetic game frames.
 License not specified DATASET EVALUATION 463 snapshot
 LLM2Jev
 Uses Valen-Eval-Game to evaluate its own inference pipeline on single-step Sokoban decisions.
 Apache-2.0
 1 / 2 These projects are maintained by their respective authors; inclusion does not imply affiliation, endorsement or independent reproduction.
 Open models. Clear decisions.
valen © 2026 Valen Team / 万澜
 Fast decisions. Continuous evolution.
Build
 Documentation Cookbook Valen API API data handling Transformers inference ONNX & SDKs
 Explore
 JevalKit Models & datasets Leaderboard

## 评论（1/1）

> **iugtmkbdfil834** · 2026-10-27T14:28:19.000Z　
> Why no model download?

## 导航

- 项目页：[[10-项目/valen-team.github.io_3f8e4fce]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
