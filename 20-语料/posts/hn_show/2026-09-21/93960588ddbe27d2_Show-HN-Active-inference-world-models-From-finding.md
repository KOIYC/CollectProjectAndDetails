---
type: "corpus"
item_id: "93960588ddbe27d2"
title: "Show HN: Active inference world models: From finding a mug to making tea"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49123549"
project_url: "https://cpnslab.com/active-inference-world-models"
author: "alexdshaw"
published_at: "2026-07-31T14:23:45Z"
captured_at: "2026-09-21T03:11:06+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-31"
tags:
  - 语料
  - hn_show
  - author_alexdshaw
  - story_49123549
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: Active inference world models: From finding a mug to making tea

> [!info] 一句话导读
> Computational Psychiatry & Neuropharmacological Systems

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49123549>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：alexdshaw　|　发布：2026-07-31T14:23:45Z
> 项目链接：<https://cpnslab.com/active-inference-world-models>
> 采集：2026-09-21T03:11:06+08:00　|　id：`93960588ddbe27d2`

## 正文

Skip to content
C
CPNS Lab
 Computational Psychiatry & Neuropharmacological Systems
New demo
 Decision logic
 Science
 Maths
 Scope
 Read the preprint
Embodied AI · Active inference · World models
Find the mug.
 Make the tea.
The first demonstration showed an agent using semantic priors and negative evidence
 to locate a hidden mug. The new Habitat-Sim task carries the same reasoning into
 multi-object search, hidden-state inference and an 18-action plan that ends with
 tea served at the dining table.
Watch the new demo
 See the original search demo
 Open the preprint
3
 objects reasoned about jointly
18
 dependent task actions
Visible
 beliefs, policies and hidden states
New embodied demonstration
 From search to structured action
The agent finds the mug, teabag and kettle, checks whether the kettle contains
 water, fills and boils it, pours, steeps and serves.
Habitat-Sim · ReplicaCAD · active inference
Watch the full reasoning trace →
New demonstration · July 2026
From uncertain search to making a cup of tea
The agent must locate three objects, reason about what is currently known,
 satisfy action dependencies and track state changes from an empty kettle to a
 served cup of tea.
Multi-object task · full decision trace
Your browser does not support embedded video.
 Open the MP4 instead.
The main view shows the agent in the task environment; the inset shows its
 first-person observation. The right-hand panels expose location beliefs,
 hidden-state confidence and the task graph while the lower panel shows the
 selected action and progress.
 Read the Technical Note.
Decision trace JSON
 Download video
00:00
 Evaluate the search space
 Candidate object–location pairs are ranked by probability, information gain, distance and task relevance.
00:12
 Opportunistic discovery
 The kettle is found while the current task frontier is still to locate the mug.
00:28
 Negative evidence
 Empty locations reduce their posterior probability and redirect the next inspection.
00:56
 Objects located
 The search phase resolves the mug, teabag and kettle before task execution proceeds.
01:20
 State-dependent actions
 The agent checks, fills and boils the kettle only when dependencies and belief preconditions are met.
01:39
 Pour, steep and serve
 Action effects update the hidden-state beliefs until the task goal is satisfied.
01
 Multi-object inference
Beliefs are maintained over the locations of the mug, teabag and kettle rather than a single target.
02
 Task relevance
The search policy can value an object that is useful downstream, even when another search node is currently active.
03
 Hidden object states
The model tracks whether water is present and hot, whether tea is brewed and whether it has been served.
04
 Dependent action sequence
Eighteen graph-linked actions connect locating and moving objects to filling, boiling, pouring, steeping and serving.
Decision-making logic
One model decides what to inspect and what to do next
Search and task execution are coupled. Evidence changes beliefs; beliefs change
 which actions are available and valuable; successful actions change the world
 state that the next decision is conditioned on.
1
 Rank object–site hypotheses
