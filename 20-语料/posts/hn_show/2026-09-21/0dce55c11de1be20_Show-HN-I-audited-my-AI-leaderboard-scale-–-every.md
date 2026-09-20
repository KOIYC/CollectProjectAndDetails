---
type: "corpus"
item_id: "0dce55c11de1be20"
title: "Show HN: I audited my AI leaderboard scale – every score dropped 6-15 points"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49110215"
project_url: "https://agiranker.com/"
author: "baraklaniado"
published_at: "2026-07-30T14:04:18Z"
captured_at: "2026-09-21T03:11:17+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-30"
tags:
  - 语料
  - hn_show
  - author_baraklaniado
  - story_49110215
  - show_hn
metrics: {"points": 4, "comments": 3, "engagement_velocity": 4}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:83d"
---

# Show HN: I audited my AI leaderboard scale – every score dropped 6-15 points

> [!info] 一句话导读
> AI BENCHMARK AGGREGATOR

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49110215>
> 指标：点赞=4 · 评论=3 · engagement_velocity=4
> 作者：baraklaniado　|　发布：2026-07-30T14:04:18Z
> 项目链接：<https://agiranker.com/>
> 采集：2026-09-21T03:11:17+08:00　|　id：`0dce55c11de1be20`

## 正文

AGI RANKER
AI BENCHMARK AGGREGATOR
Leaderboard
 Explorer
 Methodology
 Corrections
 Heatmap
 Insights
 Version History
v2.9.1
Contribute Data
Leaderboard
 Explorer
 Methodology
 Corrections
 Heatmap
 Insights
 Version History
SINCE MAY 2026
Aggregating from major public AI benchmarks
ONE SCORE.
INFINITE CLARITY.
AGI Ranker measures how close each frontier AI is to AGI. One transparent score (0-100) per model, distilled from 10 public benchmarks. Score 100 marks the AGI threshold.
Independent verification preferred over lab self-reports. Scores we can't verify are flagged, not invented. Every correction is logged publicly.
Our definition of AGI
View Live Leaderboard
Launch Interactive Explorer
TOP MODEL
-
-
FRONTIER MODELS
-
AGI Score ≥ 65
BENCHMARKS AGGREGATED
-
Live benchmarks (TBA excluded)
Distance to AGI
-
pts
Top model's gap to AGI Score = 100
Top Model Breakdown
-
Thinking
44% weight
-
Fluid Reasoning + World Knowledge
Doing
43% weight
-
Agency (tools, planning, coding) + Visual Reasoning
Communicating
13% weight
-
Language Production + Visual Reasoning output
REAL-TIME RANKINGS
The AGI Ranker Leaderboard
100 = AGI
AGI
 Coding
Reasoning
 Knowledge
Tool Use
 Value
Custom
Heads up: Reasoning has only 2 benchmarks (ARC-AGI-2 and AIME 2025) and most models have only one measured. Single-cell rankings here can be misleading. More reasoning benchmarks (FrontierMath, SimpleBench) are queued for activation once roster coverage is broad enough.
Score: High to Low
 Score: Low to High
 Value: Best Score / $
 Name A-Z
Columns
Optional columns
Arena Elo - LMSYS user-pref
Coverage - benchmarks · components
API Price - $/M tokens, in / out
Custom weights active. These are not the canonical AGI Score.
 Custom weights active. Scores below reflect your slider settings - not the canonical AGI Score (whose 100 = AGI anchor only holds at default weights).
More
Reset to default
Show contested models
Show incomplete models
Value: capability per dollar
Overall
 Coding
Reasoning
 Knowledge
 Tool Use
Sort
Capability
 Value for money
🏆 Top - highest capability
 💎 Value - most extra capability per dollar
 🪙 Budget - cheapest to run
Capability is the same score as that area's own tab. Cost is an estimate from list prices, not a measured per-task bill.
 Capability is the published score for the selected area - identical to that area's tab (Overall = the AGI Score). The 💎 best-value pick is the model giving the most extra capability per dollar; see the methodology for exactly how value for money is derived. Cost is an estimate from published list prices across four token classes at a typical mix for that workload; the coding mix is measured from real agentic sessions. Not a measured per-task bill.
More
Value frontier
The same models plotted by capability and cost. The dashed line links models where nothing else is both higher-scoring and cheaper.
#
 Model
 AGI AGI Score
 Arena Elo
 Coverage
 Price $/M tok
 · Details
Scores normalized to a per-benchmark ceiling: measured human parity where a human study exists, benchmark maximum where none does (see Methodology).
 See full methodology →
Weight customization is paused in the Value view - weights don't change the price-performance scatter. Switch to AGI or a specialty tab to customize the formula.
CUSTOMIZE THE FORMULA
Interactive Model Explorer
Adjust domain weights and instantly see how the AGI Score changes. Transparency at its core.
Balanced
 Reasoning Heavy
 Agency Focus
 Knowledge Deep
