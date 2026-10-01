---
type: "corpus"
item_id: "f4b109d42c6a7e1d"
title: "Show HN: Halv cut AI agent cost by 57.1% using Jev"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49913080"
project_url: "https://halv.ai/blog/halv-swe-rebench-astra-42-pairs"
author: "villaspedro"
published_at: "2026-09-30T19:16:09Z"
captured_at: "2026-10-01T09:41:49+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-01"
pub_day: "2026-09-30"
tags:
  - 语料
  - hn_show
  - author_villaspedro
  - story_49913080
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Halv cut AI agent cost by 57.1% using Jev

> [!info] 一句话导读
> Skip to content ½ Halv THE APP

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49913080>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：villaspedro　|　发布：2026-09-30T19:16:09Z
> 项目链接：<https://halv.ai/blog/halv-swe-rebench-astra-42-pairs>
> 采集：2026-10-01T09:41:49+08:00　|　id：`f4b109d42c6a7e1d`

## 正文

Skip to content ½ Halv THE APP
 HOW IT WORKS
 PROOF
 PRICING
 FAQ
 BLOG
 Choose language English Português (Brasil) Español Français Deutsch Italiano Nederlands 日本語 简体中文 繁體中文 한국어 ▾ Download macOS
THE APP
 HOW IT WORKS
 PROOF
 PRICING
 FAQ
 BLOG
 Download macOS
Halv /
 Blog /
 Inside Halv’s 57.1% cost reduction: the SWE-rebench data
 Technical report · Astra × JEV × SWE-rebench
 Inside Halv’s 57.1% cost reduction: the SWE-rebench data
 Across 14 tasks and three repetitions each, Halv and vanilla Codex both passed 25 of 42 runs. Halv recorded $144.67 in model cost versus $337.50.
 September 30, 2026 · Pedro Villaca
 Quick answer
 Halv recorded 57.1% lower model cost across 42 paired repetitions, with 25 verifier passes per arm. The strongest task result was ArcadeDB-4455: 81.7% lower cost and 3/3 passes on both sides. This interim workflow comparison used more tokens with Halv. Infrastructure-invalid attempts and a rolled-back policy experiment are excluded.
 Download Halv →
 −57.1% Recorded model cost
 25 / 42 Verifier passes in each arm
 14 × 3 Tasks × repetitions
 −81.7% ArcadeDB-4455 cost · both 3/3
 On this page
 The result at a glance
 The strongest results
 What changed in the workflow
 Where Halv’s recorded cost went
 Every task, including the regressions
 Selection, exclusions, and the checkpoint
 How to inspect the evidence
 What this result supports
 Frequently asked questions
 For the main results in plain language, read the short version .
Halv recorded less than half the model cost while matching vanilla’s aggregate verifier pass count.
Across 14 repository tasks, we ran three paired repetitions per task.
Each pair compared vanilla Codex with a Halv workflow that combined model routing and context tools.
Both arms passed 25 of 42 runs .
Halv recorded $144.67 , compared with $337.50 for vanilla.
That is 57.1% lower recorded model cost , including all coordinator and worker sessions in the selected runs.
This is an interim checkpoint from our own benchmark campaign.
It is a workflow comparison with different worker models, not a controlled test of one component.
The result at a glance
Metric
 Vanilla Codex
 Codex + Halv
Verifier passes
 25/42
 25/42
Pass rate
 59.5%
 59.5%
Recorded model cost
 $337.50
 $144.67
Cost per verifier pass
 $13.50
 $5.79
Total input + output tokens
 48,755,656
 170,114,775
Distinct tasks
 14
 14
Repetitions per task
 3
 3
We calculate savings from unrounded costs:
1 − ($144.666190 / $337.501056) = 57.1361%
 The numerator includes selected runs that failed verification.
The denominator uses the same accounting boundary for vanilla.
Neither arm gets to remove a valid run because its patch failed.
Equal aggregate pass counts do not establish equal quality on every task.
They also do not turn 42 repetitions into 42 independent repository tasks.
Available now
 Run your workflow with JEV.
