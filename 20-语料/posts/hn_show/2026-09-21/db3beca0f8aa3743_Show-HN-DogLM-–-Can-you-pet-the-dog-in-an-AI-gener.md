---
type: "corpus"
item_id: "db3beca0f8aa3743"
title: "Show HN: DogLM – Can you pet the dog in an AI-generated game?"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49509649"
project_url: "https://mikeushakov.github.io/doglm"
author: "mikeushakov"
published_at: "2026-08-31T13:37:10Z"
captured_at: "2026-09-21T03:11:22+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - hn_show
  - author_mikeushakov
  - story_49509649
  - show_hn
metrics: {"points": 6, "comments": 1, "engagement_velocity": 6}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:52d"
---

# Show HN: DogLM – Can you pet the dog in an AI-generated game?

> [!info] 一句话导读
> in an AI-generated game?

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49509649>
> 指标：点赞=6 · 评论=1 · engagement_velocity=6
> 作者：mikeushakov　|　发布：2026-08-31T13:37:10Z
> 项目链接：<https://mikeushakov.github.io/doglm>
> 采集：2026-09-21T03:11:22+08:00　|　id：`db3beca0f8aa3743`

## 正文

DogLM
Leaderboard
 Games demo
 Model consistency
 Score distribution
 Interaction types
 Example games
Can you pet the dog
in an AI-generated game?
DogLM is a benchmark measuring whether an LLM, when prompted to build
a video game with a background dog character in it, lets the player pet that dog.
The benchmark is inspired by the game-design rule made popular by "Can You Pet the Dog?" Twitter account ( X , Bluesky ): if a game has a dog, the player should be able to pet it .
DogLM tests whether a model applies this rule and builds a dog-petting mechanism when two conditions are simultaneously met in the game-generating prompt: (1) a dog character is present in the game description and (2) a model receives zero instruction about the player-dog interaction from the game developer.
The benchmark, the games' descriptions, and the detailed methodology are available here .
Read why this benchmark was created or the LessWrong summary of the first observations .
Leaderboard
Mean scores per model
Last update: September 5, 2026
#
 Model
 Mean score (/20)
 SD
 Cued mean (/10)
 Uncued mean (/10)
 Games scored
 Cost per game
 Tested
1 Gemini 3.7 Flash 8.2 0.4 8.0 0.2 50/50 $0.019** Aug 2026
2 Gemini 3.8 Flash 7.2 0.7 7.0 0.2 44/50 $0.039** Sep 2026
3 GPT-6 Astra 6.6 1.4 6.6 0.0 50/50 $0.273 Sep 2026
4 Muse Spark 1.3 5.6 1.5 5.6 0.0 50/50 $0.033 Sep 2026
5 Claude Fable 5.1 5.4 0.8 5.4 0.0 50/50 $0.525 Sep 2026
5 Kimi K3 5.4 0.8 5.4 0.0 48/50 $0.251 Aug 2026
7 Claude Opus 5 5.2 1.6 5.2 0.0 50/50 $0.252 Aug 2026
8 Claude Fable 5 4.8 1.2 4.8 0.0 50/50 $0.323 Aug 2026
9 Grok 4.6 3.8 0.7 3.8 0.0 50/50 $0.060 Aug 2026
10 Grok 4.5 3.4 1.9 3.4 0.0 48/50 $0.040 Aug 2026
11 GPT-5.3 Codex 2.8 0.7 2.8 0.0 50/50 $0.080 Aug 2026
12 GPT-5.6 Sol 2.4 0.5 2.4 0.0 49/50 $0.089 Aug 2026
12 GPT-5.6 Terra 2.4 0.5 2.4 0.0 50/50 $0.060 Aug 2026
12 Qwen 3.8 Max* 2.4 1.5 2.2 0.2 22/50 $0.183 Aug 2026
15 DeepSeek V4 Pro 2.2 1.3 2.2 0.0 48/50 $0.032 Aug 2026
15 Gemini 3.1 Pro 2.2 1.2 2.2 0.0 50/50 $0.157 Aug 2026
17 Qwen 3.7 Max 1.8 1.3 1.8 0.0 49/50 $0.051 Aug 2026
18 Kimi K2.7 Code 1.0 0.0 1.0 0.0 49/50 $0.042 Aug 2026
19 Claude Opus 4.8 0.6 0.8 0.6 0.0 50/50 $0.141 Aug 2026
20 Mistral Large 2512 0.2 0.4 0.2 0.0 50/50 $0.005 Aug 2026
21 GLM 5.2 0.0 0.0 0.0 0.0 41/50 $0.042 Aug 2026
How scoring works: Each generated game is scored on the player-dog interaction: 2 — you can pet the dog; 1 — the dog is interactive, but you can't pet it; 0 — the dog and the player do not interact at all. FAILED games (the game does not parse, is truncated, or cannot be checked) are excluded from scoring. A model's score per run is the sum of its ten game scores, maximum 20. Scores are averaged across runs to get the mean score. Full scoring rubric is in the DogLM repository .
Default protocol: DogLM v1, 5 runs × 10 PRDs per model, judged by Claude Sonnet 4.6. Deviations are marked in the model's row.
* As Qwen 3.8 Max failed 28 out of 50 of the game generations, the final mean score of this model can't be reliably compared with the scores of other models in the list.
** During the test, Gemini 3.7 Flash and Gemini 3.8 Flash were provided on OpenRouter at a promotional discount (75% and 50% respectively).
Games Demo
Watch how the generated games look.
Scores per model per run (Model consistency in generating interactive dogs)
Model
 Run 1
 Run 2
 Run 3
 Run 4
 Run 5
 Mean
 SD