Total: 100 %
 - normalized to 100% before scoring
RESET TO DEFAULT
Recompute Scores
SELECT MODELS TO COMPARE
 (max 4)
Domain Proficiency Radar
0 models selected
TRANSPARENT METHODOLOGY
How the AGI Score is Calculated
A transparent, reproducible composite index designed for maximum signal and minimum noise.
1
Data Ingestion & Curation
We aggregate scores from 10 headline benchmarks: GPQA Diamond, HLE, ARC-AGI-2, AIME 2025, SWE-bench Verified, Terminal-Bench 2.1, τ³-Banking, LiveBench, LiveBench Agentic Coding, and MMMU-Pro. We also publish DeepSWE v1.1 for the Coding specialty only. Each cell is cited so any score can be traced back to its origin. We do not run benchmarks ourselves - we aggregate what others have already published. Source quality is tiered: independent benchmark leaderboards (Tier 1) count fully at 1.00×; third-party evaluators with provider involvement (Tier 2) at 0.85×; self-reports from labs with verified track records (Tier 3) at 0.75×; non-verified labs and commentary content (Tier 4) are excluded from scoring entirely.
Note on the AA Intelligence Index (removed June 2026): We previously carried Artificial Analysis's composite Intelligence Index as a Language signal. We have removed it from the AGI Score. Their v4.1 revision turned it into an explicitly agentic composite (GDPval-AA, Terminal-Bench 2.1, τ³-Banking, SciCode, HLE, GPQA and more) that re-bundles benchmarks we already score directly - keeping it would double-count those signals across components and mislabel agency as language. Language now rests on LiveBench; a dedicated language/writing benchmark is on our roadmap to restore a second independent source. We continue to track the AA Index as an external reference.
2
Normalization to Best-Human
Revised in v2.0.0: each raw benchmark score is rescaled by a ceiling. Where a published human study exists under a protocol comparable to the models’, that measurement is the ceiling and 100 means human parity . Where none exists, the ceiling is the benchmark maximum and 100 means a perfect score , with no human claim attached. Today exactly one scored benchmark carries a measured human ceiling, GPQA Diamond at 0.81, and the other nine are scored against the benchmark maximum, so the AGI Score is currently a mixed scale rather than a pure human comparison. Three further benchmarks passed the same ceiling audit and none of them is on the board: OSWorld (0.72) was retired in v2.0.0, and FrontierMath (0.35) and SimpleBench (0.837) have no harvested coverage yet. We previously described every ceiling as best-human; that was not accurate for most of them, and correcting it is the main reason scores moved in v2.0.0. AGI Score = 100 remains our marker for the genesis of AGI , per our working definition in full: “AGI is an artificial intelligence that surpasses the best human on every purely brain-based intellectual task with no involvement of a physical body.” Scores climb past 100 as the AI grows from genesis into super-human (ASI-direction) territory; we preserve those scores rather than clamping, so the index stays informative in an ASI / post-AGI world.
3
5-Component Aggregation
Benchmarks roll up into 5 cognitive components AGI must master: Agency (35%), Fluid Reasoning (29%), World Knowledge (15%), Visual Reasoning (11%), Language Production (10%). Within each component, the score is the weighted mean of all the model's contributing benchmarks; each benchmark's effective weight is sub_weight × source_tier_multiplier . Sub-weights are fixed per benchmark and reflect each benchmark's relative importance within a component (e.g., ARC-AGI-2 carries 25% of Reasoning, GPQA carries 20%). The saturation rule kicks in dynamically: if the IQR of normalized scores among the top-10 ranked models on a benchmark drops below 5 percentage points, that benchmark's sub-weight is halved and the freed weight is redistributed to non-saturated benchmarks in the same component - keeping the component score responsive to whichever benchmarks still discriminate frontier models. Source tiering applies a multiplier per cell based on source independence (T1 1.00×, T2 0.85×, T3-Verified-Lab 0.75×; T4 excluded from scoring entirely). Component weights are user-adjustable in the Explorer below.
AGI Score = Σ (wᵢ × Cᵢ) / Σ wᵢ
where Cᵢ = component score (shrunk toward median if thin-coverage), wᵢ = component weight
4
Sparse-Data Handling (Asymmetric Pull-Down + Renormalize)
5
Specialty Rankings & Custom View
Above the leaderboard, tabs switch the ranking between the canonical AGI Score and task-focused views. Each specialty (currently Coding and Knowledge) re-ranks models using only the benchmarks that test that capability. An official Specialty score and rank require every active benchmark in that Specialty's battery: Coding uses DeepSWE v1.1, Terminal-Bench 2.1, and LiveBench Agentic Coding at 40%, 35%, and 25%, while Knowledge uses its three active knowledge benchmarks. Incomplete evidence remains visible only through the Specialty toggle, with measured cells and missing benchmark names but no partial total. Missing results are not treated as zero, estimated, or renormalized into an official Specialty score. Specialties are shown on a separate 0 to 10 index, not on the AGI scale , because they are a different kind of claim: 10 means a perfect score on every benchmark in that set, and it is not a statement about human performance. Most of these benchmarks have no published human study, so there is no human bar to measure distance to. A specialty index is never AGI - AGI requires the full battery, which only the canonical AGI Score measures. The Custom tab (visible when you adjust the Explorer's weight sliders) shows the AGI Score under your settings; the AGI tab always reverts to default weights, keeping the canonical view unambiguous.
Calibration Constants & Operational Discipline
reproducibility addendum
Full reproducibility requires three things beyond the formula: the exact numeric thresholds we apply, the within-set sub-weights used in specialty views, and the discipline we hold against common mis-attribution patterns. All disclosed below.
Constants unchanged since v1.4, reviewed and re-confirmed for v2.0.0. These are operational values, not permanent invariants. Future methodology versions may revise specific constants as the methodology evolves and as benchmark coverage matures; substantive changes will be noted in the version history.
Numeric thresholds
Constant
 Value
 Used in