JEV selects agents for your tasks. It is included in your Halv subscription, with no separate routing fee.
Download Halv →
The strongest results
ArcadeDB-4455: 81.7% lower cost, with 3/3 passes in both arms.
Vanilla recorded $81.85 across its three runs.
Halv recorded $14.97 and passed all three verifiers.
This is the strongest task result that combines lower cost with the same pass count.
HugeGraph-3037: 67.1% lower cost, with 3/3 Halv passes versus 2/3 vanilla passes.
Halv recorded $12.21, compared with $37.05 for vanilla.
ArcadeDB-4411: 46.1% lower cost, with 3/3 passes in both arms.
Halv recorded $7.45, compared with $13.80 for vanilla.
These examples show where the workflow worked well.
The full table also shows where it cost more or produced fewer passes.
What changed in the workflow
Both arms used Codex 0.155.1 , an Astra medium coordinator, and the default service tier.
Each pair used the same task and repository verifier.
Vanilla asked Astra to complete the task alone.
Halv used the experimental investigate-l1-l2-v1 hierarchy:
Astra assigns an investigation to Luna 6 with medium reasoning.
The investigation informs the task brief and difficulty assessment.
JEV selects the L1 worker model and reasoning effort.
L1 can assign bounded work to a cheaper L2 worker when useful.
Astra reviews and integrates the result.
Every selected worker used the Codex lane.
The recorded routes selected Sol 6 with medium or xhigh reasoning, and Luna 6 with high reasoning.
The separate investigation stage used Luna 6 medium.
L2 work appeared in 4 of the 42 Halv runs .
Most runs used the investigation and L1 stages without adding L2.
The hierarchy permits delegation; it does not require every task to create another layer.
Halv also enabled Crux 0.10.3 , RTK , and Headroom .
Crux supplied code navigation, RTK filtered command output, and Headroom processed model context.
The external benchmark monitor supplied status without asking Astra to generate routine progress updates.
These components changed together.
This experiment cannot isolate how much of the result came from JEV, model selection, context tools, or coordination policy.
Where Halv’s recorded cost went
JEV agent selection is included in the Halv subscription price.
Halv users pay no separate fee for JEV to select their agents.
The table below measures model execution costs; it does not allocate the Halv subscription fee across benchmark runs.
The selected Halv runs include all recorded roles:
Role
 Recorded cost
 Share of Halv cost
Astra coordinator
 $64.50
 44.6%
Investigation
 $1.06
 0.7%
L1 workers
 $76.03
 52.6%
L2 workers
 $3.07
 2.1%
Total
 $144.67
 100%
The coordinator still accounted for a substantial share.
The cheap investigation stage did not make coordination free.
Measuring the complete workflow prevents a short coordinator conversation from hiding expensive worker activity.
Halv used 3.49 times as many total tokens as vanilla.
Lower recorded cost came with a different mix of model usage and caching.
The result supports a cost claim for this workflow, not a claim that this hierarchy saves tokens.
Every task, including the regressions
Each row sums three repetitions per arm.
Positive savings mean Halv recorded lower cost.
Negative savings mean Halv recorded higher cost.
Costs in this table are rounded to cents; aggregate calculations use unrounded values.
Task
 Vanilla passes
 Halv passes
 Vanilla cost
 Halv cost
 Halv savings
ArcadeDB-4281
 2/3
 3/3
 $11.26
 $7.50
 33.4%
ArcadeDB-4411
 3/3
 3/3
 $13.80
 $7.45
 46.1%
ArcadeDB-4455
 3/3
 3/3
 $81.85
 $14.97
 81.7%
gentle-ai-595
 3/3
 3/3
 $8.13
 $7.19
 11.6%
nanobot-4048
 3/3
 3/3
 $4.70
 $5.71
 −21.4%
nanobot-4129
 3/3
 3/3
 $4.40
 $5.48
 −24.7%
nanobot-4274
 0/3
 0/3
 $11.17
 $14.56
 −30.4%
lossless-claw-814
 0/3
 0/3
 $20.66
 $11.97
 42.1%
Perry-3982
 3/3
 1/3
 $71.20
 $17.90
 74.9%
codex-lb-744
 3/3
 3/3
 $11.46
 $10.77
 6.0%
agno-8148
 0/3
 0/3
 $32.24
 $8.85
 72.6%
dubbo-go-3357
 0/3
 0/3
 $7.60
 $9.84
 −29.4%
hugegraph-3037
 2/3
 3/3
 $37.05
 $12.21
 67.1%
pulsar-25793
 0/3
 0/3
 $21.99
 $10.27
 53.3%
Total
 25/42
 25/42
 $337.50
 $144.67
 57.1%