Gemini 3.7 Flash 8 8 8 9 8 8.2 0.4
Gemini 3.8 Flash 7 8 7 6 8 7.2 0.7
GPT-6 Astra 5 7 8 8 5 6.6 1.4
Muse Spark 1.3 4 8 6 4 6 5.6 1.5
Claude Fable 5.1 6 6 6 4 5 5.4 0.8
Kimi K3 6 6 5 6 4 5.4 0.8
Claude Opus 5 4 6 8 4 4 5.2 1.6
Claude Fable 5 5 4 7 4 4 4.8 1.2
Grok 4.6 3 3 5 4 4 3.8 0.7
Grok 4.5 2 3 2 7 3 3.4 1.9
GPT-5.3 Codex 2 4 2 3 3 2.8 0.7
GPT-5.6 Sol 2 3 2 2 3 2.4 0.5
GPT-5.6 Terra 2 2 2 3 3 2.4 0.5
Qwen 3.8 Max* 1 2 1 5 3 2.4 1.5
DeepSeek V4 Pro 2 3 4 0 2 2.2 1.3
Gemini 3.1 Pro 2 1 3 1 4 2.2 1.2
Qwen 3.7 Max 2 2 4 1 0 1.8 1.3
Kimi K2.7 Code 1 1 1 1 1 1.0 0.0
Claude Opus 4.8 0 0 0 1 2 0.6 0.8
Mistral Large 2512 1 0 0 0 0 0.2 0.4
GLM 5.2 0 0 0 0 0 0.0 0.0
Score distribution per model (Can You Pet the Dog?)
Model
 Score 2 (Petting)
 Score 1
 Score 0
 FAILED
Gemini 3.7 Flash 15 11 24 0
GPT-6 Astra 15 3 32 0
Gemini 3.8 Flash 13 10 21 6
Muse Spark 1.3 9 10 31 0
Kimi K3 9 9 30 2
Claude Fable 5.1 8 11 31 0
Claude Fable 5 7 10 33 0
Claude Opus 5 6 14 30 0
Grok 4.6 4 11 35 0
Qwen 3.8 Max* 4 4 14 28
DeepSeek V4 Pro 4 3 41 2
Grok 4.5 3 11 34 2
Gemini 3.1 Pro 2 7 41 0
Qwen 3.7 Max 1 7 41 1
Claude Opus 4.8 1 1 48 0
GPT-5.3 Codex 0 14 36 0
GPT-5.6 Sol 0 12 37 1
GPT-5.6 Terra 0 12 38 0
Kimi K2.7 Code 0 5 44 1
Mistral Large 2512 0 1 49 0
GLM 5.2 0 0 41 9
Each point in the table represents one interactive dog.
Each row is calculated from 50 game generation attempts per model.
Total number of successfully generated games per model is in the Table 1 above (Leaderboard).
Types of Player-Dog Interactions per Model (What the dogs do)
Model
 Petting
 Proximity reaction
 Animation change
 Command response
 Total interactive dogs (/50)