Asymmetric shrinkage coverage threshold (main AGI Score & specialties with 3+ benchmarks)
 60%
 Step 4
Asymmetric shrinkage coverage threshold (specialties with 2 benchmarks, e.g. Reasoning)
 85%
 Step 5
Saturation IQR threshold (top-10 ranked models)
 5 pp
 Step 4
Coverage floor - Fluid Reasoning & Agency (core)
 40%
 Step 4
Coverage floor - Knowledge / Visual Reasoning / Language
 30%
 Step 4
Max thin components allowed in the RANKED tier
 1
 Step 4
Eval-date grace window vs. model release
 30 days
 below
Specialty sub-weight splits
Within each specialty tab, only the relevant benchmarks contribute, with fixed within-set sub-weights. Official Specialty rank requires complete coverage of the active benchmark battery. Models with incomplete evidence remain discoverable through the local "Show incomplete models" control, but they receive no aggregate Specialty score or ordinal rank. Missing results stay missing: they are not zero-filled, estimated, or renormalized into an official Specialty score. Reasoning remains withdrawn until its active battery has broad coverage.
Note on Coding methodology (v2.9.0): Coding uses DeepSWE v1.1, Terminal-Bench 2.1, and LiveBench Agentic Coding at 40%, 35%, and 25%. DeepSWE v1.1 is DataCurve's repository-level software engineering evaluation on the fixed mini-swe-agent protocol. All three active Coding benchmarks are required for an official rank. Incomplete models can be shown separately with their measured cells and missing benchmark names, but no partial Coding total is published. Missing results are not treated as zero or estimated. SWE-bench Verified remains in the headline instrument but is not a Coding specialty leg.
Contamination note for SWE-bench Verified: Public-test-set SWE-bench scores can be inflated by training-data leakage. Private-test-set evaluators (e.g., vals.ai) tend to report 5-15pp lower numbers than public-leaderboard aggregators for the same model. We prefer T1 private-test sources where available; see the Corrections Log for the DeepSeek V4 Pro GPQA correction (0.901 self-report -> 0.729 independent T2) as a concrete example of the contamination correction in action.
Pre-release builds: preview, beta and release-candidate models are ranked normally and flagged . They meet the same evidence requirements as any other entry and are not given easier treatment. Holding them off the board would mean omitting models people are already using, and parking them in Provisional would misuse a tier that means thin evidence rather than unsettled product . What does deserve saying is that the weights behind a preview can change before general availability, so the score describes the build that was measured, not a finished product. Those entries carry a Pre-release tag. If a lab ships a materially different build under the same name, we treat that as a new model rather than silently updating the old row.
Source-choice sensitivity, GPQA Diamond and MMMU-Pro: both moved from Artificial Analysis to vals.ai on 2026-07-26, to break a single-evaluator dependency: Artificial Analysis had been supplying 97% of Knowledge and 100% of Visual Reasoning. GPQA Diamond remains on vals.ai. MMMU-Pro returned to Artificial Analysis on 2026-09-17 as a whole-column evaluator migration, not a per-model exception. As with Terminal-Bench we measured the gap before switching rather than after. On GPQA Diamond the two boards agree closely, with a −0.30pp offset and 1.38pp scatter across all 20 models, and vals additionally publishes a standard error per row. On MMMU-Pro , as of 2026-09-17 the active evaluator is Artificial Analysis. AGI Ranker uses Artificial Analysis' direct model evaluations as the canonical active source for MMMU-Pro. Earlier vals.ai MMMU-Pro observations are retained historically but no longer contribute to active scoring. If Artificial Analysis has no row for a model, MMMU-Pro stays missing. We do not fall back to another evaluator to preserve coverage. Artificial Analysis evaluates 1,730 ten-option questions at pass@1. The public MMMU-Pro paper describes 3,460 source-format items; that is the published dataset size, not the number AA evaluates. Evaluator mixing is not allowed to masquerade as capability, but as of 2026-08-05 it is priced rather than banned outright. When the canonical evaluator does not list a model, a column whose measured cross-evaluator scatter is at most 2pp may admit a fallback cell : the shadow evaluator’s value converted by the column’s measured offset, carrying a widened interval (±5.61pp on GPQA Diamond), permanently labelled on the cell, and automatically replaced by the canonical value the day it publishes, even when the canonical value is less flattering. MMMU-Pro no longer uses that fallback: missing Artificial Analysis coverage remains missing. Terminal-Bench 2.1, at 4.54pp scatter, does not qualify and stays single-evaluator. Uncorrected mixing — taking vals for eleven models and Artificial Analysis for the twelfth as if the numbers were interchangeable — remains ruled out for exactly the original reason: it would put two measurement stacks in one column and call the difference capability.
Source-choice sensitivity, Terminal-Bench 2.1: we report this separately rather than folding it into the uncertainty band, because it is a different kind of doubt. Terminal-Bench 2.1 is published by two independent evaluators, and they disagree systematically: across the 19 models present on both boards, vals.ai scores 7.77 points lower on average , and lower on 18 of the 19. Matching the declared effort level does not close it; Claude Opus 4.8 is max-against-max and still 12.7 points apart. We source from vals.ai, so our Terminal-Bench column sits about 7.8 points below where it would sit had we chosen the other board. What that is worth on the AGI Score: 0.71 points on average, 1.01 at most , because Terminal-Bench is 25% of Agency and Agency is 35% of the score. Had we chosen the other evaluator, only 2 of 20 models would change rank, and those two are 0.01 apart in any case. The published interval already spans roughly ±9.5 points, so this sits comfortably inside it; folding it in would count the same doubt twice. The remaining per-model disagreement after removing that systematic gap, 4.54 points, is inside the interval, where it belongs.
Harness disclosure for Terminal-Bench 2.1: Agentic-benchmark scores depend on the scaffold used to execute tasks. Every Terminal-Bench 2.1 cell comes from vals.ai using the Terminus 2 harness, pass@1 over 89 tasks. We deliberately use one evaluator rather than blending several, because two evaluators running the same 89 tasks do not agree: across the 19 models present on both the vals.ai and Artificial Analysis boards, vals.ai sits an average of 7.8 points lower , and it is lower on 18 of those 19. Matching the declared effort level does not close the gap. Blending the two would produce a number neither evaluator published, so we pick one, name it, and carry the disagreement into the uncertainty band instead. Native-agent rows (Claude Code, Codex CLI, Cursor CLI) are excluded entirely: they measure a product, not a model. Real users running each model with its own agentic tool may see different relative performance than these scores predict.
Specialty
 Benchmarks & within-set sub-weights