Halv cost more on four of 14 tasks : the three nanobot tasks and dubbo-go-3357.
Those rows show that routing overhead can outweigh the cheaper worker mix.
The measurements alone do not identify the cause of each regression.
Perry-3982 deserves separate attention.
Halv recorded 74.9% lower cost, but passed only one repetition while vanilla passed all three.
That is a correctness regression, not an unqualified success.
The two additional Halv passes on ArcadeDB-4281 and HugeGraph-3037 offset the two missing Perry passes.
Several tasks failed in both arms.
Spending less on a failed task still does not complete that task.
Selection, exclusions, and the checkpoint
The campaign plan contains 111 tasks .
This report covers its first 14 tasks , with three repetitions per task, in fixed plan order.
The runner alternated Halv and vanilla within each repetition.
The campaign paused after Pulsar-25793 at the user’s request on September 30, 2026, at 17:42 UTC .
We did not select these 14 tasks by sorting their savings.
However, this was a discretionary interim stop, not a preregistered final endpoint.
The selector takes the first valid run for each task, arm, and repetition.
It requires complete usage, a valid verifier reward, and the required runtime checks.
Infrastructure-invalid runs can be retried.
A valid reward of zero remains in the comparison.
Operational repairs occurred during the campaign.
They included indexing launcher repairs and a Gradle stack adjustment before the Pulsar retries.
We also tried a native-completion instruction change, then restored the original waiting policy at the user’s request.
The ten recorded runs from that policy experiment were discarded before continuation.
The headline excludes:
13 infrastructure-invalid attempts in the retained results log, with $25.53 in known cost and nine unpriced attempts ;
10 recorded runs from the rolled-back policy experiment, with $40.79 in known cost ;
diagnostics and interrupted work, including an unmeasured cancelled attempt.
These exclusions matter.
The $144.67 versus $337.50 comparison is selected valid-run cost , not the entire campaign bill.
The attempt ledger preserves the excluded records and unknown costs.
How to inspect the evidence
The evidence browser links every task repetition to both run summaries.
Each summary includes the recorded verifier reward, usage by session, model configuration, cost, and source fingerprint.
Halv summaries also include routing decisions and cost by role.
The public export omits credentials, local paths, prompts, and model transcripts.
It contains sanitized summaries, not a complete transcript archive.
Source hashes identify the private source snapshot without publishing those private files.
Download the evidence archive , extract it, and run:
node verify-selected-pairs.mjs
 The script checks file hashes, unique pairs, session totals, recorded rewards, task totals, and aggregate arithmetic.
It does not rerun repository tests or independently authenticate provider billing.
The machine-readable results contain the full configuration summary and all 42 pairs.
The checksum manifest covers each published evidence file.
What this result supports
This checkpoint supports a specific claim: the Halv workflow recorded 57.1% lower model cost with the same aggregate number of verifier passes .
It does not establish statistical equivalence, universal savings, or Claude Code performance.
Three repetitions per task do not establish a stable estimate for every repository.
Recorded costs are token-based model estimates, not invoices.
They include cached input accounting and every recorded coordinator and worker session in the selected runs.
They exclude the Halv subscription, hosting, indexing compute, developer time, and unmeasured operational work.
A fixed subscription price does not fall when this metric falls.
Our earlier 20-pair report remains available with its original evidence.
It used a different model configuration and task sample.
Comparing the two headline percentages does not measure improvement between Halv versions.
For this checkpoint, the useful result is already concrete.
Halv spent $192.83 less in recorded model cost across the selected runs and matched vanilla’s 25 verifier passes .
Frequently asked questions
 What does the 57.1% savings measure?
 It compares recorded model cost across 84 selected runs: 42 Halv runs and 42 vanilla runs. Costs include coordinator sessions, worker sessions, and valid runs that failed verification. They exclude infrastructure-invalid attempts and the rolled-back policy experiment.
Did Halv solve more tasks?
 Both arms passed 25 of 42 runs. They did not solve the same set of repetitions. Halv gained passes on ArcadeDB-4281 and HugeGraph-3037, but lost two Perry passes.
Did Halv use fewer tokens?
 No. Halv used 170,114,775 total tokens versus 48,755,656 for vanilla. The routed workflow recorded lower model cost while using 3.49 times as many tokens.
Did both arms use the same model?
 Both coordinators used Astra with medium reasoning. Vanilla worked alone. Halv added Luna and Sol workers with different reasoning efforts, plus Crux, RTK, and Headroom.
Does this reduce my subscription price by 57.1%?
 No. These are recorded token-based cost estimates for the selected benchmark runs. They are not invoices or a reduction in fixed subscription prices.
Keep reading
 September 30, 2026 Same pass count. 57.1% lower model cost.
 Halv and vanilla Codex each passed 25 of 42 benchmark runs. Halv recorded $144.67 in model cost versus $337.50. Here is the result in plain language.
 September 4, 2026 Halv used 51% fewer tokens per correct answer on SWE-rebench
 On 20 paired SWE-rebench tasks, Halv used fewer tokens, cost less, and solved more tasks than vanilla Codex under the same model and verifier.
 August 29, 2026 How to save tokens in ChatGPT: 13 ways to cut Codex credit usage
 Thirteen tested ways to cut token usage in ChatGPT and Codex: the credit rate card, model and effort choice, fast mode, caching, and AGENTS.md.
Run your workflow with JEV.
 JEV agent routing is available now and included in your Halv subscription, with no separate routing fee.
 Download Halv All platforms →

## 导航

- 项目页：[[10-项目/halv.ai_beee412b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