Gemini 3.7 Flash 15 10 1 0 26
GPT-6 Astra 15 2 0 1 18
Gemini 3.8 Flash 13 9 1 0 23
Muse Spark 1.3 9 8 0 2 19
Kimi K3 9 7 2 0 18
Claude Fable 5.1 8 11 0 0 19
Claude Fable 5 7 10 0 0 17
Claude Opus 5 6 11 2 1 20
Grok 4.6 4 9 2 0 15
Qwen 3.8 Max* 4 4 0 0 8
DeepSeek V4 Pro 4 3 0 0 7
Grok 4.5 3 8 1 2 14
Gemini 3.1 Pro 2 6 1 0 9
Qwen 3.7 Max 1 6 1 0 8
Claude Opus 4.8 1 1 0 0 2
GPT-5.3 Codex 0 12 1 1 14
GPT-5.6 Sol 0 10 0 2 12
GPT-5.6 Terra 0 11 1 0 12
Kimi K2.7 Code 0 1 1 3 5
Mistral Large 2512 0 1 0 0 1
GLM 5.2 0 0 0 0 0
Interaction types. Petting: deliberate keypress → pet the dog. Proximity: proximity-triggered response. Animation: dog animation varies as player moves. Command: player-triggered command response (whistle/call/treat).
Each point in the table represents one interactive dog.
Each row is calculated from 50 game generation attempts per model.
Total number of successfully generated games per model is in the Table 1 above (Leaderboard).
Example games
Your companion dog makes circles around you when you pet it
You may adopt a stray dog on a meadow and it will follow you
The dog sits and looks at you when you stand next to it
You can toss a dog treat to your security dog and to your postman's dog
Your service dog is scared of the security alarm sound and moves closer to you when hearing it
If you guess that you can pet the dog using an interaction key, this action will increment the countdown timer in the game
When you start walking next to a stray dog, it points you to the fireflies you have to catch, or sniffs out the gems you need to collect in the maze
DogLM is made by Mike Ushakov .
Want to give feedback, support this benchmark, or collaborate? Ping me via Bluesky , X , or LinkedIn .

## 评论（1/1）

> **mikeushakov** · 2026-08-31T13:38:07.000Z　
> I built DogLM (https://mikeushakov.github.io/doglm/), a benchmark that evaluates whether an LLM, when prompted to build a video game with a background dog in it, lets the player pet that dog.I generated 804 playable games with 17 models and scored the generated games' code using Sonnet 4.6 as LLM-as-judge. First results:1. When a background dog is mentioned in the prompt that generates a game, but the player-dog interaction is not mentioned, an LLM needs to be "forced" by some hint to generate such interactions. Without such a hint, LLMs almost never make background dogs interactive. The hint that allows models to generate interactive dogs doesn't have to explicitly mention dog petting. I used "Add 2-3 game mechanics that a player would enjoy" as such a hint.2. Out of 804 games, only two games generated without such a hint had some weak form of player-dog interaction. None of those two games had pettable dogs.3. In 56 of 804 generated games, the player was able to pet the dog. But all these 56 games needed such a hint.4. In my first test, the most dog-friendly model was Gemini 3.7 Flash, generating 15 pettable dogs and 11 weaker player-dog interactions across 50 generated games.The full data, including the types of generated player-dog interactions, are posted here on my GitHub (link above).I also wrote a long blog post where I explained the idea of the benchmark, the first results, and the constraints of it that I see (it is very likely that I don't see all of them): https://mikeushakov.com/machines-of-spontaneous-warmth/Important disclaimer for HN: I'm a PhD candidate in social sciences, not an AI developer. This is my first benchmark (a proof-of-concept of it). I do understand that it is narrow and not robust yet. Will appreciate your feedback to improve it.

## 导航

- 项目页：[[10-项目/mikeushakov.github.io_2e5027d7]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