Coding
 DeepSWE v1.1 40 · Terminal-Bench 2.1 35 · LiveBench Agentic Coding 25
Reasoning
 ARC-AGI-2 70 · AIME 2025 30
Knowledge
 HLE 40 · GPQA Diamond 35 · MMMU-Pro 25
Tool Use
 withdrawn in v2.0.0 — OSWorld, BrowseComp and the two Tau-bench domains all left the board in the v2 evidence review: OSWorld had 2 clean cells out of 22, BrowseComp had no uniform browsing harness across models, and the Tau-bench retail and airline pair is superseded by τ³-Banking. That leaves a single clean non-coding tool-use benchmark, and a one-benchmark ranking is exactly what our two-benchmark minimum exists to prevent. The tab returns when a second one exists.
Value view: how value for money is derived
The Value tab pairs each model's published capability for the selected area (Overall = the AGI Score; otherwise the specialty score above - the exact same number that area's tab shows) with an estimated API cost, so capability can be weighed against price.
Estimated cost is a blended price per 1M tokens across four token classes — new context, cache writes, cache reads and output — at a typical mix for that workload, using each lab’s published list prices. The coding mix is measured from real agentic coding sessions across three vendors: about 97.6% of tokens are context read back out of cache and only 0.24% are output, which is why the cached-input rate dominates a coding bill. How broad that measurement is, precisely. It covers three vendors and three coding agents, but weighted by tokens the sample is about 87% a single agent, so read it as one workload measured carefully rather than an average across the field. Measured per agent, the share of new context ranges from about 1.8% to 7.1% — the agents differ more than the vendors do. We apply one mix to every model on purpose: the Coding score itself ranks models under a single standardised harness, and a per-vendor mix would price each model against a different workload. The other workloads are stated assumptions, not measurements. Where a lab publishes no cached-input rate we leave the model out of a cached workload rather than estimate one. Some providers also bill cache storage by the hour; because a blended per-token price has no time dimension, a model charging hourly storage for the caching mode we price is left out too, rather than have us invent how long a cache is held. No model is currently affected — every provider we verified charges nothing to hold a cache in the mode we price. Prices are the public rate you would actually pay today at the base context band. That includes published limited-time promotions, which are labelled on the card with the date they end — four models currently carry one. We absorb a promotion only when the provider publishes both the discounted rate and the period: a discount visible on one account but not quotable, or one with no stated end, stays at list and the reason is recorded against the model. Volume, subscription, batch and data-sharing tiers are still excluded. One thing the base band does not settle is how long a cache is kept: some providers charge more to hold a cache for an hour than for five minutes. That is a property of the workload rather than of the model, so we take the tier the workload actually needs — for coding, measured, that is the one-hour tier, because an agentic session holds its context far longer than five minutes and a five-minute cache would simply expire and be rewritten. For the workloads whose retention we have not measured we keep the base tier rather than guess one. Long-context surcharges, applied only where we could measure them. Most providers charge roughly double once a single prompt crosses a threshold — 200K tokens at xAI and Google, 272K at OpenAI, 512K at MiniMax — and the whole request is repriced when it does. What that costs depends on how often a workload crosses the line, which is a property of the coding agent, not of the model, so it has to be measured per vendor. We have measured it for Grok 4.5 (38.4%) and Grok 4.6 (44.6%) from real billing records, and their coding costs here include that uplift. Grok 4.3, MiniMax M3 and Gemini 3.1 Pro also have a surcharge and are shown without one , because we have no usage of them to measure and will not invent a figure — their true coding cost is higher than shown by an unknown amount. Anthropic, the Gemini Flash models and ChatGPT 5.5 Pro have no surcharge at all, which we verified rather than assumed. It is an estimate of typical cost, not a measured per-task bill.
Value for money is the extra capability a model delivers over the weakest option shown, per estimated dollar: (score − lowest score in view) / cost . We subtract that floor on purpose - a capability score has no true zero (a coding score of 0 is not "no value"), so raw score-per-dollar would over-reward the cheapest model no matter how capable it is. Subtracting the floor measures the extra capability you actually buy.
Each area surfaces three picks: Top (highest capability), Budget (cheapest to run), and Best value (the most extra capability per dollar). The ranking shows the picks rather than a raw value number, which is ambiguous to read in isolation.
Variant-attribution discipline
A cell enters scoring only when the source page's row label identifies the variant unambiguously. The lab's named max-tier configuration (OpenAI Pro , Anthropic thinking , etc.) must appear in the source label. Effort-knob suffixes are not variants.
Accept rows labeled e.g. "Claude Opus 4.7 (thinking)" or "GPT-5.5 Pro" .
Reject rows like "GPT-5.5 (xHigh)" , "GPT-5.5 (High)" , "DeepSeek V4 Pro (Max)" - these are base or default config with an effort knob, not the separately-priced Pro / thinking SKU.
Reject generic family rows where a single row on the source cannot distinguish base from Pro / thinking.
Eval-date sanity check
A cell whose eval_date predates the model's release_date by more than 30 days is rejected as a mis-attribution. The 30-day grace window covers pre-release lab evaluations; anything older almost certainly tested a preceding model that happens to share part of the name.
Two update clocks: evidence vs calibration
Adopted 2026-08-06: this board distinguishes updating the models being measured from recalibrating the measuring instrument. Evidence releases are frequent and run on a locked calibration: they may move only models that received new benchmark results, and the change is traceable to named cells. Calibration releases are scheduled, explicitly labelled, and are the only releases allowed to change benchmark discrimination weights (the saturation mechanism), which can move every model at once. The current calibration is pinned from 2026-08-05.
Why: benchmark reweighting is a legitimate response to benchmarks losing discriminating power at the frontier, but arriving unannounced inside a routine data update it reads as instability rather than method. Announced and labelled, it reads as what it is: a deliberate recalibration, explained in the changelog with before and after.
Active-roster governance
Adopted 2026-08-05: AGI Ranker tracks up to the best 4 models from each lab , including sideways SKUs (mid-ladder and specialized variants), not only flagship successions. New releases enter on arrival. When a lab’s count exceeds 4, the lowest-scoring model rotates off the board. A new entry that cannot yet be scored is protected from rotation until it becomes scoreable, or for 8 weeks, whichever comes first. Reasoning-effort settings never create separate rows.
The rule applies prospectively from its adoption date: models already on the board are grandfathered and rotate only under the rule’s normal operation going forward. The previous latest-two-generations rule governed the roster through v2.0.22 and remains documented in the version history. The specialist-slot principle carries over: a narrow branch earns its slot by qualifying for a leaderboard, not by name.
Version history
v2.9.1 · 2026-09-17 · Active MMMU-Pro evidence moved from vals.ai to Artificial Analysis to restore current frontier-model coverage. The benchmark role and weight are unchanged; every active MMMU-Pro cell now uses the same Artificial Analysis evaluator contract. Missing AA coverage stays missing rather than falling back to an older evaluator. GPT 6 Astra now receives MMMU-Pro coverage from that same canonical evaluator.
v2.9.0 · 2026-09-06 · GPT 6 Astra joins from independently verified benchmark evidence. Astra has a complete DeepSWE v1.1, Terminal-Bench 2.1 and LiveBench Agentic Coding battery, so it receives an official Coding rank. ARC-AGI-3 Standard remains research-only and the Provider Adapter harness is excluded. Existing formulas, weights and benchmark roles are unchanged.
v2.9.0 · 2026-09-05 · Coding benchmark battery modernised and Specialty coverage secured. SWE-bench Verified is replaced within Coding by DeepSWE v1.1, the DataCurve repository-level software engineering evaluation using the fixed mini-swe-agent protocol. Coding now uses DeepSWE / Terminal-Bench 2.1 / LiveBench Agentic Coding at 40 / 35 / 25, with all three active legs required for an official rank. Knowledge follows the same complete active-battery rule for its three active benchmarks. Incomplete Specialty evidence remains available through a separate toggle with no partial aggregate, while the AGI Score, headline Agency, headline coverage, and current headline behaviour are unchanged. DeepSWE remains Specialty-only and does not enter the headline. No Visual or ARC3 changes are included. This candidate does not activate headline v3 or retire SWE-bench Verified from the broader headline instrument.
v2.8.2 · 2026-09-03 · Gemini 3.8 Flash joins the board, one day after release. Google shipped it on 2 September. It has eight results: GPQA Diamond 94.44%, MMMU Pro 89.08%, SWE-bench Verified 80.00%, Terminal-Bench 2.1 81.27%, Humanity's Last Exam 47.8% (Artificial Analysis, high), T3-Banking 45.8% (Artificial Analysis, high), and on LiveBench an overall of 75.83% with 54.24% on agentic coding. It enters Ranked at 7th. Reasoning is still thin because ARC-AGI-2 has no row; one thin area is allowed. Muse Spark 1.3 joins in the same pass, also Provisional. It has five results: LiveBench overall 81.59%, agentic coding 64.09%, Humanity's Last Exam 47.5%, T3-Banking 47.2%, and GPQA Diamond 94.1% from Artificial Analysis, used because vals.ai has not listed this model (the same rule we already use when vals is silent on GPQA). Vals still has no SWE-bench or Terminal-Bench row, and MMMU-Pro is not filled from AA. That is enough to enter under v2 rules, and not enough to Rank. Highest public effort today is xhigh; Meta has withheld a max setting pending safety testing. Gemini 3.8 Flash takes official #7. Every official rank from Kimi K3 down shifts by one. No other model's score moved.
v2.8.1 · 2026-08-27 · A gap in the safeguard we shipped this morning, closed the same day. No price changed. v2.8.0 added a check that stops this site being rebuilt while any promotional price on it has expired. It compared calendar dates — and a promotion does not end on a date, it ends at a moment. The gap was eight hours wide. Z.AI’s discount on GLM 5.3 Flash ends at midnight on 9 September in Singapore, which is 4pm UTC. Between 4pm and midnight UTC that day the offer would already be over while the check still called it live — and the card would have read “Promo to 9 Sep” beside a price you could no longer get, which is worse than an unlabelled one because it looks verified. Expiry is now a moment, not a day. Where a provider states the hour and the timezone, as Z.AI does, we use exactly that. Where they state only a date, we do not guess which timezone they mean. OpenAI and Google both write “through” a date and name no zone. Rather than assume they bill in California, we treat the offer as ending at the earliest moment those words could mean anywhere on earth. For those three models the site will therefore stop rebuilding about fourteen hours before the discount most likely actually lapses. That is deliberate, and it is the cheaper mistake of the two: stopping early costs a rebuild that somebody clears by re-reading the provider’s page, which is the routine anyway. Stopping late costs you a price that cannot be bought, printed under a label saying we checked. We would rather be early and certain than punctual and guessing.
v2.8.0 · 2026-08-27 · CALIBRATION RELEASE We now show the price you would actually pay today, not the list price. Four models get cheaper, and each says when the offer ends. This changes the instrument, not the evidence. No model gained or lost a benchmark result, and no AGI Score, rank or tier moved — the Value tab does. What was wrong with the old rule. We priced every model at its standard list price and deliberately ignored promotions, to stop the board swinging with marketing campaigns. The effect was a page telling you ChatGPT 5.6 Sol costs $5 and $30 per million tokens while OpenAI’s own page showed $4 and $20, with nothing on the card to explain the gap. Limited promotions have stopped being occasional events in this market, so we absorb them and label them instead. What moved. ChatGPT 5.6 Sol $5/$30 → $4/$20, to 21 November. GLM 5.3 Flash halves, to 9 September. And the largest correction: Gemini 3.6 Flash and 3.7 Flash were priced at $1.50/$7.50, which is the rate that starts on 1 January 2027. Until then they cost $0.75/$3.75. We were publishing a price nobody pays yet, which made both models look twice as expensive to run as they actually are. What we refused to take, which matters more than what we took. A promotion counts only if the provider publishes both the discounted rate and the period. Grok 4.6 is billed to us at about a sixth of list, but xAI advertises no such offer — a rate on one account is not a price a reader can obtain, so Grok 4.6 stays at list. Qwen3.7-Max is openly labelled “limited-time 50% off” with neither the rate nor the end date published anywhere public. Thinking Machines’ discount is real but applies to training, and we price inference. Meta’s cheaper tier is bought by letting them train on your prompts, which we still exclude. MiniMax M3’s “permanent 50% off” has no end date, which makes it simply the price. Two models we could not check, recorded as unknown rather than clean. GPT-5.5 Pro has been missing from OpenAI’s pricing page for a week, and Alibaba shows promotions only to logged-in customers. Not knowing is a different thing from knowing there is nothing, and the card should not blur them. The obvious risk, and what we did about it. A promotional price is the first thing on this board that goes stale on a date with nobody touching it. GLM 5.3 Flash’s offer lapses on 9 September, and the day after, a label reading “Promo to 9 Sep” would make a wrong price look checked. So the site now refuses to rebuild at all while any promotion on it has expired. It fails shut, and the list price is kept beside every promotional one so it can be put back in a single edit. And a rounding fault this exposed. The price column showed two decimals, which was fine until promotional rates went below a cent: GLM 5.3 Flash’s $0.075 would have printed as $0.07, nearly 7% low. It now shows up to three. That also corrects a figure which has been wrong for some time — DeepSeek V4 Pro’s input price is $0.435, and we were printing $0.44. Promotions expire in both directions: Claude Sonnet 5’s introductory $2/$10 was due to rise on 1 September and has instead been made permanent. That is exactly why we date them rather than trust them. All 32 priced models were re-read at the provider’s own page for this release.
v2.7.1 · 2026-08-27 · GLM-5.3-Flash joins the board, one day after release. Z.ai shipped it on 26 August and it already has five results: Humanity’s Last Exam 39.9%, τ³-Banking 47.2%, GPQA Diamond 91.2%, and on LiveBench an overall of 71.6% with 56.8% on agentic coding. It enters as Provisional, not Ranked, and that is the honest result. Two of the five areas we score are still thin on evidence, and our rule allows one. We did not go looking for a sixth benchmark to push it over the line. A model a day old should look like a model a day old. One of its five scores is borrowed, and is labelled as such. GPQA Diamond normally comes from vals.ai, which has not tested this model — we checked its full 135-model board the same day rather than assuming. Where that happens we are permitted to fall back to Artificial Analysis, and the moment vals publishes its own number this borrowed one is retired. That happened to two other models earlier today. Priced at list, not at the number on the page. Z.ai is currently running a 50% launch discount that ends on 9 September. We record the standing price — $0.15 per million in, $0.50 out — because a promotion with an end date is not what the model costs. Its card shows no input or output types yet. Z.ai describes “native multimodal capabilities” in prose but publishes no list of what it actually accepts, and its sibling GLM-5.3 is text-only, so we would rather leave the field blank than infer one from an adjective. No other model moved.
v2.7.0 · 2026-08-27 · Qwen 3.8 27B is now officially ranked, at 12th. Vals.ai has tested it on MMMU-Pro (83.9%), which was the one area of the five we score where it had no evidence at all. That completes its coverage and moves it from Provisional to Ranked. Everything below it shifts down a place. Two borrowed scores handed back, and both went down. Where vals.ai has no result for a model, we are allowed to fall back to Artificial Analysis for GPQA Diamond — only until vals publishes its own. It now has, for two models, so the borrowed figures are retired: Qwen 3.8 27B falls 90.5% to 88.9% and GLM-5.3 falls 91.7% to 88.1%. Both models lose score. A fallback that only ever survived while it flattered would not be a fallback, so the check that runs this refuses outright if a replacement comes in higher than the borrowed figure without a human looking at it. And one re-test. Vals has re-run ChatGPT 5.6 Terra on Terminal-Bench 2.1: 73.4% to 77.5%, same harness. What we refused to add. Vals also publishes AIME results for three models we track. We did not take them. AIME currently counts for exactly one model out of thirty-six, and it is a test almost everyone scores above 90% on — so having a result on it lifts a model, and not having one costs nothing. Going from one model to four would widen that unfairness rather than fix it, and the board only covers three of our thirty-six, so covering everyone is not an option. That is the same fault we corrected at the top of the board last week, and we are not going to introduce a fresh one. AIME needs a source that reaches the whole roster, or it should stop counting until one exists. We also declined a Grok 4.5 multimodal result of 61.8%. It was set aside in August because it sits below Grok 4.3 and below the non-reasoning builds of the same model — a flagship cannot plausibly score below its own predecessor, so we cannot tell what was actually run. That decision stands. No price changed.
v2.6.1 · 2026-08-22 · GLM-5.3 now has its LiveBench results, and its score went down. LiveBench has added GLM-5.3, so it gains two results: 76.1% overall and 60.9% on agentic coding. Both are weaker than what it already had on this board — 95.4% on SWE-bench Verified, 91.7% on GPQA Diamond — so measuring it more made it score slightly lower, 74.25 to 73.77. It stays Provisional; it is still short of evidence in two of the five areas we score. And a correction we found while checking. Rather than copy the two numbers across, we re-read LiveBench’s full results file and checked every model we track against it. Twenty of our stored LiveBench figures turned out to be the number shown on their website, rounded to one decimal place, rather than the figure we are supposed to compute ourselves. That matters because LiveBench publishes only the individual task scores — the category and overall figures you see on their site are worked out in your browser and exist nowhere in their data, so we calculate them from the tasks. Twenty cells had skipped that step. All are now recomputed from the same file. How much it changed: almost nothing. Every correction is in the third decimal place of a percentage. No model changed rank and none changed tier. We fixed it anyway, because leaving GLM-5.3 computed properly while its neighbours sat on rounded website figures is the same inconsistency that caused the much larger problem we corrected earlier today. Three models keep their existing LiveBench figures: Muse Spark, GLM-5.1 and MiniMax M2.7 no longer appear on the board under any name, and a row disappearing is not a reason to change a measurement that was true when it was taken. No price changed.
v2.6.0 · 2026-08-22 · We were rewarding models for tests they had never taken. That is now fixed, and it reorders most of the board. What went wrong. One of the tests we score, τ³-Banking, is punishingly hard — every model that has taken it scores between 12% and 51%. Some models had taken it and some had not, and our Agency score averages over whichever tests a model has results for. So sitting the hard test dragged a model down, and never sitting it cost nothing. Being unmeasured was worth about three and a half points. The clearest symptom: ChatGPT 5.6 Sol beat ChatGPT 5.6 Terra on all nine tests they had both taken, and still ranked below it. Three other pairs had the same problem. Two things were wrong, not one. Ten models had no τ³ result recorded even though one was published — the numbers were in a file already on our own disk. And twelve of the results we did hold were reading the wrong line: they were picked by an old rule we replaced on 7 August and never went back to re-apply. Claude Opus 5 was being scored on its low reasoning setting, 30.3%, when its published maximum is 42.1%. What we would not do. Qwen 3.8 Max has a τ³ score of 51.3% published — one of the best on the board — and we did not take it. Artificial Analysis publishes it as a single unlabelled row, so there is no way to tell which configuration was tested, and we do not score a result we cannot identify. That decision costs Qwen 3.8 Max real points and leaves it the one model still holding an advantage from a missing result. Nemotron 3 Ultra is held for the same reason. The new order. ChatGPT 5.6 Sol rises from 4th to 2nd and now leads Terra 81.36 to 76.26, which is what beating it on every single test should look like

