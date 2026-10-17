---
type: "corpus"
item_id: "38a07a14f936d00b"
title: "Show HN: Axiom, a general-purpose model for causal discovery"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50104080"
project_url: "https://maxpagels.com/axiom"
author: "maxpagels"
published_at: "2026-10-15T14:20:31Z"
captured_at: "2026-10-16T09:35:18+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-16"
pub_day: "2026-10-15"
tags:
  - 语料
  - hn_show
  - author_maxpagels
  - story_50104080
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Axiom, a general-purpose model for causal discovery

> [!info] 一句话导读
> A general-purpose model for causal discovery. Give it a table of data, and it drafts a causal graph of what is likely to cause what.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50104080>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：maxpagels　|　发布：2026-10-15T14:20:31Z
> 项目链接：<https://maxpagels.com/axiom>
> 采集：2026-10-16T09:35:18+08:00　|　id：`38a07a14f936d00b`

## 正文

Max Pagels
 Axiom
 A general-purpose model for causal discovery. Give it a table of data, and it drafts a causal graph of what is likely to cause what.
 🤗 maxpagels/axiom-base
 Model on Hugging Face Model card Weights
 3.8M parameters · fp32 safetensors · 15 MB
Contents
 Introduction
 Causal graphs, briefly
 Why discovery is hard
 What to do with the output
 Running Axiom
 Using intervention data
 Limitations
 Benchmarks
Introduction
 Drafting a causal graph, a representation of what is thought to cause what, is often the first step in causal inference. This process is known as causal discovery .
 Discovery is usually done manually, through a blend of stakeholder interviews and domain expertise. Ideally, the result is a correct directed graph of the causal process of interest. In practice it will never be perfect, but even an imperfect graph is valuable. A partially correct graph still encodes a great deal of knowledge: which variables are plausibly related, which are almost certainly not, and the direction of influence for at least some relationships.
 Automated causal discovery aims to speed up this traditionally manual process by inferring such partial graphs directly from data. Axiom is an open general-purpose model built for this task.
Causal graphs, briefly
 A causal graph is a set of variables connected by arrows. An arrow from one variable to another means the first is a direct cause of the second: change it, and the second changes too, all else being equal. The absence of an arrow is just as informative, since it claims there is no direct influence.
Fig. 1 — A small causal graph. Arrows point from cause to effect. In the example above, every variable is a continuous measurement: temperature in degrees, irrigation in litres, evaporation and soil moisture in millimetres, crop yield in kilograms per hectare. Higher temperatures lead farmers to irrigate more and also increase evaporation. Irrigation adds water to the soil while evaporation removes it, and soil moisture in turn drives crop yield. Note what the graph does not say: irrigation has no direct effect on yield. Its influence flows entirely through soil moisture.
 Irrigation and evaporation will also be correlated in data, even though neither causes the other. Both share a common cause, temperature. Telling apart relationships like these is precisely what causal discovery tries to do.
Why discovery is hard
 Inferring causal direction from observational data alone can be impossible in principle. The same data can arise from entirely different causal structures. Take two variables, A and B. A world where A causes B and a world where B causes A can produce exactly the same joint distribution. With linear relationships and Gaussian noise, for instance, the two are indistinguishable no matter how many rows you collect.
 World 1 A → B
 A ~ N ( 0 , 1 )
 B = 0.8 A + ε
 ε ~ N ( 0 , 0.36 )
World 2 B → A
 B ~ N ( 0 , 1 )
 A = 0.8 B + ε
 ε ~ N ( 0 , 0.36 )