The policy compares candidate searches across all unresolved task-relevant
 objects, balancing current probability, expected information gain and travel cost.
2
 Use absence as evidence
When an object is not visible at an inspected site, probability mass is
 redistributed over the remaining hypotheses and the search order changes online.
3
 Respect dependencies
Actions become eligible only after their graph dependencies are complete.
 The teabag cannot be inserted before the mug is placed, and pouring waits for
 both hot water and the teabag.
4
 Update state beliefs
Inspecting, filling, boiling, pouring and steeping alter beliefs about hidden
 states. The task finishes only when the model is sufficiently confident that
 the tea has been brewed and served.
Search →
 Locate →
 Move objects →
 Inspect kettle →
 Fill & boil →
 Pour & steep →
 Serve
Foundational demonstration
Belief-guided search in a realistic 3D home
The original 32-second demo isolates the core inference loop: begin with a
 semantic prior, inspect useful locations, treat absence as evidence and replan
 until the cup is found.
Your browser does not support embedded video.
 Download the MP4 instead.
The video has no audio. All information is presented visually through the
 first-person environment, posterior belief bars, candidate policy scores and
 the final cup-detection cue.
Download video
00:00
 Semantic prior
 Kitchen 45%, dining table 30%, console 20%, side table 5%.
00:06
 First inspection
 The agent tests the most plausible and informative location.
00:15
 Negative evidence
 Failure to find the cup redistributes belief over the remaining sites.
00:30
 Cup found
 Visual evidence confirms the console and collapses the posterior.
The scientific idea
A world model that can expose its reasoning
The central object is not a fixed action policy. It is a structured belief about
 hidden states of the world, together with a model of what each possible action
 is expected to reveal.
01
 World
A realistic ReplicaCAD apartment is rendered in Habitat-Sim. The agent receives
 egocentric observations and travels between collision-free inspection viewpoints
 on the navigation mesh.
02
 Belief
The model maintains categorical beliefs over the locations of multiple objects,
 together with confidence about task-relevant states such as whether the kettle
 contains water, whether the water is hot and whether the tea has brewed.
03
 Action
Candidate inspections are scored by travel distance, probability, expected
 information gain and task relevance. A dependency graph then exposes the next
 executable action once its prerequisites and belief preconditions are satisfied.
1
 Start with structured priors
 Objects and hidden states begin with explicit, inspectable probabilities.
→
2
 Evaluate candidate policies
 Which observation or action is useful, informative, relevant and reachable?
→
3
 Act and observe
 The agent navigates, inspects or manipulates and gathers new evidence.
→
4
 Revise state and replan
 Observations and action effects update beliefs, task eligibility and the next policy.
What is active inference here?
Semantic planning under uncertainty
The active inference layer selects semantic searches and task-level actions.
 Habitat-Sim supplies local navigation, while object interactions are implemented
 as explicit simulator primitives. Detection and state inspection remain idealised
 semantic sensors. This isolates belief updating, policy selection, dependency
 handling and state-conditioned planning before learned perception, grasping and
 lower-level active inference control are added.
Accessible maths
The search policy in three ideas
The location-search component uses deliberately transparent equations. The
 tea-making demo applies this logic across object–site pairs, then hands resolved
 objects to the stateful task graph.
1
 Update beliefs with evidence
\[
 q_{t+1}(L_j)
 =
 \frac{p(o_{t+1}\mid L_j)\,q_t(L_j)}
 {\sum_k p(o_{t+1}\mid L_k)\,q_t(L_k)}
 \]
\(L_j\) is a possible location for the object currently being evaluated.
 When an inspected site is empty, its likelihood is reduced while alternatives
 remain plausible. Probability mass therefore moves elsewhere rather than
 simply disappearing.
2
 Value information
\[
 \mathrm{IG}_i
 =
 H[q_t(L)]
 -
 \mathbb{E}_{o\mid \pi_i}
 \left[H\!\left(q_{t+1}(L\mid o,\pi_i)\right)\right]
 \]
