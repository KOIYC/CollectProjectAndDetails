---
type: "corpus"
item_id: "2daaafd171a6ece1"
title: "Show HN: Jev-Like Model Learns to Cook"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49870984"
project_url: "https://rlafuente.com/posts/2026-9-26-training-a-small-decision-model-to-cook"
author: "andes314"
published_at: "2026-09-27T21:21:08Z"
captured_at: "2026-09-28T09:47:28+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-28"
pub_day: "2026-09-27"
tags:
  - 语料
  - hn_show
  - author_andes314
  - story_49870984
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Jev-Like Model Learns to Cook

> [!info] 一句话导读
> Teaching a Decision Model to Cook and Cooperate

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49870984>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：andes314　|　发布：2026-09-27T21:21:08Z
> 项目链接：<https://rlafuente.com/posts/2026-9-26-training-a-small-decision-model-to-cook>
> 采集：2026-09-28T09:47:28+08:00　|　id：`2daaafd171a6ece1`

## 正文

home |
 writing |
 post
Teaching a Decision Model to Cook and Cooperate
Published 2026-9-26
Your browser does not support embedded video.
Two independently acting copies of the same decision model serve six soups in 512 ticks. Every move is a native game control.
I trained a decision model to play cooperative Overcooked on one RTX 5080. Two independently acting copies learned to serve six soups in 512 ticks using only native controls. The policy is OpenJev , which applies the idea behind Jev : describe a situation, supply possible answers, and receive probabilities for them. OpenJev uses natural language inference to score whether each proposed answer follows from the context. Expressing actions as text lets the same classifier choose among different action spaces, making it a promising interface for learning through interaction. I’ve released the code and trained model .
Figure 1. Greedy evaluations across the initial attempt, exploration restart, and two-chef continuation. Time starts at zero for each stage. Checkpoint 220 serves six soups.
Learning from native controls
Recent game demos show how much that interface can leave to the surrounding software. TypeSafe's Doom demo uses structured text state, while a separate Doom implementation supplies tactical descriptions, three action choices, and five worked examples. The Jev Pokémon agent goes further: it builds maps from emulator RAM and offers goals such as explore and reach_exit , then uses pathfinding to execute whole sequences of button presses. In my experiment, every decision selects one native control : stay , up , down , left , right , or interact . There is no planner, action graph, pathfinder, role assignment, or macro. Navigation, cooking, and delivery all have to be learned through those six buttons.
I used PufferLib's C Overcooked environment ( Suarez, 2023 ), which follows the cooperative task studied in Overcooked-AI (Carroll et al., 2019) . The wrapper turns each chef's public 43-value observation into plain descriptions of position, inventory, nearby objects, the pot, and the teammate. It appends game rules and eight recent action outcomes without choosing subgoals. For each button, the model scores Your next action should be [action]. , and I normalize its six entailment probabilities into a policy. Both chefs share weights but choose independently from their own observations. The environment applies their actions together, rewards both for delivery, and gives individual shaping rewards for progress through cooking.
A chef must collect and deposit three onions, start cooking empty-handed, fetch a plate, return to the ready pot, and serve the soup. The rules explain these mechanics, but each interaction depends on position, orientation, inventory, and the teammate's movement. A command to move left always means one button press, even when it accomplishes nothing. The history lets the model distinguish successful movement from collisions and failed interactions.
Figure 2. Checkpoint 220 at tick 448. Each chef's observation and action probabilities appear beside the kitchen.
Training through interaction
Training started from a pretrained OpenJev v5 checkpoint with a Qwen3.5 backbone . I used rank-16 LoRA (Hu et al., 2022) and trained the existing NLI head, updating about 1.25 percent of parameters. Each update collected 8,192 decisions across eight kitchens. The algorithm adapted GRPO (Shao et al., 2024) to game trajectories using discounted reward-to-go, a group baseline, and PPO clipping (Schulman et al., 2017) . Adaptive entropy, a small observation-novelty bonus, and a repeated no-op penalty encouraged exploration. The game supplied the learning signal, with no demonstrations or teacher model.
Credit assignment and exploration were the practical difficulties. A single episode score cannot distinguish useful preparation from wasted movement. Discounted reward-to-go credits actions for subsequent rewards, with less weight on distant outcomes. A confident policy could also repeat ineffective actions indefinitely. Entropy encouraged a broader action distribution, novelty rewarded unfamiliar observations, and the no-op penalty discouraged repeated actions that changed nothing. These mechanisms use observations, actions, and rewards without needing a cooking phase detector.
The first attempt ran for roughly ten hours without serving a soup. I restarted from pretrained weights with better credit assignment and exploration, trained one chef until it reached four soups, then used its best adapter to initialize both chefs. Checkpoint 220 followed after another 32.6 hours, bringing the successful training lineage to about 52 hours. Rollout collection reached 61.5 agent actions per second with 7.45 GiB peak allocated VRAM, while backpropagation accounted for most of the time.
Learning to cooperate
The resulting policy divides the work. In the recorded rollout, chef 0 plated the first soup at tick 49 and served it at tick 58. Chef 1 had already added an onion for the next batch at tick 56. Later they reversed roles: chef 1 plated at tick 353 and served at tick 361, while chef 0 added an onion at tick 360. Delivery and preparation overlap, and either chef can take either role. This coordination comes from two independent decisions made with shared weights, without a controller assigning jobs.
The chefs' different positions, inventories, and histories let the same policy favor a plate for one and an onion for the other. Each observes the teammate's position and recent actions before choosing its own button. They exchange no messages and receive no instruction assigning a cook or server. Their alternating roles suggest that the learned behavior responds to the situation rather than a permanent job assignment.
Early rollout
 Three soups
 Six soups
