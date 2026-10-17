---
type: "corpus"
item_id: "db1121b69bd82c72"
title: "Show HN: Brian2 Atlas, a Rust engine for distributed neural simulation"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50120752"
project_url: "https://next-brain.ai/brian2-atlas"
author: "rocklee"
published_at: "2026-10-16T16:42:53Z"
captured_at: "2026-10-17T13:35:15+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-10-17"
pub_day: "2026-10-16"
tags:
  - 语料
  - hn_show
  - author_rocklee
  - story_50120752
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Brian2 Atlas, a Rust engine for distributed neural simulation

> [!info] 一句话导读
> NEXT BRAIN Computational Neuroscience & NeuroAI How it works Brian2 Atlas Models Training Experiments Explore Compute Research Blog User center Brian2 Atlas

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50120752>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：rocklee　|　发布：2026-10-16T16:42:53Z
> 项目链接：<https://next-brain.ai/brian2-atlas>
> 采集：2026-10-17T13:35:15+08:00　|　id：`db1121b69bd82c72`

## 正文

NEXT BRAIN Computational Neuroscience & NeuroAI How it works Brian2 Atlas Models Training Experiments Explore Compute Research Blog User center Brian2 Atlas · Open-source engine
 From neural equations
to distributed execution.
 An open engine for neural simulation and native training, from local machines to distributed systems.
 Keep the Brian2 modelling interface. Bring supported models to CPU, GPU, browser and MPI runtimes through a shared execution architecture.
 Get started View on GitHub
 Read the preprint ↗ Slides · 22 -page overview ↗
Model to execution 01 → 04
 01 · Describe Brian2 model Equations · clocks · events
02 · Validate AtlasIR
 Typed state, schedules, effects
and random-stream identities
 Independent Rust validator
03 · Plan Execution plans Ordering · ownership · layout
CPU GPU Browser MPI
 04 · Execute Native training: forward + reverse plans
Architecture Research results Get started Try it Paper & resources The architecture
 Describe the model.
Make execution explicit.
AtlasIR connects the equations you write to how a runtime schedules work, stores state and exchanges events. It makes those choices available for inspection and validation.
 01 A familiar modelling interface
 Define neurons, synapses, clocks and monitors with Brian2. Atlas adds its own execution backends while retaining the upstream modelling frontend.
 02 A shared model contract
 Represent typed state, scheduling, effects and event identities explicitly. Validate the representation before applying execution-plan transformations.
 03 Simulation and native training
 Alongside simulation, a bounded training extension provides forward and reverse execution plans with surrogate spike gradients.
CPU Reference & AOT Run with the reference engine or compile a model-specialized native executable.
GPU Apple Metal & NVIDIA CUDA Execute supported models on Apple or NVIDIA GPUs with float32 numeric mode.
Browser WebAssembly Export a supported model bundle for execution in a browser worker.
Distributed MPI Partition supported networks across ranks, with explicit ownership and event exchange.
Choose a backend for the model features and hardware you need. The backend guide documents setup and support for each path.
 From the v2 preprint
 Measured on real workloads.
Three studies illustrate execution speed, preparation memory and distributed capacity. Each links to its methods and measurement scope.
 CPU execution 5.43 × Best-measured time ratio
 0.839 s for Rust at 16 threads versus 4.555 s for Brian2 C++ at 8 threads, on the same Linux host.
 Full-connectome simulation + recording. Reported medians; both backends constrained to 16 physical cores on one socket. Section 5.3 · Figure 4 Laptop capacity 298.9 M Synapses on a 16 GB laptop
 The PD14 workload completed 10 seconds of model time for 77,169 neurons on an Apple M3 laptop.
 Recording disabled. The compared C++ preparation exceeded its controlled memory budget; this is a capacity result. Section 5.3 · Resource test Distributed capacity 24.1 B Recurrent synapses across four nodes
 A 4.13-million-neuron multi-area model completed 100.5 seconds of model time using 32 MPI ranks.
 A documented capacity configuration, with its own source snapshot, output checks and resource records. Section 5.2 · Figure 3
 Read the story behind the results
 Get started · v0.1.0
 Your first Atlas simulation.
Install the tagged source release, select the reference CPU engine, and run a single neuron. Atlas runs on your own machine without a Next Brain account.
 1. Install the source release
 For a Unix-like shell, with Python 3.12+, Rust/rustup and a working C/C++ compiler available. The source install builds the native simulation and training executables.
 Installation commands Copy
 git clone --branch v0.1.0 https://github.com/RockLi/brian2-atlas.git