## 评论（3/3）

> **baraklaniado** · 2026-07-30T14:04:18.000Z　
> I run AGI Ranker, an AI benchmark aggregator that calculates an AGI score for every benchmarked frontier model, and have just released v2 earlier today.
> Auditing my own scale has led to a lower AGI score, 6-15pts less, yet the models kept their shape.
> Only one of the ten benchmarks has actually measured a human ceiling, GPQA-Diamond 81%, so the other 9 are anchored to benchmark-max, not to human-parity.
> Coverage has greatly improved, from ~43% to ~80%, and that means the score leans less on shrinkage and more on measurement.
> Single evaluator dependency has been successfully dropped from ~45% to ~26%, with the new offsets published on the site.
> Agency was rebuilt on 4 benchmarks from 3 independent evaluators.
> Speciality tabs now include Coding and Knowledge, with Reasoning temporarily dropped because it was leaning on only one benchmark, but will make a comeback once AIME 2026 is published.
> The Value tab shows cost-per-capability.
> The Corrections log makes sure that all my mistakes are openly reported on the site, including a recent apology to Deepseek, for having published an unsourced ARC-AGI-2 number.
> No lab money, no paid placements, every cell traceable, open data (CC-BY). It's a solo project that I maintained while having only 450 monthly visitors, determined to offer those who do visit, the most accurate and useful information about AI model prowess.
> Known limitations are listed on the site - happy to answer questions about the methodology or the functionality of the site. Cheers!

---

> **joeyagreco** · 2026-07-30T19:16:01.000Z　
> > ONE SCORE. INFINITE CLARITY.> Distance to AGI: 19.39 ptsI don't think I've ever had less clarity lol

---

> **polotics** · 2026-07-30T21:31:08.000Z　
> Ok. As you write AGI is == 100, can you clue us in as to what general intelligence is?

## 导航

- 项目页：[[10-项目/agiranker.com_d58f8809]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