In both worlds A and B have mean 0, variance 1 and correlation 0.8, so they produce the same bivariate normal distribution. No amount of observational data can tell them apart. The basic idea behind Axiom is that, despite this, one can do much better than random guessing. Axiom is a general-purpose model with attention across both rows and columns, letting it reason jointly about individual samples and the relationships between variables. It is trained on synthetic data drawn from a wide range of causal mechanisms. Real-world processes are rarely the perfectly symmetric worst case, and they leave subtle asymmetries in their data.
What to do with the output
 The graph Axiom returns is not meant to be perfect. Think of it as a first draft: a starting point that is refined with domain knowledge. Go through it with the people who know the process best. Remove edges that are physically or logically impossible, add relationships you know exist, flip arrows that point the wrong way, and flag the ones nobody is sure about.
 Once the graph is good enough, there are several things you can do with it:
 Estimate causal effects
 The graph tells you which variables to adjust for, and which to leave alone, when estimating the effect of one variable on another. That way you avoid both confounding and bias from conditioning on the wrong variables (hint: I made Formative for this purpose).
Test your assumptions
 Every graph implies conditional independencies that can be checked against data. If the data contradicts one, part of the graph is likely wrong.
Prioritise experiments
 Edges that are uncertain or that matter a lot for a decision are natural candidates for targeted interventions. Their results can then be fed back into Axiom as intervention data.
Simulate what-if scenarios
 Fit a structural model on top of the graph to predict what happens when you change a variable, rather than merely observe it.
Running Axiom
 Install the package straight from the Hugging Face repository:
 bash pip install "git+https://huggingface.co/maxpagels/axiom-base"
 Then load the model and pass it a table. Axiom reads the whole dataset in a single forward pass. Missing values can be left as NaN .
 python from axiom import Axiom , discover
model = Axiom . from_pretrained ( "maxpagels/axiom-base" )
 g = discover (model, df) # pandas DataFrame or (n, d) array; NaN = missing
g . edges # [(cause, effect, probability), ...]
 g . edge_probs () # (d, d) matrix of P(i -> j)
 g . confounded # (d, d) 0/1 matrix: likely hidden common cause, no edge
 discover standardises each column the same way as during training, so pass your data as-is. Only use axiom.preprocess if you want to call the model directly.
 What comes back
 For every pair of variables, Axiom predicts probabilities over five classes, which are then decoded into an acyclic graph:
 none No direct causal edge.
 i → j / j → i A direct edge, with direction.
 undirected Linked, but the direction is not identifiable from the data.
 confounded No direct edge, but a hidden common cause.
Recommended use
 Rows 256 or more works best; usable from around 100, below which results get unreliable. Tables over 512 rows are split into random 512-row subsets whose predictions are averaged (8 by default, raise n_subsets to use more of a large table).
 Variables Trained on 3 to 25. On simulated data it held up to 100 with no loss in accuracy; beyond 25 on real data is untested. Memory grows quickly with the variable count: roughly 1 GB on CPU at 100 variables, 3 GB at 200.
 Interventions If any rows come from experiments, label all of them. Unlabelled experimental rows act like hidden causes and can produce wrong or reversed edges.
 Output Treat edges, and especially directions, as ranked hypotheses to check rather than a verdict.
Using intervention data
 If some rows come from experiments, where a variable was deliberately set rather than observed, tell Axiom which ones. Interventions break symmetry and can sharply improve direction accuracy.
 python # One entry per row: None = observational, otherwise the
 # column(s) that row's experiment targeted. An (n, d) bool mask also works.
 targets = [ None , "PKC" , [ "PKA" , "PIP3" ] , None , ...]
g = discover (model, df, interventions = targets)
 Label every experimental row. Rows that came from an experiment but are left unlabelled look like the work of a hidden cause, and can produce wrong or reversed edges.
Limitations
 Axiom is trained only on synthetic data. Real data that differs from that prior, such as cycles, time series, selection bias or truly discrete mechanisms, is out of distribution.
 Hidden-confounder detection is weak. Treat the confounded output as a hint.
 Directions on real data can come out reversed. The synthetic training data lets the model infer direction from which variable is more predictable from the others, and real systems often show the opposite pattern. A fix to the training data is planned.
 Causal discovery from observational data rests on assumptions. Validate important edges with domain knowledge or experiments.
Benchmarks
 Benchmark results are available on the Hugging Face model page .

## 关联链接

- https://huggingface.co/maxpagels/axiom-base

## 导航

- 项目页：[[10-项目/maxpagels.com_b59c9c08]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
