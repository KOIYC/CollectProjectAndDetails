---
type: "corpus"
item_id: "ae5b540a042fdbd5"
title: "Show HN: Try Vibe Robotics! (IRL or MuJoCo SIM)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50553913"
project_url: "https://github.com/google-deepmind/robotics-antigravity-plugin"
author: "_sshahid_"
published_at: "2026-11-18T23:38:40Z"
captured_at: "2026-11-19T09:43:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-19"
pub_day: "2026-11-18"
tags:
  - 语料
  - hn_show
  - author__sshahid_
  - story_50553913
  - show_hn
metrics: {"points": 11, "comments": 0, "engagement_velocity": 11}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Try Vibe Robotics! (IRL or MuJoCo SIM)

> [!info] 一句话导读
> Hey HN, I'm Salman, a research engineer at GDM Robotics on the team that built this robotics plugin.Whether you're a robotics founder, data company, making RL e…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50553913>
> 指标：点赞=11 · 评论=0 · engagement_velocity=11
> 作者：_sshahid_　|　发布：2026-11-18T23:38:40Z
> 项目链接：<https://github.com/google-deepmind/robotics-antigravity-plugin>
> 采集：2026-11-19T09:43:31+08:00　|　id：`ae5b540a042fdbd5`

## 正文

Hey HN, I'm Salman, a research engineer at GDM Robotics on the team that built this robotics plugin.Whether you're a robotics founder, data company, making RL environments, or just getting FOMO seeing all the cool robotics demos on X, you can just plug in a robot and start prompting away. The plugin we've written up includes skills that steer the model toward following best practices.The benefits of using the plugin are:
- fewer tokens (and therefore thinking time) needed to do bring-up the robot and to reach a successful attempt on your task
- higher fidelity real-to-sim-to-real when creating MuJoCo assets and environments
- leveraging strong motion planning, visual servoing, and collision avoidanceWe have tested on SO-101, YAM, and Franka Duo, but you don't even need real arms to test it out. You can just create cool environments in sim and then prompt the model to control a simulated robot in the environment! (Just make sure to tell it not to use privileged sim state if you want to actually evaluate how good the perception and model intelligence is).Just point your agent to the repo, good luck, and happy tinkering!Let me know if you have any questions! Will answer anything here or feel free to post on the GitHub repo directly.

## 导航

- 项目页：[[10-项目/github.com_641eff8e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