cd brian2-atlas
rustup toolchain install 1.98.1 --profile minimal
python -m venv .venv
. .venv/bin/activate
python -m pip install .
 Full installation guide
 2. Run a single neuron
 Save this as first_atlas.py and run python first_atlas.py in the activated environment. The example simulates 100 ms and reports nine spikes.
 Python example Copy
 import brian2 as b
import brian2_atlas
b.set_device("atlas", engine="reference")
group = b.NeuronGroup(
 1, "dv/dt = (1.5-v)/(10*ms) : 1",
 threshold="v>1", reset="v=0",
 method="euler", dt=0.1*b.ms,
)
spikes = b.SpikeMonitor(group)
b.Network(group, spikes).run(100*b.ms)
print(spikes.num_spikes) Expected output 9
Continue with Source examples ↗ GPU, browser & MPI guide ↗ AtlasIR specification ↗
 Atlas × Next Brain
 An open engine.
A place to explore it.
 Brian2 Atlas is the engine you can install and develop with. Next Brain brings supported Atlas models into an online workflow for exploration, simulation and training.
 How the platform works
 Browser simulation Explore an adaptive LIF population
 Inspect a compact model of threshold, reset and spike-frequency adaptation through the browser execution path.
Guided training workflow Train your first spiking network
 Follow a digit-recognition experiment through the platform's Atlas CPU training path. Running training requires an account and an available worker.
Open source · Open research
 Methods, code and evidence.
Start with the illustrated overview, read the full manuscript, or inspect the source. The reproduction materials preserve the versions and configurations behind the published experiments.
 Open-source engine
 Explore the code
 Simulation, distributed execution and native training. Start with the source installation guide and documented backend support.
 GitHub · brian2-atlas · v0.1.0 Preprint · v2
 Read the manuscript
 A Unified Intermediate Representation and Execution Architecture for Heterogeneous and Distributed Neural Simulation
 Zenodo · 44 pages · 10 October 2026 Research overview
 Start with the slides
 A visual introduction to the architecture, main results and research boundaries, with a shorter path into the manuscript.
 PDF · 22 slides · CC BY 4.0
 Manuscript and slides by Xinjun Li · Next Brain, licensed under CC BY 4.0 .
 Reproduce the work with the evidence repository , or contribute through GitHub issues .
Cite & build on the work
 Keep the source
with the result.
 Use this citation for the v2 manuscript. For software, use the repository's citation metadata and record the exact commit used. The repository also preserves the upstream Brian2 citation.
Manuscript BibTeX Copy
 @misc{li2026atlas,
 author = {Li, Xinjun},
 title = {A Unified Intermediate Representation and Execution Architecture for Heterogeneous and Distributed Neural Simulation},
 year = {2026},
 publisher = {Zenodo},
 doi = {10.5281/zenodo.23273257},
 note = {Preprint, version v2}
}
 A few useful details.
 How does Atlas relate to Brian2? Atlas retains Brian2's modelling interface, upstream history and attribution, and adds its own execution architecture. It is developed by Next Brain. The repository scope explains the relationship and licensing.
 What is open source, and under which licence? Original Atlas engine code uses Apache-2.0. Retained Brian2 code remains under CeCILL 2.1. The manuscript and slides use CC BY 4.0. See the licence scope for the combined checkout.
 Where should I start with GPU or distributed execution? Start with the CPU example, then follow the backend guide for your model and hardware. GPU paths require their platform toolchains; MPI requires an MPI installation and a supported model. Browser execution uses a separate bundle-export API.
 How can I contribute or reproduce a result? Use GitHub issues for questions, bugs and proposed changes. The preprint repository contains the historical experiments and reproduction materials tied to the paper's source versions.
 Develop in the open
 Bring your next model.
 Explore the source, reproduce an experiment, or help improve the engine.
Explore Brian2 Atlas NEXT BRAIN Computational Neuroscience & NeuroAI
 About Brian2 Atlas Research Blog GitHub Preprint Slides X @rockl2e [email protected] Privacy Cookie settings © Next Brain

## 关联链接

- https://github.com/RockLi/brian2-atlas.git

## 导航

- 项目页：[[10-项目/next-brain.ai_71d47adb]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