Entropy \(H[q]=-\sum_j q(L_j)\log q(L_j)\) measures uncertainty. An inspection
 is informative when it is expected to make the posterior sharper, whether the
 mug is found or ruled out.
3
 Select the next inspection
\[
 G_i
 =
 0.20\,d_i
 -
 3.00\,q_t(L_i)
 -
 1.50\,\mathrm{IG}_i
 \]
\(d_i\) is the navigation distance to inspection site \(i\). The second term
 favours locations where the target object is currently likely. The third favours
 actions that reduce uncertainty. Lower \(G_i\) is preferred. In the tea-making
 task, candidate object–site pairs are also weighted by their relevance to the
 remaining task graph.
In plain language:
 go somewhere plausible and informative, while accounting for the effort needed
 to get there.
How this relates to expected free energy
In the broader active inference formulation, policies are evaluated using
 expected free energy:
\[
 G(\pi)
 \approx
 \underbrace{\mathbb{E}[-\log p(o\mid C)]}_{\text{goal alignment}}
 +
 \underbrace{\mathbb{E}[H(p(o\mid s))]}_{\text{ambiguity}}
 -
 \underbrace{I(s;o\mid\pi)}_{\text{information gain}}
 \]
Both demonstrations use a compact, interpretable approximation at the
 semantic planning level. The tea-making extension evaluates searches across
 multiple task-relevant objects and then gates downstream actions through
 dependencies and probabilistic state preconditions. The decision remains visible
 rather than being hidden inside a learned policy network.
Why it matters
Reasoning continues beyond finding the object
A useful world model must decide what to look for, learn from what is absent,
 compose actions over time and keep track of how its own interventions change the
 world. The tea-making task makes that full loop visible.
Inspectability
 Beliefs, uncertainty and candidate actions remain visible throughout.
Adaptive replanning
 Search order and task execution change online as evidence changes the posterior.
Task composition
 Dependencies connect object search to a coherent sequence of goal-directed actions.
State tracking
 The model represents how inspection and manipulation change task-relevant hidden states.
Current scope
A controlled proof of concept, with a clear route forward
These demonstrations are designed to make the inference and task loop legible.
 They show meaningful progress from search to stateful action, without claiming
 general household autonomy.
Current
 Hand-specified semantic priors
Initial object-location and state probabilities encode ordinary task knowledge.
Current
 Idealised perception and inspection
Semantic simulator channels provide object detections and observations of selected hidden states.
Current
 Task graph and manipulation primitives
Active inference selects semantic searches and task actions while Habitat handles navigation and simulator-level interactions.
Next
 Learned perception and state estimation
Replace idealised channels with vision models that return graded, fallible object and state evidence.
Next
 Unseen homes and richer tasks
Test transfer across layouts, object categories, longer horizons and learned semantic relationships.
Next
 Learned grasping and lower-level inference
Replace scripted interaction primitives with grasping, locomotion and continuous active inference control.
Read the paper
Active Inference World Models: From Embodied Control to General-Purpose Adaptive Intelligence
The preprint develops the wider argument for world models grounded in active
 inference, linking embodied control, semantic priors, adaptive decision-making
 and general-purpose intelligence.
Read on Zenodo
 Copy citation
Shaw, A. D. & Berndt, L. C. S. (2026). Active Inference World Models:
 From Embodied Control to General-Purpose Adaptive Intelligence . Zenodo.
Alexander D. Shaw
 ·
 AI & Technical CV
 ·
 Consulting & collaboration
Explore further
Related CPNS resources
Interactive World Model Lab
Active inference agents and robotics
Polyphonic active inference drone
Active inference explained
CPNS Lab
 Mechanistic modelling for mind, brain and intelligent systems.
Home
 Preprint
 Contact

## 导航

- 项目页：[[10-项目/cpnslab.com_3b34105c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