Tick 24
 Tick 232
 Tick 448
Figure 3. The same rollout at three points: preparing the first batch, after three deliveries, and after six deliveries.
What the result establishes
To my knowledge, this is the first public demonstration of adapting a pretrained Jev-style classifier through online reinforcement learning to complete a cooperative game task using only primitive controls. The six-soup result comes from a greedy evaluation of the best checkpoint on one seed and layout. Nearby checkpoints scored zero to six soups, and transferring this checkpoint to a new layout produced none. Testing how the approach scales across environments is the next step.
A bridge to robotics
What I find beautiful about decision models is how naturally they connect classical RL with language models. PufferLib supplies the familiar setting: an environment produces observations, a policy chooses actions, and rewards drive learning. A decision model fits directly into that loop because its output is already an action distribution. Policy gradients, exploration, and credit assignment still apply, while the policy itself starts with representations learned through language pretraining. Describing the available actions in text also means the classifier's output dimensions need not change with every new game. That gives me a concrete way to study whether pretrained knowledge can become useful behavior through experience.
My bet is that general-purpose robotics will be built on transformers combining language, perception, and learning through action. RT-2 (Brohan et al., 2023) and OpenVLA (Kim et al., 2024) already show how pretrained vision-language models can become robot policies. Decision models offer another interface: evaluate actions, act, observe the consequences, and improve from feedback. This experiment begins my work on that idea, using fast simulation to study delayed rewards and cooperation on one GPU. The goal is to expand across tasks toward a model whose understanding of instructions and surroundings improves with its ability to act in them.
References
Almeida, D. (2026). Introducing System One Models & Jev . TypeSafe AI.
AlexWortega (2026). OpenJev . Model card.
Qwen Team (2026). Qwen3.5-0.8B . Model card.
Suarez, J. (2023). PufferLib: Making Reinforcement Learning Libraries and Environments Play Nice .
Carroll, M. et al. (2019). On the Utility of Learning about Humans for Human-AI Coordination . NeurIPS.
Hu, E. J. et al. (2022). LoRA: Low-Rank Adaptation of Large Language Models . ICLR.
Schulman, J. et al. (2017). Proximal Policy Optimization Algorithms .
Shao, Z. et al. (2024). DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models .
Boers, M. (2026). Jev Plays Pokémon Red . Code and documentation.
Dasein Labs (2026). OpenJev Doom demo . Documentation.
Brohan, A. et al. (2023). RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control .
Kim, M. J. et al. (2024). OpenVLA: An Open-Source Vision-Language-Action Model .

## 导航

- 项目页：[[10-项目/rlafuente.com_0d4d074b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
